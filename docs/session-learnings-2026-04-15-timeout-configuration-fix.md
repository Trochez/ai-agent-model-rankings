# Session Learnings: Model Timeout Configuration Fix

**Date:** 2026-04-15
**Issue:** `/omo-ralplan` frozen for 30+ minutes due to rate-limited GPT-5.4 fallback

---

## Problem Summary

The `/omo-ralplan` consensus planning workflow was frozen because:

1. Oracle agent's primary model (`nvidia/z-ai/glm5`) failed/timed out
2. System fell back to `openai/gpt-5.4` (first fallback)
3. GPT-5.4 hit rate limits (429 errors)
4. No timeout configuration → indefinite hang

---

## Root Cause Analysis

### Configuration Investigation

| Config File | Location | Status |
|-------------|----------|--------|
| Global | `~/.config/opencode/oh-my-opencode.json` | Had timeout (60s), needed update |
| trading_bot | `projects/trading_bot/oh-my-opencode.json` | **Missing** timeout config |
| explorer | Uses global | Inherited from global |

### AGENTS.md vs Actual Config Mismatch

**Critical Discovery:** The AGENTS.md Model Capability Table was outdated:

| Role | AGENTS.md (Documented) | oh-my-opencode.json (Actual) |
|------|------------------------|------------------------------|
| Frontier | `gpt-5.4-mini` | `nvidia/z-ai/glm5` |
| Standard | `gpt-5.4-mini` | `nvidia/z-ai/glm5` |
| Oracle | `gpt-5.4-mini` | `nvidia/z-ai/glm5` |

**Impact:** Documentation suggested GPT-5.4 was the primary model, but it's actually the fallback.

---

## Configuration Hierarchy Understanding

```
┌─────────────────────────────────────────────────────────┐
│ Global Config                                           │
│ ~/.config/opencode/oh-my-opencode.json                  │
│ (used as base/defaults)                                 │
└────────────────────────┬────────────────────────────────┘
                         │
                         │ Merged at runtime
                         │ (local overrides matching keys)
                         ▼
┌─────────────────────────────────────────────────────────┐
│ Project Config                                          │
│ projects/[name]/oh-my-opencode.json                     │
│ (overrides global, adds project-specific settings)      │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│ Final Config (at runtime)                               │
│ = Global merged with Local                              │
└─────────────────────────────────────────────────────────┘
```

### Key Behaviors

| Aspect | Behavior |
|--------|----------|
| **Sync** | ❌ No automatic sync |
| **Merge** | ✅ Keys are merged at runtime |
| **Override** | ✅ Local config overrides global for matching keys |
| **Direction** | One-way: Global → Local (at startup only) |
| **Updates** | Changes to global do NOT propagate to existing local configs |

---

## Solution Applied

### 1. Updated Global Config

**File:** `/home/trocha/.config/opencode/oh-my-opencode.json`

```json
"provider": {
  "nvidia": {
    "timeout": 120000
  },
  "openai": {
    "timeout": 120000
  },
  "google": {
    "timeout": 120000
  }
}
```

Changed from 60000ms (1 minute) to 120000ms (2 minutes).

### 2. Added Timeout to trading_bot Config

**File:** `/home/trocha/projects/trading_bot/oh-my-opencode.json`

Added the same `provider` section with 120s timeout for all providers.

### 3. Explorer Project

Uses global config (no local override), so automatically inherits the fix.

---

## Lessons Learned

### 1. Timeout Configuration is Critical

Without timeout configuration, rate-limited models can cause indefinite hangs. Always configure:

```json
"provider": {
  "nvidia": { "timeout": 120000 },
  "openai": { "timeout": 120000 },
  "google": { "timeout": 120000 }
}
```

### 2. Fallback Chain Order Matters

When GPT-5.4 is rate-limited, it should not be the first fallback. Consider:

```json
"fallback_models": [
  "nvidia/nvidia/nemotron-3-super-120b-a12b",
  "nvidia/meta/llama-3.3-70b-instruct",
  "openai/gpt-5.4"
]
```

### 3. AGENTS.md Can Become Stale

The AGENTS.md Model Capability Table is auto-generated and can become outdated. Always verify against actual `oh-my-opencode.json` configuration.

### 4. Local Configs Don't Sync

When updating global config, remember to also update any project-specific `oh-my-opencode.json` files.

---

## Verification Commands

```bash
# Check global config timeout
grep -A 10 '"provider"' ~/.config/opencode/oh-my-opencode.json

# Check project config timeout
grep -A 10 '"provider"' projects/trading_bot/oh-my-opencode.json

# Check for frozen processes
ps aux | grep opencode
```

---

## Related Documentation

- [FALLBACK_CONFIGURATION_GUIDE.md](./FALLBACK_CONFIGURATION_GUIDE.md)
- [session-learnings-2026-04-07-model-configuration-fix.md](./session-learnings-2026-04-07-model-configuration-fix.md)
- [session-learnings-2026-04-06-fallback-investigation.md](./session-learnings-2026-04-06-fallback-investigation.md)

---

## Action Items

- [x] Add timeout configuration to global config
- [x] Add timeout configuration to trading_bot config
- [x] Verify all configs have timeout settings
- [ ] Consider updating AGENTS.md to match actual configuration
- [ ] Consider reordering fallback chains to put working models first
