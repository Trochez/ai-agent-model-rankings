# Direct API Model Test Report
**Date**: 2026-04-07 00:34:48.231886
**Test**: 'What is 2 + 2? Reply with ONLY the number.' → Expected: '4'

## Summary: 2/11 passed (18%)

| Model | Provider | Status | Time | Response |
|-------|----------|--------|------|----------|
| `z-ai/glm-5` | openrouter | ❌ ERROR | 3963ms | ... |
| `openai/gpt-5.4` | openai | ❌ ERROR | 820ms | ... |
| `qwen/qwen3.6-plus:free` | openrouter | ❌ ERROR | 2847ms | ... |
| `google/gemini-3.1-flash-lite-preview` | google | ✅ PASS | 1472ms | 4... |
| `google/gemini-3.1-pro-preview` | google | ❌ ERROR | 984ms | ... |
| `meta-llama/llama-3.3-70b-instruct:free` | openrouter | ❌ ERROR | 1672ms | ... |
| `openai/gpt-5.3-codex` | openai | ❌ ERROR | 826ms | ... |
| `openrouter/qwen/qwen2.5-72b-instruct` | openrouter | ❌ ERROR | 247ms | ... |
| `openrouter/qwen/qwen3-coder:free` | openrouter | ❌ ERROR | 285ms | ... |
| `qwen/qwen2.5-vl-72b-instruct` | openrouter | ✅ PASS | 1377ms | 4... |
| `stepfun/step-3.5-flash:free` | openrouter | ❌ ERROR | 6266ms | ... |