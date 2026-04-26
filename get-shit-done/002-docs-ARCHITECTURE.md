---
title: ARCHITECTURE
url: https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md
source: git
fetched_at: 2026-04-16T16:20:04.615476267-03:00
rendered_js: false
word_count: 3344
summary: This document outlines the architectural design, core components, and design principles of the GSD meta-prompting framework, which serves as an orchestration layer for AI coding agents.
tags:
    - architecture
    - meta-prompting
    - multi-agent-system
    - context-management
    - workflow-automation
    - system-design
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# GSD Architecture

> System architecture for contributors and advanced users. For user-facing documentation, see [[002-docs-FEATURES|Feature Reference]] or [[002-docs-USER-GUIDE|User Guide]].

---

## System Overview

GSD is a **meta-prompting framework** that sits between the user and AI coding agents (Claude Code, Gemini CLI, OpenCode, Kilo, Codex, Copilot, Antigravity, Trae, Cline, Augment Code). It provides context engineering, multi-agent orchestration, spec-driven development, and persistent state management.

```
┌──────────────────────────────────────────────────────┐
│                      USER                            │
│            /gsd-command [args]                        │
└─────────────────────┬────────────────────────────────┘
                      │
┌─────────────────────▼────────────────────────────────┐
│              COMMAND LAYER                            │
│   commands/gsd/*.md — Prompt-based command files      │
│   (Claude Code custom commands / Codex skills)        │
└─────────────────────┬────────────────────────────────┘
                      │
┌─────────────────────▼────────────────────────────────┐
│              WORKFLOW LAYER                           │
│   get-shit-done/workflows/*.md — Orchestration logic  │
│   (Reads references, spawns agents, manages state)    │
└──────┬──────────────┬─────────────────┬──────────────┘
       │              │                 │
┌──────▼──────┐ ┌─────▼─────┐ ┌────────▼───────┐
│  AGENT      │ │  AGENT    │ │  AGENT         │
│  (fresh     │ │  (fresh   │ │  (fresh        │
│   context)  │ │   context)│ │   context)     │
└──────┬──────┘ └─────┬─────┘ └────────┬───────┘
       │              │                 │
┌──────▼──────────────▼─────────────────▼──────────────┐
│              CLI TOOLS LAYER                          │
│   gsd-sdk query (sdk/src/query) + gsd-tools.cjs       │
│   (State, config, phase, roadmap, verify, templates)  │
└──────────────────────┬───────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────┐
│              FILE SYSTEM (.planning/)                 │
│   PROJECT.md | REQUIREMENTS.md | ROADMAP.md          │
│   STATE.md | config.json | phases/ | research/       │
└──────────────────────────────────────────────────────┘
```

---

## Design Principles

### Fresh Context Per Agent

Every agent spawned by an orchestrator gets a clean context window (up to 200K tokens), eliminating context rot — quality degradation from accumulated conversation.

### Thin Orchestrators

Workflow files (`get-shit-done/workflows/*.md`) never do heavy lifting. They:
- Load context via `gsd-sdk query init.<workflow>`
- Spawn specialized agents with focused prompts
- Collect results and route to the next step
- Update state between steps

### File-Based State

All state lives in `.planning/` as human-readable Markdown and JSON. No database, no server, no external dependencies:
- State survives context resets (`/clear`)
- State is inspectable by both humans and agents
- State can be committed to git for team visibility

### Absent = Enabled

Workflow feature flags follow the **absent = enabled** pattern. Missing keys in `config.json` default to `true`. Users explicitly disable features.

### Defense in Depth

Multiple layers prevent common failure modes:
- Plans verified before execution (plan-checker agent)
- Execution produces atomic commits per task
- Post-execution verification checks against phase goals
- UAT provides human verification as final gate

---

## Component Architecture

### Commands (`commands/gsd/*.md`)

User-facing entry points with YAML frontmatter (name, description, allowed-tools) and prompt body. **Total commands:** 74.

| Runtime | Format |
|---------|--------|
| Claude Code | `/gsd-command-name` |
| OpenCode / Kilo | `/gsd-command-name` |
| Codex | `$gsd-command-name` |
| Copilot | `/gsd-command-name` |
| Antigravity | Skills |

### Workflows (`get-shit-done/workflows/*.md`)

Orchestration logic containing:
- Context loading via `gsd-sdk query` init handlers
- Agent spawn instructions with model resolution
- Gate/checkpoint definitions
- State update patterns
- Error handling and recovery

**Total workflows:** 71.

### Agents (`agents/*.md`)

Specialized agent definitions with frontmatter:
- `name` — Agent identifier
- `description` — Role and purpose
- `tools` — Allowed tool access
- `color` — Terminal output color

**Total agents:** 31.

### References (`get-shit-done/references/*.md`)

Shared knowledge documents that workflows and agents `@-reference` (35 total).

**Core references:**
- `checkpoints.md` — Checkpoint type definitions
- `gates.md` — 4 canonical gate types (Confirm, Quality, Safety, Transition)
- `model-profiles.md` — Per-agent model tier assignments
- `model-profile-resolution.md` — Model resolution algorithm
- `verification-patterns.md` — Artifact verification methods
- `verification-overrides.md` — Per-artifact verification overrides
- `planning-config.md` — Config schema and behavior
- `git-integration.md` — Git commit, branching, history patterns
- `git-planning-commit.md` — Planning directory commit conventions
- `questioning.md` — Dream extraction philosophy
- `tdd.md` — TDD integration patterns
- `ui-brand.md` — Visual output formatting
- `common-bug-patterns.md` — Bug patterns for code review

**Workflow references:**
- `agent-contracts.md` — Orchestrator/agent interface
- `context-budget.md` — Context window allocation
- `continuation-format.md` — Session continuation/resume
- `domain-probes.md` — Domain-specific probing questions
- `gate-prompts.md` — Gate/checkpoint templates
- `revision-loop.md` — Plan revision iteration
- `universal-anti-patterns.md` — Anti-patterns to detect
- `artifact-types.md` — Planning artifact types
- `phase-argument-parsing.md` — Phase argument parsing
- `decimal-phase-calculation.md` — Decimal sub-phase numbering
- `workstream-flag.md` — Workstream active pointer
- `user-profiling.md` — User behavioral profiling
- `thinking-partner.md` — Conditional thinking partner

**Thinking model references:**
- `thinking-models-debug.md` — Debugging workflows
- `thinking-models-execution.md` — Execution agents
- `thinking-models-planning.md` — Planning agents
- `thinking-models-research.md` — Research agents
- `thinking-models-verification.md` — Verification agents

**Modular planner decomposition:**
- `planner-gap-closure.md` — Gap closure mode
- `planner-reviews.md` — Cross-AI review integration
- `planner-revision.md` — Plan revision patterns

### Templates (`get-shit-done/templates/`)

Markdown templates for all planning artifacts:
- `project.md`, `requirements.md`, `roadmap.md`, `state.md` — Core files
- `phase-prompt.md` — Phase execution template
- `summary.md` (+ variants) — Summary templates
- `DEBUG.md` — Debug session template
- `UI-SPEC.md`, `UAT.md`, `VALIDATION.md` — Verification templates
- `discussion-log.md` — Discussion audit trail
- `codebase/` — Brownfield mapping templates
- `research-project/` — Research output templates

### Hooks (`hooks/`)

| Hook | Event | Purpose |
|------|-------|---------|
| `gsd-statusline.js` | `statusLine` | Displays model, task, directory, context usage bar |
| `gsd-context-monitor.js` | `PostToolUse` / `AfterTool` | Injects context warnings at 35%/25% remaining |
| `gsd-check-update.js` | `SessionStart` | Background check for new GSD versions |
| `gsd-prompt-guard.js` | `PreToolUse` | Scans `.planning/` writes for prompt injection |
| `gsd-workflow-guard.js` | `PreToolUse` | Detects edits outside GSD workflow context |
| `gsd-read-guard.js` | `PreToolUse` | Prevents Edit/Write on unread files |
| `gsd-session-state.sh` | `PostToolUse` | Session state tracking |
| `gsd-validate-commit.sh` | `PostToolUse` | Commit validation |
| `gsd-phase-boundary.sh` | `PostToolUse` | Phase boundary detection |

### CLI Tools (`get-shit-done/bin/`)

Node.js CLI (`gsd-tools.cjs`) with 19 domain modules:

| Module | Responsibility |
|--------|---------------|
| `core.cjs` | Error handling, output formatting |
| `state.cjs` | STATE.md parsing, updating, progression |
| `phase.cjs` | Phase directory operations, decimal numbering |
| `roadmap.cjs` | ROADMAP.md parsing, phase extraction |
| `config.cjs` | config.json read/write |
| `verify.cjs` | Plan structure, phase completeness |
| `template.cjs` | Template selection and filling |
| `frontmatter.cjs` | YAML frontmatter CRUD |
| `init.cjs` | Compound context loading |
| `milestone.cjs` | Milestone archival |
| `commands.cjs` | Misc commands |
| `model-profiles.cjs` | Model profile resolution |
| `security.cjs` | Path traversal prevention, prompt injection detection |
| `uat.cjs` | UAT file parsing, verification debt |
| `docs.cjs` | Docs-update workflow |
| `workstream.cjs` | Workstream CRUD |
| `schema-detect.cjs` | Schema-drift detection |
| `profile-pipeline.cjs` | User profiling data pipeline |
| `profile-output.cjs` | Profile rendering |

---

## Agent Model

### Orchestrator → Agent Pattern

```
Orchestrator (workflow .md)
    │
    ├── Load context: gsd-tools.cjs init <workflow> <phase>
    │   Returns JSON: project info, config, state, phase details
    │
    ├── Resolve model: gsd-tools.cjs resolve-model <agent-name>
    │   Returns: opus | sonnet | haiku | inherit
    │
    ├── Spawn Agent (Task/SubAgent call)
    │   ├── Agent prompt (agents/*.md)
    │   ├── Context payload (init JSON)
    │   ├── Model assignment
    │   └── Tool permissions
    │
    ├── Collect result
    │
    └── Update state: gsd-tools.cjs state update/patch/advance-plan
```

### Agent Spawn Categories

| Category | Agents | Parallelism |
|----------|--------|-------------|
| **Researchers** | gsd-project-researcher, gsd-phase-researcher, gsd-ui-researcher, gsd-advisor-researcher | 4 parallel |
| **Synthesizers** | gsd-research-synthesizer | Sequential |
| **Planners** | gsd-planner, gsd-roadmapper | Sequential |
| **Checkers** | gsd-plan-checker, gsd-integration-checker, gsd-ui-checker, gsd-nyquist-auditor | Sequential |
| **Executors** | gsd-executor | Parallel within waves |
| **Verifiers** | gsd-verifier | Sequential |
| **Mappers** | gsd-codebase-mapper | 4 parallel |
| **Debuggers** | gsd-debugger | Sequential |
| **Auditors** | gsd-ui-auditor, gsd-security-auditor | Sequential |
| **Doc Writers** | gsd-doc-writer, gsd-doc-verifier | Sequential |
| **Profilers** | gsd-user-profiler | Sequential |
| **Analyzers** | gsd-assumptions-analyzer | Sequential |

### Wave Execution Model

Plans are grouped into dependency waves during `execute-phase`:

```
Wave Analysis:
  Plan 01 (no deps)      ─┐
  Plan 02 (no deps)      ─┤── Wave 1 (parallel)
  Plan 03 (depends: 01)  ─┤── Wave 2 (waits for Wave 1)
  Plan 04 (depends: 02)  ─┘
  Plan 05 (depends: 03,04) ── Wave 3 (waits for Wave 2)
```

Each executor gets:
- Fresh 200K context window (or up to 1M for supported models)
- The specific PLAN.md to execute
- Project context (PROJECT.md, STATE.md)
- Phase context (CONTEXT.md, RESEARCH.md if available)

### Adaptive Context Enrichment (1M Models)

When context window is 500K+ tokens, subagent prompts are enriched with additional context:
- **Executor agents** receive prior wave SUMMARY.md files and phase CONTEXT.md/RESEARCH.md
- **Verifier agents** receive all PLAN.md, SUMMARY.md, CONTEXT.md files plus REQUIREMENTS.md

The orchestrator reads `context_window` from config and conditionally includes richer context when >= 500,000.

#### Parallel Commit Safety

Two mechanisms prevent conflicts in parallel execution:

1. **`--no-verify` commits** — Parallel agents skip pre-commit hooks. Orchestrator runs `git hook run pre-commit` once after each wave.
2. **STATE.md file locking** — All `writeStateMd()` calls use lockfile-based mutual exclusion (`STATE.md.lock` with `O_EXCL`). Includes stale lock detection (10s timeout) and spin-wait with jitter.

---

## Data Flow

### New Project Flow

```
User input (idea description)
    │
    ▼
Questions (questioning.md philosophy)
    │
    ▼
4x Project Researchers (parallel)
    ├── Stack → STACK.md
    ├── Features → FEATURES.md
    ├── Architecture → ARCHITECTURE.md
    └── Pitfalls → PITFALLS.md
    │
    ▼
Research Synthesizer → SUMMARY.md
    │
    ▼
Requirements extraction → REQUIREMENTS.md
    │
    ▼
Roadmapper → ROADMAP.md
    │
    ▼
User approval → STATE.md initialized
```

### Phase Execution Flow

```
discuss-phase → CONTEXT.md (user preferences)
    │
    ▼
ui-phase → UI-SPEC.md (design contract, optional)
    │
    ▼
plan-phase
    ├── Research gate (blocks if RESEARCH.md has unresolved open questions)
    ├── Phase Researcher → RESEARCH.md
    ├── Planner (with reachability check) → PLAN.md files
    └── Plan Checker → Verify loop (max 3x)
    │
    ▼
state planned-phase → STATE.md (Planned/Ready to execute)
    │
    ▼
execute-phase
    ├── Wave analysis (dependency grouping)
    ├── Executor per plan → code + atomic commits
    ├── SUMMARY.md per plan
    └── Verifier → VERIFICATION.md
    │
    ▼
verify-work → UAT.md (user acceptance testing)
    │
    ▼
ui-review → UI-REVIEW.md (visual audit, optional)
```

### Context Propagation

```
PROJECT.md ────────────────────────────────────────────► All agents
REQUIREMENTS.md ───────────────────────────────────────► Planner, Verifier, Auditor
ROADMAP.md ────────────────────────────────────────────► Orchestrators
STATE.md ──────────────────────────────────────────────► All agents (decisions, blockers)
CONTEXT.md (per phase) ────────────────────────────────► Researcher, Planner, Executor
RESEARCH.md (per phase) ─────────────────────────────► Planner, Plan Checker
PLAN.md (per plan) ────────────────────────────────────► Executor, Plan Checker
SUMMARY.md (per plan) ─────────────────────────────────► Verifier, State tracking
UI-SPEC.md (per phase) ────────────────────────────────► Executor, UI Auditor
```

---

## File System Layout

### Installation Files

```
~/.claude/                          # Claude Code (global install)
├── commands/gsd/*.md               # 74 slash commands
├── get-shit-done/
│   ├── bin/gsd-tools.cjs           # CLI utility
│   ├── bin/lib/*.cjs               # 19 domain modules
│   ├── workflows/*.md              # 71 workflow definitions
│   ├── references/*.md             # 35 shared reference docs
│   └── templates/                  # Planning artifact templates
├── agents/*.md                     # 31 agent definitions
├── hooks/
│   ├── gsd-statusline.js           # Statusline hook
│   ├── gsd-context-monitor.js      # Context warning hook
│   └── gsd-check-update.js         # Update check hook
├── settings.json                   # Hook registrations
└── VERSION                         # Installed version number
```

Other runtime paths:
- **OpenCode:** `~/.config/opencode/` or `~/.opencode/`
- **Kilo:** `~/.config/kilo/` or `~/.kilo/`
- **Gemini CLI:** `~/.gemini/`
- **Codex:** `~/.codex/`
- **Copilot:** `~/.github/`
- **Antigravity:** `~/.gemini/antigravity/` (global) or `./.agent/` (local)

### Project Files (`.planning/`)

```
.planning/
├── PROJECT.md              # Project vision, constraints, decisions
├── REQUIREMENTS.md         # Scoped requirements (v1/v2/out-of-scope)
├── ROADMAP.md              # Phase breakdown with status tracking
├── STATE.md                # Living memory: position, decisions, blockers
├── config.json             # Workflow configuration
├── MILESTONES.md           # Completed milestone archive
├── research/               # Domain research from /gsd-new-project
│   ├── SUMMARY.md
│   ├── STACK.md
│   ├── FEATURES.md
│   ├── ARCHITECTURE.md
│   └── PITFALLS.md
├── codebase/               # Brownfield mapping
│   ├── STACK.md
│   ├── ARCHITECTURE.md
│   ├── CONVENTIONS.md
│   ├── CONCERNS.md
│   ├── STRUCTURE.md
│   ├── TESTING.md
│   └── INTEGRATIONS.md
├── phases/
│   └── XX-phase-name/
│       ├── XX-CONTEXT.md       # User preferences
│       ├── XX-RESEARCH.md      # Ecosystem research
│       ├── XX-YY-PLAN.md       # Execution plans
│       ├── XX-YY-SUMMARY.md    # Execution outcomes
│       ├── XX-VERIFICATION.md # Post-execution verification
│       ├── XX-VALIDATION.md    # Nyquist test coverage
│       ├── XX-UI-SPEC.md       # UI design contract
│       ├── XX-UI-REVIEW.md     # Visual audit scores
│       └── XX-UAT.md           # User acceptance test results
├── quick/                  # Quick task tracking
│   └── YYMMDD-xxx-slug/
│       ├── PLAN.md
│       └── SUMMARY.md
├── todos/
│   ├── pending/            # Captured ideas
│   └── done/               # Completed todos
├── threads/               # Persistent context threads
├── seeds/                 # Forward-looking ideas
├── debug/                  # Active debug sessions
│   ├── *.md                # Active sessions
│   ├── resolved/           # Archived sessions
│   └── knowledge-base.md   # Persistent debug learnings
├── ui-reviews/             # Screenshots (gitignored)
└── continue-here.md        # Context handoff
```

---

## Installer Architecture

The installer (`bin/install.js`, ~3,000 lines) handles:

1. **Runtime detection** — Interactive prompt or CLI flags (`--claude`, `--opencode`, `--gemini`, `--kilo`, `--codex`, `--copilot`, `--antigravity`, `--cursor`, `--windsurf`, `--trae`, `--cline`, `--augment`, `--all`)
2. **Location selection** — Global (`--global`) or local (`--local`)
3. **File deployment** — Copies commands, workflows, references, templates, agents, hooks
4. **Runtime adaptation** — Transforms file content per runtime:
   - Claude Code: Uses as-is
   - OpenCode: Converts to flat command + subagent format
   - Kilo: Reuses OpenCode conversion pipeline
   - Codex: Generates TOML config + skills
   - Copilot: Maps tool names (Read→read, Bash→execute, etc.)
   - Gemini: Adjusts hook event names (`AfterTool` instead of `PostToolUse`)
   - Antigravity: Skills-first with Google model equivalents
   - Trae: Skills-first install to `~/.trae` / `./.trae`
   - Cline: Writes `.clinerules`
   - Augment Code: Skills-first with full skill conversion
5. **Path normalization** — Replaces `~/.claude/` paths with runtime-specific paths
6. **Settings integration** — Registers hooks in runtime's `settings.json`
7. **Patch backup** — Since v1.17, backs up locally modified files to `gsd-local-patches/`
8. **Manifest tracking** — Writes `gsd-file-manifest.json` for clean uninstall
9. **Uninstall mode** — `--uninstall` removes all GSD files, hooks, settings

### Platform Handling

- **Windows:** `windowsHide` on child processes, EPERM/EACCES protection, path separator normalization
- **WSL:** Detects Windows Node.js and warns about path mismatches
- **Docker/CI:** Supports `CLAUDE_CONFIG_DIR` env var

---

## Hook System

### Architecture

```
Runtime Engine (Claude Code / Gemini CLI)
    │
    ├── statusLine event ──► gsd-statusline.js
    │   Reads: stdin (session JSON)
    │   Writes: stdout (formatted status), /tmp/claude-ctx-{session}.json
    │
    ├── PostToolUse/AfterTool event ──► gsd-context-monitor.js
    │   Reads: stdin (tool event JSON), /tmp/claude-ctx-{session}.json
    │   Writes: stdout (additionalContext warning)
    │
    └── SessionStart event ──► gsd-check-update.js
        Reads: VERSION file
        Writes: ~/.claude/cache/gsd-update-check.json
```

### Context Monitor Thresholds

| Remaining Context | Level | Agent Behavior |
|-------------------|-------|----------------|
| > 35% | Normal | No warning injected |
| ≤ 35% | WARNING | "Avoid starting new complex work" |
| ≤ 25% | CRITICAL | "Context nearly exhausted, inform user" |

Debounce: 5 tool uses between repeated warnings. Severity escalation bypasses debounce.

### Safety Properties

- All hooks wrap in try/catch, exit silently on error
- stdin timeout guard (3s) prevents hanging
- Stale metrics (>60s old) are ignored
- Missing bridge files handled gracefully
- Context monitor is advisory only

### Security Hooks (v1.27)

**Prompt Guard** (`gsd-prompt-guard.js`):
- Triggers on Write/Edit to `.planning/` files
- Scans content for prompt injection patterns
- Advisory-only — logs detection, does not block

**Workflow Guard** (`gsd-workflow-guard.js`):
- Triggers on Write/Edit to non-`.planning/` files
- Detects edits outside GSD workflow context
- Opt-in via `hooks.workflow_guard: true`

---

## Runtime Abstraction

GSD supports multiple AI coding runtimes through a unified command/workflow architecture:

| Runtime | Command Format | Agent System | Config Location |
|---------|---------------|--------------|-----------------|
| Claude Code | `/gsd-command` | Task spawning | `~/.claude/` |
| OpenCode | `/gsd-command` | Subagent mode | `~/.config/opencode/` |
| Kilo | `/gsd-command` | Subagent mode | `~/.config/kilo/` |
| Gemini CLI | `/gsd-command` | Task spawning | `~/.gemini/` |
| Codex | `$gsd-command` | Skills | `~/.codex/` |
| Copilot | `/gsd-command` | Agent delegation | `~/.github/` |
| Antigravity | Skills | Skills | `~/.gemini/antigravity/` |
| Trae | Skills | Skills | `~/.trae/` |
| Cline | Rules | Rules | `.clinerules` |
| Augment Code | Skills | Skills | Augment config |

### Abstraction Points

1. **Tool name mapping** — Each runtime has its own tool names
2. **Hook event names** — Claude uses `PostToolUse`, Gemini uses `AfterTool`
3. **Agent frontmatter** — Each runtime has its own agent definition format
4. **Path conventions** — Each runtime stores config in different directories
5. **Model references** — `inherit` profile lets GSD defer to runtime's model selection

The installer handles all translation at install time. Workflows and agents are written in Claude Code's native format and transformed during deployment.

#architecture #meta-prompting #multi-agent-system #context-management #workflow-automation #system-design
