#!/usr/bin/env python3
"""NVIDIA ranking runner for a FREE Render web service.

A single bounded, opt-in run starts only when AUTO_RUN=1 AND NVIDIA_API_KEY exists.
No endpoint can trigger a new run. Results are public benchmark data, NOT credentials.
The ephemeral filesystem is not durable; JSON summary is also emitted to Render logs.
"""
import csv
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
GLOBAL_FIELDS = ["nombre modelo", "poder", "demanda",
                 "tiempo de respuesta promedio", "mediana tiempo respuesta en pruebas",
                 "velocidad", "indicador de pruebas", "indicador global"]
STATE = {
    "status": "starting", "mode": MODE, "started_utc": None, "ended_utc": None,
    "calls": 0, "selected": 0, "eligible": 0, "completed_models": 0,
    "current_model": None, "errors": [], "ranking": [], "excluded": [],
    "method": "behavior-suite-12-cases, repeats=5 (full) or 1 (smoke); anti-loop-adapted-160+40 only full / global-v3",
    "notice": "Poder y demanda son estimaciones de noviembre 2026; anti-loop v4.1 adaptado; nunca son medidas internas de GPU.",
}
RAW = []
T0 = {}
STOP = False
START = time.monotonic()
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
    return STATE["calls"] >= MAX_CALLS or time.monotonic() - START > MAX_SECONDS


def api(path, body=None, timeout=SOCKET_TIMEOUT):
    if should_stop():
        raise BudgetReached("max_requests_or_runtime")
    STATE["calls"] += 1
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
    out = api("/chat/completions", req)
    if not out["ok"]:
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
                "tokens": (obj.get("usage") or {}).get("completion_tokens")})
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
    trace = []
    seen = set()
    answer = ""
    tool_count = 0
    status = "not_finished"
    for step in range(8):
        result = chat(model, msgs, [TOOL] if expected == "tool" else None)
        trace.append({"step": step, "ok": result["ok"], "elapsed_s": round(result["elapsed"], 4),
                      "error": result.get("error"), "finish_reason": result.get("finish_reason")})
        if not result["ok"]:
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
    RAW.append(row)
    if phase == "behavior":
        print("BEHAVIOR_TRIAL_RESULT " + json.dumps(
            {k: row[k] for k in ("model", "test", "repeat", "status", "elapsed_s", "tool_calls")},
            ensure_ascii=False), flush=True)
    return row


def compute_ranking():
    rows = []
    completed = [m for m in STATE.get("models_done", [])]
    lat = {m: statistics.median([r["elapsed_s"] for r in RAW if r["model"] == m and
            r["phase"] == "behavior" and r["status"] == "pass"])
           for m in completed if any(r["model"] == m and r["phase"] == "behavior" and
                                     r["status"] == "pass" for r in RAW)}
    tmin = min(lat.values()) if lat else None
    tmax = max(lat.values()) if lat else None
    for m in completed:
        scored = [r for r in RAW if r["model"] == m and r["phase"] == "behavior"]
        evaluable = [r for r in scored if r["status"] not in ("infra_error", "unevaluable")]
        correct = sum(r["status"] == "pass" for r in evaluable)
        t = 100*correct/len(evaluable) if evaluable else None
        v = None
        if m in lat:
            v = 100 if tmin == tmax else 100 * (math.log1p(tmax) - math.log1p(lat[m])) / \
                (math.log1p(tmax) - math.log1p(tmin))
            v = max(0, min(100, v))
        p, d = SCORES.get(m, (None, None))
        g = .35*p + .15*(100-d) + .15*v + .35*t if None not in (p,d,v,t) else None
        probes = [r for r in STATE.get("probes", []) if r["model"] == m and r["ok"]]
        t0 = statistics.mean(r["elapsed_s"] for r in probes) if probes else None
        anti = [r for r in RAW if r["model"] == m and r["phase"] == "anti_loop"]
        row = dict(zip(GLOBAL_FIELDS, [m, p, d,
            round(t0, 3) if t0 is not None else None,
            round(lat[m], 3) if m in lat else None,
            round(v, 2) if v is not None else None,
            round(t, 2) if t is not None else None,
            round(g, 2) if g is not None else None]))
        row.update({"evaluable": len(evaluable), "planned_behavior": 12*CASE_REPEATS,
                    "passed": correct, "anti_pass": sum(x["status"] == "pass" for x in anti),
                    "anti_total": len(anti), "p_d_provenance": "historical_estimate_20261119",
                    "provisional": len(scored) < 12*CASE_REPEATS,
                    "speed_cohort_n": len(lat)})
        rows.append(row)
    rows.sort(key=lambda r: (r["indicador global"] is None,
                            -(r["indicador global"] or 0), r["nombre modelo"]))
    STATE["ranking"] = rows


def runner():
    global START
    START = time.monotonic()
    STATE["started_utc"] = now()
    STATE["status"] = "discovering"
    try:
        discovery = api("/models", timeout=40)
        if discovery["ok"]:
            entries = discovery["data"].get("data", [])
            ids = sorted({r.get("id", "") for r in entries if isinstance(r, dict) and r.get("id")})
        else:
            ids = [clean_id(x) for x in SCORES]
            STATE["errors"].append("Catalog unavailable; fallback to historical candidates.")
        possible = sorted({"nvidia/" + i for i in ids
                           if i and not SPECIAL.search(i)})
        if not possible:
            possible = ALT_MODEL_IDS
        priority = [i for i in ALT_MODEL_IDS if i in possible]
        possible = priority + [i for i in possible if i not in priority]
        only = [m.strip() for m in os.getenv("BENCHMARK_MODEL_IDS", "").split(",") if m.strip()]
        if only:
            catalog_set = set(possible)
            possible = [m for m in only if m in catalog_set]
        if MAX_MODELS:
            possible = possible[:MAX_MODELS]
        STATE["selected"] = len(possible)
        STATE["models_selected"] = possible
        print("INVENTORY_SELECTED " + json.dumps({"count":len(possible), "candidate_ids": possible}, ensure_ascii=False), flush=True)
        STATE["status"] = "availability"
        probes = []
        eligible = []
        for m in possible:
            successes = []
            for trial in range(3):
                r = chat(m, [{"role": "user", "content": "Reply exactly READY."}], limit=64)
                row = {"model": m, "request_model": clean_id(m), "trial": trial+1, "ok": r["ok"],
                       "elapsed_s": round(r["elapsed"], 5), "error": r.get("error")}
                probes.append(row)
                print("PROBE_RESULT " + json.dumps(row, ensure_ascii=False), flush=True)
                if r["ok"]:
                    successes.append(r["elapsed"])
                if r.get("http") in (401, 403):
                    STATE["errors"].append("Authentication rejected by NVIDIA; stopping.")
                    STATE["status"] = "needs_valid_key"
                    STATE["probes"] = probes
                    return
            if successes:
                eligible.append(m)
            else:
                STATE["excluded"].append(m)
            STATE["probes"] = probes
        STATE["eligible"] = len(eligible)
        STATE["models_done"] = []
        STATE["eligible_models"] = eligible
        if MODE == "probe":
            STATE["status"] = "completed"
            return
        STATE["status"] = "behavior"
        for m in eligible:
            STATE["current_model"] = m
            for name, prompt, expected in cases():
                for repeat in range(CASE_REPEATS):
                    one_trial(m, name, prompt, expected, repeat, "behavior")
            STATE["models_done"].append(m)
            STATE["completed_models"] = len(STATE["models_done"])
            compute_ranking()
            print("BEHAVIOR_MODEL_DONE " + json.dumps({"model": m, "rank": next((r for r in STATE["ranking"] if r["nombre modelo"] == m), {})}, ensure_ascii=False), flush=True)
            if MODE == "full":
                STATE["status"] = "anti_loop"
                for name, prompt, expected in anti_cases():
                    one_trial(m, name, prompt, expected, 0, "anti_loop")
            compute_ranking()
            print("MODEL_RESULT " + json.dumps(STATE["ranking"][-1] if len(STATE["ranking"]) == 1 else
                next((r for r in STATE["ranking"] if r["nombre modelo"] == m), {}), ensure_ascii=False), flush=True)
            STATE["status"] = "behavior"
        STATE["status"] = "completed"
    except BudgetReached as exc:
        STATE["status"] = "partial_budget"
        STATE["errors"].append(str(exc))
        compute_ranking()
    except Exception as exc:
        STATE["status"] = "failed"
        STATE["errors"].append(type(exc).__name__ + ": " + str(exc)[:300])
        compute_ranking()
    finally:
        STATE["ended_utc"] = now()
        STATE["current_model"] = None
        print("BENCHMARK_SUMMARY " + json.dumps({k:v for k,v in STATE.items() if k not in
              ("models_selected", "probes")}, ensure_ascii=False), flush=True)


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
                                                  "completed_models", "current_model")}
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
        {"status": STATE["status"], "mode": MODE, "free_only": True}), flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
