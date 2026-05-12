---
title: Cloud agent quickstart | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/quickstart
source: sitemap
fetched_at: 2026-04-29T15:04:18.835832466-03:00
rendered_js: false
word_count: 1174
summary: This document provides a step-by-step guide for setting up and running remote cloud agents using the Warp terminal to automate development tasks and build persistent workflows.
tags:
    - cloud-agents
    - workflow-automation
    - dev-tools
    - remote-execution
    - warp-terminal
    - docker-environments
    - task-orchestration
category: tutorial
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
**Oz cloud agents** run in a remote environment and can be triggered from events, schedules, integrations, or manually. This enables scaling agents off your laptop, automating development tasks, and building apps on top of agents. Oz handles the orchestration, execution, and observability.

Cloud agents can run interactively (where you steer them in real-time) or autonomously (as background tasks). Each run creates a persistent session that your team can inspect, share, and query through the Warp app, the CLI, web app, or API.

This guide walks you through running your first cloud agent with an environment in about 10 minutes. You'll create an environment, if needed, and launch a cloud agent to help with a development task.

**Common use cases for cloud agents:**

- Launch parallel cloud coding agents to multithread complex development tasks
- Automate repetitive development tasks (e.g., feature-flag cleanup, documentation updates, fixing server crashes)
- Build apps on top of agents, like bug triage and incident response systems

## Prerequisites

Before you begin, make sure you have:

> [!info]
> New to Warp? You'll get credits to try cloud agents. You need at least 20 credits available to run cloud agents and integrations.

## Running your first Oz cloud agent

*~10 minutes • Recommended for all users*

### 1. Open Warp

If you don't have Warp yet, download it from [warp.dev](https://warp.dev) and sign in to your account. When you open the Warp desktop app, you're automatically authenticated to Warp's services.

### 2. Run the `/cloud-agent` command

In Warp's terminal input, type:

```
/cloud-agent
```

This launches a new cloud agent for you.

> [!tip]
> The `/cloud-agent` command is your entry point to cloud agents. It checks if you have an environment set up, and if not, it guides you through creating one.

### 3. Create your environment

> [!info]
> **Already have an environment?** The `/cloud-agent` command will use your existing one. To create additional environments for different projects, use `/create-environment`.

If you don't have an environment yet, the `/cloud-agent` setup flow will guide you through creating one. You will need:

| Field | Description |
|-------|-------------|
| **Name** | A label to identify this environment (required) |
| **Repo(s)** | Type repo in `owner/repo` format or select from the dropdown. Click **Auth with GitHub** if you need to connect your repos. |
| **Docker image** | Your runtime environment (e.g., `python:3.11`, `node:20`). Not sure? Click **Suggest image** and Warp will recommend one based on your repos. |
| **Setup command(s)** | Commands to prepare your workspace, like `pip install -r requirements.txt` or `npm ci`. Add each command separately by pressing Enter. |
| **Description** | Optional notes about what this environment is for. |

> [!tip]
> Environments are composed of Docker containers + Git repos + startup commands. They give your cloud agent a consistent workspace with your code and tools. Warp detects your project automatically and suggests the right setup. Environments can be shared with your team so everyone uses the same configuration.

### 4. Describe what you want the agent to do

Enter your prompt (e.g., "analyze test coverage and suggest improvements"). The agent executes in the cloud with full access to your environment.

You can continue conversing with the agent in real-time, watch its progress, and provide additional guidance as it works autonomously on your task.

> [!tip]
> Your cloud agent is now running in Warp's infrastructure (not on your machine). It clones your repos, runs your setup commands, and starts working on your prompt. The agent has full access to your code and can run tests, make changes, and create artifacts like PRs.

### 5. View run details

You can view details of your agent's run, including commands executed, files changed, and environment used, several different ways:

- Click the session link in your terminal output.

> [!tip]
> Every cloud agent run is auto-tracked. You get a shareable link, a run record, and full visibility into what the agent did. You or your teammates can watch the agent's progress in real-time and even steer it if needed. The run record persists after completion so you can review it later.

### 6. Make it reusable with a skill (optional)

Turn your successful run into a skill that you can reuse:

```
/create-skill
```

Follow the prompts to save your task definition. Once created, you can run it again, schedule it, trigger it from Slack/Linear, or share it with your team.

> [!tip]
> Skills capture successful agent workflows as reusable building blocks. Instead of typing the same prompt repeatedly, you define it once. You can use it yourself, share it with teammates, schedule it to run automatically, or trigger it from integrations. Learn more about [Skills as Agents](https://docs.warp.dev/agent-platform/cloud-agents/skills-as-agents).

**Prefer using the CLI?** See the [Oz CLI Quick Start](https://docs.warp.dev/reference/cli/quickstart) for CLI-based workflows.

## Next steps

Now that you've run your first cloud agent, here are some next steps:

### Automate recurring tasks

[Schedule agents](https://docs.warp.dev/agent-platform/cloud-agents/triggers/scheduled-agents) to run on cron schedules for maintenance tasks like weekly dependency checks or daily dead code cleanup.

### Trigger agents from integrations

| Integration | Description |
|-------------|-------------|
| **Slack** | Tag @Oz in any Slack channel to get immediate help with code reviews, debugging, or incident response. [Learn more](https://docs.warp.dev/agent-platform/cloud-agents/integrations/slack) |
| **Linear** | Connect Oz to Linear to automate bug triage and fixes. Tag @Oz on an issue to reproduce the bug, identify root causes, and open a PR with a fix. [Learn more](https://docs.warp.dev/agent-platform/cloud-agents/integrations/linear) |
| **GitHub Actions** | Run agents in CI/CD pipelines to automate tasks like generating release notes, running security audits, or validating migrations. [Learn more](https://docs.warp.dev/agent-platform/cloud-agents/integrations/github-actions) |

> [!info]
> Integrations require a team on Build, Max, or Business plan.

### Build automations and apps on top of Oz agents

Use the [Oz API & SDK](https://docs.warp.dev/reference/api-and-sdk) to trigger agents programmatically from your own systems and workflows.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Environment creation fails** | Use official Docker Hub images like `node`, `python`, or `rust` for best compatibility. Ensure your GitHub repos are accessible. If using a custom image, avoid Alpine/musl-based images—the agent runtime requires glibc. See [Environments](https://docs.warp.dev/agent-platform/cloud-agents/environments) for more guidance. |
| **Agent can't access repos** | Warp prompts you to authorize GitHub when you create an environment or trigger your first agent. If authorization fails or needs updating, see [How GitHub Authorization works](https://docs.warp.dev/reference/cli/integration-setup#how-github-authorization-works). For automated workflows using team API keys, ensure [team GitHub authorization](https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity#team-github-authorization) is configured in the Admin Panel. Also verify repos are correctly configured in your environment with `oz environment get <ENV_ID>`. |
| **Not enough credits** | Your team needs at least 20 credits available (any type of Warp credits work). Check your credit balance in Settings or see [Access, Billing, and Identity](https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity) for details. |

## What to explore next

Now that you've run your first cloud agent, automate recurring work or connect agents to your team's tools.

- [**Scheduled Agents quickstart**](https://docs.warp.dev/agent-platform/cloud-agents/triggers/scheduled-agents-quickstart) — Set up an agent to run on a cron schedule.
- [**Integrations quickstart**](https://docs.warp.dev/agent-platform/cloud-agents/integrations/quickstart) — Connect Oz to Slack and Linear.
- [**Skills**](https://docs.warp.dev/agent-platform/warp-agents/skills) — Turn successful agent workflows into reusable instructions.