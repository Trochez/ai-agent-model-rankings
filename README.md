['OpenCode Sessions] -->|Metric Emission| B[Profile Collector]\n    B -->|Raw Metrics| C[Data Storage Layer]\n    C -->|Processed Data| D[Visualization Interface]\n    D -->|User Queries| E[API Layer]\n    E -->|REST Responses| F[Frontend]\n    C -->|Historical Data| G[Report Generation]\n```\n\n## Usage Examples\n\n### API Endpoints\n\n| Endpoint | Method | Description |\n|----------|--------|-------------|\n| `/api/v1/sessions` | GET | List all monitored sessions |\n| `/api/v1/metrics` | GET | Retrieve metric data with filtering |\n| `/api/v1/reports` | GET | Generate comprehensive reports |\n| `/api/v1/health` | GET | Health check endpoint |\n\n### Sample API Call\n\n```bash\ncurl -H "Authorization: Bearer YOUR_API_KEY" \n     "https://profile-tool.example.com/api/v1/metrics?session_id=ses_12345" \n     -G --data-urlencode "metric_type=cpu_usage" \n     --data-urlencode "start_time=2026-04-30T22:00:00Z" \n     --data-urlencode "end_time=2026-04-30T23:00:00Z', 'Development Setup\n\n### Prerequisites\n\n- Node.js 18+\n- Docker (for database containers)\n- pnpm (package manager)\n- OpenCode CLI (for session integration testing)\n\n### Installation\n\n```bash\n# Clone repository\ngit clone https://github.com/open-source-org/opencode-profile-tool.git\ncd opencode-profile-tool\n\n# Install dependencies\npnpm install\n\n# Start database (SQLite for development)\ndocker-compose up -d\n\n# Build frontend assets\npnpm run build\n\n# Run development server\npnpm run dev\n```\n\n### Configuration\n\nEnvironment variables can be set in `.env`:\n\n```env\nDATABASE_URL=sqlite://./dev.db\nAPI_PORT=3001\nAUTH_TOKEN_SECRET=your-secret-key\nMAX_RETENTION_DAYS=90\n```\n\n## Testing Strategy\n\n1. **Unit Tests**: Validate individual component logic\n2. **Integration Tests**: Verify end-to-end data flow\n3. **Load Testing**: Simulate concurrent metric emissions\n4. **Regression Testing**: Run test suite after each change\n5. **Test Coverage**: Maintain >85% coverage\n\n## Future Enhancements\n\n- Real-time streaming metrics via WebSockets\n- AI-driven anomaly detection and predictive alerts\n- Cross-session comparative analysis\n- Collaborative dashboards for team-based development\n- Export to external monitoring platforms (Prometheus, Grafana)\n\n## License\n\nMIT License - See `LICENSE` file for details']

## Project Structure

```
explorer/
├── docs/
│   ├── oh-my-opencode-agent-rankings.md # v3.0 rankings (current, April 20)
│ ├── oh-my-opencode-agent-rankings-all-providers.md # All OpenRouter providers (April 24)
│ ├── oh-my-opencode-agent-rankings-openai-only.md # OpenAI-only rankings (April 24)
│ ├── oh-my-opencode-agent-rankings-openai-cost-performance.md # OpenAI cost-performance CPI rankings (April 27)
│ ├── oh-my-opencode-agent-rankings-opencode-zen-only.md # OpenCode Zen-only rankings (April 24)
│ ├── oh-my-opencode-agent-rankings-2026-04-06.md # v2.0 rankings (historical, superseded)
│   ├── oh-my-opencode-reference.json             # Working config reference (v3.0)
│   ├── session-learnings-2026-04-04.md           # Session 1: Agent architecture insights
│   ├── session-learnings-2026-04-05.md           # Session 2: Exhaustive search methodology
│   ├── session-learnings-2026-04-06.md           # Session 3: Timeout configuration & system architecture
│   ├── session-learnings-2026-04-06-fallback-investigation.md  # Session 4: Fallback configuration
│   ├── session-learnings-2026-04-06-model-id-investigation.md  # Session 5: Model ID investigation
│   ├── session-learnings-2026-04-07.md           # Session 6: Model config updates & visual engineering
│   ├── session-learnings-2026-04-07-model-configuration-fix.md # Session 7: Model config verification
│   ├── session-learnings-2026-04-08.md           # Session 8: OMO-Team skill creation
│   ├── session-learnings-2026-04-13.md           # Session 9: Extended rankings & dual system architecture
│   ├── session-learnings-2026-04-13-documentation.md           # Session 10: Model testing & verification
│   ├── extended-rankings-visual-engineering.md   # Extended ranking (historical, pre-v3.0)
│   ├── extended-rankings-artistry.md             # Extended ranking (historical, pre-v3.0)
│   └── extended-rankings-writing.md              # Extended ranking (historical, pre-v3.0)
├── .omx/
│ └── model-rankings-report.md # OpenCode Zen agent rankings (25 agents)
├── oh-my-opencode-oacp.json # OpenAI cost-performance config (CPI-based)
└── README.md # This file
```

## Key Documents

### [Oh-My-OpenCode Agent Rankings v3.0](docs/oh-my-opencode-agent-rankings.md) (Current)

Comprehensive model rankings using only NVIDIA Build, OpenCode Zen, and OpenAI providers.

**Key Findings:**
- **nvidia/z-ai/glm-5.1** is #1 on SWE-Bench Pro (58.4%), released April 18, 2026
- **nvidia/z-ai/glm5** is DEPRECATED — migrate to `nvidia/z-ai/glm-5.1`
- Only 3 providers allowed: NVIDIA Build, OpenCode Zen, OpenAI
- `google/gemini-3.1-flash-lite-preview` replaced with `opencode/gemini-3-flash`
- momus agent added back to active config

### [Oh-My-OpenCode Agent Rankings — All OpenRouter Providers](docs/oh-my-opencode-agent-rankings-all-providers.md) (April 24, 2026)

Comprehensive model rankings across ALL 353 OpenRouter models (294 ranked after filtering). Two tables per agent/category: performance score + cost/performance ratio.

**Key Findings:**
- **z-ai/glm-5.1** leads performance across reasoning-heavy agents (sisyphus 94.5, oracle 94.7)
- **openai/gpt-5.4-pro** ranks #2 for reasoning (92.0-92.4) but at 30× the cost
- **qwen/qwen3-coder-next** tops coding agents (hephaestus 90.7) at $0.15/$0.80
- **nvidia/deepseek-ai/deepseek-v4-flash** now leads refreshed speed-heavy categories, with **openai/gpt-5.4-nano** still the best OpenAI value option
- **mistralai/mistral-nemo** offers best cost/performance across all categories ($0.01/$0.03)

### [Oh-My-OpenCode Agent Rankings — OpenAI Only](docs/oh-my-opencode-agent-rankings-openai-only.md) (April 24, 2026)

OpenAI provider-specific rankings with calculated numeric performance indicators per agent/category. Covers gpt-5.4-pro, gpt-5.4, gpt-5.4-mini, gpt-5.4-nano, o3, and o4-mini.

**Key Findings:**
- **gpt-5.4-pro** dominates reasoning-heavy agents (oracle 93, metis 93, prometheus 92)
- **gpt-5.4** remains the best OpenAI execution/vision model, while **gpt-5.4-nano** now leads refreshed librarian and writing value rankings
- **gpt-5.4-nano** is the best OpenAI speed-heavy/value option across the refreshed tables
- **o3** and **o4-mini** are outperformed by the GPT-5.4 family at similar or lower cost

### [Oh-My-OpenCode Agent Rankings — OpenAI Cost-Performance](docs/oh-my-opencode-agent-rankings-openai-cost-performance.md) (April 27, 2026)

OpenAI CPI rankings — top 10 models per agent/category ranked by value per dollar. Companion to the performance-only doc.

**Key Findings:**
- **gpt-5.4** is the cost-performance champion (8/11 agents, 6/8 categories) — 92.8% GPQA at 1/12th pro price
- **gpt-5-nano** ($0.05/$0.40) dominates speed/quick/writing categories
- **gpt-4.1-nano** wins writing CPI (1M context at $0.10/$0.40)
- **gpt-5.4-pro** and **gpt-5.5-pro** never appear in CPI top-10 — 12x+ cost for ~2x performance
- Config: [oh-my-opencode-oacp.json](oh-my-opencode-oacp.json) — CPI-based oh-my-opencode config (OpenAI-only)

### [Oh-My-OpenCode Agent Rankings v2.0](docs/oh-my-opencode-agent-rankings-2026-04-06.md) (Historical)

Superseded by v3.0. Contains OpenRouter model references and pre-GLM-5.1 rankings. Retained for historical reference only.

## Quick Reference: Best Model per Agent (v3.0)

| Agent | Best Model | Provider | Score |
|-------|-----------|----------|-------|
| sisyphus | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| hephaestus | `openai/gpt-5.4` | OpenAI | 98 |
| oracle | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| explore | `nvidia/deepseek-ai/deepseek-v4-flash` | NVIDIA Build | 80.2 |
| prometheus | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| metis | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| momus | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 |
| librarian | `nvidia/deepseek-ai/deepseek-v4-flash` | NVIDIA Build | 80.2 |
| multimodal-looker | `nvidia/qwen/qwen3.5-397b-a17b` | NVIDIA Build | 99 |
| atlas | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 98 |
| sisyphus-junior | `nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Build | 99 |

## Quick Reference: Best Model per Category (v3.0)

| Category | Best Model | Provider | Score | Use Case |
|----------|-----------|----------|-------|----------|
| visual-engineering | `nvidia/qwen/qwen3.5-397b-a17b` | NVIDIA Build | 99 | Frontend, UI/UX, design |
| ultrabrain | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 | Hard logic-heavy tasks |
| deep | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | NVIDIA Build | 99 | Autonomous problem-solving |
| artistry | `nvidia/mistral-ai/mistral-small-4-119b-2603` | NVIDIA Build | 98 | Creative solutions |
| quick | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | 93.5 | Trivial tasks, typos |
| unspecified-low | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | NVIDIA Build | 93.5 | Low effort tasks |
| unspecified-high | `nvidia/z-ai/glm-5.1` | NVIDIA Build | 99 | High effort tasks |
| writing | `nvidia/deepseek-ai/deepseek-v4-pro` | NVIDIA Build | 88.9 | Documentation, prose |

## Quick Reference: Best OpenAI Model per Agent (OpenAI-Only Rankings)

| Agent | Best OpenAI Model | Score | 2nd Choice | Score |
|-------|------------------|-------|------------|-------|
| sisyphus | `openai/gpt-5.4-pro` | 91 | `openai/gpt-5.4` | 87 |
| hephaestus | `openai/gpt-5.4` | 90 | `openai/gpt-5.4-pro` | 88 |
| oracle | `openai/gpt-5.4-pro` | 93 | `openai/gpt-5.4` | 86 |
| explore | `openai/gpt-5.4-nano` | 76.8 | `openai/gpt-5.4-mini` | 65.1 |
| prometheus | `openai/gpt-5.4-pro` | 92 | `openai/gpt-5.4` | 87 |
| metis | `openai/gpt-5.4-pro` | 93 | `openai/gpt-5.4` | 86 |
| momus | `openai/gpt-5.4-pro` | 92 | `openai/gpt-5.4` | 86 |
| librarian | `openai/gpt-5.4-nano` | 76.8 | `openai/gpt-5.4-mini` | 65.1 |
| multimodal-looker | `openai/gpt-5.4` | 85 | `openai/gpt-5.4-pro` | 83 |
| atlas | `openai/gpt-5.4-pro` | 90 | `openai/gpt-5.4` | 86 |
| sisyphus-junior | `openai/gpt-5.4-mini` | 82 | `openai/gpt-5.4-nano` | 78 |

## Model Providers

### NVIDIA Build (`nvidia/` prefix)
- GPU-optimized inference, 200+ models
- Free tier available for most models
- Specialized: reasoning, coding, vision, agentic
- Key models: glm-5.1, qwen3-coder-480b, step-3.5-flash, nemotron-3-super

### OpenCode Zen (`opencode/` prefix)
- Curated, tested models for coding agents
- Reliable routing, no rate limit issues
- Key models: gemini-3-flash, qwen3-coder, qwen3.6-plus

### OpenAI (`openai/` prefix)
- Frontier reasoning, large context windows
- Paid only ($0.20-$180 per 1M tokens)
- Key models: gpt-5.4, gpt-5.4-pro, o3, o4-mini

> Only NVIDIA Build, OpenCode Zen, and OpenAI models are used. No OpenRouter or direct Google models.

## Cost Optimization

| Task Type | Recommended Model | Cost | Context |
|-----------|------------------|------|---------|
| Quick/trivial | `nvidia/nvidia/nemotron-3-nano-30b-a3b` | $0.05/$0.20 | 1M |
| Search/research | `nvidia/deepseek-ai/deepseek-v4-flash` | FREE | 1M |
| Research/writing | `nvidia/deepseek-ai/deepseek-v4-pro` | FREE | 1M |
| Junior tasks | `nvidia/nvidia/nemotron-3-super-120b-a12b` | $0.10/$0.50 | 1M |
| Cost-effective reasoning | `openai/gpt-5.4-mini` | $0.75/$4.50 | 400K |

## Migration Guide (v2.0 → v3.0)

| Old Model | New Model | Reason |
|-----------|-----------|--------|
| `nvidia/z-ai/glm5` | `nvidia/z-ai/glm-5.1` | Deprecated April 20, 2026 |
| `google/gemini-3.1-flash-lite-preview` | `opencode/gemini-3-flash` | Provider constraint |
| `openai/gpt-5.3-codex` | `nvidia/qwen/qwen3-coder-480b-a35b-instruct` | Being retired June 5, 2026 |
| All OpenRouter models | NVIDIA Build equivalents | Provider constraint |

## Methodology

Rankings are based on SWE-Bench Pro performance, reasoning capability, context window, cost, and agentic suitability. See [v3.0 rankings doc](docs/oh-my-opencode-agent-rankings.md) for full methodology.

## Related Documentation

- [Global Config](~/.config/opencode/oh-my-opencode.json)
- [v3.0 Rankings](docs/oh-my-opencode-agent-rankings.md)
- [OpenAI-Only Rankings](docs/oh-my-opencode-agent-rankings-openai-only.md)
- [OpenAI Cost-Performance Rankings](docs/oh-my-opencode-agent-rankings-openai-cost-performance.md)
- [OpenAI CPI Config](oh-my-opencode-oacp.json)
- [Extended Librarian + Writing Rankings](docs/extended-rankings-librarian-writing-nvidia-openai.md)
- [NVIDIA Build Models](https://build.nvidia.com/models)
- [OpenAI Models](https://developers.openai.com/api/docs/models/all)

## Last Updated

April 27, 2026
