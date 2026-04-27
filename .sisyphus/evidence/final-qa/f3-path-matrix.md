# F3: Real QA Execution — Full Path Matrix Verification

## Scenario: Full blocked-path matrix passes

All paths block with the stable policy error before outbound OpenAI send.

### Evidence Summary

- **Fresh session**: Blocked at prompt send (see `task-4-direct-block.txt` and `task-4-perimeter-matrix.txt`).
- **Restored session**: Blocked on next send after restore (see `task-6-restore.txt`).
- **Retry/fallback**: OpenAI fallback candidate pruned and never sent (see `task-6-retry.txt`).
- **Delegated/background subagent**: Blocked with stable error (see `task-7-delegate.txt`).
- **Tmux-child flow**: Child reloads policy and blocks OpenAI on next send without respawn (see `task-7-tmux-reload.txt`).
- **Explicit override**: OpenAI override rejected and never sent (see `task-5-override.txt`).
- **Toggle-on control path**: Allowed-mode flows resume normally after re-enable (see `task-8-active-session.txt` and `task-8-toggle.txt`).

All evidence files confirm that the global OpenAI hard block is effective across all plugin-controlled paths.

**Result: PASS**