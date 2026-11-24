#!/usr/bin/env python3
"""NVIDIA ranking runner for a FREE Render web service.

A single bounded, opt-in run starts only when AUTO_RUN=1 AND NVIDIA_API_KEY exists.
No endpoint can trigger a new run. Results are public benchmark data, NOT credentials.
The ephemeral filesystem is not durable; JSON summary is also emitted to Render logs.
"""
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
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
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1").rstrip("/")
KEY = os.getenv("NVIDIA_API_KEY", "").strip()
MODE = os.getenv("BENCHMARK_MODE", "full")
AUTO = os.getenv("AUTO_RUN", "0") == "1"
MAX_MODELS = max(0, int(os.getenv("MAX_MODELS", "0")))
MAX_CALLS = max(1, int(os.getenv("MAX_API_CALLS", "1000")))
MAX_SECONDS = min(720, max(30, int(os.getenv("MAX_RUN_SECONDS", "720"))))
# Stay inside the free service idle window, with a drain reserve for requests.
LAST_HEALTH = None
BATCH_SECONDS = min(540, MAX_SECONDS)
BOOT_MONO = time.monotonic()
LAST_MANIFEST_API = -1e20
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
PROCESS_ID = uuid.uuid4().hex
CALL_BASE = 0
REMOTE_ROOT = "https://raw.githubusercontent.com/Trochez/ai-agent-model-rankings/render-free-nvidia-benchmark-20261123/render_free_nvidia_benchmark/"
MAX_TOTAL_CALLS = max(1, int(os.getenv("MAX_TOTAL_API_CALLS", "7000")))
MAX_SEGMENTS = min(168, max(1, int(os.getenv("MAX_WEEKLY_BATCHES", "168"))))
BATCH = 0
BATCH_CEILING = 0
AUTH_FAILED = threading.Event()
SEGMENT_CALLS = 0
JOURNAL_LOCK = threading.RLock()
CHECKPOINT = ROOT / "checkpoint.json"
STATE.update({"run_id": RUN_ID, "checkpoint_schema": SCHEMA, "segments": 0,
              "max_total_calls": MAX_TOTAL_CALLS, "max_segment_calls": MAX_CALLS,
              "process_id": PROCESS_ID, "call_base": 0, "checkpoint_source": None,
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
            or time.monotonic() - START >= BATCH_SECONDS)


def api(path, body=None, timeout=SOCKET_TIMEOUT):
    global SEGMENT_CALLS
    with CALL_LOCK:
        if AUTH_FAILED.is_set():
            raise PermissionError("NVIDIA authentication rejected")
        if weekly_id() != RUN_ID[:13]:
            raise BudgetReached("week_boundary")
        if STATE["calls"] >= MAX_TOTAL_CALLS:
            raise BudgetReached("max_total_calls")
        if BATCH_CEILING and STATE["calls"] >= BATCH_CEILING:
            raise BudgetReached("batch_call_ceiling")
        if SEGMENT_CALLS >= MAX_CALLS:
            raise BudgetReached("max_segment_calls")
        if time.monotonic() - START >= BATCH_SECONDS:
            raise BudgetReached("max_segment_runtime")
        STATE["calls"] += 1
        SEGMENT_CALLS += 1
        # Count reservations before network I/O; conservative even on abrupt termination.
        print("BENCHMARK_API_RESERVED " + json.dumps({"run_id":RUN_ID,"process_id":PROCESS_ID,
            "batch":BATCH,"calls":STATE["calls"],"call_base":CALL_BASE,
            "process_calls":STATE["calls"]-CALL_BASE}),flush=True)
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
        if exc.code in (401,403):
            AUTH_FAILED.set()
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
        if out.get("http") in (401,403):
            raise PermissionError("NVIDIA authentication rejected")
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
    if not out["text"].strip() and not out["tool_calls"] and out.get("finish_reason") != "length":
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
    if phase == "anti_loop" and name.startswith("anti_problem_"):
        # Long-context challenge, distinct from effective context-window measurement.
        j = int(name.rsplit("_",1)[1])
        count = (0, 64, 256, 1024)[j % 4]
        if count:
            msgs[1]["content"] = ("Ignore these unrelated heartbeat records.\n" +
                "\n".join("heartbeat %04d: nominal" % k for k in range(count)) +
                "\n" + prompt)
    if phase == "recovery":
        # Four controlled failure histories; not a claim of naturally observed loops.
        j = int(name.rsplit("_",1)[1])
        failures = ["ROSE. I will keep guessing ROSE.", "ROSE ROSE ROSE ROSE ROSE.",
            "I need to reconsider the same question again before answering.",
            "I cannot proceed until I repeat my previous incorrect answer ROSE."]
        msgs = [msgs[0], {"role":"user","content":"The definitive label is ORCHID. Identify it."},
                {"role":"assistant","content":failures[j%4]},
                {"role":"user","content":"Your prior response was wrong. Stop repeating it."},
                {"role":"assistant","content":failures[j%4]}, msgs[1]]
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
    calls = STATE["calls"]
    event = {"schema": SCHEMA, "run_id": RUN_ID, "kind": kind,
             "data": data, "calls": calls, "utc": now(),
             "process_id": PROCESS_ID, "call_base": CALL_BASE,
             "process_calls": calls - CALL_BASE}
    print("BENCHMARK_CHECKPOINT " + json.dumps(event, ensure_ascii=False, separators=(",", ":")), flush=True)


def trial_key(r):
    return (r["model"], r["phase"], r["test"], int(r["repeat"]))


def remote_json(path):
    # Public benchmark metrics only. Never transmit the NVIDIA API key to GitHub.
    # A cache-busting query and no-cache request avoid stale branch manifests.
    url = REMOTE_ROOT + path + "?checkpoint_read=" + uuid.uuid4().hex
    req = urllib.request.Request(url, headers={"Accept":"application/json",
        "Cache-Control":"no-cache", "User-Agent":"nvidia-benchmark-checkpoint-v2"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                data = response.read(4_000_001)
            if len(data) > 4_000_000:
                raise ValueError("checkpoint exceeds size limit")
            obj = json.loads(data)
            if not isinstance(obj, dict):
                raise ValueError("checkpoint not an object")
            return obj
        except (urllib.error.URLError, TimeoutError, OSError):
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)


def live_manifest():
    # Raw branch URLs may briefly be stale. Check the public Contents API at
    # most once per 75 seconds per process; never send NVIDIA credentials.
    global LAST_MANIFEST_API
    t = time.monotonic()
    if t - LAST_MANIFEST_API >= 75:
        LAST_MANIFEST_API = t
        url = ("https://api.github.com/repos/Trochez/ai-agent-model-rankings/contents/"
               "render_free_nvidia_benchmark/checkpoint.json"
               "?ref=render-free-nvidia-benchmark-20261123")
        req = urllib.request.Request(url,headers={"Accept":"application/vnd.github.raw+json",
            "Cache-Control":"no-cache","User-Agent":"nvidia-benchmark-checkpoint-v2"})
        try:
            with urllib.request.urlopen(req,timeout=10) as response:
                raw = response.read(4_000_001)
            if len(raw)>4_000_000:
                raise ValueError("manifest exceeds size limit")
            obj=json.loads(raw)
            if isinstance(obj,dict) and obj.get("schema")==SCHEMA and isinstance(obj.get("run_id"),str):
                return obj
        except (urllib.error.URLError, TimeoutError, OSError, ValueError):
            pass
    return remote_json("checkpoint.json")


def batch_window(t, health, boot, maximum, socket_timeout):
    # Only genuine incoming status traffic can justify the longer window.
    # Without it, keep the previous 9-minute ceiling and account for boot age.
    # Stop reserving new calls early enough to drain the last request.
    drain = max(60, socket_timeout + 15)
    if health is None or health < boot:
        return max(0, min(540, maximum, 780 - (t - boot) - drain))
    return max(0, min(maximum, 810 - (t - health) - drain))


def checkpoint_events(obj, load_part):
    if obj.get("schema") != SCHEMA:
        raise ValueError("checkpoint schema mismatch")
    if obj.get("run_id") != RUN_ID:
        return []
    events = list(obj.get("events", []))
    parts = obj.get("parts", [])
    if not isinstance(parts, list) or len(parts) > 1000 or len(set(parts)) != len(parts):
        raise ValueError("invalid checkpoint part list")
    for part in parts:
        if not re.fullmatch(r"checkpoint_events/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+\.json", part):
            raise ValueError("invalid checkpoint part")
        if part.split("/")[1] != RUN_ID:
            raise ValueError("checkpoint part from different run")
        batch = load_part(part)
        if batch.get("run_id") != RUN_ID or batch.get("schema") != SCHEMA:
            raise ValueError("checkpoint part run mismatch")
        rows = batch.get("events")
        if not isinstance(rows,list) or len(rows) > 100:
            raise ValueError("invalid checkpoint part events")
        events.extend(rows)
    for e in events:
        if e.get("schema") != SCHEMA or e.get("run_id") != RUN_ID or e.get("kind") not in ("inventory","probe","trial"):
            raise ValueError("invalid checkpoint event")
        if not isinstance(e.get("data"),dict) or int(e.get("calls",0)) < 0:
            raise ValueError("invalid checkpoint payload")
    return events


def restore(quiet=False, remote=False, reader=None):
    # The deployed checkout is immutable. On real startup load the live manifest
    # and all referenced immutable shards, then apply atomically in memory.
    # If the remote read fails, fail closed rather than replay thousands of calls.
    local = json.loads(CHECKPOINT.read_text(encoding="utf-8")) if CHECKPOINT.exists() else None
    if remote:
        reader = reader or remote_json
        obj = reader("checkpoint.json")
        if not isinstance(obj,dict) or obj.get("schema") != SCHEMA or not isinstance(obj.get("run_id"),str):
            raise ValueError("invalid remote manifest")
        if obj.get("run_id") != RUN_ID and local and local.get("run_id") == RUN_ID:
            raise ValueError("remote manifest older than deployed checkpoint")
        if obj.get("run_id") == RUN_ID and local and local.get("run_id") == RUN_ID:
            if int(obj.get("calls",0)) < int(local.get("calls",0)) or not set(local.get("parts",[])).issubset(obj.get("parts",[])):
                raise ValueError("remote manifest regressed")
        load = reader
        source = "github_live"
    else:
        if local is None:
            return
        obj = local
        load = lambda path: json.loads((ROOT / path).read_text(encoding="utf-8"))
        source = "local"
    STATE["checkpoint_source"] = source
    if obj.get("run_id") != RUN_ID:
        if remote:
            # Only an older valid weekly manifest authorizes a fresh run.
            if not re.fullmatch(r"v2-\d{4}-\d{2}-\d{2}",obj["run_id"]) or obj["run_id"] >= RUN_ID:
                raise ValueError("unexpected remote run_id")
            if not quiet:
                print("CHECKPOINT_NEW_WEEK " + json.dumps({"run_id":RUN_ID,"previous_run_id":obj["run_id"],"source":source}),flush=True)
        return
    events = checkpoint_events(obj,load)
    seen_trials, seen_probes = set(), set()
    inventory = None
    probes, trials = [], []
    calls = int(obj.get("calls",0))
    for e in events:
        calls = max(calls,int(e.get("calls",0)))
        d = e["data"]
        if e["kind"] == "inventory":
            if inventory is None:
                inventory = d
            elif inventory["candidate_ids"] != d["candidate_ids"]:
                raise ValueError("conflicting run inventory")
        elif e["kind"] == "probe":
            k = (d["model"],d["trial"])
            if k not in seen_probes:
                probes.append(d)
                seen_probes.add(k)
        elif e["kind"] == "trial":
            k = trial_key(d)
            if k not in seen_trials:
                trials.append(d)
                seen_trials.add(k)
    if remote and (probes or trials) and inventory is None:
        raise ValueError("missing run inventory")
    if inventory is not None:
        STATE["models_selected"] = inventory["candidate_ids"]
        STATE["started_utc"] = inventory["started_utc"]
    STATE["probes"] = probes
    RAW[:] = trials
    STATE["calls"] = max(STATE["calls"],calls)
    STATE["archive_cursor_utc"] = obj.get("cursor_utc")
    STATE["checkpoint_terminal"] = bool(obj.get("terminal_notified")) or obj.get("terminal_status") in ("completed","completed_with_gaps","partial_budget","failed")
    if not quiet:
        print("CHECKPOINT_RESTORED " + json.dumps({"run_id":RUN_ID,"trials":len(RAW),
            "probes":len(probes),"calls":STATE["calls"],"source":source,
            "cursor_utc":obj.get("cursor_utc"),"process_id":PROCESS_ID,
            "terminal":STATE["checkpoint_terminal"]}),flush=True)


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
    # Cover all phases early, then preserve the planned counts.
    out = []
    while b or a or c:
        for queue, size in ((b, 1), (c, 1), (a, 4)):
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
    pending = {m:[(m,n,p,e,r,phase) for n,p,e,r,phase in planned_cases()
                  if (m,phase,n,r) not in done] for m in eligible}
    progress = {m:sum(r["model"]==m for r in RAW) for m in eligible}
    # Work-conserving scheduling: one active trial per model, three workers,
    # no barrier waiting on a slow model before another worker can proceed.
    active = {}
    busy = set()
    error = None
    completed_here = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        while True:
            if error is None and not should_stop():
                ready = sorted((m for m in eligible if pending[m] and m not in busy),
                               key=lambda m:(progress[m],eligible.index(m)))
                for m in ready[:max(0,WORKERS-len(active))]:
                    job = pool.submit(one_trial,*pending[m].pop(0))
                    active[job] = m
                    busy.add(m)
            if not active:
                break
            finished,_ = wait(list(active),return_when=FIRST_COMPLETED)
            for job in finished:
                m = active.pop(job)
                busy.remove(m)
                try:
                    job.result()
                    progress[m] += 1
                    completed_here += 1
                except Exception as exc:
                    if error is None or isinstance(exc,PermissionError):
                        error = exc
            if completed_here and completed_here % 12 == 0:
                compute_ranking()
                print("MODEL_ROUND_DONE " + json.dumps({"run_id":RUN_ID,"attempted":len(RAW),
                      "ranking":STATE["ranking"]}),flush=True)
    if error:
        raise error
    if any(pending.values()):
        if STATE["calls"] >= MAX_TOTAL_CALLS:
            raise BudgetReached("max_total_calls")
        raise BudgetReached("max_segment_runtime" if time.monotonic()-START>=BATCH_SECONDS else "max_segment_calls")


def announce_summary():
    STATE["ended_utc"] = now()
    STATE["process_calls"] = max(0,STATE["calls"]-CALL_BASE)
    STATE["current_model"] = None
    print("BENCHMARK_SUMMARY " + json.dumps({k:v for k,v in STATE.items() if k not in
          ("models_selected","probes")},ensure_ascii=False),flush=True)


def valid_active_manifest(obj, week):
    rid = obj.get("run_id","")
    return (obj.get("schema")==SCHEMA and obj.get("week_id",rid[:13])==week
            and re.fullmatch(re.escape(week)+r"(?:-r[0-9]+)?",rid) is not None)


def batch_authorized(obj, process, last_batch):
    return (obj.get("authorized_process_id")==process
            and type(obj.get("authorized_batch")) is int
            and obj["authorized_batch"]>last_batch
            and type(obj.get("calls_ceiling")) is int
            and 0<=int(obj.get("calls",0))<=obj["calls_ceiling"]<=MAX_TOTAL_CALLS)


def runner():
    global START, SEGMENT_CALLS, CALL_BASE, RUN_ID, BATCH, BATCH_CEILING, BATCH_SECONDS
    STATE["started_utc"] = now()
    last_batch = 0
    announced = None
    locked_run = None
    try:
        while True:
            week = weekly_id()
            if locked_run and locked_run[:13]!=week:
                STATE["status"]="week_ended"
                return
            STATE["status"]="awaiting_authorization"
            obj = live_manifest()
            if not valid_active_manifest(obj,week):
                STATE["status"]="standby_week_not_authorized"
                time.sleep(30)
                continue
            if locked_run and obj["run_id"]!=locked_run:
                STATE["status"]="superseded"
                return
            RUN_ID=obj["run_id"]
            STATE["run_id"]=RUN_ID
            if announced!=RUN_ID:
                print("BENCHMARK_BOOT_WAIT " + json.dumps({"run_id":RUN_ID,"week_id":week,
                      "process_id":PROCESS_ID,"utc":now()}),flush=True)
                announced=RUN_ID
            if obj.get("terminal_notified") or obj.get("terminal_status") in ("completed","completed_with_gaps","partial_budget","failed"):
                restore(remote=True,reader=lambda p:obj if p=="checkpoint.json" else remote_json(p))
                possible=STATE.get("models_selected",[])
                STATE["selected"]=len(possible)
                STATE["eligible_models"]=[m for m in possible if any(r["model"]==m and r["ok"] for r in STATE.get("probes",[]))]
                STATE["eligible"]=len(STATE["eligible_models"])
                STATE["excluded"]=[m for m in possible if m not in STATE["eligible_models"]]
                compute_ranking()
                STATE["status"]="archived_terminal"
                return
            if not batch_authorized(obj,PROCESS_ID,last_batch):
                time.sleep(20)
                continue
            locked_run=RUN_ID
            previous_calls=STATE["calls"]
            previous_keys={trial_key(r) for r in RAW}
            previous_probes={(r["model"],r["trial"]) for r in STATE.get("probes",[])}
            if int(obj.get("calls",0))<previous_calls:
                raise ValueError("archive missing previous batch calls")
            STATE["status"]="restoring_checkpoint"
            restore(remote=True,reader=lambda p:obj if p=="checkpoint.json" else remote_json(p))
            if not previous_keys.issubset({trial_key(r) for r in RAW}) or not previous_probes.issubset({(r["model"],r["trial"]) for r in STATE.get("probes",[])}):
                raise ValueError("archive missing previous batch events")
            if last_batch==0:
                CALL_BASE=STATE["calls"]
            STATE["call_base"]=CALL_BASE
            BATCH=obj["authorized_batch"]
            BATCH_CEILING=obj["calls_ceiling"]
            last_batch=BATCH
            STATE["segments"]=BATCH
            STATE["batch"]=BATCH
            if BATCH>MAX_SEGMENTS or STATE["calls"]>=MAX_TOTAL_CALLS:
                STATE["status"]="partial_budget"
                STATE["errors"].append("max_segments" if BATCH>MAX_SEGMENTS else "max_total_calls")
                announce_summary()
                return
            START=time.monotonic()
            BATCH_SECONDS=batch_window(START,LAST_HEALTH,BOOT_MONO,MAX_SECONDS,SOCKET_TIMEOUT)
            STATE["batch_window_s"]=round(BATCH_SECONDS,1)
            SEGMENT_CALLS=0
            print("BENCHMARK_RUN_START " + json.dumps({"run_id":RUN_ID,"schema":SCHEMA,"batch":BATCH,
                "process_id":PROCESS_ID,"call_base":CALL_BASE,"mode":MODE,"max_total_calls":MAX_TOTAL_CALLS,
                "max_segment_calls":MAX_CALLS,"max_segment_seconds":round(BATCH_SECONDS,1),"workers":WORKERS}),flush=True)
            try:
                if BATCH_SECONDS < 30:
                    raise BudgetReached("idle_window_exhausted")
                run_segment()
                compute_ranking()
                STATE["status"]="completed" if (MODE=="probe" or (STATE["eligible"] and all(
                    not r["provisional"] for r in STATE["ranking"]))) else "completed_with_gaps"
                announce_summary()
                return
            except BudgetReached as exc:
                compute_ranking()
                reason=str(exc)
                if reason=="max_total_calls" or STATE["calls"]>=MAX_TOTAL_CALLS or BATCH>=MAX_SEGMENTS:
                    STATE["status"]="partial_budget"
                    STATE["errors"].append("max_total_calls" if STATE["calls"]>=MAX_TOTAL_CALLS else "max_segments")
                    announce_summary()
                    return
                if reason=="week_boundary":
                    STATE["status"]="week_ended"
                    announce_summary()
                    return
                STATE["status"]="awaiting_checkpoint"
                print("BENCHMARK_BATCH_DONE " + json.dumps({"run_id":RUN_ID,"batch":BATCH,"reason":reason,
                    "calls":STATE["calls"],"trials":len(RAW),"process_id":PROCESS_ID,
                    "call_base":CALL_BASE,"process_calls":STATE["calls"]-CALL_BASE}),flush=True)
                # Require an independently persisted, new authorization before another batch.
                time.sleep(20)
    except Exception as exc:
        STATE["status"]="checkpoint_unavailable" if STATE["status"] in ("restoring_checkpoint","awaiting_authorization") else "failed"
        STATE["errors"].append(type(exc).__name__)
        compute_ranking()
        announce_summary()


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
    assert batch_window(1000,990,900,720,45)==720
    assert batch_window(1000,None,900,720,45)==540
    assert batch_window(1000,300,200,720,45)==50
    assert batch_window(1000,100,0,720,45)==0
    week=weekly_id()
    assert valid_active_manifest({"schema":2,"week_id":week,"run_id":week+"-r2"},week)
    assert not valid_active_manifest({"schema":2,"run_id":"v2-2026-01-01"},week)
    auth={"authorized_process_id":"p","authorized_batch":2,"calls":10,"calls_ceiling":100}
    assert batch_authorized(auth,"p",1) and not batch_authorized(auth,"q",1) and not batch_authorized(auth,"p",2)
    # Deterministic checkpoint and scoring checks; no real NVIDIA request.
    import tempfile
    global CHECKPOINT
    old_checkpoint = CHECKPOINT
    state_before = dict(STATE)
    raw_before = list(RAW)
    try:
        m = next(iter(SCORES))
        row = {"model":m,"phase":"behavior","test":"exact_instruction","repeat":0,
               "status":"pass","elapsed_s":1.0}
        probe = {"model":m,"trial":1,"ok":True,"elapsed_s":0.5}
        event = lambda k,d: {"schema":SCHEMA,"run_id":RUN_ID,"kind":k,"data":d,"calls":3}
        with tempfile.TemporaryDirectory() as tmp:
            CHECKPOINT = Path(tmp)/"checkpoint.json"
            CHECKPOINT.write_text(json.dumps({"schema":SCHEMA,"run_id":RUN_ID,
                "events":[event("trial",row),event("trial",row),event("probe",probe)]}),encoding="utf-8")
            restore(quiet=True)
            assert len(RAW) == 1 and len(STATE["probes"]) == 1
            assert STATE["calls"] == 3
            STATE["eligible_models"] = [m]
            compute_ranking()
            result = STATE["ranking"][0]
            assert result["evaluable"] == 1 and result["provisional"]
            assert result["indicador de pruebas"] == 100
            RAW.append(dict(row,test="arithmetic",status="infra_error"))
            compute_ranking()
            assert STATE["ranking"][0]["evaluable"] == 1
            assert STATE["ranking"][0]["indicador de pruebas"] == 100
            if MODE == "full":
                RAW.append(dict(row,phase="anti_loop",test="anti_generation_00",status="bad_answer"))
                compute_ranking()
                assert abs(STATE["ranking"][0]["indicador de pruebas"] - 27.27) < .01
            CHECKPOINT.write_text(json.dumps({"schema":SCHEMA,"run_id":"other-week","events":[]}),encoding="utf-8")
            n = len(RAW)
            restore(quiet=True)
            assert len(RAW) == n
            # Live branch simulation with immutable shard, duplicate test, and accumulated calls.
            shard = "checkpoint_events/" + RUN_ID + "/sample.json"
            manifest = {"schema":SCHEMA,"run_id":RUN_ID,"parts":[shard],"calls":12}
            inv = {"candidate_ids":[m],"started_utc":"2026-11-24T00:00:00Z"}
            fixtures = {"checkpoint.json":manifest,shard:{"schema":SCHEMA,"run_id":RUN_ID,
                "events":[event("inventory",inv),event("trial",row),event("trial",row),event("probe",probe)]}}
            restore(quiet=True,remote=True,reader=lambda p:fixtures[p])
            assert len(RAW)==1 and len(STATE["probes"])==1 and STATE["calls"]==12
            assert STATE["checkpoint_source"]=="github_live"
            try:
                restore(quiet=True,remote=True,reader=lambda p:fixtures[p] if p=="checkpoint.json" else {})
            except ValueError:
                pass
            else:
                raise AssertionError("missing shard accepted")
            assert len(RAW)==1 and STATE["calls"]==12
    finally:
        CHECKPOINT = old_checkpoint
        STATE.clear()
        STATE.update(state_before)
        RAW[:] = raw_before
    print("BENCHMARK_SELFTEST_OK", flush=True)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global LAST_HEALTH
        if self.path.split("?")[0] == "/health":
            LAST_HEALTH = time.monotonic()
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
                                                  "completed_models", "current_model", "run_id", "process_id", "segments")}
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
    if MODE not in ("probe", "smoke", "full"):
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
