---
title: Getting Started
url: https://docs.bmad-method.org/tutorials/getting-started/
source: sitemap
fetched_at: 2026-04-08T11:31:39.24318904-03:00
rendered_js: false
word_count: 894
summary: This document provides a comprehensive guide to using the BMad system, detailing the entire software development lifecycle from initial planning through implementation. It explains how specialized AI agents and guided workflows help users build applications by following structured phases like Analysis, Planning, Solutioning, and Implementation.
tags:
    - ai-workflow
    - software-development
    - project-planning
    - agent-usage
    - bmad-method
    - implementation-guide
category: guide
---

Build software faster using AI-powered workflows with specialized agents that guide you through planning, architecture, and implementation.

## What You’ll Learn

[Section titled “What You’ll Learn”](#what-youll-learn)

- Install and initialize BMad Method for a new project
- Use **BMad-Help** — your intelligent guide that knows what to do next
- Choose the right planning track for your project size
- Progress through phases from requirements to working code
- Use agents and workflows effectively

## Meet BMad-Help: Your Intelligent Guide

[Section titled “Meet BMad-Help: Your Intelligent Guide”](#meet-bmad-help-your-intelligent-guide)

**BMad-Help is the fastest way to get started with BMad.** You don’t need to memorize workflows or phases — just ask, and BMad-Help will:

- **Inspect your project** to see what’s already been done
- **Show your options** based on which modules you have installed
- **Recommend what’s next** — including the first required task
- **Answer questions** like “I have a SaaS idea, where do I start?”

### How to Use BMad-Help

[Section titled “How to Use BMad-Help”](#how-to-use-bmad-help)

Run it in your AI IDE by invoking the skill:

Or combine it with a question for context-aware guidance:

```plaintext

bmad-help I have an idea for a SaaS product, I already know all the features I want. where do I get started?
```

BMad-Help will respond with:

- What’s recommended for your situation
- What the first required task is
- What the rest of the process looks like

### It Powers Workflows Too

[Section titled “It Powers Workflows Too”](#it-powers-workflows-too)

BMad-Help doesn’t just answer questions — **it automatically runs at the end of every workflow** to tell you exactly what to do next. No guessing, no searching docs — just clear guidance on the next required workflow.

## Understanding BMad

[Section titled “Understanding BMad”](#understanding-bmad)

BMad helps you build software through guided workflows with specialized AI agents. The process follows four phases:

PhaseNameWhat Happens1AnalysisBrainstorming, research, product brief or PRFAQ *(optional)*2PlanningCreate requirements (PRD or spec)3SolutioningDesign architecture *(BMad Method/Enterprise only)*4ImplementationBuild epic by epic, story by story

[**Open the Workflow Map**](https://docs.bmad-method.org/reference/workflow-map/) to explore phases, workflows, and context management.

Based on your project’s complexity, BMad offers three planning tracks:

TrackBest ForDocuments Created**Quick Flow**Bug fixes, simple features, clear scope (1-15 stories)Tech-spec only**BMad Method**Products, platforms, complex features (10-50+ stories)PRD + Architecture + UX**Enterprise**Compliance, multi-tenant systems (30+ stories)PRD + Architecture + Security + DevOps

Open a terminal in your project directory and run:

If you want the newest prerelease build instead of the default release channel, use `npx bmad-method@next install`.

When prompted to select modules, choose **BMad Method**.

The installer creates two folders:

- `_bmad/` — agents, workflows, tasks, and configuration
- `_bmad-output/` — empty for now, but this is where your artifacts will be saved

## Step 1: Create Your Plan

[Section titled “Step 1: Create Your Plan”](#step-1-create-your-plan)

Work through phases 1-3. **Use fresh chats for each workflow.**

### Phase 1: Analysis (Optional)

[Section titled “Phase 1: Analysis (Optional)”](#phase-1-analysis-optional)

All workflows in this phase are optional. [**Not sure which to use?**](https://docs.bmad-method.org/explanation/analysis-phase/)

- **brainstorming** (`bmad-brainstorming`) — Guided ideation
- **research** (`bmad-market-research` / `bmad-domain-research` / `bmad-technical-research`) — Market, domain, and technical research
- **product-brief** (`bmad-product-brief`) — Recommended foundation document when your concept is clear
- **prfaq** (`bmad-prfaq`) — Working Backwards challenge to stress-test and forge your product concept

### Phase 2: Planning (Required)

[Section titled “Phase 2: Planning (Required)”](#phase-2-planning-required)

**For BMad Method and Enterprise tracks:**

1. Invoke the **PM agent** (`bmad-agent-pm`) in a new chat
2. Run the `bmad-create-prd` workflow (`bmad-create-prd`)
3. Output: `PRD.md`

**For Quick Flow track:**

- Run `bmad-quick-dev` — it handles planning and implementation in a single workflow, skip to implementation

### Phase 3: Solutioning (BMad Method/Enterprise)

[Section titled “Phase 3: Solutioning (BMad Method/Enterprise)”](#phase-3-solutioning-bmad-methodenterprise)

**Create Architecture**

1. Invoke the **Architect agent** (`bmad-agent-architect`) in a new chat
2. Run `bmad-create-architecture` (`bmad-create-architecture`)
3. Output: Architecture document with technical decisions

**Create Epics and Stories**

1. Invoke the **PM agent** (`bmad-agent-pm`) in a new chat
2. Run `bmad-create-epics-and-stories` (`bmad-create-epics-and-stories`)
3. The workflow uses both PRD and Architecture to create technically-informed stories

**Implementation Readiness Check** *(Highly Recommended)*

1. Invoke the **Architect agent** (`bmad-agent-architect`) in a new chat
2. Run `bmad-check-implementation-readiness` (`bmad-check-implementation-readiness`)
3. Validates cohesion across all planning documents

## Step 2: Build Your Project

[Section titled “Step 2: Build Your Project”](#step-2-build-your-project)

Once planning is complete, move to implementation. **Each workflow should run in a fresh chat.**

### Initialize Sprint Planning

[Section titled “Initialize Sprint Planning”](#initialize-sprint-planning)

Invoke the **Developer agent** (`bmad-agent-dev`) and run `bmad-sprint-planning` (`bmad-sprint-planning`). This creates `sprint-status.yaml` to track all epics and stories.

For each story, repeat this cycle with fresh chats:

StepAgentWorkflowCommandPurpose1DEV`bmad-create-story``bmad-create-story`Create story file from epic2DEV`bmad-dev-story``bmad-dev-story`Implement the story3DEV`bmad-code-review``bmad-code-review`Quality validation *(recommended)*

After completing all stories in an epic, invoke the **Developer agent** (`bmad-agent-dev`) and run `bmad-retrospective` (`bmad-retrospective`).

## What You’ve Accomplished

[Section titled “What You’ve Accomplished”](#what-youve-accomplished)

You’ve learned the foundation of building with BMad:

- Installed BMad and configured it for your IDE
- Initialized a project with your chosen planning track
- Created planning documents (PRD, Architecture, Epics & Stories)
- Understood the build cycle for implementation

Your project now has:

```text

your-project/
├── _bmad/                                   # BMad configuration
├── _bmad-output/
│   ├── planning-artifacts/
│   │   ├── PRD.md                           # Your requirements document
│   │   ├── architecture.md                  # Technical decisions
│   │   └── epics/                           # Epic and story files
│   ├── implementation-artifacts/
│   │   └── sprint-status.yaml               # Sprint tracking
│   └── project-context.md                   # Implementation rules (optional)
└── ...
```

WorkflowCommandAgentPurpose**`bmad-help`** ⭐`bmad-help`Any**Your intelligent guide — ask anything!**`bmad-create-prd``bmad-create-prd`PMCreate Product Requirements Document`bmad-create-architecture``bmad-create-architecture`ArchitectCreate architecture document`bmad-generate-project-context``bmad-generate-project-context`AnalystCreate project context file`bmad-create-epics-and-stories``bmad-create-epics-and-stories`PMBreak down PRD into epics`bmad-check-implementation-readiness``bmad-check-implementation-readiness`ArchitectValidate planning cohesion`bmad-sprint-planning``bmad-sprint-planning`DEVInitialize sprint tracking`bmad-create-story``bmad-create-story`DEVCreate a story file`bmad-dev-story``bmad-dev-story`DEVImplement a story`bmad-code-review``bmad-code-review`DEVReview implemented code

**Do I always need architecture?** Only for BMad Method and Enterprise tracks. Quick Flow skips from spec to implementation.

**Can I change my plan later?** Yes. The `bmad-correct-course` workflow handles scope changes mid-implementation.

**What if I want to brainstorm first?** Invoke the Analyst agent (`bmad-agent-analyst`) and run `bmad-brainstorming` (`bmad-brainstorming`) before starting your PRD.

**Do I need to follow a strict order?** Not strictly. Once you learn the flow, you can run workflows directly using the Quick Reference above.

- **During workflows** — Agents guide you with questions and explanations
- **Community** — [Discord](https://discord.gg/gk8jAdXWmj) (#bmad-method-help, #report-bugs-and-issues)

Ready to start? Install BMad, invoke `bmad-help`, and let your intelligent guide lead the way.