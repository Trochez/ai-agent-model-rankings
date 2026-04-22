# Explorer Project

AI agent model rankings and optimization research for oh-my-opencode configuration.

## Project Structure

```
explorer/
├── docs/
│   ├── oh-my-opencode-agent-rankings.md          # v3.0 rankings (current, April 20)
│   ├── oh-my-opencode-agent-rankings-2026-04-06.md # v2.0 rankings (historical, superseded)
│   ├── oh-my-opencode-reference.json             # Working config reference (v3.0)
│   ├── session-learnings-2026-04-04.md           # Session 1: Agent architecture insights
│   ├── session-learnings-2026-04-05.md           # Session 2: Exhaustive search methodology
│   ├── session-learnings-2026-04-06.md           # Session 3: Timeout configuration & system architecture
│   ├── session-learnings-2026-04-06-fallback-investigation.md  # Session 4: Fallback configuration
│   ├── session-learnings-2026-04-06-model-id-investigation.md  # Session 5: Model ID investigation
│   ├── session-learnings-2026-04-07.md           # Session 6: Model config updates & visual engineering
│   ├── session-learnings-2026-04-07-model-configuration-fix.md # Session 7: Model config verification
│   ├── session-learnings-2026-04-08.md           # Session 8: OMO-Team skill creation
│   ├── session-learnings-2026-04-13.md           # Session 9: Extended rankings & dual system architecture
│   ├── session-learnings-2026-04-13-documentation.md           # Session 10: Model testing & verification
│   ├── extended-rankings-visual-engineering.md   # Extended ranking (historical, pre-v3.0)
│   ├── extended-rankings-artistry.md             # Extended ranking (historical, pre-v3.0)
│   └── extended-rankings-writing.md              # Extended ranking (historical, pre-v3.0)
├── .omx/
│   └── model-rankings-report.md                  # OpenCode Zen agent rankings (25 agents)
└── README.md                                     # This file
```

## Key Documents

### [Oh-My-OpenCode Agent Rankings v3.0](docs/oh-my-opencode-agent-rankings.md) (Current)

Comprehensive model rankings using only NVIDIA Build, OpenCode Zen, and OpenAI providers.

**Key Findings:**
- **nvidia/z-ai/glm-5.1** is #1 on SWE-Bench Pro (58.4%), released April 18, 2026
- **nvidia/z-ai/glm5** is DEPRECATED — migrate to `nvidia/z-ai/glm-5.1`
- Only 3 providers allowed: NVIDIA Build, OpenCode Zen, OpenAI
- `google/gemini-3.1-flash-lite-preview` replaced with `opencode/gemini-3-flash`
- momus agent added back to active config

### [Oh-My-OpenCode Agent Rankings v2.0](docs/oh-my-opencode-agent-rankings-2026-04-06.md) (Historical)

Superseded by v3.0. Contains OpenRouter model references and pre-GLM-5.1 rankings. Retained for historical reference only.

## Quick Reference: Best Model per Agent (v3.0)

| Agent | Best Model | Provider | Score |
|-------|-----------|----------|-------|
| sisyphus | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| hephaestus | `openai/gpt-5.4` | OpenAI | 98 |
| oracle | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| explore | `nvidia/stepfun-ai/step-3.5-flash` | NVIDIA Build | 98 |
| prometheus | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| metis | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| momus | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| librarian | `opencode/gemini-3-flash` | OpenCode Zen | 98 |
| multimodal-looker | `nvidia/qwen/qwen3.5-397b-a17b` | NVIDIA Build | 99 |
| atlas | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 98 |
| sisyphus-junior | `nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Build | 99 |

## Quick Reference: Best Model per Category (v3.0)

| Category | Best Model | Provider | Score | Use Case |
|----------|-----------|----------|-------|----------|
| visual-engineering | `nvidia/qwen/qwen3.5-397b-a17b` | NVIDIA Build | 99 | Frontend, UI/UX, design |
| ultrabrain | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 | Hard logic-heavy tasks |
| deep | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | NVIDIA Build | 99 | Autonomous problem-solving |
| artistry | `nvidia/mistral-ai/mistral-small-4-119b-2603` | NVIDIA Build | 98 | Creative solutions |
| quick | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | 99 | Trivial tasks, typos |
| unspecified-low | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | 99 | Low effort tasks |
| unspecified-high | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 | High effort tasks |
| writing | `opencode/gemini-3-flash` | OpenCode Zen | 98 | Documentation, prose |

## Model Providers

### NVIDIA Build (`nvidia/` prefix)
- GPU-optimized inference, 200+ models
- Free tier available for most models
- Specialized: reasoning, coding, vision, agentic
- Key models: glm-5.1, qwen3-coder-480b, step-3.5-flash, nemotron-3-super

### OpenCode Zen (`opencode/` prefix)
- Curated, tested models for coding agents
- Reliable routing, no rate limit issues
- Key models: gemini-3-flash, qwen3-coder, qwen3.6-plus

### OpenAI (`openai/` prefix)
- Frontier reasoning, large context windows
- Paid only ($0.20-$180 per 1M tokens)
- Key models: gpt-5.4, gpt-5.4-pro, o3, o4-mini

> Only NVIDIA Build, OpenCode Zen, and OpenAI models are used. No OpenRouter or direct Google models.

## Cost Optimization

| Task Type | Recommended Model | Cost | Context |
|-----------|------------------|------|---------|
| Quick/trivial | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | $0.05/$0.20 | 1M |
| Search/research | `nvidia/stepfun-ai/step-3.5-flash` | FREE | 200K |
| Research/writing | `opencode/gemini-3-flash` | $0.50/$3.00 | 128K |
| Junior tasks | `nvidia/nvidia/nemotron-3-super-120b-a12b` | $0.10/$0.50 | 1M |
| Cost-effective reasoning | `openai/gpt-5.4-mini` | $0.75/$4.50 | 400K |

## Migration Guide (v2.0 → v3.0)

| Old Model | New Model | Reason |
|-----------|-----------|--------|
| `nvidia/z-ai/glm5` | `nvidia/z-ai/glm-5.1` | Deprecated April 20, 2026 |
| `google/gemini-3.1-flash-lite-preview` | `opencode/gemini-3-flash` | Provider constraint |
| `openai/gpt-5.3-codex` | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | Being retired June 5, 2026 |
| All OpenRouter models | NVIDIA Build equivalents | Provider constraint |

## Methodology

Rankings are based on SWE-Bench Pro performance, reasoning capability, context window, cost, and agentic suitability. See [v3.0 rankings doc](docs/oh-my-opencode-agent-rankings.md) for full methodology.

## Related Documentation

- [Global Config](~/.config/opencode/oh-my-opencode.json)
- [v3.0 Rankings](docs/oh-my-opencode-agent-rankings.md)
- [NVIDIA Build Models](https://build.nvidia.com/models)
- [OpenAI Models](https://developers.openai.com/api/docs/models/all)

## Last Updated

April 20, 2026
