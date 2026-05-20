---
title: Getting Started
url: https://docs.bmad-method.org//tutorials/getting-started/
source: llms
fetched_at: 2026-05-19T08:33:03.552062073-03:00
rendered_js: false
word_count: 1031
summary: This document provides a comprehensive guide to using the BMad Method, an AI-powered framework that utilizes specialized agents to assist in software project planning, architecture design, and iterative implementation.
tags:
    - ai-agents
    - software-development
    - workflow-automation
    - project-management
    - bmad-method
    - ai-development-tools
category: guide
optimized: true
optimized_at: 2026-05-19T11:33:03Z
---
Build software faster using AI-powered workflows with specialized agents that guide you through planning, architecture, and implementation.

## What You'll Learn
BLUF: Install BMad, use BMad-Help, choose a planning track, and progress through phases to working code.

- Install and initialize BMad Method for a new project
- Use **BMad-Help** — your intelligent guide that knows what to do next
- Choose the right planning track for your project size
- Progress through phases from requirements to working code
- Use agents and workflows effectively

## Meet BMad-Help: Your Intelligent Guide
BLUF: BMad-Help inspects your project, shows options, recommends next steps, and answers questions — no memorization required.

- **Inspect your project** to see what's already been done
- **Show your options** based on which modules you have installed
- **Recommend what's next** — including the first required task
- **Answer questions** like "I have a SaaS idea, where do I start?"

### How to Use BMad-Help
Run it in your AI IDE by invoking the skill:

```plaintext

bmad-help I have an idea for a SaaS product, I already know all the features I want. where do I get started?
```

BMad-Help responds with what's recommended, the first required task, and what the rest of the process looks like.

### It Powers Workflows Too
BMad-Help automatically runs at the end of every workflow to tell you exactly what to do next.

## Understanding BMad
BLUF: BMad builds software through four guided phases with specialized AI agents.

| Phase | Name | What Happens |
|-------|------|--------------|
| 1 | Analysis | Brainstorming, research, product brief or PRFAQ *(optional)* |
| 2 | Planning | Create requirements (PRD or spec) |
| 3 | Solutioning | Design architecture *(BMad Method/Enterprise only)* |
| 4 | Implementation | Build epic by epic, story by story |

[[004-reference-workflow-map|Open the Workflow Map]] to explore phases, workflows, and context management.

BMad offers three planning tracks based on project complexity:

| Track | Best For | Documents Created |
|-------|----------|-------------------|
| **Quick Flow** | Bug fixes, simple features, clear scope (1-15 stories) | Tech-spec only |
| **BMad Method** | Products, platforms, complex features (10-50+ stories) | PRD + Architecture + UX |
| **Enterprise** | Compliance, multi-tenant systems (30+ stories) | PRD + Architecture + Security + DevOps |

Open a terminal in your project directory and run:

```bash

npx bmad-method install
```

For the newest prerelease build instead of the default release channel, use `npx bmad-method@next install`.

When prompted to select modules, choose **BMad Method**.

The installer creates two folders:

- `_bmad/` — agents, workflows, tasks, and configuration
- `_bmad-output/` — empty for now, but this is where your artifacts will be saved

## Step 1: Create Your Plan
BLUF: Work through phases 1-3. Use fresh chats for each workflow.

### Phase 1: Analysis (Optional)
All workflows in this phase are optional. [**Not sure which to use?**](https://docs.bmad-method.org/explanation/analysis-phase/)

- **brainstorming** (`bmad-brainstorming`) — Guided ideation
- **research** (`bmad-market-research` / `bmad-domain-research` / `bmad-technical-research`) — Market, domain, and technical research
- **product-brief** (`bmad-product-brief`) — Recommended foundation document when your concept is clear
- **prfaq** (`bmad-prfaq`) — Working Backwards challenge to stress-test and forge your product concept

### Phase 2: Planning (Required)
**For BMad Method and Enterprise tracks:**
1. Run `bmad-prd` in a new chat — state your intent (Create / Update / Validate) or let the skill ask
2. Output: `prd.md`, `addendum.md`, `decision-log.md`

**For Quick Flow track:**
- Run `bmad-quick-dev` — it handles planning and implementation in a single workflow, skip to implementation

### Phase 3: Solutioning (BMad Method/Enterprise)
**Create Architecture**
1. Invoke the **Architect agent** (`bmad-agent-architect`) in a new chat
2. Run `bmad-create-architecture`
3. Output: Architecture document with technical decisions

**Create Epics and Stories**
1. Invoke the **PM agent** (`bmad-agent-pm`) in a new chat
2. Run `bmad-create-epics-and-stories`
3. Uses both PRD and Architecture to create technically-informed stories

**Implementation Readiness Check** *(Highly Recommended)*
1. Invoke the **Architect agent** (`bmad-agent-architect`) in a new chat
2. Run `bmad-check-implementation-readiness`
3. Validates cohesion across all planning documents

## Step 2: Build Your Project
BLUF: Move to implementation once planning is complete. Run each workflow in a fresh chat.

### Initialize Sprint Planning
Invoke the **Developer agent** (`bmad-agent-dev`) and run `bmad-sprint-planning`. This creates `sprint-status.yaml` to track all epics and stories.

For each story, repeat this cycle with fresh chats:

| Step | Agent | Workflow | Command | Purpose |
|------|-------|----------|---------|---------|
| 1 | DEV | `bmad-create-story` | `bmad-create-story` | Create story file from epic |
| 2 | DEV | `bmad-dev-story` | `bmad-dev-story` | Implement the story |
| 3 | DEV | `bmad-code-review` | `bmad-code-review` | Quality validation *(recommended)* |

After completing all stories in an epic, invoke the **Developer agent** (`bmad-agent-dev`) and run `bmad-retrospective`.

## What You've Accomplished
BLUF: You've installed BMad, chosen a track, created planning documents, and understood the build cycle.

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

### Quick Reference

| Workflow | Command | Agent | Purpose |
|----------|---------|-------|---------|
| **`bmad-help`** ⭐ | `bmad-help` | Any | **Your intelligent guide — ask anything!** |
| `bmad-prd` | `bmad-prd` | Any | Create, update, or validate a PRD |
| `bmad-create-architecture` | `bmad-create-architecture` | Architect | Create architecture document |
| `bmad-generate-project-context` | `bmad-generate-project-context` | Analyst | Create project context file |
| `bmad-create-epics-and-stories` | `bmad-create-epics-and-stories` | PM | Break down PRD into epics |
| `bmad-check-implementation-readiness` | `bmad-check-implementation-readiness` | Architect | Validate planning cohesion |
| `bmad-sprint-planning` | `bmad-sprint-planning` | DEV | Initialize sprint tracking |
| `bmad-create-story` | `bmad-create-story` | DEV | Create a story file |
| `bmad-dev-story` | `bmad-dev-story` | DEV | Implement a story |
| `bmad-code-review` | `bmad-code-review` | DEV | Review implemented code |

### FAQ

- **Do I always need architecture?** Only for BMad Method and Enterprise tracks. Quick Flow skips from spec to implementation.
- **Can I change my plan later?** Yes. The `bmad-correct-course` workflow handles scope changes mid-implementation.
- **What if I want to brainstorm first?** Invoke the Analyst agent (`bmad-agent-analyst`) and run `bmad-brainstorming` before starting your PRD.
- **Do I need to follow a strict order?** Not strictly. Once you learn the flow, you can run workflows directly using the Quick Reference above.

- **During workflows** — Agents guide you with questions and explanations
- **Community** — [Discord](https://discord.gg/gk8jAdXWmj) (#bmad-method-help, #report-bugs-and-issues)

Ready to start? Install BMad, invoke `bmad-help`, and let your intelligent guide lead the way.

#ai-agents #software-development #workflow-automation #project-management #bmad-method
