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
| 1 | nvidia/deepseek-ai/deepseek-v4-flash | NVIDIA Build | 80.2 | 1M | Best speed-heavy balance: free, 1M ctx, SWE-Bench 38% |
| 2 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 80.0 | 256K | Nearly tied #1: free, fast, GPQA 83.5% |
| 3 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 78.5 | 1M | Best paid value: $0.05/$0.20, 1M ctx |
| 4 | nvidia/qwen/qwen3.5-122b-a10b | NVIDIA Build | 78.3 | 262K | Free 122B/10B act MoE, strong search quality |
| 5 | nvidia/z-ai/glm-4.7 | NVIDIA Build | 78.0 | 2.54M | Massive context + SWE 52% |
| 6 | openai/gpt-5.4-nano | OpenAI | 76.8 | 400K | Best OpenAI speed/cost option |

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
| 1 | nvidia/deepseek-ai/deepseek-v4-flash | NVIDIA Build | 80.2 | 1M | Best overall research/search value in refreshed benchmark set |
| 2 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 80.0 | 256K | Free, fast, strong GPQA for doc lookup |
| 3 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 78.5 | 1M | Cheap + 1M context for repository-scale reference work |
| 4 | nvidia/qwen/qwen3.5-122b-a10b | NVIDIA Build | 78.3 | 262K | Strong free MoE research option |
| 5 | nvidia/z-ai/glm-4.7 | NVIDIA Build | 78.0 | 2.54M | Best long-context librarian candidate |
| 6 | openai/gpt-5.4-nano | OpenAI | 76.8 | 400K | Best OpenAI librarian model on cost/perf |

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
| 1 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 93.5 | 1M | Best overall quick model: cheap, fast, smart |
| 2 | nvidia/qwen/qwen3.5-9b | NVIDIA Build | 92.7 | 256K | Frontier reasoning at 9B for tiny fixes |
| 3 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 91.0 | 256K | Free + GPQA 83.5% |

### unspecified-low
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 93.5 | 1M | Best balance for low-effort tasks |
| 2 | nvidia/qwen/qwen3.5-9b | NVIDIA Build | 92.7 | 256K | Strong small-model quality |
| 3 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 91.0 | 256K | Free and fast with excellent GPQA |

### unspecified-high
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | 200K | Needs reasoning |
| 2 | openai/gpt-5.4 | OpenAI | 97 | 1.05M | High reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 128K | Reasoning |

### writing
| Rank | Model | Provider | Score | Context | Rationale |
|---|---|---|---|---|---|
| 1 | nvidia/deepseek-ai/deepseek-v4-pro | NVIDIA Build | 88.9 | 1M | Best writing score: free + strong MMLU/GPQA |
| 2 | nvidia/z-ai/glm-4.7 | NVIDIA Build | 87.7 | 2.54M | Huge context + strong writing benchmarks |
| 3 | nvidia/deepseek-ai/deepseek-v4-flash | NVIDIA Build | 83.2 | 1M | Free, strong general writing quality |

## Summary: Best Model per Agent

| Agent | Model |
|---|---|
| sisyphus | nvidia/z-ai/glm-5.1 |
| hephaestus | openai/gpt-5.4 |
| oracle | nvidia/z-ai/glm-5.1 |
| explore | nvidia/deepseek-ai/deepseek-v4-flash |
| prometheus | nvidia/z-ai/glm-5.1 |
| metis | nvidia/z-ai/glm-5.1 |
| momus | nvidia/z-ai/glm-5.1 |
| librarian | nvidia/deepseek-ai/deepseek-v4-flash |
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
| writing | nvidia/deepseek-ai/deepseek-v4-pro |

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

- Use `nvidia/deepseek-ai/deepseek-v4-flash` or `nvidia/stepfun-ai/step-3.5-flash` for search/research tasks.
- Use `nvidia/nvidia/nemotron-3-nano-30b-a3b` for quick and efficient low-effort tasks.
- Use `openai/gpt-5.4-nano` when you want the best OpenAI speed/cost tradeoff.

## Key Insights

- GLM-5.1 remains the reasoning benchmark leader, but speed-heavy rankings shifted toward cheaper free NVIDIA models.
- DeepSeek-V4-Flash now leads refreshed explore/librarian rankings on the speed-heavy formula.
- Nemotron-3-Nano-30B-A3B remains the best quick/unspecified-low option after the expanded NVIDIA-only refresh.
- DeepSeek-V4-Pro leads refreshed writing rankings, with GPT-5.4-Nano still the strongest OpenAI writing/value option.

## Methodology

Rankings are based on SWE-Bench Pro performance, reasoning capability, context window, cost, and agentic suitability.

## Migration Guide

- nvidia/z-ai/glm5 → nvidia/z-ai/glm-5.1 (deprecated)
- google/gemini-3.1-flash-lite-preview → opencode/gemini-3-flash (provider constraint)
- Removal of all OpenRouter model references.
