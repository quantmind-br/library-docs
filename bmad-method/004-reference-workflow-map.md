---
title: Workflow Map
url: https://docs.bmad-method.org//reference/workflow-map/
source: llms
fetched_at: 2026-05-19T08:33:03.54626913-03:00
rendered_js: false
word_count: 493
summary: The BMad Method is a structured, multi-phase framework designed to improve AI agent performance by providing systematic context engineering and progressive planning workflows.
tags:
    - ai-agents
    - context-engineering
    - agile-methodology
    - project-management
    - workflow-automation
    - software-development
category: guide
optimized: true
optimized_at: 2026-05-19T11:33:03Z
---
The BMad Method (BMM) builds context progressively across 4 phases. Each phase produces documents that inform the next, so agents always know what to build and why. Concepts derive from proven agile methodologies.

> [!tip]
> Unsure what to do next? Use `bmad-help` for interactive guidance.

Every workflow below can be run directly via skill or by loading an agent first and using the agents menu.

[Open diagram in new tab ↗](https://docs.bmad-method.org/workflow-map-diagram.html)

## Phase 1: Analysis (Optional)
BLUF: Explore the problem space and validate ideas before committing to planning. [Learn what each tool does and when to use it](https://docs.bmad-method.org/explanation/analysis-phase/).

| Workflow | Purpose | Produces |
|----------|---------|----------|
| `bmad-brainstorming` | Brainstorm project ideas with guided facilitation | `brainstorming-report.md` |
| `bmad-domain-research`, `bmad-market-research`, `bmad-technical-research` | Validate market, technical, or domain assumptions | Research findings |
| `bmad-product-brief` | Capture strategic vision — best when your concept is clear | `product-brief.md` |
| `bmad-prfaq` | Working Backwards — stress-test and forge your product concept | `prfaq-{project}.md` |

## Phase 2: Planning
BLUF: Define what to build and for whom.

| Workflow | Purpose | Produces |
|----------|---------|----------|
| `bmad-prd` | Create, update, or validate a PRD — facilitated discovery, three intents in one skill | Create/Update: `prd.md`, `addendum.md`, `decision-log.md`; Validate: `validation-report.html` + `.md` |
| `bmad-create-ux-design` | Design user experience (when UX matters) | `ux-spec.md` |

## Phase 3: Solutioning
BLUF: Decide how to build it and break work into stories.

| Workflow | Purpose | Produces |
|----------|---------|----------|
| `bmad-create-architecture` | Make technical decisions explicit | `architecture.md` with ADRs |
| `bmad-create-epics-and-stories` | Break requirements into implementable work | Epic files with stories |
| `bmad-check-implementation-readiness` | Gate check before implementation | PASS/CONCERNS/FAIL decision |

## Phase 4: Implementation
BLUF: Build it, one story at a time.

| Workflow | Purpose | Produces |
|----------|---------|----------|
| `bmad-sprint-planning` | Initialize tracking (once per project) | `sprint-status.yaml` |
| `bmad-create-story` | Prepare next story for implementation | `story-[slug].md` |
| `bmad-dev-story` | Implement the story | Working code + tests |
| `bmad-code-review` | Validate implementation quality | Approved or changes requested |
| `bmad-correct-course` | Handle significant mid-sprint changes | Updated plan or re-routing |
| `bmad-sprint-status` | Track sprint progress and story status | Sprint status update |
| `bmad-retrospective` | Review after epic completion | Lessons learned |
| `bmad-investigate` | Forensic case investigation with evidence-graded findings | `{slug}-investigation.md` |

## Quick Flow (Parallel Track)
BLUF: Skip phases 1-3 for small, well-understood work.

| Workflow | Purpose | Produces |
|----------|---------|----------|
| `bmad-quick-dev` | Unified quick flow — clarify intent, plan, implement, review, and present | `spec-*.md` + code |

## Context Management
BLUF: Each document becomes context for the next phase. Without this structure, agents make inconsistent decisions.

- **Manually** — Create `_bmad-output/project-context.md` with your technology stack and implementation rules
- **Generate it** — Run `bmad-generate-project-context` to auto-generate from your architecture or codebase

[Learn more about project-context.md](https://docs.bmad-method.org/explanation/project-context/)

#ai-agents #context-engineering #agile-methodology #project-management #workflow-automation
