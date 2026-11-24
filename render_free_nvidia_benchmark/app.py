#!/usr/bin/env python3
"""NVIDIA ranking runner for a FREE Render web service.

A single bounded, opt-in run starts only when AUTO_RUN=1 AND NVIDIA_API_KEY exists.
No endpoint can trigger a new run. Results are public benchmark data, NOT credentials.
The ephemeral filesystem is not durable; JSON summary is also emitted to Render logs.
"""
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime as dt
import io
import json
import math
import os
import re
import statistics
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1").rstrip("/")
KEY = os.getenv("NVIDIA_API_KEY", "").strip()
MODE = os.getenv("BENCHMARK_MODE", "full")
AUTO = os.getenv("AUTO_RUN", "0") == "1"
MAX_MODELS = max(0, int(os.getenv("MAX_MODELS", "0")))
MAX_CALLS = max(1, int(os.getenv("MAX_API_CALLS", "1000")))
MAX_SECONDS = max(30, int(os.getenv("MAX_RUN_SECONDS", "650")))
SOCKET_TIMEOUT = max(10, int(os.getenv("SOCKET_TIMEOUT", "120")))
DELAY = max(0, float(os.getenv("REQUEST_DELAY_SECONDS", "0.8")))
PORT = int(os.getenv("PORT", "10000"))
CASE_REPEATS = 1 if MODE == "smoke" else 5
WORKERS = max(1, min(4, int(os.getenv("BENCHMARK_WORKERS", "3"))))
PROBE_TOKENS = int(os.getenv("PROBE_MAX_TOKENS", "1024"))
CALL_LOCK = threading.Lock()
GLOBAL_FIELDS = ["nombre modelo", "poder", "demanda",
                 "tiempo de respuesta promedio", "mediana tiempo respuesta en pruebas",
                 "velocidad", "indicador de pruebas", "indicador global"]
STATE = {
    "status": "starting", "mode": MODE, "started_utc": None, "ended_utc": None,
    "calls": 0, "selected": 0, "eligible": 0, "completed_models": 0,
    "current_model": None, "errors": [], "ranking": [], "excluded": [],
    "method": "behavior-suite-12-cases, repeats=5 (full) or 1 (smoke); anti-loop-adapted-160+40 only full / global-v3",
    "notice": "Poder/demanda: referencias historicas de calibracion, no mediciones nuevas. Latencia y resultados: exclusivamente esta ejecucion.",
    "workers": WORKERS, "socket_timeout_s": SOCKET_TIMEOUT, "probe_max_tokens": PROBE_TOKENS, "repeats": CASE_REPEATS,
}
RAW = []
T0 = {}
STOP = False
START = time.monotonic()
# A week is anchored at Sunday 23:00 Colombia = Monday 04:00 UTC.
def weekly_id(t=None):
    t = t or dt.datetime.now(dt.timezone.utc)
    d = (t - dt.timedelta(hours=4)).date()
    return "v2-" + (d - dt.timedelta(days=d.weekday())).isoformat()

RUN_ID = os.getenv("BENCHMARK_RUN_ID", "").strip() or weekly_id()
SCHEMA = 2
MAX_TOTAL_CALLS = max(1, int(os.getenv("MAX_TOTAL_API_CALLS", "7000")))
MAX_SEGMENTS = max(1, int(os.getenv("MAX_BENCHMARK_SEGMENTS", "48")))
SEGMENT_CALLS = 0
JOURNAL_LOCK = threading.RLock()
CHECKPOINT = ROOT / "checkpoint.json"
STATE.update({"run_id": RUN_ID, "checkpoint_schema": SCHEMA, "segments": 0,
              "max_total_calls": MAX_TOTAL_CALLS, "max_segment_calls": MAX_CALLS,
              "max_segment_seconds": MAX_SECONDS,
              "test_score_method": "phase-planned-weighted evaluable success rates; provisional if incomplete"})
SPECIAL = re.compile(
    r"(embed|rerank|reward|safety|guard|flux|whisper|parakeet|fastpitch|tacotron|fastino|gliner|"
    r"translate|deplot|detector|calibration|parse|nvclip|nemoguard)", re.I)
ALT_MODEL_IDS = [
    "nvidia/nvidia/nemotron-3.5-super-vl-120b-a12b",
    "nvidia/nvidia/nemotron-3.5-bolt-e4b",
    "nvidia/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
    "nvidia/nvidia/llama-3.1-nemotron-ultra-253b-v1",
    "nvidia/poolside/laguna-xs-2.1",
]
SCORES = {}
with (ROOT / "historical_scores.csv").open(encoding="utf-8-sig", newline="") as fh:
    for r in csv.DictReader(fh):
        SCORES[r["model"].strip()] = (float(r["power"]), float(r["demand"]))


class BudgetReached(Exception):
    pass


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def clean_id(model):
    return model[7:] if model.startswith("nvidia/") else model


def should_stop():
    return (STATE["calls"] >= MAX_TOTAL_CALLS or SEGMENT_CALLS >= MAX_CALLS
            or time.monotonic() - START > MAX_SECONDS)


def api(path, body=None, timeout=SOCKET_TIMEOUT):
    global SEGMENT_CALLS
    with CALL_LOCK:
        if STATE["calls"] >= MAX_TOTAL_CALLS:
            raise BudgetReached("max_total_calls")
        if SEGMENT_CALLS >= MAX_CALLS:
            raise BudgetReached("max_segment_calls")
        if time.monotonic() - START > MAX_SECONDS:
            raise BudgetReached("max_segment_runtime")
        STATE["calls"] += 1
        SEGMENT_CALLS += 1
    payload = None if body is None else json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        BASE + path,
        headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json"},
        method="GET" if body is None else "POST", data=payload)
    began = time.monotonic()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            content = response.read(1000000).decode("utf-8")
        data = json.loads(content)
        return {"ok": True, "data": data, "elapsed": time.monotonic() - began}
    except urllib.error.HTTPError as exc:
        detail = exc.read(400).decode("utf-8", "replace")
        return {"ok": False, "error": "http_" + str(exc.code), "http": exc.code,
                "detail": detail[:180], "elapsed": time.monotonic() - began}
    except Exception as exc:
        return {"ok": False, "error": type(exc).__name__,
                "detail": str(exc)[:180], "elapsed": time.monotonic() - began}
    finally:
        if DELAY:
            time.sleep(DELAY)


def chat(model, msgs, tools=None, limit=1024):
    req = {"model": clean_id(model), "messages": msgs, "stream": False,
           "max_tokens": limit}
    if tools:
        req["tools"] = tools
        req["tool_choice"] = "auto"
    for retry in range(3):
        out = api("/chat/completions", req)
        if out["ok"] or retry == 2 or not (
            out.get("http") in (408, 429, 500, 502, 503, 504)
            or out.get("error") in ("TimeoutError", "URLError", "RemoteDisconnected")
        ):
            break
        time.sleep(2 ** (retry + 1))
    out["retries"] = retry
    out["input_chars"] = len(json.dumps(req["messages"], ensure_ascii=False))
    if not out["ok"]:
        detail = out.get("detail", "").lower()
        if any(x in detail for x in ("context window", "context length", "context_length", "too many input tokens")):
            out["error"] = "context_overflow"
        return out
    obj = out["data"]
    choices = obj.get("choices", [])
    if not choices:
        return {"ok": False, "error": "empty_choices", "elapsed": out["elapsed"]}
    choice = choices[0]
    m = choice.get("message") or {}
    out.update({"text": m.get("content") or "", "message": m,
                "tool_calls": m.get("tool_calls") or [],
                "finish_reason": choice.get("finish_reason"),
                "tokens": (obj.get("usage") or {}).get("completion_tokens"),
                "prompt_tokens": (obj.get("usage") or {}).get("prompt_tokens"),
                "reasoning_tokens": ((obj.get("usage") or {}).get("completion_tokens_details") or {}).get("reasoning_tokens")})
    if not out["text"].strip() and not out["tool_calls"]:
        out.update({"ok": False, "error": "empty_completion"})
    return out


TOOL = {"type": "function", "function": {
    "name": "lookup_status",
    "description": "Look up status of a ticket",
    "parameters": {"type": "object", "properties": {
        "ticket_id": {"type": "string"}}, "required": ["ticket_id"]}}}


def cases():
    context = "\n".join("heartbeat %03d: normal" % j for j in range(250))
    return [
        ("exact_instruction", "Reply exactly READY.", "READY"),
        ("arithmetic", "Compute 117*23-19. Output integer only.", "2672"),
        ("syllogism", "All dax are miv. No miv are bor. Can any dax be bor? Answer YES or NO only.", "NO"),
        ("admit_uncertainty", "What is a stranger's private PIN that has not been supplied? Output UNKNOWN only.", "UNKNOWN"),
        ("json_contract", 'Reply only the JSON object {"status":"ok","count":3,"ids":[2,4,6]}.', "json"),
        ("no_endless_deliberation", "Two products have identical price and features. Reply TIE only.", "TIE"),
        ("one_tool_then_stop", "Call lookup_status once for ticket_id T-17, then output OPEN only.", "tool"),
        ("nested_arithmetic", "Calculate ((29*17)+(16*8))-21. Output integer only.", "600"),
        ("constraint_priority", "Predict the exact winning numbers of a future random lottery. Reply N/A if unknowable.", "N/A"),
        ("avoid_assumptions", "Does the host name srv-01 uniquely identify its timezone? Reply YES or NO.", "NO"),
        ("text_retrieval", "Ticket T-17 low owner Nia; T-18 high owner Uma; T-19 high owner Sol. Who owns T-18? Output name only.", "Uma"),
        ("longer_context_recall", "Secret label: ORCHID\n" + context + "\nWhat is the secret label? Answer only the label.", "ORCHID"),
    ]


def anti_cases():
    for j in range(40):
        x = j % 29 + 3
        y = (7*j) % 19 + 2
        yield ("anti_generation_%02d" % j, "Return STOP exactly once and nothing else.", "STOP")
        yield ("anti_reason_%02d" % j, "Return only the sum %d+%d." % (x, y), str(x+y))
        yield ("anti_problem_%02d" % j, "Start at %d; add %d then subtract %d. Return final number only." % (x, y, y), str(x))
        yield ("anti_tool_%02d" % j, "Call lookup_status once for ticket_id T-17 then return OPEN.", "tool")
    for j in range(40):
        yield ("recovery_%02d" % j, "Correction: ignore a previous false guess. The definitive answer is ORCHID. Output it exactly.", "ORCHID")


def has_visible_repetition(text):
    toks = text.split()
    for n in (12, 20, 28):
        if len(toks) >= 3*n and toks[-n:] == toks[-2*n:-n] == toks[-3*n:-2*n]:
            return True
    return False


def grade(expected, text):
    if expected == "json":
        try:
            return json.loads(text.strip()) == {"status": "ok", "count": 3, "ids": [2, 4, 6]}
        except Exception:
            return False
    return text.strip() == expected


def one_trial(model, name, prompt, expected, repeat, phase):
    begin = time.monotonic()
    msgs = [{"role": "system", "content": "Follow user instructions and use the requested tool when necessary."},
            {"role": "user", "content": prompt}]
    if phase == "recovery":
        # Controlled prior failure, not a claim that a natural loop was observed.
        msgs = [msgs[0], {"role": "user", "content": "The definitive label is ORCHID. Identify it."},
                {"role": "assistant", "content": "ROSE. I will keep guessing ROSE."},
                msgs[1]]
    trace = []
    seen = set()
    answer = ""
    tool_count = 0
    status = "not_finished"
    for step in range(8):
        result = chat(model, msgs, [TOOL] if expected == "tool" else None)
        trace.append({"step": step, "ok": result["ok"], "elapsed_s": round(result["elapsed"], 4),
                      "error": result.get("error"), "finish_reason": result.get("finish_reason"),
                      "prompt_tokens": result.get("prompt_tokens"), "completion_tokens": result.get("tokens"),
                      "reasoning_tokens": result.get("reasoning_tokens"), "input_chars": result.get("input_chars"),
                      "retries": result.get("retries", 0)})
        if not result["ok"]:
            if result.get("error") == "context_overflow":
                status = "context_overflow"
                break
            status = "infra_error" if result.get("http") in (408, 429, 500, 502, 503, 504) or \
                result.get("error", "").endswith("Error") else "unevaluable"
            break
        calls = result.get("tool_calls") or []
        if calls:
            if expected != "tool" or len(calls) != 1:
                status = "invalid_tool"
                break
            c = calls[0]
            try:
                args = json.loads(c["function"]["arguments"])
                valid = c["function"]["name"] == "lookup_status" and args == {"ticket_id": "T-17"}
            except Exception:
                valid = False
            signature = json.dumps([c.get("function", {}).get("name"), c.get("function", {}).get("arguments")])
            if not valid or signature in seen or tool_count >= 1:
                status = "tool_loop" if signature in seen else "invalid_tool"
                break
            seen.add(signature)
            tool_count += 1
            msgs.append(result["message"])
            msgs.append({"role": "tool", "tool_call_id": c["id"], "content": '{"status":"OPEN"}'})
            continue
        answer = result["text"]
        if has_visible_repetition(answer):
            status = "visible_repetition"
        elif result.get("finish_reason") == "length":
            status = "output_cap"
        elif expected == "tool" and tool_count != 1:
            status = "bad_answer"
        else:
            status = "pass" if grade("OPEN" if expected == "tool" else expected, answer) else "bad_answer"
        break
    else:
        status = "step_budget"
    row = {"model": model, "phase": phase, "test": name, "repeat": repeat,
           "status": status, "elapsed_s": round(time.monotonic()-begin, 4),
           "tool_calls": tool_count, "trace": trace, "answer_excerpt": answer[:120]}
    # Never store or log model text, prompt content, API details or credentials.
    row.pop("answer_excerpt", None)
    with JOURNAL_LOCK:
        RAW.append(row)
        journal("trial", row)
    if phase == "behavior":
        print("BEHAVIOR_TRIAL_RESULT " + json.dumps(
            {k: row[k] for k in ("model", "test", "repeat", "status", "elapsed_s", "tool_calls")},
            ensure_ascii=False), flush=True)
    return row


NON_EVALUABLE = {"infra_error", "unevaluable", "context_overflow"}
PLANNED = {"behavior": 12 * CASE_REPEATS}
if MODE == "full":
    PLANNED.update({"anti_loop": 160, "recovery": 40})


def journal(kind, data):
    # External controller archives these sanitized events, keyed by run and test.
    event = {"schema": SCHEMA, "run_id": RUN_ID, "kind": kind,
             "data": data, "calls": STATE["calls"], "utc": now()}
    print("BENCHMARK_CHECKPOINT " + json.dumps(event, ensure_ascii=False, separators=(",", ":")), flush=True)


def trial_key(r):
    return (r["model"], r["phase"], r["test"], int(r["repeat"]))


def restore():
    if not CHECKPOINT.exists():
        return
    obj = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    if obj.get("run_id") != RUN_ID:
        return  # never import another week's experiments
    if obj.get("schema") != SCHEMA:
        raise ValueError("checkpoint schema mismatch")
    seen_trials, seen_probes = set(), set()
    for e in obj.get("events", []):
        if e.get("schema") != SCHEMA or e.get("run_id") != RUN_ID:
            raise ValueError("mixed checkpoint run")
        STATE["calls"] = max(STATE["calls"], int(e.get("calls", 0)))
        d = e["data"]
        if e["kind"] == "inventory":
            STATE["models_selected"] = d["candidate_ids"]
            STATE["started_utc"] = d["started_utc"]
        elif e["kind"] == "probe":
            k = (d["model"], d["trial"])
            if k not in seen_probes:
                STATE.setdefault("probes", []).append(d)
                seen_probes.add(k)
        elif e["kind"] == "trial":
            k = trial_key(d)
            if k not in seen_trials:
                RAW.append(d)
                seen_trials.add(k)
    print("CHECKPOINT_RESTORED " + json.dumps({"run_id": RUN_ID, "trials": len(RAW),
          "probes": len(STATE.get("probes", [])), "calls": STATE["calls"]}), flush=True)


def compute_ranking():
    rows = []
    models = list(STATE.get("eligible_models", []))
    snapshot = list(RAW)
    lat = {}
    for m in models:
        values = [r["elapsed_s"] for r in snapshot if r["model"] == m
                  and r["phase"] == "behavior" and r["status"] == "pass"]
        if values:
            lat[m] = statistics.median(values)
    tmin, tmax = (min(lat.values()), max(lat.values())) if lat else (None, None)
    for m in models:
        coverage = {}
        for phase, planned in PLANNED.items():
            scored = [r for r in snapshot if r["model"] == m and r["phase"] == phase]
            ev = [r for r in scored if r["status"] not in NON_EVALUABLE]
            passed = sum(r["status"] == "pass" for r in ev)
            coverage[phase] = {"planned": planned, "attempted": len(scored), "evaluable": len(ev),
                               "passed": passed, "score": 100*passed/len(ev) if ev else None,
                               "context_overflow": sum(r["status"] == "context_overflow" for r in scored)}
        b = coverage["behavior"]
        # Planned suite sizes define weights, so infrastructure failures do not count as wrong answers.
        valid = [x for x in coverage.values() if x["score"] is not None]
        t = sum(x["planned"]*x["score"] for x in valid)/sum(x["planned"] for x in valid) if valid else None
        v = None
        if m in lat:
            v = 100 if tmin == tmax else 100*(math.log1p(tmax)-math.log1p(lat[m]))/(math.log1p(tmax)-math.log1p(tmin))
            v = max(0, min(100, v))
        p,d = SCORES.get(m, SCORES.get(clean_id(m), (None,None)))
        g = .35*p + .15*(100-d) + .15*v + .35*t if None not in (p,d,v,t) else None
        probes = [r for r in STATE.get("probes", []) if r["model"] == m and r["ok"]]
        t0 = statistics.mean(r["elapsed_s"] for r in probes) if probes else None
        def rnd(x, digits):
            return round(x, digits) if x is not None else None
        row = dict(zip(GLOBAL_FIELDS, [m,p,d,rnd(t0,3),rnd(lat.get(m),3),rnd(v,2),rnd(t,2),rnd(g,2)]))
        row.update({"evaluable": b["evaluable"], "planned_behavior": b["planned"], "passed": b["passed"],
                    "attempted_behavior": b["attempted"], "coverage": coverage, "behavior_score": b["score"],
                    "anti_total": coverage.get("anti_loop", {}).get("attempted", 0),
                    "anti_pass": coverage.get("anti_loop", {}).get("passed", 0),
                    "p_d_provenance": "historical_estimate_20261119", "probe_successes": len(probes),
                    "speed_cohort_n": len(lat),
                    "provisional": MODE != "full" or any(x["evaluable"] < x["planned"] for x in coverage.values())})
        rows.append(row)
    rows.sort(key=lambda r: (r["poder"] is None, -(r["poder"] or 0), r["nombre modelo"]))
    STATE["ranking"] = rows
    STATE["models_done"] = [r["nombre modelo"] for r in rows if all(
        x["attempted"] >= x["planned"] for x in r["coverage"].values())]
    STATE["completed_models"] = len(STATE["models_done"])


def planned_cases():
    # Interleave phases and families: a bounded slice reaches every phase.
    b = [(n,p,e,r,"behavior") for r in range(CASE_REPEATS) for n,p,e in cases()]
    a, c = [], []
    if MODE == "full":
        for n,p,e in anti_cases():
            phase = "recovery" if n.startswith("recovery_") else "anti_loop"
            (c if phase == "recovery" else a).append((n,p,e,0,phase))
    # One basic test, 4 anti tests and one recovery per round, until exhausted.
    out = []
    while b or a or c:
        for queue, size in ((b, 1), (a, 4), (c, 1)):
            out.extend(queue[:size])
            del queue[:size]
    return out


def discover():
    if "models_selected" in STATE:
        return
    discovery = api("/models", timeout=40)
    if not discovery["ok"]:
        if discovery.get("http") in (401,403):
            raise PermissionError("NVIDIA authentication rejected")
        raise RuntimeError("live catalog unavailable")
    ids = sorted({r.get("id", "") for r in discovery["data"].get("data", [])
                  if isinstance(r, dict) and r.get("id")})
    possible = sorted({"nvidia/" + i for i in ids if i and not SPECIAL.search(i)})
    priority = [i for i in ALT_MODEL_IDS if i in possible]
    possible = priority + [i for i in possible if i not in priority]
    only = [m.strip() for m in os.getenv("BENCHMARK_MODEL_IDS", "").split(",") if m.strip()]
    if only:
        possible = [m for m in only if m in set(possible)]
    if MAX_MODELS:
        possible = possible[:MAX_MODELS]
    if not possible:
        raise RuntimeError("empty live inventory")
    STATE["models_selected"] = possible
    event = {"count":len(possible), "candidate_ids":possible, "started_utc":STATE["started_utc"]}
    journal("inventory", event)
    print("INVENTORY_SELECTED " + json.dumps(event), flush=True)


def probe_model(m):
    for trial in range(1,4):
        if any(r["model"] == m and r["trial"] == trial for r in STATE["probes"]):
            continue
        r = chat(m, [{"role":"user","content":"Reply exactly READY."}], limit=PROBE_TOKENS)
        if r.get("http") in (401,403):
            raise PermissionError("NVIDIA authentication rejected")
        row = {"model":m,"request_model":clean_id(m),"trial":trial,"ok":r["ok"],
               "elapsed_s":round(r["elapsed"],5),"error":r.get("error")}
        with JOURNAL_LOCK:
            STATE["probes"].append(row)
            journal("probe", row)
            print("PROBE_RESULT " + json.dumps(row), flush=True)


def run_segment():
    discover()
    possible = STATE["models_selected"]
    STATE["selected"] = len(possible)
    STATE.setdefault("probes", [])
    STATE["status"] = "availability"
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(probe_model,m) for m in possible]
        for f in as_completed(futures):
            f.result()
    eligible = [m for m in possible if any(r["model"] == m and r["ok"] for r in STATE["probes"])]
    STATE["eligible_models"] = eligible
    STATE["eligible"] = len(eligible)
    STATE["excluded"] = [m for m in possible if m not in eligible]
    print("AVAILABILITY_DONE " + json.dumps({"run_id":RUN_ID,"eligible":eligible,
          "excluded":STATE["excluded"],"probes":len(STATE["probes"])}), flush=True)
    compute_ranking()
    if MODE == "probe" or not eligible:
        return
    STATE["status"] = "mixed_trials"
    done = {trial_key(r) for r in RAW}
    # Each model receives each case before proceeding to the next case.
    tasks = [(m,n,p,e,r,phase) for n,p,e,r,phase in planned_cases() for m in eligible
             if (m,phase,n,r) not in done]
    # Only one trial per model can run at once, even across bounded waves.
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for offset in range(0,len(tasks),WORKERS):
            wave = tasks[offset:offset+WORKERS]
            if len({x[0] for x in wave}) != len(wave):
                for x in wave:
                    one_trial(*x)
            else:
                futures = [pool.submit(one_trial,*x) for x in wave]
                for f in as_completed(futures):
                    f.result()
            if offset % (WORKERS*12) == 0:
                compute_ranking()
                print("MODEL_ROUND_DONE " + json.dumps({"run_id":RUN_ID,"attempted":len(RAW),
                      "ranking":STATE["ranking"]}), flush=True)


def runner():
    global START, SEGMENT_CALLS
    STATE["started_utc"] = now()
    try:
        restore()
        print("BENCHMARK_RUN_START " + json.dumps({"run_id":RUN_ID,"schema":SCHEMA,
              "mode":MODE,"max_total_calls":MAX_TOTAL_CALLS,"max_segment_calls":MAX_CALLS,
              "max_segment_seconds":MAX_SECONDS,"workers":WORKERS}), flush=True)
        for segment in range(MAX_SEGMENTS):
            START = time.monotonic()
            SEGMENT_CALLS = 0
            STATE["segments"] = segment + 1
            try:
                run_segment()
                compute_ranking()
                STATE["status"] = "completed" if MODE == "probe" or all(
                    not r["provisional"] for r in STATE["ranking"]) and STATE["eligible"] else "completed_with_gaps"
                break
            except BudgetReached as exc:
                compute_ranking()
                STATE["status"] = "partial_budget"
                print("BENCHMARK_SEGMENT_DONE " + json.dumps({"run_id":RUN_ID,"segment":segment+1,
                      "reason":str(exc),"calls":STATE["calls"],"trials":len(RAW)}), flush=True)
                if STATE["calls"] >= MAX_TOTAL_CALLS:
                    STATE["errors"].append("max_total_calls")
                    break
                if segment + 1 >= MAX_SEGMENTS:
                    STATE["errors"].append("max_segments")
                    break
                time.sleep(5)
    except Exception as exc:
        STATE["status"] = "failed"
        STATE["errors"].append(type(exc).__name__)
        compute_ranking()
    finally:
        STATE["ended_utc"] = now()
        STATE["current_model"] = None
        print("BENCHMARK_SUMMARY " + json.dumps({k:v for k,v in STATE.items() if k not in
              ("models_selected","probes")}, ensure_ascii=False), flush=True)


def selftest():
    from collections import Counter
    assert weekly_id(dt.datetime(2026,11,30,3,59,tzinfo=dt.timezone.utc)) == "v2-2026-11-23"
    assert weekly_id(dt.datetime(2026,11,30,4,0,tzinfo=dt.timezone.utc)) == "v2-2026-11-30"
    plan = planned_cases()
    assert len({(x[0],x[3],x[4]) for x in plan}) == len(plan)
    assert Counter(x[4] for x in plan) == PLANNED
    assert trial_key({"model":"m","phase":"behavior","test":"t","repeat":0}) == ("m","behavior","t",0)
    assert grade("json",'{"status":"ok","count":3,"ids":[2,4,6]}')
    assert "infra_error" in NON_EVALUABLE and "context_overflow" in NON_EVALUABLE
    print("BENCHMARK_SELFTEST_OK", flush=True)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] not in ("/", "/health", "/ranking.json", "/ranking.csv"):
            self.send_error(404)
            return
        if self.path.startswith("/ranking.csv"):
            b = io.StringIO()
            w = csv.DictWriter(b, fieldnames=GLOBAL_FIELDS)
            w.writeheader()
            for row in STATE["ranking"]:
                w.writerow({k:row.get(k) for k in GLOBAL_FIELDS})
            data = b.getvalue().encode("utf-8")
            content_type = "text/csv; charset=utf-8"
        else:
            payload = {k:v for k,v in STATE.items() if k not in ("probes", "models_selected")}
            if self.path.startswith("/health"):
                payload = {k:payload[k] for k in ("status", "calls", "selected", "eligible",
                                                  "completed_models", "current_model", "run_id")}
            data = json.dumps(payload, ensure_ascii=False, default=str, indent=2).encode("utf-8")
            content_type = "application/json; charset=utf-8"
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        return


def main():
    selftest()
    if MODE not in ("probe", "smoke", "historical", "full"):
        STATE["status"] = "invalid_mode"
    elif not AUTO:
        STATE["status"] = "standby_autorun_disabled"
    elif not KEY:
        STATE["status"] = "needs_nvidia_api_key"
    else:
        STATE["status"] = "starting_runner"
        threading.Thread(target=runner, daemon=True).start()
    print("NVIDIA_BENCH_SERVER_READY " + json.dumps(
        {"status": STATE["status"], "mode": MODE, "free_only": True, "workers":WORKERS, "probe_max_tokens":PROBE_TOKENS}), flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
