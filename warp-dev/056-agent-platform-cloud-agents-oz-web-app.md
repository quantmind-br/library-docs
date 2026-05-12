---
title: Oz web app | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/oz-web-app
source: sitemap
fetched_at: 2026-04-29T15:04:37.404354351-03:00
rendered_js: false
word_count: 914
summary: This document provides an overview of the Oz web application, a visual interface for managing, monitoring, and configuring cloud agents and their environments.
tags:
    - cloud-agents
    - web-dashboard
    - agent-management
    - workflow-automation
    - integration-configuration
category: guide
optimized: true
optimized_at: 2026-04-29T15:04:37.404354351-03:00
---
The [Oz web app](https://oz.warp.dev) provides a visual interface for managing cloud agents — start runs, browse agents, create schedules, configure environments, and set up integrations without installing Warp or using the CLI.

> [!info]
> The Oz web app works on mobile devices for monitoring from anywhere.

[Watch the demo](https://oz.warp.dev) to create an environment and run an agent.

## Quick reference

### When to use the web app

- **Monitor agent activity** — View runs, check status, inspect outputs from any device
- **Start quick runs** — Dispatch agents without opening a terminal
- **Manage schedules visually** — Create and edit scheduled agents with a guided interface
- **Configure environments** — Set up repos, Docker images, and setup commands
- **Set up integrations** — Connect Slack and Linear with a guided setup flow

For scripting, automation, and CI/CD, use the [Oz CLI](https://docs.warp.dev/reference/cli) or [API](https://docs.warp.dev/reference/api-and-sdk/agent).

## Getting started

On first sign-in, a guided onboarding flow asks "What brings you to Oz?" with three paths:

- **Create an agent automation** — Set up a scheduled agent, integration-triggered agent, or other automation
- **Run Oz Cloud Agents in Warp** — Open the Warp desktop app (or download page) for interactive cloud agents
- **Build an app that uses agents** — Link to [Oz Platform](https://docs.warp.dev/agent-platform/cloud-agents/platform) docs for CLI, SDK, or API usage

Skip onboarding anytime to go directly to the Runs page.

## Dashboard

The **Dashboard** page (`/dashboard`) provides quick access to common actions.

### Quick actions

Four action cards:
- **New run** — Start a cloud agent run
- **New agent** — Create a new skill
- **New schedule** — Set up a scheduled agent
- **New environment** — Configure a new execution environment

Each action opens a guided side pane without leaving the Dashboard.

### Suggested agents

Curated list of pre-built skills from Warp's public [oz-skills repository](https://github.com/warpdotdev/oz-skills). Click **Run** on any suggested agent to start a run.

### Recent agents

Last three agents you've run. If none yet, prompts guide you to start a run or create your first agent.

### Featured reads

Curated articles and documentation (visible on desktop).

## Runs

The **Runs** page (`/runs`) shows all runs across your account — CLI, API, integrations, and schedules.

### Run details

Each run displays: status, source, creator, start time, duration, and environment. Click any run to view the full transcript, artifacts, and metadata.

### Filtering and search

Search by title, prompt, or skill name. Add advanced filters for source, status, creator, and date range.

### Starting a new run

> [!info]
> Click **New run** in the header.

1. **Select an agent (optional)** — Choose a skill as base instructions, or select "Quick run"
2. **Select an environment** — Choose which environment the agent runs in
3. **Add a prompt** — Provide context and instructions for this run

## Agents

The **Agents** page (`/agents`) shows all skills from your environments plus suggested skills from [oz-skills](https://github.com/warpdotdev/oz-skills).

### Skill details

Each skill displays: name, description, environment, last run, and source.

Filter by environment or switch to the **Suggested** tab for pre-built skills (code review, dependency updates, documentation sync).

### Running a skill as an agent

Click any skill to view details, then click **Run** to start an agent. Alternatively, click **New run** from the header.

> [!info]
> For details on how skills work with cloud agents, see [[058-agent-platform-cloud-agents-self-hosting-managed-docker|Skills as Agents]].

### Creating new agents

Click **New agent** to create a new skill. The guided flow helps define instructions available for future runs.

## Schedules

The **Schedules** page (`/schedules`) manages scheduled agents that run automatically on cron schedules.

### Schedule details

Each schedule displays: name, frequency, environment, agent, last run, and next run.

### Creating a schedule

> [!info]
> Click **New schedule** in the header.

1. **Name** — Descriptive name
2. **Frequency** — Cron schedule (with presets for common patterns)
3. **Environment** — Select environment to run in
4. **Agent (optional)** — Choose a skill
5. **Prompt** — Define what the agent should do

### Managing schedules

Click any schedule to view details and recent run history. From the detail pane:
- **Edit** the schedule configuration
- **Pause** or **enable** the schedule
- **Delete** the schedule
- **View past runs** triggered by this schedule

## Environments

The **Environments** page (`/environments`) shows all environments configured for your account. Environments define the execution context including repos, Docker images, and setup commands.

### Environment details

Each environment displays: name, Docker image, repositories, setup commands, and last used.

### Creating an environment

> [!info]
> Click **New environment** in the header.

1. **Name** — Descriptive name
2. **Docker image** — Specify a Docker image (Warp provides prebuilt dev images, or use your own)
3. **Repositories** — Add GitHub repos the agent should access
4. **Setup commands** — Define commands to run when the environment starts (e.g., `npm install`)

## Integrations

The **Integrations** page (`/integrations`) configures first-party integrations with Slack and Linear.

### Available integrations

| Integration | Description |
|-------------|-------------|
| Slack | Trigger agents from Slack messages and receive run notifications |
| Linear | Trigger agents from Linear issues and update issue status |

### Setting up an integration

Click an integration to start the guided setup flow. Authorize Warp to connect with the external service, select an environment, and configure integration-specific settings.

> [!info]
> For detailed setup instructions, see [[053-agent-platform-cloud-agents-integrations-slack|Slack]] and [[052-agent-platform-cloud-agents-integrations-linear|Linear]] integrations.

## Related pages

- [[058-agent-platform-cloud-agents-self-hosting-managed-docker|Skills as Agents]] — Run agents based on reusable skill definitions
- [[205-agent-platform-cloud-agents-environments|Environments]] — Configure runtime context for cloud agents