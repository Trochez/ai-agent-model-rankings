# OpenCode Model Ranking (v3.0)

**Session ID**: ses_2a8f5ef4fffe4j4L3wntR3DQeK (original)
**Date**: April 21, 2026 (v3.0 update)
**Agent**: Sisyphus
**Provider Constraint**: Only NVIDIA Build, OpenCode Zen, and OpenAI models. No OpenRouter or direct Google models.

---

## Executive Summary

Comprehensive analysis mapping **30 OpenCode agents** to optimal models across **3 providers** (NVIDIA Build, OpenCode Zen, and OpenAI). All OpenRouter references removed. GLM-5.1 is the new #1 model (SWE-Bench Pro 58.4%).

---

## Key Findings

### Top Models by Use Case

1. **nvidia/z-ai/glm-5.1** — NVIDIA Build (FREE)
   - Best for: architect, analyst, planner, security-reviewer, code-reviewer, critic
   - Score range: 95-99 across reasoning agents
   - #1 SWE-Bench Pro (58.4%), 200K ctx, thinking enabled

2. **nvidia/qwen/qwen3-coder-480b-a35b-instruct** — NVIDIA Build (FREE)
   - Best for: executor, build-fixer, git-master, ultraqa, worker
   - Score range: 93-97 across coding agents
   - Best agentic coding model, 256K ctx

3. **nvidia/stepfun-ai/step-3.5-flash** — NVIDIA Build (FREE)
   - Best for: explore, style-reviewer, trace, doctor, help, cancel
   - Score range: 87-96 across fast agents
   - 200B MoE, fast, FREE

4. **opencode/gemini-3-flash** — OpenCode Zen ($0.50/$3.00)
   - Best for: researcher, writer, deep-research
   - Score range: 89-98 across research/writing agents
   - Web-native, fast, optimized for documentation

5. **nvidia/qwen/qwen3.5-397b-a17b** — NVIDIA Build
   - Best for: vision, visual-verdict, frontend-ui-ux
   - Score range: 89-99 across vision agents
   - VLM with vision, 128K ctx

---

## Model Sources

### NVIDIA Build (200+ Models)
- Free tier available for most models
- Specializes: GPU-optimized inference, agentic workflows
- Key models: glm-5.1, qwen3-coder-480b, step-3.5-flash, nemotron-3-super
- Model ID format: `nvidia/publisher/model-name`

### OpenCode Zen (Curated Models)
- Models: gemini-3-flash, qwen3-coder, qwen3.6-plus
- Reliable routing, no rate limit issues
- Cost: $0.45-$3.00 per 1M tokens

### OpenAI (Paid Tier)
- Flagship: gpt-5.4, gpt-5.4-pro, o3
- Efficient: gpt-5.4-mini, gpt-5.4-nano, o4-mini
- Cost: $0.20-$180 per 1M tokens

---

## Agent Categories

### Frontier Agents (High Reasoning)
- architect, analyst, planner, security-reviewer
- code-reviewer, test-engineer, critic, code-simplifier
- team-executor

### Standard Agents (Balanced)
- executor, debugger, verifier, quality-reviewer
- api-reviewer, performance-reviewer, dependency-expert
- quality-strategist, build-fixer, designer
- git-master, product-manager, ux-researcher
- information-architect, product-analyst

### Fast-Lane Agents (Speed Priority)
- explore, style-reviewer, writer, researcher
- vision, qa-tester

---

## Detailed Agent Rankings

### Frontier Agents

#### architect
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | #1 SWE-Bench, FREE |
| 2 | openai/gpt-5.4-pro | OpenAI | 97 | Deep reasoning, $30/$180 |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 95 | 685B reasoning |
| 4 | openai/gpt-5.4 | OpenAI | 93 | High reasoning |
| 5 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 91 | Agentic coding |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 87 | General purpose |

#### analyst
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 98 | Best for analysis |
| 2 | openai/gpt-5.4-pro | OpenAI | 96 | Deep reasoning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 93 | 685B reasoning |
| 4 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 90 | Code analysis |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 86 | General purpose |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 83 | 1M ctx |

#### planner
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 97 | Strategic planning |
| 2 | openai/gpt-5.4-pro | OpenAI | 95 | Complex planning |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 92 | Reasoning |
| 4 | openai/o3 | OpenAI | 90 | Reasoning |
| 5 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 88 | Hybrid reasoning |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 86 | General purpose |

#### security-reviewer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 99 | Security-critical |
| 2 | openai/gpt-5.4-pro | OpenAI | 97 | OWASP analysis |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 94 | Security patterns |
| 4 | openai/o3 | OpenAI | 91 | Security reasoning |
| 5 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 85 | Code security |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 82 | Agentic security |

#### code-reviewer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 98 | Comprehensive review |
| 2 | openai/gpt-5.4-pro | OpenAI | 96 | Quality + security |
| 3 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 93 | Code patterns |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 90 | Multi-file review |
| 5 | opencode/qwen3-coder | OpenCode Zen | 87 | Cost-effective |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 84 | Agentic analysis |

#### test-engineer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 96 | Test generation |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 94 | Test strategy |
| 3 | nvidia/mistral-ai/devstral-2-123b-instruct-2512 | NVIDIA Build | 92 | Code-focused |
| 4 | openai/gpt-5.4-mini | OpenAI | 89 | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 86 | Coding partner |
| 6 | nvidia/meta/llama-3.3-70b-instruct | NVIDIA Build | 82 | General purpose |

#### critic
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 97 | Critical analysis |
| 2 | openai/gpt-5.4-pro | OpenAI | 95 | Quality assessment |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 92 | Deep evaluation |
| 4 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 89 | Code evaluation |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 85 | General review |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 82 | Agentic review |

#### code-simplifier
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 95 | Code refactoring |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 93 | Simplification logic |
| 3 | nvidia/mistral-ai/devstral-2-123b-instruct-2512 | NVIDIA Build | 91 | Code-focused |
| 4 | openai/gpt-5.4-mini | OpenAI | 88 | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 86 | Coding partner |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 83 | Agentic simplification |

#### team-executor
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 94 | Team orchestration |
| 2 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 92 | Worker coordination |
| 3 | openai/gpt-5.4 | OpenAI | 90 | Complex workflows |
| 4 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 88 | 1M ctx |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 85 | General purpose |
| 6 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 82 | Hybrid reasoning |

---

### Standard Agents

#### executor
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | openai/gpt-5.4 | OpenAI | 98 | Frontier coding |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 97 | High reasoning |
| 3 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 95 | Agentic coding |
| 4 | openai/gpt-5.4-mini | OpenAI | 92 | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 90 | Coding partner |
| 6 | nvidia/mistral-ai/devstral-2-123b-instruct-2512 | NVIDIA Build | 89 | Code-focused |

#### debugger
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 96 | Best for debugging |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 94 | Root cause analysis |
| 3 | nvidia/mistral-ai/devstral-2-123b-instruct-2512 | NVIDIA Build | 92 | Code-focused |
| 4 | openai/gpt-5.4-mini | OpenAI | 89 | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 87 | Coding partner |
| 6 | nvidia/meta/llama-3.3-70b-instruct | NVIDIA Build | 83 | General purpose |

#### verifier
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 96 | Verification logic |
| 2 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 93 | Code verification |
| 3 | openai/gpt-5.4 | OpenAI | 91 | High reasoning |
| 4 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 88 | Hybrid reasoning |
| 5 | opencode/qwen3-coder | OpenCode Zen | 85 | Coding partner |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 82 | Agentic verification |

#### quality-reviewer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 97 | Quality assessment |
| 2 | openai/gpt-5.4-pro | OpenAI | 95 | Deep quality review |
| 3 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 92 | Code quality |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 89 | Multi-file review |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 85 | General review |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 82 | Agentic review |

#### api-reviewer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 96 | API design review |
| 2 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 93 | API patterns |
| 3 | openai/gpt-5.4 | OpenAI | 91 | API reasoning |
| 4 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 88 | Hybrid reasoning |
| 5 | opencode/qwen3-coder | OpenCode Zen | 85 | Coding partner |
| 6 | nvidia/meta/llama-3.3-70b-instruct | NVIDIA Build | 81 | General purpose |

#### performance-reviewer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 95 | Performance analysis |
| 2 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 92 | Code optimization |
| 3 | openai/gpt-5.4 | OpenAI | 90 | Performance reasoning |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 87 | Deep analysis |
| 5 | opencode/qwen3-coder | OpenCode Zen | 84 | Coding partner |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 81 | Agentic analysis |

#### dependency-expert
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 94 | Dependency analysis |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 92 | Version reasoning |
| 3 | nvidia/mistral-ai/devstral-2-123b-instruct-2512 | NVIDIA Build | 90 | Code-focused |
| 4 | openai/gpt-5.4-mini | OpenAI | 87 | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 85 | Coding partner |
| 6 | nvidia/meta/llama-3.3-70b-instruct | NVIDIA Build | 80 | General purpose |

#### quality-strategist
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 96 | Strategy reasoning |
| 2 | openai/gpt-5.4-pro | OpenAI | 94 | Deep strategy |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 91 | Complex analysis |
| 4 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 88 | Hybrid reasoning |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 85 | General purpose |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 82 | Agentic strategy |

#### build-fixer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 97 | Best for build fixes |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 95 | Type error resolution |
| 3 | nvidia/mistral-ai/devstral-2-123b-instruct-2512 | NVIDIA Build | 93 | Code-focused |
| 4 | openai/gpt-5.4-mini | OpenAI | 90 | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 88 | Coding partner |
| 6 | nvidia/meta/llama-3.3-70b-instruct | NVIDIA Build | 84 | General purpose |

#### designer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3.5-397b-a17b | NVIDIA Build | 95 | VLM with vision |
| 2 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 93 | Creative design |
| 3 | opencode/gemini-3-flash | OpenCode Zen | 91 | Web-native design |
| 4 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 88 | High reasoning |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 85 | UI generation |
| 6 | nvidia/nvidia/nemotron-nano-12b-v2-vl | NVIDIA Build | 82 | Vision model |

#### git-master
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 94 | Git operations |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 92 | History analysis |
| 3 | nvidia/mistral-ai/devstral-2-123b-instruct-2512 | NVIDIA Build | 90 | Code-focused |
| 4 | openai/gpt-5.4-mini | OpenAI | 87 | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 85 | Coding partner |
| 6 | nvidia/meta/llama-3.3-70b-instruct | NVIDIA Build | 81 | General purpose |

#### product-manager
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 95 | Product reasoning |
| 2 | openai/gpt-5.4 | OpenAI | 93 | Feature analysis |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 90 | Complex analysis |
| 4 | opencode/gemini-3-flash | OpenCode Zen | 88 | Research |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 85 | General purpose |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 82 | Agentic |

#### ux-researcher
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3.5-397b-a17b | NVIDIA Build | 94 | VLM with vision |
| 2 | opencode/gemini-3-flash | OpenCode Zen | 92 | Web-native research |
| 3 | nvidia/mistral-ai/mistral-small-4-119b-2603 | NVIDIA Build | 89 | Creative analysis |
| 4 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 87 | High reasoning |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 84 | General purpose |
| 6 | nvidia/nvidia/nemotron-nano-12b-v2-vl | NVIDIA Build | 81 | Vision model |

#### information-architect
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 96 | Architecture reasoning |
| 2 | openai/gpt-5.4 | OpenAI | 94 | Complex architecture |
| 3 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 91 | Deep analysis |
| 4 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 88 | Code architecture |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 85 | General purpose |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 82 | Agentic |

#### product-analyst
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 95 | Analysis reasoning |
| 2 | openai/gpt-5.4 | OpenAI | 93 | Product analysis |
| 3 | opencode/gemini-3-flash | OpenCode Zen | 90 | Research |
| 4 | nvidia/deepseek-ai/deepseek-v3.2 | NVIDIA Build | 87 | Deep analysis |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 84 | General purpose |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 81 | Agentic |

---

### Fast-Lane Agents

#### explore
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 98 | Fast, FREE, search-optimized |
| 2 | opencode/gemini-3-flash | OpenCode Zen | 95 | Web-native research |
| 3 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 92 | 1M ctx, $0.05/$0.20 |
| 4 | openai/gpt-5.4-nano | OpenAI | 90 | Cost-effective |
| 5 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | NVIDIA Build | 88 | Edge/quick |
| 6 | openai/o4-mini | OpenAI | 85 | Cost-effective |

#### style-reviewer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 94 | Fast style checks |
| 2 | opencode/gemini-3-flash | OpenCode Zen | 91 | Web-native |
| 3 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 89 | Efficient |
| 4 | openai/gpt-5.4-nano | OpenAI | 87 | Fast |
| 5 | nvidia/nvidia/nvidia-nemotron-nano-9b-v2 | NVIDIA Build | 85 | Edge/quick |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 82 | General purpose |

#### writer
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | opencode/gemini-3-flash | OpenCode Zen | 98 | #1 for writing |
| 2 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 96 | Quick docs |
| 3 | nvidia/nvidia/nemotron-3-nano-30b-a3b | NVIDIA Build | 94 | Efficient |
| 4 | openai/gpt-5.4-mini | OpenAI | 91 | Cost-effective |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 90 | Versatile |
| 6 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 88 | Technical docs |

#### researcher
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | opencode/gemini-3-flash | OpenCode Zen | 96 | Web-native research |
| 2 | nvidia/stepfun-ai/step-3.5-flash | NVIDIA Build | 94 | Fast, FREE |
| 3 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 91 | Synthesis |
| 4 | openai/gpt-5.4 | OpenAI | 89 | Multi-source |
| 5 | opencode/qwen3.6-plus | OpenCode Zen | 85 | General purpose |
| 6 | nvidia/nvidia/nemotron-3-super-120b-a12b | NVIDIA Build | 82 | Broad knowledge |

#### vision
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3.5-397b-a17b | NVIDIA Build | 99 | VLM with vision |
| 2 | nvidia/meta/llama-3.2-11b-vision-instruct | NVIDIA Build | 95 | Vision |
| 3 | nvidia/nvidia/nemotron-nano-12b-v2-vl | NVIDIA Build | 92 | Vision |
| 4 | openai/gpt-5.4 | OpenAI | 90 | Frontier vision |
| 5 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 88 | High reasoning |
| 6 | opencode/qwen3.6-plus | OpenCode Zen | 85 | General purpose |

#### qa-tester
| Rank | Model | Provider | Score | Notes |
|------|-------|----------|-------|-------|
| 1 | nvidia/qwen/qwen3-coder-480b-a35b-instruct | NVIDIA Build | 95 | Test generation |
| 2 | nvidia/z-ai/glm-5.1 | NVIDIA Build | 93 | Test strategy |
| 3 | nvidia/mistral-ai/devstral-2-123b-instruct-2512 | NVIDIA Build | 91 | Code-focused |
| 4 | openai/gpt-5.4-mini | OpenAI | 88 | Cost-effective |
| 5 | opencode/qwen3-coder | OpenCode Zen | 86 | Coding partner |
| 6 | nvidia/meta/llama-3.3-70b-instruct | NVIDIA Build | 82 | General purpose |

---

## Configuration Examples

### NVIDIA Build Free Tier (Zero Cost)
```json
{
  "agent": {
    "executor": {
      "model": "nvidia/qwen/qwen3-coder-480b-a35b-instruct"
    },
    "architect": {
      "model": "nvidia/z-ai/glm-5.1"
    },
    "explore": {
      "model": "nvidia/stepfun-ai/step-3.5-flash"
    }
  }
}
```

### OpenCode Zen Setup ($0.45-$3.00 per 1M tokens)
```json
{
  "agent": {
    "executor": {
      "model": "opencode/qwen3-coder"
    },
    "researcher": {
      "model": "opencode/gemini-3-flash"
    },
    "writer": {
      "model": "opencode/gemini-3-flash"
    }
  }
}
```

### OpenAI Paid Setup ($0.20-$180 per 1M tokens)
```json
{
  "agent": {
    "executor": {
      "model": "openai/gpt-5.4"
    },
    "architect": {
      "model": "openai/gpt-5.4-pro"
    },
    "explore": {
      "model": "openai/gpt-5.4-nano"
    }
  }
}
```

### Hybrid Setup (Best Cost-Performance)
```json
{
  "agent": {
    "executor": {
      "model": "nvidia/qwen/qwen3-coder-480b-a35b-instruct"
    },
    "architect": {
      "model": "nvidia/z-ai/glm-5.1"
    },
    "explore": {
      "model": "nvidia/stepfun-ai/step-3.5-flash"
    },
    "researcher": {
      "model": "opencode/gemini-3-flash"
    },
    "vision": {
      "model": "nvidia/qwen/qwen3.5-397b-a17b"
    }
  }
}
```

---

## Sources

1. NVIDIA. "Try NVIDIA NIM APIs - Models Catalog." *build.nvidia.com*, 2026.
2. OpenCode. "OpenCode Zen | Reliable optimized models for coding agents." *opencode.ai/zen*, 2026.
3. OpenAI. "Models - OpenAI API." *platform.openai.com*, 2026.
4. SWE-Bench Pro benchmark results (April 2026).
5. Multiple benchmark sources: HumanEval, MMLU, LiveCodeBench.

---

## Conclusion

The v3.0 rankings reflect a major shift in the AI model landscape. **nvidia/z-ai/glm-5.1** emerges as the dominant model for reasoning tasks (FREE, #1 SWE-Bench Pro), while **nvidia/qwen/qwen3-coder-480b-a35b-instruct** leads coding tasks (FREE, best agentic coding). **nvidia/stepfun-ai/step-3.5-flash** is the optimal choice for fast/search tasks (FREE). **opencode/gemini-3-flash** excels at research and writing. The free tier from NVIDIA Build now competes with or exceeds paid alternatives in most domains.

---

**Last Updated**: April 21, 2026
