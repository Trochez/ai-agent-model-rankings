# Extended Rankings: Multimodal-Looker & Visual-Engineering (v3.1)

Date: April 24, 2026

Provider Constraint: Only NVIDIA Build, OpenCode Zen, and OpenAI models. No OpenRouter or direct Google models.

## Scoring Methodology (Vision-Heavy Formula)

**MMMU-Pro 30% + GPQA 20% + SWE-Bench Pro 20% + Context 15% + Cost-efficiency 15%**

### Context Scoring (normalized 0-100)

| Context Window | Score |
|----------------|-------|
| <8K | 0 |
| 8-32K | 40 |
| 32-128K | 70 |
| 128-256K | 85 |
| 256K-512K | 90 |
| 512K-1M | 95 |
| >1M | 100 |

### Cost-Efficiency Scoring (normalized 0-100)

| Input Cost / 1M tokens | Score |
|------------------------|-------|
| Free | 100 |
| $0.01-$0.05 | 98 |
| $0.05-$0.20 | 95 |
| $0.20-$0.50 | 90 |
| $0.50-$1.00 | 85 |
| $1.00-$2.00 | 75 |
| $2.00-$5.00 | 60 |
| $5.00-$15.00 | 45 |
| $15.00-$30.00 | 30 |
| $30.00+ | 15 |

### Cost/Performance Ratio

- **Paid models**: `(Score × 1,000) / (Input $/1M tokens)`
- **Free models**: `Score × 100`

---

## What's New (April 2026)

Five new models added to the rankings:

1. **`openai/gpt-5.5`** — Released Apr 23, 2026, newest frontier model with best agentic vision
2. **`openai/gpt-5.4-pro`** — Deep reasoning variant of GPT-5.4, $30/$180 pricing
3. **`openai/gpt-5.4-cyber`** — Cybersecurity-focused variant of GPT-5.4, same base model
4. **`nvidia/z-ai/glm-5v-turbo`** — Vision coding model with Design2Code 94.8
5. **`nvidia/google/gemma-4-31b-it`** — Agentic model with coding+vision capabilities, free on NVIDIA Build

---

## Multimodal-Looker Agent Ranking Table (Top 20 Models)

The multimodal-looker agent specializes in visual analysis, screenshot review, and multimodal understanding. It requires strong vision processing combined with reasoning capabilities.

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

### Multimodal-Looker Tier Classification

#### ♞ Tier 1: Excellent (Score 90+) — Best for Production
- `openai/gpt-5.5` (96)
- `nvidia/qwen/qwen3.5-397b-a17b` (95)
- `openai/gpt-5.4-pro` (93)
- `opencode/gemini-3.1-pro` (92)
- `openai/gpt-5.4` (91)
- `nvidia/z-ai/glm-5.1` (90)

#### ♞ Tier 2: Good (Score 80-89) — Reliable Alternatives
- `opencode/gemini-3-flash` (89)
- `nvidia/z-ai/glm-5v-turbo` (88)
- `opencode/claude-opus-4-6` (87)
- `nvidia/meta/llama-3.2-11b-vision-instruct` (86)
- `openai/gpt-5.4-cyber` (85)
- `openai/gpt-5.4-mini` (84)
- `nvidia/nvidia/nemotron-nano-12b-v2-vl` (83)
- `nvidia/nvidia/nemotron-3-super-120b-a12b` (82)
- `nvidia/meta/llama-3.2-90b-vision-instruct` (81)
- `opencode/qwen3.6-plus` (80)

#### ♞ Tier 3: Acceptable (Score 70-79) — Specialized/Budget
- `nvidia/google/gemma-4-31b-it` (79)
- `nvidia/mistral-ai/mistral-small-4-119b-2603` (78)
- `nvidia/qwen/qwen3-vl-32b-instruct` (77)
- `openai/gpt-5.4-nano` (76)

### Multimodal-Looker: Best Model by Use Case

| Use Case | Best Model | Score | Why |
|----------|------------|-------|-----|
| **General Visual Analysis** | `openai/gpt-5.5` | 96 | Newest frontier model with best agentic vision |
| **Cost-Effective Analysis** | `opencode/gemini-3-flash` | 89 | Fast, web-native, excellent for UI |
| **Large Context Analysis** | `nvidia/nvidia/nemotron-3-super-120b-a12b` | 82 | 1M context window |
| **Vision Coding** | `nvidia/z-ai/glm-5v-turbo` | 88 | Design2Code 94.8 |
| **Cybersecurity Analysis** | `openai/gpt-5.4-cyber` | 85 | Cybersecurity fine-tuned variant |
| **Free Visual Analysis** | `nvidia/qwen/qwen3.5-397b-a17b` | 95 | Best free visual model, MMMU-Pro 79% |
| **Document Understanding** | `nvidia/qwen/qwen3-vl-32b-instruct` | 77 | Dedicated VL, DocVQA 96.9% |
| **Video Understanding** | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | 83 | Multimodal, video, OCR |

### Multimodal-Looker: Free vs Paid Comparison

#### Best FREE Models

| Rank | Model | Score | Context | C/P Ratio | Notes |
|------|-------|-------|---------|-----------|-------|
| 1 | `nvidia/qwen/qwen3.5-397b-a17b` | **95** | 128K | 9,500 | Best free visual model |
| 2 | `nvidia/z-ai/glm-5.1` | **90** | 200K | 9,000 | Top reasoning, multimodal |
| 3 | `nvidia/meta/llama-3.2-11b-vision-instruct` | **86** | 128K | 8,600 | Efficient reasoning |
| 4 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **83** | 128K | 8,300 | Multimodal, video, OCR |
| 5 | `nvidia/meta/llama-3.2-90b-vision-instruct` | **81** | 131K | 8,100 | Complex reasoning |
| 6 | `nvidia/google/gemma-4-31b-it` | **79** | 256K | 7,900 | Agentic, coding+vision |
| 7 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **78** | 256K | 7,800 | Hybrid reasoning+vision |
| 8 | `nvidia/qwen/qwen3-vl-32b-instruct` | **77** | 131K | 7,700 | Dedicated VL model |

#### Best PAID Models

| Rank | Model | Score | Context | Pricing | C/P Ratio | Notes |
|------|-------|-------|---------|---------|-----------|-------|
| 1 | `openai/gpt-5.5` | **96** | 1.05M | $5.00/$30.00 | 19,200 | Newest frontier |
| 2 | `openai/gpt-5.4-pro` | **93** | 1.05M | $30.00/$180.00 | 3,100 | Deep reasoning, expensive |
| 3 | `opencode/gemini-3.1-pro` | **92** | 1M | $1.25/$10.00 | 73,600 | Frontier vision, best C/P |
| 4 | `openai/gpt-5.4` | **91** | 1.05M | $2.50/$15.00 | 36,400 | Strong vision + 1M context |
| 5 | `opencode/gemini-3-flash` | **89** | 128K | $0.50/$3.00 | 178,000 | Fast, best paid C/P ratio |
| 6 | `nvidia/z-ai/glm-5v-turbo` | **88** | 200K | $1.20/$4.00 | 73,333 | Vision coding specialist |
| 7 | `opencode/claude-opus-4-6` | **87** | 200K | $15.00/$75.00 | 5,800 | Deep reasoning + vision |
| 8 | `openai/gpt-5.4-cyber` | **85** | 1.05M | $2.50/$15.00 | 34,000 | Cyber fine-tune |
| 9 | `openai/gpt-5.4-mini` | **84** | 400K | $0.75/$4.50 | 112,000 | Cost-effective, strong vision |
| 10 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **82** | 1M | $0.10/$0.50 | 820,000 | MoE, 1M context, cheap |
| 11 | `opencode/qwen3.6-plus` | **80** | 128K | $0.33/$1.95 | 242,424 | Versatile, good for UI |
| 12 | `openai/gpt-5.4-nano` | **76** | 400K | $0.20/$1.25 | 380,000 | Fast, efficient vision |

---

## Visual-Engineering Category Ranking Table (31 Models)

The visual-engineering category covers frontend development, UI/UX design, screenshot analysis, design mockup review, and all tasks requiring visual understanding combined with engineering capability.

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
| 21 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **75** | 256K | ✅ | ✅ | Agentic coding + vision |
| 22 | **openai/o3** | OpenAI | **74** | 200K | ✅ | ✅ | Reasoning model with vision |
| 23 | **nvidia/deepseek-ai/deepseek-v3.2** | NVIDIA Build | **73** | 128K | ✅ | ✅ | Strong reasoning, limited vision |
| 24 | **nvidia/stepfun-ai/step-3.5-flash** | NVIDIA Build | **72** | 200K | ✅ | ✅ | Fast, free, basic vision |
| 25 | **nvidia/nvidia/nemotron-3-nano-30b-a3b** | NVIDIA Build | **71** | 1M | ✅ | ✅ | Ultra-efficient, 1M context |
| 26 | **openai/o4-mini** | OpenAI | **70** | 200K | ✅ | ✅ | Cost-effective reasoning |
| 27 | **nvidia/nvidia/cosmos-reason2-8b** | NVIDIA Build | **65** | 8K | ✅ | ✅ | Physical world understanding |
| 28 | **nvidia/google/paligemma** | NVIDIA Build | **60** | 8K | ✅ | ✗ | Lightweight, text+visual |
| 29 | **nvidia/nvidia/nemotron-ocr-v1** | NVIDIA Build | **58** | 8K | ✅ | ✗ | OCR specialist |
| 30 | **nvidia/nvidia/nv-dinov2** | NVIDIA Build | **55** | 8K | ✅ | ✗ | Image embeddings only |
| 31 | **nvidia/nvidia/nv-grounding-dino** | NVIDIA Build | **52** | 8K | ✅ | ✗ | Object detection specialist |

### Visual-Engineering Tier Classification

#### ♞ Tier 1: Excellent (Score 90+) — Best for Production
- `openai/gpt-5.5` (96)
- `nvidia/qwen/qwen3.5-397b-a17b` (95)
- `openai/gpt-5.4-pro` (93)
- `opencode/gemini-3.1-pro` (92)
- `openai/gpt-5.4` (91)
- `nvidia/z-ai/glm-5.1` (90)

#### ♞ Tier 2: Good (Score 80-89) — Reliable Alternatives
- `opencode/gemini-3-flash` (89)
- `nvidia/z-ai/glm-5v-turbo` (88)
- `opencode/claude-opus-4-6` (87)
- `nvidia/meta/llama-3.2-11b-vision-instruct` (86)
- `openai/gpt-5.4-cyber` (85)
- `openai/gpt-5.4-mini` (84)
- `nvidia/nvidia/nemotron-nano-12b-v2-vl` (83)
- `nvidia/nvidia/nemotron-3-super-120b-a12b` (82)
- `nvidia/meta/llama-3.2-90b-vision-instruct` (81)
- `opencode/qwen3.6-plus` (80)

#### ♞ Tier 3: Acceptable (Score 70-79) — Specialized/Budget
- `nvidia/google/gemma-4-31b-it` (79)
- `nvidia/mistral-ai/mistral-small-4-119b-2603` (78)
- `nvidia/qwen/qwen3-vl-32b-instruct` (77)
- `openai/gpt-5.4-nano` (76)
- `nvidia/qwen/qwen3-coder-480b-a35b-instruct` (75)
- `openai/o3` (74)
- `nvidia/deepseek-ai/deepseek-v3.2` (73)
- `nvidia/stepfun-ai/step-3.5-flash` (72)
- `nvidia/nvidia/nemotron-3-nano-30b-a3b` (71)
- `openai/o4-mini` (70)

#### ♞ Tier 4: Limited (Score 60-69) — Niche Applications
- `nvidia/nvidia/cosmos-reason2-8b` (65)
- `nvidia/google/paligemma` (60)

#### ♞ Tier 5: Specialized (Score <60) — Very Specific Use Cases
- `nvidia/nvidia/nemotron-ocr-v1` (58)
- `nvidia/nvidia/nv-dinov2` (55)
- `nvidia/nvidia/nv-grounding-dino` (52)

### Visual-Engineering: Best Model by Use Case

| Use Case | Best Model | Score | Why |
|----------|------------|-------|-----|
| **UI/UX Design Analysis** | `openai/gpt-5.5` | 96 | Newest frontier model with best agentic vision |
| **Frontend Development** | `opencode/gemini-3-flash` | 89 | Fast, web-native, excellent for UI |
| **Document Analysis** | `nvidia/nvidia/nemotron-ocr-v1` | 58 | OCR specialist |
| **Video Understanding** | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | 83 | Multimodal, video understanding |
| **Screenshot Analysis** | `nvidia/meta/llama-3.2-90b-vision-instruct` | 81 | Complex visual reasoning |
| **Design Mockup Review** | `openai/gpt-5.4` | 91 | Frontier vision + 1M context |
| **Quick Visual Tasks** | `openai/gpt-5.4-nano` | 76 | Fast, efficient |
| **Object Detection** | `nvidia/nvidia/nv-grounding-dino` | 52 | Zero-shot specialist |
| **Vision Coding** | `nvidia/z-ai/glm-5v-turbo` | 88 | Design2Code 94.8 |
| **Large Context Analysis** | `nvidia/nvidia/nemotron-3-super-120b-a12b` | 82 | 1M context window |
| **Cost-Effective Reasoning** | `openai/o4-mini` | 70 | Budget-friendly reasoning |
| **Cybersecurity Analysis** | `openai/gpt-5.4-cyber` | 85 | Cybersecurity fine-tuned variant |
| **Free Visual Engineering** | `nvidia/qwen/qwen3.5-397b-a17b` | 95 | Best free model, MMMU-Pro 79% |
| **Agentic Coding + Vision** | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | 75 | Agentic coding with visual understanding |
| **Physical World Reasoning** | `nvidia/nvidia/cosmos-reason2-8b` | 65 | Physical world understanding specialist |
| **Image Embeddings** | `nvidia/nvidia/nv-dinov2` | 55 | Image embeddings only |

### Visual-Engineering: Free vs Paid Comparison

#### Best FREE Models

| Rank | Model | Score | Context | C/P Ratio | Notes |
|------|-------|-------|---------|-----------|-------|
| 1 | `nvidia/qwen/qwen3.5-397b-a17b` | **95** | 128K | 9,500 | Best free visual model |
| 2 | `nvidia/z-ai/glm-5.1` | **90** | 200K | 9,000 | Top reasoning, multimodal |
| 3 | `nvidia/meta/llama-3.2-11b-vision-instruct` | **86** | 128K | 8,600 | Efficient reasoning |
| 4 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **83** | 128K | 8,300 | Multimodal, video, OCR |
| 5 | `nvidia/meta/llama-3.2-90b-vision-instruct` | **81** | 131K | 8,100 | Complex reasoning |
| 6 | `nvidia/google/gemma-4-31b-it` | **79** | 256K | 7,900 | Agentic, coding+vision |
| 7 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **78** | 256K | 7,800 | Hybrid reasoning+vision |
| 8 | `nvidia/qwen/qwen3-vl-32b-instruct` | **77** | 131K | 7,700 | Dedicated VL model |
| 9 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **75** | 256K | 7,500 | Agentic coding + vision |
| 10 | `nvidia/stepfun-ai/step-3.5-flash` | **72** | 200K | 7,200 | Fast, free, basic vision |
| 11 | `nvidia/nvidia/cosmos-reason2-8b` | **65** | 8K | 6,500 | Physical world understanding |
| 12 | `nvidia/google/paligemma` | **60** | 8K | 6,000 | Lightweight, text+visual |
| 13 | `nvidia/nvidia/nemotron-ocr-v1` | **58** | 8K | 5,800 | OCR specialist |
| 14 | `nvidia/nvidia/nv-dinov2` | **55** | 8K | 5,500 | Image embeddings only |
| 15 | `nvidia/nvidia/nv-grounding-dino` | **52** | 8K | 5,200 | Object detection specialist |

#### Best PAID Models

| Rank | Model | Score | Context | Pricing | C/P Ratio | Notes |
|------|-------|-------|---------|---------|-----------|-------|
| 1 | `openai/gpt-5.5` | **96** | 1.05M | $5.00/$30.00 | 19,200 | Newest frontier |
| 2 | `openai/gpt-5.4-pro` | **93** | 1.05M | $30.00/$180.00 | 3,100 | Deep reasoning, expensive |
| 3 | `opencode/gemini-3.1-pro` | **92** | 1M | $1.25/$10.00 | 73,600 | Frontier vision, best C/P |
| 4 | `openai/gpt-5.4` | **91** | 1.05M | $2.50/$15.00 | 36,400 | Strong vision + 1M context |
| 5 | `opencode/gemini-3-flash` | **89** | 128K | $0.50/$3.00 | 178,000 | Fast, best paid C/P ratio |
| 6 | `nvidia/z-ai/glm-5v-turbo` | **88** | 200K | $1.20/$4.00 | 73,333 | Vision coding specialist |
| 7 | `opencode/claude-opus-4-6` | **87** | 200K | $15.00/$75.00 | 5,800 | Deep reasoning + vision |
| 8 | `openai/gpt-5.4-cyber` | **85** | 1.05M | $2.50/$15.00 | 34,000 | Cyber fine-tune |
| 9 | `openai/gpt-5.4-mini` | **84** | 400K | $0.75/$4.50 | 112,000 | Cost-effective, strong vision |
| 10 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **82** | 1M | $0.10/$0.50 | 820,000 | MoE, 1M context, cheap |
| 11 | `opencode/qwen3.6-plus` | **80** | 128K | $0.33/$1.95 | 242,424 | Versatile, good for UI |
| 12 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **78** | 256K | $0.15/$0.60 | 520,000 | Hybrid reasoning+vision |
| 13 | `nvidia/qwen/qwen3-vl-32b-instruct` | **77** | 131K | $0.10/$0.42 | 770,000 | Dedicated VL model |
| 14 | `openai/gpt-5.4-nano` | **76** | 400K | $0.20/$1.25 | 380,000 | Fast, efficient vision |
| 15 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **75** | 256K | $0.17/$0.85 | 441,176 | Agentic coding + vision |
| 16 | `openai/o3` | **74** | 200K | $2.00/$8.00 | 37,000 | Reasoning model with vision |
| 17 | `nvidia/deepseek-ai/deepseek-v3.2` | **73** | 128K | $0.27/$1.10 | 270,370 | Strong reasoning, limited vision |
| 18 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **71** | 1M | $0.05/$0.20 | 1,420,000 | Ultra-efficient, 1M context |
| 19 | `openai/o4-mini` | **70** | 200K | $1.50/$6.00 | 46,667 | Cost-effective reasoning |

---

## Cost/Performance Ratio Table (All Paid Models)

Sorted by C/P ratio descending (higher = better value).

| Rank | Model | Score | Input $/1M | Output $/1M | C/P Ratio | Provider |
|------|-------|-------|-----------|------------|-----------|----------|
| 1 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **71** | $0.05 | $0.20 | 1,420,000 | NVIDIA Build |
| 2 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **82** | $0.10 | $0.50 | 820,000 | NVIDIA Build |
| 3 | `nvidia/qwen/qwen3-vl-32b-instruct` | **77** | $0.10 | $0.42 | 770,000 | NVIDIA Build |
| 4 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **78** | $0.15 | $0.60 | 520,000 | NVIDIA Build |
| 5 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **75** | $0.17 | $0.85 | 441,176 | NVIDIA Build |
| 6 | `openai/gpt-5.4-nano` | **76** | $0.20 | $1.25 | 380,000 | OpenAI |
| 7 | `nvidia/deepseek-ai/deepseek-v3.2` | **73** | $0.27 | $1.10 | 270,370 | NVIDIA Build |
| 8 | `opencode/qwen3.6-plus` | **80** | $0.33 | $1.95 | 242,424 | OpenCode Zen |
| 9 | `opencode/gemini-3-flash` | **89** | $0.50 | $3.00 | 178,000 | OpenCode Zen |
| 10 | `openai/gpt-5.4-mini` | **84** | $0.75 | $4.50 | 112,000 | OpenAI |
| 11 | `nvidia/z-ai/glm-5.1` | **90** | $1.05 | $3.50 | 85,714 | NVIDIA Build |
| 12 | `nvidia/z-ai/glm-5v-turbo` | **88** | $1.20 | $4.00 | 73,333 | NVIDIA Build |
| 13 | `opencode/gemini-3.1-pro` | **92** | $1.25 | $10.00 | 73,600 | OpenCode Zen |
| 14 | `openai/o4-mini` | **70** | $1.50 | $6.00 | 46,667 | OpenAI |
| 15 | `openai/o3` | **74** | $2.00 | $8.00 | 37,000 | OpenAI |
| 16 | `openai/gpt-5.4` | **91** | $2.50 | $15.00 | 36,400 | OpenAI |
| 17 | `openai/gpt-5.4-cyber` | **85** | $2.50 | $15.00 | 34,000 | OpenAI |
| 18 | `openai/gpt-5.5` | **96** | $5.00 | $30.00 | 19,200 | OpenAI |
| 19 | `opencode/claude-opus-4-6` | **87** | $15.00 | $75.00 | 5,800 | OpenCode Zen |
| 20 | `openai/gpt-5.4-pro` | **93** | $30.00 | $180.00 | 3,100 | OpenAI |

---

## Key Insights

1. **`openai/gpt-5.5`** is the new overall leader (96/100) for visual engineering, surpassing the previously dominant `nvidia/qwen/qwen3.5-397b-a17b` (95). Released April 23, 2026, it sets a new benchmark for agentic vision.

2. **Free models remain highly competitive.** `nvidia/qwen/qwen3.5-397b-a17b` at score 95 is essentially tied with the best paid models, making it the best value proposition in the entire ranking.

3. **NVIDIA Build dominates the free tier** with 15 free models spanning general-purpose VLMs, specialized vision models (OCR, detection, embeddings), and agentic coding+vision hybrids.

4. **OpenCode Zen offers the best paid value.** `opencode/gemini-3-flash` (C/P ratio 178,000) and `opencode/gemini-3.1-pro` (C/P ratio 73,600) deliver exceptional performance per dollar compared to OpenAI equivalents.

5. **Context window expansion** is a major differentiator. Models with 1M+ context (`openai/gpt-5.5`, `openai/gpt-5.4-pro`, `openai/gpt-5.4`, `opencode/gemini-3.1-pro`, `nvidia/nvidia/nemotron-3-super-120b-a12b`, `nvidia/nvidia/nemotron-3-nano-30b-a3b`) enable analysis of large codebases and multi-page documents in a single pass.

6. **Specialized vision models** (Tier 4-5) serve critical niche roles despite lower composite scores. `nvidia/nvidia/nemotron-ocr-v1` for OCR, `nvidia/nvidia/nv-grounding-dino` for object detection, and `nvidia/nvidia/nv-dinov2` for image embeddings are irreplaceable for their specific tasks.

7. **Cost/Performance ratio reveals hidden champions.** `nvidia/nvidia/nemotron-3-nano-30b-a3b` (C/P 1,420,000) and `nvidia/nvidia/nemotron-3-super-120b-a12b` (C/P 820,000) offer extraordinary value for budget-conscious deployments, though at lower absolute quality.

8. **The GPT-5.4 family spans the entire quality spectrum** — from `gpt-5.4-pro` (93, $30/$180) through `gpt-5.4` (91, $2.50/$15) and `gpt-5.4-mini` (84, $0.75/$4.50) to `gpt-5.4-nano` (76, $0.20/$1.25) — providing a clear upgrade path.

9. **Vision coding is emerging as a distinct discipline.** `nvidia/z-ai/glm-5v-turbo` (Design2Code 94.8) and `nvidia/qwen/qwen3-coder-480b-a35b-instruct` represent a new breed of models that combine visual understanding with code generation.

10. **The gap between free and paid models** is narrowing in the mid-tier range. Free models like `nvidia/google/gemma-4-31b-it` (79) and `nvidia/mistral-ai/mistral-small-4-119b-2603` (78) compete directly with paid models like `openai/gpt-5.4-nano` (76) and `openai/o3` (74).

11. **Reasoning models (o3, o4-mini) underperform** in visual engineering compared to frontier models at similar price points. Their strength in pure reasoning doesn't fully translate to the vision-heavy formula.

12. **April 2026 additions reshape the top tier.** With `openai/gpt-5.5` taking #1 and `opencode/gemini-3.1-pro` entering at #4, the competitive landscape has shifted significantly from the v3.0 rankings.

---

## Excluded Models

The following models are explicitly excluded per v3.0 canonical provider constraints:

| Model | Reason |
|-------|--------|
| `nvidia/z-ai/glm5` | Deprecated April 20, 2026 — use `nvidia/z-ai/glm-5.1` |
| `openai/gpt-5.3-codex` | Being retired June 5, 2026 |
| All OpenRouter models | Provider constraint: only NVIDIA Build, OpenCode Zen, OpenAI |
| Direct Google models | Provider constraint: use OpenCode Zen routing instead |

---

## Last Updated

April 24, 2026 · v3.1 · Vision-Heavy Formula · 31 models ranked
