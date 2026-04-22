# Extended Ranking: Writing Category (v3.0)

Date: April 21, 2026

Provider Constraint: Only NVIDIA Build, OpenCode Zen, and OpenAI models. No OpenRouter or direct Google models.

**Requirements**: Documentation, prose, technical writing, minimal reasoning — efficiency preferred over frontier capability.

---

## Complete Ranking Table (15 Models)

| Rank | Model | Provider | Score | Context | Vision | Tools | Rationale |
|------|-------|----------|-------|---------|--------|-------|-----------|
| 1 | **opencode/gemini-3-flash** | OpenCode Zen | **98** | 128K | ✅ | ✅ | Web-native, fast, #1 for writing |
| 2 | **nvidia/stepfun-ai/step-3.5-flash** | NVIDIA Build | **96** | 200K | ❌ | ✅ | Fast, FREE, great for quick docs |
| 3 | **nvidia/nvidia/nemotron-3-nano-30b-a3b** | NVIDIA Build | **94** | 1M | ❌ | ✅ | 1M ctx, $0.05/$0.20, efficient |
| 4 | **openai/gpt-5.4-mini** | OpenAI | **91** | 400K | ✅ | ✅ | Cost-effective, good for docs |
| 5 | **opencode/qwen3.6-plus** | OpenCode Zen | **90** | 128K | ✅ | ✅ | Versatile writing, 1M context |
| 6 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **90** | 1M | ❌ | ✅ | Long-form writing, 1M ctx |
| 7 | **openai/gpt-5.4-nano** | OpenAI | **89** | 400K | ✅ | ✅ | Fast writing, $0.20/$1.25 |
| 8 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **88** | 200K | ✅ | ✅ | Technical docs, high reasoning |
| 9 | **openai/gpt-5.4** | OpenAI | **87** | 1.05M | ✅ | ✅ | Technical reports, 1.05M ctx |
| 10 | **nvidia/nvidia/nvidia-nemotron-nano-9b-v2** | NVIDIA Build | **86** | 128K | ❌ | ✅ | Edge/quick writing |
| 11 | **opencode/qwen3-coder** | OpenCode Zen | **85** | 128K | ❌ | ✅ | Code documentation |
| 12 | **nvidia/google/gemma-4-31b-it** | NVIDIA Build | **84** | 256K | ❌ | ✅ | Lightweight writing |
| 13 | **openai/o4-mini** | OpenAI | **83** | 200K | ❌ | ✅ | Cost-effective reasoning |
| 14 | **nvidia/minimaxai/minimax-m2.7** | NVIDIA Build | **82** | 128K | ❌ | ✅ | Office productivity writing |
| 15 | **nvidia/meta/llama-3.3-70b-instruct** | NVIDIA Build | **80** | 128K | ❌ | ✅ | General purpose, multilingual |

---

## Tier Classification

### Tier 1: Excellent (Score 90-100) - Best for Writing

| Model | Provider | Score | Key Strength |
|-------|----------|-------|--------------|
| `opencode/gemini-3-flash` | OpenCode Zen | 98 | Fast, web-native, #1 for writing |
| `nvidia/stepfun-ai/step-3.5-flash` | NVIDIA Build | 96 | Fast, FREE, quick docs |
| `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | 94 | 1M ctx, efficient |
| `openai/gpt-5.4-mini` | OpenAI | 91 | Cost-effective, good for docs |
| `opencode/qwen3.6-plus` | OpenCode Zen | 90 | Versatile, 1M context |
| `nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Build | 90 | Long-form, 1M ctx |

### Tier 2: Good (Score 80-89) - Reliable Alternatives

| Model | Provider | Score | Key Strength |
|-------|----------|-------|--------------|
| `openai/gpt-5.4-nano` | OpenAI | 89 | Fast writing |
| `nvidia/z-ai/glm-5.1` | NVIDIA Build | 88 | Technical docs |
| `openai/gpt-5.4` | OpenAI | 87 | Technical reports |
| `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | NVIDIA Build | 86 | Edge/quick |
| `opencode/qwen3-coder` | OpenCode Zen | 85 | Code documentation |
| `nvidia/google/gemma-4-31b-it` | NVIDIA Build | 84 | Lightweight |
| `openai/o4-mini` | OpenAI | 83 | Cost-effective reasoning |
| `nvidia/minimaxai/minimax-m2.7` | NVIDIA Build | 82 | Office productivity |
| `nvidia/meta/llama-3.3-70b-instruct` | NVIDIA Build | 80 | Multilingual |

---

## Best Model by Use Case

| Use Case | Best Model | Score | Why |
|----------|------------|-------|-----|
| **Technical Documentation** | `opencode/gemini-3-flash` | 98 | Fast, web-native, optimized |
| **Quick Documentation** | `nvidia/stepfun-ai/step-3.5-flash` | 96 | Fast, FREE |
| **Long-Form Writing** | `nvidia/nvidia/nemotron-3-super-120b-a12b` | 90 | 1M context |
| **Code Documentation** | `opencode/qwen3-coder` | 85 | Specialized for code |
| **Cost-Effective Writing** | `openai/gpt-5.4-mini` | 91 | Good for docs, $0.75/$4.50 |
| **Fast Writing** | `openai/gpt-5.4-nano` | 89 | Fast, $0.20/$1.25 |
| **Technical Reports** | `openai/gpt-5.4` | 87 | 1.05M ctx, frontier |
| **Multilingual Writing** | `nvidia/meta/llama-3.3-70b-instruct` | 80 | Multilingual support |
| **Simple Writing Tasks** | `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | 86 | Edge/quick |

---

## Free vs Paid Comparison

### Best FREE Models for Writing

| Rank | Model | Score | Context | Notes |
|------|-------|-------|---------|-------|
| 1 | `opencode/gemini-3-flash` | 98 | 128K | **Best overall for writing** |
| 2 | `nvidia/stepfun-ai/step-3.5-flash` | 96 | 200K | Fast, FREE |
| 3 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | 94 | 1M | Efficient, 1M ctx |
| 4 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | 90 | 1M | Long-form |
| 5 | `nvidia/z-ai/glm-5.1` | 88 | 200K | Technical docs |
| 6 | `nvidia/google/gemma-4-31b-it` | 84 | 256K | Lightweight |

### Best PAID Models for Writing

| Rank | Model | Score | Context | Pricing |
|------|-------|-------|---------|---------|
| 1 | `openai/gpt-5.4-mini` | 91 | 400K | $0.75/$4.50 per 1M tokens |
| 2 | `openai/gpt-5.4-nano` | 89 | 400K | $0.20/$1.25 per 1M tokens |
| 3 | `openai/gpt-5.4` | 87 | 1.05M | $2.50/$15.00 per 1M tokens |

---

## Key Insights

1. **`opencode/gemini-3-flash`** is the top choice for writing (98/100) — fast, web-native, optimized for documentation
2. **`nvidia/stepfun-ai/step-3.5-flash`** is the best free NVIDIA Build option (96/100) — fast and FREE
3. **`nvidia/nvidia/nemotron-3-nano-30b-a3b`** offers 1M context for long documents (94/100) at $0.05/$0.20
4. **Writing category requires minimal reasoning** — efficient models preferred over frontier models
5. **Free tier has excellent options** — paid models only needed for specialized technical writing
6. **NVIDIA Build dominates the free tier** with multiple efficient writing-capable models

---

**Last Updated**: April 21, 2026
