# Explorer Project

AI agent model rankings and optimization research for oh-my-opencode configuration.

## Project Structure

```
explorer/
├── docs/
│   ├── oh-my-opencode-agent-rankings.md # Comprehensive model rankings for 11 agents (v1.0)
│   ├── oh-my-opencode-agent-rankings-2026-04-06.md # Updated comprehensive report (v2.0)
│   ├── session-learnings-2026-04-04.md # Session 1: Agent architecture insights
│   ├── session-learnings-2026-04-05.md # Session 2: Exhaustive search methodology
│   └── session-learnings-2026-04-06.md # Session 3: Timeout configuration & system architecture
├── .omx/
│   └── model-rankings-report.md # OpenCode Zen agent rankings (25 agents)
├── session_opencode_model_ranking.md # Previous session notes
└── README.md # This file
```
explorer/
├── docs/
│   ├── oh-my-opencode-agent-rankings.md    # Comprehensive model rankings for 11 agents
│   └── session-learnings-2026-04-04.md     # Detailed session learnings and insights
├── .omx/
│   └── model-rankings-report.md            # OpenCode agent rankings (different system)
├── session_opencode_model_ranking.md       # Previous session notes
└── README.md                               # This file
```

## Key Documents

### 1. [Oh-My-OpenCode Agent Rankings (v2.0)](docs/oh-my-opencode-agent-rankings-2026-04-06.md)

**Most comprehensive** model effectiveness ranking with numeric scores (0-100).

**Key Findings:**
- **qwen/qwen3.6-plus:free** is the most versatile free model (top choice for 8/11 agents, 6/8 categories)
- **google/lyria-3-pro-preview:free** is the best free visual model (95/100)
- **qwen/qwen3-coder:free** is the best free coding model (89/100)
- Current configuration is well-optimized but has cost optimization opportunities
- **Provider column added** for clarity (OpenRouter, NVIDIA Build, OpenCode, OpenAI)

**Covers:**
- **11 Agents:** sisyphus, hephaestus, oracle, explore, prometheus, metis, momus, librarian, multimodal-looker, atlas, sisyphus-junior
- **8 Categories:** visual-engineering, ultrabrain, deep, artistry, quick, unspecified-low, unspecified-high, writing

### 2. [Session Learnings - April 4](docs/session-learnings-2026-04-04.md)

Initial analysis session covering:
- Agent architecture insights (11 specialized agents)
- Free model landscape analysis (28 OpenRouter + 91 NVIDIA + OpenCode)
- Effectiveness scoring methodology (0-100 scale)
- Critical discoveries (qwen3.6-plus as "Swiss Army Knife")
- Practical recommendations for configuration

### 3. [Session Learnings - April 5](docs/session-learnings-2026-04-05.md)

Exhaustive search methodology session covering:
- Document structure analysis (3 ranking systems, 65+ tables)
- Category system architecture (8 distinct categories)
- Provider landscape understanding (4 major ecosystems)
- Search methodology insights (parallel agents + multi-pattern grep)
- User request handling ("show me" requires exhaustive discovery)

### 4. [Session Learnings - April 6](docs/session-learnings-2026-04-06.md)

Timeout configuration & system architecture session covering:
- **OpenCode timeout architecture** (3 distinct timeout layers)
- **Critical bug discovery** (Background task fallback ignored - Issue #2203)
- **Configuration management** (Environment variables, provider-level, agent-level)
- **Solution implementation** (OPENCODE_MODEL_TIMEOUT=120000 globally)
- **System architecture insights** (OpenCode core vs. oh-my-opencode plugin)

## Quick Reference: Best Free Models by Agent

| Agent | Best Free Model | Provider | Score |
|-------|-----------------|----------|-------|
| sisyphus | qwen/qwen3.6-plus:free | OpenRouter | 88/100 |
| hephaestus | qwen/qwen3-coder:free | OpenRouter | 89/100 |
| oracle | qwen/qwen3.6-plus:free | OpenRouter | 82/100 |
| explore | qwen/qwen3.6-plus:free | OpenRouter | 90/100 |
| prometheus | qwen/qwen3.6-plus:free | OpenRouter | 85/100 |
| metis | qwen/qwen3.6-plus:free | OpenRouter | 91/100 |
| momus | qwen/qwen3.6-plus:free | OpenRouter | 84/100 |
| librarian | qwen/qwen3.6-plus:free | OpenRouter | 90/100 |
| multimodal-looker | google/lyria-3-pro-preview:free | OpenRouter | 95/100 |
| atlas | qwen/qwen3.6-plus:free | OpenRouter | 90/100 |
| sisyphus-junior | qwen/qwen3.6-plus:free | OpenRouter | 88/100 |

## Quick Reference: Best Free Models by Category

| Category | Best Free Model | Provider | Score | Use Case |
|----------|-----------------|----------|-------|----------|
| visual-engineering | google/lyria-3-pro-preview:free | OpenRouter | 95/100 | Frontend, UI/UX, design |
| ultrabrain | qwen/qwen3.6-plus:free | OpenRouter | 82/100 | Hard logic-heavy tasks |
| deep | qwen/qwen3.6-plus:free | OpenRouter | 85/100 | Autonomous problem-solving |
| artistry | qwen/qwen3.6-plus:free | OpenRouter | 85/100 | Creative solutions |
| quick | qwen/qwen3.6-plus:free | OpenRouter | 92/100 | Trivial tasks, typos |
| unspecified-low | qwen/qwen3.6-plus:free | OpenRouter | 90/100 | Low effort tasks |
| unspecified-high | qwen/qwen3.6-plus:free | OpenRouter | 88/100 | High effort tasks |
| writing | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 88/100 | Documentation, prose |

## Model Sources

### OpenRouter Free Models (28 total)
- Rate limits: 20 req/min, 200 req/day
- Cost: $0 (no credit card required)
- Top models: qwen3.6-plus, qwen3-coder, lyria-3

### NVIDIA Build Free Endpoints (91 total)
- GPU-optimized inference
- Top models: glm5 (744B MoE), nemotron-3-super

### OpenCode Free Models
- opencode/qwen3.6-plus-free
- opencode/gemini-3-flash

### OpenAI Models (Paid)
- gpt-5.4, gpt-5.4-pro, gpt-5.3-codex
- Cost: $0.20-$180 per 1M tokens

## Cost Optimization Recommendations

### Immediate Free Tier Adoption (100% Savings)

| Agent/Category | Switch From | Switch To | Provider | Savings |
|----------------|-------------|-----------|----------|---------|
| explore | nvidia/z-ai/glm5 | qwen/qwen3.6-plus:free | OpenRouter | 100% |
| librarian | opencode/gemini-3-flash | qwen/qwen3.6-plus:free | OpenRouter | 100% |
| quick | nvidia/z-ai/glm5 | qwen/qwen3.6-plus:free | OpenRouter | 100% |
| unspecified-low | nvidia/z-ai/glm5 | qwen/qwen3.6-plus:free | OpenRouter | 100% |
| writing | opencode/gemini-3-flash | meta-llama/llama-3.3-70b-instruct:free | OpenRouter | 100% |

### Keep Paid Models for Critical Tasks

| Agent/Category | Keep Model | Provider | Rationale |
|----------------|-----------|----------|-----------|
| sisyphus | nvidia/z-ai/glm5 | NVIDIA Build | Orchestration requires thinking |
| hephaestus | openai/gpt-5.4 | OpenAI | Best implementation performance |
| oracle | openai/gpt-5.4 | OpenAI | Critical architecture consultation |
| prometheus | openai/gpt-5.4 | OpenAI | Strategic planning needs frontier |
| momus | openai/gpt-5.4 | OpenAI | Quality assurance needs high reasoning |
| ultrabrain | openai/gpt-5.4 | OpenAI | Hard logic tasks need frontier |
| deep | openai/gpt-5.3-codex | OpenAI | Autonomous problem-solving needs strong coding |

## Methodology

**Effectiveness Score (0-100) based on:**
- Task-specific capability matching (40%)
- Context window size (20%)
- Reasoning level requirements (20%)
- Tool support (vision, tools, function calling) (10%)
- Cost efficiency (10%)

## Related Documentation

- [Oh-My-OpenCode Configuration](~/.config/opencode/oh-my-opencode.json)
- [Timeout Configuration Guide](~/.config/opencode/TIMEOUT_CONFIGURATION.md)
- [OpenRouter Free Models](https://openrouter.ai)
- [NVIDIA Build Models](https://build.nvidia.com/models)
- [OpenAI Models](https://developers.openai.com/api/docs/models/all)

## Last Updated

April 6, 2026

**Recent Changes:**
- Added session-learnings-2026-04-06.md documenting timeout configuration & system architecture
- Created TIMEOUT_CONFIGURATION.md with comprehensive timeout guide
- Implemented global timeout reduction (OPENCODE_MODEL_TIMEOUT=120000)
- Documented critical bug: Background task fallback ignored (Issue #2203)
- Added Provider column to all ranking tables (April 5)
- Created session-learnings-2026-04-05.md documenting exhaustive search methodology (April 5)
- Updated README with category rankings quick reference (April 5)
