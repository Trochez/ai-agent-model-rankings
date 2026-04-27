# Extended Rankings — Librarian + Writing (NVIDIA Build + OpenAI)

**Date:** April 25, 2026  
**Scope:** NVIDIA Build + OpenAI models only  
**Categories:** `librarian` and `writing`  
**Librarian Formula:** Cost-eff 30% + Latency-tier 25% + GPQA 15% + SWE-Bench Pro 15% + Context 15%  
**Writing Formula:** MMLU-Pro 30% + GPQA 20% + Cost-eff 25% + Context 15% + SWE-Bench Pro 10%

---

## Librarian Performance Ranking (45 Models)

| Rank | Model | Provider | Score | Params | Ctx | $/1M In | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/deepseek-ai/deepseek-v4-flash` | NVIDIA Build | **80.2** | 284B/13B act | 1M | $0.00 | ✅ |
| 2 | `nvidia/stepfun-ai/step-3.5-flash` | NVIDIA Build | **80.0** | 196B/11B act | 256K | $0.00 | ✅ |
| 3 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | **78.5** | 31.6B/3.6B act | 1M | $0.05 | |
| 4 | `nvidia/qwen/qwen3.5-122b-a10b` | NVIDIA Build | **78.3** | 122B/10B act MoE | 262K | $0.00 | ✅ |
| 5 | `nvidia/z-ai/glm-4.7` | NVIDIA Build | **78.0** | 490B/49B act MoE | 2.54M | $0.00 | ✅ |
| 6 | `nvidia/deepseek-ai/deepseek-v4-pro` | NVIDIA Build | **77.7** | 1.6T/49B act MoE | 1M | $0.00 | ✅ |
| 7 | `nvidia/qwen/qwen3.5-9b` | NVIDIA Build | **77.3** | 9.65B dense | 256K | $0.05 | |
| 8 | `openai/gpt-5.4-nano` | OpenAI | **76.8** | undisclosed | 400K | $0.20 | |
| 9 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Build | **76.6** | 120B/12B act | 1M | $0.10 | |
| 10 | `nvidia/microsoft/phi-4-multimodal-instruct` | NVIDIA Build | **74.0** | ~5.6B dense | 128K | $0.00 | ✅ |
| 11 | `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | NVIDIA Build | **73.3** | 9B dense | 128K | $0.00 | ✅ |
| 12 | `nvidia/google/gemma-4-26b-a4b-it` | NVIDIA Build | **73.2** | 25.2B/3.8B act | 256K | $0.08 | |
| 13 | `nvidia/microsoft/phi-3-small-128k-instruct` | NVIDIA Build | **70.5** | 7B dense | 128K | $0.00 | ✅ |
| 14 | `nvidia/meta-llama/llama-3.2-1b-instruct` | NVIDIA Build | **70.4** | 1.23B dense | 128K | $0.00 | ✅ |
| 15 | `nvidia/mistralai/mistral-nemo-minitron-8b-base` | NVIDIA Build | **70.2** | 8B dense | 128K | $0.00 | ✅ |
| 16 | `nvidia/meta-llama/llama-3.2-3b-instruct` | NVIDIA Build | **70.1** | 3.21B dense | 128K | $0.00 | ✅ |
| 17 | `nvidia/microsoft/phi-3-mini-128k-instruct` | NVIDIA Build | **69.6** | 3.8B dense | 128K | $0.00 | ✅ |
| 18 | `nvidia/meta-llama/llama-3.2-11b-vision-instruct` | NVIDIA Build | **69.1** | 10.6B dense | 128K | $0.00 | ✅ |
| 19 | `nvidia/ising/ising-calibration-1-35b-a3b` | NVIDIA Build | **68.5** | 35B/3B act MoE | 128K | $0.00 | ✅ |
| 20 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | NVIDIA Build | **68.0** | 119B/22B act MoE | 256K | $0.10 | |
| 21 | `nvidia/minimax/minimax-m2.7` | NVIDIA Build | **67.0** | 230B dense | 3.05M | $0.00 | ✅ |
| 22 | `nvidia/microsoft/phi-4-mini-instruct` | NVIDIA Build | **65.3** | 3.8B dense | 128K | $0.075 | |
| 23 | `openai/gpt-5.4-mini` | OpenAI | **65.1** | undisclosed | 400K | $0.75 | |
| 24 | `nvidia/qwen/qwen3.5-35b-a3b` | NVIDIA Build | **64.8** | 36B/3B act | 262K | $0.25 | |
| 25 | `nvidia/mistralai/devstral-2-123b-instruct-2512` | NVIDIA Build | **63.8** | 123B dense | 256K | $0.00 | ✅ |
| 26 | `nvidia/google/gemma-2-2b-it` | NVIDIA Build | **63.7** | 2B dense | 32K | $0.00 | ✅ |
| 27 | `nvidia/google/gemma-3-27b-it` | NVIDIA Build | **63.6** | 27B dense | 128K | $0.00 | ✅ |
| 28 | `nvidia/qwen/qwen3.5-397b-a17b` | NVIDIA Build | **63.5** | 397B/17B act MoE | 262K | $0.25 | |
| 29 | `nvidia/google/gemma-3n-e2b-it` | NVIDIA Build | **63.4** | 2B dense | 32K | $0.00 | ✅ |
| 30 | `nvidia/google/gemma-3-1b-it` | NVIDIA Build | **63.0** | 1B dense | 32K | $0.00 | ✅ |
| 31 | `nvidia/google/gemma-3n-e4b-it` | NVIDIA Build | **62.8** | 4B dense | 32K | $0.00 | ✅ |
| 32 | `nvidia/microsoft/phi-3-small-8k-instruct` | NVIDIA Build | **61.5** | 7B dense | 8K | $0.00 | ✅ |
| 33 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | NVIDIA Build | **61.4** | 12B dense | 128K | $0.20 | |
| 34 | `nvidia/nvidia/nemotron-mini-4b-instruct` | NVIDIA Build | **59.8** | 4B dense | 8K | $0.00 | ✅ |
| 35 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | NVIDIA Build | **59.6** | 24B dense | 128K | $0.10 | |
| 36 | `nvidia/mistralai/mistral-small-24b-instruct` | NVIDIA Build | **59.5** | 24B dense | 33K | $0.05 | |
| 37 | `openai/o4-mini` | OpenAI | **58.2** | undisclosed | 200K | $1.10 | |
| 38 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | NVIDIA Build | **57.3** | 49B dense | 131K | $0.10 | |
| 39 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | NVIDIA Build | **56.5** | 480B/35B act MoE | 262K | $0.50 | |
| 40 | `nvidia/deepseek-ai/deepseek-v3.2` | NVIDIA Build | **54.2** | 685B/37B act MoE | 128K | $0.50 | |
| 41 | `openai/gpt-5.4` | OpenAI | **52.1** | undisclosed | 1.05M | $2.50 | |
| 42 | `nvidia/z-ai/glm-5.1` | NVIDIA Build | **52.0** | 490B/49B act MoE | 200K | $1.05 | |
| 43 | `openai/gpt-5.4-pro` | OpenAI | **49.7** | undisclosed | 1.05M | $30.00 | |
| 44 | `nvidia/ibm-granite/granite-3.3-8b-instruct` | NVIDIA Build | **47.7** | 8B dense | 128K | $0.50 | |
| 45 | `openai/o3` | OpenAI | **47.2** | undisclosed | 200K | $10.00 | |

---

## Writing Performance Ranking (45 Models)

| Rank | Model | Provider | Score | Params | Ctx | $/1M In | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/deepseek-ai/deepseek-v4-pro` | NVIDIA Build | **88.9** | 1.6T/49B act MoE | 1M | $0.00 | ✅ |
| 2 | `nvidia/z-ai/glm-4.7` | NVIDIA Build | **87.7** | 490B/49B act MoE | 2.54M | $0.00 | ✅ |
| 3 | `nvidia/deepseek-ai/deepseek-v4-flash` | NVIDIA Build | **83.2** | 284B/13B act | 1M | $0.00 | ✅ |
| 4 | `nvidia/stepfun-ai/step-3.5-flash` | NVIDIA Build | **82.7** | 196B/11B act | 256K | $0.00 | ✅ |
| 5 | `nvidia/minimax/minimax-m2.7` | NVIDIA Build | **81.4** | 230B dense | 3.05M | $0.00 | ✅ |
| 6 | `nvidia/qwen/qwen3.5-122b-a10b` | NVIDIA Build | **80.8** | 122B/10B act MoE | 262K | $0.00 | ✅ |
| 7 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Build | **77.7** | 120B/12B act | 1M | $0.10 | |
| 8 | `openai/gpt-5.4-nano` | OpenAI | **77.5** | undisclosed | 400K | $0.20 | |
| 9 | `nvidia/qwen/qwen3.5-9b` | NVIDIA Build | **76.4** | 9.65B dense | 256K | $0.05 | |
| 10 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | NVIDIA Build | **75.3** | 119B/22B act MoE | 256K | $0.10 | |
| 11 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | **75.0** | 31.6B/3.6B act | 1M | $0.05 | |
| 12 | `nvidia/qwen/qwen3.5-397b-a17b` | NVIDIA Build | **73.3** | 397B/17B act MoE | 262K | $0.25 | |
| 13 | `nvidia/google/gemma-4-26b-a4b-it` | NVIDIA Build | **72.8** | 25.2B/3.8B act | 256K | $0.08 | |
| 14 | `openai/gpt-5.4-mini` | OpenAI | **72.8** | undisclosed | 400K | $0.75 | |
| 15 | `nvidia/mistralai/devstral-2-123b-instruct-2512` | NVIDIA Build | **71.0** | 123B dense | 256K | $0.00 | ✅ |
| 16 | `openai/o4-mini` | OpenAI | **69.0** | undisclosed | 200K | $1.10 | |
| 17 | `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | NVIDIA Build | **68.5** | 9B dense | 128K | $0.00 | ✅ |
| 18 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | NVIDIA Build | **67.6** | 480B/35B act MoE | 262K | $0.50 | |
| 19 | `openai/gpt-5.4-pro` | OpenAI | **67.5** | undisclosed | 1.05M | $30.00 | |
| 20 | `nvidia/z-ai/glm-5.1` | NVIDIA Build | **66.7** | 490B/49B act MoE | 200K | $1.05 | |
| 21 | `openai/gpt-5.4` | OpenAI | **66.5** | undisclosed | 1.05M | $2.50 | |
| 22 | `nvidia/qwen/qwen3.5-35b-a3b` | NVIDIA Build | **66.4** | 36B/3B act | 262K | $0.25 | |
| 23 | `nvidia/deepseek-ai/deepseek-v3.2` | NVIDIA Build | **66.2** | 685B/37B act MoE | 128K | $0.50 | |
| 24 | `nvidia/microsoft/phi-4-multimodal-instruct` | NVIDIA Build | **65.8** | ~5.6B dense | 128K | $0.00 | ✅ |
| 25 | `openai/o3` | OpenAI | **65.8** | undisclosed | 200K | $10.00 | |
| 26 | `nvidia/google/gemma-3-27b-it` | NVIDIA Build | **64.8** | 27B dense | 128K | $0.00 | ✅ |
| 27 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | NVIDIA Build | **64.0** | 49B dense | 131K | $0.10 | |
| 28 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | NVIDIA Build | **62.5** | 24B dense | 128K | $0.10 | |
| 29 | `nvidia/mistralai/mistral-nemo-minitron-8b-base` | NVIDIA Build | **61.8** | 8B dense | 128K | $0.00 | ✅ |
| 30 | `nvidia/meta-llama/llama-3.2-11b-vision-instruct` | NVIDIA Build | **61.1** | 10.6B dense | 128K | $0.00 | ✅ |
| 31 | `nvidia/mistralai/mistral-small-24b-instruct` | NVIDIA Build | **60.5** | 24B dense | 33K | $0.05 | |
| 32 | `nvidia/microsoft/phi-3-small-128k-instruct` | NVIDIA Build | **58.5** | 7B dense | 128K | $0.00 | ✅ |
| 33 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | NVIDIA Build | **57.3** | 12B dense | 128K | $0.20 | |
| 34 | `nvidia/microsoft/phi-3-mini-128k-instruct` | NVIDIA Build | **56.7** | 3.8B dense | 128K | $0.00 | ✅ |
| 35 | `nvidia/meta-llama/llama-3.2-3b-instruct` | NVIDIA Build | **56.5** | 3.21B dense | 128K | $0.00 | ✅ |
| 36 | `nvidia/ising/ising-calibration-1-35b-a3b` | NVIDIA Build | **55.1** | 35B/3B act MoE | 128K | $0.00 | ✅ |
| 37 | `nvidia/microsoft/phi-4-mini-instruct` | NVIDIA Build | **54.9** | 3.8B dense | 128K | $0.075 | |
| 38 | `nvidia/meta-llama/llama-3.2-1b-instruct` | NVIDIA Build | **53.1** | 1.23B dense | 128K | $0.00 | ✅ |
| 39 | `nvidia/microsoft/phi-3-small-8k-instruct` | NVIDIA Build | **49.5** | 7B dense | 8K | $0.00 | ✅ |
| 40 | `nvidia/google/gemma-3n-e4b-it` | NVIDIA Build | **46.5** | 4B dense | 32K | $0.00 | ✅ |
| 41 | `nvidia/google/gemma-2-2b-it` | NVIDIA Build | **45.2** | 2B dense | 32K | $0.00 | ✅ |
| 42 | `nvidia/nvidia/nemotron-mini-4b-instruct` | NVIDIA Build | **44.3** | 4B dense | 8K | $0.00 | ✅ |
| 43 | `nvidia/google/gemma-3n-e2b-it` | NVIDIA Build | **43.9** | 2B dense | 32K | $0.00 | ✅ |
| 44 | `nvidia/google/gemma-3-1b-it` | NVIDIA Build | **42.1** | 1B dense | 32K | $0.00 | ✅ |
| 45 | `nvidia/ibm-granite/granite-3.3-8b-instruct` | NVIDIA Build | **41.6** | 8B dense | 128K | $0.50 | |

---

## Librarian Cost/Performance Ranking (Top 15)

| Rank | Model | C/P | Score | $/1M In | Ctx |
|---|---|---|---|---|---|
| 1 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,569,000** | 78.5 | $0.05 | 1M |
| 2 | `nvidia/qwen/qwen3.5-9b` | **1,546,100** | 77.3 | $0.05 | 256K |
| 3 | `nvidia/mistralai/mistral-small-24b-instruct` | **1,191,000** | 59.5 | $0.05 | 33K |
| 4 | `nvidia/google/gemma-4-26b-a4b-it` | **915,562** | 73.2 | $0.08 | 256K |
| 5 | `nvidia/microsoft/phi-4-mini-instruct` | **871,067** | 65.3 | $0.075 | 128K |
| 6 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **766,050** | 76.6 | $0.10 | 1M |
| 7 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **679,500** | 68.0 | $0.10 | 256K |
| 8 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | **595,500** | 59.6 | $0.10 | 128K |
| 9 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | **572,550** | 57.3 | $0.10 | 131K |
| 10 | `openai/gpt-5.4-nano` | **383,900** | 76.8 | $0.20 | 400K |
| 11 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **306,875** | 61.4 | $0.20 | 128K |
| 12 | `nvidia/qwen/qwen3.5-35b-a3b` | **259,320** | 64.8 | $0.25 | 262K |
| 13 | `nvidia/qwen/qwen3.5-397b-a17b` | **253,800** | 63.5 | $0.25 | 262K |
| 14 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **113,000** | 56.5 | $0.50 | 262K |
| 15 | `nvidia/deepseek-ai/deepseek-v3.2` | **108,500** | 54.2 | $0.50 | 128K |

---

## Writing Cost/Performance Ranking (Top 15)

| Rank | Model | C/P | Score | $/1M In | Ctx |
|---|---|---|---|---|---|
| 1 | `nvidia/qwen/qwen3.5-9b` | **1,527,800** | 76.4 | $0.05 | 256K |
| 2 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,499,000** | 75.0 | $0.05 | 1M |
| 3 | `nvidia/mistralai/mistral-small-24b-instruct` | **1,211,000** | 60.5 | $0.05 | 33K |
| 4 | `nvidia/google/gemma-4-26b-a4b-it` | **909,500** | 72.8 | $0.08 | 256K |
| 5 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **776,900** | 77.7 | $0.10 | 1M |
| 6 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **753,500** | 75.3 | $0.10 | 256K |
| 7 | `nvidia/microsoft/phi-4-mini-instruct` | **731,867** | 54.9 | $0.075 | 128K |
| 8 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | **639,900** | 64.0 | $0.10 | 131K |
| 9 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | **625,000** | 62.5 | $0.10 | 128K |
| 10 | `openai/gpt-5.4-nano` | **387,750** | 77.5 | $0.20 | 400K |
| 11 | `nvidia/qwen/qwen3.5-397b-a17b` | **293,200** | 73.3 | $0.25 | 262K |
| 12 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **286,750** | 57.3 | $0.20 | 128K |
| 13 | `nvidia/qwen/qwen3.5-35b-a3b` | **265,760** | 66.4 | $0.25 | 262K |
| 14 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **135,200** | 67.6 | $0.50 | 262K |
| 15 | `nvidia/deepseek-ai/deepseek-v3.2` | **132,300** | 66.2 | $0.50 | 128K |

---

## Key Insights

1. **Librarian and explore now converge** on the same top three: `deepseek-v4-flash`, `step-3.5-flash`, and `nemotron-3-nano-30b-a3b`.
2. **Writing is dominated by free large NVIDIA models**: `deepseek-v4-pro`, `glm-4.7`, and `deepseek-v4-flash` all beat the paid OpenAI frontier models on this formula.
3. **`openai/gpt-5.4-nano` is the best OpenAI option** for both librarian and writing on value-adjusted scoring.
4. **Cost and context dominate speed-heavy tasks**: `glm-5.1` has frontier reasoning, but it falls far down librarian because $1.05 input pricing kills the score.
5. **Small, cheap paid NVIDIA models still matter**: `qwen3.5-9b` and `nemotron-3-nano-30b-a3b` are the strongest paid cost/performance picks.

---

*Generated April 25, 2026. Companion to the April 25 refreshed speed-heavy and writing rankings.*  
*See also: [v3.0 Canonical Rankings](oh-my-opencode-agent-rankings.md) | [Extended Explore Rankings](extended-rankings-explore-nvidia-build.md) | [Extended Quick Rankings](extended-rankings-quick-nvidia-build.md)*
