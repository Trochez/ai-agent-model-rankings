# Worker 9 — T9 regression/proof result

Status: complete

Summary:
- Finalized focused T9 regression/proof coverage for the global provider-first OpenAI hard block.
- Kept scope at openai/* only.
- Fixed two incidental repo issues needed for verification (`background-executor.test.ts` module path/test shape and `openai-hard-block-toggle.ts` import), plus the `openaiBlockStatus` hook call typo in `chat-message.ts`.

Verification:
- Targeted regression suite: 67 pass / 0 fail
- `bun run typecheck`: pass
- `bun run build`: pass

Evidence:
- /home/trocha/projects/explorer/.sisyphus/evidence/task-9-test-matrix.txt
- /home/trocha/projects/explorer/.sisyphus/evidence/task-9-openai-proof.txt

Coverage delivered:
- direct
- override
- retry/fallback
- restored-session
- delegate/background
- child/tmux reload-before-next-prompt
- observability/perimeter proof for MODEL_POLICY_BLOCKED_OPENAI
