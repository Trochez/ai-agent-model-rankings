# Failed Models Re-Test Report (No OpenAI)
**Date**: 2026-04-06 16:23:53.070905
**Test**: 'What is 2 + 2? Reply with ONLY the number.' → Expected: '4'
**Models Retested**: 7 (excluding OpenAI models)

## Summary: 1/7 passed (14%)

| Model | Provider | Previous Error | Status | Time | Response |
|-------|----------|----------------|--------|------|----------|
| `qwen/qwen3.6-plus:free` | openrouter | HTTP 429: rate limit... | ❌ ERROR | 3144ms | N/A... |
| `google/gemini-3.1-flash-lite-preview` | google | HTTP 503: high demand... | ✅ PASS | 2235ms | 4... |
| `google/gemini-3.1-pro-preview` | google | HTTP 429: quota exceeded... | ❌ ERROR | 1495ms | N/A... |
| `meta-llama/llama-3.3-70b-instruct:free` | openrouter | HTTP 429: rate limit... | ❌ ERROR | 1029ms | N/A... |
| `openrouter/qwen/qwen2.5-72b-instruct` | openrouter | HTTP 400: invalid model ID... | ❌ ERROR | 765ms | N/A... |
| `openrouter/qwen/qwen3-coder:free` | openrouter | HTTP 400: invalid model ID... | ❌ ERROR | 523ms | N/A... |
| `stepfun/step-3.5-flash:free` | openrouter | null error... | ❌ ERROR | 3140ms | N/A... |