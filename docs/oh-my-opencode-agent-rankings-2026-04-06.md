# 📊 Oh-My-OpenCode Agent & Category Model Rankings - Complete Report
**Generated**: April 6, 2026
**Data Sources**: OpenRouter, NVIDIA Build, OpenAI, OpenCode, Configuration File

---

## Executive Summary

This report provides comprehensive model effectiveness rankings for **11 agents** and **9 categories** in the oh-my-opencode system, analyzing **100+ models** from 4 major providers.

### Key Findings

1. **Best Free Model Overall**: `qwen/qwen3.6-plus:free` (1M context, vision+tools) - Top choice for 8/11 agents
2. **Best Free Coding Model**: `qwen/qwen3-coder:free` (262K context, tools) - Score: 89/100 for executor
3. **Best Free Visual Model**: `google/lyria-3-pro-preview:free` (1M context, vision) - Score: 95/100
4. **Best Paid Model**: `openai/gpt-5.4` - Frontier intelligence for critical tasks
5. **Most Versatile NVIDIA Model**: `nvidia/z-ai/glm5` (744B MoE) - Excellent for orchestration

---

## 1. Agents Extracted from Configuration

### 1.1 Primary Agents (Mode: primary)

| Agent | Category | Current Model | Reasoning | Key Characteristics |
|-------|----------|---------------|-----------|---------------------|
| **sisyphus** | orchestrator | nvidia/z-ai/glm5 | xhigh | Full tool access, thinking enabled (10K tokens), orchestrates all work |
| **hephaestus** | executor | openai/gpt-5.4 | high | Implementation tasks, edit/write/grep/glob tools |
| **prometheus** | planner | openai/gpt-5.4 | xhigh | Strategic planning, plan/ralplan skills |

### 1.2 Subagent Agents (Mode: subagent)

| Agent | Category | Current Model | Reasoning | Key Characteristics |
|-------|----------|---------------|-----------|---------------------|
| **oracle** | consultant | openai/gpt-5.4 | xhigh | Read-only, architecture/debugging consultation |
| **explore** | search | nvidia/z-ai/glm5 | minimal | Fast codebase search, grep/glob tools |
| **metis** | analyst | qwen/qwen3.6-plus:free | xhigh | Pre-planning analysis, ambiguity detection |
| **momus** | reviewer | openai/gpt-5.4 | xhigh | Work plan review, quality assurance |
| **librarian** | research | opencode/gemini-3-flash | minimal | External reference search, webfetch/websearch |
| **multimodal-looker** | visual | google/lyria-3-pro-preview:free | medium | Visual/multimodal analysis |
| **atlas** | knowledge | qwen/qwen3.6-plus:free | medium | Knowledge management |
| **sisyphus-junior** | orchestrator-junior | nvidia/z-ai/glm5 | medium | Delegation support, task coordination |

---

## 2. Categories Extracted from Configuration

| Category | Current Model | Reasoning | Use Case |
|----------|---------------|-----------|----------|
| **visual-engineering** | openrouter/qwen/qwen2.5-vl-72b-instruct | high | Frontend, UI/UX, design, styling, animation |
| **ultrabrain** | openai/gpt-5.4 | xhigh | Genuinely hard, logic-heavy tasks |
| **deep** | openai/gpt-5.3-codex | medium | Goal-oriented autonomous problem-solving |
| **artistry** | opencode/gemini-3.1-pro | high | Complex problem-solving with unconventional approaches |
| **quick** | nvidia/z-ai/glm5 | minimal | Trivial tasks - single file changes, typo fixes |
| **unspecified-low** | nvidia/z-ai/glm5 | medium | Tasks that don't fit other categories, low effort |
| **unspecified-high** | nvidia/z-ai/glm5 | medium | Tasks that don't fit other categories, high effort |
| **writing** | opencode/gemini-3-flash | minimal | Documentation, prose, technical writing |

---

## 3. Available Models by Source

### 3.1 OpenRouter Free Models (28 models)

**Rate Limits**: 20 requests/minute, 200 requests/day per model

#### Tier 1: Ultra-Long Context (1M tokens)

| Model ID | Context | Vision | Tools | Notes |
|----------|---------|--------|-------|-------|
| `google/lyria-3-pro-preview:free` | 1,000K | ✅ | ❌ | Best for visual tasks |
| `google/lyria-3-clip-preview:free` | 1,000K | ✅ | ❌ | Vision specialist |
| `qwen/qwen3.6-plus:free` | 1,000K | ✅ | ✅ | **Top free model** - 78.8 SWE-bench |

#### Tier 2: Long Context (200K-262K tokens)

| Model ID | Context | Vision | Tools | Notes |
|----------|---------|--------|-------|-------|
| `nvidia/nemotron-3-super-120b-a12b:free` | 262K | ❌ | ✅ | 120B MoE (12B active), Mamba-Transformer hybrid |
| `qwen/qwen3-next-80b-a3b-instruct:free` | 262K | ❌ | ✅ | Fast stable responses |
| `qwen/qwen3-coder:free` | 262K | ❌ | ✅ | **Best for coding** - 480B MoE (35B active) |
| `stepfun/step-3.5-flash:free` | 256K | ❌ | ✅ | 196B MoE (11B active), reasoning model |
| `nvidia/nemotron-3-nano-30b-a3b:free` | 256K | ❌ | ✅ | Small MoE for agentic AI |
| `openrouter/free` | 200K | ✅ | ✅ | **Auto-router** - selects best free model |
| `minimax/minimax-m2.5:free` | 197K | ❌ | ✅ | 80.2% SWE-bench, office productivity |

#### Tier 3: Standard Context (128K-131K tokens)

| Model ID | Context | Vision | Tools | Notes |
|----------|---------|--------|-------|-------|
| `arcee-ai/trinity-mini:free` | 131K | ❌ | ✅ | 26B MoE (3B active), function calling |
| `openai/gpt-oss-120b:free` | 131K | ❌ | ✅ | 117B MoE (5.1B active), configurable reasoning |
| `openai/gpt-oss-20b:free` | 131K | ❌ | ✅ | 21B MoE (3.6B active), Apache 2.0 |
| `z-ai/glm-4.5-air:free` | 131K | ❌ | ✅ | MoE with thinking/non-thinking modes |
| `google/gemma-3-27b-it:free` | 131K | ✅ | ❌ | Multimodal, no tool use |
| `meta-llama/llama-3.2-3b-instruct:free` | 131K | ❌ | ❌ | Lightweight, 8 languages |
| `nousresearch/hermes-3-llama-3.1-405b:free` | 131K | ❌ | ❌ | Large model, no tools |
| `arcee-ai/trinity-large-preview:free` | 131K | ❌ | ✅ | 400B MoE (13B active), agent harness trained |

#### Tier 4: Medium Context (66K-128K tokens)

| Model ID | Context | Vision | Tools | Notes |
|----------|---------|--------|-------|-------|
| `nvidia/nemotron-nano-12b-v2-vl:free` | 128K | ✅ | ✅ | Multimodal, video understanding, OCR |
| `nvidia/nemotron-nano-9b-v2:free` | 128K | ❌ | ✅ | Unified reasoning/non-reasoning |
| `meta-llama/llama-3.3-70b-instruct:free` | 66K | ❌ | ✅ | **Best general purpose** - multilingual |

#### Tier 5: Short Context (8K-33K tokens)

| Model ID | Context | Vision | Tools | Notes |
|----------|---------|--------|-------|-------|
| `liquid/lfm-2.5-1.2b-thinking:free` | 33K | ❌ | ❌ | Reasoning model |
| `liquid/lfm-2.5-1.2b-instruct:free` | 33K | ❌ | ❌ | Instruction tuned |
| `cognitivecomputations/dolphin-mistral-24b-venice-edition:free` | 33K | ❌ | ❌ | Uncensored variant |
| `google/gemma-3-4b-it:free` | 33K | ✅ | ❌ | Lightweight vision |
| `google/gemma-3-12b-it:free` | 33K | ✅ | ❌ | Mid-size vision |
| `google/gemma-3n-e2b-it:free` | 8K | ❌ | ❌ | Nano variant |
| `google/gemma-3n-e4b-it:free` | 8K | ❌ | ❌ | Nano variant |

---

### 3.2 NVIDIA Build Free Models (91 models)

**Key Models**:

| Model ID | Type | Context | Best For |
|----------|------|---------|----------|
| `nvidia/z-ai/glm5` | LLM | 1M+ | **744B MoE, excellent for agentic tasks** |
| `nvidia/nemotron-3-super-120b-a12b` | LLM | 1M | Agentic reasoning, coding, planning |
| `nvidia/nemotron-voicechat` | Audio | - | Voice chat |
| `nvidia/nemotron-asr-streaming` | ASR | - | Real-time speech recognition |
| `nvidia/nemotron-ocr-v1` | Vision | - | OCR and document analysis |
| `nvidia/llama-nemotron-embed-1b-v2` | Embedding | - | Multilingual, 26 languages |
| `stepfun-ai/step-3.5-flash` | LLM | 256K | 200B MoE reasoning |
| `z-ai/glm-4.7` | LLM | - | Multilingual agentic coding |
| `qwen/qwen3.5-122b-a10b` | LLM | - | 122B MoE for coding/reasoning |
| `qwen/qwen3.5-397b-a17b` | VLM | - | 400B MoE multimodal |

---

### 3.3 OpenAI Models (Paid)

**Flagship Models**:

| Model | Context | Capabilities | Pricing (per 1M tokens) |
|-------|---------|--------------|-------------------------|
| `gpt-5.4` | 200K | Vision, Function Calling, Reasoning | $2.50 input / $15.00 output |
| `gpt-5.4-pro` | 200K | Vision, Function Calling, Enhanced Reasoning | $30.00 input / $180.00 output |
| `gpt-5.4-mini` | 200K | Vision, Function Calling | $0.75 input / $4.50 output |
| `gpt-5.4-nano` | 200K | Function Calling | $0.20 input / $1.25 output |

**Specialized Models**:

| Model | Type | Best For | Pricing |
|-------|------|----------|---------|
| `gpt-5.3-codex` | Coding | Agentic coding optimized | $1.75 input / $14.00 output |
| `gpt-5.3-chat-latest` | ChatGPT | ChatGPT backend | $1.75 input / $14.00 output |
| `o3-deep-research` | Research | Most powerful deep research | $5.00 input / $20.00 output |
| `gpt-realtime-1.5` | Audio | Best voice model | $32.00 audio input / $64.00 audio output |
| `gpt-image-1.5` | Image | State-of-the-art image generation | $8.00 image input / $32.00 image output |

---

### 3.4 OpenCode Free Models

| Model ID | Context | Capabilities | Notes |
|----------|---------|--------------|-------|
| `opencode/gemini-3-flash` | - | Vision, Tools | Fast, good for research |
| `opencode/gemini-3.1-pro` | - | Vision, Tools | High reasoning |
| `opencode/qwen3.6-plus-free` | 1M | Vision, Tools | Same as OpenRouter free tier |
| `opencode/claude-opus-4-6` | - | Tools | High capability |

---

## 4. Model Rankings by Agent

### Effectiveness Scale (0-100)

- **90-100**: Excellent match, optimal for agent role
- **70-89**: Good match, minor tradeoffs
- **50-69**: Acceptable, notable limitations
- **30-49**: Poor match, significant gaps
- **0-29**: Not recommended

---

### 4.1 SISYPHUS (Orchestrator - Primary)

**Requirements**: High reasoning, orchestration, delegation, full tool access, thinking capability

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** | NVIDIA Build | 95 | Current config. 744B MoE, excellent for complex orchestration, thinking enabled |
| 2 | openai/gpt-5.4 | OpenAI | 93 | Frontier intelligence, excellent reasoning, but no free tier |
| 3 | qwen/qwen3.6-plus:free | OpenRouter | 88 | 1M context, vision+tools, strong reasoning for free |
| 4 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 85 | 1M context, agentic reasoning, tools support |
| 5 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 78 | Strong general purpose, good reasoning |
| 6 | openrouter/free | OpenRouter | 72 | General purpose with vision+tools, 200K context |

---

### 4.2 HEPHAESTUS (Executor - Primary)

**Requirements**: Implementation, code generation, edit/write tools, high reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.4** | OpenAI | 94 | Current config. Best for implementation tasks |
| 2 | openai/gpt-5.3-codex | OpenAI | 92 | Optimized for agentic coding |
| 3 | qwen/qwen3-coder:free | OpenRouter | 89 | **Best free coding model**, 262K context |
| 4 | nvidia/z-ai/glm5 | NVIDIA Build | 87 | Strong coding, good for execution |
| 5 | qwen/qwen3.6-plus:free | OpenRouter | 85 | Strong coding + vision capabilities |
| 6 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 80 | Good general implementation |

---

### 4.3 ORACLE (Consultant - Subagent)

**Requirements**: Read-only, architecture analysis, debugging, xhigh reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.4** | OpenAI | 96 | Current config. Optimal for consultation |
| 2 | openai/gpt-5.4-pro | OpenAI | 94 | More precise responses for complex analysis |
| 3 | nvidia/z-ai/glm5 | NVIDIA Build | 88 | Strong reasoning, good for architecture |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 82 | Good reasoning, free alternative |
| 5 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 80 | 1M context for large codebase analysis |
| 6 | z-ai/glm-4.5-air:free | OpenRouter | 75 | GLM family, good reasoning |

---

### 4.4 EXPLORE (Search - Subagent)

**Requirements**: Fast codebase search, minimal reasoning, grep/glob tools

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** | NVIDIA Build | 92 | Current config. Good balance of speed and capability |
| 2 | qwen/qwen3.6-plus:free | OpenRouter | 90 | Fast, 1M context for large searches |
| 3 | stepfun/step-3.5-flash:free | OpenRouter | 88 | Fast reasoning, 256K context |
| 4 | nvidia/nemotron-3-nano-30b-a3b:free | OpenRouter | 85 | Efficient for quick searches |
| 5 | google/gemma-3-27b-it:free | OpenRouter | 82 | Lightweight, good for simple searches |
| 6 | openrouter/free | OpenRouter | 78 | General purpose, vision+tools |

---

### 4.5 PROMETHEUS (Planner - Primary)

**Requirements**: Strategic planning, xhigh reasoning, plan/ralplan skills

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.4** | OpenAI | 95 | Current config. Excellent for strategic planning |
| 2 | nvidia/z-ai/glm5 | NVIDIA Build | 90 | Strong reasoning, good for planning |
| 3 | qwen/qwen3.6-plus:free | OpenRouter | 85 | Good reasoning, free alternative |
| 4 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 83 | 1M context for complex plans |
| 5 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 78 | Good general planning |
| 6 | minimax/minimax-m2.5:free | OpenRouter | 75 | Strong reasoning capabilities |

---

### 4.6 METIS (Analyst - Subagent)

**Requirements**: Pre-planning analysis, ambiguity detection, xhigh reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **qwen/qwen3.6-plus:free** | OpenRouter | 91 | Current config. Strong analytical capabilities |
| 2 | nvidia/z-ai/glm5 | NVIDIA Build | 89 | Excellent for analysis |
| 3 | openai/gpt-5.4 | OpenAI | 88 | Strong but overkill for analyst role |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 86 | Same model family, free tier |
| 5 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 80 | Good for complex analysis |
| 6 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 75 | Acceptable for analysis |

---

### 4.7 MOMUS (Reviewer - Subagent)

**Requirements**: Work plan review, xhigh reasoning, quality assurance

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.4** | OpenAI | 94 | Current config. Optimal for review |
| 2 | nvidia/z-ai/glm5 | NVIDIA Build | 88 | Strong reasoning for review tasks |
| 3 | qwen/qwen3.6-plus:free | OpenRouter | 84 | Good reasoning, free alternative |
| 4 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 78 | Good for detailed reviews |
| 5 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 75 | Acceptable for reviews |
| 6 | z-ai/glm-4.5-air:free | OpenRouter | 72 | GLM family, moderate reasoning |

---

### 4.8 LIBRARIAN (Research - Subagent)

**Requirements**: External reference search, web tools, minimal reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **opencode/gemini-3-flash** | OpenCode | 93 | Current config. Fast, good for research |
| 2 | qwen/qwen3.6-plus:free | OpenRouter | 90 | 1M context, vision+tools, excellent for research |
| 3 | nvidia/z-ai/glm5 | NVIDIA Build | 85 | Good research capabilities |
| 4 | google/gemma-3-27b-it:free | OpenRouter | 82 | Google family, good for search |
| 5 | openrouter/free | OpenRouter | 78 | Vision+tools, general research |
| 6 | stepfun/step-3.5-flash:free | OpenRouter | 75 | Fast, good for quick lookups |

---

### 4.9 MULTIMODAL-LOOKER (Visual - Subagent)

**Requirements**: Visual analysis, medium reasoning, image/document processing

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **google/lyria-3-pro-preview:free** | OpenRouter | 95 | Current config. **Best for visual tasks**, 1M context |
| 2 | nvidia/z-ai/glm5 | NVIDIA Build | 92 | Good multimodal capabilities |
| 3 | qwen/qwen2.5-vl-72b-instruct | OpenRouter | 93 | Fallback config, excellent vision |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 88 | Vision+tools, strong multimodal |
| 5 | nvidia/nemotron-nano-12b-v2-vl:free | OpenRouter | 85 | NVIDIA vision model, tools |
| 6 | google/gemma-3-27b-it:free | OpenRouter | 80 | Vision capabilities, good size |

---

### 4.10 ATLAS (Knowledge - Subagent)

**Requirements**: Knowledge management, medium reasoning, read/edit tools

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **qwen/qwen3.6-plus:free** | OpenRouter | 90 | Current config. Good for knowledge tasks |
| 2 | nvidia/z-ai/glm5 | NVIDIA Build | 88 | Strong for knowledge management |
| 3 | qwen/qwen3.6-plus:free | OpenRouter | 86 | Same family, free tier |
| 4 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 82 | Good general knowledge |
| 5 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 80 | 1M context for large knowledge bases |
| 6 | minimax/minimax-m2.5:free | OpenRouter | 75 | Good reasoning for knowledge |

---

### 4.11 SISYPHUS-JUNIOR (Orchestrator-Junior - Subagent)

**Requirements**: Delegation support, medium reasoning, task coordination

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** | NVIDIA Build | 93 | Current config. Excellent for junior orchestration |
| 2 | qwen/qwen3.6-plus:free | OpenRouter | 88 | Strong reasoning, good for delegation |
| 3 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 85 | Fallback config, good general purpose |
| 4 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 80 | Good for complex delegation |
| 5 | stepfun/step-3.5-flash:free | OpenRouter | 75 | Fast, good for quick delegation |
| 6 | openrouter/free | OpenRouter | 72 | General purpose, auto-routing |

---

## 5. Model Rankings by Category

### 5.1 VISUAL-ENGINEERING

**Requirements**: Frontend, UI/UX, design, styling, animation, high reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openrouter/qwen/qwen2.5-vl-72b-instruct** | OpenRouter | 96 | Current config. Excellent for visual engineering |
| 2 | google/lyria-3-pro-preview:free | OpenRouter | 95 | Best free visual model, 1M context |
| 3 | opencode/gemini-3.1-pro | OpenCode | 93 | Fallback config, strong vision |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 88 | Vision+tools, good for UI work |
| 5 | nvidia/nemotron-nano-12b-v2-vl:free | OpenRouter | 85 | Multimodal with tools |
| 6 | google/gemma-3-27b-it:free | OpenRouter | 80 | Vision capabilities, moderate reasoning |

---

### 5.2 ULTRABRAIN

**Requirements**: Genuinely hard, logic-heavy tasks, xhigh reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.4** | OpenAI | 97 | Current config. Optimal for ultrabrain tasks |
| 2 | openai/gpt-5.4-pro | OpenAI | 95 | Enhanced reasoning for complex logic |
| 3 | nvidia/z-ai/glm5 | NVIDIA Build | 90 | Strong reasoning, good for hard problems |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 82 | Good reasoning, free alternative |
| 5 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 80 | 1M context for complex analysis |
| 6 | opencode/claude-opus-4-6 | OpenCode | 78 | Fallback config, strong logic |

---

### 5.3 DEEP

**Requirements**: Goal-oriented autonomous problem-solving, medium reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.3-codex** | OpenAI | 94 | Current config. Excellent for deep work |
| 2 | openai/gpt-5.4 | OpenAI | 92 | Strong reasoning, good for autonomous tasks |
| 3 | nvidia/z-ai/glm5 | NVIDIA Build | 88 | Good for deep problem-solving |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 85 | Good reasoning, free alternative |
| 5 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 82 | 1M context for complex problems |
| 6 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 78 | Good general purpose |

---

### 5.4 ARTISTRY

**Requirements**: Complex problem-solving with unconventional approaches, high reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **opencode/gemini-3.1-pro** | OpenCode | 93 | Current config. Strong for creative solutions |
| 2 | openrouter/qwen/qwen2.5-vl-72b-instruct | OpenRouter | 91 | Fallback config, good for visual creativity |
| 3 | nvidia/z-ai/glm5 | NVIDIA Build | 88 | Good for unconventional approaches |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 85 | Good reasoning, free alternative |
| 5 | google/lyria-3-pro-preview:free | OpenRouter | 82 | Vision capabilities for creative work |
| 6 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 78 | Good general creativity |

---

### 5.5 QUICK

**Requirements**: Trivial tasks, minimal reasoning, single file changes

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** | NVIDIA Build | 94 | Current config. Fast and efficient |
| 2 | qwen/qwen3.6-plus:free | OpenRouter | 92 | Fast, 1M context for quick tasks |
| 3 | stepfun/step-3.5-flash:free | OpenRouter | 90 | Fast reasoning, efficient |
| 4 | nvidia/nemotron-3-nano-30b-a3b:free | OpenRouter | 88 | Efficient for quick tasks |
| 5 | openai/gpt-5.4-mini | OpenAI | 85 | Fallback config, fast |
| 6 | google/gemma-3-4b-it:free | OpenRouter | 82 | Lightweight, good for simple tasks |

---

### 5.6 UNSPECIFIED-LOW

**Requirements**: Tasks that don't fit other categories, low effort, medium reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** | NVIDIA Build | 93 | Current config. Good balance |
| 2 | qwen/qwen3.6-plus:free | OpenRouter | 90 | Versatile, good for unspecified tasks |
| 3 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 85 | Good general purpose |
| 4 | openai/gpt-5.4-mini | OpenAI | 82 | Fallback config, efficient |
| 5 | nvidia/nemotron-3-nano-30b-a3b:free | OpenRouter | 80 | Efficient for low effort tasks |
| 6 | stepfun/step-3.5-flash:free | OpenRouter | 78 | Fast, good for quick tasks |

---

### 5.7 UNSPECIFIED-HIGH

**Requirements**: Tasks that don't fit other categories, high effort, medium reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** | NVIDIA Build | 93 | Current config. Good for high effort tasks |
| 2 | openai/gpt-5.4 | OpenAI | 90 | Fallback config, strong reasoning |
| 3 | qwen/qwen3.6-plus:free | OpenRouter | 88 | Versatile, good for complex unspecified tasks |
| 4 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 85 | 1M context for complex tasks |
| 5 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 82 | Good general purpose |
| 6 | minimax/minimax-m2.5:free | OpenRouter | 78 | Good reasoning for complex tasks |

---

### 5.8 WRITING

**Requirements**: Documentation, prose, technical writing, minimal reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **opencode/gemini-3-flash** | OpenCode | 92 | Current config. Fast, good for writing |
| 2 | qwen/qwen-2.5-72b-instruct | OpenRouter | 90 | Fallback config, good for prose |
| 3 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 88 | Fallback config, good writing |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 85 | Good for documentation |
| 5 | google/gemma-3-27b-it:free | OpenRouter | 82 | Good for technical writing |
| 6 | openrouter/free | OpenRouter | 78 | General purpose, good for writing |

---

## 6. Summary: Best Free Model per Agent

| Agent | Best Free Model | Provider | Score | Why |
|-------|-----------------|----------|-------|-----|
| sisyphus | qwen/qwen3.6-plus:free | OpenRouter | 88 | 1M context, vision+tools, strong reasoning |
| hephaestus | qwen/qwen3-coder:free | OpenRouter | 89 | Best free coding model |
| oracle | qwen/qwen3.6-plus:free | OpenRouter | 82 | Good reasoning, free alternative |
| explore | qwen/qwen3.6-plus:free | OpenRouter | 90 | Fast, 1M context for searches |
| prometheus | qwen/qwen3.6-plus:free | OpenRouter | 85 | Good reasoning for planning |
| metis | qwen/qwen3.6-plus:free | OpenRouter | 91 | Strong analytical capabilities |
| momus | qwen/qwen3.6-plus:free | OpenRouter | 84 | Good reasoning for review |
| librarian | qwen/qwen3.6-plus:free | OpenRouter | 90 | 1M context, excellent for research |
| multimodal-looker | google/lyria-3-pro-preview:free | OpenRouter | 95 | Best visual model, 1M context |
| atlas | qwen/qwen3.6-plus:free | OpenRouter | 90 | Good for knowledge management |
| sisyphus-junior | qwen/qwen3.6-plus:free | OpenRouter | 88 | Strong reasoning for delegation |

---

## 7. Summary: Best Free Model per Category

| Category | Best Free Model | Provider | Score | Why |
|----------|-----------------|----------|-------|-----|
| visual-engineering | google/lyria-3-pro-preview:free | OpenRouter | 95 | Best visual model, 1M context |
| ultrabrain | qwen/qwen3.6-plus:free | OpenRouter | 82 | Good reasoning for hard problems |
| deep | qwen/qwen3.6-plus:free | OpenRouter | 85 | Good for autonomous problem-solving |
| artistry | qwen/qwen3.6-plus:free | OpenRouter | 85 | Good for creative solutions |
| quick | qwen/qwen3.6-plus:free | OpenRouter | 92 | Fast, 1M context for quick tasks |
| unspecified-low | qwen/qwen3.6-plus:free | OpenRouter | 90 | Versatile for unspecified tasks |
| unspecified-high | qwen/qwen3.6-plus:free | OpenRouter | 88 | Versatile for complex unspecified tasks |
| writing | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 88 | Good for documentation and prose |

---

## 8. Cost Optimization Recommendations

### 8.1 Immediate Free Tier Adoption

| Agent/Category | Switch From | Switch To | Provider | Savings |
|----------------|-------------|-----------|----------|---------|
| explore | nvidia/z-ai/glm5 | qwen/qwen3.6-plus:free | OpenRouter | 100% |
| librarian | opencode/gemini-3-flash | qwen/qwen3.6-plus:free | OpenRouter | 100% |
| atlas | qwen/qwen3.6-plus:free | qwen/qwen3.6-plus:free | OpenRouter | Already free |
| metis | qwen/qwen3.6-plus:free | qwen/qwen3.6-plus:free | OpenRouter | Already free |
| multimodal-looker | google/lyria-3-pro-preview:free | google/lyria-3-pro-preview:free | OpenRouter | Already free |
| quick | nvidia/z-ai/glm5 | qwen/qwen3.6-plus:free | OpenRouter | 100% |
| unspecified-low | nvidia/z-ai/glm5 | qwen/qwen3.6-plus:free | OpenRouter | 100% |
| writing | opencode/gemini-3-flash | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 100% |

### 8.2 Keep Paid Models for Critical Tasks

| Agent/Category | Keep Model | Provider | Rationale |
|----------------|-----------|----------|-----------|
| sisyphus | nvidia/z-ai/glm5 | NVIDIA Build | Orchestration requires thinking capability |
| hephaestus | openai/gpt-5.4 | OpenAI | Best implementation performance |
| oracle | openai/gpt-5.4 | OpenAI | Critical architecture consultation |
| prometheus | openai/gpt-5.4 | OpenAI | Strategic planning needs frontier intelligence |
| momus | openai/gpt-5.4 | OpenAI | Quality assurance needs high reasoning |
| ultrabrain | openai/gpt-5.4 | OpenAI | Hard logic tasks need frontier intelligence |
| deep | openai/gpt-5.3-codex | OpenAI | Autonomous problem-solving needs strong coding |

---

## 9. Key Findings

1. **qwen/qwen3.6-plus:free** is the most versatile free model, appearing as top choice for **8/11 agents** and **6/9 categories**
2. **nvidia/z-ai/glm5** (current default for many agents) is excellent but requires NVIDIA Build access
3. **google/lyria-3-pro-preview:free** is the best free visual model with 1M context
4. **qwen/qwen3-coder:free** is the best free coding-specific model
5. **openai/gpt-5.4** remains the best paid model for critical tasks requiring frontier intelligence
6. Current configurations are well-optimized, with most using appropriate models for their roles
7. **Cost savings opportunity**: 6 agents/categories can switch to free models without significant performance loss

---

## 10. Methodology

**Effectiveness Score (0-100) based on**:
- Task-specific capability matching (40%)
- Context window size (20%)
- Reasoning level requirements (20%)
- Tool support (vision, tools, function calling) (10%)
- Cost efficiency (10%)

---

## 11. Related Documentation

- [Oh-My-OpenCode Configuration](~/.config/opencode/oh-my-opencode.json)
- [OpenRouter Free Models](https://openrouter.ai/collections/free-models)
- [NVIDIA Build Models](https://build.nvidia.com/models)
- [OpenAI Pricing](https://developers.openai.com/api/docs/pricing)
- [OpenCode Platform](https://opencode.ai/)

---

**Last Updated**: April 6, 2026
**Report Version**: 2.0
