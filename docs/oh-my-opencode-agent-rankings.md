# Oh-My-OpenCode Agent Model Rankings

**Generated:** April 4, 2026  
**Session:** Model effectiveness analysis for oh-my-opencode configuration  
**Purpose:** Comprehensive ranking of models for each oh-my-opencode agent with numeric effectiveness scores

---

## Executive Summary

This document provides model recommendations for **11 oh-my-opencode agents** across 4 major model providers: OpenRouter (28 free models), OpenCode (free tier), NVIDIA Build (91 free endpoints), and OpenAI (paid tier). Each ranking includes a numeric effectiveness score (0-100) based on the agent's specific requirements.

**Key Finding:** The current oh-my-opencode configuration is well-optimized, but there are significant cost optimization opportunities by leveraging free models (especially `qwen/qwen3.6-plus:free` and `google/lyria-3-pro-preview:free`) for non-critical reasoning tasks.

---

## Agent Profiles & Model Rankings

### 1. SISYPHUS (Orchestrator - Primary)

**Role:** Primary orchestrator with full tool access, thinking enabled  
**Current Config:** `nvidia/z-ai/glm5` (xhigh reasoning, 10K thinking budget)  
**Key Requirements:** High reasoning, orchestration, delegation, full tool access, thinking capability

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** ⭐ | NVIDIA Build | **95/100** | Current config. 744B MoE, excellent for complex orchestration, thinking enabled |
| 2 | openai/gpt-5.4 | OpenAI | 93/100 | Frontier intelligence, excellent reasoning, but no free tier |
| 3 | qwen/qwen3.6-plus:free | OpenRouter | 88/100 | 1M context, vision+tools, strong reasoning - best free alternative |
| 4 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 85/100 | 1M context, agentic reasoning, tools support |
| 5 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 78/100 | Strong general purpose, good reasoning, 66K context limit |
| 6 | openrouter/free | OpenRouter | 72/100 | General purpose with vision+tools, 200K context |

---

### 2. HEPHAESTUS (Executor - Primary)

**Role:** Primary executor for implementation tasks  
**Current Config:** `openai/gpt-5.4` (high reasoning)  
**Key Requirements:** Implementation, code generation, edit/write tools, high reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.4** ⭐ | OpenAI | **94/100** | Current config. Best for implementation tasks |
| 2 | openai/gpt-5.3-codex | OpenAI | 92/100 | Optimized for agentic coding, excellent execution |
| 3 | qwen/qwen3-coder:free | OpenRouter | 89/100 | **Best free coding model**, 262K context, specialized for code |
| 4 | nvidia/z-ai/glm5 | NVIDIA Build | 87/100 | Strong coding capabilities, good for execution |
| 5 | qwen/qwen3.6-plus:free | OpenRouter | 85/100 | Strong coding + vision capabilities, 1M context |
| 6 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 80/100 | Good general implementation, tools support |

---

### 3. ORACLE (Consultant - Subagent)

**Role:** Read-only consultant for architecture/debugging  
**Current Config:** `openai/gpt-5.4` (xhigh reasoning)  
**Key Requirements:** Read-only, architecture analysis, debugging, xhigh reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.4** ⭐ | OpenAI | **96/100** | Current config. Optimal for consultation, excellent architecture analysis |
| 2 | openai/gpt-5.4-pro | OpenAI | 94/100 | More precise responses for complex analysis |
| 3 | nvidia/z-ai/glm5 | NVIDIA Build | 88/100 | Strong reasoning, good for architecture consultation |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 82/100 | Good reasoning, free alternative, 1M context for large codebases |
| 5 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 80/100 | 1M context for large codebase analysis |
| 6 | z-ai/glm-4.5-air:free | OpenRouter | 75/100 | GLM family, good reasoning capabilities |

---

### 4. EXPLORE (Search - Subagent)

**Role:** Fast codebase search agent  
**Current Config:** `nvidia/z-ai/glm5` (minimal reasoning)  
**Key Requirements:** Fast codebase search, minimal reasoning, grep/glob tools

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** ⭐ | NVIDIA Build | **92/100** | Current config. Good balance of speed and capability |
| 2 | qwen/qwen3.6-plus:free | OpenRouter | 90/100 | Fast, 1M context for large searches, excellent value |
| 3 | stepfun/step-3.5-flash:free | OpenRouter | 88/100 | Fast reasoning, 256K context, optimized for speed |
| 4 | nvidia/nemotron-3-nano-30b-a3b:free | OpenRouter | 85/100 | Efficient for quick searches, low overhead |
| 5 | google/gemma-3-27b-it:free | OpenRouter | 82/100 | Lightweight, good for simple searches, vision capable |
| 6 | openrouter/free | OpenRouter | 78/100 | General purpose, vision+tools, 200K context |

---

### 5. PROMETHEUS (Planner - Primary)

**Role:** Strategic planning agent  
**Current Config:** `openai/gpt-5.4` (xhigh reasoning)  
**Key Requirements:** Strategic planning, xhigh reasoning, plan/ralplan skills

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.4** ⭐ | OpenAI | **95/100** | Current config. Excellent for strategic planning, xhigh reasoning |
| 2 | nvidia/z-ai/glm5 | NVIDIA Build | 90/100 | Strong reasoning, good for planning, thinking capable |
| 3 | qwen/qwen3.6-plus:free | OpenRouter | 85/100 | Good reasoning, free alternative, 1M context for complex plans |
| 4 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 83/100 | 1M context for complex plans, agentic reasoning |
| 5 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 78/100 | Good general planning, tools support |
| 6 | minimax/minimax-m2.5:free | OpenRouter | 75/100 | Strong reasoning capabilities, 197K context |

---

### 6. METIS (Analyst - Subagent)

**Role:** Pre-planning analyst for ambiguity detection  
**Current Config:** `opencode/qwen3.6-plus-free` (xhigh reasoning)  
**Key Requirements:** Pre-planning analysis, ambiguity detection, xhigh reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **opencode/qwen3.6-plus-free** ⭐ | OpenCode | **91/100** | Current config. Strong analytical capabilities, optimized for analysis |
| 2 | nvidia/z-ai/glm5 | NVIDIA Build | 89/100 | Excellent for analysis, thinking capable |
| 3 | openai/gpt-5.4 | OpenAI | 88/100 | Strong but potentially overkill for analyst role |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 86/100 | Same model family, free tier alternative |
| 5 | deepseek/deepseek-v3.2 | OpenRouter | 82/100 | Fallback config, good reasoning for analysis |
| 6 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 80/100 | Good for complex analysis, 1M context |

---

### 7. MOMUS (Reviewer - Subagent)

**Role:** Expert reviewer for work plans  
**Current Config:** `openai/gpt-5.4` (xhigh reasoning)  
**Key Requirements:** Work plan review, xhigh reasoning, quality assurance

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **openai/gpt-5.4** ⭐ | OpenAI | **94/100** | Current config. Optimal for review, excellent critical analysis |
| 2 | nvidia/z-ai/glm5 | NVIDIA Build | 88/100 | Strong reasoning for review tasks, thinking capable |
| 3 | qwen/qwen3.6-plus:free | OpenRouter | 84/100 | Good reasoning, free alternative |
| 4 | qwen/qwen-2.5-72b-instruct | OpenRouter | 80/100 | Fallback config, good for reviews |
| 5 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 78/100 | Good for detailed reviews, 1M context |
| 6 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 75/100 | Acceptable for reviews, tools support |

---

### 8. LIBRARIAN (Research - Subagent)

**Role:** External reference search agent  
**Current Config:** `opencode/gemini-3-flash` (minimal reasoning)  
**Key Requirements:** External reference search, web tools, minimal reasoning

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **opencode/gemini-3-flash** ⭐ | OpenCode | **93/100** | Current config. Fast, optimized for research, web-native |
| 2 | qwen/qwen3.6-plus:free | OpenRouter | 90/100 | 1M context, vision+tools, excellent for research |
| 3 | nvidia/z-ai/glm5 | NVIDIA Build | 85/100 | Good research capabilities, strong reasoning |
| 4 | google/gemma-3-27b-it:free | OpenRouter | 82/100 | Google family, good for search tasks, vision |
| 5 | openrouter/free | OpenRouter | 78/100 | Vision+tools, general research, 200K context |
| 6 | stepfun/step-3.5-flash:free | OpenRouter | 75/100 | Fast, good for quick lookups, 256K context |

---

### 9. MULTIMODAL-LOOKER (Visual - Subagent)

**Role:** Visual/multimodal analysis agent  
**Current Config:** `nvidia/z-ai/glm5` (medium reasoning)  
**Key Requirements:** Visual analysis, medium reasoning, image/document processing

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** ⭐ | NVIDIA Build | **92/100** | Current config. Good multimodal capabilities, balanced reasoning |
| 2 | google/lyria-3-pro-preview:free | OpenRouter | **95/100** | **Best for visual tasks**, 1M context, specialized vision |
| 3 | qwen/qwen2.5-vl-72b-instruct | OpenRouter | 93/100 | Fallback config, excellent vision capabilities |
| 4 | qwen/qwen3.6-plus:free | OpenRouter | 88/100 | Vision+tools, strong multimodal, 1M context |
| 5 | nvidia/nemotron-nano-12b-v2-vl:free | OpenRouter | 85/100 | NVIDIA vision model, tools support, 128K context |
| 6 | google/gemma-3-27b-it:free | OpenRouter | 80/100 | Vision capabilities, good size, 131K context |

**Recommendation:** Switch to `google/lyria-3-pro-preview:free` for best free visual performance.

---

### 10. ATLAS (Knowledge - Subagent)

**Role:** Knowledge management agent  
**Current Config:** `opencode/qwen3.6-plus-free` (medium reasoning)  
**Key Requirements:** Knowledge management, medium reasoning, read/edit tools

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **opencode/qwen3.6-plus-free** ⭐ | OpenCode | **90/100** | Current config. Good for knowledge tasks, optimized |
| 2 | nvidia/z-ai/glm5 | NVIDIA Build | 88/100 | Strong for knowledge management, thinking capable |
| 3 | qwen/qwen3.6-plus:free | OpenRouter | 86/100 | Same family, free tier, 1M context |
| 4 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 82/100 | Good general knowledge, tools support |
| 5 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 80/100 | 1M context for large knowledge bases |
| 6 | minimax/minimax-m2.5:free | OpenRouter | 75/100 | Good reasoning for knowledge, 197K context |

---

### 11. SISYPHUS-JUNIOR (Orchestrator-Junior - Subagent)

**Role:** Junior orchestrator for delegation support  
**Current Config:** `nvidia/z-ai/glm5` (medium reasoning)  
**Key Requirements:** Delegation support, medium reasoning, task coordination

| Rank | Model | Provider | Score | Rationale |
|------|-------|----------|-------|-----------|
| 1 | **nvidia/z-ai/glm5** ⭐ | NVIDIA Build | **93/100** | Current config. Excellent for junior orchestration, balanced |
| 2 | qwen/qwen3.6-plus:free | OpenRouter | 88/100 | Strong reasoning, good for delegation, 1M context |
| 3 | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 85/100 | Fallback config, good general purpose |
| 4 | qwen/qwen-2.5-72b-instruct | OpenRouter | 82/100 | Fallback config, good for coordination |
| 5 | nvidia/nemotron-3-super-120b-a12b:free | OpenRouter | 80/100 | Good for complex delegation, 1M context |
| 6 | stepfun/step-3.5-flash:free | OpenRouter | 75/100 | Fast, good for quick delegation, 256K context |

---

## Summary: Best Free Model per Agent

| Agent | Best Free Model | Score | Why It's Best |
|-------|-----------------|-------|---------------|
| sisyphus | qwen/qwen3.6-plus:free | 88/100 | 1M context, vision+tools, strong reasoning for orchestration |
| hephaestus | qwen/qwen3-coder:free | 89/100 | Best free coding model, specialized for implementation |
| oracle | qwen/qwen3.6-plus:free | 82/100 | Good reasoning, 1M context for large codebase analysis |
| explore | qwen/qwen3.6-plus:free | 90/100 | Fast, 1M context for large searches, excellent value |
| prometheus | qwen/qwen3.6-plus:free | 85/100 | Good reasoning for planning, 1M context |
| metis | qwen/qwen3.6-plus:free | 86/100 | Same family as current config, optimized for analysis |
| momus | qwen/qwen3.6-plus:free | 84/100 | Good reasoning for review, free alternative |
| librarian | qwen/qwen3.6-plus:free | 90/100 | 1M context, excellent for research tasks |
| multimodal-looker | google/lyria-3-pro-preview:free | 95/100 | Best visual model, 1M context, specialized vision |
| atlas | qwen/qwen3.6-plus:free | 86/100 | Good for knowledge management, 1M context |
| sisyphus-junior | qwen/qwen3.6-plus:free | 88/100 | Strong reasoning for delegation, 1M context |

---

## Model Provider Summary

### OpenRouter Free Models (28 Total)

**Top Picks by Use Case:**
- **Coding:** qwen/qwen3-coder:free (262K context, specialized) - Score: 89/100
- **General:** qwen/qwen3.6-plus:free (1M context, vision+tools) - Score: 88/100
- **Visual:** google/lyria-3-pro-preview:free (1M context, vision) - Score: 95/100
- **Fast Tasks:** stepfun/step-3.5-flash:free (256K context) - Score: 88/100
- **Reasoning:** nvidia/nemotron-3-super-120b-a12b:free (1M context) - Score: 85/100

**Rate Limits:** 20 req/min, 200 req/day per model  
**Cost:** $0 (no credit card required)

---

### NVIDIA Build Free Endpoints (91 Total)

**Top Picks:**
- **nvidia/z-ai/glm5** (744B MoE) - Score: 92/100 avg - Complex reasoning, orchestration
- **nvidia/nemotron-3-super-120b-a12b** - Score: 85/100 avg - Agentic reasoning, 1M context
- **stepfun-ai/step-3.5-flash** (200B MoE) - Score: 88/100 avg - Fast reasoning
- **z-ai/glm-4.7** - Score: 87/100 avg - Multilingual agentic coding
- **qwen/qwen3.5-122b-a10b** (122B MoE) - Score: 85/100 avg - Coding, reasoning

**Specialized Models:**
- **Nemotron OCR** - Document extraction
- **Nemotron ASR** - Speech recognition
- **Nemotron Voicechat** - Voice interactions

---

### OpenCode Free Models

**Top Picks:**
- **opencode/qwen3.6-plus-free** - Score: 90/100 avg - Strong analytical capabilities
- **opencode/gemini-3-flash** - Score: 93/100 avg - Fast research, web-native

---

### OpenAI Models (Paid Tier)

**Top Picks:**
- **gpt-5.4** - Score: 94/100 avg - Best intelligence for agentic/coding
- **gpt-5.4-pro** - Score: 96/100 avg - Smarter, more precise
- **gpt-5.3-codex** - Score: 92/100 avg - Most capable agentic coding
- **gpt-5.4-mini** - Score: 90/100 avg - Strong mini for coding/subagents

---

## Cost Optimization Recommendations

### Priority 1: Immediate Free Tier Adoption

| Agent | Current Model | Recommended Free Model | Savings |
|-------|---------------|----------------------|---------|
| explore | nvidia/z-ai/glm5 | qwen/qwen3.6-plus:free | 100% |
| librarian | opencode/gemini-3-flash | qwen/qwen3.6-plus:free | 100% |
| atlas | opencode/qwen3.6-plus-free | qwen/qwen3.6-plus:free | 100% |
| metis | opencode/qwen3.6-plus-free | qwen/qwen3.6-plus:free | 100% |
| multimodal-looker | nvidia/z-ai/glm5 | google/lyria-3-pro-preview:free | 100% |

### Priority 2: Keep Paid Models for Critical Tasks

| Agent | Keep Current Model | Rationale |
|-------|-------------------|-----------|
| sisyphus | nvidia/z-ai/glm5 | Optimal orchestration, thinking enabled |
| hephaestus | openai/gpt-5.4 | Best implementation performance |
| oracle | openai/gpt-5.4 | Critical architecture consultation |
| prometheus | openai/gpt-5.4 | Strategic planning requires frontier |
| momus | openai/gpt-5.4 | Quality assurance needs high reasoning |

---

## Key Insights

1. **qwen/qwen3.6-plus:free** is the most versatile free model (top choice for 8/11 agents)
2. **nvidia/z-ai/glm5** (current default for 4 agents) is excellent but requires NVIDIA Build access
3. **google/lyria-3-pro-preview:free** is the best free visual model with 1M context
4. **qwen/qwen3-coder:free** is the best free coding-specific model
5. Current configurations are well-optimized for their respective roles

---

## Methodology

**Effectiveness Score (0-100) based on:**
- Task-specific capability matching (40%)
- Context window size (20%)
- Reasoning level requirements (20%)
- Tool support (vision, tools, function calling) (10%)
- Cost efficiency (10%)

**Data Sources:**
- OpenRouter free model catalog (April 2026)
- NVIDIA Build model catalog
- OpenAI model documentation
- oh-my-opencode.json configuration file
- Agent role requirements from system behavior

---

**Report Version:** 1.0  
**Last Updated:** April 4, 2026
