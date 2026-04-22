# Session Learnings: Session Interruption Analysis & Fixes

**Date:** 2026-04-20
**Issue:** OpenCode sessions interrupted suddenly — root cause analysis and configuration fixes

---

## Problem Summary

OpenCode sessions were being interrupted suddenly due to multiple configuration gaps that left the system vulnerable to timeout cascades, SSE stream deaths, and false-positive circuit breaker triggers.

---

## Root Cause Analysis

### 6 Categories of Interruption (Ranked by Likelihood)

| Priority | Category | Root Cause | Symptom |
|----------|----------|------------|---------|
| P0 | Rate Limit + Timeout Cascade | Missing `timeout_seconds` in runtime_fallback | 30+ min freeze, then death |
| P0 | SSE Stream Death | Missing `chunkTimeout` in provider config | Blank TUI, "stream error" |
| P1 | Context Window Overflow | No NVIDIA-specific recovery hook | 400 error, session abort |
| P1 | Circuit Breaker False Positive | Default `consecutiveThreshold: 20` too low | Task ends with "interrupt" status |
| P2 | Subagent Spawn Limits | Hard limits (depth=3, budget=50) | Delegated task fails immediately |
| P2 | Process Signal Death | SIGINT/SIGTERM/SIGHUP | Process exit code 130/143 |

### Architecture Findings

**Three Timeout Layers:**
| Layer | Default | Your Config | Purpose |
|-------|---------|-------------|---------|
| Provider timeout | 300,000ms (5min) | 120,000ms | Model API request timeout |
| Background task timeout | 2,700,000ms (45min) | 60,000ms | Background agent execution |
| MCP server timeout | 5,000ms (5sec) | default | MCP server communication |

**SSE Stream Architecture:**
- 15-second inactivity timeout on GlobalSDK event stream
- Auto-reconnect after 250ms on stream failure
- `chunkTimeout` controls per-chunk SSE timeout (was missing)

**Circuit Breaker Defaults:**
- `consecutiveThreshold: 20` — same tool called 20+ times with identical input
- `maxToolCalls: 4000` — total tool call limit per task
- Search-heavy agents (explore, librarian) easily exceed 20 consecutive calls

---

## Fixes Applied

### Fix 1: Runtime Fallback Timeout & Cooldown

**Problem:** Without `timeout_seconds`, fallback retries had no independent timeout cap. A rate-limited fallback model (e.g., GPT-5.4 hitting 429) could retry indefinitely until `staleTimeoutMs` killed the entire task.

**Change:**
```json
"runtime_fallback": {
  "enabled": true,
  "retry_on_errors": [429, 500, 502, 503, 504, 529],
  "retry_on_timeout": true,
  "retry_on_network_error": true,
  "max_fallback_attempts": 5,
  "backoff_ms": 1000,
  "max_backoff_ms": 30000,
  "timeout_seconds": 120,        // NEW: 2-minute cap per fallback attempt
  "cooldown_seconds": 30         // NEW: 30s cooldown between fallback attempts
}
```

**Impact:** Prevents indefinite retry loops on rate-limited fallbacks. Each fallback attempt now has a hard 2-minute timeout, with 30s cooldown between attempts.

### Fix 2: Provider Chunk Timeout

**Problem:** Without `chunkTimeout`, there was no per-chunk SSE timeout. If the LLM stopped sending tokens mid-stream (e.g., during "thinking" time), the connection could hang until the provider-level timeout (2 min) or the SSE inactivity timeout (15s) triggered.

**Change:**
```json
"provider": {
  "nvidia": {
    "timeout": 120000,
    "chunkTimeout": 30000       // NEW: 30s between SSE chunks
  },
  "openai": {
    "timeout": 120000,
    "chunkTimeout": 30000       // NEW: 30s between SSE chunks
  },
  "google": {
    "timeout": 120000,
    "chunkTimeout": 30000       // NEW: 30s between SSE chunks
  }
}
```

**Impact:** If no SSE chunk arrives within 30 seconds, the request is aborted and fallback is triggered. This prevents indefinite hangs on stalled streams while still allowing reasonable "thinking" time.

### Fix 3: Circuit Breaker Override

**Problem:** Default `consecutiveThreshold: 20` was too aggressive for search-heavy agents. Explore and librarian agents legitimately call `grep`/`read` 20+ times with similar patterns, triggering false-positive loop detection.

**Change:**
```json
"background_task": {
  "staleTimeoutMs": 60000,
  "circuitBreaker": {
    "enabled": true,
    "consecutiveThreshold": 50,   // NEW: raised from default 20
    "maxToolCalls": 8000          // NEW: raised from default 4000
  }
}
```

**Impact:** Search-heavy agents can make up to 50 consecutive identical tool calls and 8000 total tool calls before circuit breaking. Still protects against genuine infinite loops.

---

## Files Modified

| File | Changes |
|------|---------|
| `/home/trocha/projects/explorer/oh-my-opencode.json` | All 3 fixes applied |
| `/home/trocha/.config/opencode/oh-my-opencode.json` | All 3 fixes applied (global config) |

**Note:** Both project-level and global configs were updated to ensure consistency. Previous session (April 15) documented that local configs don't auto-sync from global updates.

---

## Known Bugs (Unfixed — Upstream)

| Bug | Status | Impact | Workaround |
|-----|--------|--------|------------|
| #2203: Background tasks ignore `fallback_models` | Closed (PR #2800) | 30-min hangs | Update oh-my-opencode |
| #54060: TUI shows error despite successful fallback | Open | User confusion | Check logs for `candidate_succeeded` |
| #3011: No retry-count-based fallback | Open | Only error/timeout triggers fallback | N/A |
| #15149: SSE stream leaks on client disconnect | Open | Corrupted server state | Restart server |
| #14769: Sessions stay in "thinking" forever | Open | Requires manual intervention | Ctrl+C |

---

## Verification

```bash
# Verify both configs are valid JSON
python3 -c "import json; json.load(open('oh-my-opencode.json')); print('OK')"

# Verify all fixes present
python3 -c "
import json
with open('oh-my-opencode.json') as f:
    cfg = json.load(f)
rf = cfg['runtime_fallback']
assert rf['timeout_seconds'] == 120
assert rf['cooldown_seconds'] == 30
for p in ['nvidia','openai','google']:
    assert cfg['provider'][p]['chunkTimeout'] == 30000
assert cfg['background_task']['circuitBreaker']['consecutiveThreshold'] == 50
assert cfg['background_task']['circuitBreaker']['maxToolCalls'] == 8000
print('All fixes verified')
"
```

---

## Related Documentation

- [session-learnings-2026-04-06.md](./session-learnings-2026-04-06.md) — Original timeout architecture discovery
- [session-learnings-2026-04-06-fallback-investigation.md](./session-learnings-2026-04-06-fallback-investigation.md) — Fallback mechanism investigation
- [session-learnings-2026-04-15-timeout-configuration-fix.md](./session-learnings-2026-04-15-timeout-configuration-fix.md) — Previous timeout fix
- [FALLBACK_CONFIGURATION_GUIDE.md](./FALLBACK_CONFIGURATION_GUIDE.md) — Complete fallback configuration guide

---

## Action Items

- [x] Add `timeout_seconds` and `cooldown_seconds` to runtime_fallback (both configs)
- [x] Add `chunkTimeout` to all provider configs (both configs)
- [x] Add `circuitBreaker` overrides to background_task (both configs)
- [x] Verify JSON validity for both configs
- [x] Document session learnings
- [ ] Monitor session stability after fixes applied
- [ ] Check if trading_bot project config also needs updates
