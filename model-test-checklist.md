# Model Test Checklist for oh-my-opencode.json

**Purpose**: Validate that all models (primary + fallback) respond correctly to simple prompts  
**Created**: 2026-04-06  
**Config File**: `/home/trocha/.config/opencode/oh-my-opencode.json`

---

## Test Methodology

Each model should be tested with a **simple, unambiguous prompt** that:
1. Requires basic reasoning (not just pattern matching)
2. Has a clear, verifiable correct answer
3. Tests the model's ability to follow instructions
4. Completes within reasonable time (< 30 seconds)

### Universal Test Prompt
```
"What is 2 + 2? Reply with ONLY the number, no explanation."
```

**Expected Response**: `4`  
**Validation**: Response contains the digit "4" and nothing else (or minimal extra text)

---

## Model Inventory

### Primary Models (Agents)

| Agent | Model | Category | Test Status |
|-------|-------|----------|-------------|
| sisyphus | `z-ai/glm-5` | orchestrator | ⬜ Pending |
| hephaestus | `openai/gpt-5.4` | executor | ⬜ Pending |
| prometheus | `openai/gpt-5.4` | planner | ⬜ Pending |
| oracle | `openai/gpt-5.4` | consultant | ⬜ Pending |
| explore | `z-ai/glm-5` | search | ⬜ Pending |
| metis | `qwen/qwen3.6-plus:free` | analyst | ⬜ Pending |
| momus | `openai/gpt-5.4` | reviewer | ⬜ Pending |
| librarian | `google/gemini-3.1-flash-preview` | research | ⬜ Pending |
| multimodal-looker | `google/lyria-3-pro-preview:free` | visual | ⬜ Pending |
| atlas | `qwen/qwen3.6-plus:free` | knowledge | ⬜ Pending |
| sisyphus-junior | `z-ai/glm-5` | orchestrator-junior | ⬜ Pending |

### Category Models

| Category | Model | Test Status |
|----------|-------|-------------|
| visual-engineering | `qwen/qwen2.5-vl-72b-instruct` | ⬜ Pending |
| ultrabrain | `openai/gpt-5.4` | ⬜ Pending |
| deep | `openai/gpt-5.3-codex` | ⬜ Pending |
| artistry | `google/gemini-3.1-pro-preview` | ⬜ Pending |
| quick | `z-ai/glm-5` | ⬜ Pending |
| unspecified-low | `z-ai/glm-5` | ⬜ Pending |
| unspecified-high | `z-ai/glm-5` | ⬜ Pending |
| writing | `google/gemini-3.1-flash-preview` | ⬜ Pending |

---

## Fallback Models (Unique)

All fallback models across agents and categories:

| Model | Used By | Test Status |
|-------|---------|-------------|
| `openai/gpt-5.4` | sisyphus, metis, momus, ultrabrain, deep, unspecified-high | ⬜ Pending |
| `qwen/qwen3.6-plus:free` | sisyphus, oracle, prometheus, metis, momus, explore, atlas, sisyphus-junior, quick, unspecified-low, unspecified-high | ⬜ Pending |
| `z-ai/glm-5` | hephaestus, oracle, prometheus, metis, momus, librarian, multimodal-looker, atlas, sisyphus-junior, ultrabrain, deep, artistry, quick, unspecified-low, unspecified-high | ⬜ Pending |
| `qwen/qwen3-coder-plus` | hephaestus | ⬜ Pending |
| `stepfun/step-3.5-flash:free` | explore, quick | ⬜ Pending |
| `qwen/qwen2.5-vl-72b-instruct` | multimodal-looker, visual-engineering, artistry | ⬜ Pending |
| `meta-llama/llama-3.3-70b-instruct:free` | atlas, sisyphus-junior, unspecified-low | ⬜ Pending |
| `google/lyria-3-pro-preview:free` | visual-engineering | ⬜ Pending |
| `google/gemini-3.1-pro-preview` | visual-engineering, artistry | ⬜ Pending |
| `openai/gpt-5.3-codex` | deep | ⬜ Pending |
| `qwen/qwen-2.5-72b-instruct` | writing | ⬜ Pending |

---

## Unique Models to Test (Master List)

**Total Unique Models**: 13

### 1. `z-ai/glm-5`
- **Provider**: NVIDIA/OpenRouter
- **Type**: Primary orchestrator model
- **Used in**: sisyphus, explore, sisyphus-junior, quick, unspecified-low, unspecified-high
- **Fallback for**: hephaestus, oracle, prometheus, metis, momus, librarian, multimodal-looker, atlas, ultrabrain, deep, artistry
- **Test Prompt**: Universal test
- **Status**: ⬜ Pending

### 2. `openai/gpt-5.4`
- **Provider**: OpenAI
- **Type**: High-reasoning model
- **Used in**: hephaestus, prometheus, oracle, momus, ultrabrain
- **Fallback for**: sisyphus, metis, unspecified-high, deep
- **Test Prompt**: Universal test
- **Status**: ⬜ Pending

### 3. `qwen/qwen3.6-plus:free`
- **Provider**: OpenRouter (free tier)
- **Type**: General-purpose model
- **Used in**: metis, atlas
- **Fallback for**: sisyphus, oracle, prometheus, momus, explore, sisyphus-junior, quick, unspecified-low, unspecified-high
- **Test Prompt**: Universal test
- **Status**: ⬜ Pending

### 4. `google/gemini-3.1-flash-preview`
- **Provider**: Google
- **Type**: Fast response model
- **Used in**: librarian, writing
- **Fallback for**: None
- **Test Prompt**: Universal test
- **Status**: ⬜ Pending

### 5. `google/lyria-3-pro-preview:free`
- **Provider**: Google (free tier)
- **Type**: Visual/multimodal model
- **Used in**: multimodal-looker
- **Fallback for**: visual-engineering
- **Test Prompt**: Universal test (or visual variant)
- **Status**: ⬜ Pending

### 6. `qwen/qwen2.5-vl-72b-instruct`
- **Provider**: OpenRouter
- **Type**: Vision-language model
- **Used in**: visual-engineering
- **Fallback for**: multimodal-looker, artistry
- **Test Prompt**: Universal test (or visual variant)
- **Status**: ⬜ Pending

### 7. `openai/gpt-5.3-codex`
- **Provider**: OpenAI
- **Type**: Code-specialized model
- **Used in**: deep
- **Fallback for**: None
- **Test Prompt**: Universal test (or code variant)
- **Status**: ⬜ Pending

### 8. `google/gemini-3.1-pro-preview`
- **Provider**: Google
- **Type**: Pro-tier reasoning model
- **Used in**: artistry
- **Fallback for**: visual-engineering
- **Test Prompt**: Universal test
- **Status**: ⬜ Pending

### 9. `qwen/qwen3-coder-plus`
- **Provider**: OpenRouter
- **Type**: Code-specialized model
- **Used in**: None (fallback only)
- **Fallback for**: hephaestus
- **Test Prompt**: Universal test (or code variant)
- **Status**: ⬜ Pending

### 10. `stepfun/step-3.5-flash:free`
- **Provider**: OpenRouter (free tier)
- **Type**: Fast response model
- **Used in**: None (fallback only)
- **Fallback for**: explore, quick
- **Test Prompt**: Universal test
- **Status**: ⬜ Pending

### 11. `meta-llama/llama-3.3-70b-instruct:free`
- **Provider**: OpenRouter (free tier)
- **Type**: Large language model
- **Used in**: None (fallback only)
- **Fallback for**: atlas, sisyphus-junior, unspecified-low
- **Test Prompt**: Universal test
- **Status**: ⬜ Pending

### 12. `qwen/qwen-2.5-72b-instruct`
- **Provider**: OpenRouter
- **Type**: General-purpose model
- **Used in**: None (fallback only)
- **Fallback for**: writing
- **Test Prompt**: Universal test
- **Status**: ⬜ Pending

### 13. `google/gemini-3.1-pro-preview` (duplicate - see #8)

---

## Test Execution Checklist

### Pre-Test Setup
- [ ] Verify API keys are configured for all providers
- [ ] Check network connectivity to model endpoints
- [ ] Ensure rate limits won't be exceeded
- [ ] Prepare logging/measurement tools

### Test Execution Template

For each model, execute:

```bash
# Test command template (adjust based on your testing framework)
test_model --model "<model_id>" --prompt "What is 2 + 2? Reply with ONLY the number, no explanation."
```

**Record**:
- Response time
- Response content
- Whether response contains "4"
- Any errors or timeouts
- Token usage (if available)

### Test Cases

#### Test Case 1: Basic Arithmetic (Universal)
**Prompt**: "What is 2 + 2? Reply with ONLY the number, no explanation."  
**Expected**: Response contains "4"  
**Models**: All 13 unique models

#### Test Case 2: Instruction Following
**Prompt**: "List three colors. Use a numbered list."  
**Expected**: Numbered list with 3 color names  
**Models**: All 13 unique models

#### Test Case 3: Simple Logic
**Prompt**: "If it's raining, I need an umbrella. It's raining. Do I need an umbrella? Answer yes or no."  
**Expected**: "yes"  
**Models**: All 13 unique models

#### Test Case 4: Code Understanding (Code Models Only)
**Prompt**: "What does this code output? ```python\nprint(3 * 4)\n```"  
**Expected**: "12"  
**Models**: `qwen/qwen3-coder-plus`, `openai/gpt-5.3-codex`

#### Test Case 5: Visual Understanding (Vision Models Only)
**Prompt**: "Describe what you see in this image: [simple image of a red circle]"  
**Expected**: Mentions "red" and "circle"  
**Models**: `qwen/qwen2.5-vl-72b-instruct`, `google/lyria-3-pro-preview:free`

---

## Test Results Template

### Model: `z-ai/glm-5`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `openai/gpt-5.4`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `qwen/qwen3.6-plus:free`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `google/gemini-3.1-flash-preview`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `google/lyria-3-pro-preview:free`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `qwen/qwen2.5-vl-72b-instruct`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `openai/gpt-5.3-codex`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 4 (Code)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `google/gemini-3.1-pro-preview`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `qwen/qwen3-coder-plus`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 4 (Code)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `stepfun/step-3.5-flash:free`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `meta-llama/llama-3.3-70b-instruct:free`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

### Model: `qwen/qwen-2.5-72b-instruct`
- **Test 1 (Arithmetic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 2 (Instructions)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Test 3 (Logic)**: ⬜ Pass / ⬜ Fail
- Response: `[paste response]`
- Time: `[ms]`
- **Notes**: `[any observations]`

---

## Failure Classification

### Failure Types
1. **No Response**: Model endpoint unreachable or timeout
2. **Wrong Answer**: Model provides incorrect response
3. **Format Violation**: Model doesn't follow instruction format
4. **Rate Limited**: Too many requests to provider
5. **Auth Error**: Invalid API key or credentials
6. **Model Not Found**: Model ID incorrect or deprecated

### Failure Handling
- **Primary model fails**: Document failure, test fallback chain
- **Fallback model fails**: Document failure, mark as critical
- **All models in chain fail**: Escalate to configuration review

---

## Summary Statistics

**Total Unique Models**: 13
**Primary Models**: 11
**Fallback-Only Models**: 2
**Models Tested**: 0/13
**Models Passed**: 0/13
**Models Failed**: 0/13

**Test Execution Status**: ⚠️ **API KEYS REQUIRED**

To execute tests, you need to provide API keys for the following providers:

1. **OpenRouter** (for 8 models):
   - `z-ai/glm-5`
   - `qwen/qwen3.6-plus:free`
   - `qwen/qwen2.5-vl-72b-instruct`
   - `qwen/qwen3-coder-plus`
   - `stepfun/step-3.5-flash:free`
   - `meta-llama/llama-3.3-70b-instruct:free`
   - `qwen/qwen-2.5-72b-instruct`
   - `google/lyria-3-pro-preview:free`

2. **OpenAI** (for 2 models):
   - `openai/gpt-5.4`
   - `openai/gpt-5.3-codex`

3. **Google** (for 2 models):
   - `google/gemini-3.1-flash-preview`
   - `google/gemini-3.1-pro-preview`

### How to Run Tests

**Option 1: Set Environment Variables**
```bash
export OPENROUTER_API_KEY='your-key-here'
export OPENAI_API_KEY='your-key-here'
export GOOGLE_API_KEY='your-key-here'
python3 test_models.py
```

**Option 2: Interactive Mode**
```bash
python3 test_models_interactive.py
```

**Option 3: Use Test Script**
```bash
export OPENROUTER_API_KEY='your-key-here'
./run_model_tests.sh
```

---

## Next Steps

1. [x] Set up testing environment with API access
2. [ ] Execute Test Case 1 for all 13 models
3. [ ] Record results in Test Results Template
4. [ ] Execute Test Cases 2-5 for applicable models
5. [ ] Analyze failures and classify by type
6. [ ] Update configuration if models are deprecated
7. [x] Create automated test script for future validation

### Test Scripts Created

- **`test_models.py`**: Automated test script (requires API keys in environment)
- **`test_models_interactive.py`**: Interactive test script (prompts for API keys)
- **`run_model_tests.sh`**: Bash wrapper script for running tests
- **`model-test-results.json`**: JSON output file (generated after test execution)
- **`model-test-report.md`**: Markdown report (generated after test execution)

---

## Appendix: Model Provider Information

### OpenRouter Models
- `z-ai/glm-5`
- `qwen/qwen3.6-plus:free`
- `qwen/qwen3-coder-plus`
- `qwen/qwen2.5-vl-72b-instruct`
- `qwen/qwen-2.5-72b-instruct`
- `stepfun/step-3.5-flash:free`
- `meta-llama/llama-3.3-70b-instruct:free`

### OpenAI Models
- `openai/gpt-5.4`
- `openai/gpt-5.3-codex`

### Google Models
- `google/gemini-3.1-flash-preview`
- `google/gemini-3.1-pro-preview`
- `google/lyria-3-pro-preview:free`

---

**Last Updated**: 2026-04-06  
**Maintainer**: oh-my-opencode testing team
