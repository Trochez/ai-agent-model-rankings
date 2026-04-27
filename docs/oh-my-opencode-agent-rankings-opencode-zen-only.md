# Oh-My-OpenCode Agent Model Rankings — OpenCode Zen Only

**Date:** April 24, 2026
**Scope:** Only models available on OpenCode Zen (`opencode/` prefix)
**Companion to:** [oh-my-opencode-agent-rankings.md](./oh-my-opencode-agent-rankings.md) (v3.0, all 3 providers)

---

## Executive Summary

This document provides model rankings for every oh-my-opencode agent and category, covering **only OpenCode Zen models**. Each agent/category has **two tables**:

1. **Performance Table**: Top 3 models by composite performance score (0-100)
2. **Cost/Performance Table**: Top 3 models by cost-performance ratio (higher = better value)

### OpenCode Zen Models Included

| Model | Input $/1M | Output $/1M | Context | Vision | Tools |
|-------|-----------|------------|---------|--------|-------|
| `opencode/gemini-3-flash` | $0.50 | $3.00 | 128K | Yes | Yes |
| `opencode/qwen3-coder` | $0.45 | $1.50 | 128K | No | Yes |
| `opencode/qwen3.6-plus` | $0.50 | $3.00 | 128K | Yes | Yes |
| `opencode/qwen3.6-plus-free` | Free | Free | 1M | Yes | Yes |
| `opencode/gemini-3.1-pro` | $2.00 | $12.00 | 128K | Yes | Yes |
| `opencode/claude-opus-4-6` | $5.00 | $25.00 | 200K | No | Yes |

### Scoring Methodology

Scores follow the same weight formulas as the all-providers document:

| Agent Type | Agents/Categories | Weight Formula |
|---|---|---|
| **Reasoning-heavy** | sisyphus, prometheus, atlas, unspecified-high | GPQA 30% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 15% + Cost-eff 10% |
| **Coding-heavy** | hephaestus | SWE-Bench Pro 35% + HumanEval 25% + GPQA 15% + Terminal-Bench 15% + Cost-eff 10% |
| **Deep-reasoning** | oracle, metis, momus, ultrabrain, deep, artistry | GPQA 35% + SWE-Bench Pro 25% + ARC-AGI-2 20% + MMLU-Pro 10% + Cost-eff 10% |
| **Speed-heavy** | explore, librarian | Cost-eff 30% + Latency-tier 25% + GPQA 15% + SWE-Bench Pro 15% + Context 15% |
| **Vision-heavy** | multimodal-looker, visual-engineering | MMMU-Pro 30% + GPQA 20% + SWE-Bench Pro 20% + Context 15% + Cost-eff 15% |
| **Writing/research** | writing | MMLU-Pro 30% + GPQA 20% + Cost-eff 25% + Context 15% + SWE-Bench Pro 10% |
| **Quick/low** | quick, unspecified-low | Cost-eff 40% + Latency-tier 30% + GPQA 15% + Context 15% |
| **Junior/orchestration** | sisyphus-junior | SWE-Bench Pro 25% + GPQA 25% + ARC-AGI-2 15% + Cost-eff 20% + Context 15% |

**Cost/Performance Score** = `(Performance Score × 1000) / (Input Cost per 1M tokens)`
- Free models: Score = `Performance Score × 100` (very high, reflecting zero cost)
- Higher cost/performance = better value for money

### Data Sources

- **Explicit scores**: From v3.0 rankings doc and .omx model-rankings-report.md
- **Estimated scores**: For models without explicit per-agent scores, estimated from all-providers benchmark data and OpenCode Zen pricing
- **Pricing**: From OpenCode Zen official documentation (opencode.ai/docs/zen)

---

## Agent Rankings

### sisyphus (Orchestrator — Reasoning-heavy)

**Performance Ranking — sisyphus**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **90** | $5.00 |
| 2 | `opencode/qwen3.6-plus` | **88** | $0.50 |
| 3 | `opencode/gemini-3.1-pro` | **87** | $2.00 |

**Cost/Performance Ranking — sisyphus**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,600** | 86 | Free |
| 2 | `opencode/qwen3.6-plus` | **176,000** | 88 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### hephaestus (Executor — Coding-heavy)

**Performance Ranking — hephaestus**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/qwen3-coder` | **90** | $0.45 |
| 2 | `opencode/claude-opus-4-6` | **89** | $5.00 |
| 3 | `opencode/gemini-3.1-pro` | **87** | $2.00 |

**Cost/Performance Ranking — hephaestus**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,400** | 84 | Free |
| 2 | `opencode/qwen3-coder` | **200,000** | 90 | $0.45 |
| 3 | `opencode/qwen3.6-plus` | **170,000** | 85 | $0.50 |

### oracle (Consultant — Deep-reasoning)

**Performance Ranking — oracle**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 |
| 2 | `opencode/gemini-3.1-pro` | **89** | $2.00 |
| 3 | `opencode/qwen3.6-plus` | **88** | $0.50 |

**Cost/Performance Ranking — oracle**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,600** | 86 | Free |
| 2 | `opencode/qwen3.6-plus` | **176,000** | 88 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### explore (Search — Speed-heavy)

**Performance Ranking — explore**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **95** | $0.50 |
| 2 | `opencode/qwen3.6-plus-free` | **93** | Free |
| 3 | `opencode/qwen3-coder` | **91** | $0.45 |

**Cost/Performance Ranking — explore**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **9,300** | 93 | Free |
| 2 | `opencode/qwen3-coder` | **202,222** | 91 | $0.45 |
| 3 | `opencode/gemini-3-flash` | **190,000** | 95 | $0.50 |

### prometheus (Planner — Reasoning-heavy)

**Performance Ranking — prometheus**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 |
| 2 | `opencode/qwen3.6-plus` | **89** | $0.50 |
| 3 | `opencode/gemini-3.1-pro` | **88** | $2.00 |

**Cost/Performance Ranking — prometheus**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,700** | 87 | Free |
| 2 | `opencode/qwen3.6-plus` | **178,000** | 89 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### metis (Analyst — Deep-reasoning)

**Performance Ranking — metis**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **92** | $5.00 |
| 2 | `opencode/qwen3.6-plus` | **90** | $0.50 |
| 3 | `opencode/gemini-3.1-pro` | **89** | $2.00 |

**Cost/Performance Ranking — metis**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,800** | 88 | Free |
| 2 | `opencode/qwen3.6-plus` | **180,000** | 90 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### momus (Critic — Deep-reasoning)

**Performance Ranking — momus**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 |
| 2 | `opencode/qwen3.6-plus` | **89** | $0.50 |
| 3 | `opencode/gemini-3.1-pro` | **88** | $2.00 |

**Cost/Performance Ranking — momus**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,700** | 87 | Free |
| 2 | `opencode/qwen3.6-plus` | **178,000** | 89 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### librarian (Research — Speed-heavy)

**Performance Ranking — librarian**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **98** | $0.50 |
| 2 | `opencode/qwen3.6-plus-free` | **95** | Free |
| 3 | `opencode/qwen3-coder` | **93** | $0.45 |

**Cost/Performance Ranking — librarian**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **9,500** | 95 | Free |
| 2 | `opencode/qwen3-coder` | **206,667** | 93 | $0.45 |
| 3 | `opencode/gemini-3-flash` | **196,000** | 98 | $0.50 |

### multimodal-looker (Vision — Vision-heavy)

**Performance Ranking — multimodal-looker**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/gemini-3.1-pro` | **93** | $2.00 |
| 2 | `opencode/claude-opus-4-6` | **88** | $5.00 |
| 3 | `opencode/qwen3.6-plus` | **85** | $0.50 |

**Cost/Performance Ranking — multimodal-looker**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,200** | 82 | Free |
| 2 | `opencode/qwen3.6-plus` | **170,000** | 85 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **160,000** | 80 | $0.50 |

### atlas (Knowledge — Reasoning-heavy)

**Performance Ranking — atlas**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **90** | $5.00 |
| 2 | `opencode/qwen3.6-plus` | **88** | $0.50 |
| 3 | `opencode/gemini-3.1-pro` | **87** | $2.00 |

**Cost/Performance Ranking — atlas**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,600** | 86 | Free |
| 2 | `opencode/qwen3.6-plus` | **176,000** | 88 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### sisyphus-junior (Junior Orchestrator — Junior/orchestration)

**Performance Ranking — sisyphus-junior**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/qwen3-coder` | **89** | $0.45 |
| 2 | `opencode/qwen3.6-plus` | **87** | $0.50 |
| 3 | `opencode/claude-opus-4-6` | **86** | $5.00 |

**Cost/Performance Ranking — sisyphus-junior**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,500** | 85 | Free |
| 2 | `opencode/qwen3-coder` | **197,778** | 89 | $0.45 |
| 3 | `opencode/qwen3.6-plus` | **174,000** | 87 | $0.50 |

---

## Category Rankings

### visual-engineering (Vision-heavy)

**Performance Ranking — visual-engineering**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/gemini-3.1-pro` | **92** | $2.00 |
| 2 | `opencode/claude-opus-4-6` | **87** | $5.00 |
| 3 | `opencode/gemini-3-flash` | **85** | $0.50 |

**Cost/Performance Ranking — visual-engineering**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,200** | 82 | Free |
| 2 | `opencode/gemini-3-flash` | **170,000** | 85 | $0.50 |
| 3 | `opencode/qwen3.6-plus` | **164,000** | 82 | $0.50 |

### ultrabrain (Deep-reasoning)

**Performance Ranking — ultrabrain**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 |
| 2 | `opencode/gemini-3.1-pro` | **88** | $2.00 |
| 3 | `opencode/qwen3.6-plus` | **87** | $0.50 |

**Cost/Performance Ranking — ultrabrain**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,500** | 85 | Free |
| 2 | `opencode/qwen3.6-plus` | **174,000** | 87 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### deep (Deep-reasoning)

**Performance Ranking — deep**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 |
| 2 | `opencode/gemini-3.1-pro` | **88** | $2.00 |
| 3 | `opencode/qwen3.6-plus` | **87** | $0.50 |

**Cost/Performance Ranking — deep**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,500** | 85 | Free |
| 2 | `opencode/qwen3.6-plus` | **174,000** | 87 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### artistry (Deep-reasoning)

**Performance Ranking — artistry**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **91** | $5.00 |
| 2 | `opencode/gemini-3.1-pro` | **88** | $2.00 |
| 3 | `opencode/qwen3.6-plus` | **87** | $0.50 |

**Cost/Performance Ranking — artistry**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,500** | 85 | Free |
| 2 | `opencode/qwen3.6-plus` | **174,000** | 87 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### quick (Quick/low)

**Performance Ranking — quick**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **97** | $0.50 |
| 2 | `opencode/qwen3.6-plus-free` | **96** | Free |
| 3 | `opencode/qwen3-coder` | **94** | $0.45 |

**Cost/Performance Ranking — quick**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **9,600** | 96 | Free |
| 2 | `opencode/qwen3-coder` | **208,889** | 94 | $0.45 |
| 3 | `opencode/gemini-3-flash` | **194,000** | 97 | $0.50 |

### unspecified-low (Quick/low)

**Performance Ranking — unspecified-low**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **97** | $0.50 |
| 2 | `opencode/qwen3.6-plus-free` | **96** | Free |
| 3 | `opencode/qwen3-coder` | **94** | $0.45 |

**Cost/Performance Ranking — unspecified-low**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **9,600** | 96 | Free |
| 2 | `opencode/qwen3-coder` | **208,889** | 94 | $0.45 |
| 3 | `opencode/gemini-3-flash` | **194,000** | 97 | $0.50 |

### unspecified-high (Reasoning-heavy)

**Performance Ranking — unspecified-high**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/claude-opus-4-6` | **90** | $5.00 |
| 2 | `opencode/qwen3.6-plus` | **88** | $0.50 |
| 3 | `opencode/gemini-3.1-pro` | **87** | $2.00 |

**Cost/Performance Ranking — unspecified-high**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **8,600** | 86 | Free |
| 2 | `opencode/qwen3.6-plus` | **176,000** | 88 | $0.50 |
| 3 | `opencode/gemini-3-flash` | **150,000** | 75 | $0.50 |

### writing (Writing/research)

**Performance Ranking — writing**

| # | Model | Score | $/1M In |
|---|---|---|---|
| 1 | `opencode/gemini-3-flash` | **98** | $0.50 |
| 2 | `opencode/qwen3.6-plus-free` | **95** | Free |
| 3 | `opencode/qwen3.6-plus` | **91** | $0.50 |

**Cost/Performance Ranking — writing**

| # | Model | C/P | Score | $/1M In |
|---|---|---|---|---|
| 1 | `opencode/qwen3.6-plus-free` | **9,500** | 95 | Free |
| 2 | `opencode/gemini-3-flash` | **196,000** | 98 | $0.50 |
| 3 | `opencode/qwen3.6-plus` | **182,000** | 91 | $0.50 |

---

## Summary: Best OpenCode Zen Model per Agent (Performance)

| Agent | Best Model | Score | 2nd Best | Score | 3rd Best | Score |
|---|---|---|---|---|---|---|
| sisyphus | `opencode/claude-opus-4-6` | **90** | `opencode/qwen3.6-plus` | 88 | `opencode/gemini-3.1-pro` | 87 |
| hephaestus | `opencode/qwen3-coder` | **90** | `opencode/claude-opus-4-6` | 89 | `opencode/gemini-3.1-pro` | 87 |
| oracle | `opencode/claude-opus-4-6` | **91** | `opencode/gemini-3.1-pro` | 89 | `opencode/qwen3.6-plus` | 88 |
| explore | `opencode/gemini-3-flash` | **95** | `opencode/qwen3.6-plus-free` | 93 | `opencode/qwen3-coder` | 91 |
| prometheus | `opencode/claude-opus-4-6` | **91** | `opencode/qwen3.6-plus` | 89 | `opencode/gemini-3.1-pro` | 88 |
| metis | `opencode/claude-opus-4-6` | **92** | `opencode/qwen3.6-plus` | 90 | `opencode/gemini-3.1-pro` | 89 |
| momus | `opencode/claude-opus-4-6` | **91** | `opencode/qwen3.6-plus` | 89 | `opencode/gemini-3.1-pro` | 88 |
| librarian | `opencode/gemini-3-flash` | **98** | `opencode/qwen3.6-plus-free` | 95 | `opencode/qwen3-coder` | 93 |
| multimodal-looker | `opencode/gemini-3.1-pro` | **93** | `opencode/claude-opus-4-6` | 88 | `opencode/qwen3.6-plus` | 85 |
| atlas | `opencode/claude-opus-4-6` | **90** | `opencode/qwen3.6-plus` | 88 | `opencode/gemini-3.1-pro` | 87 |
| sisyphus-junior | `opencode/qwen3-coder` | **89** | `opencode/qwen3.6-plus` | 87 | `opencode/claude-opus-4-6` | 86 |

## Summary: Best OpenCode Zen Model per Category (Performance)

| Category | Best Model | Score | 2nd Best | Score | 3rd Best | Score |
|---|---|---|---|---|---|---|
| visual-engineering | `opencode/gemini-3.1-pro` | **92** | `opencode/claude-opus-4-6` | 87 | `opencode/gemini-3-flash` | 85 |
| ultrabrain | `opencode/claude-opus-4-6` | **91** | `opencode/gemini-3.1-pro` | 88 | `opencode/qwen3.6-plus` | 87 |
| deep | `opencode/claude-opus-4-6` | **91** | `opencode/gemini-3.1-pro` | 88 | `opencode/qwen3.6-plus` | 87 |
| artistry | `opencode/claude-opus-4-6` | **91** | `opencode/gemini-3.1-pro` | 88 | `opencode/qwen3.6-plus` | 87 |
| quick | `opencode/gemini-3-flash` | **97** | `opencode/qwen3.6-plus-free` | 96 | `opencode/qwen3-coder` | 94 |
| unspecified-low | `opencode/gemini-3-flash` | **97** | `opencode/qwen3.6-plus-free` | 96 | `opencode/qwen3-coder` | 94 |
| unspecified-high | `opencode/claude-opus-4-6` | **90** | `opencode/qwen3.6-plus` | 88 | `opencode/gemini-3.1-pro` | 87 |
| writing | `opencode/gemini-3-flash` | **98** | `opencode/qwen3.6-plus-free` | 95 | `opencode/qwen3.6-plus` | 91 |

## Summary: Best Value OpenCode Zen Model per Agent (Cost/Performance)

| Agent | Best Value Model | C/P | Score | Cost |
|---|---|---|---|---|
| sisyphus | `opencode/qwen3.6-plus-free` | **8,600** | 86 | Free |
| hephaestus | `opencode/qwen3.6-plus-free` | **8,400** | 84 | Free |
| oracle | `opencode/qwen3.6-plus-free` | **8,600** | 86 | Free |
| explore | `opencode/qwen3.6-plus-free` | **9,300** | 93 | Free |
| prometheus | `opencode/qwen3.6-plus-free` | **8,700** | 87 | Free |
| metis | `opencode/qwen3.6-plus-free` | **8,800** | 88 | Free |
| momus | `opencode/qwen3.6-plus-free` | **8,700** | 87 | Free |
| librarian | `opencode/qwen3.6-plus-free` | **9,500** | 95 | Free |
| multimodal-looker | `opencode/qwen3.6-plus-free` | **8,200** | 82 | Free |
| atlas | `opencode/qwen3.6-plus-free` | **8,600** | 86 | Free |
| sisyphus-junior | `opencode/qwen3.6-plus-free` | **8,500** | 85 | Free |

## Summary: Best Value OpenCode Zen Model per Category (Cost/Performance)

| Category | Best Value Model | C/P | Score | Cost |
|---|---|---|---|---|
| visual-engineering | `opencode/qwen3.6-plus-free` | **8,200** | 82 | Free |
| ultrabrain | `opencode/qwen3.6-plus-free` | **8,500** | 85 | Free |
| deep | `opencode/qwen3.6-plus-free` | **8,500** | 85 | Free |
| artistry | `opencode/qwen3.6-plus-free` | **8,500** | 85 | Free |
| quick | `opencode/qwen3.6-plus-free` | **9,600** | 96 | Free |
| unspecified-low | `opencode/qwen3.6-plus-free` | **9,600** | 96 | Free |
| unspecified-high | `opencode/qwen3.6-plus-free` | **8,600** | 86 | Free |
| writing | `opencode/qwen3.6-plus-free` | **9,500** | 95 | Free |

---

## Key Insights

1. **`opencode/claude-opus-4-6`** leads performance in reasoning-heavy agents (90-92) but at $5/$25 — 10× the cost of qwen3.6-plus
2. **`opencode/gemini-3-flash`** dominates speed-heavy and writing categories (95-98) at only $0.50/$3.00
3. **`opencode/qwen3-coder`** tops coding-heavy agents (90) at the lowest paid price ($0.45/$1.50)
4. **`opencode/qwen3.6-plus-free`** wins cost/performance everywhere (free, 1M context) but with lower raw scores (82-96)
5. **`opencode/gemini-3.1-pro`** is the best for vision-heavy tasks (92-93) at $2/$12
6. **`opencode/qwen3.6-plus`** is the best-value paid model across reasoning agents (88-90 at $0.50/$3.00)

---

## Related Documents

- [Oh-My-OpenCode Agent Rankings v3.0](./oh-my-opencode-agent-rankings.md) — NVIDIA Build + OpenCode Zen + OpenAI
- [Oh-My-OpenCode Agent Rankings — All OpenRouter Providers](./oh-my-opencode-agent-rankings-all-providers.md) — All 294 ranked models
- [Oh-My-OpenCode Agent Rankings — OpenAI Only](./oh-my-opencode-agent-rankings-openai-only.md) — OpenAI provider deep dive
- [OpenCode Zen Model Rankings (.omx)](../.omx/model-rankings-report.md) — 25-agent detailed report

---

**Last Updated:** April 24, 2026
