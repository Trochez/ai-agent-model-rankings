# Extended Rankings — Explore Category (NVIDIA Build Only)

**Date:** April 25, 2026
**Scope:** NVIDIA Build models only, explore/librarian agent category
**Formula:** Cost-eff 30% + Latency-tier 25% + GPQA 15% + SWE-Bench Pro 15% + Context 15%

---

## Methodology

### Explore (Speed-heavy) Weight Formula

| Component | Weight | Description |
|---|---|---|
| Cost-efficiency | 30% | Normalized pricing score (FREE=100, higher cost=lower) |
| Latency-tier | 25% | Normalized speed score based on active params (<3B=100, 3-8B=95, 8-15B=85, MoE 3-4B act=90, MoE 10B+ act=75, 24B dense=60, 27B dense=55, 49B dense=45, 120B+ dense=30) |
| GPQA Diamond | 15% | Graduate-level reasoning benchmark, raw% used directly (0–100) |
| SWE-Bench Pro | 15% | Software engineering benchmark, raw% used directly (0–100, max ~60%) |
| Context window | 15% | Normalized context (3M+=100, 2.5M+=100, 1M+=100, 256K=90, 262K=90, 200K=85, 131K=80, 128K=75, 33K=40, 32K=38, 8K=15) |

Each component is normalized to 0–100 before weighting. Final Score = Σ(component × weight).

### SWE-Bench Pro Normalization

SWE-Bench Pro raw scores are used directly as the 0–100 component (consistent with GPQA treatment). Current frontier max is ~60% (GLM-5.1 at 58.4%, Nemotron-3-Super at 60%). Small models (1–9B) typically score 0–5%. Code-focused models (Devstral, Qwen3-Coder) score higher than general models of similar size.

**SWE-Bench Pro estimates** are based on:
- Published scores: GLM-5.1 (58.4%), Nemotron-3-Super-120B (60%), GPT-5.4 family (52–60%)
- Model family proxies: Devstral (code-focused, ~40%), Qwen3-Coder (~50%), DeepSeek-V4-Pro (~55%)
- Size-based interpolation for small models where no published data exists

### Cost/Performance Ratio

- **Paid models:** `C/P = (Score × 1,000) / (Input $/1M tokens)`
- **Free models:** `C/P = Score × 100` (reflects infinite value at zero cost, capped for comparability)

---

## Performance Ranking (Expanded — 39 Models)

| Rank | Model | Score | Params | Ctx | $/1M In | $/1M Out | Free | Key Strength |
|---|---|---|---|---|---|---|---|---|
| 1 | `nvidia/deepseek-ai/deepseek-v4-flash` | **80.2** | 284B/13B act | 1M | $0.00 | $0.00 | ✅ | Free + 1M ctx + SWE 38% |
| 2 | `nvidia/stepfun-ai/step-3.5-flash` | **80.0** | 196B/11B act | 256K | $0.00 | $0.00 | ✅ | Free + GPQA 83.5% + SWE 35% |
| 3 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **78.5** | 31.6B/3.6B act | 1M | $0.05 | $0.20 | | Cheap + fast + 1M ctx |
| 4 | `nvidia/qwen/qwen3.5-122b-a10b` | **78.3** | 122B/10B act MoE | 262K | $0.00 | $0.00 | ✅ | Free MoE 122B/10B act |
| 5 | `nvidia/z-ai/glm-4.7` | **78.0** | 490B/49B act MoE | 2.54M | $0.00 | $0.00 | ✅ | Free + 2.54M ctx + SWE 52% |
| 6 | `nvidia/deepseek-ai/deepseek-v4-pro` | **77.7** | 1.6T/49B act MoE | 1M | $0.00 | $0.00 | ✅ | Free + 1M ctx + SWE 55% |
| 7 | `nvidia/qwen/qwen3.5-9b` | **77.3** | 9.65B dense | 256K | $0.05 | $0.15 | | Best small dense, GPQA 81.7% |
| 8 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **76.6** | 120B/12B act | 1M | $0.10 | $0.50 | | 1M ctx + SWE 60% |
| 9 | `nvidia/microsoft/phi-4-multimodal-instruct` | **74.0** | ~5.6B dense | 128K | $0.00 | $0.00 | ✅ | Free + vision + Phi‑4 |
| 10 | `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | **73.3** | 9B dense | 128K | $0.00 | $0.00 | ✅ | Free + fast 9B |
| 11 | `nvidia/google/gemma-4-26b-a4b-it` | **73.2** | 25.2B/3.8B act | 256K | $0.08 | $0.35 | | MoE efficient, GPQA 82% |
| 12 | `nvidia/microsoft/phi-3-small-128k-instruct` | **70.5** | 7B dense | 128K | $0.00 | $0.00 | ✅ | Free 7B + 128K |
| 13 | `nvidia/meta-llama/llama-3.2-1b-instruct` | **70.4** | 1.23B dense | 128K | $0.00 | $0.00 | ✅ | Free + minimal latency |
| 14 | `nvidia/mistralai/mistral-nemo-minitron-8b-base` | **70.2** | 8B dense | 128K | $0.00 | $0.00 | ✅ | Free 8B workhorse |
| 15 | `nvidia/meta-llama/llama-3.2-3b-instruct` | **70.1** | 3.21B dense | 128K | $0.00 | $0.00 | ✅ | Free ultra-fast 3B |
| 16 | `nvidia/microsoft/phi-3-mini-128k-instruct` | **69.6** | 3.8B dense | 128K | $0.00 | $0.00 | ✅ | Free + 128K ctx |
| 17 | `nvidia/meta-llama/llama-3.2-11b-vision-instruct` | **69.1** | 10.6B dense | 128K | $0.00 | $0.00 | ✅ | Free + vision 11B |
| 18 | `nvidia/ising/ising-calibration-1-35b-a3b` | **68.5** | 35B/3B act MoE | 128K | $0.00 | $0.00 | ✅ | Free quantum VLM MoE |
| 19 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **68.0** | 119B/22B act MoE | 256K | $0.10 | $0.40 | | Hybrid reasoning 119B |
| 20 | `nvidia/minimax/minimax-m2.7` | **67.0** | 230B dense | 3.05M | $0.00 | $0.00 | ✅ | Free + 3.05M ctx |
| 21 | `nvidia/microsoft/phi-4-mini-instruct` | **65.3** | 3.8B dense | 128K | $0.075 | $0.30 | | Best math at 3.8B |
| 22 | `nvidia/qwen/qwen3.5-35b-a3b` | **64.8** | 36B/3B act | 262K | $0.25 | $1.25 | | MoE 3B act, GPQA 84% |
| 23 | `nvidia/mistralai/devstral-2-123b-instruct-2512` | **63.8** | 123B dense | 256K | $0.00 | $0.00 | ✅ | Free code-focused 123B |
| 24 | `nvidia/google/gemma-2-2b-it` | **63.7** | 2B dense | 32K | $0.00 | $0.00 | ✅ | Free edge model |
| 25 | `nvidia/google/gemma-3-27b-it` | **63.6** | 27B dense | 128K | $0.00 | $0.00 | ✅ | Free 27B dense |
| 26 | `nvidia/qwen/qwen3.5-397b-a17b` | **63.5** | 397B/17B act MoE | 262K | $0.25 | $1.25 | | Frontier MoE 397B |
| 27 | `nvidia/google/gemma-3n-e2b-it` | **63.4** | 2B dense | 32K | $0.00 | $0.00 | ✅ | Gemma‑3 edge 2B |
| 28 | `nvidia/google/gemma-3-1b-it` | **63.0** | 1B dense | 32K | $0.00 | $0.00 | ✅ | Free ultra-edge |
| 29 | `nvidia/google/gemma-3n-e4b-it` | **62.8** | 4B dense | 32K | $0.00 | $0.00 | ✅ | Gemma‑3 edge 4B |
| 30 | `nvidia/microsoft/phi-3-small-8k-instruct` | **61.5** | 7B dense | 8K | $0.00 | $0.00 | ✅ | Free (8K ctx limit) |
| 31 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **61.4** | 12B dense | 128K | $0.20 | $0.20 | | Vision-language 12B |
| 32 | `nvidia/nvidia/nemotron-mini-4b-instruct` | **59.8** | 4B dense | 8K | $0.00 | $0.00 | ✅ | Free + 2GB VRAM |
| 33 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | **59.6** | 24B dense | 128K | $0.10 | $0.30 | | Multimodal 24B |
| 34 | `nvidia/mistralai/mistral-small-24b-instruct` | **59.5** | 24B dense | 33K | $0.05 | $0.08 | | Cheap but 33K ctx |
| 35 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | **57.3** | 49B dense | 131K | $0.10 | $0.40 | | 49B dense, SWE 25% |
| 36 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **56.5** | 480B/35B act MoE | 262K | $0.50 | $2.50 | | Code-focused 480B MoE |
| 37 | `nvidia/deepseek-ai/deepseek-v3.2` | **54.2** | 685B/37B act MoE | 128K | $0.50 | $2.50 | | Deep reasoning 685B MoE |
| 38 | `nvidia/z-ai/glm-5.1` | **52.0** | 490B/49B act MoE | 200K | $1.05 | $3.50 | | SWE-Bench Pro #1 (58.4%) |
| 39 | `nvidia/ibm-granite/granite-3.3-8b-instruct` | **47.7** | 8B dense | 128K | $0.50 | $0.50 | | Overpriced vs free 8Bs |

---

## Cost/Performance Ranking (Top 20)

| Rank | Model | C/P | Score | $/1M In | $/1M Out | Ctx | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,569,000** | 78.5 | $0.05 | $0.20 | 1M | |
| 2 | `nvidia/qwen/qwen3.5-9b` | **1,546,100** | 77.3 | $0.05 | $0.15 | 256K | |
| 3 | `nvidia/mistralai/mistral-small-24b-instruct` | **1,191,000** | 59.5 | $0.05 | $0.08 | 33K | |
| 4 | `nvidia/google/gemma-4-26b-a4b-it` | **915,562** | 73.2 | $0.08 | $0.35 | 256K | |
| 5 | `nvidia/microsoft/phi-4-mini-instruct` | **871,067** | 65.3 | $0.075 | $0.30 | 128K | |
| 6 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **766,050** | 76.6 | $0.10 | $0.50 | 1M | |
| 7 | `nvidia/mistral-ai/mistral-small-4-119b-2603` | **679,500** | 68.0 | $0.10 | $0.40 | 256K | |
| 8 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | **595,500** | 59.6 | $0.10 | $0.30 | 128K | |
| 9 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | **572,550** | 57.3 | $0.10 | $0.40 | 131K | |
| 10 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **306,875** | 61.4 | $0.20 | $0.20 | 128K | |
| 11 | `nvidia/qwen/qwen3.5-35b-a3b` | **259,320** | 64.8 | $0.25 | $1.25 | 262K | |
| 12 | `nvidia/qwen/qwen3.5-397b-a17b` | **253,800** | 63.5 | $0.25 | $1.25 | 262K | |
| 13 | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | **113,000** | 56.5 | $0.50 | $2.50 | 262K | |
| 14 | `nvidia/deepseek-ai/deepseek-v3.2` | **108,500** | 54.2 | $0.50 | $2.50 | 128K | |
| 15 | `nvidia/ibm-granite/granite-3.3-8b-instruct` | **95,300** | 47.7 | $0.50 | $0.50 | 128K | |
| 16 | `nvidia/z-ai/glm-5.1` | **49,533** | 52.0 | $1.05 | $3.50 | 200K | |

**Free models (C/P = Score × 100):**

| Rank | Model | C/P | Score | $/1M In | $/1M Out | Ctx | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/deepseek-ai/deepseek-v4-flash` | **8,020** | 80.2 | $0.00 | $0.00 | 1M | ✅ |
| 2 | `nvidia/stepfun-ai/step-3.5-flash` | **8,003** | 80.0 | $0.00 | $0.00 | 256K | ✅ |
| 3 | `nvidia/qwen/qwen3.5-122b-a10b` | **7,830** | 78.3 | $0.00 | $0.00 | 262K | ✅ |
| 4 | `nvidia/z-ai/glm-4.7` | **7,805** | 78.0 | $0.00 | $0.00 | 2.54M | ✅ |
| 5 | `nvidia/deepseek-ai/deepseek-v4-pro` | **7,770** | 77.7 | $0.00 | $0.00 | 1M | ✅ |
| 6 | `nvidia/microsoft/phi-4-multimodal-instruct` | **7,400** | 74.0 | $0.00 | $0.00 | 128K | ✅ |
| 7 | `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | **7,330** | 73.3 | $0.00 | $0.00 | 128K | ✅ |
| 8 | `nvidia/microsoft/phi-3-small-128k-instruct` | **7,055** | 70.5 | $0.00 | $0.00 | 128K | ✅ |
| 9 | `nvidia/meta-llama/llama-3.2-1b-instruct` | **7,040** | 70.4 | $0.00 | $0.00 | 128K | ✅ |
| 10 | `nvidia/mistralai/mistral-nemo-minitron-8b-base` | **7,015** | 70.2 | $0.00 | $0.00 | 128K | ✅ |

---

## Score Breakdown (Top 10 + Highlights)

| Model | Cost-eff (30%) | Latency (25%) | GPQA (15%) | SWE-Bench (15%) | Context (15%) | Total |
|---|---|---|---|---|---|---|
| deepseek-v4-flash | 100 → 30.0 | 70 → 17.5 | 80.0 → 12.0 | 38.0 → 5.7 | 100 → 15.0 | **80.2** |
| step-3.5-flash | 100 → 30.0 | 75 → 18.8 | 83.5 → 12.5 | 35.0 → 5.2 | 90 → 13.5 | **80.0** |
| nemotron-3-nano-30b-a3b | 95 → 28.5 | 90 → 22.5 | 75.0 → 11.2 | 8.0 → 1.2 | 100 → 15.0 | **78.5** |
| qwen3.5-122b-a10b | 100 → 30.0 | 75 → 18.8 | 82.0 → 12.3 | 25.0 → 3.8 | 90 → 13.5 | **78.3** |
| glm-4.7 | 100 → 30.0 | 50 → 12.5 | 85.0 → 12.8 | 52.0 → 7.8 | 100 → 15.0 | **78.0** |
| deepseek-v4-pro | 100 → 30.0 | 45 → 11.2 | 88.0 → 13.2 | 55.0 → 8.2 | 100 → 15.0 | **77.7** |
| qwen3.5-9b | 95 → 28.5 | 85 → 21.2 | 81.7 → 12.3 | 12.0 → 1.8 | 90 → 13.5 | **77.3** |
| nemotron-3-super-120b-a12b | 75 → 22.5 | 75 → 18.8 | 75.7 → 11.4 | 60.0 → 9.0 | 100 → 15.0 | **76.6** |
| phi-4-multimodal | 100 → 30.0 | 95 → 23.8 | 55.0 → 8.2 | 5.0 → 0.8 | 75 → 11.2 | **74.0** |
| nemotron-nano-9b-v2 | 100 → 30.0 | 85 → 21.2 | 64.0 → 9.6 | 8.0 → 1.2 | 75 → 11.2 | **73.3** |
| devstral-2-123b | 100 → 30.0 | 30 → 7.5 | 45.0 → 6.8 | 40.0 → 6.0 | 90 → 13.5 | **63.8** |
| glm-5.1 | 15 → 4.5 | 50 → 12.5 | 90.0 → 13.5 | 58.4 → 8.8 | 85 → 12.8 | **52.0** |

---

## Key Insights

1. **#1 deepseek-v4-flash** (80.2) — the explore king: FREE, 1M ctx, SWE-Bench 38%, GPQA 80%. Unbeatable for search/grep tasks at zero cost.
2. **#2 step-3.5-flash** (80.0) — nearly tied, FREE, GPQA 83.5%, SWE-Bench 35%. Slightly better reasoning but 256K ctx vs 1M.
3. **SWE-Bench Pro reshuffles the ranking** vs quick/unspecified-low. Free large models with high SWE scores (glm-4.7, deepseek-v4-pro) jump into top 6, while small free models (llama-3.2-1b, phi-3-mini) drop because SWE-Bench Pro ≈ 0–2%.
4. **glm-4.7** (78.0) — the biggest surprise: FREE, 2.54M ctx, SWE-Bench 52%. Massive context + strong coding = ideal for explore.
5. **nemotron-3-nano-30b-a3b** (78.5) — still #3 despite SWE-Bench 8%. Its $0.05 cost + 1M ctx + 3.6B active params keep it competitive.
6. **glm-5.1** (52.0) — SWE-Bench Pro #1 at 58.4%, but $1.05/$3.50 pricing kills its explore score. Explore prioritizes speed/cost over raw reasoning.
7. **devstral-2-123b** (63.8) — SWE-Bench 40% is excellent, but 123B dense = latency tier 30. Free but slow for search tasks.
8. **nemotron-3-super-120b-a12b** (76.6) — highest SWE-Bench (60%) among paid models, 1M ctx. Best paid option for explore when quality matters.
9. **minimax-m2.7** (67.0) — 3.05M ctx is the largest in the ranking, but 230B dense = latency tier 25. Context-heavy explore tasks only.
10. **granite-3.3-8b** (47.7) — still the worst value. $0.50/$0.50 for 8B when free 8Bs exist.

---

## Explore vs Quick Ranking Comparison

| Model | Quick Score | Explore Score | Delta | Reason |
|---|---|---|---|---|
| deepseek-v4-flash | 90.4 | 80.2 | −10.2 | SWE-Bench 38% adds value but weight shift (Cost 40→30%, Lat 30→25%) hurts |
| step-3.5-flash | 91.0 | 80.0 | −11.0 | Same weight shift effect |
| nemotron-3-nano-30b-a3b | 93.5 | 78.5 | −15.0 | SWE-Bench 8% doesn't compensate for weight shift away from cost/latency |
| glm-4.7 | N/A | 78.0 | NEW | Free + 2.54M ctx + SWE 52% — explore-only addition |
| deepseek-v4-pro | N/A | 77.7 | NEW | Free + 1M ctx + SWE 55% — explore-only addition |
| glm-5.1 | N/A | 52.0 | NEW | SWE #1 but $1.05 kills explore score |

---

## Benchmark Sources

- **GPQA Diamond:** HuggingFace model cards, LLM Stats, pricepertoken.com, OpenRouter benchmarks
- **SWE-Bench Pro:** swebench.com leaderboard, NVIDIA technical reports, model family proxy estimates
- **Pricing:** build.nvidia.com/models, NVIDIA NIM API, pricepertoken.com/pricing-page/provider/nvidia
- **Context windows:** NVIDIA Build model documentation
- **MoE active params:** Model cards and technical reports

**Note:** SWE-Bench Pro scores for small models (1–12B) are estimates based on model family and size, as no published benchmarks were found for most NVIDIA Build variants. Code-focused models (Devstral, Qwen3-Coder) are estimated higher than general models of similar size. Published scores exist for: GLM-5.1 (58.4%), Nemotron-3-Super-120B (60%), GPT-5.4 family (52–60%).

---

*Generated April 25, 2026. Part of the oh-my-opencode agent rankings series.*
*See also: [v3.0 Canonical Rankings](oh-my-opencode-agent-rankings.md) | [All-Providers Rankings](oh-my-opencode-agent-rankings-all-providers.md) | [Extended Quick Rankings](extended-rankings-quick-nvidia-build.md)*
