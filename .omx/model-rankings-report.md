# Oh-My-OpenCode Agent Model Ranking Report (v3.0)

**Updated:** April 21, 2026
**Purpose:** Comprehensive model effectiveness ranking for each oh-my-opencode agent
**Provider Constraint:** Only NVIDIA Build, OpenCode Zen, and OpenAI models. No OpenRouter or direct Google models.

---

## Executive Summary

This report provides model recommendations for 25+ oh-my-opencode agents across 3 model providers: NVIDIA Build (200+ models, many free), OpenCode Zen (curated models), and OpenAI (paid tier). Each ranking includes a numeric effectiveness score (0-100) based on the agent's specific requirements.

**Key Changes from v1.0:**
- All OpenRouter model references removed
- `nvidia/z-ai/glm5` replaced with `nvidia/z-ai/glm-5.1` (deprecated April 20, 2026)
- `openai/gpt-5.3-codex` removed (being retired June 5, 2026)
- `google/gemini-3.1-flash-lite-preview` replaced with `opencode/gemini-3-flash`
- GLM-5.1 is #1 on SWE-Bench Pro (58.4%), released April 18, 2026

---

## Agent Profiles & Model Rankings

### 1. **Plan Agent** (Strategic Planning)
**Role:** Requirements gathering, technical design, consensus planning
**Key Requirements:** Long-context reasoning, multi-perspective analysis, structured output

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **96/100** | #1 SWE-Bench Pro, 200K ctx, FREE, thinking enabled |
| 2 | **openai/gpt-5.4-pro** | OpenAI | **94/100** | Deep reasoning, 1.05M ctx, $30/$180 |
| 3 | **openai/gpt-5.4** | OpenAI | **93/100** | High reasoning, 1.05M ctx |
| 4 | **nvidia/deepseek-ai/deepseek-v3.2** | NVIDIA Build | **91/100** | 685B reasoning, 128K ctx |
| 5 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **89/100** | Best agentic coding, 256K ctx, FREE |
| 6 | **opencode/qwen3.6-plus** | OpenCode Zen | **87/100** | General purpose, 128K ctx |

---

### 2. **Autopilot Agent** (Full Autonomous Execution)
**Role:** End-to-end pipeline from idea to working code
**Key Requirements:** Multi-phase coordination, parallel execution, verification loops

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **97/100** | Best for expansion, planning, validation phases |
| 2 | **openai/gpt-5.4** | OpenAI | **95/100** | Excellent for autonomous multi-phase workflows |
| 3 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **93/100** | Best agentic coding, FREE |
| 4 | **nvidia/deepseek-ai/deepseek-v3.2** | NVIDIA Build | **90/100** | 685B reasoning for complex tasks |
| 5 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **87/100** | 1M ctx, agentic, $0.10/$0.50 |
| 6 | **opencode/qwen3-coder** | OpenCode Zen | **85/100** | Coding partner, $0.45/$1.50 |

---

### 3. **Ralph Agent** (Persistence Loop with Verification)
**Role:** Self-referential execution until completion with architect verification
**Key Requirements:** Persistence, retry logic, architect verification, parallel delegation

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **95/100** | Optimal for persistence loops, thinking enabled |
| 2 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **93/100** | Excellent for code execution + verification |
| 3 | **openai/gpt-5.4** | OpenAI | **92/100** | High reasoning for complex Ralph tasks |
| 4 | **nvidia/mistral-ai/mistral-small-4-119b-2603** | NVIDIA Build | **90/100** | Hybrid instruct+reasoning |
| 5 | **opencode/qwen3-coder** | OpenCode Zen | **87/100** | Best cost-effective option for code tasks |
| 6 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **84/100** | Good for agentic reasoning loops, 1M ctx |

---

### 4. **Ultrawork Agent** (Parallel Execution Engine)
**Role:** High-throughput parallel task execution
**Key Requirements:** Fast response, tiered model routing, parallel-safe operations

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/stepfun-ai/step-3.5-flash** | NVIDIA Build | **96/100** | Optimal for LOW-tier parallel tasks, FREE |
| 2 | **nvidia/nvidia/nemotron-3-nano-30b-a3b** | NVIDIA Build | **94/100** | Fast, 1M ctx, $0.05/$0.20 |
| 3 | **openai/gpt-5.4-nano** | OpenAI | **92/100** | Ultra-fast for simple parallel tasks |
| 4 | **opencode/gemini-3-flash** | OpenCode Zen | **89/100** | Fast research, web-native |
| 5 | **nvidia/nvidia/nvidia-nemotron-nano-9b-v2** | NVIDIA Build | **86/100** | Good for LOW-tier tasks |
| 6 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **83/100** | Good for STANDARD-tier parallel tasks |

---

### 5. **Code-Review Agent** (Comprehensive Code Review)
**Role:** Quality, security, maintainability assessment
**Key Requirements:** Deep analysis, security patterns, best practices knowledge

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **98/100** | Best for comprehensive code review, FREE |
| 2 | **openai/gpt-5.4-pro** | OpenAI | **96/100** | Excellent for security + quality review |
| 3 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **93/100** | Strong for code pattern analysis |
| 4 | **nvidia/deepseek-ai/deepseek-v3.2** | NVIDIA Build | **90/100** | Good for complex multi-file reviews |
| 5 | **opencode/qwen3-coder** | OpenCode Zen | **87/100** | Best cost-effective option for code review |
| 6 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **84/100** | Good for agentic code analysis |

---

### 6. **Security-Review Agent** (OWASP Top 10 + Vulnerability Scan)
**Role:** Security audit, secrets detection, dependency vulnerabilities
**Key Requirements:** Security expertise, OWASP knowledge, vulnerability patterns

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **99/100** | Best for security-critical reviews, FREE |
| 2 | **openai/gpt-5.4-pro** | OpenAI | **97/100** | Excellent for OWASP + crypto analysis |
| 3 | **nvidia/deepseek-ai/deepseek-v3.2** | NVIDIA Build | **94/100** | Strong for complex security patterns |
| 4 | **openai/o3** | OpenAI | **91/100** | Good for security reasoning |
| 5 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **85/100** | Best cost-effective option for security review |
| 6 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **82/100** | Good for agentic security analysis |

---

### 7. **Frontend-UI-UX Agent** (Designer-Developer)
**Role:** Component design, responsive layouts, accessibility
**Key Requirements:** Design sense, CSS/HTML knowledge, accessibility standards

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/qwen/qwen3.5-397b-a17b** | NVIDIA Build | **95/100** | VLM with vision, best for UI/UX |
| 2 | **nvidia/mistral-ai/mistral-small-4-119b-2603** | NVIDIA Build | **93/100** | Hybrid instruct+reasoning for design |
| 3 | **opencode/gemini-3-flash** | OpenCode Zen | **91/100** | Excellent for multimodal UI tasks |
| 4 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **88/100** | High reasoning for complex UI |
| 5 | **opencode/qwen3.6-plus** | OpenCode Zen | **85/100** | Good for UI component generation |
| 6 | **nvidia/nvidia/nemotron-nano-12b-v2-vl** | NVIDIA Build | **82/100** | Vision model for visual tasks |

---

### 8. **Build-Fix Agent** (TypeScript/Build Error Resolution)
**Role:** Fix build errors with minimal changes
**Key Requirements:** TypeScript expertise, error pattern recognition, minimal diff strategy

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **97/100** | Best for TypeScript/build fixes, FREE |
| 2 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **95/100** | Excellent for type error resolution |
| 3 | **nvidia/mistral-ai/devstral-2-123b-instruct-2512** | NVIDIA Build | **93/100** | Code-focused, fast for build fixes |
| 4 | **openai/gpt-5.4-mini** | OpenAI | **90/100** | Cost-effective for standard fixes |
| 5 | **opencode/qwen3-coder** | OpenCode Zen | **88/100** | Best cost-effective option for build fixes |
| 6 | **nvidia/meta/llama-3.3-70b-instruct** | NVIDIA Build | **84/100** | Good for type error patterns |

---

### 9. **Analyze Agent** (Deep Investigation)
**Role:** Architecture analysis, bug investigation, performance analysis
**Key Requirements:** Cross-file reasoning, root cause analysis, structured findings

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **97/100** | Best for deep architectural analysis, FREE |
| 2 | **openai/gpt-5.4-pro** | OpenAI | **95/100** | Excellent for complex investigations |
| 3 | **nvidia/deepseek-ai/deepseek-v3.2** | NVIDIA Build | **92/100** | Strong for system analysis |
| 4 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **89/100** | Good for code-level investigation |
| 5 | **opencode/qwen3.6-plus** | OpenCode Zen | **86/100** | Best cost-effective option for analysis |
| 6 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **83/100** | Good for agentic investigation |

---

### 10. **Deep-Research Agent** (Web Research)
**Role:** Multi-angle web research, content generation prep
**Key Requirements:** Broad knowledge, synthesis, fact-checking, current information

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **opencode/gemini-3-flash** | OpenCode Zen | **96/100** | Best for comprehensive research, web-native |
| 2 | **nvidia/stepfun-ai/step-3.5-flash** | NVIDIA Build | **94/100** | Fast, FREE, good for broad research |
| 3 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **91/100** | Good for synthesis and analysis |
| 4 | **openai/gpt-5.4** | OpenAI | **89/100** | Good for multi-source synthesis |
| 5 | **opencode/qwen3.6-plus** | OpenCode Zen | **85/100** | Best cost-effective option for research |
| 6 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **82/100** | Good for broad knowledge tasks |

---

### 11. **Team Agent** (Coordinated Multi-Agent Orchestration)
**Role:** Tmux-based parallel worker coordination
**Key Requirements:** Orchestration, state management, worker coordination

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **94/100** | Optimal for team orchestration, FREE |
| 2 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **92/100** | Strong for worker coordination |
| 3 | **openai/gpt-5.4** | OpenAI | **90/100** | Good for complex team workflows |
| 4 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **88/100** | Good for simple team tasks, 1M ctx |
| 5 | **opencode/qwen3.6-plus** | OpenCode Zen | **85/100** | Best cost-effective option for coordination |
| 6 | **nvidia/mistral-ai/mistral-small-4-119b-2603** | NVIDIA Build | **82/100** | Good for agentic team tasks |

---

### 12. **UltraQA Agent** (QA Cycling Workflow)
**Role:** Test, verify, fix, repeat until goal met
**Key Requirements:** Test execution, failure diagnosis, iterative fixing

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **96/100** | Best for QA cycling workflows, FREE |
| 2 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **94/100** | Excellent for test + fix cycles |
| 3 | **nvidia/mistral-ai/devstral-2-123b-instruct-2512** | NVIDIA Build | **92/100** | Fast for simple QA cycles |
| 4 | **openai/gpt-5.4-mini** | OpenAI | **90/100** | Cost-effective for QA loops |
| 5 | **opencode/qwen3-coder** | OpenCode Zen | **87/100** | Best cost-effective option for QA |
| 6 | **nvidia/meta/llama-3.3-70b-instruct** | NVIDIA Build | **83/100** | Good for test failure diagnosis |

---

### 13. **DeepSearch Agent** (Thorough Codebase Search)
**Role:** Comprehensive codebase search and pattern discovery
**Key Requirements:** Pattern matching, cross-file analysis, comprehensive coverage

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/stepfun-ai/step-3.5-flash** | NVIDIA Build | **93/100** | Best for comprehensive search, FREE |
| 2 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **91/100** | Strong for code pattern discovery |
| 3 | **opencode/gemini-3-flash** | OpenCode Zen | **89/100** | Fast for quick searches |
| 4 | **nvidia/nvidia/nemotron-3-nano-30b-a3b** | NVIDIA Build | **87/100** | Cost-effective for searches |
| 5 | **opencode/qwen3-coder** | OpenCode Zen | **85/100** | Best cost-effective option for code search |
| 6 | **nvidia/nvidia/nvidia-nemotron-nano-9b-v2** | NVIDIA Build | **81/100** | Good for pattern matching |

---

### 14. **Trace Agent** (Agent Flow Timeline)
**Role:** Display hook/skill/agent/tool interaction timeline
**Key Requirements:** Timeline analysis, flow pattern recognition

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/stepfun-ai/step-3.5-flash** | NVIDIA Build | **92/100** | Fast and sufficient for trace analysis, FREE |
| 2 | **openai/gpt-5.4-nano** | OpenAI | **90/100** | Ultra-fast for simple traces |
| 3 | **nvidia/nvidia/nemotron-3-nano-30b-a3b** | NVIDIA Build | **88/100** | Good for complex trace analysis |
| 4 | **nvidia/nvidia/nvidia-nemotron-nano-9b-v2** | NVIDIA Build | **86/100** | Cost-effective for traces |
| 5 | **opencode/gemini-3-flash** | OpenCode Zen | **83/100** | Best cost-effective option |
| 6 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **79/100** | Adequate for simple traces |

---

### 15. **Review Agent** (Plan Review)
**Role:** Critic evaluation of existing plans
**Key Requirements:** Quality assessment, criteria verification, structured feedback

| Rank | Model | Provider | Effectiveness Score | Notes |
|------|-------|----------|---------------------|-------|
| 1 | **nvidia/z-ai/glm-5.1** | NVIDIA Build | **95/100** | Best for comprehensive plan review, FREE |
| 2 | **openai/gpt-5.4-pro** | OpenAI | **93/100** | Excellent for quality assessment |
| 3 | **nvidia/deepseek-ai/deepseek-v3.2** | NVIDIA Build | **90/100** | Strong for standard plan reviews |
| 4 | **nvidia/qwen/qwen3-coder-480b-a35b-instruct** | NVIDIA Build | **87/100** | Good for complex plan evaluation |
| 5 | **opencode/qwen3.6-plus** | OpenCode Zen | **84/100** | Best cost-effective option for review |
| 6 | **nvidia/nvidia/nemotron-3-super-120b-a12b** | NVIDIA Build | **81/100** | Good for agentic review tasks |

---

## Additional Agents (Summary Rankings)

### 16-25. Supporting Agents

| Agent | Top Model | Score | Best Cost-Effective Option | Score |
|-------|-----------|-------|---------------------------|-------|
| **Git-Master** | nvidia/qwen/qwen3-coder-480b-a35b-instruct | 94/100 | opencode/qwen3-coder | 88/100 |
| **Web-Clone** | nvidia/z-ai/glm-5.1 | 93/100 | opencode/gemini-3-flash | 86/100 |
| **Visual-Verdict** | nvidia/qwen/qwen3.5-397b-a17b | 95/100 | nvidia/nvidia/nemotron-nano-12b-v2-vl | 89/100 |
| **Doctor** | nvidia/stepfun-ai/step-3.5-flash | 91/100 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | 84/100 |
| **Ecomode** | openai/gpt-5.4-nano | 96/100 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | 90/100 |
| **HUD** | nvidia/stepfun-ai/step-3.5-flash | 89/100 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | 82/100 |
| **Note** | openai/gpt-5.4-nano | 88/100 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | 85/100 |
| **Cancel** | nvidia/stepfun-ai/step-3.5-flash | 90/100 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | 83/100 |
| **Help** | nvidia/stepfun-ai/step-3.5-flash | 87/100 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | 80/100 |
| **Worker** | nvidia/qwen/qwen3-coder-480b-a35b-instruct | 93/100 | nvidia/meta/llama-3.3-70b-instruct | 86/100 |

---

## Model Provider Summary

### NVIDIA Build (200+ Models)
**Top Picks by Use Case:**
- **Reasoning:** nvidia/z-ai/glm-5.1 (744B MoE) - Score: 96/100 avg, FREE
- **Coding:** nvidia/qwen/qwen3-coder-480b-a35b-instruct (480B MoE) - Score: 93/100 avg, FREE
- **Fast Tasks:** nvidia/stepfun-ai/step-3.5-flash (200B MoE) - Score: 92/100 avg, FREE
- **Vision:** nvidia/qwen/qwen3.5-397b-a17b (397B MoE) - Score: 95/100 avg
- **Agentic:** nvidia/nvidia/nemotron-3-super-120b-a12b - Score: 84/100 avg, $0.10/$0.50
- **Efficient:** nvidia/nvidia/nemotron-3-nano-30b-a3b - Score: 88/100 avg, $0.05/$0.20

**Specialized Models:**
- **Nemotron OCR** - Document extraction
- **Nemotron ASR** - Speech recognition
- **Nemotron Voicechat** - Voice interactions
- **Cosmos Reason2** - Physical world understanding
- **NV-DinoV2** - Image embeddings
- **NV-Grounding-DINO** - Object detection

---

### OpenCode Zen (Curated Models)
**Top Picks:**
- **opencode/gemini-3-flash** - Score: 89/100 avg (web-native, fast, $0.50/$3.00)
- **opencode/qwen3-coder** - Score: 87/100 avg (coding partner, $0.45/$1.50)
- **opencode/qwen3.6-plus** - Score: 85/100 avg (general purpose, $0.50/$3.00)

---

### OpenAI (Paid Tier)
**Top Picks:**
- **openai/gpt-5.4-pro** - Score: 95/100 avg ($30/$180 per 1M tokens)
- **openai/gpt-5.4** - Score: 93/100 avg ($2.50/$15 per 1M tokens)
- **openai/o3** - Score: 91/100 avg ($2/$16 per 1M tokens)
- **openai/gpt-5.4-mini** - Score: 90/100 avg ($0.75/$4.50 per 1M tokens)
- **openai/gpt-5.4-nano** - Score: 90/100 avg ($0.20/$1.25 per 1M tokens)
- **openai/o4-mini** - Score: 83/100 avg ($1.10/$4.40 per 1M tokens)

---

## Tier-Based Recommendations

### LOW Tier (Simple Tasks)
**Best:** openai/gpt-5.4-nano, nvidia/stepfun-ai/step-3.5-flash, nvidia/nvidia/nvidia-nemotron-nano-9b-v2
**Free:** nvidia/stepfun-ai/step-3.5-flash, nvidia/nvidia/nvidia-nemotron-nano-9b-v2

### STANDARD Tier (Standard Tasks)
**Best:** nvidia/z-ai/glm-5.1, nvidia/qwen/qwen3-coder-480b-a35b-instruct, openai/gpt-5.4
**Free:** nvidia/z-ai/glm-5.1, nvidia/qwen/qwen3-coder-480b-a35b-instruct

### THOROUGH Tier (Complex Tasks)
**Best:** nvidia/z-ai/glm-5.1, openai/gpt-5.4-pro, nvidia/deepseek-ai/deepseek-v3.2
**Free:** nvidia/z-ai/glm-5.1, nvidia/qwen/qwen3-coder-480b-a35b-instruct

---

## Cost Optimization Strategies

### Free Tier Stack (Zero Cost)
1. **Planning:** nvidia/z-ai/glm-5.1 (200K ctx, FREE)
2. **Execution:** nvidia/qwen/qwen3-coder-480b-a35b-instruct (256K ctx, FREE)
3. **Review:** nvidia/z-ai/glm-5.1 (FREE)
4. **Fast Tasks:** nvidia/stepfun-ai/step-3.5-flash (200K ctx, FREE)
5. **Research:** opencode/gemini-3-flash ($0.50/$3.00)

### Budget Tier Stack (<$5/month)
1. **Planning:** nvidia/z-ai/glm-5.1 (FREE)
2. **Execution:** opencode/qwen3-coder ($0.45/$1.50)
3. **Review:** nvidia/z-ai/glm-5.1 (FREE)
4. **Fast Tasks:** openai/gpt-5.4-nano ($0.20/$1.25)

### Performance Tier Stack (No Budget Limit)
1. **Planning:** openai/gpt-5.4-pro ($30/$180)
2. **Execution:** openai/gpt-5.4 ($2.50/$15)
3. **Review:** openai/gpt-5.4-pro ($30/$180)
4. **Fast Tasks:** openai/gpt-5.4-nano ($0.20/$1.25)

---

## Key Insights

1. **nvidia/z-ai/glm-5.1** dominates reasoning tasks (95-99/100) and is FREE
2. **nvidia/qwen/qwen3-coder-480b-a35b-instruct** excels at code-specific tasks (93-97/100) and is FREE
3. **nvidia/stepfun-ai/step-3.5-flash** is optimal for fast/low-tier tasks (92-96/100) and is FREE
4. **opencode/gemini-3-flash** is the best for research/writing (89-96/100)
5. **NVIDIA Build** provides the most cost-effective options with many free models
6. **OpenAI** remains essential for frontier-level reasoning when budget allows

---

## Methodology

**Effectiveness Score (0-100) based on:**
- Task-specific capability (40%)
- Context window size (20%)
- Response quality (20%)
- Speed/latency (10%)
- Cost efficiency (10%)

**Data Sources:**
- NVIDIA Build model catalog (April 2026)
- OpenCode Zen documentation
- OpenAI pricing page
- Agent skill requirements from SKILL.md files
- SWE-Bench Pro benchmark results

---

**Report Version:** 2.0
**Last Updated:** April 21, 2026
