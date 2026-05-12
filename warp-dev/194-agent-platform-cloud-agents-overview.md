---
title: Cloud agents overview | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/overview
source: sitemap
fetched_at: 2026-04-29T15:04:18.117786464-03:00
rendered_js: false
word_count: 693
summary: This document provides an overview of Oz Cloud Agents, explaining their architecture, trigger mechanisms, observability features, and deployment models for continuous engineering automation.
tags:
    - cloud-agents
    - automation
    - infrastructure
    - observability
    - orchestration
    - task-management
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Oz Cloud Agents are cloud-connected background agents that run on the [Oz Platform](https://docs.warp.dev/agent-platform/cloud-agents/platform). Start with the [[194-agent-platform-cloud-agents-overview|Cloud Agents Quick Start]] to run your first agent in ~10 minutes.

## What cloud agents are designed for

- **React to system events** — crashes, bug reports, Slack interactions, cron timers, CI steps
- **Provide observability** — see what ran, when, and what it did across teams
- **Scale parallelism** — run many tasks concurrently, shard repo-wide tasks across runs, fan out to multiple targets
- **Operate continuously** — scheduled maintenance, integration-driven automation

## What is a cloud agent run?

A **run** is a task created when a trigger fires (webhook, schedule) or a user starts it explicitly. Each task includes:

| Component | Description |
|---|---|
| **Inputs** | Prompt + context from triggering system (Slack message, PR metadata, CI logs) |
| **Execution context** | Optional [Environment](https://docs.warp.dev/agent-platform/cloud-agents/environments) defining repo, image, startup commands |
| **Lifecycle state** | `created → running → completed / failed` |
| **Persistent record** | Status, metadata, session transcript |

> [!info]
> If you can define (1) what triggers it, (2) what context it needs, and (3) how the team will inspect the output — it's a good fit for a cloud agent.

## How cloud agents work

Cloud agents run on the [Oz Platform](https://docs.warp.dev/agent-platform/cloud-agents/platform), which provides primitives for triggering, orchestration, execution, secret injection, and result inspection.

1. Something **triggers** an agent task
2. The **orchestrator** creates and tracks the task
3. The **agent executes** on a host (optionally inside an [Environment](https://docs.warp.dev/agent-platform/cloud-agents/environments)) with needed [Secrets](https://docs.warp.dev/agent-platform/cloud-agents/secrets)

Execution can be Warp-hosted or self-hosted (managed Docker daemon on your machines, or unmanaged `oz agent run` in CI/Kubernetes). See [Self-Hosting](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting) for details.

## What you get by default

### Codebase Context

Agent runs automatically benefit from [Codebase Context](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/codebase-context) for semantic code understanding — as long as Codebase Context is enabled for your account.

### Observability and steerability

- [Agent Session Sharing](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/session-sharing) — authorized teammates attach to running tasks to monitor and steer
- Session transcripts and task metadata for post-run review

### Centralized configuration

Shared configuration (MCP servers, rules, saved prompts, environment variables, [Secrets](https://docs.warp.dev/agent-platform/cloud-agents/secrets)) applies consistently across all triggers (Slack + CI + schedules) without duplicating setup. See [MCP Servers](https://docs.warp.dev/agent-platform/cloud-agents/mcp) for details.

### API access to tasks

The [Oz API and SDKs](https://docs.warp.dev/reference/api-and-sdk) let teams query running/completed tasks, fetch metadata and outcomes, and build internal dashboards (success rates, runtime, failure reasons).

## Using cloud agents with or without the Warp app

Cloud agents do not require the Warp desktop app. Deploy and operate via the [Oz Platform](https://docs.warp.dev/agent-platform/cloud-agents/platform):

- [Oz web app](https://docs.warp.dev/agent-platform/cloud-agents/oz-web-app) — visual interface for managing runs, schedules, environments, and integrations (works on mobile)

If your team also uses Warp's terminal, CLI-launched tasks can hand off into an interactive session for review or continuation.

## Billing and plan requirements

Cloud agents and [integrations](https://docs.warp.dev/agent-platform/cloud-agents/integrations) run on the Oz Platform control plane and consume Warp credits.

> [!info]
> [BYOK](https://docs.warp.dev/support-and-community/plans-and-billing/bring-your-own-api-key) is **not supported** for cloud agent runs. BYOK keys are stored locally and inaccessible to cloud-hosted agents.

| Runner type | Requirements |
|---|---|
| **CLI/API (individual)** | Warp-hosted infrastructure; no team required |
| **Self-hosted agents** | Team subscription required |
| **Integrations (Slack/Linear)** | Warp team required; supported plans: Build, Max, Business (not Pro/Turbo/Lightspeed/legacy Business); at least 20 credits available |

> [!warning]
> If credit balance reaches zero, cloud agent runs will not execute until credits are replenished. See [Access, Billing, and Identity Permissions](https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity) for full details.

## Learn more

- [Oz Platform](https://docs.warp.dev/agent-platform/cloud-agents/platform) — CLI, Oz API/SDK, orchestration, tasks, environments, hosts, integrations
- [Skills as Agents](https://docs.warp.dev/agent-platform/cloud-agents/skills-as-agents) — run agents from reusable skill definitions on a schedule
- [Oz CLI](https://docs.warp.dev/reference/cli) — non-interactive agent runs from CI, scripts, remote machines
- [Environments](https://docs.warp.dev/agent-platform/cloud-agents/environments) — runtime context for agent tasks
- [Oz API and SDK](https://docs.warp.dev/reference/api-and-sdk) — REST API for creating, querying, monitoring tasks programmatically
- [Agent Secrets](https://docs.warp.dev/agent-platform/cloud-agents/secrets) — safely store, scope, and inject credentials into agent runs
- [MCP Servers](https://docs.warp.dev/agent-platform/cloud-agents/mcp) — configure MCP servers for agent tool access
- [Deployment Patterns](https://docs.warp.dev/agent-platform/cloud-agents/deployment-patterns) — compare common deployment options
- [Access, Billing, and Identity Permissions](https://docs.warp.dev/agent-platform/cloud-agents/team-access-billing-and-identity) — individual and team requirements, credit billing, permission model

#cloud-agents #automation #infrastructure #observability #orchestration #task-management
