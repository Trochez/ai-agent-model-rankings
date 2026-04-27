# T1 Evidence: Plugin-controlled prompt-send perimeter inventory

## Canonical patch target
- Repo: `/home/trocha/projects/opencode/oh-my-openagent`
- Origin: `https://github.com/code-yeongyu/oh-my-openagent.git`
- Commit: `a941774e994c5a04d14bc238d5461e17f90ab6ed`

## Source mapping for bundle anchors

| Bundle anchor | Source path | Source line |
|---|---|---:|
| `AGENT_MODEL_REQUIREMENTS` | `src/shared/model-requirements.ts` | 20 |
| `resolveModelPipeline()` | `src/shared/model-resolution-pipeline.ts` | 40 |
| `applyModelResolution()` | `src/agents/builtin-agents/model-resolution.ts` | 4 |
| `createBuiltinAgents()` | `src/agents/builtin-agents.ts` | 61 |
| `prepareFallback()` | `src/hooks/runtime-fallback/fallback-state.ts` | 39 |
| `resolveFallbackBootstrapModel()` | `src/hooks/runtime-fallback/fallback-bootstrap-model.ts` | 14 |
| `createCallOmoAgent()` | `src/tools/call-omo-agent/tools.ts` | 97 |
| `resolveSubagentExecution()` | `src/tools/delegate-task/subagent-resolver.ts` | 29 |
| `createNoHephaestusNonGptHook()` | `src/hooks/no-hephaestus-non-gpt/hook.ts` | 37 |

## Plugin-controlled prompt / promptAsync send perimeter

These are the prompt-send sites that are reachable from plugin-controlled flows and therefore must be covered by the hard-block design.

| Path | Line | Function / context | Classification | Model path context |
|---|---|---:|---|---|
| `src/plugin/event.ts` | 292-310 | `autoContinueAfterFallback()` | plugin-controlled | re-enters active session after fallback/continue handling |
| `src/hooks/runtime-fallback/auto-retry.ts` | 140 | auto-retry dispatch | plugin-controlled | retry path after fallback model selection |
| `src/features/background-agent/manager.ts` | 576-593 | background launch via `promptWithModelSuggestionRetry(...)` | plugin-controlled | background task initial spawn with agent/model payload |
| `src/features/background-agent/manager.ts` | 866-884 | resumed background task promptAsync | plugin-controlled | resumed task send uses persisted task model |
| `src/features/background-agent/manager.ts` | 1702, 1833-1843 | `notifyParentSession()` | plugin-controlled | parent-session notification send with inherited agent/model |
| `src/features/background-agent/spawner.ts` | 219, 301-315 | `resumeTask()` | plugin-controlled | resumed background task send + fallback-agent retry |
| `src/tools/call-omo-agent/sync-executor.ts` | 56, 105-119 | `executeSync()` | plugin-controlled | sync delegated subagent send |
| `src/hooks/ralph-loop/continuation-prompt-injector.ts` | 78 | continuation injection | plugin-controlled | resumed self-loop send |
| `src/hooks/todo-continuation-enforcer/continuation-injection.ts` | 187 | continuation enforcement | plugin-controlled | resumed todo-continuation send |
| `src/hooks/session-recovery/resume.ts` | 35 | session recovery resume | plugin-controlled | restored-session next prompt |
| `src/hooks/session-recovery/recover-tool-result-missing.ts` | 102 | missing-tool-result recovery | plugin-controlled | replay/recovery send |
| `src/hooks/atlas/boulder-continuation-injector.ts` | 84 | Boulder continuation | plugin-controlled | continuation send |
| `src/hooks/compaction-context-injector/recovery.ts` | 84 | compaction recovery | plugin-controlled | recovery send |
| `src/plugin/unstable-agent-babysitter.ts` | 28-31 | babysitter prompt resend | plugin-controlled | recovery/resend path |
| `src/hooks/unstable-agent-babysitter/unstable-agent-babysitter-hook.ts` | 216 | unstable-agent retry | plugin-controlled | hook-driven resend |
| `src/hooks/anthropic-context-window-limit-recovery/aggressive-truncation-strategy.ts` | 66 | truncation recovery | plugin-controlled | retry send after recovery |

## Supporting model-resolution / delegate boundaries feeding the perimeter

These are not final send sites by themselves, but they feed model choice into the prompt-send perimeter and therefore must participate in the policy design.

- `src/shared/model-resolution-pipeline.ts:40` — shared model resolution path
- `src/agents/builtin-agents/model-resolution.ts:4` — builtin agent wrapper over shared resolution
- `src/agents/builtin-agents.ts:61` — builtin registration path
- `src/hooks/runtime-fallback/fallback-state.ts:39` — runtime fallback state preparation
- `src/hooks/runtime-fallback/fallback-bootstrap-model.ts:14` — bootstrap model derivation
- `src/tools/delegate-task/subagent-resolver.ts:29` — delegated subagent resolution
- `src/tools/call-omo-agent/tools.ts:97` — delegated tool entrypoint

## Core-unreachable / non-plugin-controlled findings

| Path | Line | Classification | Blast radius |
|---|---|---|---|
| `src/cli/run/runner.ts` | 126 | core / CLI runner path, not plugin-controlled | medium — if the goal is a plugin-only hard block, this path is outside the guaranteed boundary and must be documented as upstream/core territory |
| `src/shared/model-suggestion-retry.ts` | 89-177 | shared utility, not a standalone perimeter site | medium — safe only if every caller reaching it is policy-guarded before invocation |

## Inventory conclusion

- Canonical editable checkout exists and is usable.
- The plugin-controlled perimeter is concentrated in plugin event handling, recovery hooks, runtime fallback, background-agent resumption/notification, and delegated-agent execution.
- v1 scope remains provider-first `openai/*` blocking.
- Any hard-block guarantee must treat the plugin-controlled prompt-send sites above as the authoritative perimeter.
