# Model Test Results - Quick Reference
**Test Date**: 2026-04-06 15:07:32
**Total Models**: 11 | **Passing**: 2 (18%) | **Failing**: 9 (82%)

---

## ✅ PASSING MODELS (2/11)

| Model | Provider | Time | Status |
|-------|----------|------|--------|
| `z-ai/glm-5` | OpenRouter | 9.7s | ✅ Working |
| `qwen/qwen2.5-vl-72b-instruct` | OpenRouter | 2.2s | ✅ Working |

---

## ❌ FAILING MODELS (9/11)

### 🔧 CONFIG ERRORS (2 models) - FIX REQUIRED

| Current (WRONG) | Should Be | Error |
|-----------------|-----------|-------|
| `openrouter/qwen/qwen2.5-72b-instruct` | `qwen/qwen2.5-72b-instruct` | Invalid ID |
| `openrouter/qwen/qwen3-coder:free` | `qwen/qwen3-coder:free` | Invalid ID |

### ⚠️ QUOTA LIMITS (3 models)

| Model | Provider | Error |
|-------|----------|-------|
| `openai/gpt-5.4` | OpenAI | Quota exceeded |
| `openai/gpt-5.3-codex` | OpenAI | Quota exceeded |
| `google/gemini-3.1-pro-preview` | Google | Quota exceeded |

### ⚠️ RATE LIMITS (2 models)

| Model | Provider | Limit |
|-------|----------|-------|
| `qwen/qwen3.6-plus:free` | OpenRouter | 20 req/min, 200 req/day |
| `meta-llama/llama-3.3-70b-instruct:free` | OpenRouter | 20 req/min, 200 req/day |

### 🔴 AVAILABILITY ISSUES (2 models)

| Model | Provider | Issue |
|-------|----------|-------|
| `google/gemini-3.1-flash-lite-preview` | Google | High demand (503) |
| `stepfun/step-3.5-flash:free` | OpenRouter | Timeout |

---

## 🎯 IMMEDIATE ACTIONS

1. **Fix Config** (2 models): Remove "openrouter/" prefix
2. **Check Quotas** (3 models): OpenAI + Google billing
3. **Wait** (2 models): 1-2 hours for rate limit reset
4. **Retry** (2 models): Check availability later

---

## 📊 Pass Rate Projection

- **Current**: 2/11 (18%)
- **After Config Fixes**: 4/11 (36%)
- **After All Fixes**: 9/11 (82%) - assuming quotas addressed

---

**Files Saved**:
- `MODEL_TEST_RESULTS_20260406_FINAL.json` - Complete data
- `MODEL_TEST_QUICK_REFERENCE_20260406.md` - This file
