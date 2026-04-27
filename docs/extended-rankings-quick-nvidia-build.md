# Extended Rankings — Quick Category (NVIDIA Build Only)

**Date:** April 25, 2026  
**Scope:** NVIDIA Build models only, quick/unspecified-low agent category  
**Formula:** Cost-eff 40% + Latency-tier 30% + GPQA 15% + Context 15%

---

## Methodology

### Quick/low Weight Formula

| Component | Weight | Description |
|---|---|---|
| Cost-efficiency | 40% | Normalized pricing score (FREE=100, higher cost=lower) |
| Latency-tier | 30% | Normalized speed score based on active params (<3B=100, 3-8B=95, 8-15B=85, MoE 3-4B act=90, MoE 11B+ act=75, 24B dense=60) |
| GPQA Diamond | 15% | Graduate-level reasoning benchmark, normalized 0–100 |
| Context window | 15% | Normalized context (1M+=100, 256K=90, 131K=80, 128K=75, 33K=40, 32K=38, 8K=15) |

Each component is normalized to 0–100 before weighting. Final Score = Σ(component × weight).

### Cost/Performance Ratio

- **Paid models:** `C/P = (Score × 1,000) / (Input $/1M tokens)`
- **Free models:** `C/P = Score × 100` (reflects infinite value at zero cost, capped for comparability)

---

## Performance Ranking (Expanded — 30 Models)

| Rank | Model | Score | Params | Ctx | $/1M In | $/1M Out | Free | Key Strength |
|---|---|---|---|---|---|---|---|---|
| 1 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **93.5** | 31.6B/3.6B act | 1M | $0.05 | $0.20 | | Best balance: cheap + fast + smart |
| 2 | `nvidia/qwen/qwen3.5-9b` | **92.7** | 9.65B | 256K | $0.05 | $0.15 | | Frontier reasoning at 9B |
| 3 | `nvidia/stepfun-ai/step-3.5-flash` | **91.0** | 196B/11B act | 256K | $0.00 | $0.00 | ✅ | Free + GPQA 83.5% |
| 4 | `nvidia/deepseek-ai/deepseek-v4-flash` | **90.4** | 284B/13B act | 1M | $0.00 | $0.00 | ✅ | Free + 1M ctx + MIT |
| 5 | `nvidia/microsoft/phi-4-multimodal-instruct` | **88.1** | ~5.6B | 128K | $0.00 | $0.00 | ✅ | Phi‑4 reasoning + vision |
| 6 | `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | **88.3** | 9B | 128K | $0.00 | $0.00 | ✅ | Free + 126 tok/s |
| 7 | `nvidia/google/gemma-4-26b-a4b-it` | **87.4** | 25.2B/3.8B act | 256K | $0.08 | $0.35 | | GPQA 82.3%, MoE efficient |
| 8 | `nvidia/mistralai/mistral-nemo-minitron-8b-base` | **87.0** | 8B | 128K | $0.00 | $0.00 | ✅ | Free 8B workhorse |
| 9 | `nvidia/microsoft/phi-3-mini-128k-instruct` | **86.1** | 3.8B | 128K | $0.00 | $0.00 | ✅ | Free + 128K ctx |
| 10 | `nvidia/meta-llama/llama-3.2-3b-instruct` | **85.8** | 3.21B | 128K | $0.00 | $0.00 | ✅ | Free ultra-fast |
| 11 | `nvidia/microsoft/phi-3-small-128k-instruct` | **85.4** | 7B | 128K | $0.00 | $0.00 | ✅ | Free + 7B quality |
| 12 | `nvidia/meta-llama/llama-3.2-1b-instruct` | **84.0** | 1.23B | 128K | $0.00 | $0.00 | ✅ | Free + minimal latency |
| 13 | `nvidia/meta-llama/llama-3.2-11b-vision-instruct` | **83.1** | 10.6B | 128K | $0.00 | $0.00 | ✅ | Free + vision |
| 14 | `nvidia/ising/ising-calibration-1-35b-a3b` | **82.8** | 35B/3B act MoE | 128K | $0.00 | $0.00 | ✅ | Quantum calibration VLM |
| 15 | `nvidia/microsoft/phi-4-mini-instruct` | **81.6** | 3.8B | 128K | $0.075 | $0.30 | | Best math at 3.8B |
| 16 | `nvidia/google/gemma-2-2b-it` | **79.3** | 2B | 32K | $0.00 | $0.00 | ✅ | Free edge model |
| 17 | `nvidia/google/gemma-3n-e2b-it` | **78.0** | 2B | 32K | $0.00 | $0.00 | ✅ | Gemma‑3 edge (2B) |
| 18 | `nvidia/google/gemma-3n-e4b-it` | **78.0** | 4B | 32K | $0.00 | $0.00 | ✅ | Gemma‑3 edge (4B) |
| 19 | `nvidia/nvidia/nemotron-nano-12b-v2-vl` | **78.7** | 12B | 128K | $0.20 | $0.20 | | Vision-language |
| 20 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **77.7** | 120B/12B act | 1M | $0.10 | $0.50 | | 1M ctx + SWE-bench 60% |
| 21 | `nvidia/google/gemma-3-27b-it` | **77.1** | 27B dense | 128K | $0.00 | $0.00 | ✅ | Gemma‑3 27B dense |
| 22 | `nvidia/mistralai/devstral-2-123b-instruct-2512` | **77.8** | 123B dense | 256K | $0.00 | $0.00 | ✅ | Code‑focused 123B |
| 23 | `nvidia/google/gemma-3-1b-it` | **77.5** | 1B | 32K | $0.00 | $0.00 | ✅ | Free ultra-edge |
| 24 | `nvidia/microsoft/phi-3-small-8k-instruct` | **76.5** | 7B | 8K | $0.00 | $0.00 | ✅ | Free (8K ctx limit) |
| 25 | `nvidia/nvidia/nemotron-mini-4b-instruct` | **76.2** | 4B | 8K | $0.00 | $0.00 | ✅ | Free + 2GB VRAM |
| 26 | `nvidia/qwen/qwen3.5-35b-a3b` | **75.2** | 36B/3B act | 262K | $0.25 | $1.25 | | MoE 3B active, GPQA ~82% |
| 27 | `nvidia/mistralai/mistral-small-24b-instruct` | **71.1** | 24B | 33K | $0.05 | $0.08 | | Cheap but 33K ctx |
| 28 | `nvidia/mistralai/mistral-small-3.1-24b-instruct-2503` | **70.4** | 24B | 128K | $0.10 | $0.30 | | Multimodal 24B |
| 29 | `nvidia/meta-llama/llama-3.3-nemotron-super-49b-v1.5` | **67.8** | 49B dense | 131K | $0.10 | $0.40 | | Expensive for GPQA 51.7% |
| 30 | `nvidia/ibm-granite/granite-3.3-8b-instruct` | **63.9** | 8B | 128K | $0.50 | $0.50 | | Overpriced vs free 8Bs |

**Note:** `qwen/qwen3.5-122b-a10b` (122B/10B act MoE) likely FREE on NVIDIA Build but GPQA uncertain; `glm-4.7` endpoint exists but specs unclear; `gemma-4-31b-it` and `ministral-14b-instruct-2512` are downloadable‑only (no hosted API).

---

## Cost/Performance Ranking (Top 15)

| Rank | Model | C/P | Score | $/1M In | $/1M Out | Ctx | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/stepfun-ai/step-3.5-flash` | **9,100** | 91.0 | $0.00 | $0.00 | 256K | ✅ |
| 2 | `nvidia/deepseek-ai/deepseek-v4-flash` | **9,040** | 90.4 | $0.00 | $0.00 | 1M | ✅ |
| 3 | `nvidia/microsoft/phi-4-multimodal-instruct` | **8,810** | 88.1 | $0.00 | $0.00 | 128K | ✅ |
| 4 | `nvidia/nvidia/nvidia-nemotron-nano-9b-v2` | **8,830** | 88.3 | $0.00 | $0.00 | 128K | ✅ |
| 5 | `nvidia/mistralai/mistral-nemo-minitron-8b-base` | **8,700** | 87.0 | $0.00 | $0.00 | 128K | ✅ |
| 6 | `nvidia/microsoft/phi-3-mini-128k-instruct` | **8,610** | 86.1 | $0.00 | $0.00 | 128K | ✅ |
| 7 | `nvidia/meta-llama/llama-3.2-3b-instruct` | **8,580** | 85.8 | $0.00 | $0.00 | 128K | ✅ |
| 8 | `nvidia/microsoft/phi-3-small-128k-instruct` | **8,540** | 85.4 | $0.00 | $0.00 | 128K | ✅ |
| 9 | `nvidia/meta-llama/llama-3.2-1b-instruct` | **8,400** | 84.0 | $0.00 | $0.00 | 128K | ✅ |
| 10 | `nvidia/meta-llama/llama-3.2-11b-vision-instruct` | **8,310** | 83.1 | $0.00 | $0.00 | 128K | ✅ |
| 11 | `nvidia/ising/ising-calibration-1-35b-a3b` | **8,280** | 82.8 | $0.00 | $0.00 | 128K | ✅ |
| 12 | `nvidia/google/gemma-3n-e2b-it` | **7,800** | 78.0 | $0.00 | $0.00 | 32K | ✅ |
| 13 | `nvidia/google/gemma-3n-e4b-it` | **7,800** | 78.0 | $0.00 | $0.00 | 32K | ✅ |
| 14 | `nvidia/google/gemma-3-27b-it` | **7,710** | 77.1 | $0.00 | $0.00 | 128K | ✅ |
| 15 | `nvidia/mistralai/devstral-2-123b-instruct-2512` | **7,780** | 77.8 | $0.00 | $0.00 | 256K | ✅ |

**Paid models (C/P > 1M):**
| Rank | Model | C/P | Score | $/1M In | $/1M Out | Ctx | Free |
|---|---|---|---|---|---|---|---|
| 1 | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | **1,870,000** | 93.5 | $0.05 | $0.20 | 1M | |
| 2 | `nvidia/qwen/qwen3.5-9b` | **1,854,000** | 92.7 | $0.05 | $0.15 | 256K | |
| 3 | `nvidia/mistralai/mistral-small-24b-instruct` | **1,422,000** | 71.1 | $0.05 | $0.08 | 33K | |
| 4 | `nvidia/google/gemma-4-26b-a4b-it` | **1,092,500** | 87.4 | $0.08 | $0.35 | 256K | |
| 5 | `nvidia/microsoft/phi-4-mini-instruct` | **1,088,000** | 81.6 | $0.075 | $0.30 | 128K | |
| 6 | `nvidia/nvidia/nemotron-3-super-120b-a12b` | **777,000** | 77.7 | $0.10 | $0.50 | 1M | |

---

## Score Breakdown (Top 10 + New Highlights)

| Model | Cost-eff (40%) | Latency (30%) | GPQA (15%) | Context (15%) | Total |
|---|---|---|---|---|---|
| nemotron-3-nano-30b-a3b | 95 → 38.0 | 90 → 27.0 | 90 → 13.5 | 100 → 15.0 | **93.5** |
| qwen3.5-9b | 90 → 36.0 | 95 → 28.5 | 98 → 14.7 | 90 → 13.5 | **92.7** |
| step-3.5-flash | 100 → 40.0 | 75 → 22.5 | 100 → 15.0 | 90 → 13.5 | **91.0** |
| deepseek-v4-flash | 100 → 40.0 | 70 → 21.0 | 96 → 14.4 | 100 → 15.0 | **90.4** |
| phi-4-multimodal | 100 → 40.0 | 95 → 28.5 | 55 → 8.3 | 75 → 11.3 | **88.1** |
| nemotron-nano-9b-v2 | 100 → 40.0 | 85 → 25.5 | 77 → 11.6 | 75 → 11.3 | **88.3** |
| gemma-4-26b-a4b-it | 80 → 32.0 | 90 → 27.0 | 99 → 14.9 | 90 → 13.5 | **87.4** |
| mistral-nemo-minitron-8b | 100 → 40.0 | 95 → 28.5 | 48 → 7.2 | 75 → 11.3 | **87.0** |
| phi-3-mini-128k | 100 → 40.0 | 95 → 28.5 | 42 → 6.3 | 75 → 11.3 | **86.1** |
| ising-calibration-1-35b-a3b | 100 → 40.0 | 90 → 27.0 | 30 → 4.5 | 75 → 11.3 | **82.8** |
| llama-3.3-nemotron-super-49b | 75 → 30.0 | 60 → 18.0 | 51.7 → 7.8 | 80 → 12.0 | **67.8** |

---

## Key Insights (Expanded)

1. **#1 nemotron-3-nano-30b-a3b** (93.5) — best overall: $0.05/$0.20, 1M ctx, 3.6B active params, GPQA 75%. The sweet spot for quick tasks.
2. **step-3.5-flash** and **deepseek-v4-flash** are FREE with 90+ scores — unbeatable C/P if you don't need guaranteed SLAs.
3. **qwen3.5-9b** at 92.7 is remarkable — 9B dense model with GPQA 81.7%, only $0.05/$0.15.
4. **phi-4-multimodal-instruct** (88.1) enters as a strong free contender — Phi‑4 reasoning + vision at zero cost.
5. The free tier is crowded: 15 models score 77–91, all at $0 cost. Differentiation comes from context window and GPQA.
6. **ising-calibration-1-35b-a3b** (82.8) — niche quantum calibration VLM, FREE, MoE 35B/3B active.
7. **llama-3.3-nemotron-super-49b-v1.5** (67.8) — expensive for its GPQA 51.7%: $0.10/$0.40 for 49B dense.
8. **granite-3.3-8b** (63.9) remains the worst value — $0.50/$0.50 when free 8B alternatives exist.
9. Among free models, **step-3.5-flash** leads on quality (GPQA 83.5%) while **llama-3.2-1b** leads on latency (1.23B params).
10. **gemma-3-27b-it** (77.1) and **devstral-2-123b** (77.8) offer large‑model capabilities at zero cost, but GPQA lags behind smaller free models.

---

## Benchmark Sources

- GPQA Diamond: LLM Stats, HuggingFace model cards, OpenRouter benchmarks, pricepertoken.com (for Nemotron variants)
- Pricing: build.nvidia.com/models, NVIDIA NIM API, pricepertoken.com/pricing-page/provider/nvidia (9 paid NVIDIA models)
- Context windows: NVIDIA Build model documentation
- Throughput/latency: NVIDIA NIM performance benchmarks, BuildFastWithAI April 2026 rankings
- MoE active params: Model cards and technical reports

**Note:** GPQA scores for newly added models (Gemma‑3, Phi‑4, Ising, Devstral) are estimates based on model family and size, pending official benchmark publication.

---

*Generated April 25, 2026. Part of the oh-my-opencode agent rankings series.*  
*See also: [v3.0 Canonical Rankings](oh-my-opencode-agent-rankings.md) | [All-Providers Rankings](oh-my-opencode-agent-rankings-all-providers.md) | [Extended Visual-Engineering Rankings](extended-rankings-visual-engineering.md)*