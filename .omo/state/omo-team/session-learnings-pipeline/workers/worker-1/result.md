# Embedding Models for Semantic Search: Session Learnings

## Executive Summary
*   **Top Performer**: `nv-embed-v1` (NVIDIA Build) leads in MTEB benchmarks (69.32) and context window (32k tokens), making it the optimal choice for high-quality semantic search.
*   **Multilingual/Flexible**: `llama-nemotron-embed-1b-v2` (NVIDIA Build/OpenCode) offers strong multilingual support and Matryoshka embedding capabilities for optimized storage.
*   **Cost-Efficiency**: `text-embedding-3-small` (OpenAI) remains the best option for cost-sensitive MVPs, balancing performance and price.
*   **Platform Strategy**: NVIDIA Build is the primary source for high-performance, specialized embedding models, while OpenAI provides stable, enterprise-ready APIs.

## Detailed Learnings

### Performance Metrics
*   **nv-embed-v1**: High-dimensional (4096) model with a large context window (32k). Best for complex RAG tasks where precision is critical.
*   **text-embedding-3-large**: Good enterprise choice, but `text-embedding-3-small` often provides better value for general use cases.
*   **llama-nemotron-embed-1b-v2**: Efficient model (2048 dims) with Matryoshka support, allowing for dynamic dimensionality reduction without significant performance loss.

### Platform Availability
*   **NVIDIA Build**: Hosts the most advanced models for technical and RAG-heavy tasks (`nv-embed-v1`, `nv-embedcode-7b-v1`).
*   **OpenAI**: Offers reliable, low-latency API access for standard semantic search needs.
*   **OpenCode**: Supports self-hosted or local deployment of models like `llama-nemotron-embed-1b-v2`, providing control over data privacy and infrastructure.

## Recommendations

| Use Case | Recommended Model | Platform |
| :--- | :--- | :--- |
| **Maximum Quality/Precision** | `nv-embed-v1` | NVIDIA Build |
| **Multilingual/Self-hosted** | `llama-nemotron-embed-1b-v2` | NVIDIA Build / OpenCode |
| **Cost-Effective MVP** | `text-embedding-3-small` | OpenAI |
| **General Enterprise** | `text-embedding-3-large` | OpenAI |

## Caveats and Limitations
*   **Context Window**: While `nv-embed-v1` supports 32k tokens, ensure your downstream LLM can handle the retrieved context size.
*   **Deployment**: Self-hosting models like `llama-nemotron-embed-1b-v2` requires infrastructure management compared to using managed APIs.
*   **Dimensionality**: High-dimensional models (4096) increase storage requirements for vector databases. Consider Matryoshka-capable models if storage is a constraint.
