# Extended Rankings: Multimodal-Looker & Visual-Engineering — All Providers

**Date:** April 24, 2026
**Scope:** 40 models across NVIDIA Build, OpenCode Zen, OpenAI, and OpenRouter providers
**Companion to:** [oh-my-opencode-agent-rankings-all-providers.md](./oh-my-opencode-agent-rankings-all-providers.md) (v3.0 canonical)
**Categories:** multimodal-looker (agent), visual-engineering (category) — both Vision-heavy

---

## What's New (since April 21, 2026)

| Model | Provider | Notes |
|---|---|---|
| `openai/gpt-5.5` | OpenAI | Released April 23, 2026 — new #1 in both categories |
| `nvidia/qwen/qwen3.5-397b-a17b` | NVIDIA Build | New free-tier MoE, #2 performance |
| `opencode/gemini-3.1-pro` | OpenCode Zen | New Gemini 3.1 Pro endpoint |
| `opencode/gemini-3-flash` | OpenCode Zen | New Gemini 3 Flash endpoint |
| `opencode/claude-opus-4-6` | OpenCode Zen | New Claude Opus 4-6 endpoint |
| `opencode/qwen3.6-plus` | OpenCode Zen | New Qwen 3.6 Plus endpoint |
| `nvidia/z-ai/glm-5v-turbo` | NVIDIA Build | Vision-tuned GLM-5 variant |
| `nvidia/nvidia/nemotron-nano-12b-v2-vl` | NVIDIA Build | New vision nano model |
| `nvidia/google/gemma-4-31b-it` | NVIDIA Build | New Gemma 4 vision model |
| `nvidia/mistral-ai/mistral-small-4-119b-2603` | NVIDIA Build | New Mistral Small 4 |
| `nvidia/qwen/qwen3-vl-32b-instruct` | NVIDIA Build | New Qwen3 VL 32B |
| `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | NVIDIA Build | New Qwen3 Coder 480B MoE |
| `nvidia/stepfun-ai/step-3.5-flash` | NVIDIA Build | New free Step 3.5 Flash |
| `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | New Nemotron 3 Nano |
| `nvidia/nvidia/cosmos-reason2-8b` | NVIDIA Build | New Cosmos vision model |
| `nvidia/google/paligemma` | NVIDIA Build | New PaliGemma vision model |
| `nvidia/deepseek-ai/deepseek-v3.2` | NVIDIA Build | New DeepSeek V3.2 on NVIDIA |

> **Note:** `nvidia/z-ai/glm5` is DEPRECATED — use `nvidia/z-ai/glm-5.1`. `openai/gpt-5.3-codex` is being retired June 5, 2026 and is excluded.

---

## Scoring Methodology (Vision-heavy)

Both **multodal-looker** and **visual-engineering** use the Vision-heavy formula:

**Composite Score = MMMU-Pro 30% + GPQA 20% + SWE-Bench Pro 20% + Context 15% + Cost-eff 15%**

### Context Scoring (normalized 0-100)

| Context Window | Score |
|---|---|
| < 8K | 0 |
| 8K – 32K | 40 |
| 32K – 128K | 70 |
| 128K – 256K | 85 |
| 256K – 512K | 90 |
| 512K – 1M | 95 |
| > 1M | 100 |

### Cost-Efficiency Scoring (normalized 0-100)

| Input Cost / 1M tokens | Score |
|---|---|
| Free | 100 |
| $0.01 – $0.05 | 98 |
| $0.05 – $0.20 | 95 |
| $0.20 – $0.50 | 90 |
| $0.50 – $1.00 | 85 |
| $1.00 – $2.00 | 75 |
| $2.00 – $5.00 | 60 |
| $5.00 – $15.00 | 45 |
| $15.00 – $30.00 | 30 |
| $30.00+ | 15 |

### Cost/Performance Ratio

- **Paid models:** `(Performance Score × 1,000) / (Input $/1M tokens)`
- **Free models:** `Performance Score × 100`
- Higher = better value for money

---

## multimodal-looker (Vision — Vision-heavy)

### Performance Ranking — multimodal-looker (Top 25)

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free | Provider |
|---|---|---|---|---|---|---|---|
| 1 | `openai/gpt-5.5` | **96** | $5.00 | $30.00 | 1,050,000 | | OpenAI |
| 2 | `nvidia/qwen/qwen3.5-397b-a17b` | **95** | FREE | FREE | 128,000 | ✅ | NVIDIA Build |
| 3 | `openai/gpt-5.4-pro` | **93** | $30.00 | $180.00 | 1,050,000 | | OpenAI |
| 4 | `opencode/gemini-3.1-pro` | **92** | $1.25 | $10.00 | 1,048,576 | | OpenCode Zen |
| 5 | `deepseek/deepseek-v4-pro` | **92** | $1.74 | $3.48 | 1,048,576 | | OpenRouter |
| 6 | `google/gemini-2.5-pro` | **92** | $1.25 | $10.00 | 1,048,576 | | OpenRouter |
| 7 | `openai/gpt-5.4` | **91** | $2.50 | $15.00 | 1,050,000 | | OpenAI |
| 8 | `nvidia/z-ai/glm-5.1` | **90** | $1.05 | $3.50 | 202,752 | | NVIDIA Build |
| 9 | `opencode/gemini-3-flash` | **89** | $0.50 | $3.00 | 128,000 | | OpenCode Zen |
| 10 | `nvidia/z-ai/glm-5v-turbo` | **88** | $1.20 | $4.00 | 202,752 | | NVIDIA Build |
| 11 | `anthropic/claude-opus-4` | **87** | $15.00 | $75.00 | 200,000 | | OpenRouter |
| 12 | `opencode/claude-opus-4-6` | **87** | $15.00 | $75.00 | 200,000 | | OpenCode Zen |
| 13 | `nvidia/meta/llama-3.2-11b-vision-instruct` | **86** | FREE | FREE | 128,000 | ✅ | NVIDIA Build |
| 14 | `openai/gpt-5.4-cyber` | **85** | $2.50 | $15.00 | 1,050,000 | | OpenAI |
| 15 | `anthropic/claude-sonnet-4` | **85** | $3.00 | $15.00 | 1,000,000 | | OpenRouter |
| 16 | `openai/gpt-5.4-mini` | **84** | $0.75 | $4.50 | 400,000 | | OpenAI |
| 17 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **83** | FREE | FREE | 128,000 | ✅ | NVIDIA Build |
| 18 | `deepseek/deepseek-v4-flash` | **83** | $0.14 | $0.28 | 1,048,576 | | OpenRouter |
| 19 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **82** | $0.10 | $0.50 | 1,000,000 | | NVIDIA Build |
| 20 | `nvidia/meta/llama-3.2-90b-vision-instruct` | **81** | FREE | FREE | 131,072 | ✅ | NVIDIA Build |
| 21 | `qwen/qwen3-coder-plus` | **81** | $0.65 | $3.25 | 1,000,000 | | OpenRouter |
| 22 | `qwen/qwen3.6-plus` | **80** | $0.33 | $1.95 | 1,000,000 | | OpenRouter |
| 23 | `opencode/qwen3.6-plus` | **80** | $0.33 | $1.95 | 128,000 | | OpenCode Zen |
| 24 | `nvidia/google/gemma-4-31b-it` | **79** | FREE | FREE | 256,000 | ✅ | NVIDIA Build |
| 25 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **78** | $0.15 | $0.60 | 256,000 | | NVIDIA Build |

### Cost/Performance Ranking — multimodal-looker (Top 25)

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/qwen/qwen3.5-397b-a17b` | **9,500** | 95 | FREE | FREE | 128K | ✅ |
| 2 | `nvidia/meta/llama-3.2-11b-vision-instruct` | **8,600** | 86 | FREE | FREE | 128K | ✅ |
| 3 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **8,300** | 83 | FREE | FREE | 128K | ✅ |
| 4 | `nvidia/meta/llama-3.2-90b-vision-instruct` | **8,100** | 81 | FREE | FREE | 131K | ✅ |
| 5 | `nvidia/google/gemma-4-31b-it` | **7,900** | 79 | FREE | FREE | 256K | ✅ |
| 6 | `nvidia/stepfun-ai/step-3.5-flash` | **7,200** | 72 | FREE | FREE | 200K | ✅ |
| 7 | `nvidia/nvidia/cosmos-reason2-8b` | **6,500** | 65 | FREE | FREE | 8K | ✅ |
| 8 | `nvidia/google/paligemma` | **6,000** | 60 | FREE | FREE | 8K | ✅ |
| 9 | `qwen/qwen3-vl-8b-instruct` | **1,700,000** | 68 | $0.04 | $0.16 | 1M | |
| 10 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,420,000** | 71 | $0.05 | $0.20 | 1M | |
| 11 | `nvidia/qwen/qwen3-vl-32b-instruct` | **770,000** | 77 | $0.10 | $0.42 | 131K | |
| 12 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **820,000** | 82 | $0.10 | $0.50 | 1M | |
| 13 | `deepseek/deepseek-v4-flash` | **592,857** | 83 | $0.14 | $0.28 | 1M | |
| 14 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **520,000** | 78 | $0.15 | $0.60 | 256K | |
| 15 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **441,176** | 75 | $0.17 | $0.85 | 256K | |
| 16 | `qwen/qwen3.6-plus` | **242,424** | 80 | $0.33 | $1.95 | 1M | |
| 17 | `opencode/gemini-3-flash` | **178,000** | 89 | $0.50 | $3.00 | 128K | |
| 18 | `qwen/qwen3-coder-plus` | **124,615** | 81 | $0.65 | $3.25 | 1M | |
| 19 | `openai/gpt-5.4-mini` | **112,000** | 84 | $0.75 | $4.50 | 400K | |
| 20 | `nvidia/z-ai/glm-5.1` | **85,714** | 90 | $1.05 | $3.50 | 200K | |
| 21 | `nvidia/z-ai/glm-5v-turbo` | **73,333** | 88 | $1.20 | $4.00 | 200K | |
| 22 | `opencode/gemini-3.1-pro` | **73,600** | 92 | $1.25 | $10.00 | 1M | |
| 23 | `google/gemini-2.5-pro` | **73,600** | 92 | $1.25 | $10.00 | 1M | |
| 24 | `deepseek/deepseek-v4-pro` | **52,874** | 92 | $1.74 | $3.48 | 1M | |
| 25 | `openai/gpt-5.4` | **36,400** | 91 | $2.50 | $15.00 | 1M | |

---

## visual-engineering (Vision — Vision-heavy)

### Performance Ranking — visual-engineering (All 40 Models)

| Rank | Model | Perf Score | Input $/1M | Output $/1M | Context | Free | Provider |
|---|---|---|---|---|---|---|---|
| 1 | `openai/gpt-5.5` | **96** | $5.00 | $30.00 | 1,050,000 | | OpenAI |
| 2 | `nvidia/qwen/qwen3.5-397b-a17b` | **95** | FREE | FREE | 128,000 | ✅ | NVIDIA Build |
| 3 | `openai/gpt-5.4-pro` | **93** | $30.00 | $180.00 | 1,050,000 | | OpenAI |
| 4 | `opencode/gemini-3.1-pro` | **92** | $1.25 | $10.00 | 1,048,576 | | OpenCode Zen |
| 5 | `deepseek/deepseek-v4-pro` | **92** | $1.74 | $3.48 | 1,048,576 | | OpenRouter |
| 6 | `google/gemini-2.5-pro` | **92** | $1.25 | $10.00 | 1,048,576 | | OpenRouter |
| 7 | `openai/gpt-5.4` | **91** | $2.50 | $15.00 | 1,050,000 | | OpenAI |
| 8 | `nvidia/z-ai/glm-5.1` | **90** | $1.05 | $3.50 | 202,752 | | NVIDIA Build |
| 9 | `opencode/gemini-3-flash` | **89** | $0.50 | $3.00 | 128,000 | | OpenCode Zen |
| 10 | `nvidia/z-ai/glm-5v-turbo` | **88** | $1.20 | $4.00 | 202,752 | | NVIDIA Build |
| 11 | `anthropic/claude-opus-4` | **87** | $15.00 | $75.00 | 200,000 | | OpenRouter |
| 12 | `opencode/claude-opus-4-6` | **87** | $15.00 | $75.00 | 200,000 | | OpenCode Zen |
| 13 | `nvidia/meta/llama-3.2-11b-vision-instruct` | **86** | FREE | FREE | 128,000 | ✅ | NVIDIA Build |
| 14 | `openai/gpt-5.4-cyber` | **85** | $2.50 | $15.00 | 1,050,000 | | OpenAI |
| 15 | `anthropic/claude-sonnet-4` | **85** | $3.00 | $15.00 | 1,000,000 | | OpenRouter |
| 16 | `openai/gpt-5.4-mini` | **84** | $0.75 | $4.50 | 400,000 | | OpenAI |
| 17 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **83** | FREE | FREE | 128,000 | ✅ | NVIDIA Build |
| 18 | `deepseek/deepseek-v4-flash` | **83** | $0.14 | $0.28 | 1,048,576 | | OpenRouter |
| 19 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **82** | $0.10 | $0.50 | 1,000,000 | | NVIDIA Build |
| 20 | `nvidia/meta/llama-3.2-90b-vision-instruct` | **81** | FREE | FREE | 131,072 | ✅ | NVIDIA Build |
| 21 | `qwen/qwen3-coder-plus` | **81** | $0.65 | $3.25 | 1,000,000 | | OpenRouter |
| 22 | `qwen/qwen3.6-plus` | **80** | $0.33 | $1.95 | 1,000,000 | | OpenRouter |
| 23 | `opencode/qwen3.6-plus` | **80** | $0.33 | $1.95 | 128,000 | | OpenCode Zen |
| 24 | `nvidia/google/gemma-4-31b-it` | **79** | FREE | FREE | 256,000 | ✅ | NVIDIA Build |
| 25 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **78** | $0.15 | $0.60 | 256,000 | | NVIDIA Build |
| 26 | `nvidia/qwen/qwen3-vl-32b-instruct` | **77** | $0.10 | $0.42 | 131,072 | | NVIDIA Build |
| 27 | `qwen/qwen3-vl-32b-instruct` | **77** | $0.10 | $0.42 | 131,072 | | OpenRouter |
| 28 | `openai/gpt-5.4-nano` | **76** | $0.20 | $1.25 | 400,000 | | OpenAI |
| 29 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **75** | $0.17 | $0.85 | 256,000 | | NVIDIA Build |
| 30 | `openai/o3` | **74** | $2.00 | $8.00 | 200,000 | | OpenAI |
| 31 | `nvidia/deepseek-ai/deepseek-v3.2` | **73** | $0.27 | $1.10 | 128,000 | | NVIDIA Build |
| 32 | `nvidia/stepfun-ai/step-3.5-flash` | **72** | FREE | FREE | 200,000 | ✅ | NVIDIA Build |
| 33 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **71** | $0.05 | $0.20 | 1,000,000 | | NVIDIA Build |
| 34 | `openai/o4-mini` | **70** | $1.50 | $6.00 | 200,000 | | OpenAI |
| 35 | `qwen/qwen3-vl-8b-instruct` | **68** | $0.04 | $0.16 | 1,000,000 | | OpenRouter |
| 36 | `meta-llama/llama-3.2-90b-vision-instruct` | **67** | $0.35 | $0.40 | 128,000 | | OpenRouter |
| 37 | `google/gemma-3-27b-it` | **66** | $0.18 | $0.70 | 131,072 | | OpenRouter |
| 38 | `nvidia/nvidia/cosmos-reason2-8b` | **65** | FREE | FREE | 8,000 | ✅ | NVIDIA Build |
| 39 | `mistralai/mistral-small-2603` | **64** | $0.15 | $0.60 | 256,000 | | OpenRouter |
| 40 | `nvidia/google/paligemma` | **60** | FREE | FREE | 8,000 | ✅ | NVIDIA Build |

### Cost/Performance Ranking — visual-engineering (Top 25)

| Rank | Model | Cost/Perf | Perf Score | Input $/1M | Output $/1M | Context | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/qwen/qwen3.5-397b-a17b` | **9,500** | 95 | FREE | FREE | 128K | ✅ |
| 2 | `nvidia/meta/llama-3.2-11b-vision-instruct` | **8,600** | 86 | FREE | FREE | 128K | ✅ |
| 3 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **8,300** | 83 | FREE | FREE | 128K | ✅ |
| 4 | `nvidia/meta/llama-3.2-90b-vision-instruct` | **8,100** | 81 | FREE | FREE | 131K | ✅ |
| 5 | `nvidia/google/gemma-4-31b-it` | **7,900** | 79 | FREE | FREE | 256K | ✅ |
| 6 | `nvidia/stepfun-ai/step-3.5-flash` | **7,200** | 72 | FREE | FREE | 200K | ✅ |
| 7 | `nvidia/nvidia/cosmos-reason2-8b` | **6,500** | 65 | FREE | FREE | 8K | ✅ |
| 8 | `nvidia/google/paligemma` | **6,000** | 60 | FREE | FREE | 8K | ✅ |
| 9 | `qwen/qwen3-vl-8b-instruct` | **1,700,000** | 68 | $0.04 | $0.16 | 1M | |
| 10 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,420,000** | 71 | $0.05 | $0.20 | 1M | |
| 11 | `nvidia/qwen/qwen3-vl-32b-instruct` | **770,000** | 77 | $0.10 | $0.42 | 131K | |
| 12 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **820,000** | 82 | $0.10 | $0.50 | 1M | |
| 13 | `deepseek/deepseek-v4-flash` | **592,857** | 83 | $0.14 | $0.28 | 1M | |
| 14 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **520,000** | 78 | $0.15 | $0.60 | 256K | |
| 15 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **441,176** | 75 | $0.17 | $0.85 | 256K | |
| 16 | `qwen/qwen3.6-plus` | **242,424** | 80 | $0.33 | $1.95 | 1M | |
| 17 | `opencode/gemini-3-flash` | **178,000** | 89 | $0.50 | $3.00 | 128K | |
| 18 | `qwen/qwen3-coder-plus` | **124,615** | 81 | $0.65 | $3.25 | 1M | |
| 19 | `openai/gpt-5.4-mini` | **112,000** | 84 | $0.75 | $4.50 | 400K | |
| 20 | `nvidia/z-ai/glm-5.1` | **85,714** | 90 | $1.05 | $3.50 | 200K | |
| 21 | `nvidia/z-ai/glm-5v-turbo` | **73,333** | 88 | $1.20 | $4.00 | 200K | |
| 22 | `opencode/gemini-3.1-pro` | **73,600** | 92 | $1.25 | $10.00 | 1M | |
| 23 | `google/gemini-2.5-pro` | **73,600** | 92 | $1.25 | $10.00 | 1M | |
| 24 | `deepseek/deepseek-v4-pro` | **52,874** | 92 | $1.74 | $3.48 | 1M | |
| 25 | `openai/gpt-5.4` | **36,400** | 91 | $2.50 | $15.00 | 1M | |

---

## Summary: Best Model per Provider (Performance)

| Provider | Best Model | Perf Score | Cost | Context |
|---|---|---|---|---|
| **OpenAI** | `openai/gpt-5.5` | **96** | $5.00/$30.00 | 1,050,000 |
| **NVIDIA Build** | `nvidia/qwen/qwen3.5-397b-a17b` | **95** | FREE | 128,000 |
| **OpenCode Zen** | `opencode/gemini-3.1-pro` | **92** | $1.25/$10.00 | 1,048,576 |
| **OpenRouter** | `deepseek/deepseek-v4-pro` | **92** | $1.74/$3.48 | 1,048,576 |

## Summary: Best Value per Provider (Cost/Performance)

| Provider | Best Value Model | Cost/Perf | Perf Score | Cost |
|---|---|---|---|---|
| **NVIDIA Build** | `nvidia/qwen/qwen3.5-397b-a17b` | **9,500** | 95 | FREE |
| **OpenRouter** | `qwen/qwen3-vl-8b-instruct` | **1,700,000** | 68 | $0.04/$0.16 |
| **OpenCode Zen** | `opencode/gemini-3-flash` | **178,000** | 89 | $0.50/$3.00 |
| **OpenAI** | `openai/gpt-5.4-mini` | **112,000** | 84 | $0.75/$4.50 |

---

## Key Insights

1. **GPT-5.5 takes the crown** — Released April 23, 2026, `openai/gpt-5.5` scores **96** and leads both categories by a clear margin. Its 1M+ context window and strong MMMU-Pro performance make it the top vision model, though at $5/$30 per 1M tokens it's a premium choice.

2. **Free vision models are remarkably strong** — `nvidia/qwen/qwen3.5-397b-a17b` scores **95** for FREE, making it the best value in the entire ranking. NVIDIA Build's free tier dominates the cost/performance table with 8 of the top 8 positions.

3. **NVIDIA Build dominates value** — All 8 free models in the cost/perf top 8 are from NVIDIA Build. The paid NVIDIA models also offer strong ratios: `nvidia/nvidia/nemotron-3-super-120b-a12b` at **820,000** cost/perf for just $0.10/$0.50.

4. **OpenCode Zen offers the best mid-tier balance** — `opencode/gemini-3-flash` at **89** performance and **178,000** cost/perf hits the sweet spot for production visual-engineering workloads where reliability matters.

5. **Vision-specialized models outperform generalists** — Models with explicit vision support (GLM-5v-turbo, Llama 3.2 Vision, Nemotron Nano VL, Gemma 4, Qwen3-VL) consistently outscore similarly-priced general-purpose models in this category.

6. **Context window is a major differentiator** — The 15% context weight heavily favors models with 1M+ context (GPT-5.5, GPT-5.4 family, Gemini, DeepSeek V4). Models limited to 8K context (cosmos-reason2-8b, paligemma) pay a steep penalty despite being free.

7. **OpenRouter adds critical diversity** — OpenRouter provides access to `deepseek/deepseek-v4-pro` (**92** at $1.74), `google/gemini-2.5-pro` (**92** at $1.25), and `anthropic/claude-sonnet-4` (**85** at $3.00) — models not available on NVIDIA Build or OpenCode Zen.

8. **The 80+ performance tier is crowded** — 23 models score 80 or above, giving teams abundant choices across every price point. The key decision factor becomes provider preference and context window needs rather than raw capability.

9. **Small vision models struggle** — Models below 12B parameters (cosmos-reason2-8b, paligemma, qwen3-vl-8b) score 60-68, making them suitable only for simple visual tasks or as fallback options.

10. **GPT-5.4-cyber is a niche option** — Scoring **85** at the same price as GPT-5.4 (**91**), the cyber variant trades vision performance for security specialization — only useful for security-focused visual analysis.

---

## Related Documents

- [Oh-My-OpenCode Agent Rankings v3.0](./oh-my-opencode-agent-rankings.md) — NVIDIA Build + OpenCode Zen + OpenAI (canonical)
- [Oh-My-OpenCode Agent Rankings — All Providers](./oh-my-opencode-agent-rankings-all-providers.md) — Full 353-model ranking
- [Oh-My-OpenCode Agent Rankings — OpenAI Only](./oh-my-opencode-agent-rankings-openai-only.md) — OpenAI deep dive
- [Extended Rankings: Visual Engineering (pre-v3.0)](./extended-rankings-visual-engineering.md) — Historical
- [Extended Rankings: Multimodal Looker (pre-v3.0)](./extended-rankings-multimodal-looker.md) — Historical

---

**Last Updated:** April 24, 2026
