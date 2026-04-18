# Extended Ranking: Writing Category

**Requirements**: Documentation, prose, technical writing, minimal reasoning

---

## Complete Ranking Table (20 Models)

| Rank | Model | Provider | Score | Context | Vision | Tools | Rationale |
|------|-------|----------|-------|---------|--------|-------|-----------|
| 1 | **opencode/gemini-3-flash** | OpenCode | **92** | - | ✅ | ✅ | Current config. Fast, good for writing, web-native |
| 2 | **qwen/qwen-2.5-72b-instruct** | OpenRouter | **90** | 131K | ❌ | ✅ | Fallback config, good for prose, excellent language generation |
| 3 | **google/gemini-3.1-flash-lite-preview** | OpenRouter | **90** | - | ✅ | ✅ | Fast, good for documentation, generous limits |
| 4 | **meta-llama/llama-3.3-70b-instruct:free** | OpenRouter | **88** | 66K | ❌ | ✅ | Fallback config, good writing, multilingual |
| 5 | **openai/gpt-5.4-mini** | OpenAI | **88** | 200K | ✅ | ✅ | Fast, good for documentation (paid) |
| 6 | **qwen/qwen3.6-plus:free** | OpenRouter | **85** | 1M | ✅ | ✅ | Good for documentation, versatile, 1M context |
| 7 | **nvidia/z-ai/glm5** | NVIDIA Build | **85** | 1M+ | ✅ | ✅ | Good for technical documentation, 744B MoE |
| 8 | **openai/gpt-5.4** | OpenAI | **85** | 200K | ✅ | ✅ | Excellent for technical writing (paid) |
| 9 | **google/gemma-3-27b-it:free** | OpenRouter | **82** | 131K | ✅ | ❌ | Good for technical writing, vision capable |
| 10 | **qwen/qwen3-coder:free** | OpenRouter | **82** | 262K | ❌ | ✅ | Good for code documentation, 480B MoE |
| 11 | **stepfun/step-3.5-flash:free** | OpenRouter | **80** | 256K | ❌ | ✅ | Fast, good for quick documentation |
| 12 | **nvidia/nemotron-3-super-120b-a12b:free** | OpenRouter | **78** | 262K | ❌ | ✅ | Good for long-form documentation, 1M context available |
| 13 | **openrouter/free** | OpenRouter | **78** | 200K | ✅ | ✅ | General purpose, good for writing, auto-routing |
| 14 | **minimax/minimax-m2.5:free** | OpenRouter | **77** | 197K | ❌ | ✅ | Good for office productivity writing |
| 15 | **nousresearch/hermes-3-llama-3.1-405b:free** | OpenRouter | **76** | 131K | ❌ | ❌ | Large model, good for prose |
| 16 | **arcee-ai/trinity-large-preview:free** | OpenRouter | **75** | 131K | ❌ | ✅ | 400B MoE, good for documentation |
| 17 | **google/gemma-3-12b-it:free** | OpenRouter | **75** | 33K | ✅ | ❌ | Mid-size, good for simple writing tasks |
| 18 | **z-ai/glm-4.5-air:free** | OpenRouter | **74** | 131K | ❌ | ✅ | MoE with thinking modes, good for technical writing |
| 19 | **liquid/lfm-2.5-1.2b-instruct:free** | OpenRouter | **72** | 33K | ❌ | ❌ | Lightweight, good for simple prose |
| 20 | **google/gemma-3-4b-it:free** | OpenRouter | **70** | 33K | ✅ | ❌ | Lightweight vision, basic writing |

---

## Tier Classification

### 🥇 Tier 1: Excellent (Score 90-100) - Best for Writing

| Model | Provider | Score | Key Strength |
|-------|----------|-------|--------------|
| `opencode/gemini-3-flash` | OpenCode | 92 | Fast, web-native, optimized for writing |
| `qwen/qwen-2.5-72b-instruct` | OpenRouter | 90 | Excellent prose generation |
| `google/gemini-3.1-flash-lite-preview` | OpenRouter | 90 | Fast, generous limits |

### 🥈 Tier 2: Good (Score 80-89) - Reliable Alternatives

| Model | Provider | Score | Key Strength |
|-------|----------|-------|--------------|
| `meta-llama/llama-3.3-70b-instruct:free` | OpenRouter | 88 | Multilingual, good writing |
| `openai/gpt-5.4-mini` | OpenAI | 88 | Fast, good for docs (paid) |
| `qwen/qwen3.6-plus:free` | OpenRouter | 85 | Versatile, 1M context |
| `nvidia/z-ai/glm5` | NVIDIA Build | 85 | 744B MoE, technical docs |
| `openai/gpt-5.4` | OpenAI | 85 | Excellent technical writing (paid) |
| `google/gemma-3-27b-it:free` | OpenRouter | 82 | Technical writing, vision |
| `qwen/qwen3-coder:free` | OpenRouter | 82 | Code documentation |
| `stepfun/step-3.5-flash:free` | OpenRouter | 80 | Quick documentation |

### 🥉 Tier 3: Acceptable (Score 70-79) - Budget Options

| Model | Provider | Score | Key Strength |
|-------|----------|-------|--------------|
| `nvidia/nemotron-3-super-120b-a12b:free` | OpenRouter | 78 | Long-form docs |
| `openrouter/free` | OpenRouter | 78 | Auto-routing |
| `minimax/minimax-m2.5:free` | OpenRouter | 77 | Office productivity |
| `nousresearch/hermes-3-llama-3.1-405b:free` | OpenRouter | 76 | Large model, prose |
| `arcee-ai/trinity-large-preview:free` | OpenRouter | 75 | 400B MoE |
| `google/gemma-3-12b-it:free` | OpenRouter | 75 | Mid-size |
| `z-ai/glm-4.5-air:free` | OpenRouter | 74 | Thinking modes |
| `liquid/lfm-2.5-1.2b-instruct:free` | OpenRouter | 72 | Lightweight prose |
| `google/gemma-3-4b-it:free` | OpenRouter | 70 | Basic writing |

---

## Best Model by Use Case

| Use Case | Best Model | Score | Why |
|----------|------------|-------|-----|
| **Technical Documentation** | `opencode/gemini-3-flash` | 92 | Fast, web-native, optimized |
| **Prose/Creative Writing** | `qwen/qwen-2.5-72b-instruct` | 90 | Excellent language generation |
| **Code Documentation** | `qwen/qwen3-coder:free` | 82 | Specialized for code |
| **Long-Form Writing** | `qwen/qwen3.6-plus:free` | 85 | 1M context |
| **Multilingual Writing** | `meta-llama/llama-3.3-70b-instruct:free` | 88 | Multilingual support |
| **Quick Documentation** | `stepfun/step-3.5-flash:free` | 80 | Fast, efficient |
| **Technical Reports** | `nvidia/z-ai/glm5` | 85 | 744B MoE, high quality |
| **Simple Writing Tasks** | `google/gemma-3-12b-it:free` | 75 | Lightweight, efficient |

---

## Free vs Paid Comparison

### Best FREE Models for Writing

| Rank | Model | Score | Context | Notes |
|------|-------|-------|---------|-------|
| 1 | `meta-llama/llama-3.3-70b-instruct:free` | 88 | 66K | **Best free for writing** |
| 2 | `google/gemini-3.1-flash-lite-preview` | 90 | - | Fast, generous limits |
| 3 | `qwen/qwen3.6-plus:free` | 85 | 1M | Versatile, long context |
| 4 | `google/gemma-3-27b-it:free` | 82 | 131K | Technical writing |
| 5 | `qwen/qwen3-coder:free` | 82 | 262K | Code documentation |

### Best PAID Models for Writing

| Rank | Model | Score | Context | Pricing |
|------|-------|-------|---------|---------|
| 1 | `openai/gpt-5.4-mini` | 88 | 200K | $0.75/$4.50 per 1M tokens |
| 2 | `openai/gpt-5.4` | 85 | 200K | $2.50/$15.00 per 1M tokens |

---

## Key Insights

1. **`opencode/gemini-3-flash`** is the top choice for writing (92/100) - fast and web-native
2. **`meta-llama/llama-3.3-70b-instruct:free`** is the best free option (88/100) - multilingual
3. **`qwen/qwen-2.5-72b-instruct`** excels at prose (90/100) - excellent language generation
4. **`qwen/qwen3.6-plus:free`** offers 1M context for long-form writing (85/100)
5. **Writing category requires minimal reasoning** - efficient models preferred over frontier models
6. **Free tier has excellent options** - paid models only needed for specialized technical writing

---

**Last Updated**: April 13, 2026
