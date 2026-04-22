# Worker 3 — T3 result

## Patch target
- `/home/trocha/projects/opencode/oh-my-openagent`

## Implemented
- Added `src/shared/model-policy.ts`
- Exported policy engine via `src/shared/index.ts`
- Added `src/shared/model-policy.test.ts`

## evaluateModelPolicy()
- Normalizes provider/model IDs to lowercase
- Strips duplicated provider prefix from model IDs like `OpenAI/GPT-5.4`
- Infers `openai` for bare OpenAI aliases like `gpt-5.4`
- Preserves nested non-provider model paths like `z-ai/glm-5.1`
- Returns stable deny contract with `MODEL_POLICY_BLOCKED_OPENAI`
- Global OpenAI policy takes precedence over `allow_non_gpt_model`

## Verification
- LSP diagnostics clean:
  - `src/shared/model-policy.ts`
  - `src/shared/model-policy.test.ts`
  - `src/shared/index.ts`
- Unit tests passed: `bun test src/shared/model-policy.test.ts`
- Build passed: `bun run build`

## Evidence files
- `.sisyphus/evidence/task-3-deny.txt`
- `.sisyphus/evidence/task-3-precedence.txt`
