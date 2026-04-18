# Embedding Models for Semantic Search

## Overview

This document captures session learnings for embedding model selection in semantic search and RAG workloads.

### Models Evaluated

- `nv-embed-v1` (NVIDIA Build)
- `llama-nemotron-embed-1b-v2` (NVIDIA Build / OpenCode)
- `text-embedding-3-small` (OpenAI)
- `text-embedding-3-large` (OpenAI)

## Ranking (Session Recommendation)

| Rank | Model | Platform | Score (/100) | Notes |
| :-- | :-- | :-- | :--: | :-- |
| 1 | `nv-embed-v1` | NVIDIA Build | 95 | Best overall quality for retrieval; strong benchmark signal (MTEB 69.32) and 32k context |
| 2 | `llama-nemotron-embed-1b-v2` | NVIDIA Build / OpenCode | 91 | Strong multilingual performance and Matryoshka support for storage/latency optimization |
| 3 | `text-embedding-3-small` | OpenAI | 88 | Best cost/performance for MVP and high-volume workloads |
| 4 | `text-embedding-3-large` | OpenAI | 86 | Solid enterprise default when prioritizing quality over cost |

> Scoring is recommendation-oriented for this project (quality, flexibility, cost, and deployment fit), based on the worker synthesis.

## Platform-Specific Recommendations

### NVIDIA Build

- **Use when**: maximum retrieval precision, technical/RAG-heavy workloads, large context needs.
- **Primary model**: `nv-embed-v1`
- **Alternative**: `llama-nemotron-embed-1b-v2` when multilingual support or dimensionality flexibility is needed.

### OpenAI

- **Use when**: managed API simplicity, stable latency, enterprise integrations.
- **Primary model (cost-sensitive)**: `text-embedding-3-small`
- **Primary model (quality-sensitive)**: `text-embedding-3-large`

### OpenCode

- **Use when**: self-hosted/local control, privacy constraints, and infrastructure ownership.
- **Recommended model**: `llama-nemotron-embed-1b-v2` (self-hosted or routed through configured providers).

## Model ID Formats and Configuration Examples

Use provider-correct IDs; do not assume cross-provider naming is interchangeable.

### OpenAI Embeddings API

```json
{
  "model": "text-embedding-3-small",
  "input": "example semantic search text"
}
```

### NVIDIA Build (provider-routed configuration style)

```json
{
  "provider": "nvidia",
  "model": "nvidia/nv-embed-v1"
}
```

### OpenCode-style model selection (self-hosted/provider-backed)

```json
{
  "model": "nvidia/llama-nemotron-embed-1b-v2"
}
```

## Practical Selection Guide

- **Need top quality** → pick `nv-embed-v1`
- **Need multilingual + storage optimization** → pick `llama-nemotron-embed-1b-v2`
- **Need low cost at scale** → pick `text-embedding-3-small`
- **Need managed enterprise default** → pick `text-embedding-3-large`

## Caveats

- 4096-dimensional embeddings (for example, `nv-embed-v1`) can materially increase vector DB storage.
- If you self-host, include operational costs (deployment, monitoring, autoscaling) in total cost analysis.
- Keep chunking strategy aligned with the embedding model context limit and downstream retriever behavior.

## Official Documentation

- OpenAI Embeddings: https://platform.openai.com/docs/guides/embeddings
- OpenAI Models: https://platform.openai.com/docs/models
- NVIDIA Build Models: https://build.nvidia.com/models
- NVIDIA NIM / Embeddings overview: https://docs.nvidia.com/nim/
- OpenCode documentation: https://opencode.ai/docs
