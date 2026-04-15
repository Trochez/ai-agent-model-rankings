# Session Learnings: 2026-04-15

## Session Overview

**Focus**: Fix stuck delegated agents (30-minute freeze) and organize OMO skill repos.

---

## Key Learnings

### 1. Root Cause: 30-Minute Timeout Freeze

**Symptom**: Delegated agents (oracle, metis, momus, explore, librarian) freeze for 30 minutes.

**Root Causes**:
1. **Hardcoded default timeout**: Background tasks default to 1,800,000ms (30 minutes)
2. **GPT rate limits**: GPT-5.4 in fallback chain hits weekly limits
3. **Bug #2203**: Background tasks ignore `fallback_models` configuration
4. **No provider timeout**: Missing provider-level timeout to force faster fallback

**Solution**:
```json
{
  "provider": {
    "nvidia": { "timeout": 60000 },
    "openai": { "timeout": 60000 },
    "google": { "timeout": 60000 }
  },
  "background_task": { "staleTimeoutMs": 60000 }
}
```

**Files Modified**:
- `/home/trocha/.config/opencode/oh-my-opencode.json`

---

### 2. Skill Architecture: /omo-worker is Required

**Discovery**: `/omo-worker` was a local-only skill with no GitHub repo.

**Problem**:
- `/omo-team` requires `/omo-worker` to function
- Workers need the protocol to know how to:
  - Parse task context
  - Write results to correct location
  - Report completion
  - Handle errors
- No GitHub repo existed for `/omo-worker`

**Solution**:
- Created GitHub repo: https://github.com/Trochez/omo-worker
- Added README.md, LICENSE, .gitignore
- Updated `/omo-team` to document dependency
- Cross-linked both repos

---

### 3. Configuration Hierarchy for Timeouts

**Three layers of timeout protection**:

| Layer | Configuration | Scope |
|-------|---------------|-------|
| Environment | `OPENCODE_MODEL_TIMEOUT=120000` | Global (all sessions) |
| Provider-level | `"provider": { "nvidia": { "timeout": 60000 } }` | Per-provider |
| Background task | `"background_task": { "staleTimeoutMs": 60000 }` | Background agents |

**Recommendation**: Configure all three layers for defense-in-depth.

---

### 4. Fallback Chain Behavior

**How it works**:
```
Primary model (GLM5)
    ↓ (fails/times out)
Fallback 1 (GPT-5.4) ← Rate limit issue
    ↓ (fails)
Fallback 2 (Nemotron-120B)
    ↓ (fails)
30-minute hardcoded timeout
```

**Known Issue (GitHub #2203)**:
- Background tasks may ignore `fallback_models` configuration
- Falls back to hardcoded free-tier models instead
- **Workaround**: Use provider-level timeouts

---

### 5. Skill Repository Organization

**Before**:
```
~/.agents/skills/
├── omo-team/      ← No GitHub repo
├── omo-worker/    ← No GitHub repo
└── omo-ralplan/   ← Had GitHub repo
```

**After**:
```
GitHub Repos:
├── https://github.com/Trochez/omo-team      ← Created & linked
├── https://github.com/Trochez/omo-worker    ← Created NEW
└── https://github.com/Trochez/omo-ralplan   ← Updated

Cross-links:
omo-team ──► omo-worker (required dependency)
omo-worker ──► omo-team (parent skill)
```

---

## Documentation Updates

### Files Updated

| Repo | File | Changes |
|------|------|---------|
| `omo-ralplan` | `docs/configuration.md` | Added provider timeout config |
| `omo-team` | `README.md` | Added timeout config, omo-worker dependency, GitHub links |
| `omo-worker` | `README.md` | Created with full documentation, GitHub links |
| `oh-my-opencode.json` | (config) | Added provider timeouts, background_task config |

---

## Action Items for Future

1. **Monitor GPT rate limits**: Check when weekly limits reset
2. **Test timeout behavior**: Verify 60-second fallback works
3. **Document for team**: Share timeout configuration with team
4. **Consider circuit breaker**: Add explicit rate limit detection

---

## Related GitHub Issues

- **Issue #2203**: Background task fallback bug
- **Issue #15582**: Provider timeout not respected (fixed)
- **Issue #20098**: Configurable provider/model fallback

---

## Session Metrics

| Metric | Value |
|--------|-------|
| Skills documented | 3 |
| GitHub repos created | 1 (omo-worker) |
| GitHub repos updated | 3 |
| Configuration fixes | 1 (oh-my-opencode.json) |
| Commits pushed | 6 |

---

**Session Date**: 2026-04-15  
**Session Focus**: Timeout fixes + skill repo organization
