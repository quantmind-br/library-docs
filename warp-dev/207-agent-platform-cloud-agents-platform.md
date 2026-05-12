---
title: Oz platform | Agents | Warp
url: https://docs.warp.dev/agent-platform/cloud-agents/platform
source: sitemap
fetched_at: 2026-04-29T15:04:19.939402782-03:00
rendered_js: false
word_count: 1067
summary: This document provides an overview of the Oz Platform architecture, detailing how cloud agents are triggered, orchestrated, executed in isolated environments, and monitored via CLI, API, and SDKs.
tags:
    - cloud-agents
    - orchestration
    - developer-tools
    - automation
    - api-integration
    - workflow-management
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Cloud agents run on the **Oz Platform**: a consistent way to trigger work, orchestrate and track tasks, execute agents (in optional environments), and inspect outcomes with team visibility.

**Production flow:**

1. **Trigger** fires (schedule, integration, CI, webhook, API, manual)
2. **Orchestration layer** creates task and tracks lifecycle
3. **Agent executes** on a host, optionally in an environment
4. **Persistent record** produced (status, metadata, transcript, outputs)

## Key concepts

| Term | Definition |
|------|------------|
| **Trigger** | Event that starts work (cron, Slack mention, PR opened, CI failure, "run now") |
| **Task** | Unit of work Warp tracks: inputs, state, metadata, execution record |
| **Context** | Additional inputs attached to a task (Slack message, PR metadata, CI logs) |
| **Outputs** | What the task produced (PR, Slack reply, report, transcript + summary) |

In practice: **triggers create tasks; tasks execute on a host (optionally in an environment); tasks produce outputs.**

## Oz CLI

The [Oz CLI](https://docs.warp.dev/reference/cli) is the headless interface for running Oz agents non-interactively—commonly used in CI, scripts, and server environments.

Key property: **cloud-connected**. Even when started locally or in CI, agents report progress to Warp's servers, enabling team visibility and programmatic tracking.

### When to use the CLI

- Run an agent anywhere (local machine, CI runner, remote dev box, server)
- External system orchestrating runs (GitHub Actions, custom automation)
- Task observability and auditing without requiring Warp desktop

### How it fits in the Oz Platform

- Authenticates as you (or team member)
- Starts work by creating a task in orchestrator
- Streams progress back to Warp for observability
- Optionally attaches an environment and configuration

## Warp Orchestrator

The orchestration layer manages cloud agent task lifecycle: creates tasks, tracks state transitions, is system of record.

### What the orchestrator does

- Runs on Warp's servers (cloud control plane)
- Creates tasks when triggers fire
- Tracks lifecycle state (`created` → `running` → `completed`/`failed`)
- Powers SDKs (TypeScript/Python) for programmatic usage

### When teams use the API/SDK

- Triggering agents from custom internal systems (incident tools, bots)
- Building internal dashboards or monitoring
- Coordinating many runs (fanout, sharding, queueing, retries)
- Creating higher-level workflows using tasks as building blocks

## Environments

[Environments](https://docs.warp.dev/agent-platform/cloud-agents/environments) define the execution context an agent runs in.

**An Environment typically includes:**

| Component | Description |
|-----------|-------------|
| **Docker image** | Toolchain and runtime |
| **Repository/workspace** | One or more repos to clone |
| **Setup commands** | Dependency install, bootstrapping |
| **Environment variables** | Optional runtime settings |

> [!info]
> Environments ensure agent runs are consistent across triggers (Slack, CI, schedules) and hosts.

### Environments are optional

Agents can run without an environment (existing local checkout, CI workspace). Move to environments when you want stronger reproducibility, isolation, and standardization.

### When to use environments

- Agent needs consistent toolchain (linters, build tools, language runtimes)
- Want repeatable execution across CI and cloud
- Want standard execution across a team
- Reduce "works on my machine" variability

## Oz API and SDK

The Oz [Agent API](https://docs.warp.dev/reference/api-and-sdk/agent) is the HTTP interface to the Oz Platform.

**What you can do:**

- Run an agent by submitting a prompt + optional configuration
- Monitor execution by listing tasks and tracking state transitions
- Inspect results by fetching task details (prompt, metadata, session link, resolved config)

### Oz Agent SDKs

Official [Python](https://github.com/warpdotdev/oz-sdk-python) and [TypeScript](https://github.com/warpdotdev/oz-sdk-typescript) SDKs provide:

- Typed requests/responses
- Built-in retries and timeouts
- Consistent error types mapped to API status codes
- Helpers for raw responses

> [!info]
> SDKs are typically the quickest and safest starting point for integrations.

### SDK vs raw REST

| Approach | Best for |
|----------|----------|
| **SDK** | Strong typing, standardized error handling, easy concurrency |
| **Raw REST** | Minimal dependencies, full HTTP client control |

## Execution hosts

A host describes where the agent executes. Warp supports multiple execution models:

| Host type | Description |
|-----------|-------------|
| **Warp-hosted (default)** | Warp runs the environment on Warp-managed infrastructure |
| **Self-hosted** | Agent runs on customer-managed infrastructure; Oz still manages lifecycle and observability |

> [!info]
> **Enterprise feature**: Self-hosted execution requires Enterprise plan. See [Self-Hosting](https://docs.warp.dev/agent-platform/cloud-agents/self-hosting).

## Integrations

[Integrations](https://docs.warp.dev/agent-platform/cloud-agents/integrations) connect external events to cloud agent tasks. When an event occurs, Warp creates a task with relevant context.

### First-party integrations

Warp manages event subscription and context extraction end-to-end. Examples:
- [Slack](https://docs.warp.dev/agent-platform/cloud-agents/integrations/slack): message text, channel, thread, user identity
- [GitHub](https://docs.warp.dev/agent-platform/cloud-agents/integrations/github-actions): PR metadata, diffs, labels, check results
- CI: logs, job metadata, artifacts

### Custom integrations

You own the webhook and event-handling logic. Apply filtering/enrichment, then call the API or SDK to create a task.

**Best for:**
- Internal event sources (custom tooling, proprietary systems)
- Custom filtering, routing, or enrichment before triggering
- Custom permissioning, queueing, or governance around triggers

## Secrets

Cloud agents often need credentials for external systems (APIs, cloud providers, databases, MCP servers). Warp provides a [secrets store](https://docs.warp.dev/agent-platform/cloud-agents/secrets) that injects secrets at runtime without exposing values in logs or UI.

### What secrets are for

- API keys and tokens (GitHub, Slack, Linear, internal APIs)
- Shared team credentials (cloud providers, CI identities)
- Database credentials (read-only query bots, reporting)
- MCP server credentials

### Scoping and control

| Scope | Description |
|-------|-------------|
| **Team secrets** | Shared credentials available to the team |
| **Personal secrets** | Credentials tied to an individual |

## Management and observability

Cloud agents are designed for team visibility:

- **[Management UI](https://docs.warp.dev/agent-platform/cloud-agents/managing-cloud-agents)**: lists tasks, status, timing, metadata, history
- **[Agent Session Sharing](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/session-sharing)**: attach to running tasks to monitor/steer
- **[APIs/SDKs](https://docs.warp.dev/reference/api-and-sdk/agent)**: query task history, build monitoring, generate reports

### Access control

- Teams can restrict who can run, view, or intervene in agent tasks
- Organizations can enable system-wide visibility for auditing

## Centralized configuration

Cloud agent setups often include shared configuration. Warp supports centralized configuration so settings apply consistently regardless of where a task is launched—useful when the same workflow triggers from multiple sources (Slack, CI, schedules).

## Using the Oz Platform with or without the Warp app

[Cloud agents](https://docs.warp.dev/agent-platform/cloud-agents/overview) do not require Warp's desktop terminal. Teams can operate cloud agent workflows using:
- [Session sharing](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/session-sharing) — attach to running tasks to monitor or steer

**If using Warp's terminal:**
- Tasks launched via CLI can be handed off into an interactive session for review/edits/continuation
- Human checkpoints without losing the audit trail from the cloud agent run
