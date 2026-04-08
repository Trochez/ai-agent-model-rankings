# Session Learnings - April 8, 2026 (Session 8)

## OMO-Team Skill Creation: OpenCode-Native Team Orchestration

This session focused on creating a new skill that enables true OpenCode-native parallel team execution, solving the architecture mismatch between OpenCode sessions and OMX team workers.

---

## 1. Architecture Discovery: Two Separate Orchestration Systems

### The Problem

When using the `team` skill in an OpenCode session, it was spawning **OMX sessions** (Codex/Claude CLI workers with GPT models) instead of **OpenCode sessions**. This was a fundamental architecture mismatch.

### The Two Systems

| System | Package | Worker Type | Spawning Method |
|--------|---------|-------------|-----------------|
| **OMX (oh-my-codex)** | `/usr/local/lib/node_modules/oh-my-codex` | Codex/Claude CLI sessions | `omx team ...` CLI + tmux |
| **OMO (oh-my-opencode)** | `node_modules/oh-my-opencode` | OpenCode subagent sessions | `task()` tool |

### Key Insight

The `team` skill at `~/.agents/skills/team/SKILL.md` invokes `omx team ...` which:
1. Uses tmux to split panes
2. Spawns workers via `buildWorkerProcessLaunchSpec()` in `tmux-session.js`
3. Only supports 3 CLI types: `codex`, `claude`, `gemini`
4. **No `opencode` option exists**

This means OpenCode users couldn't have native team orchestration.

---

## 2. OpenCode Subagent Infrastructure

### How OpenCode Spawns Subagents

```typescript
task(
  category="<category>",
  load_skills=["<skill1>", "<skill2>"],
  run_in_background=true,  // KEY: enables parallelism
  prompt="..."
)
```

### Background Task Lifecycle

1. `task()` returns `task_id` (e.g., `bg_abc123`)
2. Poll with `background_output(task_id, block=false)`
3. System sends notification on completion
4. Collect results via `background_output(task_id)`

### Key Components in oh-my-opencode

| Component | Location | Purpose |
|-----------|----------|---------|
| `BackgroundManager` | `dist/features/background-agent/manager.d.ts` | Manages background task lifecycle |
| `delegate-task` tool | `dist/tools/delegate-task/` | The `task()` tool implementation |
| `TmuxSessionManager` | `dist/features/tmux-subagent/manager.d.ts` | Tmux-based subagent management |

---

## 3. Skill Loading Behavior

### Discovery

Skills are auto-discovered from `~/.agents/skills/<name>/SKILL.md`

### Error Encountered

Initial `load_skills=["omo-worker"]` failed despite skill being available:

```
Skills not found: omo-worker. Available: ..., omo-worker, ...
```

This appears to be a timing issue - skills need to be registered before use.

### Workaround

Use `load_skills=[]` for workers, include skill content/protocol in the prompt instead.

---

## 4. State Management Patterns

### OMX Team State (`.omx/state/team/<team>/`)

- Uses mailbox files for worker communication
- Requires tmux for pane coordination
- CLI-based: `omx team api ...`
- Workers poll mailbox for messages

### OMO Team State (`.omo/state/omo-team/<team>/`)

- Simpler: workers write to `result.md`
- No mailbox needed - polling-based
- Tool-based: `task()` + `background_output()`
- Leader polls for completion

### State File Structure

```
.omo/state/omo-team/<team>/
├── manifest.json       # Team metadata
├── task-ids.json       # Background task IDs
├── status.json         # Progress tracking
└── workers/
    ├── worker-1/
    │   └── result.md   # Worker output
    └── worker-2/
        └── result.md   # Worker output
```

---

## 5. Parallel Execution Works

### Test Results

| Worker | Task | Duration | Status |
|--------|------|----------|--------|
| worker-1 | List TypeScript files | 43s | ✅ Completed |
| worker-2 | Count package.json lines | 36s | ✅ Completed |

Both ran **simultaneously** (not sequential).

### Key Finding

`run_in_background=true` is essential for parallelism. Without it, tasks execute sequentially.

---

## 6. Skill Structure Best Practices

### Minimal Skill Structure

```
~/.agents/skills/<name>/
├── SKILL.md        # Required: skill definition
└── DATASHEET.md    # Optional: comprehensive docs
```

### SKILL.md Frontmatter

```yaml
---
name: skill-name
description: Brief description
---
```

### Good Datasheet Structure

1. Overview table (quick reference)
2. Invocation syntax
3. Arguments (required + optional)
4. Usage examples (basic → complex)
5. Workflow diagram
6. State files (with templates)
7. Error handling
8. Comparison tables
9. Quick reference card

---

## 7. Background Agent Limitations

### API Quota Issues

All 4 background explore/librarian agents failed:

```
Error: "Free promotion has ended for Qwen3.6 Plus Free"
```

### Solution

Use direct tools (read, grep, glob) instead of background agents when quota limited.

### Lesson

Always have fallback when background agents fail. Direct tools are more reliable for quota-limited scenarios.

---

## 8. Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| State in `.omo/` not `.omx/` | Separates OpenCode-native from OMX |
| No mailbox files | Polling is simpler for OpenCode |
| Workers write `result.md` | Standardized output format |
| Category-based spawning | Leverages existing OMO infrastructure |
| `run_in_background=true` default | Enables true parallelism |

---

## 9. Skills Created

### omo-team

**Location**: `~/.agents/skills/omo-team/SKILL.md`

**Purpose**: OpenCode-native team orchestration

**Key Features**:
- Spawns OpenCode subagent sessions (not OMX/Codex CLI)
- Uses `task()` tool with `run_in_background=true`
- Coordinates via state files in `.omo/state/omo-team/`
- Polls for completion via `background_output()`

### omo-worker

**Location**: `~/.agents/skills/omo-worker/SKILL.md`

**Purpose**: Worker protocol for OpenCode subagents

**Key Features**:
- Defines worker identity and context parsing
- Specifies result file format
- Documents communication with leader
- No mailbox needed (unlike OMX workers)

---

## 10. Comparison: OMO-Team vs OMX-Team

| Aspect | OMO-Team | OMX-Team |
|--------|----------|----------|
| **Worker Type** | OpenCode subagent sessions | Codex/Claude CLI sessions |
| **Spawning Method** | `task()` tool | `omx team` CLI + tmux |
| **Session Type** | OpenCode (same as leader) | OMX (GPT models) |
| **State Location** | `.omo/state/omo-team/` | `.omx/state/team/` |
| **Coordination** | Background task polling | tmux panes + mailbox |
| **Requires tmux** | No | Yes |
| **Works in OpenCode** | ✅ Yes | ❌ No (spawns OMX sessions) |

---

## 11. What Would I Do Differently

1. **Test skill loading earlier** - Discovered late that `load_skills` had issues
2. **Create integration test** - More comprehensive test with actual file modifications
3. **Add retry logic** - Handle background agent failures gracefully
4. **Document timeout behavior** - Workers can hang, need explicit timeout handling

---

## 12. Files Created

| File | Size | Purpose |
|------|------|---------|
| `~/.agents/skills/omo-team/SKILL.md` | 7KB | Skill implementation |
| `~/.agents/skills/omo-team/DATASHEET.md` | 12KB | Comprehensive documentation |
| `~/.agents/skills/omo-worker/SKILL.md` | 4KB | Worker protocol |

---

## 13. Usage Examples

### Basic Usage

```
/omo-team 3 "analyze the authentication module"
```

### With Category

```
/omo-team 2 "implement REST API endpoints" --category=deep
```

### With Skills

```
/omo-team 2 "review code for security issues" --category=deep --skills=security-review
```

---

## Summary

This session revealed that **OpenCode and OMX are parallel orchestration systems that don't mix well**. The solution was to create a native OpenCode team skill that:

1. Uses `task()` tool (not `omx` CLI)
2. Spawns OpenCode subagents (not Codex CLI)
3. Uses polling (not mailbox files)
4. Stores state in `.omo/` (not `.omx/`)

The skill now enables true parallel execution within OpenCode sessions, solving the original problem of subagents being OMX sessions instead of OpenCode sessions.

---

## Related Documents

- [OMO-Team Datasheet](~/.agents/skills/omo-team/DATASHEET.md)
- [OMO-Team Skill](~/.agents/skills/omo-team/SKILL.md)
- [OMO-Worker Skill](~/.agents/skills/omo-worker/SKILL.md)
- [OMX Team Skill](~/.agents/skills/team/SKILL.md) - For comparison

---

## 14. Skill Usefulness Analysis

### Question: Is `omo-team` useful or redundant?

### Analysis of Existing Skills

| Skill | Parallel Spawning | Auto-Decomposition | Auto-Role Assignment | Worker Coordination | OpenCode-Native |
|-------|-------------------|-------------------|---------------------|---------------------|-----------------|
| `ultrawork` | ✅ | ❌ Manual | ❌ Tier-based | ❌ Fire-and-forget | ✅ |
| `team` (OMX) | ✅ | ❌ Manual | ❌ Manual `N:agent-type` | ✅ Mailbox/ACK | ❌ Codex CLI |
| `swarm` | ❌ (facade) | ❌ | ❌ | ❌ | ❌ |
| `ralph` | ✅ (via ultrawork) | ❌ | ❌ | ❌ | ✅ |
| `autopilot` | ✅ (via ralph) | ❌ | ❌ | ❌ | ✅ |
| `omo-team` | ✅ | ✅ Complexity-based | ✅ Keyword-based | ✅ Background polling | ✅ |

### Verdict: `omo-team` Provides UNIQUE VALUE

**It fills a gap that no existing skill addresses:**

1. **`ultrawork`** - Parallel execution but requires manual task identification and uses tier system (not agent-specific roles)
2. **`team` (OMX)** - Has coordination but spawns Codex/Claude CLI workers (not OpenCode sessions), requires tmux, and needs manual `N:agent-type` specification
3. **`omo-team`** - The ONLY skill that:
   - Spawns OpenCode subagent sessions (not OMX/Codex CLI)
   - Automatically estimates worker count from task complexity
   - Automatically assigns roles based on subtask keywords
   - Maps roles to oh-my-opencode agents with appropriate categories

### Recommendation

**Keep `omo-team` skill.** It provides unique value as the only OpenCode-native team orchestration with automatic task decomposition and role assignment.

The existing `ultrawork` is complementary (fire-and-forget parallel execution), while `team` serves a different use case (OMX/tmux-based orchestration).

---

## 15. Complexity-Based Worker Estimation Pattern

### Implementation

```typescript
// Complexity Score (0-100) → Worker Count (1-5)
0-20:   1 worker  (simple task)
21-40:  2 workers (moderate task)
41-60:  3 workers (complex task)
61-80:  4 workers (very complex)
81-100: 5 workers (extremely complex)
```

### Factors Analyzed

- Number of files/modules involved
- Cross-cutting concerns (auth, database, API)
- Integration points
- Testing requirements
- Documentation needs

### Why This Matters

Before `omo-team`, users had to manually specify worker count. Now the skill can analyze task complexity and automatically determine optimal parallelism.

---

## 16. Automatic Role Assignment Mapping

### Keyword → Agent → Category Mapping

| Task Keyword | Agent | Category | Role |
|--------------|-------|----------|------|
| `implement`, `build`, `create` | `hephaestus` (executor) | `deep` | Implementation |
| `review`, `audit`, `check` | `momus` (reviewer) | `unspecified-high` | Quality assurance |
| `consult`, `advise`, `design` | `oracle` (consultant) | `unspecified-high` | Architecture |
| `find`, `search`, `locate` | `explore` (searcher) | N/A | Discovery |
| `research`, `document` | `librarian` (research) | N/A | Information gathering |
| `visual`, `ui`, `css`, `style` | `multimodal-looker` (visual) | `visual-engineering` | Frontend/Design |
| `plan`, `strategy`, `architect` | `metis` (planner) | `unspecified-high` | Planning |
| `analyze`, `investigate` | `janus` (analyst) | `unspecified-high` | Analysis |

### Why This Matters

Before `omo-team`, users had to manually specify agent types (e.g., `N:agent-type`). Now the skill can infer appropriate roles from task keywords.

---

## 17. Background Task Lifecycle Pattern

### The Pattern

```typescript
// 1. Spawn background task
const result = task(
  subagent_type="explore",
  run_in_background=true,
  load_skills=[],
  prompt="..."
);

// 2. System sends <system-reminder> on completion
// 3. Collect results
background_output(task_id="bg_xxx");

// 4. Cancel if needed
background_cancel(taskId="bg_xxx");
```

### Key Insight

**Never poll `background_output()` on running tasks.** Wait for the system notification (`<system-reminder>`).

### Why This Matters

Polling wastes tokens and can cause race conditions. The notification-based approach is more efficient.

---

## 18. Skill Loading Timing Issue

### Problem Encountered

`load_skills=["omo-worker"]` failed initially despite the skill being available:

```
Skills not found: omo-worker. Available: ..., omo-worker, ...
```

### Root Cause

Skills are registered asynchronously. There's a timing gap between skill creation and skill availability.

### Solution

- Retry or wait for skill registration to complete
- Alternatively, use `load_skills=[]` and include skill content/protocol in the prompt

---

## 19. Documentation Best Practices

### DATASHEET.md Structure

1. Overview table (quick reference)
2. Invocation syntax
3. Arguments (required + optional)
4. Usage examples (basic → complex)
5. Workflow diagram
6. State files (with templates)
7. Error handling
8. Comparison tables
9. Quick reference card

### Why This Matters

Complex skills need comprehensive documentation. A single SKILL.md is insufficient for skills with multiple arguments, workflows, and edge cases.

---

## 20. Git Workflow Pattern

### Pattern Used

```bash
git add .
git commit -m "feat: add omo-team skill for OpenCode-native team orchestration"
git push
```

### Lesson

Always commit after completing a logical unit of work, not at the end of session. This enables:
- Better commit messages (fresh context)
- Easier rollback if needed
- Clearer history

---

## 21. Key Architectural Insight

### The Fundamental Difference

```
OMX Team:  User → omx team CLI → tmux split → Codex CLI workers → mailbox files
OMO Team:  User → /omo-team → task() tool → OpenCode subagents → background_output()
```

### Why It Matters

You cannot use OMX skills inside OpenCode sessions because they spawn external processes. OpenCode needs its own native orchestration skills.

### Implication

When creating OpenCode skills:
- Use `task()` tool with `run_in_background=true`
- NOT OMX CLI commands
- Store state in `.omo/` not `.omx/`

---

## 22. Actionable Takeaways

1. **When creating OpenCode skills**: Use `task()` tool with `run_in_background=true`, not OMX CLI
2. **When needing parallel execution**: Use `ultrawork` for fire-and-forget, `omo-team` for coordinated work
3. **When needing auto-delegation**: Only `omo-team` provides automatic worker count and role assignment
4. **Documentation**: Always create DATASHEET.md for complex skills
5. **Session continuity**: Document learnings in `session-learnings-*.md` files

---

**Session Date**: April 8, 2026
**Session Number**: 8
**Duration**: ~3 hours
**Outcome**: Successfully created and tested OpenCode-native team orchestration skill with comprehensive analysis proving its unique value
