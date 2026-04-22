# Direct API Model Test Report
**Date**: 2026-04-06 15:07:32.523569
**Test**: 'What is 2 + 2? Reply with ONLY the number.' → Expected: '4'

## Summary: 2/11 passed (18%)

| Model | Provider | Status | Time | Response |
|-------|----------|--------|------|----------|
| `z-ai/glm-5` | openrouter | ✅ PASS | 9658ms | 4... |
| `openai/gpt-5.4` | openai | ❌ ERROR | 1828ms | ... |
| `qwen/qwen3.6-plus:free` | openrouter | ❌ ERROR | 1093ms | ... |
| `google/gemini-3.1-flash-lite-preview` | google | ❌ ERROR | 2062ms | ... |
| `google/gemini-3.1-pro-preview` | google | ❌ ERROR | 775ms | ... |
| `meta-llama/llama-3.3-70b-instruct:free` | openrouter | ❌ ERROR | 1039ms | ... |
| `openai/gpt-5.3-codex` | openai | ❌ ERROR | 1239ms | ... |
| `openrouter/qwen/qwen2.5-72b-instruct` | openrouter | ❌ ERROR | 1664ms | ... |
| `openrouter/qwen/qwen3-coder:free` | openrouter | ❌ ERROR | 921ms | ... |
| `qwen/qwen2.5-vl-72b-instruct` | openrouter | ✅ PASS | 2226ms | 4... |
| `stepfun/step-3.5-flash:free` | openrouter | ❌ ERROR | 5773ms | ... |