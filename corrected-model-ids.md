# Corrected Model IDs - Quick Reference

**Generated**: April 6, 2026
**Source**: Investigation of failed models from test execution

---

## Models Requiring ID Correction

### 1. Qwen 2.5 72B Instruct

| Field | Value |
|-------|-------|
| **Incorrect ID** | `openrouter/qwen/qwen2.5-72b-instruct` |
| **Correct ID** | `qwen/qwen-2.5-72b-instruct` |
| **Provider** | OpenRouter |
| **Context** | 32,768 tokens |
| **Released** | Sep 19, 2024 |
| **Pricing** | $0.12/M input, $0.39/M output |
| **Issue** | Extra `openrouter/` prefix + wrong hyphenation (`qwen2.5` → `qwen-2.5`) |

---

### 2. Qwen 3 Coder (Free)

| Field | Value |
|-------|-------|
| **Incorrect ID** | `openrouter/qwen/qwen3-coder:free` |
| **Correct ID** | `qwen/qwen3-coder:free` |
| **Provider** | OpenRouter |
| **Context** | 262,000 tokens |
| **Released** | Jul 23, 2025 |
| **Pricing** | FREE |
| **Issue** | Extra `openrouter/` prefix |

---

## Models with Correct IDs (Rate Limited)

These models have correct IDs but are temporarily failing due to rate limits:

### 3. Qwen 3.6 Plus (Free)

| Field | Value |
|-------|-------|
| **Model ID** | `qwen/qwen3.6-plus:free` ✅ |
| **Status** | CORRECT ID |
| **Error** | HTTP 429 - Rate limit |
| **Context** | 1M tokens |
| **Released** | Apr 2, 2026 |
| **Pricing** | FREE |
| **Action** | Wait for daily reset (200 req/day limit) |

---

### 4. Meta Llama 3.3 70B (Free)

| Field | Value |
|-------|-------|
| **Model ID** | `meta-llama/llama-3.3-70b-instruct:free` ✅ |
| **Status** | CORRECT ID |
| **Error** | HTTP 429 - Rate limit |
| **Context** | 65,536 tokens |
| **Released** | Dec 6, 2024 |
| **Pricing** | FREE |
| **Action** | Wait for daily reset |

---

### 5. Google Gemini 3.1 Flash Lite

| Field | Value |
|-------|-------|
| **Model ID** | `google/gemini-3.1-flash-lite-preview` ✅ |
| **Status** | CORRECT ID - WORKING |
| **Error** | None (previously HTTP 503, now resolved) |
| **Context** | 1M tokens |
| **Generation** | Gemini 3.1 |
| **Pricing** | FREE tier available |
| **Action** | None - model is passing tests |

---

### 6. Google Gemini 3.1 Pro

| Field | Value |
|-------|-------|
| **Model ID** | `google/gemini-3.1-pro-preview` ✅ |
| **Status** | CORRECT ID |
| **Error** | HTTP 429 - Quota exceeded |
| **Context** | 1M tokens |
| **Generation** | Gemini 3.1 |
| **Pricing** | Requires billing setup |
| **Action** | Set up Google AI Studio billing |

---

### 7. StepFun Step 3.5 Flash (Free)

| Field | Value |
|-------|-------|
| **Model ID** | `stepfun/step-3.5-flash:free` ✅ |
| **Status** | CORRECT ID |
| **Error** | Timeout (3904ms, null error) |
| **Context** | 256,000 tokens |
| **Released** | Jan 29, 2026 |
| **Architecture** | MoE (196B total, 11B active) |
| **Pricing** | FREE |
| **Action** | Increase timeout or retry |

---

## Configuration Update Script

```bash
# Update oh-my-opencode.json or similar config file

# BEFORE (incorrect):
# "openrouter/qwen/qwen2.5-72b-instruct"
# "openrouter/qwen/qwen3-coder:free"

# AFTER (correct):
# "qwen/qwen-2.5-72b-instruct"
# "qwen/qwen3-coder:free"
```

---

## Key Learnings

1. **OpenRouter ID Format**: Never prefix with `openrouter/`
   - ✅ Correct: `qwen/model-name`
   - ❌ Wrong: `openrouter/qwen/model-name`

2. **Hyphenation Matters**: 
   - ✅ Correct: `qwen-2.5` (hyphenated)
   - ❌ Wrong: `qwen2.5` (no hyphen)

3. **Free Tier Suffix**: Use `:free` for free variants
   - Example: `qwen/qwen3-coder:free`

4. **Google Gemini Generation**: Current is **3.1**, not 2.0 or 1.5
   - `gemini-3.1-pro`
   - `gemini-3.1-flash`

---

## Test Results Summary

| Model | Previous Status | New Status | Change |
|-------|----------------|------------|--------|
| `google/gemini-3.1-flash-lite-preview` | HTTP 503 | ✅ PASS | **FIXED** |
| `qwen/qwen3.6-plus:free` | HTTP 429 | HTTP 429 | Still rate limited |
| `meta-llama/llama-3.3-70b-instruct:free` | HTTP 429 | HTTP 429 | Still rate limited |
| `google/gemini-3.1-pro-preview` | HTTP 429 | HTTP 429 | Quota issue |
| `openrouter/qwen/qwen2.5-72b-instruct` | HTTP 400 | - | **NEEDS FIX** |
| `openrouter/qwen/qwen3-coder:free` | HTTP 400 | - | **NEEDS FIX** |
| `stepfun/step-3.5-flash:free` | Null error | HTTP 429/timeout | Provider issue |

---

## Next Steps

1. ✅ Update configuration files with correct model IDs
2. ⏳ Wait for OpenRouter rate limit reset (daily)
3. 💳 Set up Google AI Studio billing for Gemini Pro
4. 🔧 Increase timeout for StepFun Step 3.5 Flash
5. 🧪 Re-run tests after fixes
