# Extended Ranking: Visual-Engineering Category

**Requirements**: Frontend, UI/UX, design, styling, animation, high reasoning

---

## Complete Ranking Table (22 Models)

| Rank | Model | Provider | Score | Context | Vision | Tools | Rationale |
|------|-------|----------|-------|---------|--------|-------|-----------|
| 1 | **openrouter/qwen/qwen2.5-vl-72b-instruct** | OpenRouter | **96** | 32K | ✅ | ✅ | Current config. Excellent for visual engineering, specialized VL model |
| 2 | **google/lyria-3-pro-preview:free** | OpenRouter | **95** | 1M | ✅ | ❌ | Best free visual model, 1M context, specialized vision |
| 3 | **opencode/gemini-3.1-pro** | OpenCode | **93** | - | ✅ | ✅ | Fallback config, strong vision, high reasoning |
| 4 | **qwen/qwen2.5-vl-72b-instruct** | OpenRouter | **93** | 32K | ✅ | ✅ | Excellent vision capabilities, good for UI work |
| 5 | **nvidia/z-ai/glm5** | NVIDIA Build | **92** | 1M+ | ✅ | ✅ | Good multimodal capabilities, 744B MoE |
| 6 | **qwen/qwen3.6-plus:free** | OpenRouter | **88** | 1M | ✅ | ✅ | Vision+tools, good for UI work, versatile |
| 7 | **meta/llama-3.2-90b-vision-instruct** | NVIDIA Build | **85** | 131K | ✅ | ✅ | Complex visual reasoning, strong for design analysis |
| 8 | **nvidia/nemotron-nano-12b-v2-vl:free** | OpenRouter | **85** | 128K | ✅ | ✅ | Multimodal with tools, video understanding, OCR |
| 9 | **google/gemma-3-27b-it:free** | OpenRouter | **80** | 131K | ✅ | ❌ | Vision capabilities, moderate reasoning, good size |
| 10 | **nvidia/cosmos-reason2-8b** | NVIDIA Build | **80** | - | ✅ | ✅ | Physical world understanding, good for UI screenshots |
| 11 | **meta/llama-3.2-11b-vision-instruct** | NVIDIA Build | **82** | 131K | ✅ | ✅ | High-quality reasoning from images, efficient |
| 12 | **google/paligemma** | NVIDIA Build | **78** | - | ✅ | ✅ | Text and visual comprehension, lightweight |
| 13 | **google/gemma-3-12b-it:free** | OpenRouter | **78** | 33K | ✅ | ❌ | Mid-size vision, good for simple visual tasks |
| 14 | **qwen/qwen3.5-397b-a17b** | NVIDIA Build | **78** | - | ✅ | ✅ | 400B MoE multimodal, powerful but slower |
| 15 | **openrouter/free** | OpenRouter | **72** | 200K | ✅ | ✅ | Auto-router, selects best free model, general purpose |
| 16 | **google/gemma-3-4b-it:free** | OpenRouter | **75** | 33K | ✅ | ❌ | Lightweight vision, good for simple tasks |
| 17 | **nvidia/nv-dinov2** | NVIDIA Build | **75** | - | ✅ | ❌ | Visual foundation model, image embeddings |
| 18 | **nvidia/nv-grounding-dino** | NVIDIA Build | **73** | - | ✅ | ❌ | Zero-shot object detection, specialized |
| 19 | **google/lyria-3-clip-preview:free** | OpenRouter | **72** | 1M | ✅ | ❌ | Vision specialist, 1M context, CLIP-based |
| 20 | **google/gemma-3n-e4b-it:free** | OpenRouter | **70** | 8K | ✅ | ❌ | Nano variant, minimal context, basic vision |
| 21 | **nvidia/nemotron-ocr-v1** | NVIDIA Build | **74** | - | ✅ | ❌ | OCR and document analysis, specialized |
| 22 | **openai/gpt-5.4** | OpenAI | **90** | 200K | ✅ | ✅ | Frontier vision, paid tier, excellent for complex UI |

---

## Tier Classification

### 🥇 Tier 1: Excellent (Score 90-100) - Best for Production

| Model | Provider | Score | Key Strength |
|-------|----------|-------|--------------|
| `openrouter/qwen/qwen2.5-vl-72b-instruct` | OpenRouter | 96 | Best overall for visual engineering |
| `google/lyria-3-pro-preview:free` | OpenRouter | 95 | Best free visual model |
| `opencode/gemini-3.1-pro` | OpenCode | 93 | Strong vision + tools |
| `qwen/qwen2.5-vl-72b-instruct` | OpenRouter | 93 | Excellent VL capabilities |
| `nvidia/z-ai/glm5` | NVIDIA Build | 92 | 744B MoE, multimodal |
| `openai/gpt-5.4` | OpenAI | 90 | Frontier vision (paid) |

### 🥈 Tier 2: Good (Score 80-89) - Reliable Alternatives

| Model | Provider | Score | Key Strength |
|-------|----------|-------|--------------|
| `qwen/qwen3.6-plus:free` | OpenRouter | 88 | Versatile, 1M context |
| `meta/llama-3.2-90b-vision-instruct` | NVIDIA Build | 85 | Complex visual reasoning |
| `nvidia/nemotron-nano-12b-v2-vl:free` | OpenRouter | 85 | Video + OCR + tools |
| `meta/llama-3.2-11b-vision-instruct` | NVIDIA Build | 82 | Efficient image reasoning |
| `google/gemma-3-27b-it:free` | OpenRouter | 80 | Good size, vision capable |
| `nvidia/cosmos-reason2-8b` | NVIDIA Build | 80 | Physical world understanding |

### 🥉 Tier 3: Acceptable (Score 70-79) - Budget Options

| Model | Provider | Score | Key Strength |
|-------|----------|-------|--------------|
| `google/paligemma` | NVIDIA Build | 78 | Lightweight, text+visual |
| `google/gemma-3-12b-it:free` | OpenRouter | 78 | Mid-size vision |
| `qwen/qwen3.5-397b-a17b` | NVIDIA Build | 78 | 400B MoE, powerful |
| `google/gemma-3-4b-it:free` | OpenRouter | 75 | Lightweight vision |
| `nvidia/nv-dinov2` | NVIDIA Build | 75 | Image embeddings |
| `nvidia/nemotron-ocr-v1` | NVIDIA Build | 74 | OCR specialist |
| `nvidia/nv-grounding-dino` | NVIDIA Build | 73 | Object detection |
| `google/lyria-3-clip-preview:free` | OpenRouter | 72 | CLIP-based vision |
| `openrouter/free` | OpenRouter | 72 | Auto-routing |

---

## Best Model by Use Case

| Use Case | Best Model | Score | Why |
|----------|------------|-------|-----|
| **UI/UX Design Analysis** | `google/lyria-3-pro-preview:free` | 95 | Best visual model, 1M context for large designs |
| **Frontend Development** | `qwen/qwen2.5-vl-72b-instruct` | 96 | Vision+tools, excellent for UI code generation |
| **Document Analysis** | `nvidia/nemotron-nano-12b-v2-vl:free` | 85 | OCR, chart reasoning, document intelligence |
| **Video Understanding** | `nvidia/nemotron-nano-12b-v2-vl:free` | 85 | Efficient Video Sampling (EVS) |
| **Screenshot Analysis** | `meta/llama-3.2-90b-vision-instruct` | 85 | Complex visual reasoning |
| **Design Mockup Review** | `opencode/gemini-3.1-pro` | 93 | Strong vision + high reasoning |
| **Quick Visual Tasks** | `google/gemma-3-12b-it:free` | 78 | Lightweight, fast |
| **Object Detection** | `nvidia/nv-grounding-dino` | 73 | Zero-shot detection specialist |
| **OCR/Text Extraction** | `nvidia/nemotron-ocr-v1` | 74 | OCR specialist |

---

## Free vs Paid Comparison

### Best FREE Models for Visual Engineering

| Rank | Model | Score | Context | Notes |
|------|-------|-------|---------|-------|
| 1 | `google/lyria-3-pro-preview:free` | 95 | 1M | **Best free visual model** |
| 2 | `qwen/qwen3.6-plus:free` | 88 | 1M | Vision+tools, versatile |
| 3 | `nvidia/nemotron-nano-12b-v2-vl:free` | 85 | 128K | Video+OCR+tools |
| 4 | `meta/llama-3.2-11b-vision-instruct` | 82 | 131K | Efficient image reasoning |
| 5 | `google/gemma-3-27b-it:free` | 80 | 131K | Good size, vision |

### Best PAID Models for Visual Engineering

| Rank | Model | Score | Context | Pricing |
|------|-------|-------|---------|---------|
| 1 | `openai/gpt-5.4` | 90 | 200K | $2.50/$15.00 per 1M tokens |
| 2 | `openai/gpt-5.4-pro` | 92 | 200K | $30.00/$180.00 per 1M tokens |

---

## Key Insights

1. **`google/lyria-3-pro-preview:free`** is the best free visual model (95/100) with 1M context
2. **`qwen/qwen2.5-vl-72b-instruct`** is the best overall for visual engineering (96/100) with vision+tools
3. **`nvidia/nemotron-nano-12b-v2-vl:free`** is the best for video/OCR tasks (85/100)
4. **NVIDIA Build** offers 10+ specialized vision models for free
5. **Free tier** has excellent options - paid models only needed for frontier-level reasoning
6. **Context matters**: 1M context models (lyria-3, qwen3.6-plus) are better for large design files

---

**Last Updated**: April 13, 2026
