# Updated Model Test Report
**Date**: 2026-04-07 00:51:31.658088
**Test**: 'What is 2 + 2? Reply with ONLY the number.' → Expected: '4'

## Summary: 3/10 passed (30%)

| Model | Provider | Source | Status | Time | Response |
|-------|----------|--------|--------|------|----------|
| `z-ai/glm-5` | openrouter | sisyphus, explore, multimodal-looker, si | ✅ PASS | 6412ms | 4... |
| `openai/gpt-5.4` | openai | hephaestus, oracle, prometheus, momus, u | ❌ ERROR | 874ms | ... |
| `opencode/qwen3.6-plus-free` | opencode | metis, atlas, visual-engineering | ❌ ERROR | 522ms | ... |
| `google/gemini-3.1-flash-lite-preview` | google | librarian, writing | ✅ PASS | 19969ms | 4... |
| `openai/gpt-5.3-codex` | openai | deep | ❌ ERROR | 738ms | ... |
| `qwen/qwen3-coder-4.08.97b-a35b-instruct` | openrouter | hephaestus fallback | ❌ ERROR | 236ms | ... |
| `stepfun-ai/step-3.5-flash` | openrouter | explore, quick fallback | ❌ ERROR | 283ms | ... |
| `nvidia/nemotron-3-nano-30b-a3b` | nvidia | multimodal-looker, visual-engineering, u | ❌ ERROR | 388ms | ... |
| `nvidia/meta/llama-3.3-70b-instruct` | nvidia | atlas, sisyphus-junior, artistry, unspec | ✅ PASS | 36292ms | 4... |
| `nvidia/meta/llama-3.2-11b-vision-instruct` | nvidia | visual-engineering fallback | ❌ ERROR | 45355ms | ... |