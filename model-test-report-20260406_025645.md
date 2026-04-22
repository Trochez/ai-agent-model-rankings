# Model Test Execution Report

**Test Date**: 2026-04-06 02:56:45.117119
**Test Prompt**: "What is 2 + 2? Reply with ONLY the number."
**Expected Response**: "4"

## Summary

- **Total Models Tested**: 12
- **Passed**: 2
- **Failed**: 10
- **Pass Rate**: 16%

## Detailed Results

| Model | Status | Response Time | Response | Pass/Fail |
|-------|--------|---------------|----------|----------|
| `nvidia/z-ai/glm5` | PASS | 21611ms | 4... | ✅ |
| `openai/gpt-5.4` | TIMEOUT | 30085ms | ... | ❌ |
| `openrouter/qwen/qwen3.6-plus:free` | PASS | 23392ms | 4... | ✅ |
| `google/gemini-3.1-flash-preview` | FAIL | 9460ms | ... | ❌ |
| `openrouter/google/lyria-3-pro-preview:free` | FAIL | 15696ms | ... | ❌ |
| `openrouter/qwen/qwen2.5-vl-72b-instruct` | TIMEOUT | 30218ms | ... | ❌ |
| `openai/gpt-5.3-codex` | TIMEOUT | 30347ms | ... | ❌ |
| `google/gemini-3.1-pro-preview` | TIMEOUT | 30262ms | ... | ❌ |
| `openrouter/qwen/qwen3-coder-plus` | FAIL | 29680ms | ... | ❌ |
| `openrouter/stepfun/step-3.5-flash:free` | TIMEOUT | 30211ms | ... | ❌ |
| `openrouter/meta-llama/llama-3.3-70b-instruct:free` | TIMEOUT | 30244ms | ... | ❌ |
| `openrouter/qwen/qwen-2.5-72b-instruct` | FAIL | 28834ms | ... | ❌ |
