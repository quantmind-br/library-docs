---
title: Scheduled agents quickstart | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/triggers/scheduled-agents-quickstart
source: sitemap
fetched_at: 2026-04-29T15:04:22.593235015-03:00
rendered_js: false
word_count: 377
summary: Configure and manage recurring scheduled agents within the Oz platform to automate routine tasks like GitHub issue triage.
tags:
    - cloud-agents
    - automation
    - cron-jobs
    - workflow-automation
    - github-integration
    - scheduled-tasks
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Scheduled agents are Oz cloud agents that run on a recurring cron schedule, handling recurring tasks automatically without manual triggers. This guide sets up an agent that triages GitHub bug reports weekly, checks whether each issue has enough detail, and posts follow-up comments when information is missing — using a prebundled skill and the Oz web app with no CLI or custom code required.

## Prerequisites

| Requirement | Details |
|---|---|
| **Warp plan** | Build, Max, or Business with credits available. See [Access, Billing, and Identity](https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity). |
| **Oz cloud environment** | Agents run inside a configured environment with repos and dependencies. If you don't have one, follow the [Cloud Agents Quickstart](https://docs.warp.dev/agent-platform/cloud-agents/quickstart) first. |

## 1. Set Up a Scheduled Agent

1. Enter a name, e.g. `Weekly bug report triage`.
2. Under **Agent**, select **github-bug-report-triage** from the suggested skills.
3. Choose your environment.
4. Under **Frequency**, choose a preset or enter a custom cron expression (e.g., `0 9 * * 1` for every Monday at 9 AM).
5. Click **Create schedule**.

> [!note]
> The schedule lives in Oz's cloud infrastructure. Unlike a local cron job, it fires even when your machine is off. Each run starts a fresh, isolated session with no state from previous executions. Every run is tracked and auditable in the [Oz web app](https://docs.warp.dev/agent-platform/cloud-agents/oz-web-app).

## 2. Watch Your First Run

To verify your setup without waiting for the schedule:

1. Click ⋮ and select **Run now**, then click **Run** to confirm.
2. Your test run appears under **All** on the [Runs page](https://oz.warp.dev/runs).
3. Once the schedule fires on its cron, those runs appear under **Recurring**.

Runs are also accessible from the conversation panel in the Warp app and on mobile via the Oz web app.

> [!tip]
> Prefer the CLI? See [Scheduled Agents](https://docs.warp.dev/agent-platform/cloud-agents/triggers/scheduled-agents) for `oz schedule create`, `oz schedule list`, and full schedule management commands. To use a custom skill instead of a prebundled one, see [Skills as Agents](https://docs.warp.dev/agent-platform/cloud-agents/skills-as-agents).

## Next Steps

- **Trigger agents from your tools** — Connect Oz to Slack or Linear. See [Integrations Quickstart](https://docs.warp.dev/agent-platform/cloud-agents/integrations/quickstart).
- **Manage and refine your schedule** — Change frequency, swap skills, or pause/resume. See [Scheduled Agents](https://docs.warp.dev/agent-platform/cloud-agents/triggers/scheduled-agents).
- **Share with your team** — Schedules and environments are shared across your Warp team automatically.
