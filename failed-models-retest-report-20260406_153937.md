# Failed Models Re-Test Report
**Date**: 2026-04-06 15:39:37.625075
**Test**: 'What is 2 + 2? Reply with ONLY the number.' → Expected: '4'
**Models Retested**: 9 (from direct-api-test-results-20260406_150732.json)

## Summary: 1/9 passed (11%)

| Model | Provider | Previous Error | Status | Time | Response |
|-------|----------|----------------|--------|------|----------|
| `openai/gpt-5.4` | openai | HTTP 429: quota exceeded... | ❌ ERROR | 872ms | N/A... |
| `qwen/qwen3.6-plus:free` | openrouter | HTTP 429: rate limit... | ❌ ERROR | 831ms | N/A... |
| `google/gemini-3.1-flash-lite-preview` | google | HTTP 503: high demand... | ✅ PASS | 1457ms | 4... |
| `google/gemini-3.1-pro-preview` | google | HTTP 429: quota exceeded... | ❌ ERROR | 839ms | N/A... |
| `meta-llama/llama-3.3-70b-instruct:free` | openrouter | HTTP 429: rate limit... | ❌ ERROR | 619ms | N/A... |
| `openai/gpt-5.3-codex` | openai | HTTP 429: quota exceeded... | ❌ ERROR | 424ms | N/A... |
| `openrouter/qwen/qwen2.5-72b-instruct` | openrouter | HTTP 400: invalid model ID... | ❌ ERROR | 260ms | N/A... |
| `openrouter/qwen/qwen3-coder:free` | openrouter | HTTP 400: invalid model ID... | ❌ ERROR | 443ms | N/A... |
| `stepfun/step-3.5-flash:free` | openrouter | null error... | ❌ ERROR | 3904ms | N/A... |