# Oh-My-OpenCode Agent Model Rankings v3.0

Date: April 20, 2026

## Executive Summary

- GLM-5.1 is #1 on SWE-Bench Pro (58.4%), released April 18, 2026.
- GLM-5 (nvidia/z-ai/glm5) is DEPRECATED as of April 20, 2026. Migrate to nvidia/z-ai/glm-5.1.
- Only 3 providers allowed: NVIDIA Build, OpenCode Zen, OpenAI.
- google/gemini-3.1-flash-lite-preview replaced with opencode/gemini-3-flash.
- momus agent added back to active config.

## Agent Rankings

### sisyphus
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Orchestrator, xhigh reasoning |
| 2 | openai/gpt-5.4 | OpenAI | 97 | 1.05M | High reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 128K | Reasoning |
| 4 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 92 | 256K | Agentic coding |
| 5 | openai/o3 | OpenAI | 90 | 200K | Reasoning |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 88 | 128K | General purpose |

### hephaestus
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | openai/gpt-5.4 | OpenAI | 98 | 1.05M | Executor, high reasoning |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 97 | 200K | High reasoning |
| 3 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 95 | 256K | Agentic coding |
| 4 | openai/gpt-5.4-mini | OpenAI | 92 | 400K | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 90 | 128K | Coding partner |
| 6 | nvidia/mistral-ai/devstral-2-123b-instruct-2512 | NVIDIA Build | 89 | 256K | Code-focused |

### oracle
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Consultant, xhigh reasoning |
| 2 | openai/gpt-5.4-pro | OpenAI | 98 | 1.05M | Deep reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 96 | 128K | Reasoning |
| 4 | openai/o3 | OpenAI | 94 | 200K | Reasoning |
| 5 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 90 | 256K | Hybrid reasoning |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 88 | 128K | General purpose |

### explore
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 98 | 200K | Search, fast/cheap |
| 2 | opencode/gemini-3-flash | OpenCode Zen | 95 | 128K | Research, fast |
| 3 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 92 | 1M | Quick tasks |
| 4 | openai/gpt-5.4-nano | OpenAI | 90 | 400K | Cost-effective |
| 5 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | NVIDIA Build | 88 | 128K | Edge/quick |
| 6 | openai/o4-mini | OpenAI | 85 | 200K | Cost-effective |

### prometheus
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Planner, xhigh reasoning |
| 2 | openai/gpt-5.4 | OpenAI | 97 | 1.05M | High reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 128K | Reasoning |
| 4 | openai/o3 | OpenAI | 93 | 200K | Reasoning |
| 5 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 91 | 256K | Hybrid reasoning |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 89 | 128K | General purpose |

### metis
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Analyst, xhigh reasoning |
| 2 | openai/gpt-5.4-pro | OpenAI | 98 | 1.05M | Deep reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 96 | 128K | Reasoning |
| 4 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 94 | 256K | Agentic coding |
| 5 | openai/o3 | OpenAI | 92 | 200K | Reasoning |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 90 | 128K | General purpose |

### momus
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Reviewer, xhigh reasoning |
| 2 | openai/gpt-5.4 | OpenAI | 97 | 1.05M | High reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 128K | Reasoning |
| 4 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 93 | 256K | Agentic coding |
| 5 | openai/o3 | OpenAI | 91 | 200K | Reasoning |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 89 | 128K | General purpose |

### librarian
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | opencode/gemini-3-flash | OpenCode Zen | 98 | 128K | Research, fast |
| 2 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 96 | 200K | Fast/cheap |
| 3 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 93 | 1M | Quick tasks |
| 4 | openai/gpt-5.4-mini | OpenAI | 91 | 400K | Cost-effective |
| 5 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | NVIDIA Build | 89 | 128K | Edge/quick |
| 6 | openai/o4-mini | OpenAI | 87 | 200K | Cost-effective |

### multimodal-looker
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/qwen/qwen3.5-397b-a17b | NVIDIA Build | 99 | 128K | VLM with vision |
| 2 | nvidia/meta/llama-3.2-11b-vision-instruct | NVIDIA Build | 95 | 128K | Vision |
| 3 | nvidia/nvidia/nemotron-nano-12b-v2-vl | NVIDIA Build | 92 | 128K | Vision |
| 4 | openai/gpt-5.4 | OpenAI | 90 | 1.05M | High reasoning |
| 5 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 88 | 200K | High reasoning |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 85 | 128K | General purpose |

### atlas
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 98 | 200K | Knowledge, medium reasoning |
| 2 | openai/gpt-5.4 | OpenAI | 96 | 1.05M | High reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 94 | 128K | Reasoning |
| 4 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 92 | 256K | Agentic coding |
| 5 | openai/o3 | OpenAI | 90 | 200K | Reasoning |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 88 | 128K | General purpose |

### sisyphus-junior
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 99 | 1M | Orchestrator-junior, medium reasoning |
| 2 | nvidia/z-ai/glm-4.7 | NVIDIA Build | 96 | 128K | Agentic coding |
| 3 | nvidia/google/gemma-4-31b-it | NVIDIA Build | 93 | 256K | Coding+agentic |
| 4 | openai/gpt-5.4-mini | OpenAI | 91 | 400K | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 89 | 128K | Coding partner |
| 6 | nvidia/meta/llama-3.3-70b-instruct | NVIDIA Build | 87 | 128K | General purpose |

## Category Rankings

### visual-engineering
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/qwen/qwen3.5-397b-a17b | NVIDIA Build | 99 | 128K | VLM with vision |
| 2 | nvidia/meta/llama-3.2-11b-vision-instruct | NVIDIA Build | 95 | 128K | Vision |
| 3 | nvidia/nvidia/nemotron-nano-12b-v2-vl | NVIDIA Build | 92 | 128K | Vision |

### ultrabrain
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Needs top reasoning |
| 2 | openai/gpt-5.4-pro | OpenAI | 98 | 1.05M | Deep reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 96 | 128K | Reasoning |

### deep
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 99 | 256K | Best agentic coding |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 97 | 200K | High reasoning |
| 3 | openai/gpt-5.4 | OpenAI | 95 | 1.05M | High reasoning |

### artistry
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 98 | 256K | Hybrid instruct+reasoning |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 96 | 200K | High reasoning |
| 3 | openai/gpt-5.4 | OpenAI | 94 | 1.05M | High reasoning |

### quick
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 99 | 1M | Fast, cheap |
| 2 | opencode/gemini-3-flash | OpenCode Zen | 97 | 128K | Fast research |
| 3 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | NVIDIA Build | 95 | 128K | Edge/quick |

### unspecified-low
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 99 | 1M | Efficient |
| 2 | opencode/gemini-3-flash | OpenCode Zen | 97 | 128K | Fast research |
| 3 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | NVIDIA Build | 95 | 128K | Edge/quick |

### unspecified-high
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Needs reasoning |
| 2 | openai/gpt-5.4 | OpenAI | 97 | 1.05M | High reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 128K | Reasoning |

### writing
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | opencode/gemini-3-flash | OpenCode Zen | 98 | 128K | Fast research |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 96 | 200K | High reasoning |
| 3 | openai/gpt-5.4 | OpenAI | 94 | 1.05M | High reasoning |

## Summary: Best Model per Agent

| Agent | Model |
|---|---|
| sisyphus | nvidia/z-ai/glm-5.1 |
| hephaestus | openai/gpt-5.4 |
| oracle | nvidia/z-ai/glm-5.1 |
| explore | nvidia/stepfun-ai/step-3.5-flash |
| prometheus | nvidia/z-ai/glm-5.1 |
| metis | nvidia/z-ai/glm-5.1 |
| momus | nvidia/z-ai/glm-5.1 |
| librarian | opencode/gemini-3-flash |
| multimodal-looker | nvidia/qwen/qwen3.5-397b-a17b |
| atlas | nvidia/z-ai/glm-5.1 |
| sisyphus-junior | nvidia/nvidia/nemotron-3-super-120b-a12b |

## Summary: Best Model per Category

| Category | Model |
|---|---|
| visual-engineering | nvidia/qwen/qwen3.5-397b-a17b |
| ultrabrain | nvidia/z-ai/glm-5.1 |
| deep | nvidia/qwen/qwen3-coder-480b-a35b-instruct |
| artistry | nvidia/mistral-ai/mistral-small-4-119b-2603 |
| quick | nvidia/nvidia/nemotron-3-nano-30b-a3b |
| unspecified-low | nvidia/nvidia/nemotron-3-nano-30b-a3b |
| unspecified-high | nvidia/z-ai/glm-5.1 |
| writing | opencode/gemini-3-flash |

## Model Provider Summary

### NVIDIA Build
- High performance, free models, specialized agentic coding models.
- Best for: Reasoning, coding, vision, quick tasks.

### OpenCode Zen
- Curated models, reliable routing.
- Best for: Research, general purpose, coding.

### OpenAI
- High reasoning, large context.
- Best for: Complex tasks, deep reasoning.

## Cost Optimization

- Use `nvidia/stepfun-ai/step-3.5-flash` or `opencode/gemini-3-flash` for quick/research tasks.
- Use `nvidia/nvidia/nemotron-3-nano-30b-a3b` for efficient tasks.
- Use `openai/gpt-5.4-mini` or `openai/gpt-5.4-nano` for cost-effective reasoning.

## Key Insights

- GLM-5.1 is the new standard for reasoning and agentic tasks.
- NVIDIA Build provides the most cost-effective and high-performance options.
- OpenCode Zen is essential for reliable routing and curated models.
- OpenAI remains a strong choice for deep reasoning and large context.

## Methodology

Rankings are based on SWE-Bench Pro performance, reasoning capability, context window, cost, and agentic suitability.

## Migration Guide

- nvidia/z-ai/glm5 → nvidia/z-ai/glm-5.1 (deprecated)
- google/gemini-3.1-flash-lite-preview → opencode/gemini-3-flash (provider constraint)
- Removal of all OpenRouter model references.
