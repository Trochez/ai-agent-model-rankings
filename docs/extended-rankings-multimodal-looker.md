# Extended Ranking: Multimodal-Looker Agent (v3.1)

Date: April 24, 2026

Provider Constraint: Only NVIDIA Build, OpenCode Zen, and OpenAI models. No OpenRouter or direct Google models.

## What's New (April 2026)

Five new models added to the rankings:
1. `openai/gpt-5.5` - Released Apr 23, 2026, newest frontier model
2. `openai/gpt-5.4-pro` - Deep reasoning variant of GPT-5.4
3. `openai/gpt-5.4-cyber` - Cybersecurity-focused variant of GPT-5.4
4. `nvidia/z-ai/glm-5v-turbo` - Vision coding model with Design2Code 94.8
5. `nvidia/google/gemma-4-31b-it` - Agentic model with coding+vision capabilities

## Multimodal-Looker Agent Ranking Table (Top 20 Models)

| Rank | Model | Provider | Score | Context | Vision | Tools | Rationale |
|------|-------|----------|-------|---------|--------|-------|-----------|
| 1 | **openai/gpt-5.5** | OpenAI | **96** | 1.05M | ✅ | ✅ | Newest frontier, best agentic vision |
| 2 | **nvidia/qwen/qwen3.5-397b-a17b** | NVIDIA Build | **95** | 128K | ✅ | ✅ | Best open VLM, MMMU-Pro 79% |
| 3 | **openai/gpt-5.4-pro** | OpenAI | **93** | 1.05M | ✅ | ✅ | Deep reasoning vision, expensive |
| 4 | **opencode/gemini-3.1-pro** | OpenCode Zen | **92** | 1M | ✅ | ✅ | Frontier vision, massive context |
| 5 | **openai/gpt-5.4** | OpenAI | **91** | 1.05M | ✅ | ✅ | Strong vision + 1M context |
| 6 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **90** | 200K | ✅ | ✅ | Top reasoning, multimodal |
| 7 | **opencode/gemini-3-flash** | OpenCode Zen | **89** | 128K | ✅ | ✅ | Fast, web-native, excellent UI |
| 8 | **nvidia/z-ai/glm-5v-turbo** | NVIDIA Build | **88** | 200K | ✅ | ✅ | Vision coding specialist, Design2Code 94.8 |
| 9 | **opencode/claude-opus-4-6** | OpenCode Zen | **87** | 200K | ✅ | ✅ | Deep reasoning + vision |
| 10 | **nvidia/meta/llama-3.2-11b-vision-instruct** | NVIDIA Build | **86** | 128K | ✅ | ✅ | Efficient, high-quality vision |
| 11 | **openai/gpt-5.4-cyber** | OpenAI | **85** | 1.05M | ✅ | ✅ | GPT-5.4 base + cyber fine-tune |
| 12 | **openai/gpt-5.4-mini** | OpenAI | **84** | 400K | ✅ | ✅ | Cost-effective, strong vision |
| 13 | **nvidia/nvidia/nemotron-nano-12b-v2-vl** | NVIDIA Build | **83** | 128K | ✅ | ✅ | Multimodal, video, OCR |
| 14 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **82** | 1M | ✅ | ✅ | MoE efficient, 1M context |
| 15 | **nvidia/meta/llama-3.2-90b-vision-instruct** | NVIDIA Build | **81** | 131K | ✅ | ✅ | Complex visual reasoning |
| 16 | **opencode/qwen3.6-plus** | OpenCode Zen | **80** | 128K | ✅ | ✅ | Versatile, good for UI |
| 17 | **nvidia/google/gemma-4-31b-it** | NVIDIA Build | **79** | 256K | ✅ | ✅ | Agentic, coding+vision |
| 18 | **nvidia/mistral-ai/mistral-small-4-119b-2603** | NVIDIA Build | **78** | 256K | ✅ | ✅ | Hybrid reasoning+vision |
| 19 | **nvidia/qwen/qwen3-vl-32b-instruct** | NVIDIA Build | **77** | 131K | ✅ | ✅ | Dedicated VL, DocVQA 96.9% |
| 20 | **openai/gpt-5.4-nano** | OpenAI | **76** | 400K | ✅ | ✅ | Fast, efficient vision |

## Tier Classification

### ♞ Tier 1: Excellent (Score 90+) - Best for Production
- `openai/gpt-5.5` (96)
- `nvidia/qwen/qwen3.5-397b-a17b` (95)
- `openai/gpt-5.4-pro` (93)
- `opencode/gemini-3.1-pro` (92)
- `openai/gpt-5.4` (91)
- `nvidia/z-ai/glm-5.1` (90)

### ♞ Tier 2: Good (Score 80-89) - Reliable Alternatives
- `opencode/gemini-3-flash` (89)
- `nvidia/z-ai/glm-5v-turbo` (88)
- `opencode/claude-opus-4-6` (87)
- `nvidia/meta/llama-3.2-11b-vision-instruct` (86)
- `openai/gpt-5.4-cyber` (85)
- `openai/gpt-5.4-mini` (84)
- `nvidia/nvidia/nemotron-nano-12b-v2-vl` (83)
- `nvidia/nvidia/nemotron-3-super-120b-a12b` (82)
- `nvidia/meta/llama-3.2-90b-vision-instruct` (81)

## Best Model by Use Case

| Use Case | Best Model | Score | Why |
|----------|------------|-------|-----|
| **General Visual Analysis** | `openai/gpt-5.5` | 96 | Newest frontier model with best agentic vision |
| **Cost-Effective Analysis** | `opencode/gemini-3-flash` | 89 | Fast, web-native, excellent for UI |
| **Large Context Analysis** | `nvidia/nvidia/nemotron-3-super-120b-a12b` | 82 | 1M context window |
| **Vision Coding** | `nvidia/z-ai/glm-5v-turbo` | 88 | Design2Code 94.8 |
| **Cybersecurity Analysis** | `openai/gpt-5.4-cyber` | 85 | Cybersecurity fine-tuned variant |

## Free vs Paid Comparison

### Best FREE Models for Multimodal-Looker
| Rank | Model | Score | Context | Notes |
|------|-------|-------|---------|-------|
| 1 | `nvidia/qwen/qwen3.5-397b-a17b` | 95 | 128K | Best free visual model |
| 2 | `nvidia/meta/llama-3.2-11b-vision-instruct` | 86 | 128K | Efficient reasoning |
| 3 | `nvidia/z-ai/glm-5.1` | 90 | 200K | Top reasoning, multimodal |
| 4 | `nvidia/meta/llama-3.2-90b-vision-instruct` | 81 | 131K | Complex reasoning |
| 5 | `nvidia/google/gemma-4-31b-it` | 79 | 256K | Agentic, coding+vision |
| 6 | `nvidia/qwen/qwen3-vl-32b-instruct` | 77 | 131K | Dedicated VL model |

### Best PAID Models for Multimodal-Looker
| Rank | Model | Score | Context | Pricing | Cost/Performance Ratio |
|------|-------|-------|---------|---------|-------------------------|
| 1 | `openai/gpt-5.5` | 96 | 1.05M | $5.00/$30.00 | 19,200 |
| 2 | `openai/gpt-5.4-pro` | 93 | 1.05M | $30.00/$180.00 | 3,100 |
| 3 | `opencode/gemini-3.1-pro` | 92 | 1M | $1.25/$10.00 | 73,600 |
| 4 | `openai/gpt-5.4` | 91 | 1.05M | $2.50/$15.00 | 36,400 |
| 5 | `opencode/claude-opus-4-6` | 87 | 200K | $15.00/$75.00 | 5,800 |
| 6 | `openai/gpt-5.4-cyber` | 85 | 1.05M | $2.50/$15.00 | 34,000 |

## Key Insights

1. **`openai/gpt-5.5`** is the clear leader for the multimodal-looker agent, with a score of 96, making it the best choice for complex visual analysis tasks.

2. **Free models** like `nvidia/qwen/qwen3.5-397b-a17b` (95) perform nearly as well as the paid models, making them excellent cost-effective alternatives.

3. **Context window size** is critical for the multimodal-looker agent, with the best models offering 1M+ token contexts.

4. **Vision coding capabilities** are increasingly important, with specialized models like `nvidia/z-ai/glm-5v-turbo` excelling in this area.

5. **Cost/Performance ratios** show that `opencode/gemini-3.1-pro` offers the best value among paid models, while `openai/gpt-5.4-pro` has the worst ratio.

6. **The multimodal-looker agent** benefits most from models with strong reasoning capabilities combined with excellent vision processing.

## Last Updated
April 24, 2026