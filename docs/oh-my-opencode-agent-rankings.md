# Oh-My-OpenCode Agent Model Rankings v4.0

Date: April 29, 2026

## Executive Summary

- **GPT-5.5** (released April 23, 2026) is new OpenAI flagship model, ranks #2 for reasoning-heavy agents.
- **GLM-5.1** remains #1 overall (free, 58.4% SWE-Bench Pro).
- **GPT-5.5-pro** introduced as premium variant ($30/$180 per 1M tokens).
- **GPT-5.4-pro** now officially ranked (previously unlisted).
- **o4-mini** deprecated (replaced by GPT-5.4-mini/GPT-5-mini).
- Only 3 providers allowed: NVIDIA Build, OpenCode Zen, OpenAI.

## Agent Rankings

### sisyphus
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Orchestrator, xhigh reasoning, free |
| 2 | openai/gpt-5.5 | OpenAI | 97 | 1.05M | New flagship, high reasoning, $5/$30 |
| 3 | openai/gpt-5.4 | OpenAI | 96 | 1.05M | High reasoning, cost-effective |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 128K | Reasoning, free |
| 5 | openai/gpt-5.5-pro | OpenAI | 94 | 1.05M | Premium reasoning, $30/$180 |
| 6 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 92 | 256K | Agentic coding, free |

### hephaestus
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | openai/gpt-5.4 | OpenAI | 98 | 1.05M | Executor, high reasoning, $2.5/$15 |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 97 | 200K | High reasoning, free |
| 3 | openai/gpt-5.5 | OpenAI | 96 | 1.05M | New flagship coding, $5/$30 |
| 4 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 95 | 256K | Agentic coding, free |
| 5 | openai/gpt-5.4-mini | OpenAI | 92 | 400K | Cost-effective, $0.75/$4.5 |
| 6 | opencode/qwen3-coder | OpenCode Zen | 90 | 128K | Coding partner |

### oracle
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Consultant, xhigh reasoning, free |
| 2 | openai/gpt-5.5 | OpenAI | 98 | 1.05M | Deep reasoning, $5/$30 |
| 3 | openai/gpt-5.4-pro | OpenAI | 97 | 1.05M | Deep reasoning, $30/$180 |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 96 | 128K | Reasoning, free |
| 5 | openai/o3-pro | OpenAI | 94 | 200K | Reasoning specialist, $20/$80 |
| 6 | openai/o3 | OpenAI | 92 | 200K | Reasoning, $2/$8 |

### explore
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/deepseek-ai/deepseek-v4-flash | NVIDIA Build | 80.2 | 1M | Best speed-heavy: free, 1M ctx |
| 2 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 80.0 | 256K | Nearly tied #1: free, fast |
| 3 | openai/gpt-5.4-nano | OpenAI | 78.5 | 400K | Best paid value: $0.20/$1.25 |
| 4 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 78.0 | 1M | Low cost: $0.05/$0.20 |
| 5 | openai/gpt-5.4-mini | OpenAI | 76.5 | 400K | Cost-effective: $0.75/$4.5 |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 75.0 | 128K | General purpose |

### prometheus
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Planner, xhigh reasoning, free |
| 2 | openai/gpt-5.5 | OpenAI | 97 | 1.05M | New flagship planning, $5/$30 |
| 3 | openai/gpt-5.4 | OpenAI | 96 | 1.05M | High reasoning, $2.5/$15 |
| 4 | openai/gpt-5.5-pro | OpenAI | 95 | 1.05M | Premium planning, $30/$180 |
| 5 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 94 | 128K | Reasoning, free |
| 6 | openai/o3-pro | OpenAI | 92 | 200K | Reasoning specialist, $20/$80 |

### metis
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Analyst, xhigh reasoning, free |
| 2 | openai/gpt-5.5 | OpenAI | 98 | 1.05M | New analyst, $5/$30 |
| 3 | openai/gpt-5.4-pro | OpenAI | 97 | 1.05M | Deep analysis, $30/$180 |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 96 | 128K | Reasoning, free |
| 5 | openai/o3-pro | OpenAI | 94 | 200K | Reasoning specialist, $20/$80 |
| 6 | openai/gpt-5.4 | OpenAI | 93 | 1.05M | Cost-effective analysis, $2.5/$15 |

### momus
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Critic, xhigh reasoning, free |
| 2 | openai/gpt-5.5 | OpenAI | 98 | 1.05M | New critic, $5/$30 |
| 3 | openai/gpt-5.4-pro | OpenAI | 97 | 1.05M | Deep criticism, $30/$180 |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 96 | 128K | Reasoning, free |
| 5 | openai/o3-pro | OpenAI | 94 | 200K | Reasoning specialist, $20/$80 |
| 6 | openai/gpt-5.4 | OpenAI | 93 | 1.05M | Cost-effective criticism, $2.5/$15 |

### librarian
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/deepseek-ai/deepseek-v4-flash | NVIDIA Build | 80.2 | 1M | Research: free, 1M ctx |
| 2 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 80.0 | 256K | Research: free, fast |
| 3 | openai/gpt-5.4-nano | OpenAI | 78.5 | 400K | Best paid research: $0.20/$1.25 |
| 4 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 78.0 | 1M | Low-cost research: $0.05/$0.20 |
| 5 | openai/gpt-5.4-mini | OpenAI | 76.5 | 400K | Cost-effective: $0.75/$4.5 |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 75.0 | 128K | General research |

### multimodal-looker
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | openai/gpt-5.5 | OpenAI | 99 | 1.05M | Vision: new flagship, $5/$30 |
| 2 | nvidia/qwen/qwen3.5-397b-a17b | NVIDIA Build | 98 | 256K | Vision: free, high MMMU-Pro |
| 3 | openai/gpt-5.4 | OpenAI | 97 | 1.05M | Vision: cost-effective, $2.5/$15 |
| 4 | openai/gpt-5.4-pro | OpenAI | 96 | 1.05M | Premium vision, $30/$180 |
| 5 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 95 | 200K | Vision reasoning, free |
| 6 | nvidia/meta/llama-3.2-11b-vision-instruct | NVIDIA Build | 90 | 128K | Pure vision, free |

### atlas
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Knowledge, xhigh reasoning, free |
| 2 | openai/gpt-5.5 | OpenAI | 97 | 1.05M | New knowledge, $5/$30 |
| 3 | openai/gpt-5.4 | OpenAI | 96 | 1.05M | High reasoning, $2.5/$15 |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 128K | Reasoning, free |
| 5 | openai/gpt-5.5-pro | OpenAI | 94 | 1.05M | Premium knowledge, $30/$180 |
| 6 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 92 | 256K | Agentic knowledge, free |

### sisyphus-junior
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 99 | 1M | Junior orchestrator, free |
| 2 | openai/gpt-5.4-mini | OpenAI | 96 | 400K | Cost-effective junior, $0.75/$4.5 |
| 3 | openai/gpt-5.5 | OpenAI | 95 | 1.05M | New junior, $5/$30 |
| 4 | nvidia/z-ai/glm4.7 | NVIDIA Build | 94 | 256K | Junior reasoning, free |
| 5 | openai/gpt-5.4-nano | OpenAI | 92 | 400K | Low-cost junior, $0.20/$1.25 |
| 6 | nvidia/google/gemma-4-31b-it | NVIDIA Build | 90 | 128K | Stable junior, free |

## Category Rankings

### visual-engineering
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/qwen/qwen3.5-397b-a17b | NVIDIA Build | 99 | 256K | Frontend, UI/UX, design, free |
| 2 | openai/gpt-5.5 | OpenAI | 98 | 1.05M | New vision flagship, $5/$30 |
| 3 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 97 | 200K | Design reasoning, free |
| 4 | openai/gpt-5.4 | OpenAI | 96 | 1.05M | Cost-effective vision, $2.5/$15 |
| 5 | nvidia/meta/llama-3.2-11b-vision-instruct | NVIDIA Build | 95 | 128K | Pure vision, free |
| 6 | openai/gpt-5.4-pro | OpenAI | 94 | 1.05M | Premium vision, $30/$180 |

### ultrabrain
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Hard logic, xhigh reasoning, free |
| 2 | openai/gpt-5.5 | OpenAI | 98 | 1.05M | New logic flagship, $5/$30 |
| 3 | openai/gpt-5.4-pro | OpenAI | 97 | 1.05M | Premium logic, $30/$180 |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 96 | 128K | Logic, free |
| 5 | openai/o3-pro | OpenAI | 95 | 200K | Reasoning specialist, $20/$80 |
| 6 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 94 | 256K | Agentic logic, free |

### deep
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 99 | 256K | Autonomous problem-solving, free |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 98 | 200K | Deep reasoning, free |
| 3 | openai/gpt-5.5 | OpenAI | 97 | 1.05M | New autonomous, $5/$30 |
| 4 | openai/gpt-5.4 | OpenAI | 96 | 1.05M | Cost-effective deep, $2.5/$15 |
| 5 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 128K | Deep reasoning, free |
| 6 | openai/gpt-5.4-pro | OpenAI | 94 | 1.05M | Premium deep, $30/$180 |

### artistry
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Creative solutions, xhigh reasoning, free |
| 2 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 98 | 256K | Creative coding, free |
| 3 | openai/gpt-5.5 | OpenAI | 97 | 1.05M | New creative, $5/$30 |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 96 | 128K | Creative reasoning, free |
| 5 | openai/gpt-5.4 | OpenAI | 95 | 1.05M | Cost-effective creative, $2.5/$15 |
| 6 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 94 | 256K | Fast creative, free |

### quick
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 93.5 | 1M | Trivial tasks, $0.05/$0.20 |
| 2 | openai/gpt-5.4-nano | OpenAI | 92.5 | 400K | Quick OpenAI, $0.20/$1.25 |
| 3 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 91.0 | 256K | Fast free, free |
| 4 | openai/gpt-5.4-mini | OpenAI | 90.0 | 400K | Cost-effective quick, $0.75/$4.5 |
| 5 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | NVIDIA Build | 88.5 | 128K | Ultra-low cost, $0.01/$0.05 |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 87.0 | 128K | General quick |

### unspecified-low
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 93.5 | 1M | Low effort tasks, $0.05/$0.20 |
| 2 | openai/gpt-5.4-nano | OpenAI | 92.5 | 400K | Low-cost OpenAI, $0.20/$1.25 |
| 3 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 91.0 | 256K | Fast free, free |
| 4 | openai/gpt-5.4-mini | OpenAI | 90.0 | 400K | Cost-effective, $0.75/$4.5 |
| 5 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | NVIDIA Build | 88.5 | 128K | Ultra-low cost, $0.01/$0.05 |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 87.0 | 128K | General low effort |

### unspecified-high
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | High effort tasks, xhigh reasoning, free |
| 2 | openai/gpt-5.5 | OpenAI | 97 | 1.05M | New high effort, $5/$30 |
| 3 | openai/gpt-5.4 | OpenAI | 96 | 1.05M | Cost-effective high, $2.5/$15 |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 128K | High reasoning, free |
| 5 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 94 | 256K | Agentic high, free |
| 6 | openai/gpt-5.5-pro | OpenAI | 93 | 1.05M | Premium high, $30/$180 |

### writing
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/deepseek-ai/deepseek-v4-pro | NVIDIA Build | 88.9 | 1M | Documentation, prose, free |
| 2 | nvidia/z-ai/glm4.7 | NVIDIA Build | 87.5 | 256K | Writing reasoning, free |
| 3 | openai/gpt-5.4-mini | OpenAI | 86.0 | 400K | Cost-effective writing, $0.75/$4.5 |
| 4 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 85.5 | 256K | Fast writing, free |
| 5 | openai/gpt-5.4-nano | OpenAI | 84.0 | 400K | Low-cost writing, $0.20/$1.25 |
| 6 | nvidia/minimaxai/minimax-m2.7 | NVIDIA Build | 83.0 | 128K | Specialized writing, free |

## New Models Summary

### GPT-5.5 (OpenAI)
- **Released**: April 23, 2026
- **Pricing**: $5.00/$30.00 per 1M tokens (input/output)
- **Context**: 1.05M tokens
- **Max Output**: 128K tokens
- **Capabilities**: Text, Image input, Vision, Function calling, Structured outputs, Tools
- **Reasoning**: Yes (supports: none, low, medium, high, xhigh)
- **Ranking Impact**: #2 for reasoning-heavy agents, #1 for multimodal-looker

### GPT-5.5 Pro (OpenAI)
- **Pricing**: $30.00/$180.00 per 1M tokens
- **Context**: 1.05M tokens
- **Capabilities**: Same as GPT-5.5 with extended reasoning
- **Ranking Impact**: Premium option, appears in top 6 for reasoning agents

### GPT-5.4 Pro (OpenAI)
- **Now Officially Listed**: Previously unranked, now in pricing docs
- **Pricing**: $30.00/$180.00 per 1M tokens
- **Context**: 1.05M tokens
- **Ranking Impact**: #3 for oracle, metis, momus

## Deprecated Models

- **o4-mini**: Deprecated (replaced by GPT-5.4-mini/GPT-5-mini)
- **computer-use-preview**: Deprecated (use GPT-5.5 + computer tool)
- **GPT-5.1 series**: Being retired July 23, 2026
- **GPT-5.2-Codex**: Deprecated (replaced by GPT-5.4)

## Methodology Updates

Rankings incorporate latest benchmark data (SWE-Bench Verified as of April 29, 2026) and updated model specifications. Scoring follows same methodology as v3.0:

- **Task-specific capability**: 40% (benchmark performance)
- **Context window**: 20% (agent-appropriate sizing)
- **Reasoning level**: 20% (support for reasoning effort levels)
- **Tool support**: 10% (function calling, structured outputs)
- **Cost efficiency**: 10% (price per 1M tokens)

## Migration Guide (v3.0 → v4.0)

| Change | Action |
|---|---|
| multimodal-looker uses GPT-5.5 | Update config: `"model": "openai/gpt-5.5"` |
| GPT-5.5 available for reasoning agents | Consider for fallback models |
| o4-mini deprecated | Remove from configs, use GPT-5.4-mini |
| GPT-5.4-pro now ranked | Can be used for premium reasoning |

## Cost Optimization

| Task Type | Recommended Model | Cost | Context |
|---|---|---|---|
| Quick/trivial | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | $0.05/$0.20 | 1M |
| Search/research | `nvidia/deepseek-ai/deepseek-v4-flash` | FREE | 1M |
| Reasoning-heavy | `nvidia/z-ai/glm-5.1` | FREE | 200K |
| Vision-heavy | `openai/gpt-5.5` | $5/$30 | 1.05M |
| Cost-effective reasoning | `openai/gpt-5.4` | $2.5/$15 | 1.05M |
| Premium reasoning | `openai/gpt-5.5-pro` | $30/$180 | 1.05M |

## Next Steps

1. Update `oh-my-opencode.json` config with GPT-5.5 for multimodal-looker
2. Consider GPT-5.5 for reasoning agent fallback chains
3. Monitor NVIDIA Build for GLM-5.2 or similar updates
4. Watch for GPT-5.6 expected Q3 2026

---
*Generated April 29, 2026. Based on NVIDIA Build, OpenCode Zen, and OpenAI models as of this date.*