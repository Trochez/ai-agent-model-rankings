# Fallback Configuration Guide

**Purpose:** Comprehensive guide to model fallback configuration in oh-my-opencode
**Last Updated:** April 6, 2026
**Status:** Complete - All agents configured

---

## Table of Contents

1. [Overview](#overview)
2. [Current Configuration Status](#current-configuration-status)
3. [How Fallback Works](#how-fallback-works)
4. [Known Limitations](#known-limitations)
5. [Known Bugs](#known-bugs)
6. [Configuration Examples](#configuration-examples)
7. [Troubleshooting](#troubleshooting)
8. [Best Practices](#best-practices)

---

## Overview

### What is Model Fallback?

Model fallback is an automatic failover mechanism that switches to alternative models when the primary model fails due to:
- Usage limits (HTTP 429)
- Rate limits
- Timeouts
- Authentication errors
- Server errors (5xx)

### Current Implementation

**Type:** Error-triggered and timeout-triggered fallback
**NOT IMPLEMENTED:** Retry-count-based fallback (e.g., "switch after 5 retries")

**GitHub Issue #3011** (OPEN): Feature request for configurable retry mechanism

---

## Current Configuration Status

### Global Fallback Toggle

```json
{
  "model_fallback": true  // Line 3 of oh-my-opencode.json
}
```

### All Agents Configured

✅ **All 11 agents have fallback chains configured**
✅ **All 8 categories have fallback chains configured**
✅ **Global timeout set to 120000ms (2 minutes)**

### Agent Fallback Coverage

#### Agents Using GPT-5.4 as Primary (High Usage Limit Risk)

| Agent | Primary Model | Fallback 1 | Fallback 2 | Status |
|-------|---------------|------------|------------|--------|
| hephaestus | openai/gpt-5.4 | qwen3-coder:free | glm-5 | ✅ Excellent |
| oracle | openai/gpt-5.4 | glm-5 | qwen3.6-plus:free | ✅ Excellent |
| prometheus | openai/gpt-5.4 | glm-5 | qwen3.6-plus:free | ✅ Excellent |
| momus | openai/gpt-5.4 | glm-5 | qwen3.6-plus:free | ✅ Excellent |

#### Agents Using Free Models as Primary (No Usage Limit Risk)

| Agent | Primary Model | Why Safe | Fallback Chain |
|-------|---------------|----------|----------------|
| sisyphus | z-ai/glm-5 | NVIDIA Build - no limits | gpt-5.4 → qwen3.6-plus:free |
| explore | z-ai/glm-5 | NVIDIA Build - no limits | qwen3.6-plus:free → step-3.5-flash:free |
| metis | qwen3.6-plus:free | OpenRouter free tier | glm-5 → gpt-5.4 |
| librarian | gemini-3.1-flash-lite | Google - generous limits | qwen3.6-plus:free → glm-5 |
| multimodal-looker | qwen3.6-plus:free | OpenRouter free tier | qwen2.5-vl-72b-instruct → glm-5 |
| atlas | qwen3.6-plus:free | OpenRouter free tier | glm-5 → llama-3.3-70b-instruct:free |
| sisyphus-junior | z-ai/glm-5 | NVIDIA Build - no limits | qwen3.6-plus:free → llama-3.3-70b-instruct:free |

### Category Fallback Coverage

All 8 categories have fallback chains:

| Category | Primary Model | Fallback 1 | Fallback 2 |
|----------|---------------|------------|------------|
| visual-engineering | qwen2.5-vl-72b-instruct | qwen3.6-plus:free | gemini-3.1-pro-preview |
| ultrabrain | openai/gpt-5.4 | glm-5 | qwen3.6-plus:free |
| deep | openai/gpt-5.3-codex | gpt-5.4 | glm-5 |
| artistry | gemini-3.1-pro-preview | qwen2.5-vl-72b-instruct | glm-5 |
| quick | z-ai/glm-5 | qwen3.6-plus:free | step-3.5-flash:free |
| unspecified-low | z-ai/glm-5 | qwen3.6-plus:free | llama-3.3-70b-instruct:free |
| unspecified-high | z-ai/glm-5 | gpt-5.4 | qwen3.6-plus:free |
| writing | gemini-3.1-flash-lite-preview | qwen2.5-72b-instruct | llama-3.3-70b-instruct:free |

---

## How Fallback Works

### Automatic Fallback Triggers

The system automatically falls back when it detects:

| Trigger | Example | HTTP Code | Fallback? |
|---------|---------|-----------|-----------|
| **Usage limit exceeded** | "You have hit your ChatGPT usage limit" | 429 | ✅ Yes |
| **Rate limit** | "API rate limit reached" | 429 | ✅ Yes |
| **Timeout** | Model doesn't respond within timeout | N/A | ✅ Yes |
| **Auth error** | Invalid API key | 401 | ✅ Yes |
| **Server error** | Provider issues | 5xx | ✅ Yes |

### Fallback Flow

```
1. User selects agent (e.g., Prometheus)
   ↓
2. Try: openai/gpt-5.4 (primary model)
   ↓
3. Error: Usage limit reached (HTTP 429)
   ↓
4. AUTOMATIC FALLBACK TRIGGERED
   ↓
5. Try: z-ai/glm-5 (first fallback)
   ↓
6. Success! Response returned to user
```

### Configuration Hierarchy

```
Environment Variables (OPENCODE_MODEL_TIMEOUT)
↓ (global override)
Provider-level timeout (opencode.json)
↓ (provider-specific)
Agent-level fallback (oh-my-opencode.json)
↓ (agent-specific)
SDK defaults (hardcoded)
```

---

## Known Limitations

### 1. Retry-Count-Based Fallback NOT Implemented

**What doesn't exist:**
- Configure fallback to trigger after N retries
- Example: "Switch to fallback after 5 attempts"

**Current behavior:**
- Fallback triggers on errors/timeouts, not retry counts
- No configuration for `maxAttempts` or `retryCount`

**Workaround:**
- Use timeout-based fallback (already configured: 120000ms)
- Adjust `OPENCODE_MODEL_TIMEOUT` for faster/slower fallback

**GitHub Issue:** [#3011](https://github.com/anomalyco/opencode/issues/3011) (OPEN)

### 2. SSE Retry Configuration is Connection-Level

**Found in SDK:**
```typescript
{
  sseDefaultRetryDelay: 3000,
  sseMaxRetryAttempts: number,
  sseMaxRetryDelay: 30000
}
```

**Important:** This is for **SSE connection retries** (network failures), NOT model fallback switching.

---

## Known Bugs

### Bug 1: TUI Doesn't Show Fallback Response

**Issue:** When primary model hits usage limits:
- ✅ Fallback is triggered correctly
- ✅ Fallback model succeeds
- ❌ TUI shows original error instead of fallback response

**Evidence:**
```
Logs show: "model_fallback_decision: candidate_succeeded"
TUI shows: "⚠️ API rate limit reached. Please try again later."
```

**Impact:** Users think fallback isn't working when it actually is.

**Workaround:**
1. Wait 2-3 seconds after error
2. Check logs for `candidate_succeeded`
3. Press Enter or refresh TUI
4. Trust the configuration - it's working

**Similar Issue:** [OpenClaw #54060](https://github.com/openclaw/openclaw/issues/54060)

### Bug 2: Background Task Fallback Ignored

**Issue:** Background tasks (explore/librarian) ignore configured fallback models.

**Root Cause:**
- `setSessionFallbackChain()` not called in `executeBackgroundTask()`
- Background sessions use hardcoded fallback chains

**Impact:**
- Affects delegated agents (explore, librarian)
- Configured fallback models ignored for background tasks

**Workaround:**
- Aggressive timeout (already configured: 120000ms)
- Ensures faster fallback even with hardcoded chains

**GitHub Issue:** [#2203](https://github.com/code-yeongyu/oh-my-openagent/issues/2203) (CLOSED)

---

## Configuration Examples

### Example 1: Agent with GPT-5.4 Primary

```json
{
  "prometheus": {
    "model": "openai/gpt-5.4",
    "variant": "max",
    "reasoningEffort": "xhigh",
    "temperature": 0.3,
    "top_p": 0.9,
    "maxTokens": 16384,
    "mode": "primary",
    "category": "planner",
    "fallback_models": [
      "z-ai/glm-5",
      "qwen/qwen3.6-plus:free"
    ]
  }
}
```

**Behavior:**
1. Try: openai/gpt-5.4
2. On error: Try z-ai/glm-5
3. On error: Try qwen/qwen3.6-plus:free

### Example 2: Agent with Free Model Primary

```json
{
  "explore": {
    "model": "z-ai/glm-5",
    "variant": "low",
    "reasoningEffort": "minimal",
    "temperature": 0.3,
    "top_p": 0.9,
    "maxTokens": 16384,
    "mode": "subagent",
    "category": "search",
    "fallback_models": [
      "qwen/qwen3.6-plus:free",
      "stepfun/step-3.5-flash:free"
    ]
  }
}
```

**Behavior:**
1. Try: z-ai/glm-5 (NVIDIA Build - no limits)
2. On error: Try qwen/qwen3.6-plus:free
3. On error: Try stepfun/step-3.5-flash:free

### Example 3: Category-Level Fallback

```json
{
  "categories": {
    "ultrabrain": {
      "model": "openai/gpt-5.4",
      "variant": "xhigh",
      "reasoningEffort": "xhigh",
      "temperature": 0.3,
      "top_p": 0.9,
      "maxTokens": 16384,
      "fallback_models": [
        "z-ai/glm-5",
        "qwen/qwen3.6-plus:free"
      ]
    }
  }
}
```

**Behavior:**
- Applies to all tasks delegated to `ultrabrain` category
- Independent of specific agent used

---

## Troubleshooting

### Issue: "Fallback doesn't seem to work"

**Check:**
1. ✅ Verify `model_fallback: true` in oh-my-opencode.json
2. ✅ Verify agent has `fallback_models` array
3. ✅ Check logs for `model_fallback_decision`
4. ⚠️ Be aware of TUI display bug (fallback may work but not show)

**Solution:**
- Configuration is likely correct
- Check logs to verify fallback actually triggered
- Wait 2-3 seconds after error for response

### Issue: "Infinite hold in TUI"

**Check:**
1. ✅ Verify `OPENCODE_MODEL_TIMEOUT` is set (120000ms recommended)
2. ✅ Check if model is actually processing (check logs)
3. ⚠️ May be TUI display bug, not actual hang

**Solution:**
- Current timeout (2 minutes) should prevent infinite holds
- If still occurring, reduce timeout to 60000ms (1 minute)

### Issue: "Background agents don't use configured fallback"

**Check:**
1. ⚠️ Known bug (Issue #2203)
2. Affects explore and librarian agents when delegated

**Solution:**
- Aggressive timeout (already configured) provides workaround
- Bug is being tracked and will be fixed

### Issue: "Usage limits reached on GPT-5.4"

**Check:**
1. ✅ Fallback should trigger automatically
2. ✅ Configuration already has fallback chains

**Solution:**
- Trust the configuration - fallback will work
- Consider using free models as primary to avoid limits
- Monitor logs for `candidate_succeeded`

---

## Best Practices

### 1. Diversify Fallback Chains

**Good:**
```json
"fallback_models": [
  "z-ai/glm-5",           // NVIDIA Build
  "qwen/qwen3.6-plus:free" // OpenRouter
]
```

**Why:** Different providers = resilience against provider-specific outages

### 2. Use Free Models as Fallbacks

**Good:**
```json
"fallback_models": [
  "qwen/qwen3.6-plus:free",
  "meta-llama/llama-3.3-70b-instruct:free"
]
```

**Why:** No usage limits, no cost, always available

### 3. Configure Aggressive Timeout

**Good:**
```bash
export OPENCODE_MODEL_TIMEOUT=120000  # 2 minutes
```

**Why:** Faster fallback, better user experience

### 4. Monitor Logs

**Check for:**
```
model_fallback_decision: candidate_succeeded
```

**Why:** Confirms fallback actually worked (even if TUI doesn't show it)

### 5. Trust the Configuration

**Current status:**
- ✅ All agents configured
- ✅ All categories configured
- ✅ Global fallback enabled
- ✅ Timeout configured

**Action:** No changes needed - configuration is optimal

---

## Related Documentation

- [Session Learnings - April 6 (Fallback Investigation)](session-learnings-2026-04-06-fallback-investigation.md)
- [Session Learnings - April 6 (Timeout Configuration)](session-learnings-2026-04-06.md)
- [Oh-My-OpenCode Configuration](~/.config/opencode/oh-my-opencode.json)
- [Timeout Configuration Guide](~/.config/opencode/TIMEOUT_CONFIGURATION.md)

---

## GitHub Issues

1. **Issue #3011** - Configurable Retry Mechanism
   - https://github.com/anomalyco/opencode/issues/3011
   - Status: OPEN
   - Impact: High - enables retry-count-based fallback

2. **Issue #54060** - TUI surfaces rate limit error even though fallback succeeds
   - https://github.com/openclaw/openclaw/issues/54060
   - Status: CLOSED
   - Impact: High - affects user perception of fallback

3. **Issue #2203** - Background task fallback bug
   - https://github.com/code-yeongyu/oh-my-openagent/issues/2203
   - Status: CLOSED (PR #2800)
   - Impact: Critical - affects all background tasks

---

**Document Version:** 1.0
**Last Updated:** April 6, 2026
