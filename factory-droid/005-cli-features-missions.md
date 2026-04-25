---
title: Missions - Factory Documentation
url: https://docs.factory.ai/cli/features/missions
source: sitemap
fetched_at: 2026-04-15T09:00:54.022549908-03:00
rendered_js: false
word_count: 786
summary: This document explains the Missions feature in Droid, a structured workflow for executing complex, multi-feature projects through collaborative planning, milestone-based validation, and agent orchestration.
tags:
    - project-management
    - ai-orchestration
    - workflow-automation
    - task-decomposition
    - agentic-workflow
    - mission-control
category: concept
---

## What are Missions?

Missions are a structured way to take on large, multi-feature work with Droid. Instead of tackling everything in a single session, you collaborate with Droid upfront to build a plan — features, milestones, and the skills needed to accomplish each part — then hand off execution to an orchestration layer that manages the work. Access Missions with the `/missions` command (also available via `/mission` and `/enter-mission`).

## How it works

## The planning phase matters most

The biggest value we have found in Missions is in the planning phase. Getting the upfront plan right — the features, the ordering, the milestones, the skills involved — is what determines whether the execution succeeds. Droid will push back, ask questions, and iterate with you until the plan is solid. This is intentional. A well-scoped plan with clear milestones produces dramatically better results than jumping straight into execution on a vague goal.

### Validation

- *Milestones** define validation frequency. Validation workers run at the end of each milestone, verifying its work. For simple projects, one milestone is often enough; for longer or complex projects, more frequent milestone validation helps keep the foundation stable as work scales.

For smaller, straightforward projects, a single milestone is often enough. For larger or longer-running projects, more granular milestones can prevent drift and reduce expensive rework later.

### Estimating cost and duration

As a rough planning heuristic, mission duration and cost scale with the number of worker runs:

- **Feature workers:** roughly one run per feature
- **Validator workers:** roughly one run per milestone

So an initial estimate is approximately: `total runs ≈ #features + 2 * #milestones` In practice, this is a floor rather than a ceiling. Validation may surface issues that require follow-up work, and the orchestrator can create additional fix features during execution.

## What Missions are good for

We have built and tested Missions across a range of work:

- **Full-stack development** — Building complete applications with frontend, backend, database, and deployment.
- **Research** — Deep investigation tasks that require exploring multiple approaches, synthesizing findings, and producing structured output.
- **Brownfield migrations** — Modernizing existing codebases, swapping frameworks, or restructuring large projects while preserving existing behavior.
- **Ambitious prototypes** — Product experiments that need to be functional, not just sketched out.

The common thread: work that benefits from upfront planning and structured decomposition rather than ad-hoc prompting.

## Working with Mission Control

Once the plan is approved, Droid enters Mission Control — the orchestration view that manages execution. From here you can track progress across features and milestones, see which agents are working on what, and intervene when things need adjustment.

### Intervening and redirecting

Missions are not fire-and-forget. The orchestrator is an agent, and you can talk to it. The most effective way to use Missions is to treat yourself as the project manager — monitoring progress, unblocking workers, and redirecting when the plan needs to change.

### A new kind of debugging

The skillset for working with Missions looks less like traditional debugging and more like **project management of agents**. You are not stepping through code line by line — you are monitoring a team of workers, unblocking them when they get stuck, redirecting them when priorities change, and making judgment calls about when to push through versus when to re-plan. This is a meaningfully different way of working with AI. The core skill is knowing when and how to intervene, not writing the code yourself.

## Configuration inheritance

Missions inherit your existing Droid configuration:

- **MCP integrations** — Workers can use your connected tools (Linear, Sentry, Notion, etc.)
- **Custom skills** — Your existing skills are available and new ones can be developed during planning.
- **Hooks** — Lifecycle hooks fire during mission execution.
- **Custom droids** — Subagents configured in your project are available to workers.
- **AGENTS.md** — Workers follow your project conventions and coding standards.

## Open questions

Missions are early. We are shipping this as a research preview because there are fundamental questions we are still working through:

- **Is parallelization necessary?** Running multiple agents in parallel sounds good in theory, but does it actually produce better results than sequential execution? We are testing this.
- **How do you maximize correctness?** Long-running plans accumulate errors. What validation and correction strategies work best at each stage?
- **Cost vs. quality tradeoffs** — How aggressive should the orchestrator be? More planning and validation means higher cost but potentially better output. Where is the right balance?

We want your feedback on these. Use Missions, push them hard, and tell us what works and what does not.

## See also

- [Specification Mode](https://docs.factory.ai/cli/user-guides/specification-mode) — For well-scoped tasks that benefit from planning before implementation
- [Implementing Large Features](https://docs.factory.ai/cli/user-guides/implementing-large-features) — Manual workflow for multi-phase projects
- [Custom Droids](https://docs.factory.ai/cli/configuration/custom-droids) — Build specialized subagents that missions can use
- [Skills](https://docs.factory.ai/cli/configuration/skills) — Create and manage skills that missions can leverage