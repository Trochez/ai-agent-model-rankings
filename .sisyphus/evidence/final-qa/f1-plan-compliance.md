# F1: Plan Compliance Audit

## Must Have Items

### 1. provider-first v1 blocking of `openai/*`
- **Check**: Look for policy engine that blocks based on provider being openai.
- **Evidence**: 
  - `src/shared/model-policy.ts`: `evaluateModelPolicy` function checks `providerID === "openai"`.
  - `src/shared/model-policy.test.ts`: tests show denial for `openai/*` models.
  - `task-3-deny.txt`: shows OpenAI provider denied with stable error code.
- **Status**: PASS

### 2. early filtering + prompt-time enforcement
- **Check**: 
  - Early filtering: model resolution pipeline calls `evaluateModelPolicy` to filter candidates.
  - Prompt-time enforcement: `assertPromptModelAllowed` called before each prompt send.
- **Evidence**:
  - Early filtering: `src/shared/model-resolution-pipeline.ts` lines 225-230 (isBlocked check).
  - Prompt-time: `src/model-policy-prompt-guard.ts` `assertPromptModelAllowed` used in `src/tools/call-omo-agent/sync-executor.ts` and `src/features/background-agent/spawner.ts`.
  - `task-4-direct-block.txt` and `task-4-perimeter-matrix.txt` show prompt-time blocking.
- **Status**: PASS

### 3. restored-session and retry/fallback revalidation
- **Check**: 
  - Restored session: model cache cleared on restore, revalidated before next send.
  - Retry/fallback: fallback lists prune blocked OpenAI models; bootstrap derivation skips blocked.
- **Evidence**:
  - Restored session: `src/plugin/chat-message.ts` clears model cache on restore; `src/hooks/runtime-fallback/fallback-state.ts` revalidates before retry.
  - `task-6-restore.txt` shows restored session blocked.
  - `task-6-retry.txt` shows retry skips OpenAI fallback.
- **Status**: PASS

### 4. delegate/subagent/background/tmux-child coverage
- **Check**: 
  - Delegate/subagent: `src/tools/delegate-task/subagent-resolver.ts` calls `evaluateModelPolicy`.
  - Background: `src/features/background-agent/spawner.ts` calls `assertPromptModelAllowed` in `startTask` and `resumeTask`.
  - Tmux-child: reload-before-next-prompt via `src/plugin/chat-message.ts` hook `openaiBlockStatus` and session hook.
- **Evidence**:
  - `task-7-delegate.txt` shows delegated agent blocked.
  - `task-7-tmux-reload.txt` shows tmux child reloads before next prompt.
  - `task-8-active-session.txt` shows active session respects toggle change.
- **Status**: PASS

### 5. global-overrides-agent precedence
- **Check**: Global block overrides agent-level `allow_non_gpt_model`.
- **Evidence**:
  - `src/shared/model-policy.ts`: `evaluateModelPolicy` only checks global policy and normalized provider/model; agent context is ignored for OpenAI block.
  - `task-3-precedence.txt`: shows global precedence over agent field.
- **Status**: PASS

## Must NOT Have Items

### 1. No Bun dist-cache-only production patch
- **Check**: Ensure we did not modify `~/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js`.
- **Evidence**: 
  - All changes are in `/home/trocha/projects/opencode/oh-my-openagent/` (canonical source).
  - `task-1-source-checkout.txt` confirms the editable checkout path.
- **Status**: PASS

### 2. No reliance on `no-hephaestus-non-gpt` as global enforcement
- **Check**: Ensure we did not use or require the `no-hephaestus-non-gpt` hook for global block.
- **Evidence**: 
  - No references to `no-hephaestus-non-gpt` in our changes.
  - The policy engine is independent of any agent-specific hooks.
- **Status**: PASS

### 3. No silent bypass via overrides, hidden fallback chains, or cached session state
- **Check**: 
  - Overrides: explicit OpenAI override is stripped in model resolution pipeline.
  - Hidden fallback chains: fallback lists and bootstrap derivation prune blocked models.
  - Cached session state: restored session model cache cleared and revalidated.
- **Evidence**:
  - `task-5-override.txt` shows explicit override rejected.
  - `task-6-retry.txt` and `task-6-restore.txt` show fallback and session state sanitization.
- **Status**: PASS

### 4. No ambiguous child-propagation rule; v1 is reload-before-next-prompt
- **Check**: Ensure tmux-child propagation is implemented as reload-before-next-prompt, not force-respawn.
- **Evidence**:
  - `src/plugin/chat-message.ts` wiring of `openaiBlockStatus` hook triggers on config change.
  - `src/features/background-agent/spawner.ts` `resumeTask` calls `assertPromptModelAllowed` before each prompt send (reload-before-next-prompt).
  - `task-7-tmux-reload.txt` shows child reloads policy and blocks without respawn.
- **Status**: PASS

## Summary
All Must Have items are present and all Must NOT Have items are absent.

**Overall Result: PASS**