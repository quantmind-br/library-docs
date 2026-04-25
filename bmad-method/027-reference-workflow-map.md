---
title: Workflow Map
url: https://docs.bmad-method.org/reference/workflow-map/
source: sitemap
fetched_at: 2026-04-08T11:31:35.532796696-03:00
rendered_js: false
word_count: 505
summary: This document describes the BMad Method (BMM), a structured, four-phase process designed to ensure AI agents build complex projects by progressively building and sharing context across analysis, planning, solutioning, and implementation.
tags:
    - bmad-method
    - context-engineering
    - ai-agent-workflow
    - software-development-lifecycle
    - planning
    - implementation
category: guide
---

The BMad Method (BMM) is a module in the BMad Ecosystem, targeted at following the best practices of context engineering and planning. AI agents work best with clear, structured context. The BMM system builds that context progressively across 4 distinct phases - each phase, and multiple workflows optionally within each phase, produce documents that inform the next, so agents always know what to build and why.

The rationale and concepts come from agile methodologies that have been used across the industry with great success as a mental framework.

If at any time you are unsure what to do, the `bmad-help` skill will help you stay on track or know what to do next. You can always refer to this for reference also - but `bmad-help` is fully interactive and much quicker if you have already installed the BMad Method. Additionally, if you are using different modules that have extended the BMad Method or added other complementary non-extension modules - `bmad-help` evolves to know all that is available to give you the best in-the-moment advice.

Final important note: Every workflow below can be run directly with your tool of choice via skill or by loading an agent first and using the entry from the agents menu.

[Open diagram in new tab ↗](https://docs.bmad-method.org/workflow-map-diagram.html)

## Phase 1: Analysis (Optional)

[Section titled “Phase 1: Analysis (Optional)”](#phase-1-analysis-optional)

Explore the problem space and validate ideas before committing to planning. [**Learn what each tool does and when to use it**](https://docs.bmad-method.org/explanation/analysis-phase/).

WorkflowPurposeProduces`bmad-brainstorming`Brainstorm Project Ideas with guided facilitation of a brainstorming coach`brainstorming-report.md``bmad-domain-research`, `bmad-market-research`, `bmad-technical-research`Validate market, technical, or domain assumptionsResearch findings`bmad-product-brief`Capture strategic vision — best when your concept is clear`product-brief.md``bmad-prfaq`Working Backwards — stress-test and forge your product concept`prfaq-{project}.md`

## Phase 2: Planning

[Section titled “Phase 2: Planning”](#phase-2-planning)

Define what to build and for whom.

WorkflowPurposeProduces`bmad-create-prd`Define requirements (FRs/NFRs)`PRD.md``bmad-create-ux-design`Design user experience (when UX matters)`ux-spec.md`

## Phase 3: Solutioning

[Section titled “Phase 3: Solutioning”](#phase-3-solutioning)

Decide how to build it and break work into stories.

WorkflowPurposeProduces`bmad-create-architecture`Make technical decisions explicit`architecture.md` with ADRs`bmad-create-epics-and-stories`Break requirements into implementable workEpic files with stories`bmad-check-implementation-readiness`Gate check before implementationPASS/CONCERNS/FAIL decision

## Phase 4: Implementation

[Section titled “Phase 4: Implementation”](#phase-4-implementation)

Build it, one story at a time. Coming soon, full phase 4 automation!

WorkflowPurposeProduces`bmad-sprint-planning`Initialize tracking (once per project to sequence the dev cycle)`sprint-status.yaml``bmad-create-story`Prepare next story for implementation`story-[slug].md``bmad-dev-story`Implement the storyWorking code + tests`bmad-code-review`Validate implementation qualityApproved or changes requested`bmad-correct-course`Handle significant mid-sprint changesUpdated plan or re-routing`bmad-sprint-status`Track sprint progress and story statusSprint status update`bmad-retrospective`Review after epic completionLessons learned

## Quick Flow (Parallel Track)

[Section titled “Quick Flow (Parallel Track)”](#quick-flow-parallel-track)

Skip phases 1-3 for small, well-understood work.

WorkflowPurposeProduces`bmad-quick-dev`Unified quick flow — clarify intent, plan, implement, review, and present`spec-*.md` + code

## Context Management

[Section titled “Context Management”](#context-management)

Each document becomes context for the next phase. The PRD tells the architect what constraints matter. The architecture tells the dev agent which patterns to follow. Story files give focused, complete context for implementation. Without this structure, agents make inconsistent decisions.

**How to create it:**

- **Manually** — Create `_bmad-output/project-context.md` with your technology stack and implementation rules
- **Generate it** — Run `bmad-generate-project-context` to auto-generate from your architecture or codebase

[**Learn more about project-context.md**](https://docs.bmad-method.org/explanation/project-context/)