# Extended Ranking: Visual-Engineering Category (v3.0)

Date: April 21, 2026

Provider Constraint: Only NVIDIA Build, OpenCode Zen, and OpenAI models. No OpenRouter or direct Google models.

## Complete Ranking Table (15 Models)
| Rank | Model | Provider | Score | Context | Vision | Tools | Rationale |
|------|-------|----------|-------|---------|--------|-------|-----------|
| 1 | **nvidia/qwen/qwen3.5-397b-a17b** | NVIDIA Build | **99** | 128K | ✅ | ✅ | Frontier VLM, best overall for visual engineering |
| 2 | **nvidia/meta/llama-3.2-11b-vision-instruct** | NVIDIA Build | **95** | 128K | ✅ | ✅ | Efficient, high-quality reasoning |
| 3 | **nvidia/nvidia/nemotron-nano-12b-v2-vl** | NVIDIA Build | **92** | 128K | ✅ | ✅ | Multimodal, video understanding, OCR |
| 4 | **opencode/gemini-3-flash** | OpenCode Zen | **90** | 128K | ✅ | ✅ | Fast, web-native, excellent for UI |
| 5 | **openai/gpt-5.4** | OpenAI | **90** | 1.05M | ✅ | ✅ | Frontier vision, massive context |
| 6 | **nvidia/meta/llama-3.2-90b-vision-instruct** | NVIDIA Build | **88** | 131K | ✅ | ✅ | Complex visual reasoning |
| 7 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **88** | 1M+ | ✅ | ✅ | High-reasoning, multimodal |
| 8 | **openai/gpt-5.4-mini** | OpenAI | **86** | 400K | ✅ | ✅ | Cost-effective, strong vision |
| 9 | **opencode/qwen3.6-plus** | OpenCode Zen | **85** | 128K | ✅ | ✅ | Versatile, good for UI work |
| 10 | **openai/gpt-5.4-nano** | OpenAI | **82** | 400K | ✅ | ✅ | Fast, efficient vision |
| 11 | **nvidia/nvidia/cosmos-reason2-8b** | NVIDIA Build | **80** | - | ✅ | ✅ | Physical world understanding |
| 12 | **nvidia/google/paligemma** | NVIDIA Build | **78** | - | ✅ | ✅ | Lightweight, text+visual |
| 13 | **nvidia/nvidia/nv-dinov2** | NVIDIA Build | **75** | - | ✅ | ✗ | Image embeddings |
| 14 | **nvidia/nvidia/nemotron-ocr-v1** | NVIDIA Build | **74** | - | ✅ | ✗ | OCR specialist |
| 15 | **nvidia/nvidia/nv-grounding-dino** | NVIDIA Build | **73** | - | ✅ | ✗ | Object detection specialist |

## Tier Classification

### ♞ Tier 1: Excellent (Score 90-100) - Best for Production
- `nvidia/qwen/qwen3.5-397b-a17b` (99)
- `nvidia/meta/llama-3.2-11b-vision-instruct` (95)
- `nvidia/nvidia/nemotron-nano-12b-v2-vl` (92)
- `opencode/gemini-3-flash` (90)
- `openai/gpt-5.4` (90)

### ♞ Tier 2: Good (Score 80-89) - Reliable Alternatives
- `nvidia/meta/llama-3.2-90b-vision-instruct` (88)
- `nvidia/z-ai/glm-5.1` (88)
- `openai/gpt-5.4-mini` (86)
- `opencode/qwen3.6-plus` (85)
- `openai/gpt-5.4-nano` (82)
- `nvidia/nvidia/cosmos-reason2-8b` (80)

### ♞ Tier 3: Acceptable (Score 70-79) - Specialized/Budget
- `nvidia/google/paligemma` (78)
- `nvidia/nvidia/nv-dinov2` (75)
- `nvidia/nvidia/nemotron-ocr-v1` (74)
- `nvidia/nvidia/nv-grounding-dino` (73)

## Best Model by Use Case

| Use Case | Best Model | Score | Why |
|----------|------------|-------|-----|
| **UI/UX Design Analysis** | `nvidia/qwen/qwen3.5-397b-a17b` | 99 | Best overall VLM |
| **Frontend Development** | `opencode/gemini-3-flash` | 90 | Fast, web-native |
| **Document Analysis** | `nvidia/nvidia/nemotron-ocr-v1` | 74 | OCR specialist |
| **Video Understanding** | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | 92 | Efficient video sampling |
| **Screenshot Analysis** | `nvidia/meta/llama-3.2-90b-vision-instruct` | 88 | Complex visual reasoning |
| **Design Mockup Review** | `openai/gpt-5.4` | 90 | Frontier vision |
| **Quick Visual Tasks** | `openai/gpt-5.4-nano` | 82 | Fast, efficient |
| **Object Detection** | `nvidia/nvidia/nv-grounding-dino` | 73 | Zero-shot specialist |

## Free vs Paid Comparison

### Best FREE Models for Visual Engineering
| Rank | Model | Score | Context | Notes |
|------|-------|-------|---------|-------|
| 1 | `nvidia/qwen/qwen3.5-397b-a17b` | 99 | 128K | Best free visual model |
| 2 | `nvidia/meta/llama-3.2-11b-vision-instruct` | 95 | 128K | Efficient reasoning |
| 3 | `opencode/gemini-3-flash` | 90 | 128K | Fast, web-native |
| 4 | `nvidia/meta/llama-3.2-90b-vision-instruct` | 88 | 131K | Complex reasoning |

### Best PAID Models for Visual Engineering
| Rank | Model | Score | Context | Pricing |
|------|-------|-------|---------|---------|
| 1 | `openai/gpt-5.4` | 90 | 1.05M | $2.50/$15.00 |
| 2 | `openai/gpt-5.4-mini` | 86 | 400K | $0.75/$4.50 |
| 3 | `openai/gpt-5.4-nano` | 82 | 400K | $0.20/$1.25 |

## Key Insights
1. **`nvidia/qwen/qwen3.5-397b-a17b`** is the undisputed leader (99/100) for visual engineering.
2. **NVIDIA Build** provides the most specialized vision models (OCR, detection, embeddings).
3. **OpenAI models** are essential for massive context (1M+) and frontier-level reasoning.
4. **OpenCode Zen** offers the best balance of speed and cost for web-native tasks.
5. **Free tier** is highly capable; paid models are only necessary for extreme context or frontier reasoning.

## Last Updated
April 21, 2026