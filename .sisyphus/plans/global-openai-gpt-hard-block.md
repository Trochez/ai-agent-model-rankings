# Global OpenAI Provider Hard Block for OpenCode TUI

## TL;DR

> **Quick Summary**: Implement a global provider-first model policy that blocks `openai/*` everywhere in plugin-controlled OpenCode flows. Use one shared policy engine for early filtering and fallback sanitization, but treat **prompt-time validation immediately before each plugin-controlled `prompt` / `promptAsync` send** as the authoritative hard-block boundary.
>
> **Deliverables**:
> - global persisted OpenAI block toggle
> - shared `evaluateModelPolicy()` engine with normalized IDs and stable error code
> - prompt-send enforcement on all inventoried plugin-controlled send paths
> - fallback/delegate/restored-session/tmux-child coverage
> - TUI toggle/status surface and regression proof
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES — 3 waves
> **Critical Path**: T1 → T2/T3 → T4 → T6/T7 → T8 → T9 → Final verification

---

## Context

### Original Request
Create a concrete implementation plan for a mechanism that enables/disables OpenAI model usage in all opencode TUI sessions, with an easy interface to toggle GPT usage and a HARD BLOCK preventing any GPT/OpenAI use in delegations or subprocesses when disabled.

### Verified Evidence
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:18239-18401` — `AGENT_MODEL_REQUIREMENTS` contains hardcoded provider/model requirements and OpenAI-related fallback entries.
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:19169-19334` — `resolveModelPipeline()` is the primary shared model resolution path.
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:140138-140145` — `applyModelResolution()` wraps builtin-agent model resolution.
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:140401-140490` — `createBuiltinAgents()` registers builtin agents from resolved models.
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:98482-98508` — `prepareFallback()` advances runtime fallback candidates.
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:98962-99004` — `resolveFallbackBootstrapModel()` can derive retry/bootstrap models later.
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:119223-119272` — `createCallOmoAgent()` builds delegated-agent fallback behavior.
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:121550-121678` — `resolveSubagentExecution()` re-resolves models for delegate/subagent flows.
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:88318-88339` — `createNoHephaestusNonGptHook()` is agent-specific and insufficient as a global boundary.
- `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/package.json` — package metadata confirms the locally installed runtime is `oh-my-openagent` v3.15.1.

### Workspace Reality Check
- `/home/trocha/projects/explorer` is a research repo, not the editable OpenCode source checkout.
- `/home/trocha/projects/opencode/` exists but is empty and not a usable patch target.
- No editable local clone of `https://github.com/code-yeongyu/oh-my-openagent.git` is present on this machine at planning time.
- Therefore the executor must first obtain or be given a canonical editable source checkout path before making implementation changes.

### Consensus Outcome
- **Architect review**: added normalized-ID policy engine, stable error contract, and explicit runtime/cache invalidation story.
- **Critic review**: tightened v1 semantics to provider-first `openai/*` blocking with explicit acceptance criteria by execution path.
- **Final architect/critic loop**: resolved the last blockers by:
  - committing to **prompt-time validation** as the real plugin-layer hard block,
  - committing to **reload-before-next-prompt** for tmux/child propagation,
  - requiring a **perimeter inventory** of every plugin-controlled prompt send path.

---

## RALPLAN-DR Summary

### Principles
1. Fail closed at the last controllable boundary.
2. One shared policy engine, reused at multiple boundaries.
3. Provider-first semantics for v1.
4. UI is control plane only.
5. Cached/resumed work must revalidate before next prompt send.

### Decision Drivers
- Guarantee hard-block semantics across fresh, retried, delegated, background, restored, and tmux-child flows.
- Minimize policy ambiguity.
- Keep v1 small enough to test exhaustively.

### Viable Options
- **A. UI-only toggle + warning hook**
  - Pros: cheap
  - Cons: cosmetic, bypassable
- **B. Shared `evaluateModelPolicy()` engine + early filtering + prompt-time enforcement + fallback sanitization** **(chosen)**
  - Pros: strongest guarantee with good UX
  - Cons: touches multiple boundaries and requires careful perimeter inventory
- **C. Prompt-time-only enforcement**
  - Pros: simpler security story than A
  - Cons: poorer UX, noisier fallback behavior, less predictable operator experience

### Why B Won
It preserves the hard security boundary of C while also pruning blocked candidates earlier so users see cleaner failures and fewer noisy fallback attempts.

---

## ADR

### Decision
Implement a **global provider-first OpenAI block** with one shared `evaluateModelPolicy()` engine and two uses:
1. **Early filtering** in resolution and fallback construction for UX/candidate hygiene.
2. **Prompt-time validation** immediately before every plugin-controlled `prompt` / `promptAsync` send as the authoritative hard block.

### Drivers
- Hardcoded fallback chains already contain OpenAI entries.
- Startup-only filtering is not enough because retry, delegate, restored-session, and child-process flows can re-enter model selection later.
- The plugin architecture’s real control point is prompt submission, not a hypothetical core middleware seam.

### Alternatives Considered
- UI-only hook/warning approach: rejected as cosmetic.
- Prompt-time-only enforcement: viable but inferior UX.
- Provider-cache manipulation only: brittle and incomplete.

### Consequences
- Multiple modules must call the same policy engine.
- Toggle changes must trigger reread/revalidation before the next prompt send.
- Global policy overrides per-agent relaxations such as `allow_non_gpt_model`.
- Any unreachable core-only fallback path discovered during implementation must be explicitly measured and tracked as an upstream follow-up.

### Follow-Ups
- Decide whether non-OpenAI GPT aliases justify a v2 family-level block.
- If any core-only fallback bypass exists, open/track an upstream change request for core-level enforcement.

---

## Work Objectives

### Core Objective
Deliver a production-grade global OpenAI hard-block mechanism for OpenCode TUI that is easy to toggle yet impossible to bypass within plugin-controlled paths through builtin agent selection, retry/fallback, delegated agents, background tasks, restored sessions, and tmux child flows.

### Concrete Deliverables
- global persisted OpenAI policy config
- shared normalized policy evaluator and stable error contract
- prompt-send enforcement on all inventoried plugin-controlled send paths
- sanitized fallback/delegate/bootstrap handling
- toggle UI/status surface
- regression tests and proof artifact

### Definition of Done
- [ ] With policy disabled, no inventoried plugin-controlled path can send `openai/*`.
- [ ] Covered paths emit a stable blocked error code before prompt send.
- [ ] Existing plugin-visible fallback lists containing `openai/*` never result in outbound OpenAI prompt sends.
- [ ] Toggle state is visible in UI and respected by next prompt send in active/restored/tmux-child work.
- [ ] A canonical editable source checkout path is recorded before any code changes begin.

### Must Have
- provider-first v1 blocking of `openai/*`
- early filtering + prompt-time enforcement
- restored-session and retry/fallback revalidation
- delegate/subagent/background/tmux-child coverage
- global-overrides-agent precedence

### Must NOT Have
- No Bun dist-cache-only production patch
- No reliance on `no-hephaestus-non-gpt` as global enforcement
- No silent bypass via overrides, hidden fallback chains, or cached session state
- No ambiguous child-propagation rule; v1 is reload-before-next-prompt

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — all checks must be agent-executable.

### Test Decision
- **Infrastructure exists**: confirm in T1 against the actual source repo
- **Automated tests**: YES (tests-after)
- **Framework**: repo-native framework discovered in T1

### QA Policy
- **Unit**: normalization, allow/deny logic, precedence, fallback sanitization
- **Integration**: builtin registration, delegate/subagent resolution, runtime fallback, restored-session revalidation, tmux-child reload-before-next-prompt behavior
- **E2E**: toggle off then attempt direct, delegated, retried, restored, and child-process OpenAI usage
- **Observability**: verify stable error code + logs/toasts/evidence
- **Precondition**: T1 must record the canonical editable checkout path plus repo-native commands before any implementation or final verification step runs

Evidence location: `.sisyphus/evidence/task-{N}-{scenario}.{ext}`

---

## Execution Strategy

### Parallel Execution Waves

```text
Wave 1 (foundation)
├── T1: Inventory source repo + plugin-controlled send perimeter
├── T2: Add global config schema + persistence
└── T3: Implement shared evaluateModelPolicy() engine

Wave 2 (hard enforcement)
├── T4: Add prompt-time enforcement to every inventoried send path
├── T5: Apply early filtering to builtin/initial resolution
├── T6: Sanitize runtime fallback/bootstrap + restored-session revalidation
└── T7: Apply delegate/background/tmux-child propagation + precedence rules

Wave 3 (operator surface + proof)
├── T8: Add TUI/settings/slash-command toggle + visible status
└── T9: Add regression coverage + observability proof

Wave FINAL
├── F1: Plan compliance audit
├── F2: Code quality review
├── F3: Real QA execution
└── F4: Scope fidelity check
```

### Dependency Matrix
- **T1**: blocked by none → blocks T2-T9
- **T2**: blocked by T1 → blocks T4-T9
- **T3**: blocked by T1 → blocks T4-T9
- **T4**: blocked by T1,T2,T3 → blocks T5-T9
- **T5**: blocked by T1,T2,T3,T4 → blocks T8,T9
- **T6**: blocked by T1,T2,T3,T4 → blocks T8,T9
- **T7**: blocked by T1,T2,T3,T4 → blocks T8,T9
- **T8**: blocked by T2,T5,T6,T7 → blocks T9, F1-F4
- **T9**: blocked by T4-T8 → blocks F1-F4

### Agent Dispatch Summary
- **Wave 1**: T1 → `deep`; T2 → `quick`; T3 → `unspecified-high`
- **Wave 2**: T4 → `deep`; T5 → `unspecified-high`; T6 → `deep`; T7 → `deep`
- **Wave 3**: T8 → `visual-engineering`; T9 → `unspecified-high`
- **Final**: F1 → `oracle`; F2 → `unspecified-high`; F3 → `unspecified-high`; F4 → `deep`

---

## TODOs

- [ ] **T1. Inventory the canonical source repo and the plugin-controlled enforcement perimeter**

  **What to do**:
  - Identify or obtain the editable source checkout corresponding to the traced bundle.
  - If no editable checkout exists locally, clone or otherwise provision `https://github.com/code-yeongyu/oh-my-openagent.git` into a canonical working path before any code edits.
  - Produce a call-site inventory of every plugin-controlled prompt send path.
  - Classify any core-unreachable path and estimate its blast radius.
  - Freeze v1 semantics to provider-first `openai/*` blocking.

  **Must NOT do**:
  - Do not treat the Bun cache dist bundle as the final patch target.
  - Do not leave the enforcement perimeter undefined.
  - Do not begin implementation in this research repo.

  **Recommended Agent Profile**:
  - **Category**: `deep`
  - **Skills**: [`deepsearch`]

  **Parallelization**: can start immediately; blocks T2-T9.

  **References**:
  - `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:19169-19334` - shared model resolution path to map back into the canonical source checkout
  - `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:98482-98508` - runtime fallback path that must be represented in the source inventory
  - `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:119223-119272` - delegated-agent send path setup to trace into editable source modules
  - `/home/trocha/.bun/install/cache/oh-my-openagent@3.15.1@@@1/dist/index.js:121550-121678` - delegate/subagent model-finalization path to include in the perimeter map
  - `https://github.com/code-yeongyu/oh-my-openagent.git` - canonical upstream repository to provision locally if no editable checkout exists

  **Acceptance Criteria**:
  - [ ] Canonical source repo path recorded
  - [ ] If no editable checkout existed locally at start, a canonical editable checkout is provisioned and recorded
  - [ ] Plugin-controlled send perimeter documented with concrete call sites/module boundaries
  - [ ] Any core-unreachable path documented with blast radius estimate
  - [ ] v1 scope explicitly fixed to `openai/*` provider block

  **QA Scenarios**:
  ```text
  Scenario: Perimeter inventory complete
    Tool: Bash/Read/Grep in source repo
    Steps: enumerate all prompt/promptAsync send wrappers and related caller modules in the canonical editable checkout
    Expected Result: one inventory artifact listing all plugin-controlled send paths in the real patch target
    Evidence: .sisyphus/evidence/task-1-perimeter.md

  Scenario: Editable checkout established
    Tool: Bash/Read
    Steps: verify canonical source repo path exists, is writable, and corresponds to the upstream repository or approved internal mirror
    Expected Result: implementation work has a real patch target distinct from Bun cache and this research repo
    Evidence: .sisyphus/evidence/task-1-source-checkout.txt

  Scenario: Core-unreachable gap measured
    Tool: Bash/Read
    Steps: classify any unresolved core-only path
    Expected Result: measured blast radius documented or explicitly none
    Evidence: .sisyphus/evidence/task-1-core-gap.md
  ```

- [ ] **T2. Add global config schema and persistence for the OpenAI block toggle**

  **What to do**:
  - Add narrow v1 config fields for global OpenAI blocking.
  - Pick one consistent config pattern and document precedence.
  - Wire persistence/load so runtime code can read effective policy.

  **Must NOT do**:
  - Do not add a broad policy DSL in v1.

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: [`build-fix`]

  **Parallelization**: Wave 1 with T3; blocked by T1; blocks T4-T9.

  **Acceptance Criteria**:
  - [ ] Global toggle schema added
  - [ ] Invalid values rejected by validation
  - [ ] Runtime code can read effective OpenAI block state

  **QA Scenarios**:
  ```text
  Scenario: Toggle persists and loads
    Tool: Bash/Read
    Steps: set policy disabled in config; reload config path
    Expected Result: effective policy reports OpenAI blocked
    Evidence: .sisyphus/evidence/task-2-config-load.txt

  Scenario: Invalid config rejected
    Tool: Bash
    Steps: inject malformed policy shape; run validation/load command
    Expected Result: deterministic validation failure
    Evidence: .sisyphus/evidence/task-2-config-invalid.txt
  ```

- [ ] **T3. Implement shared `evaluateModelPolicy()` and stable error contract**

  **What to do**:
  - Add `evaluateModelPolicy(providerID, modelID, context)`.
  - Normalize IDs before policy checks.
  - Make it own precedence, including global override of agent-level relaxations.
  - Return stable error metadata, e.g. `MODEL_POLICY_BLOCKED_OPENAI`.

  **Must NOT do**:
  - Do not rely on raw string matching without normalization.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: [`build-fix`]

  **Parallelization**: Wave 1 with T2; blocked by T1; blocks T4-T9.

  **Acceptance Criteria**:
  - [ ] Engine returns allow/deny + code/message using normalized IDs
  - [ ] `openai/*` evaluates to deny when toggle is off
  - [ ] `allow_non_gpt_model` or similar per-agent fields never override global block

  **QA Scenarios**:
  ```text
  Scenario: OpenAI provider denied
    Tool: Bash unit test runner
    Steps: evaluate `openai/gpt-5.4` with policy off
    Expected Result: denied with `MODEL_POLICY_BLOCKED_OPENAI`
    Evidence: .sisyphus/evidence/task-3-deny.txt

  Scenario: Global precedence over agent field
    Tool: Bash unit test runner
    Steps: evaluate OpenAI model with agent config containing `allow_non_gpt_model: true`
    Expected Result: still denied by global policy
    Evidence: .sisyphus/evidence/task-3-precedence.txt
  ```

- [ ] **T4. Add prompt-time enforcement to every inventoried send path**

  **What to do**:
  - Insert `evaluateModelPolicy()` immediately before each inventoried plugin-controlled `prompt` / `promptAsync` send.
  - Treat this as the authoritative hard-block boundary.

  **Must NOT do**:
  - Do not assume early resolution filtering is sufficient.
  - Do not leave any inventoried send path unenforced.

  **Recommended Agent Profile**:
  - **Category**: `deep`
  - **Skills**: [`build-fix`]

  **Parallelization**: starts Wave 2; blocked by T1,T2,T3; blocks T5-T9.

  **Acceptance Criteria**:
  - [ ] Every inventoried plugin-controlled prompt send path validates via `evaluateModelPolicy()` before send
  - [ ] Blocked attempts terminate before request body submission
  - [ ] Stable error code surfaced to callers

  **QA Scenarios**:
  ```text
  Scenario: Direct prompt send blocked
    Tool: integration test / instrumented send wrapper
    Steps: attempt direct send with `openai/*` while toggle off
    Expected Result: zero outbound prompt send; stable error returned
    Evidence: .sisyphus/evidence/task-4-direct-block.txt

  Scenario: Perimeter completeness
    Tool: integration test
    Steps: execute each inventoried send path once under blocked policy
    Expected Result: all paths reject before send
    Evidence: .sisyphus/evidence/task-4-perimeter-matrix.txt
  ```

- [ ] **T5. Apply early filtering to builtin and initial model resolution**

  **What to do**:
  - Filter blocked candidates in `resolveModelPipeline`, builtin wrappers, and builtin registration.
  - Keep this as UX optimization and candidate hygiene.

  **Must NOT do**:
  - Do not silently substitute OpenAI from hardcoded fallback chains when disabled.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: [`build-fix`]

  **Parallelization**: Wave 2 with T6,T7; blocked by T1,T2,T3,T4; blocks T8,T9.

  **Acceptance Criteria**:
  - [ ] Resolution prunes blocked `openai/*` candidates before selection
  - [ ] Explicit per-agent OpenAI override no longer resolves successfully when blocked
  - [ ] No-cache startup still depends on T4 for final hard block

  **QA Scenarios**:
  ```text
  Scenario: Builtin registration prunes OpenAI
    Tool: integration test
    Steps: build builtin agents with policy off and OpenAI in fallback chains
    Expected Result: OpenAI candidates are pruned or unresolved early
    Evidence: .sisyphus/evidence/task-5-builtin.txt

  Scenario: Explicit override rejected
    Tool: integration test
    Steps: set agent override to `openai/gpt-5.4`; resolve model
    Expected Result: override is rejected and never sent
    Evidence: .sisyphus/evidence/task-5-override.txt
  ```

- [ ] **T6. Sanitize runtime fallback, bootstrap derivation, and restored-session state**

  **What to do**:
  - Filter fallback lists and bootstrap-derived models.
  - Revalidate/invalidate restored session model state, retry state, and cached fallback chains on next send.

  **Must NOT do**:
  - Do not let cached retry state keep an old OpenAI candidate alive.

  **Recommended Agent Profile**:
  - **Category**: `deep`
  - **Skills**: [`build-fix`]

  **Parallelization**: Wave 2 with T5,T7; blocked by T1,T2,T3,T4; blocks T8,T9.

  **Acceptance Criteria**:
  - [ ] Runtime fallback never sends `openai/*` when blocked
  - [ ] Restored sessions revalidate on next send
  - [ ] Toggle change invalidates cached candidate state before next send

  **QA Scenarios**:
  ```text
  Scenario: Retry skips OpenAI fallback
    Tool: integration test
    Steps: seed fallback list with allowed model then `openai/*`; force retry
    Expected Result: OpenAI entry is pruned/blocked and never sent
    Evidence: .sisyphus/evidence/task-6-retry.txt

  Scenario: Restored session blocked
    Tool: integration/e2e test
    Steps: restore session previously pointing at `openai/*`; send next message with toggle off
    Expected Result: immediate `MODEL_POLICY_BLOCKED_OPENAI` before send
    Evidence: .sisyphus/evidence/task-6-restore.txt
  ```

- [ ] **T7. Apply policy to delegate, background, and tmux-child paths**

  **What to do**:
  - Reuse the policy engine in delegate-task model resolution and fallback-chain construction.
  - Ensure child work rereads global policy before next prompt send.
  - Implement v1 tmux propagation as **reload-before-next-prompt**.

  **Must NOT do**:
  - Do not let child work rely on stale inherited model state without revalidation.
  - Do not substitute force-respawn as the default v1 behavior.

  **Recommended Agent Profile**:
  - **Category**: `deep`
  - **Skills**: [`build-fix`]

  **Parallelization**: Wave 2 with T5,T6; blocked by T1,T2,T3,T4; blocks T8,T9.

  **Acceptance Criteria**:
  - [ ] Delegated agents cannot send `openai/*`
  - [ ] Background tasks revalidate policy before retry send
  - [ ] Tmux child obeys reload-before-next-prompt after toggle change

  **QA Scenarios**:
  ```text
  Scenario: Delegated subagent blocked
    Tool: integration/e2e test
    Steps: toggle off; launch delegated agent with OpenAI override/fallback
    Expected Result: child resolution or send blocks with stable error
    Evidence: .sisyphus/evidence/task-7-delegate.txt

  Scenario: Tmux child reloads before next prompt
    Tool: tmux automation + integration test
    Steps: start child under allowed state; disable OpenAI; trigger next child prompt send
    Expected Result: child rereads policy and blocks OpenAI on next send without respawn
    Evidence: .sisyphus/evidence/task-7-tmux-reload.txt
  ```

- [ ] **T8. Add TUI/settings/slash-command toggle and visible policy status**

  **What to do**:
  - Add easy operator control to enable/disable OpenAI usage.
  - Surface clear status such as `OpenAI hard blocked`.

  **Must NOT do**:
  - Do not make the toggle the only enforcement layer.

  **Recommended Agent Profile**:
  - **Category**: `visual-engineering`
  - **Skills**: [`frontend-ui-ux`]

  **Parallelization**: Wave 3; blocked by T2,T5,T6,T7; blocks T9.

  **Acceptance Criteria**:
  - [ ] Operator can toggle OpenAI hard block on/off from intended UX surface
  - [ ] Status reflects effective policy state
  - [ ] Active session next send respects changed state

  **QA Scenarios**:
  ```text
  Scenario: Toggle off updates status
    Tool: Playwright or TUI automation
    Steps: disable OpenAI in settings; inspect visible status/banner
    Expected Result: status shows OpenAI hard blocked and persisted state updates
    Evidence: .sisyphus/evidence/task-8-toggle.png

  Scenario: Toggle change affects active session next send
    Tool: TUI automation
    Steps: start session under allowed state; disable OpenAI; trigger OpenAI-bound action
    Expected Result: next send blocks with stable error
    Evidence: .sisyphus/evidence/task-8-active-session.txt
  ```

- [ ] **T9. Add regression coverage, observability, and proof artifact**

  **What to do**:
  - Add the full verification matrix and block-reason telemetry.
  - Produce proof that existing plugin-visible fallback lists containing `openai/*` never send under disabled mode.

  **Must NOT do**:
  - Do not claim done without negative tests for each bypass class.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: [`ultraqa`]

  **Parallelization**: Wave 3 with T8; blocked by T4-T8; blocks final verification.

  **Acceptance Criteria**:
  - [ ] Unit, integration, and E2E coverage exists for every bypass class
  - [ ] Observability captures reason code and path context
  - [ ] Proof artifact shows zero outbound OpenAI prompt sends from plugin-visible fallback lists

  **QA Scenarios**:
  ```text
  Scenario: Verification matrix passes
    Tool: repo-native test commands from T1
    Steps: run targeted unit/integration/e2e suites
    Expected Result: all policy-block regression tests pass
    Evidence: .sisyphus/evidence/task-9-test-matrix.txt

  Scenario: Existing fallback list proof
    Tool: integration test / trace capture
    Steps: execute flows with plugin-visible fallback chains containing `openai/*` under disabled policy
    Expected Result: trace shows zero outbound OpenAI prompt sends
    Evidence: .sisyphus/evidence/task-9-openai-proof.txt
  ```

---

## Available Agent Types & Staffing Guidance

### Available Agent Types Roster
- `oracle` — architecture and hard-problem review
- `explore` — local code search / pattern mapping
- `librarian` — external docs / upstream repo research
- `metis` — pre-plan gap analysis
- `momus` — final plan review
- `deep` lane — cross-cutting runtime work
- `quick` lane — narrow config/schema edits
- `visual-engineering` lane — TUI/settings work

### Suggested Reasoning Levels by Lane
- Runtime enforcement / fallback / delegate flows: **high**
- Config/schema plumbing: **medium**
- Toggle/status UX: **medium**
- Final audit / proof validation: **high**

### Ralph Staffing Guidance
- Use `/start-work global-openai-gpt-hard-block` if one agent should execute sequentially through the critical path and preserve the enforcement model coherently.

### Team Staffing Guidance
- Lane A: T1-T3 (source mapping, config, policy engine)
- Lane B: T4-T6 (prompt-time enforcement + runtime fallback)
- Lane C: T7-T8 (delegate/background/tmux-child + UX)
- Lane D: T9 + verification evidence

### Team → Ralph Verification Path
After team lanes land changes, run one sequential Ralph-style verification sweep across T4-T9 to confirm no inventoried path can still send `openai/*`.

---

## Final Verification Wave

- [ ] **F1. Plan Compliance Audit** — `oracle`
  - Verify every must-have exists and every must-not-have is absent.
  - Confirm evidence files exist for T1-T9.

  **QA Scenarios**:
  ```text
  Scenario: Must-have / must-not-have audit executes cleanly
    Tool: Read + Grep + Bash
    Preconditions: Implementation branch contains all planned changes and `.sisyphus/evidence/task-*.{md,txt,png}` artifacts
    Steps:
      1. Read the `Must Have` and `Must NOT Have` sections from this plan.
      2. Search the changed codepaths and evidence directory for each required behavior and each forbidden pattern.
      3. Record pass/fail for every listed requirement in a single audit artifact.
    Expected Result: audit artifact shows every must-have present and every must-not-have absent
    Failure Indicators: any required behavior missing, any forbidden bypass pattern found, or any required evidence artifact absent
    Evidence: .sisyphus/evidence/final-qa/f1-plan-compliance.md

  Scenario: Evidence inventory complete
    Tool: Bash + Read
    Preconditions: T1-T9 marked complete by executor
    Steps:
      1. Enumerate `.sisyphus/evidence/` for `task-1-*` through `task-9-*` files.
      2. Compare found artifacts to the QA scenarios declared in T1-T9.
      3. Record missing or extra artifacts.
    Expected Result: all declared evidence files for T1-T9 exist and are readable
    Failure Indicators: missing task evidence, unreadable files, or mismatched artifact naming
    Evidence: .sisyphus/evidence/final-qa/f1-evidence-inventory.txt
  ```

- [ ] **F2. Code Quality Review** — `unspecified-high`
  - Run repo-native typecheck/lint/test commands identified in T1.
  - Check for raw prompt send calls added outside the policy validation perimeter.

  **QA Scenarios**:
  ```text
  Scenario: Native quality gates pass
    Tool: Bash
    Preconditions: T1 has recorded the canonical source repo path plus native lint/typecheck/test commands
    Steps:
      1. Run the repo-native typecheck command from T1 in the canonical source repo.
      2. Run the repo-native lint command from T1 in the canonical source repo.
      3. Run the repo-native targeted policy regression test command from T1.
      4. Save combined output.
    Expected Result: typecheck, lint, and targeted tests all exit 0
    Failure Indicators: non-zero exit code, new warnings promoted to failures, or regression tests failing
    Evidence: .sisyphus/evidence/final-qa/f2-quality-gates.txt

  Scenario: No unenforced raw prompt sends added
    Tool: Grep + Read
    Preconditions: Executor has landed enforcement changes
    Steps:
      1. Search the canonical source repo for newly added `prompt(` and `promptAsync(` call sites in touched files.
      2. Inspect each hit to confirm `evaluateModelPolicy()` runs immediately before send on every plugin-controlled path.
      3. Record any call site that bypasses the policy engine.
    Expected Result: every new or modified plugin-controlled prompt send path is policy-guarded
    Failure Indicators: any raw prompt send path without immediate policy validation
    Evidence: .sisyphus/evidence/final-qa/f2-send-perimeter.md
  ```

- [ ] **F3. Real QA Execution** — `unspecified-high`
  - Execute the path matrix: fresh, restored, retry, delegate, background, tmux child, override.
  - Save evidence under `.sisyphus/evidence/final-qa/`.

  **QA Scenarios**:
  ```text
  Scenario: Full blocked-path matrix passes
    Tool: Bash + integration/e2e runner + tmux automation where applicable
    Preconditions: Global OpenAI block is disabled in config; executor has seeded test fixtures for fresh, restored, retry, delegate, background, tmux-child, and explicit-override flows
    Steps:
      1. Run the fresh-session OpenAI-bound flow and capture the blocked error.
      2. Run restored-session flow pointing at `openai/gpt-5.4` and capture the blocked error before send.
      3. Run retry/fallback flow with an OpenAI fallback candidate and confirm it never sends.
      4. Run delegated/background subagent flow with OpenAI override/fallback and confirm it blocks.
      5. Run tmux-child flow: start child under allowed state, disable OpenAI, trigger next prompt send, confirm reload-before-next-prompt block.
      6. Save a matrix with each path, observed result, and evidence file.
    Expected Result: every path blocks with the stable policy error before outbound OpenAI send
    Failure Indicators: any outbound OpenAI request observed, any path missing the stable error, or any child flow requiring respawn to apply policy
    Evidence: .sisyphus/evidence/final-qa/f3-path-matrix.md

  Scenario: Toggle-on control path still works for allowed execution
    Tool: Bash + integration/e2e runner
    Preconditions: Same fixtures as above, but global OpenAI block toggled back on/allowed per planned UX semantics
    Steps:
      1. Re-enable OpenAI usage via the configured control path.
      2. Execute one direct OpenAI-bound flow and one delegated flow.
      3. Record whether allowed-mode behavior resumes normally.
    Expected Result: allowed-mode flows no longer emit `MODEL_POLICY_BLOCKED_OPENAI`
    Failure Indicators: policy remains sticky after re-enable or unrelated providers break
    Evidence: .sisyphus/evidence/final-qa/f3-allow-control.txt
  ```

- [ ] **F4. Scope Fidelity Check** — `deep`
  - Verify v1 remains provider-first and did not creep into unrelated provider-ranking or prompt work.

  **QA Scenarios**:
  ```text
  Scenario: Diff matches v1 scope only
    Tool: Bash + Read
    Preconditions: Implementation commits exist and git diff is available in the canonical source repo
    Steps:
      1. Read the v1 scope statements in this plan: provider-first `openai/*` block, no broad DSL, no unrelated provider-ranking changes.
      2. Inspect the implementation diff for all touched files.
      3. Classify each changed file as in-scope or out-of-scope.
      4. Record any change that affects unrelated provider ranking, prompt formatting, or non-OpenAI policy families.
    Expected Result: every changed file maps to a declared task and v1 scope boundary
    Failure Indicators: unaccounted file changes, non-OpenAI policy expansion, or unrelated prompt/system behavior edits
    Evidence: .sisyphus/evidence/final-qa/f4-scope-fidelity.md

  Scenario: Provider-first semantics preserved
    Tool: Read + Grep
    Preconditions: Policy engine implementation complete
    Steps:
      1. Inspect the policy engine and config schema.
      2. Confirm the deny rule is keyed to `openai/*` provider semantics for v1.
      3. Confirm no additional family-wide heuristics or ranking rewrites were added.
    Expected Result: implementation preserves the narrow provider-first contract defined in the plan
    Failure Indicators: family-level GPT alias blocking added in v1 or unrelated provider policy logic introduced
    Evidence: .sisyphus/evidence/final-qa/f4-provider-first.txt
  ```

---

## Commit Strategy

- **Commit 1**: `feat(model-policy): add global OpenAI block config and evaluator`
- **Commit 2**: `fix(runtime): enforce policy on prompt send and fallback paths`
- **Commit 3**: `feat(tui): add OpenAI block toggle and regression coverage`

---

## Success Criteria

### Verification Commands
Use the canonical editable source repo’s native commands discovered in T1. Minimum required command classes:

```bash
<repo-test-command>      # Expected: targeted policy regression suites pass
<repo-lint-command>      # Expected: no new lint errors in touched files
<repo-typecheck-command> # Expected: clean type/schema/runtime boundary changes
```

### Final Checklist
- [ ] No inventoried plugin-controlled path can send `openai/*` when the global block is off
- [ ] Fresh, restored, delegated, retried, background, and tmux-child flows all block consistently
- [ ] Stable error contract is returned for blocked attempts
- [ ] Toggle state is visible and respected on next prompt send
- [ ] Proof artifact demonstrates plugin-visible fallback lists containing OpenAI never send under disabled mode
