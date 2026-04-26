---
title: USER GUIDE
url: https://github.com/gsd-build/get-shit-done/blob/main/docs/USER-GUIDE.md
source: git
fetched_at: 2026-04-16T16:20:06.513077891-03:00
rendered_js: false
word_count: 6321
summary: Comprehensive operational manual for the GSD system, covering project lifecycle workflows, automated planning procedures, and the Nyquist validation architecture.
tags:
    - project-management
    - workflow-automation
    - system-configuration
    - software-development
    - quality-assurance
    - technical-reference
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# GSD User Guide

> [!info] For quick-start setup, see the [README](../README.md).

# Workflow Diagrams

## Full Project Lifecycle

```
  ┌──────────────────────────────────────────────────┐
  │                   NEW PROJECT                    │
  │  /gsd-new-project                                │
  │  Questions -> Research -> Requirements -> Roadmap│
  └─────────────────────────┬────────────────────────┘
                            │
             ┌──────────────▼─────────────┐
             │      FOR EACH PHASE:       │
             │                            │
             │  ┌────────────────────┐    │
             │  │ /gsd-discuss-phase │    │  <- Lock in preferences
             │  └──────────┬─────────┘    │
             │             │              │
             │  ┌──────────▼─────────┐    │
             │  │ /gsd-ui-phase      │    │  <- Design contract (frontend)
             │  └──────────┬─────────┘    │
             │             │              │
             │  ┌──────────▼─────────┐    │
             │  │ /gsd-plan-phase    │    │  <- Research + Plan + Verify
             │  └──────────┬─────────┘    │
             │             │              │
             │  ┌──────────▼─────────┐    │
             │  │ /gsd-execute-phase │    │  <- Parallel execution
             │  └──────────┬─────────┘    │
             │             │              │
             │  ┌──────────▼─────────┐    │
             │  │ /gsd-verify-work   │    │  <- Manual UAT
             │  └──────────┬─────────┘    │
             │             │              │
             │  ┌──────────▼─────────┐    │
             │  │ /gsd-ship          │    │  <- Create PR (optional)
             │  └──────────┬─────────┘    │
             │             │              │
             │     Next Phase?────────────┘
             │             │ No
             └─────────────┼──────────────┘
                            │
            ┌───────────────▼──────────────┐
            │  /gsd-audit-milestone        │
            │  /gsd-complete-milestone     │
            └───────────────┬──────────────┘
                            │
                   Another milestone?
                       │          │
                      Yes         No -> Done!
                       │
               ┌───────▼──────────────┐
               │  /gsd-new-milestone  │
               └──────────────────────┘
```

## Planning Agent Coordination

```
  /gsd-plan-phase N
         │
         ├── Phase Researcher (x4 parallel)
         │     ├── Stack researcher
         │     ├── Features researcher
         │     ├── Architecture researcher
         │     └── Pitfalls researcher
         │           │
         │     ┌──────▼──────┐
         │     │ RESEARCH.md │
         │     └──────┬──────┘
         │            │
         │     ┌──────▼──────┐
         │     │   Planner   │  <- Reads PROJECT.md, REQUIREMENTS.md,
         │     │             │     CONTEXT.md, RESEARCH.md
         │     └──────┬──────┘
         │            │
         │     ┌──────▼───────────┐     ┌────────┐
         │     │   Plan Checker   │────>│ PASS?  │
         │     └──────────────────┘     └───┬────┘
         │                                  │
         │                             Yes  │  No
         │                              │   │   │
         │                              │   └───┘  (loop, up to 3x)
         │                              │
         │                        ┌─────▼──────┐
         │                        │ PLAN files │
         │                        └────────────┘
         └── Done
```

## Validation Architecture (Nyquist Layer)

GSD maps automated test coverage to each phase requirement during plan-phase research before any code is written, ensuring feedback exists when executor commits a task.

The researcher detects existing test infrastructure, maps each requirement to a specific test command, and identifies test scaffolding needed before implementation (Wave 0 tasks). The plan-checker enforces this as an 8th verification dimension: plans without automated verify commands are not approved.

**Output:** `{phase}-VALIDATION.md`

**Disable:** Set `workflow.nyquist_validation: false` in `/gsd-settings`

## Retroactive Validation (`/gsd-validate-phase`)

For phases executed before Nyquist existed, or existing codebases with traditional test suites:

```
  /gsd-validate-phase N
         |
         +-- Detect state (VALIDATION.md exists? SUMMARY.md exists?)
         |
         +-- Discover: scan implementation, map requirements to tests
         |
         +-- Analyze gaps: which requirements lack automated verification?
         |
         +-- Present gap plan for approval
         |
         +-- Spawn auditor: generate tests, run, debug (max 3 attempts)
         |
         +-- Update VALIDATION.md
               |
               +-- COMPLIANT -> all requirements have automated checks
               +-- PARTIAL -> some gaps escalated to manual-only
```

The auditor never modifies implementation code — only test files and VALIDATION.md. Flags implementation bugs as escalations.

**When to use:** After phases planned before Nyquist enabled, or after `/gsd-audit-milestone` surfaces compliance gaps.

## Assumptions Discussion Mode

`/gsd-discuss-phase` asks open-ended questions by default. Assumptions mode inverts this: GSD reads your codebase first, surfaces structured assumptions, asks only for corrections.

**Enable:** Set `workflow.discuss_mode` to `'assumptions'` via `/gsd-settings`

**How it works:**
1. Reads PROJECT.md, codebase mapping, existing conventions
2. Generates structured list of assumptions
3. Presents for confirmation/correction
4. Writes CONTEXT.md from confirmed assumptions

**When to use:**
- Experienced developers who know their codebase
- Rapid iteration where open-ended questions slow you down
- Projects with well-established patterns

---

# UI Design Contract

## Why

AI-generated frontends are visually inconsistent because no design contract existed before execution. `/gsd-ui-phase` locks the design contract before planning. `/gsd-ui-review` audits the result after execution.

## Commands

| Command | Description |
|---------|-------------|
| `/gsd-ui-phase [N]` | Generate UI-SPEC.md design contract for frontend phase |
| `/gsd-ui-review [N]` | Retroactive 6-pillar visual audit of implemented UI |

## Workflow: `/gsd-ui-phase`

**When:** After `/gsd-discuss-phase`, before `/gsd-plan-phase` — for phases with frontend/UI work.

**Flow:**
1. Reads CONTEXT.md, RESEARCH.md, REQUIREMENTS.md
2. Detects design system state (shadcn components.json, Tailwind config, tokens)
3. shadcn initialization gate — offers to initialize if React/Next.js/Vite project has none
4. Asks only unanswered design contract questions
5. Writes `{phase}-UI-SPEC.md` to phase directory
6. Validates against 6 dimensions
7. Revision loop if BLOCKED (max 2 iterations)

**Output:** `{padded_phase}-UI-SPEC.md` in `.planning/phases/{phase-dir}/`

## Workflow: `/gsd-ui-review`

**When:** After `/gsd-execute-phase` or `/gsd-verify-work` — for any project with frontend code.

**Standalone:** Works on any project, not just GSD-managed ones. If no UI-SPEC.md exists, audits against abstract 6-pillar standards.

**6 Pillars (scored 1-4 each):**
1. Copywriting — CTA labels, empty states, error states
2. Visuals — Focal points, visual hierarchy, icon accessibility
3. Color — accent usage discipline, 60/30/10 compliance
4. Typography — font size/weight constraint adherence
5. Spacing — grid alignment, token consistency
6. Experience Design — loading/error/empty state coverage

**Output:** `{padded_phase}-UI-REVIEW.md` with scores and top 3 priority fixes.

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `workflow.ui_phase` | `true` | Generate UI design contracts |
| `workflow.ui_safety_gate` | `true` | plan-phase prompts to run /gsd-ui-phase |

Both follow absent=enabled pattern. Disable via `/gsd-settings`.

## shadcn Initialization

For React/Next.js/Vite projects, UI researcher offers to initialize shadcn if no `components.json` is found:

1. Visit `ui.shadcn.com/create`, configure preset
2. Copy preset string
3. Run `npx shadcn init --preset {paste}`

Preset encodes entire design system — colors, border radius, fonts. Becomes first-class GSD planning artifact.

## Registry Safety Gate

Third-party shadcn registries can inject arbitrary code. Safety gate requires:
- `npx shadcn view {component}` — inspect before installing
- `npx shadcn diff {component}` — compare against official

Controlled by `workflow.ui_safety_gate` config toggle.

## Screenshot Storage

`/gsd-ui-review` captures screenshots via Playwright CLI to `.planning/ui-reviews/`. `.gitignore` created automatically. Screenshots cleaned during `/gsd-complete-milestone`.

---

# Backlog & Threads

## Backlog Parking Lot

Ideas not ready for active planning go into backlog using 999.x numbering.

```
/gsd-add-backlog "GraphQL API layer"     # Creates 999.1-graphql-api-layer/
/gsd-add-backlog "Mobile responsive"     # Creates 999.2-mobile-responsive/
```

Backlog items get full phase directories. Use `/gsd-discuss-phase 999.1` to explore, `/gsd-plan-phase 999.1` when ready.

**Review and promote** with `/gsd-review-backlog`

## Seeds

Seeds are forward-looking ideas with trigger conditions. Surface automatically when the right milestone arrives.

```
/gsd-plant-seed "Add real-time collab when WebSocket infra is in place"
```

Seeds preserve full WHY and WHEN. `/gsd-new-milestone` scans all seeds and presents matches.

**Storage:** `.planning/seeds/SEED-NNN-slug.md`

## Persistent Context Threads

Lightweight cross-session knowledge stores for work spanning multiple sessions but not belonging to a specific phase.

```
/gsd-thread                              # List all threads
/gsd-thread fix-deploy-key-auth          # Resume existing thread
/gsd-thread "Investigate TCP timeout"    # Create new thread
```

Threads are lighter than `/gsd-pause-work` — no phase state, no plan context. Each thread includes Goal, Context, References, Next Steps.

Threads can be promoted to phases or backlog items.

**Storage:** `.planning/threads/{slug}.md`

---

# Workstreams

Workstreams let you work on multiple milestone areas concurrently without state collisions. Each workstream gets isolated `.planning/` state.

**When to use:** Backend API and frontend dashboard planned/executed independently without context bleed.

## Commands

| Command | Purpose |
|---------|---------|
| `/gsd-workstreams create <name>` | Create new workstream with isolated planning state |
| `/gsd-workstreams switch <name>` | Switch active context to different workstream |
| `/gsd-workstreams list` | Show all workstreams and which is active |
| `/gsd-workstreams complete <name>` | Mark workstream done and archive its state |

## How It Works

Each workstream maintains own `.planning/` directory subtree. GSD swaps active planning context so `/gsd-progress`, `/gsd-discuss-phase`, `/gsd-plan-phase` operate on that workstream's state.

Lighter weight than `/gsd-new-workspace`. Workstreams share same codebase and git history but isolate planning artifacts.

---

# Security

## Defense-in-Depth (v1.27)

GSD generates markdown files that become LLM system prompts. User-controlled text flowing into planning artifacts is a potential indirect prompt injection vector.

**Path Traversal Prevention:** All user-supplied file paths validated to resolve within project directory. macOS `/var` → `/private/var` symlink resolution handled.

**Prompt Injection Detection:** `security.cjs` module scans for known injection patterns in user-supplied text before it enters planning artifacts.

**Runtime Hooks:**
- `gsd-prompt-guard.js` — Scans Write/Edit calls to `.planning/` for injection patterns (always active, advisory-only)
- `gsd-workflow-guard.js` — Warns on file edits outside GSD workflow context (opt-in via `hooks.workflow_guard`)

**CI Scanner:** `prompt-injection-scan.test.cjs` scans all agent, workflow, command files for embedded injection vectors.

## Execution Wave Coordination

```
  /gsd-execute-phase N
         │
         ├── Analyze plan dependencies
         │
         ├── Wave 1 (independent plans):
         │     ├── Executor A (fresh 200K context) -> commit
         │     └── Executor B (fresh 200K context) -> commit
         │
         ├── Wave 2 (depends on Wave 1):
         │     └── Executor C (fresh 200K context) -> commit
         │
         └── Verifier
               ├── Check codebase against phase goals
               ├── Test quality audit
               │
               ├── PASS -> VERIFICATION.md
               └── FAIL -> Issues logged for /gsd-verify-work
```

## Brownfield Workflow (Existing Codebase)

```
  /gsd-map-codebase
         │
         ├── Stack Mapper     -> codebase/STACK.md
         ├── Arch Mapper      -> codebase/ARCHITECTURE.md
         ├── Convention Mapper -> codebase/CONVENTIONS.md
         └── Concern Mapper   -> codebase/CONCERNS.md
                │
        ┌───────▼──────────┐
        │ /gsd-new-project │  <- Questions focus on what you're ADDING
        └──────────────────┘
```

---

# Code Review Workflow

## Phase Code Review

After executing a phase, run structured code review before UAT:

```bash
/gsd-code-review 3               # Review all changed files in phase 3
/gsd-code-review 3 --depth=deep  # Deep cross-file review
```

Reviewer scopes files using SUMMARY.md (preferred) or git diff fallback. Findings classified as Critical, Warning, or Info in `{phase}-REVIEW.md`.

```bash
/gsd-code-review-fix 3           # Fix Critical + Warning findings atomically
/gsd-code-review-fix 3 --auto    # Fix and re-review until clean (max 3 iterations)
```

## Autonomous Audit-to-Fix

```bash
/gsd-audit-fix                   # Audit + classify + fix (medium+ severity, max 5)
/gsd-audit-fix --dry-run         # Preview classification without fixing
```

## Code Review in Full Phase Lifecycle

```
/gsd-execute-phase N   ->  /gsd-code-review N  ->  /gsd-code-review-fix N  ->  /gsd-verify-work N
```

---

# Exploration & Discovery

## Socratic Exploration

Before committing to a new phase or plan, use `/gsd-explore`:

```bash
/gsd-explore                           # Open-ended ideation
/gsd-explore "caching strategy"        # Explore specific topic
```

Exploration session guides through probing questions, optionally spawns research agent, routes output to appropriate GSD artifact.

## Codebase Intelligence

Enable intel system:

```json
{ "intel": { "enabled": true } }
```

Then build index:

```bash
/gsd-intel refresh             # Analyze codebase and write .planning/intel/ files
/gsd-intel query auth          # Search for term across all intel files
/gsd-intel status              # Check freshness of intel files
/gsd-intel diff                # See what changed since last snapshot
```

Intel files cover stack, API surface, dependency graph, file roles, architecture decisions.

## Quick Scan

```bash
/gsd-scan                      # Quick tech + arch overview
/gsd-scan --focus quality      # Quality and code health only
/gsd-scan --focus concerns     # Risk areas and concerns
```

---

# Command Reference

## Core Workflow

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/gsd-new-project` | Full project init | Start of new project |
| `/gsd-new-project --auto @idea.md` | Automated init from document | Have PRD ready |
| `/gsd-discuss-phase [N]` | Capture implementation decisions | Before planning |
| `/gsd-ui-phase [N]` | Generate UI design contract | After discuss-phase (frontend) |
| `/gsd-plan-phase [N]` | Research + plan + verify | Before executing |
| `/gsd-execute-phase <N>` | Execute all plans in parallel waves | After planning complete |
| `/gsd-verify-work [N]` | Manual UAT with auto-diagnosis | After execution |
| `/gsd-ship [N]` | Create PR from verified work | After verification |
| `/gsd-fast <text>` | Inline trivial tasks | Typo fixes, config changes |
| `/gsd-next` | Auto-detect state and run next step | Anytime |
| `/gsd-ui-review [N]` | Retroactive 6-pillar visual audit | After execution |
| `/gsd-audit-milestone` | Verify milestone definition of done | Before completing milestone |
| `/gsd-complete-milestone` | Archive milestone, tag release | All phases verified |
| `/gsd-new-milestone [name]` | Start next version cycle | After completing milestone |

## Navigation

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/gsd-progress` | Show status and next steps | "Where am I?" |
| `/gsd-resume-work` | Restore full context from last session | Starting new session |
| `/gsd-pause-work` | Save structured handoff | Stopping mid-phase |
| `/gsd-session-report` | Generate session summary | End of session |
| `/gsd-help` | Show all commands | Quick reference |
| `/gsd-update` | Update GSD with changelog | Check for versions |
| `/gsd-join-discord` | Open Discord invite | Questions |

## Phase Management

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/gsd-add-phase` | Append new phase to roadmap | Scope grows |
| `/gsd-insert-phase [N]` | Insert urgent work (decimal) | Urgent fix mid-milestone |
| `/gsd-remove-phase [N]` | Remove future phase and renumber | Descoping |
| `/gsd-list-phase-assumptions [N]` | Preview Claude's intended approach | Before planning |
| `/gsd-analyze-dependencies` | Detect phase dependencies | Before `/gsd-manager` |
| `/gsd-plan-milestone-gaps` | Create phases for audit gaps | After audit |
| `/gsd-research-phase [N]` | Deep ecosystem research | Complex domain |

## Brownfield & Utilities

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/gsd-map-codebase` | Analyze existing codebase | Before `/gsd-new-project` on existing code |
| `/gsd-scan [--focus area]` | Rapid single-focus scan | Quick assessment |
| `/gsd-intel [query\|status\|diff\|refresh]` | Query codebase intelligence | Look up APIs |
| `/gsd-explore [topic]` | Socratic ideation | Exploring unfamiliar space |
| `/gsd-quick` | Ad-hoc task with GSD guarantees | Bug fixes, small features |
| `/gsd-autonomous` | Run remaining phases autonomously | Hands-free execution |
| `/gsd-undo --last N\|--phase NN\|--plan NN-MM` | Safe git revert | Roll back bad execution |
| `/gsd-import --from <file>` | Ingest external plan | Import plans |
| `/gsd-debug [desc]` | Systematic debugging | Something breaks |
| `/gsd-forensics` | Diagnostic report | State seems corrupted |
| `/gsd-add-todo [desc]` | Capture idea for later | Think of something |
| `/gsd-check-todos` | List pending todos | Review captured ideas |
| `/gsd-settings` | Configure workflow toggles | Change model, toggle agents |
| `/gsd-set-profile <profile>` | Quick profile switch | Change cost/quality |
| `/gsd-reapply-patches` | Restore local modifications | After update |

## Code Quality & Review

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/gsd-review --phase N` | Cross-AI peer review | Before executing |
| `/gsd-code-review <N>` | Review source files for bugs/security | After execution |
| `/gsd-code-review-fix <N>` | Auto-fix issues from code review | After review |
| `/gsd-audit-fix` | Audit-to-fix pipeline | After UAT |
| `/gsd-pr-branch` | Clean PR branch | Before creating PR |
| `/gsd-audit-uat` | Audit verification debt | Before milestone completion |

## Backlog & Threads

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/gsd-add-backlog <desc>` | Add idea to backlog (999.x) | Ideas not ready |
| `/gsd-review-backlog` | Promote/keep/remove backlog items | Before new milestone |
| `/gsd-plant-seed <idea>` | Forward-looking idea with triggers | Ideas for future milestone |
| `/gsd-thread [name]` | Persistent context threads | Cross-session work |

---

# Configuration Reference

GSD stores project settings in `.planning/config.json`. Configure during `/gsd-new-project` or via `/gsd-settings`.

## Full config.json Schema

```json
{
  "mode": "interactive",
  "granularity": "standard",
  "model_profile": "balanced",
  "planning": {
    "commit_docs": true,
    "search_gitignored": false
  },
  "workflow": {
    "research": true,
    "plan_check": true,
    "verifier": true,
    "nyquist_validation": true,
    "ui_phase": true,
    "ui_safety_gate": true,
    "research_before_questions": false,
    "discuss_mode": "standard",
    "skip_discuss": false
  },
  "resolve_model_ids": "anthropic",
  "hooks": {
    "context_warnings": true,
    "workflow_guard": false
  },
  "git": {
    "branching_strategy": "none",
    "phase_branch_template": "gsd/phase-{phase}-{slug}",
    "milestone_branch_template": "gsd/{milestone}-{slug}",
    "quick_branch_template": null
  }
}
```

## Core Settings

| Setting | Options | Default | What it Controls |
|---------|---------|---------|------------------|
| `mode` | `interactive`, `yolo` | `interactive` | `yolo` auto-approves; `interactive` confirms |
| `granularity` | `coarse`, `standard`, `fine` | `standard` | Phase count: 3-5, 5-8, or 8-12 |
| `model_profile` | `quality`, `balanced`, `budget`, `inherit` | `balanced` | Model tier per agent |

## Planning Settings

| Setting | Options | Default | What it Controls |
|---------|---------|---------|------------------|
| `planning.commit_docs` | `true`, `false` | `true` | Whether `.planning/` committed to git |
| `planning.search_gitignored` | `true`, `false` | `false` | Add `--no-ignore` to searches |

> [!note] If `.planning/` is in `.gitignore`, `commit_docs` is automatically `false`.

## Workflow Toggles

| Setting | Options | Default | What it Controls |
|---------|---------|---------|------------------|
| `workflow.research` | `true`, `false` | `true` | Domain investigation before planning |
| `workflow.plan_check` | `true`, `false` | `true` | Plan verification loop (up to 3 iterations) |
| `workflow.verifier` | `true`, `false` | `true` | Post-execution verification |
| `workflow.nyquist_validation` | `true`, `false` | `true` | Nyquist validation architecture |
| `workflow.ui_phase` | `true`, `false` | `true` | UI design contract generation |
| `workflow.ui_safety_gate` | `true`, `false` | `true` | Prompt for ui-phase on frontend phases |
| `workflow.research_before_questions` | `true`, `false` | `false` | Run research before discussion |
| `workflow.discuss_mode` | `standard`, `assumptions` | `standard` | Discussion style |
| `workflow.skip_discuss` | `true`, `false` | `false` | Skip discuss-phase in autonomous mode |
| `response_language` | language code | (none) | Agent response language |

## Hook Settings

| Setting | Options | Default | What it Controls |
|---------|---------|---------|------------------|
| `hooks.context_warnings` | `true`, `false` | `true` | Context window usage warnings |
| `hooks.workflow_guard` | `true`, `false` | `false` | Warn on file edits outside GSD context |

## Git Branching

| Setting | Options | Default | What it Controls |
|---------|---------|---------|------------------|
| `git.branching_strategy` | `none`, `phase`, `milestone` | `none` | When/how branches created |
| `git.phase_branch_template` | Template string | `gsd/phase-{phase}-{slug}` | Branch name for phase strategy |
| `git.milestone_branch_template` | Template string | `gsd/{milestone}-{slug}` | Branch name for milestone strategy |
| `git.quick_branch_template` | Template string or `null` | `null` | Branch name for `/gsd-quick` tasks |

**Branching strategies:**
| Strategy | Creates Branch | Best For |
|----------|---------------|----------|
| `none` | Never | Solo development |
| `phase` | One branch per phase | Code review per phase |
| `milestone` | One branch per milestone | Release branches |

**Template variables:** `{phase}` = zero-padded number (e.g., "03"), `{slug}` = lowercase hyphenated name, `{milestone}` = version (e.g., "v1.0"), `{num}`/`{quick}` = quick task ID

## Model Profiles (Per-Agent)

| Agent | quality | balanced | budget | inherit |
|-------|---------|----------|--------|---------|
| gsd-planner | Opus | Opus | Sonnet | Inherit |
| gsd-roadmapper | Opus | Sonnet | Sonnet | Inherit |
| gsd-executor | Opus | Sonnet | Sonnet | Inherit |
| gsd-phase-researcher | Opus | Sonnet | Haiku | Inherit |
| gsd-project-researcher | Opus | Sonnet | Haiku | Inherit |
| gsd-research-synthesizer | Sonnet | Sonnet | Haiku | Inherit |
| gsd-debugger | Opus | Sonnet | Sonnet | Inherit |
| gsd-codebase-mapper | Sonnet | Haiku | Haiku | Inherit |
| gsd-verifier | Sonnet | Sonnet | Haiku | Inherit |
| gsd-plan-checker | Sonnet | Sonnet | Haiku | Inherit |
| gsd-integration-checker | Sonnet | Sonnet | Haiku | Inherit |

**Profile philosophy:**
- **quality** — Opus for decision-making, Sonnet for verification
- **balanced** — Opus only for planning, Sonnet for everything else (default)
- **budget** — Sonnet for code, Haiku for research/verification
- **inherit** — Use current session model. Best for non-Anthropic providers (OpenRouter, local models)

---

# Usage Examples

## New Project (Full Cycle)

```bash
claude --dangerously-skip-permissions
/gsd-new-project            # Answer questions, configure, approve roadmap
/clear
/gsd-discuss-phase 1        # Lock in preferences
/gsd-ui-phase 1             # Design contract (frontend phases)
/gsd-plan-phase 1           # Research + plan + verify
/gsd-execute-phase 1        # Parallel execution
/gsd-verify-work 1          # Manual UAT
/gsd-ship 1                 # Create PR from verified work
/gsd-ui-review 1            # Visual audit (frontend phases)
/clear
/gsd-next                   # Auto-detect and run next step
...
/gsd-audit-milestone        # Check everything shipped
/gsd-complete-milestone     # Archive, tag, done
/gsd-session-report         # Generate session summary
```

## New Project from Existing Document

```bash
/gsd-new-project --auto @prd.md   # Auto-runs research/requirements/roadmap
/clear
/gsd-discuss-phase 1               # Normal flow from here
```

## Existing Codebase

```bash
/gsd-map-codebase           # Analyze what exists (parallel agents)
/gsd-new-project            # Questions focus on what you're ADDING
```

## Quick Bug Fix

```bash
/gsd-quick
> "Fix the login button not responding on mobile Safari"
```

## Resuming After Break

```bash
/gsd-progress               # See where you left off
/gsd-resume-work            # Full context restoration
```

## Speed vs Quality Presets

| Scenario | Mode | Granularity | Profile | Research | Plan Check | Verifier |
|----------|------|-------|---------|----------|------------|----------|
| Prototyping | `yolo` | `coarse` | `budget` | off | off | off |
| Normal dev | `interactive` | `standard` | `balanced` | on | on | on |
| Production | `interactive` | `fine` | `quality` | on | on | on |

**Skipping discuss-phase:** Set `workflow.skip_discuss: true` via `/gsd-settings` in `yolo` mode with well-established preferences.

## Mid-Milestone Scope Changes

```bash
/gsd-add-phase              # Append new phase
/gsd-insert-phase 3         # Insert urgent work between 3 and 4
/gsd-remove-phase 7         # Descope phase 7 and renumber
```

## Multi-Project Workspaces

```bash
/gsd-new-workspace --name feature-b --repos hr-ui,ZeymoAPI
/gsd-new-workspace --name feature-b --repos .
cd ~/gsd-workspaces/feature-b
/gsd-new-project
/gsd-list-workspaces
/gsd-remove-workspace feature-b
```

Each workspace gets its own `.planning/` directory and git worktrees.

---

# Troubleshooting

## Programmatic CLI (`gsd-sdk query` vs `gsd-tools.cjs`)

Prefer **`gsd-sdk query`** for automation. The legacy **`node $HOME/.claude/get-shit-done/bin/gsd-tools.cjs`** CLI remains supported.

**Not yet on `gsd-sdk query` (use CJS):** `state validate`, `state sync`, `audit-open`, `graphify`, `from-gsd2`

## STATE.md Out of Sync

```bash
node "$HOME/.claude/get-shit-done/bin/gsd-tools.cjs" state validate          # Detect drift
node "$HOME/.claude/get-shit-done/bin/gsd-tools.cjs" state sync --verify     # Preview sync
node "$HOME/.claude/get-shit-done/bin/gsd-tools.cjs" state sync              # Reconstruct from disk
```

New in v1.32.

## Read-Before-Edit Infinite Retry Loop

Some non-Claude runtimes (Cline, Augment Code) may enter infinite retry loops. Add to your `CLAUDE.md`:

```markdown
## Edit Safety Rule
Always read a file before editing it.
```

## Context Degradation During Long Sessions

Clear context with `/clear`. GSD designed around fresh contexts — every subagent gets clean 200K window. Use `/gsd-resume-work` or `/gsd-progress` to restore state.

## Plans Seem Wrong or Misaligned

Run `/gsd-discuss-phase [N]` before planning. Run `/gsd-list-phase-assumptions [N]` to preview Claude's intended approach.

## Execution Fails or Produces Stubs

Plans should have 2-3 tasks maximum. Re-plan with smaller scope if tasks are too large.

## Using Non-Claude Runtimes (Codex, OpenCode, Gemini CLI, Kilo)

Installer sets `resolve_model_ids: "omit"` in config, telling GSD to skip Anthropic model ID resolution. To assign different models:

```json
{
  "resolve_model_ids": "omit",
  "model_overrides": {
    "gsd-planner": "o3",
    "gsd-executor": "o4-mini"
  }
}
```

## Executor Subagent Gets "Permission denied"

Add required patterns to `~/.claude/settings.json`:

**All stacks (git + gh):**
```json
"Bash(git add:*)",
"Bash(git commit:*)",
"Bash(git merge:*)",
"Bash(git worktree:*)",
"Bash(git rebase:*)",
"Bash(git reset:*)",
"Bash(git checkout:*)",
"Bash(git switch:*)",
"Bash(git restore:*)",
"Bash(git stash:*)",
"Bash(git rm:*)",
"Bash(git mv:*)",
"Bash(git fetch:*)",
"Bash(git cherry-pick:*)",
"Bash(git apply:*)",
"Bash(gh:*)"
```

**Rails/Ruby:**
```json
"Bash(bin/rails:*)",
"Bash(bundle:*)",
"Bash(rubocop:*)"
```

**Python/uv:**
```json
"Bash(uv:*)",
"Bash(python:*)",
"Bash(pytest:*)",
"Bash(ruff:*)",
"Bash(mypy:*)"
```

**Node/npm/pnpm/bun:**
```json
"Bash(npm:*)",
"Bash(npx:*)",
"Bash(pnpm:*)",
"Bash(bun:*)",
"Bash(node:*)"
```

**Per-project:** Add to `.claude/settings.local.json` instead of `~/.claude/settings.json`.

## Parallel Execution Causes Build Lock Errors

GSD handles this automatically since v1.26 — parallel agents use `--no-verify` on commits. To disable parallel execution: `/gsd-settings` → set `parallelization.enabled` to `false`.

---

# Recovery Quick Reference

| Problem | Solution |
|---------|----------|
| Lost context / new session | `/gsd-resume-work` or `/gsd-progress` |
| Phase went wrong | `git revert` phase commits, then re-plan |
| Need to change scope | `/gsd-add-phase`, `/gsd-insert-phase`, `/gsd-remove-phase` |
| Milestone audit found gaps | `/gsd-plan-milestone-gaps` |
| Something broke | `/gsd-debug "description"` |
| STATE.md out of sync | `state validate` then `state sync` |
| Workflow state corrupted | `/gsd-forensics` |
| Quick targeted fix | `/gsd-quick` |
| Plan doesn't match vision | `/gsd-discuss-phase [N]` then re-plan |
| Costs running high | `/gsd-set-profile budget` |
| Update broke local changes | `/gsd-reapply-patches` |
| Want session summary | `/gsd-session-report` |
| Don't know next step | `/gsd-next` |
| Parallel execution build errors | Update GSD or set `parallelization.enabled: false` |

---

# Project File Structure

```
.planning/
  PROJECT.md              # Project vision and context
  REQUIREMENTS.md         # Scoped requirements with IDs
  ROADMAP.md              # Phase breakdown with status
  STATE.md                # Decisions, blockers, session memory
  config.json             # Workflow configuration
  MILESTONES.md           # Completed milestone archive
  HANDOFF.json            # Structured session handoff
  research/               # Domain research
  reports/                # Session reports
  todos/
    pending/              # Captured ideas
    done/                 # Completed todos
  debug/                  # Active debug sessions
    resolved/             # Archived debug sessions
  codebase/               # Brownfield codebase mapping
  phases/
    XX-phase-name/
      XX-YY-PLAN.md       # Atomic execution plans
      XX-YY-SUMMARY.md    # Execution outcomes
      CONTEXT.md          # Implementation preferences
      RESEARCH.md         # Ecosystem research
      VERIFICATION.md      # Post-execution verification
      XX-UI-SPEC.md       # UI design contract
      XX-UI-REVIEW.md     # Visual audit scores
  ui-reviews/             # Screenshots (gitignored)
```

#project-management #workflow-automation #system-configuration #software-development #quality-assurance
