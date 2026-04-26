---
title: FEATURES
url: https://github.com/gsd-build/get-shit-done/blob/main/docs/FEATURES.md
source: git
fetched_at: 2026-04-16T16:20:06.436006827-03:00
rendered_js: false
word_count: 13762
summary: Complete feature and function documentation with requirements for the GSD framework across all version iterations.
tags:
    - gsd-framework
    - feature-reference
    - project-management
    - development-workflow
    - automation
    - cli-tools
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# GSD Feature Reference

> [!info] For architecture details, see [Architecture](ARCHITECTURE.md). For command syntax, see [Command Reference](COMMANDS.md).

# Core Features

## 1. Project Initialization

**Command:** `/gsd-new-project [--auto @file.md]`

**Purpose:** Transform an idea into a structured project with research, scoped requirements, and a phased roadmap.

**Requirements:**
- REQ-INIT-01: Adaptive questioning until project scope is fully understood
- REQ-INIT-02: Parallel research agents investigate the domain ecosystem
- REQ-INIT-03: Extract requirements into v1 (must-have), v2 (future), and out-of-scope categories
- REQ-INIT-04: Generate phased roadmap with requirement traceability
- REQ-INIT-05: Require user approval of roadmap before proceeding
- REQ-INIT-06: Prevent re-initialization when `.planning/PROJECT.md` exists
- REQ-INIT-07: Support `--auto @file.md` to skip questions and extract from a document

**Produces:**
| Artifact | Description |
|----------|-------------|
| `PROJECT.md` | Project vision, constraints, technical decisions, evolution rules |
| `REQUIREMENTS.md` | Scoped requirements with unique IDs (REQ-XX) |
| `ROADMAP.md` | Phase breakdown with status tracking and requirement mapping |
| `STATE.md` | Initial project state with position, decisions, metrics |
| `config.json` | Workflow configuration |
| `research/SUMMARY.md` | Synthesized domain research |
| `research/STACK.md` | Technology stack investigation |
| `research/FEATURES.md` | Feature implementation patterns |
| `research/ARCHITECTURE.md` | Architecture patterns and trade-offs |
| `research/PITFALLS.md` | Common failure modes and mitigations |

**Process:** Questions (dream extraction) → 4 parallel researchers → Synthesis → Requirements → Roadmap

> [!note] Granularity setting controls phase count: `coarse` (3-5), `standard` (5-8), `fine` (8-12). Existing codebase context loads automatically if present.

---

## 2. Phase Discussion

**Command:** `/gsd-discuss-phase [N] [--auto] [--batch]`

**Purpose:** Capture implementation preferences and decisions before research and planning. Eliminates gray areas that cause AI to guess.

**Requirements:**
- REQ-DISC-01: Analyze phase scope and identify decision areas (gray areas)
- REQ-DISC-02: Categorize gray areas by type (visual, API, content, organization)
- REQ-DISC-03: Ask only unanswered questions
- REQ-DISC-04: Persist decisions in `{phase}-CONTEXT.md`
- REQ-DISC-05: Support `--auto` flag for recommended defaults
- REQ-DISC-06: Support `--batch` for grouped question intake
- REQ-DISC-07: Scout relevant source files before identifying gray areas
- REQ-DISC-08: Adapt gray area language to product-outcome terms when `USER-PROFILE.md` indicates non-technical owner
- REQ-DISC-09: Rewrite `advisor_research` rationale in plain language when REQ-DISC-08 applies

**Produces:** `{padded_phase}-CONTEXT.md`

**Gray Area Categories:**
| Category | Example Decisions |
|----------|-------------------|
| Visual | Layout, density, interactions, empty states |
| APIs/CLIs | Response format, flags, error handling, verbosity |
| Content | Structure, tone, depth, flow |
| Organization | Grouping criteria, naming, duplicates, exceptions |

---

## 3. UI Design Contract

**Command:** `/gsd-ui-phase [N]`

**Purpose:** Lock design decisions before planning for consistent visual standards across all components in a phase.

**Requirements:**
- REQ-UI-01: Detect existing design system state (shadcn, Tailwind, tokens)
- REQ-UI-02: Ask only unanswered design contract questions
- REQ-UI-03: Validate against 6 dimensions
- REQ-UI-04: Enter revision loop if BLOCKED (max 2 iterations)
- REQ-UI-05: Offer shadcn initialization for React/Next.js/Vite without `components.json`
- REQ-UI-06: Enforce registry safety gate for third-party shadcn registries

**Produces:** `{padded_phase}-UI-SPEC.md`

**6 Validation Dimensions:**
1. **Copywriting** — CTA labels, empty states, error messages
2. **Visuals** — Focal points, visual hierarchy, icon accessibility
3. **Color** — Accent usage discipline, 60/30/10 compliance
4. **Typography** — Font size/weight constraint adherence
5. **Spacing** — Grid alignment, token consistency
6. **Registry Safety** — Third-party component inspection requirements

**shadcn Integration:** Preset string from `ui.shadcn.com/create` becomes a reproducible planning artifact. Safety gate requires `npx shadcn view` and `npx shadcn diff`.

---

## 4. Phase Planning

**Command:** `/gsd-plan-phase [N] [--auto] [--skip-research] [--skip-verify]`

**Purpose:** Research implementation domain and produce verified, atomic execution plans.

**Requirements:**
- REQ-PLAN-01: Spawn phase researcher to investigate implementation approaches
- REQ-PLAN-02: Produce plans with 2-3 tasks each, sized for a single context window
- REQ-PLAN-03: Structure plans as XML with `<task>` elements
- REQ-PLAN-04: Include `read_first` and `acceptance_criteria` in every plan
- REQ-PLAN-05: Run plan checker verification loop (up to 3 iterations)
- REQ-PLAN-06: Support `--skip-research` and `--skip-verify` flags
- REQ-PLAN-07: Prompt for `/gsd-ui-phase` if frontend phase detected without UI-SPEC.md
- REQ-PLAN-08: Include Nyquist validation mapping when enabled
- REQ-PLAN-09: Verify all phase requirements are covered by at least one plan

**Produces:**
| Artifact | Description |
|----------|-------------|
| `{phase}-RESEARCH.md` | Ecosystem research findings |
| `{phase}-{N}-PLAN.md` | Atomic execution plans (2-3 tasks each) |
| `{phase}-VALIDATION.md` | Test coverage mapping (Nyquist layer) |

**Plan Structure (XML):**
```xml
<task type="auto">
  <name>Create login endpoint</name>
  <files>src/app/api/auth/login/route.ts</files>
  <action>Use jose for JWT. Validate credentials against users table. Return httpOnly cookie on success.</action>
  <verify>curl -X POST localhost:3000/api/auth/login returns 200 + Set-Cookie</verify>
  <done>Valid credentials return cookie, invalid return 401</done>
</task>
```

**Plan Checker Verification (8 Dimensions):**
1. Requirement coverage
2. Task atomicity
3. Dependency ordering
4. File scope
5. Verification commands
6. Context fit
7. Gap detection
8. Nyquist compliance (when enabled)

---

## 5. Phase Execution

**Command:** `/gsd-execute-phase <N>`

**Purpose:** Execute all plans using wave-based parallelization with fresh context windows per executor.

**Requirements:**
- REQ-EXEC-01: Analyze plan dependencies and group into waves
- REQ-EXEC-02: Spawn independent plans in parallel within each wave
- REQ-EXEC-03: Give each executor a fresh 200K token context
- REQ-EXEC-04: Produce atomic git commits per task
- REQ-EXEC-05: Produce SUMMARY.md for each completed plan
- REQ-EXEC-06: Run post-execution verifier
- REQ-EXEC-07: Support git branching strategies
- REQ-EXEC-08: Invoke node repair on task verification failure
- REQ-EXEC-09: Run prior phases' test suites to catch cross-phase regressions

**Wave Execution:** Plans with no dependencies → Wave 1 (parallel). Wave 2 waits for Wave 1. Continues until all plans complete.

**Parallel Safety:** Pre-commit hooks skipped by parallel agents (`--no-verify`), run once by orchestrator after each wave. STATE.md locking prevents concurrent write corruption.

---

## 6. Work Verification

**Command:** `/gsd-verify-work [N]`

**Purpose:** User acceptance testing — walk through each deliverable and auto-diagnose failures.

**Requirements:**
- REQ-VERIFY-01: Extract testable deliverables from the phase
- REQ-VERIFY-02: Present deliverables one at a time for confirmation
- REQ-VERIFY-03: Spawn debug agents to diagnose failures
- REQ-VERIFY-04: Create fix plans for identified issues
- REQ-VERIFY-05: Inject cold-start smoke test for phases modifying server/database/seed/startup
- REQ-VERIFY-06: Produce UAT.md with pass/fail results

**Produces:** `{phase}-UAT.md`

---

## 6.5. Ship

**Command:** `/gsd-ship [N] [--draft]`

**Purpose:** Bridge local completion to merged PR. Push branch, create PR with auto-generated body, track in STATE.md.

**Requirements:**
- REQ-SHIP-01: Verify phase passed verification before shipping
- REQ-SHIP-02: Push branch and create PR via `gh` CLI
- REQ-SHIP-03: Auto-generate PR body from SUMMARY.md, VERIFICATION.md, REQUIREMENTS.md
- REQ-SHIP-04: Update STATE.md with shipping status and PR number
- REQ-SHIP-05: Support `--draft` for draft PRs

**Prerequisites:** Phase verified, `gh` CLI installed/authenticated, work on feature branch

---

## 7. UI Review

**Command:** `/gsd-ui-review [N]`

**Purpose:** Retroactive 6-pillar visual audit of implemented frontend code. Works standalone on any project.

**Requirements:**
- REQ-UIREVIEW-01: Score each of 6 pillars on 1-4 scale
- REQ-UIREVIEW-02: Capture screenshots via Playwright CLI to `.planning/ui-reviews/`
- REQ-UIREVIEW-03: Create `.gitignore` for screenshot directory
- REQ-UIREVIEW-04: Identify top 3 priority fixes
- REQ-UIREVIEW-05: Work standalone using abstract quality standards if no UI-SPEC.md exists

**6 Audit Pillars (scored 1-4):**
1. Copywriting — CTA labels, empty states, error states
2. Visuals — Focal points, visual hierarchy, icon accessibility
3. Color — Accent usage discipline, 60/30/10 compliance
4. Typography — Font size/weight constraint adherence
5. Spacing — Grid alignment, token consistency
6. Experience Design — Loading/error/empty state coverage

**Produces:** `{padded_phase}-UI-REVIEW.md`

---

## 8. Milestone Management

**Commands:** `/gsd-audit-milestone`, `/gsd-complete-milestone`, `/gsd-new-milestone [name]`

**Purpose:** Verify completion, archive, tag release, start next development cycle.

**Requirements:**
- REQ-MILE-01: Audit verifies all milestone requirements are met
- REQ-MILE-02: Detect stubs, placeholder implementations, untested code
- REQ-MILE-03: Check Nyquist validation compliance across phases
- REQ-MILE-04: Archive milestone data to MILESTONES.md
- REQ-MILE-05: Offer git tag creation
- REQ-MILE-06: Offer squash merge or merge with history
- REQ-MILE-07: Clean up UI review screenshots
- REQ-MILE-08: New milestone follows same flow as new-project
- REQ-MILE-09: New milestone does NOT reset existing workflow configuration

---

# Planning Features

## 9. Phase Management

**Commands:** `/gsd-add-phase`, `/gsd-insert-phase [N]`, `/gsd-remove-phase [N]`

**Purpose:** Dynamic roadmap modification during development.

**Requirements:**
- REQ-PHASE-01: Add appends new phase to end of roadmap
- REQ-PHASE-02: Insert uses decimal numbering (e.g., 3.1)
- REQ-PHASE-03: Remove renumbers subsequent phases
- REQ-PHASE-04: Remove prevents removing executed phases
- REQ-PHASE-05: All operations update ROADMAP.md and phase directories

---

## 10. Quick Mode

**Command:** `/gsd-quick [--full] [--discuss] [--research]`

**Purpose:** Ad-hoc task execution with GSD guarantees via faster path.

**Requirements:**
- REQ-QUICK-01: Accept freeform task description
- REQ-QUICK-02: Use same planner + executor agents as full workflow
- REQ-QUICK-03: Skip research, plan checker, and verifier by default
- REQ-QUICK-04: `--full` enables plan checking (max 2 iterations) and post-execution verification
- REQ-QUICK-05: `--discuss` runs lightweight pre-planning discussion
- REQ-QUICK-06: `--research` spawns focused research agent
- REQ-QUICK-07: Flags are composable
- REQ-QUICK-08: Track in `.planning/quick/YYMMDD-xxx-slug/`
- REQ-QUICK-09: Produce atomic commits

---

## 11. Autonomous Mode

**Command:** `/gsd-autonomous [--from N]`

**Purpose:** Run all remaining phases autonomously — discuss → plan → execute per phase.

**Requirements:**
- REQ-AUTO-01: Iterate through all incomplete phases in roadmap order
- REQ-AUTO-02: Run discuss → plan → execute for each phase
- REQ-AUTO-03: Pause for explicit user decisions
- REQ-AUTO-04: Re-read ROADMAP.md after each phase
- REQ-AUTO-05: `--from N` starts from specific phase

---

## 12. Freeform Routing

**Command:** `/gsd-do`

**Purpose:** Parse freeform text and route to appropriate GSD command.

**Requirements:**
- REQ-DO-01: Parse user intent from natural language
- REQ-DO-02: Map intent to best matching GSD command
- REQ-DO-03: Confirm routing before executing
- REQ-DO-04: Handle project-exists vs no-project contexts differently

---

## 13. Note Capture

**Command:** `/gsd-note`

**Purpose:** Zero-friction idea capture. Append timestamped notes, list all notes, promote to todos.

**Requirements:**
- REQ-NOTE-01: Save timestamped note files with single Write call
- REQ-NOTE-02: Support `list` subcommand for project and global scopes
- REQ-NOTE-03: Support `promote N` to convert note to structured todo
- REQ-NOTE-04: Support `--global` for global scope
- REQ-NOTE-05: Run inline only — no Task, AskUserQuestion, or Bash

---

## 14. Auto-Advance (Next)

**Command:** `/gsd-next`

**Purpose:** Detect current project state and advance to next logical workflow step.

**Requirements:**
- REQ-NEXT-01: Read STATE.md, ROADMAP.md, phase directories to determine position
- REQ-NEXT-02: Detect whether discuss, plan, execute, or verify is needed
- REQ-NEXT-03: Invoke correct command automatically
- REQ-NEXT-04: Suggest `/gsd-new-project` if no project exists
- REQ-NEXT-05: Suggest `/gsd-complete-milestone` when all phases complete

**State Detection Logic:**
| State | Action |
|-------|--------|
| No `.planning/` | Suggest `/gsd-new-project` |
| Phase has no CONTEXT.md | Run `/gsd-discuss-phase` |
| Phase has no PLAN.md | Run `/gsd-plan-phase` |
| Phase has plans but no SUMMARY.md | Run `/gsd-execute-phase` |
| Phase executed but no VERIFICATION.md | Run `/gsd-verify-work` |
| All phases complete | Suggest `/gsd-complete-milestone` |

---

# Quality Assurance Features

## 15. Nyquist Validation

**Purpose:** Map automated test coverage to phase requirements before code is written. Named after Nyquist sampling theorem — ensures a feedback signal exists for every requirement.

**Requirements:**
- REQ-NYQ-01: Detect existing test infrastructure during plan-phase research
- REQ-NYQ-02: Map each requirement to a specific test command
- REQ-NYQ-03: Identify Wave 0 tasks (test scaffolding)
- REQ-NYQ-04: Plan checker enforces Nyquist compliance as 8th dimension
- REQ-NYQ-05: Support retroactive validation via `/gsd-validate-phase`
- REQ-NYQ-06: Disableable via `workflow.nyquist_validation: false`

**Produces:** `{phase}-VALIDATION.md`

**Retroactive Validation (`/gsd-validate-phase [N]`):**
- Scan implementation, map requirements to tests
- Identify gaps lacking automated verification
- Spawn auditor to generate tests (max 3 attempts)
- Never modifies implementation code — only test files and VALIDATION.md

---

## 16. Plan Checking

**Purpose:** Goal-backward verification that plans will achieve phase objectives before execution.

**Requirements:**
- REQ-PLANCK-01: Verify plans against 8 quality dimensions
- REQ-PLANCK-02: Loop up to 3 iterations until plans pass
- REQ-PLANCK-03: Produce specific, actionable feedback on failures
- REQ-PLANCK-04: Disableable via `workflow.plan_check: false`

---

## 17. Post-Execution Verification

**Purpose:** Automated check that codebase delivers what the phase promised.

**Requirements:**
- REQ-POSTVER-01: Check against phase goals, not just task completion
- REQ-POSTVER-02: Produce VERIFICATION.md with pass/fail analysis
- REQ-POSTVER-03: Log issues for `/gsd-verify-work`
- REQ-POSTVER-04: Disableable via `workflow.verifier: false`

---

## 18. Node Repair

**Purpose:** Autonomous recovery when task verification fails during execution.

**Requirements:**
- REQ-REPAIR-01: Analyze failure, choose strategy: RETRY, DECOMPOSE, or PRUNE
- REQ-REPAIR-02: RETRY attempts with concrete adjustment
- REQ-REPAIR-03: DECOMPOSE breaks task into smaller verifiable sub-steps
- REQ-REPAIR-04: PRUNE removes unachievable tasks and escalates
- REQ-REPAIR-05: Respect repair budget (default: 2 attempts per task)
- REQ-REPAIR-06: Configurable via `workflow.node_repair_budget` and `workflow.node_repair`

---

## 19. Health Validation

**Command:** `/gsd-health [--repair]`

**Purpose:** Validate `.planning/` directory integrity and auto-repair issues.

**Requirements:**
- REQ-HEALTH-01: Check for missing required files
- REQ-HEALTH-02: Validate configuration consistency
- REQ-HEALTH-03: Detect orphaned plans without summaries
- REQ-HEALTH-04: Check phase numbering and roadmap sync
- REQ-HEALTH-05: `--repair` auto-fixes recoverable issues

---

## 20. Cross-Phase Regression Gate

**Purpose:** Run prior phases' test suites after execution to prevent regressions from compounding.

**Requirements:**
- REQ-REGR-01: Run test suites from all completed prior phases
- REQ-REGR-02: Report test failures as cross-phase regressions
- REQ-REGR-03: Surface regressions before post-execution verification
- REQ-REGR-04: Identify which prior phase's tests were broken

**When:** Runs automatically during `/gsd-execute-phase` before verifier step.

---

## 21. Requirements Coverage Gate

**Purpose:** Ensure all phase requirements are covered by at least one plan before planning completes.

**Requirements:**
- REQ-COVGATE-01: Extract all requirement IDs from ROADMAP.md
- REQ-COVGATE-02: Verify each requirement appears in at least one PLAN.md
- REQ-COVGATE-03: Uncovered requirements block planning completion
- REQ-COVGATE-04: Report which specific requirements lack coverage

**When:** Runs automatically at end of `/gsd-plan-phase`.

---

# Context Engineering Features

## 22. Context Window Monitoring

**Purpose:** Prevent context rot by alerting when context is running low.

**Requirements:**
- REQ-CTX-01: Statusline displays context usage percentage
- REQ-CTX-02: Inject warnings at ≤35% remaining (WARNING)
- REQ-CTX-03: Inject warnings at ≤25% remaining (CRITICAL)
- REQ-CTX-04: Warnings debounce (5 tool uses between repeats)
- REQ-CTX-05: Severity escalation bypasses debounce
- REQ-CTX-06: Differentiate GSD-active vs non-GSD-active projects
- REQ-CTX-07: Warnings advisory only, never imperative
- REQ-CTX-08: All hooks fail silently

---

## 23. Session Management

**Commands:** `/gsd-pause-work`, `/gsd-resume-work`, `/gsd-progress`

**Purpose:** Maintain project continuity across context resets and sessions.

**Requirements:**
- REQ-SESSION-01: Pause saves to `continue-here.md` and `HANDOFF.json`
- REQ-SESSION-02: Resume restores from HANDOFF.json (preferred) or state files
- REQ-SESSION-03: Progress shows position, next action, completion
- REQ-SESSION-04: Progress reads all state files
- REQ-SESSION-05: All operations work after `/clear`
- REQ-SESSION-06: HANDOFF.json includes blockers, pending human actions, in-progress state
- REQ-SESSION-07: Resume surfaces human actions/blockers immediately

---

## 24. Session Reporting

**Command:** `/gsd-session-report`

**Purpose:** Generate structured post-session summary capturing work, outcomes, resource usage.

**Requirements:**
- REQ-REPORT-01: Gather data from STATE.md, git log, plan/summary files
- REQ-REPORT-02: Include commits, plans executed, phases progressed
- REQ-REPORT-03: Estimate token usage and cost
- REQ-REPORT-04: Include active blockers and decisions
- REQ-REPORT-05: Recommend next steps

**Produces:** `.planning/reports/SESSION_REPORT.md`

---

## 25. Multi-Agent Orchestration

**Purpose:** Coordinate specialized agents with fresh context windows for each task.

**Requirements:**
- REQ-ORCH-01: Each agent receives fresh context window
- REQ-ORCH-02: Orchestrators are thin (spawn, collect, route)
- REQ-ORCH-03: Context payload includes all relevant project artifacts
- REQ-ORCH-04: Parallel agents are truly independent
- REQ-ORCH-05: Agent results written to disk before orchestrator processes
- REQ-ORCH-06: Detect failed agents via spot-check

---

## 26. Model Profiles

**Command:** `/gsd-set-profile <quality|balanced|budget|inherit>`

**Purpose:** Control which AI model each agent uses, balancing quality vs cost.

**Requirements:**
- REQ-MODEL-01: Support 4 profiles: `quality`, `balanced`, `budget`, `inherit`
- REQ-MODEL-02: Each profile defines model tier per agent
- REQ-MODEL-03: Per-agent overrides take precedence
- REQ-MODEL-04: `inherit` defers to runtime's current model
- REQ-MODEL-04a: `inherit` required for non-Anthropic providers
- REQ-MODEL-05: Profile switch is programmatic
- REQ-MODEL-06: Model resolution happens once per orchestration

**Profile Assignments:**
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
| gsd-nyquist-auditor | Sonnet | Sonnet | Haiku | Inherit |

---

# Brownfield Features

## 27. Codebase Mapping

**Command:** `/gsd-map-codebase [area]`

**Purpose:** Analyze existing codebase before starting new project.

**Requirements:**
- REQ-MAP-01: Spawn parallel mapper agents
- REQ-MAP-02: Produce structured documents in `.planning/codebase/`
- REQ-MAP-03: Detect: stack, architecture, conventions, concerns
- REQ-MAP-04: Subsequent `/gsd-new-project` loads mapping and focuses on what's being added
- REQ-MAP-05: Optional `[area]` argument scopes mapping

**Produces:**
| Document | Content |
|----------|---------|
| `STACK.md` | Languages, frameworks, databases, infrastructure |
| `ARCHITECTURE.md` | Patterns, layers, data flow, boundaries |
| `CONVENTIONS.md` | Naming, file organization, code style, testing |
| `CONCERNS.md` | Technical debt, security issues, performance |
| `STRUCTURE.md` | Directory layout and file organization |
| `TESTING.md` | Test infrastructure, coverage, patterns |
| `INTEGRATIONS.md` | External services, APIs, third-party deps |

---

# Utility Features

## 28. Debug System

**Command:** `/gsd-debug [description]`

**Purpose:** Systematic debugging with persistent state across context resets.

**Requirements:**
- REQ-DEBUG-01: Create debug session file in `.planning/debug/`
- REQ-DEBUG-02: Track hypotheses, evidence, eliminated theories
- REQ-DEBUG-03: Persist state across context resets
- REQ-DEBUG-04: Require human verification before marking resolved
- REQ-DEBUG-05: Resolved sessions append to `.planning/debug/knowledge-base.md`
- REQ-DEBUG-06: Knowledge base consulted on new sessions

**Debug Session States:** `gathering` → `investigating` → `fixing` → `verifying` → `awaiting_human_verify` → `resolved`

---

## 29. Todo Management

**Commands:** `/gsd-add-todo [desc]`, `/gsd-check-todos`

**Requirements:**
- REQ-TODO-01: Capture todo from current conversation context
- REQ-TODO-02: Store in `.planning/todos/pending/`
- REQ-TODO-03: Completed todos move to `.planning/todos/completed/`
- REQ-TODO-04: Check-todos lists all pending items

---

## 30. Statistics Dashboard

**Command:** `/gsd-stats`

**Purpose:** Display project metrics — phases, plans, requirements, git history.

**Requirements:**
- REQ-STATS-01: Show phase/plan completion counts
- REQ-STATS-02: Show requirement coverage
- REQ-STATS-03: Show git commit metrics
- REQ-STATS-04: Support multiple output formats (json, table, bar)

---

## 31. Update System

**Command:** `/gsd-update`

**Purpose:** Update GSD to latest version with changelog preview.

**Requirements:**
- REQ-UPDATE-01: Check for new versions via npm
- REQ-UPDATE-02: Display changelog before updating
- REQ-UPDATE-03: Be runtime-aware
- REQ-UPDATE-04: Back up locally modified files to `gsd-local-patches/`
- REQ-UPDATE-05: `/gsd-reapply-patches` restores local modifications

---

## 32. Settings Management

**Command:** `/gsd-settings`

**Purpose:** Interactive configuration of workflow toggles and model profile.

**Requirements:**
- REQ-SETTINGS-01: Present current settings with toggle options
- REQ-SETTINGS-02: Update `.planning/config.json`
- REQ-SETTINGS-03: Support saving as global defaults (`~/.gsd/defaults.json`)

**Configurable Settings:**
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `mode` | enum | `interactive` | `interactive` or `yolo` |
| `granularity` | enum | `standard` | `coarse`, `standard`, or `fine` |
| `model_profile` | enum | `balanced` | `quality`, `balanced`, `budget`, `inherit` |
| `workflow.research` | boolean | `true` | Domain research before planning |
| `workflow.plan_check` | boolean | `true` | Plan verification loop |
| `workflow.verifier` | boolean | `true` | Post-execution verification |
| `workflow.nyquist_validation` | boolean | `true` | Nyquist test coverage mapping |
| `workflow.ui_phase` | boolean | `true` | UI design contract generation |
| `workflow.ui_safety_gate` | boolean | `true` | Prompt for ui-phase on frontend phases |
| `workflow.node_repair` | boolean | `true` | Autonomous task repair |
| `workflow.node_repair_budget` | number | `2` | Max repair attempts |
| `planning.commit_docs` | boolean | `true` | Commit `.planning/` to git |
| `parallelization.enabled` | boolean | `true` | Run independent plans simultaneously |
| `git.branching_strategy` | enum | `none` | `none`, `phase`, or `milestone` |

---

## 33. Test Generation

**Command:** `/gsd-add-tests [N]`

**Purpose:** Generate tests for completed phase based on UAT criteria and implementation.

**Requirements:**
- REQ-TEST-01: Analyze completed phase implementation
- REQ-TEST-02: Generate tests based on UAT and acceptance criteria
- REQ-TEST-03: Use existing test infrastructure patterns

---

# Infrastructure Features

## 34. Git Integration

**Purpose:** Atomic commits, branching strategies, clean history management.

**Requirements:**
- REQ-GIT-01: Each task gets its own atomic commit
- REQ-GIT-02: Commit messages follow `type(scope): description` format
- REQ-GIT-03: Support 3 branching strategies: `none`, `phase`, `milestone`
- REQ-GIT-04: Phase strategy creates one branch per phase
- REQ-GIT-05: Milestone strategy creates one branch per milestone
- REQ-GIT-06: Complete-milestone offers squash merge
- REQ-GIT-07: Respect `commit_docs` setting for `.planning/`
- REQ-GIT-08: Auto-detect `.planning/` in `.gitignore`

---

## 35. CLI Tools

**Purpose:** Programmatic utilities for workflows and agents.

**Requirements:**
- REQ-CLI-01: Provide atomic commands for state, config, phase, roadmap operations
- REQ-CLI-02: Provide compound `init` commands
- REQ-CLI-03: Support `--raw` for machine-readable output
- REQ-CLI-04: Support `--cwd` for sandboxed subagent operation
- REQ-CLI-05: Use forward-slash paths on Windows

**Command Categories:** State (11 subcommands), Phase (5), Roadmap (3), Verify (8), Template (2), Frontmatter (4), Scaffold (4), Init (12), Validate (2), Progress, Stats, Todo

---

## 36. Multi-Runtime Support

**Purpose:** Run GSD across multiple AI coding agent runtimes.

**Requirements:**
- REQ-RUNTIME-01: Support Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Antigravity, Trae, Cline, Augment Code, CodeBuddy, Qwen Code
- REQ-RUNTIME-02: Installer transforms content per runtime
- REQ-RUNTIME-03: Support interactive and non-interactive modes
- REQ-RUNTIME-04: Support both global and local installation
- REQ-RUNTIME-05: Uninstall cleanly removes all GSD files
- REQ-RUNTIME-06: Handle platform differences

---

## 37. Hook System

**Purpose:** Runtime event hooks for context monitoring, status display, update checking.

**Requirements:**
- REQ-HOOK-01: Statusline displays model, task, directory, context usage
- REQ-HOOK-02: Context monitor injects warnings at thresholds
- REQ-HOOK-03: Update checker runs in background on session start
- REQ-HOOK-04: All hooks respect `CLAUDE_CONFIG_DIR` env var
- REQ-HOOK-05: Include 3-second stdin timeout guard
- REQ-HOOK-06: Fail silently on any error
- REQ-HOOK-07: Context usage normalized for autocompact buffer

**Statusline:** `[⬆ /gsd-update │] model │ [current task │] directory [█████░░░░░ 50%]`

Color coding: <50% green, <65% yellow, <80% orange, ≥80% red with skull emoji

---

## 38. Developer Profiling

**Command:** `/gsd-profile-user [--questionnaire] [--refresh]`

**Purpose:** Analyze session history to build behavioral profiles across 8 dimensions.

**Dimensions:**
1. Communication style (terse vs verbose)
2. Decision patterns (rapid vs deliberate)
3. Debugging approach (systematic vs intuitive)
4. UX preferences (design sensibility)
5. Vendor/technology choices (framework preferences)
6. Frustration triggers (what causes friction)
7. Learning style (documentation vs examples)
8. Explanation depth (high-level vs implementation detail)

**Generated Artifacts:**
- `USER-PROFILE.md` — Full behavioral profile
- `/gsd-dev-preferences` command
- `CLAUDE.md` profile section

---

## 39. Execution Hardening

**Purpose:** Three additive quality improvements catching cross-plan failures before cascade.

**Components:**

**1. Pre-Wave Dependency Check** — Before spawning wave N+1, verify key-links from prior wave artifacts exist.

**2. Cross-Plan Data Contracts (Dimension 9)** — Check plans sharing data pipelines have compatible transformations.

**3. Export-Level Spot Check** — Spot-check individual exports for actual usage after wiring verification.

**Requirements:**
- REQ-HARD-01: Pre-wave check verifies key-links from all prior wave artifacts
- REQ-HARD-02: Cross-plan contract check detects incompatible data transformations
- REQ-HARD-03: Export spot-check identifies dead stores in wired files

---

## 40. Verification Debt Tracking

**Command:** `/gsd-audit-uat`

**Purpose:** Surface verification debt across all prior phases so items are never forgotten.

**Components:**
1. **Cross-Phase Health Check** — Every `/gsd-progress` scans all phases for outstanding items
2. **`status: partial`** — Distinguishes "session ended" from "all tests resolved"
3. **`result: blocked` with `blocked_by`** — For tests blocked by external dependencies
4. **HUMAN-UAT.md Persistence** — Items with `human_needed` persisted as trackable file
5. **Phase Completion Warnings** — CLI returns verification debt warnings

**Requirements:**
- REQ-DEBT-01: Surface outstanding UAT items from ALL prior phases in `/gsd-progress`
- REQ-DEBT-02: Distinguish incomplete (partial) from completed (complete)
- REQ-DEBT-03: Categorize blocked tests with `blocked_by` tags
- REQ-DEBT-04: Persist human_needed items as trackable UAT files
- REQ-DEBT-05: Warn during phase completion when verification debt exists
- REQ-DEBT-06: `/gsd-audit-uat` produces human test plan

---

# v1.27 Features

## 41. Fast Mode

**Command:** `/gsd-fast [task description]`

**Purpose:** Execute trivial tasks inline without spawning subagents or generating PLAN.md files.

**Requirements:**
- REQ-FAST-01: Execute directly in current context without subagents
- REQ-FAST-02: Produce atomic git commit
- REQ-FAST-03: Track in `.planning/quick/` for state consistency
- REQ-FAST-04: NOT for tasks requiring research, multi-step planning, or verification

**When to use:**
- `/gsd-fast` — One-sentence tasks under 2 minutes (typo, config change, small addition)
- `/gsd-quick` — Anything needing research, multi-step planning, or verification

---

## 42. Cross-AI Peer Review

**Command:** `/gsd-review --phase N [--gemini] [--claude] [--codex] [--coderabbit] [--opencode] [--qwen] [--cursor] [--all]`

**Purpose:** Invoke external AI CLIs to independently review phase plans.

**Requirements:**
- REQ-REVIEW-01: Detect available AI CLIs on system
- REQ-REVIEW-02: Build structured review prompt from phase plans
- REQ-REVIEW-03: Invoke each selected CLI independently
- REQ-REVIEW-04: Collect responses and produce `REVIEWS.md`
- REQ-REVIEW-05: Reviews consumable by `/gsd-plan-phase --reviews`

**Produces:** `{phase}-REVIEWS.md`

---

## 43. Backlog Parking Lot

**Commands:** `/gsd-add-backlog <description>`, `/gsd-review-backlog`, `/gsd-plant-seed <idea>`

**Purpose:** Capture ideas not ready for active planning. Backlog uses 999.x numbering. Seeds are forward-looking with trigger conditions.

**Requirements:**
- REQ-BACKLOG-01: Backlog items use 999.x numbering
- REQ-BACKLOG-02: Phase directories created immediately
- REQ-BACKLOG-03: `/gsd-review-backlog` supports promote, keep, remove
- REQ-BACKLOG-04: Promoted items renumbered into active sequence
- REQ-SEED-01: Seeds capture full WHY and WHEN
- REQ-SEED-02: `/gsd-new-milestone` scans seeds and presents matches

**Produces:**
| Artifact | Description |
|----------|-------------|
| `.planning/phases/999.x-slug/` | Backlog item directory |
| `.planning/seeds/SEED-NNN-slug.md` | Seed with trigger conditions |

---

## 44. Persistent Context Threads

**Command:** `/gsd-thread [name | description]`

**Purpose:** Lightweight cross-session knowledge stores. Lighter than `/gsd-pause-work`.

**Requirements:**
- REQ-THREAD-01: Support create, list, resume modes
- REQ-THREAD-02: Store in `.planning/threads/` as markdown
- REQ-THREAD-03: Thread files include Goal, Context, References, Next Steps
- REQ-THREAD-04: Resume loads full context
- REQ-THREAD-05: Promotable to phases or backlog items

**Produces:** `.planning/threads/{slug}.md`

---

## 45. PR Branch Filtering

**Command:** `/gsd-pr-branch [target branch]`

**Purpose:** Create clean branch for PRs by filtering out `.planning/` commits.

**Requirements:**
- REQ-PRBRANCH-01: Identify commits only modifying `.planning/` files
- REQ-PRBRANCH-02: Create new branch with planning commits filtered out
- REQ-PRBRANCH-03: Code changes preserved exactly

---

## 46. Security Hardening

**Purpose:** Defense-in-depth for GSD's planning artifacts against prompt injection.

**Components:**

**1. Centralized Security Module** (`security.cjs`):
- Path traversal prevention
- Prompt injection detection
- Safe JSON parsing
- Field name validation
- Shell argument validation

**2. Prompt Injection Guard Hook** (`gsd-prompt-guard.js`) — Scans Write/Edit calls to `.planning/` for injection patterns (advisory-only).

**3. Workflow Guard Hook** (`gsd-workflow-guard.js`) — Detects file edits outside GSD workflow context.

**4. CI-Ready Injection Scanner** (`prompt-injection-scan.test.cjs`)

**Requirements:**
- REQ-SEC-01: Validate all user-supplied file paths against project directory
- REQ-SEC-02: Detect prompt injection patterns before text enters artifacts
- REQ-SEC-03: Security hooks advisory-only
- REQ-SEC-04: JSON parsing catches malformed data gracefully
- REQ-SEC-05: Handle macOS `/var` → `/private/var` symlink resolution

---

## 47. Multi-Repo Workspace Support

**Purpose:** Auto-detection and project root resolution for monorepos.

**Requirements:**
- REQ-MULTIREPO-01: Auto-detect multi-repo workspace configuration
- REQ-MULTIREPO-02: Resolve project root across repository boundaries
- REQ-MULTIREPO-03: Record per-repo commit hashes in multi-repo mode

---

## 48. Discussion Audit Trail

**Purpose:** Auto-generate `DISCUSSION-LOG.md` during `/gsd-discuss-phase`.

**Requirements:**
- REQ-DISCLOG-01: Auto-generate DISCUSSION-LOG.md during discuss-phase
- REQ-DISCLOG-02: Log captures questions, options, decisions
- REQ-DISCLOG-03: Decision IDs enable traceability from discuss to plan phase

---

# v1.28 Features

## 49. Forensics

**Command:** `/gsd-forensics [description]`

**Purpose:** Post-mortem investigation of failed or stuck GSD workflows.

**Requirements:**
- REQ-FORENSICS-01: Analyze git history for anomalies
- REQ-FORENSICS-02: Check artifact integrity
- REQ-FORENSICS-03: Generate markdown report to `.planning/forensics/`
- REQ-FORENSICS-04: Offer to create GitHub issue with findings
- REQ-FORENSICS-05: Read-only investigation

**Produces:** `.planning/forensics/report-{timestamp}.md`

---

## 50. Milestone Summary

**Command:** `/gsd-milestone-summary [version]`

**Purpose:** Generate comprehensive project summary for team onboarding.

**Requirements:**
- REQ-SUMMARY-01: Aggregate phase plans, summaries, verification results
- REQ-SUMMARY-02: Work for current and archived milestones
- REQ-SUMMARY-03: Produce single navigable document

**Produces:** `MILESTONE-SUMMARY.md`

---

## 51. Workstream Namespacing

**Command:** `/gsd-workstreams`

**Purpose:** Parallel workstreams for concurrent work on different milestone areas.

**Requirements:**
- REQ-WS-01: Isolate workstream state in `.planning/workstreams/{name}/`
- REQ-WS-02: Validate workstream names (alphanumeric + hyphens only)
- REQ-WS-03: Support list, create, switch, status, progress, complete, resume

---

## 52. Manager Dashboard

**Command:** `/gsd-manager`

**Purpose:** Interactive command center for managing multiple phases.

**Requirements:**
- REQ-MGR-01: Show overview of all phases with status
- REQ-MGR-02: Filter to current milestone scope
- REQ-MGR-03: Show phase dependencies and conflicts

---

## 53. Assumptions Discussion Mode

**Command:** `/gsd-discuss-phase` with `workflow.discuss_mode: 'assumptions'`

**Purpose:** Replace interview-style questioning with codebase-first assumption analysis.

**Requirements:**
- REQ-ASSUME-01: Analyze codebase to generate structured assumptions
- REQ-ASSUME-02: Classify assumptions by confidence (Confident/Likely/Unclear)
- REQ-ASSUME-03: Produce identical CONTEXT.md format as default mode
- REQ-ASSUME-04: Support confidence-based skip gate (all HIGH = no questions)

---

## 54. UI Phase Auto-Detection

**Purpose:** Detect UI-heavy projects and surface `/gsd-ui-phase` recommendation.

**Requirements:**
- REQ-UI-DETECT-01: Detect UI signals in project description
- REQ-UI-DETECT-02: Annotate ROADMAP.md phases with `ui_hint`
- REQ-UI-DETECT-03: Suggest `/gsd-ui-phase` in next steps for UI-heavy phases
- REQ-UI-DETECT-04: NOT mandatory

---

## 55. Multi-Runtime Installer Selection

**Purpose:** Select multiple runtimes in single interactive install session.

**Requirements:**
- REQ-MULTI-RT-01: Interactive prompt supports multi-select
- REQ-MULTI-RT-02: CLI flags continue to work for non-interactive installs

---

# v1.29 Features

## 56. Windsurf Runtime Support

**Purpose:** Add Windsurf as supported AI CLI runtime.

**Requirements:**
- REQ-WINDSURF-01: Detect Windsurf runtime and offer as target
- REQ-WINDSURF-02: GSD commands function correctly within Windsurf sessions

---

## 57. Internationalized Documentation

**Purpose:** Provide GSD documentation in Portuguese, Korean, Japanese.

**Requirements:**
- REQ-I18N-01: Available in Portuguese (pt), Korean (ko), Japanese (ja)
- REQ-I18N-02: Stay synchronized with English source

---

# v1.30 Features

## 58. GSD SDK

**Command:** Programmatic API (headless)

**Purpose:** Run GSD workflows programmatically without CLI session.

**Requirements:**
- REQ-SDK-01: Expose GSD workflow operations as TypeScript functions
- REQ-SDK-02: Support headless execution without interactive prompts
- REQ-SDK-03: Produce same artifacts as CLI-driven workflows

---

# v1.31 Features

## 59. Schema Drift Detection

**Purpose:** Detect when ORM schema files modified without migration, preventing false-positive verification.

**Requirements:**
- REQ-SCHEMA-01: Detect modifications to ORM schema files (Prisma, Drizzle, Payload, Sanity, Mongoose)
- REQ-SCHEMA-02: Verify corresponding migration/push commands exist
- REQ-SCHEMA-03: Implement two-layer defense: plan-time injection and execute-time gate
- REQ-SCHEMA-04: Support `GSD_SKIP_SCHEMA_CHECK` env var
- REQ-SCHEMA-05: Prevent false-positive verification

**Config:** `GSD_SKIP_SCHEMA_CHECK`

---

## 60. Security Enforcement

**Command:** `/gsd-secure-phase <N>`

**Purpose:** Threat-model-anchored security verification.

**Requirements:**
- REQ-SEC-01: Perform threat-model-anchored verification
- REQ-SEC-02: Support configurable OWASP ASVS verification levels (1-3)
- REQ-SEC-03: Block phase advancement based on severity threshold
- REQ-SEC-04: Spawn `gsd-security-auditor` agent

**Config:**
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `security_enforcement` | boolean | `true` | Enable threat-model security verification |
| `security_asvs_level` | number | `1` | OWASP ASVS verification level (1-3) |
| `security_block_on` | string | `"high"` | Minimum severity to block |

---

## 61. Documentation Generation

**Command:** `/gsd-docs-update`

**Purpose:** Generate and verify project documentation.

**Requirements:**
- REQ-DOCS-01: Spawn `gsd-doc-writer` agent to generate documentation
- REQ-DOCS-02: Spawn `gsd-doc-verifier` agent to check accuracy
- REQ-DOCS-03: Verify generated documentation against actual implementation

---

## 62. Discuss Chain Mode

**Flag:** `/gsd-discuss-phase <N> --chain`

**Purpose:** Auto-chain discuss, plan, execute to reduce manual sequencing.

**Requirements:**
- REQ-CHAIN-01: Auto-chain discuss → plan → execute when `--chain` provided
- REQ-CHAIN-02: Respect all gate settings between chained phases
- REQ-CHAIN-03: Halt chain if any phase fails

---

## 63. Single-Phase Autonomous

**Flag:** `/gsd-autonomous --only N`

**Purpose:** Execute just one phase autonomously.

**Requirements:**
- REQ-ONLY-01: Execute only specified phase number with `--only N`
- REQ-ONLY-02: Follow same discuss → plan → execute flow
- REQ-ONLY-03: Stop after specified phase completes

---

## 64. Scope Reduction Detection

**Purpose:** Prevent silent requirement dropping during plan generation.

**Requirements:**
- REQ-SCOPE-01: Prohibit planners from reducing scope without explicit justification
- REQ-SCOPE-02: Plan-checker verifies requirement dimension coverage
- REQ-SCOPE-03: Orchestrator recovers dropped requirements
- REQ-SCOPE-04: Three-layer defense: planner prohibition, checker dimension, orchestrator recovery

---

## 65. Claim Provenance Tagging

**Purpose:** Ensure research claims tagged with source evidence; assumptions logged separately.

**Requirements:**
- REQ-PROVENANCE-01: Mark claims with source evidence references
- REQ-PROVENANCE-02: Log assumptions separately from sourced claims
- REQ-PROVENANCE-03: Distinguish evidenced facts from inferred assumptions

---

## 66. Worktree Toggle

**Config:** `workflow.use_worktrees: false`

**Purpose:** Disable git worktree isolation for users preferring sequential execution.

**Requirements:**
- REQ-WORKTREE-01: Respect `workflow.use_worktrees` setting
- REQ-WORKTREE-02: Default to `true` (worktrees enabled)
- REQ-WORKTREE-03: Fall back to sequential execution when disabled

---

## 67. Project Code Prefixing

**Config:** `project_code: "ABC"`

**Purpose:** Prefix phase directory names with project code for multi-project disambiguation.

**Requirements:**
- REQ-PREFIX-01: Prefix phase directories when configured (e.g., `ABC-01-setup/`)
- REQ-PREFIX-02: Use standard naming when not set
- REQ-PREFIX-03: Apply prefix consistently across all operations

---

## 68. Claude Code Skills Migration

**Purpose:** Migrate GSD commands to Claude Code 2.1.88+ skills format with backward compatibility.

**Requirements:**
- REQ-SKILLS-01: Write `skills/gsd-*/SKILL.md` for Claude Code 2.1.88+
- REQ-SKILLS-02: Auto-clean legacy `commands/gsd/` directory
- REQ-SKILLS-03: Maintain backward compatibility via Gemini path

---

# v1.32 Features

## 69. STATE.md Consistency Gates

**Commands:** `state validate`, `state sync [--verify]`, `state planned-phase --phase N --plans N`

**Purpose:** Detect and repair drift between STATE.md and filesystem.

**Requirements:**
- REQ-STATE-01: `state validate` detects drift
- REQ-STATE-02: `state sync` reconstructs STATE.md from disk
- REQ-STATE-03: `state sync --verify` performs dry-run
- REQ-STATE-04: `state planned-phase` records post-plan-phase state transition

---

## 70. Autonomous `--to N` Flag

**Flag:** `/gsd-autonomous --to N`

**Purpose:** Stop autonomous execution after completing specific phase.

**Requirements:**
- REQ-TO-01: Stop after specified phase number completes
- REQ-TO-02: Follow same discuss → plan → execute flow
- REQ-TO-03: Combinable with `--from N`

---

## 71. Research Gate

**Purpose:** Block planning when RESEARCH.md has unresolved open questions.

**Requirements:**
- REQ-RESGATE-01: Scan RESEARCH.md for unresolved open questions
- REQ-RESGATE-02: Block plan-phase entry when open questions exist
- REQ-RESGATE-03: Surface specific unresolved questions

---

## 72. Verifier Milestone Scope Filtering

**Purpose:** Distinguish genuine gaps from items deferred to later phases.

**Requirements:**
- REQ-VSCOPE-01: Check whether gap addressed in later milestone phase
- REQ-VSCOPE-02: Mark deferred items separately from genuine gaps
- REQ-VSCOPE-03: Only genuine gaps reported as failures

---

## 73. Read-Before-Edit Guard Hook

**Purpose:** Prevent infinite retry loops by ensuring files read before editing.

**Requirements:**
- REQ-RBE-01: Detect Edit/Write calls to unread files
- REQ-RBE-02: Advise reading file first (advisory)
- REQ-RBE-03: Prevent infinite retry loops

---

## 74. Context Reduction

**Purpose:** Reduce context prompt sizes through markdown truncation.

**Requirements:**
- REQ-CTXRED-01: Truncate oversized markdown artifacts
- REQ-CTXRED-02: Order prompts for cache-friendly assembly
- REQ-CTXRED-03: Preserve essential information (headings, requirements, task structure)

---

## 75. Discuss-Phase `--power` Flag

**Flag:** `/gsd-discuss-phase --power`

**Purpose:** File-based bulk question answering for discuss-phase.

**Requirements:**
- REQ-POWER-01: Accept file containing pre-written answers
- REQ-POWER-02: Map answers to corresponding gray area questions
- REQ-POWER-03: Produce identical CONTEXT.md

---

## 76. Debug `--diagnose` Flag

**Flag:** `/gsd-debug --diagnose`

**Purpose:** Diagnosis-only mode that investigates without attempting fixes.

**Requirements:**
- REQ-DIAG-01: Perform full debug investigation
- REQ-DIAG-02: NOT attempt any code modifications
- REQ-DIAG-03: Produce diagnostic report with findings

---

## 77. Phase Dependency Analysis

**Command:** `/gsd-analyze-dependencies`

**Purpose:** Detect phase dependencies and suggest `Depends on` entries for ROADMAP.md.

**Requirements:**
- REQ-DEP-01: Detect file overlap between phases
- REQ-DEP-02: Detect semantic dependencies (API/schema producers/consumers)
- REQ-DEP-03: Detect data flow dependencies
- REQ-DEP-04: Suggest entries with user confirmation

---

## 78. Anti-Pattern Severity Levels

**Purpose:** Mandatory understanding checks at resume with severity-based enforcement.

**Requirements:**
- REQ-ANTI-01: Classify anti-patterns by severity
- REQ-ANTI-02: Enforce mandatory understanding checks at session resume
- REQ-ANTI-03: Higher severity blocks workflow progression

---

## 79. Methodology Artifact Type

**Purpose:** Define consumption mechanisms for methodology documents.

**Requirements:**
- REQ-METHOD-01: Support methodology as distinct artifact type
- REQ-METHOD-02: Methodology artifacts have defined consumption mechanisms

---

## 80. Planner Reachability Check

**Purpose:** Validate plan steps reference reachable files and APIs before committing.

**Requirements:**
- REQ-REACH-01: Validate each plan step references reachable files/APIs
- REQ-REACH-02: Flag unreachable steps during planning

---

## 81. Playwright-MCP UI Verification

**Purpose:** Automated visual verification using Playwright-MCP during verify-phase.

**Requirements:**
- REQ-PLAY-01: Support optional Playwright-MCP visual verification
- REQ-PLAY-02: Opt-in, not mandatory
- REQ-PLAY-03: Capture and compare visual state against UI-SPEC.md

---

## 82. Pause-Work Expansion

**Purpose:** Support non-phase contexts with richer handoff data.

**Requirements:**
- REQ-PAUSE-01: Support pausing in non-phase contexts
- REQ-PAUSE-02: Handoff data includes richer context for work type

---

## 83. Response Language Config

**Config:** `response_language`

**Purpose:** Cross-phase language consistency for non-English users.

**Requirements:**
- REQ-LANG-01: Respect `response_language` across all phases and agents
- REQ-LANG-02: Propagate to all spawned agents

---

## 84. Manual Update Procedure

**Purpose:** Document manual update path for environments without npm access.

**Requirements:**
- REQ-MANUAL-01: Describe step-by-step manual update procedure
- REQ-MANUAL-02: Work without npm access

---

## 85. New Runtime Support (Trae, Cline, Augment Code)

**Purpose:** Extend GSD installation to Trae, Cline, Augment Code runtimes.

**Requirements:**
- REQ-TRAE-01: Support `--trae` flag for Trae IDE installation
- REQ-CLINE-01: Support Cline via `.clinerules` configuration
- REQ-AUGMENT-01: Support Augment Code with skill conversion

---

## 86. Autonomous `--interactive` Flag

**Flag:** `/gsd-autonomous --interactive`

**Purpose:** Lean-context autonomous mode keeping discuss-phase interactive while dispatching plan/execute as background agents.

**Requirements:**
- REQ-INTERACT-01: Run discuss-phase inline with user interaction
- REQ-INTERACT-02: Dispatch plan-phase and execute-phase as background agents
- REQ-INTERACT-03: Enable pipeline parallelism
- REQ-INTERACT-04: Main context only accumulates discuss conversations

---

## 87. Commit-Docs Guard Hook

**Hook:** `gsd-commit-docs.js`

**Purpose:** Enforce `commit_docs` configuration, preventing `.planning/` commits when disabled.

**Requirements:**
- REQ-COMMITDOCS-01: Intercept git commit commands staging `.planning/` files
- REQ-COMMITDOCS-02: Block commits containing `.planning/` when `commit_docs` is `false`
- REQ-COMMITDOCS-03: Advisory — does not block when `commit_docs` is `true`

---

## 88. Community Hooks Opt-In

**Hooks:** `gsd-validate-commit.sh`, `gsd-session-state.sh`, `gsd-phase-boundary.sh`

**Purpose:** Optional git and session hooks, gated behind `hooks.community: true`.

**Requirements:**
- REQ-COMMUNITY-01: No-ops unless `hooks.community` is `true`
- REQ-COMMUNITY-02: `gsd-validate-commit.sh` enforces Conventional Commits
- REQ-COMMUNITY-03: `gsd-session-state.sh` tracks session state transitions
- REQ-COMMUNITY-04: `gsd-phase-boundary.sh` enforces phase boundary checks

---

# v1.34.0 Features

## 89. Global Learnings Store

**Purpose:** Persist cross-session, cross-project learnings in global store for planner to learn from patterns.

**Requirements:**
- REQ-LEARN-01: Auto-copy learnings from `.planning/` to global store at phase completion
- REQ-LEARN-02: Planner agent receives relevant learnings at spawn time
- REQ-LEARN-03: Injection capped by `learnings.max_inject`
- REQ-LEARN-04: Opt-in via `features.global_learnings: true`

**Config:**
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `features.global_learnings` | boolean | `false` | Enable cross-project learnings |
| `learnings.max_inject` | number | system default | Maximum learnings entries injected |

---

## 90. Queryable Codebase Intelligence

**Command:** `/gsd-intel [query <term>|status|diff|refresh]`
**Config:** `intel.enabled`

**Purpose:** Maintain queryable JSON index of codebase structure, API surface, dependency graph in `.planning/intel/`.

**Requirements:**
- REQ-INTEL-01: Intel files stored as JSON in `.planning/intel/`
- REQ-INTEL-02: `query` searches across all intel files
- REQ-INTEL-03: `status` reports freshness (STALE threshold: 24 hours)
- REQ-INTEL-04: `diff` compares to last snapshot
- REQ-INTEL-05: `refresh` rebuilds all files
- REQ-INTEL-06: Opt-in via `intel.enabled: true`

**Intel files produced:**
| File | Contents |
|------|----------|
| `stack.json` | Technology stack and dependencies |
| `api-map.json` | Exported functions and API surface |
| `dependency-graph.json` | Inter-module dependency relationships |
| `file-roles.json` | Role classification for each source file |
| `arch-decisions.json` | Detected architecture decisions |

---

## 91. Execution Context Profiles

**Config:** `context_profile`

**Purpose:** Select pre-configured execution context tuned for specific work type.

**Requirements:**
- REQ-CTX-01: `dev` profile optimizes for iterative development
- REQ-CTX-02: `research` profile optimizes for research-heavy work
- REQ-CTX-03: `review` profile optimizes for code review

**Available profiles:** `dev`, `research`, `review`

---

## 92. Gates Taxonomy

**Purpose:** Define 4 canonical gate types for workflow decision points.

**Gate types:**
| Type | Description |
|------|-------------|
| **Confirm** | User approves before proceeding |
| **Quality** | Automated quality check must pass |
| **Safety** | Hard stop on detected risk or policy violation |
| **Transition** | Phase or milestone boundary acknowledgment |

**Requirements:**
- REQ-GATES-01: plan-checker classifies each checkpoint as one of 4 gate types
- REQ-GATES-02: verifier applies gate logic appropriate to gate type
- REQ-GATES-03: Hard stop safety gates never bypassed by `--auto` flags

---

## 93. Code Review Pipeline

**Commands:** `/gsd-code-review`, `/gsd-code-review-fix`

**Purpose:** Structured review of source files changed during phase, with separate auto-fix pass.

**Requirements:**
- REQ-REVIEW-01: Scope files to phase using SUMMARY.md and git diff fallback
- REQ-REVIEW-02: Support three depth levels: `quick`, `standard`, `deep`
- REQ-REVIEW-03: Severity-classified: Critical, Warning, Info
- REQ-REVIEW-04: `gsd-code-review-fix` reads REVIEW.md and fixes Critical + Warning findings
- REQ-REVIEW-05: Each fix committed atomically
- REQ-REVIEW-06: `--auto` enables fix + re-review iteration loop (max 3 iterations)
- REQ-REVIEW-07: Gated by `workflow.code_review` config flag

**Config:**
| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `workflow.code_review` | boolean | `true` | Enable code review commands |
| `workflow.code_review_depth` | string | `standard` | Default review depth |

---

## 94. Socratic Exploration

**Command:** `/gsd-explore [topic]`

**Purpose:** Guide developer through exploring an idea via Socratic probing before committing to a plan.

**Requirements:**
- REQ-EXPLORE-01: Use Socratic probing — ask questions before proposing solutions
- REQ-EXPLORE-02: Offer to route outputs to appropriate GSD artifact
- REQ-EXPLORE-03: Optional topic argument primes first question
- REQ-EXPLORE-04: Optionally spawn research agent for technical feasibility

---

## 95. Safe Undo

**Command:** `/gsd-undo --last N | --phase NN | --plan NN-MM`

**Purpose:** Roll back GSD phase or plan commits using phase manifest and git log.

**Requirements:**
- REQ-UNDO-01: `--phase` mode identifies all commits for phase via manifest
- REQ-UNDO-02: `--plan` mode identifies all commits for specific plan
- REQ-UNDO-03: `--last N` mode displays recent GSD commits for selection
- REQ-UNDO-04: Check for dependent phases/plans before reverting
- REQ-UNDO-05: Confirmation gate before any git revert

---

## 96. Plan Import

**Command:** `/gsd-import --from <filepath>`

**Purpose:** Ingest external plan file into GSD with conflict detection against `PROJECT.md` decisions.

**Requirements:**
- REQ-IMPORT-01: Detect conflicts between external plan and PROJECT.md decisions
- REQ-IMPORT-02: Present conflicts to user for resolution before writing
- REQ-IMPORT-03: Write as valid GSD PLAN.md format
- REQ-IMPORT-04: Pass `gsd-plan-checker` validation

---

## 97. Rapid Codebase Scan

**Command:** `/gsd-scan [--focus tech|arch|quality|concerns|tech+arch]`

**Purpose:** Lightweight alternative to `/gsd-map-codebase` spawning single mapper agent.

**Requirements:**
- REQ-SCAN-01: Spawn exactly one mapper agent
- REQ-SCAN-02: Focus area: `tech`, `arch`, `quality`, `concerns`, `tech+arch` (default)
- REQ-SCAN-03: Output written to `.planning/codebase/`

---

## 98. Autonomous Audit-to-Fix

**Command:** `/gsd-audit-fix [--source <audit>] [--severity high|medium|all] [--max N] [--dry-run]`

**Purpose:** End-to-end pipeline: audit, classify findings, autonomously fix auto-fixable issues.

**Requirements:**
- REQ-AUDITFIX-01: Classify findings as auto-fixable or manual-only before changes
- REQ-AUDITFIX-02: Each fix verified with tests before committing
- REQ-AUDITFIX-03: Each fix committed atomically
- REQ-AUDITFIX-04: `--dry-run` shows classification without fixing
- REQ-AUDITFIX-05: `--max N` limits fixes per run (default: 5)

---

## 99. Improved Prompt Injection Scanner

**Purpose:** Enhanced detection adding invisible Unicode, encoding obfuscation, entropy-based analysis.

**Requirements:**
- REQ-SCAN-INJ-01: Detect invisible Unicode characters
- REQ-SCAN-INJ-02: Detect encoding obfuscation patterns (base64, homoglyphs)
- REQ-SCAN-INJ-03: Apply entropy analysis to flag high-entropy strings
- REQ-SCAN-INJ-04: Remain advisory-only

---

## 100. Stall Detection in Plan-Phase

**Purpose:** Detect when planner revision loop has stalled and break cycle.

**Requirements:**
- REQ-STALL-01: Detect identical plan output across consecutive iterations
- REQ-STALL-02: Escalate strategy before retrying on stall detection
- REQ-STALL-03: Maximum stall retries bounded

---

## 101. Hard Stop Safety Gates in /gsd-next

**Purpose:** Prevent `/gsd-next` from entering runaway loops.

**Requirements:**
- REQ-NEXT-GATE-01: Track consecutive same-step calls
- REQ-NEXT-GATE-02: Present hard stop gate on repeated same-step
- REQ-NEXT-GATE-03: User must explicitly confirm to continue

---

## 102. Adaptive Model Preset

**Config:** `model_profile: "adaptive"`

**Purpose:** Role-based model assignment selecting appropriate tier based on agent role.

**Requirements:**
- REQ-ADAPTIVE-01: Assign model tiers based on agent role
- REQ-ADAPTIVE-02: Selectable via `/gsd-set-profile adaptive`

---

## 103. Post-Merge Hunk Verification

**Command:** `/gsd-reapply-patches`

**Purpose:** After applying local patches, verify all hunks were actually applied.

**Requirements:**
- REQ-PATCH-VERIFY-01: Verify each hunk was applied after merge
- REQ-PATCH-VERIFY-02: Report dropped or partial hunks with file and line context
- REQ-PATCH-VERIFY-03: Verification runs after all patches applied

---

# v1.35.0 Features

## 104. New Runtime Support (Cline, CodeBuddy, Qwen Code)

**Purpose:** Extend GSD installation to Cline, CodeBuddy, Qwen Code runtimes.

**Requirements:**
- REQ-CLINE-02: Cline writes `.clinerules` to `~/.cline/` or `./.cline/`
- REQ-CODEBUDDY-01: CodeBuddy deploys skills to `~/.codebuddy/skills/`
- REQ-QWEN-01: Qwen Code deploys skills to `~/.qwen/skills/`

**Runtime summary:**
| Runtime | Install Format | Config Path | Flag |
|---------|---------------|-------------|------|
| Cline | `.clinerules` | `~/.cline/` or `./.cline/` | `--cline` |
| CodeBuddy | Skills | `~/.codebuddy/skills/` | `--codebuddy` |
| Qwen Code | Skills | `~/.qwen/skills/` | `--qwen` |

---

## 105. GSD-2 Reverse Migration

**Command:** `/gsd-from-gsd2 [--dry-run] [--force] [--path <dir>]`

**Purpose:** Migrate project from GSD-2 format (`.gsd/`) back to v1 `.planning/` format.

**Requirements:**
- REQ-FROM-GSD2-01: Read `.gsd/` from specified or current directory
- REQ-FROM-GSD2-02: Flatten Milestone→Slice hierarchy to sequential phase numbers
- REQ-FROM-GSD2-03: Guard against overwriting existing `.planning/` without `--force`
- REQ-FROM-GSD2-04: `--dry-run` previews without writing
- REQ-FROM-GSD2-05: Produce PROJECT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, phase directories

**Flags:**
| Flag | Description |
|------|-------------|
| `--dry-run` | Preview without writing |
| `--force` | Overwrite existing `.planning/` |
| `--path <dir>` | Specify GSD-2 root directory |

---

## 106. AI Integration Phase Wizard

**Command:** `/gsd-ai-integration-phase [N]`

**Purpose:** Guide developers through selecting, integrating, planning evaluation for AI/LLM capabilities.

**Requirements:**
- REQ-AISPEC-01: Present interactive decision matrix for framework selection, model choice, integration approach
- REQ-AISPEC-02: Surface domain-specific failure modes and eval criteria
- REQ-AISPEC-03: Spawn 3 parallel specialists: domain-researcher, framework-selector, eval-planner
- REQ-AISPEC-04: Produce `{phase}-AI-SPEC.md`

---

## 107. AI Eval Review

**Command:** `/gsd-eval-review [N]`

**Purpose:** Retroactively audit an executed AI phase's evaluation coverage against `AI-SPEC.md`.

**Requirements:**
- REQ-EVALREVIEW-01: Read `AI-SPEC.md` from specified phase
- REQ-EVALREVIEW-02: Score each eval dimension as COVERED, PARTIAL, or MISSING
- REQ-EVALREVIEW-03: Output includes findings, gap descriptions, remediation guidance
- REQ-EVALREVIEW-04: Write `EVAL-REVIEW.md` to phase directory

---

# v1.36.0 Features

## 108. Plan Bounce

**Command:** `/gsd-plan-phase N --bounce`

**Purpose:** After plans pass checker, optionally refine through external script.

**Requirements:**
- REQ-BOUNCE-01: `--bounce` flag or `workflow.plan_bounce: true` activates
- REQ-BOUNCE-02: `workflow.plan_bounce_script` must point to valid executable
- REQ-BOUNCE-03: Each plan backed up before script runs
- REQ-BOUNCE-04: Broken YAML or failed plan checker triggers restore from backup
- REQ-BOUNCE-05: `workflow.plan_bounce_passes` controls refinement passes (default: 2)

**Configuration:** `workflow.plan_bounce`, `workflow.plan_bounce_script`, `workflow.plan_bounce_passes`

---

## 109. External Code Review Command

**Command:** `/gsd-ship` (enhanced)

**Purpose:** Before manual review in `/gsd-ship`, automatically run external code review command if configured.

**Requirements:**
- REQ-EXTREVIEW-01: `workflow.code_review_command` must be set
- REQ-EXTREVIEW-02: Diff generated against `BASE_BRANCH`
- REQ-EXTREVIEW-03: Review prompt piped via stdin
- REQ-EXTREVIEW-04: 120-second timeout; stderr captured on failure
- REQ-EXTREVIEW-05: JSON output parsed for `verdict`, `confidence`, `summary`, `issues`

**Configuration:** `workflow.code_review_command`

---

## 110. Cross-AI Execution Delegation

**Command:** `/gsd-execute-phase N --cross-ai`

**Purpose:** Delegate individual plans to external AI runtime for execution.

**Requirements:**
- REQ-CROSSAI-01: `--cross-ai` forces all plans through cross-AI; `--no-cross-ai` disables
- REQ-CROSSAI-02: `workflow.cross_ai_execution: true` and plan frontmatter `cross_ai: true` for per-plan
- REQ-CROSSAI-03: Task prompt piped via stdin to prevent injection
- REQ-CROSSAI-04: Dirty working tree produces warning before execution
- REQ-CROSSAI-05: On failure, user chooses: retry, skip, or abort

**Configuration:** `workflow.cross_ai_execution`, `workflow.cross_ai_command`, `workflow.cross_ai_timeout`

---

## 111. Architectural Responsibility Mapping

**Purpose:** During phase research, map each capability to its architectural tier owner.

**Requirements:**
- REQ-ARM-01: Phase researcher produces Architectural Responsibility Map table in RESEARCH.md
- REQ-ARM-02: Planner sanity-checks task-to-tier assignments
- REQ-ARM-03: Plan checker validates tier compliance as Dimension 7c

**Produces:** `## Architectural Responsibility Map` section in `{phase}-RESEARCH.md`

---

## 112. Extract Learnings

**Command:** `/gsd-extract-learnings N`

**Purpose:** Extract structured knowledge from completed phase artifacts.

**Requirements:**
- REQ-LEARN-01: Requires PLAN.md and SUMMARY.md
- REQ-LEARN-02: Each extracted item includes source attribution
- REQ-LEARN-03: If `capture_thought` tool available, captures with metadata
- REQ-LEARN-04: If unavailable, completes successfully
- REQ-LEARN-05: Running twice overwrites previous `LEARNINGS.md`

**Produces:** `{phase}-LEARNINGS.md` with YAML frontmatter

---

## 113. SDK Workstream Support

**Command:** `gsd-sdk init @prd.md --ws my-workstream`

**Purpose:** Route all SDK `.planning/` paths to `.planning/workstreams/<name>/`.

**Requirements:**
- REQ-WS-01: `--ws <name>` routes all paths to workstream directory
- REQ-WS-02: Without `--ws`, behavior unchanged
- REQ-WS-03: Name validated to alphanumeric, hyphens, underscores, dots
- REQ-WS-04: Config resolves from workstream path first, falls back to root

---

## 114. Context-Window-Aware Prompt Thinning

**Purpose:** Reduce static prompt overhead by ~40% for models with context windows under 200K tokens.

**Requirements:**
- REQ-THIN-01: When `CONTEXT_WINDOW < 200000`, executor and planner prompts omit inline examples
- REQ-THIN-02: Extracted content lives in reference files
- REQ-THIN-03: Standard (200K-500K) and enriched (500K+) tiers unaffected
- REQ-THIN-04: Core rules and decision logic remain inline

**Reference files:** `executor-examples.md`, `planner-antipatterns.md`

---

## 115. Configurable CLAUDE.md Path

**Purpose:** Allow projects to store CLAUDE.md in non-root location.

**Requirements:**
- REQ-CMDPATH-01: `claude_md_path` defaults to `./CLAUDE.md`
- REQ-CMDPATH-02: Profile generation commands read from config
- REQ-CMDPATH-03: Relative paths resolved from project root

---

## 116. TDD Pipeline Mode

**Purpose:** Opt-in TDD (red-green-refactor) as first-class phase execution mode.

**Requirements:**
- REQ-TDD-01: `workflow.tdd_mode` config key (boolean, default `false`)
- REQ-TDD-02: When enabled, planner applies TDD heuristics to eligible tasks
- REQ-TDD-03: Executor enforces RED/GREEN/REFACTOR gate sequence
- REQ-TDD-04: Executor fails fast if tests pass unexpectedly during RED phase
- REQ-TDD-05: End-of-phase review checkpoint verifies gate compliance
- REQ-TDD-06: Gate violations surfaced in SUMMARY.md

**Configuration:** `workflow.tdd_mode`
**Reference files:** `tdd.md`, `checkpoints.md`

#project-management #workflow-automation #gsd-framework #feature-reference
