# Model ID Investigation Report

**Date**: April 6, 2026
**Purpose**: Identify correct model IDs for failed models (excluding OpenAI)

---

## Summary

Investigated 6 failed models from the last test execution. Found that **2 models have INCORRECT IDs** (configuration errors), while **4 models are experiencing rate/quota limits** (temporary issues).

---

## Findings by Model

### 1. ❌ `qwen/qwen3.6-plus:free` (OpenRouter)

**Status**: ✅ **CORRECT ID** - Model exists and is available
**Error Type**: HTTP 429 - Rate limit (temporary)
**Correct ID**: `qwen/qwen3.6-plus:free`
**Details**:
- Model is available on OpenRouter
- Free tier with 1M context window
- Currently hitting OpenRouter's free tier rate limits (20 req/min, 200 req/day)
- **Action**: Wait for rate limit reset or reduce request frequency

---

### 2. ❌ `google/gemini-3.1-flash-lite-preview` (Google)

**Status**: ✅ **CORRECT ID** - Model exists and WORKS
**Error Type**: HTTP 503 (resolved) → Now PASSING
**Correct ID**: `google/gemini-3.1-flash-lite-preview`
**Details**:
- Model exists in Google's Gemini 3.1 family
- Successfully passed re-test (1457ms response time)
- Previous HTTP 503 was temporary (high demand)
- **Action**: No action needed - model is working

---

### 3. ❌ `google/gemini-3.1-pro-preview` (Google)

**Status**: ✅ **CORRECT ID** - Model exists
**Error Type**: HTTP 429 - Quota exceeded
**Correct ID**: `google/gemini-3.1-pro-preview`
**Details**:
- Model exists in Google's Gemini 3.1 family
- Requires Google AI Studio / Vertex AI billing setup
- Free tier quota exceeded
- **Action**: Set up billing or wait for quota reset

---

### 4. ❌ `meta-llama/llama-3.3-70b-instruct:free` (OpenRouter)

**Status**: ✅ **CORRECT ID** - Model exists and is available
**Error Type**: HTTP 429 - Rate limit (temporary)
**Correct ID**: `meta-llama/llama-3.3-70b-instruct:free`
**Details**:
- Model is available on OpenRouter (released Dec 6, 2024)
- Free tier with 65,536 context window
- Currently hitting OpenRouter's free tier rate limits
- **Action**: Wait for rate limit reset or reduce request frequency

---

### 5. ❌ `openrouter/qwen/qwen2.5-72b-instruct` (OpenRouter)

**Status**: ❌ **INCORRECT ID** - Configuration error
**Error Type**: HTTP 400 - Invalid model ID
**Incorrect ID**: `openrouter/qwen/qwen2.5-72b-instruct`
**Correct ID**: `qwen/qwen-2.5-72b-instruct`
**Details**:
- The model ID has an extra `openrouter/` prefix
- OpenRouter model IDs do NOT include the `openrouter/` prefix
- Correct format: `qwen/qwen-2.5-72b-instruct` (note: `qwen-2.5` not `qwen2.5`)
- Model released Sep 19, 2024 with 32,768 context window
- **Action**: Update configuration to use correct ID

---

### 6. ❌ `openrouter/qwen/qwen3-coder:free` (OpenRouter)

**Status**: ❌ **INCORRECT ID** - Configuration error
**Error Type**: HTTP 400 - Invalid model ID
**Incorrect ID**: `openrouter/qwen/qwen3-coder:free`
**Correct ID**: `qwen/qwen3-coder:free`
**Details**:
- The model ID has an extra `openrouter/` prefix
- OpenRouter model IDs do NOT include the `openrouter/` prefix
- Correct format: `qwen/qwen3-coder:free`
- Model released Jul 23, 2025 with 262,000 context window
- Free tier available
- **Action**: Update configuration to use correct ID

---

### 7. ❌ `stepfun/step-3.5-flash:free` (OpenRouter)

**Status**: ✅ **CORRECT ID** - Model exists and is available
**Error Type**: Unknown (null error, 3904ms timeout)
**Correct ID**: `stepfun/step-3.5-flash:free`
**Details**:
- Model is available on OpenRouter (released Jan 29, 2026)
- Free tier with 256,000 context window
- Sparse MoE architecture (196B params, 11B active)
- Error may be due to model complexity or provider issues
- **Action**: Retry with longer timeout or investigate provider status

---

## Configuration Fixes Required

### Immediate Fixes (Invalid Model IDs)

| Current ID | Correct ID | Provider |
|------------|------------|----------|
| `openrouter/qwen/qwen2.5-72b-instruct` | `qwen/qwen-2.5-72b-instruct` | OpenRouter |
| `openrouter/qwen/qwen3-coder:free` | `qwen/qwen3-coder:free` | OpenRouter |

### Rate Limit Issues (Temporary)

These models have correct IDs but are hitting rate limits:
- `qwen/qwen3.6-plus:free` - Wait for reset
- `meta-llama/llama-3.3-70b-instruct:free` - Wait for reset
- `google/gemini-3.1-pro-preview` - Requires billing setup

### Working Models

- `google/gemini-3.1-flash-lite-preview` - ✅ PASSING

---

## OpenRouter Model ID Convention

**Important**: OpenRouter model IDs follow this pattern:
```
{provider}/{model-name}
```

**DO NOT** prefix with `openrouter/`:
- ❌ Wrong: `openrouter/qwen/qwen3-coder:free`
- ✅ Correct: `qwen/qwen3-coder:free`

The `:free` suffix indicates free tier availability.

---

## Google Gemini Model Names

Google Gemini models are named:
- `gemini-3.1-pro` (or `gemini-3.1-pro-preview`)
- `gemini-3.1-flash` (or `gemini-3.1-flash-lite-preview`)
- `gemini-2.0-flash` (older generation)

Note: The current generation is **Gemini 3.1**, not 2.0 or 1.5.

---

## Recommendations

1. **Fix configuration** for the 2 models with incorrect IDs
2. **Wait for rate limit reset** for OpenRouter free models (resets daily)
3. **Set up billing** for Google Gemini Pro if needed
4. **Increase timeout** for `stepfun/step-3.5-flash:free` (complex MoE model)
5. **Monitor** rate limit usage to avoid hitting daily limits

---

## Sources

- OpenRouter Models: https://openrouter.ai/models
- OpenRouter Qwen Models: https://openrouter.ai/qwen
- Google Gemini API: https://ai.google.dev/gemini-api/docs/models
- OpenRouter Free Models: https://openrouter.ai/collections/free-models
