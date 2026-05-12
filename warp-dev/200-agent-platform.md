---
title: Agents overview | Agents | Warp
url: https://docs.warp.dev/agent-platform
source: sitemap
fetched_at: 2026-04-29T15:03:43.538502419-03:00
rendered_js: false
word_count: 317
summary: This document introduces Oz, Warp's orchestration platform designed for managing, deploying, and running autonomous coding agents at scale.
tags:
    - warp-terminal
    - oz-platform
    - agent-orchestration
    - cloud-agents
    - developer-tools
    - automation
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp includes **Oz**, the orchestration platform for cloud agents. While Warp provides the terminal and coding surface you work in day-to-day, Oz is the underlying orchestration layer that makes running agents at scale possible.

Warp's client is [open source under AGPL v3](https://github.com/warpdotdev/warp/blob/master/LICENSE), so the editor and terminal that host your agents are fully auditable. See [Contributing to Warp](https://docs.warp.dev/support-and-community/community/contributing) for the source and contribution flow.

With Oz, you can:
- Run interactive agent conversations in Warp for real-time coding assistance
- Deploy autonomous agents that run in the cloud from triggers, schedules, or integrations
- Coordinate multiple agents concurrently across machines, repos, and teams
- Track, audit, and share agent activity with full visibility into what ran and what it did

Oz is fully programmable—launch agents manually or build custom logic around them with triggers, schedules, environments, and your choice of hosting (Warp's cloud or your own).

---

## Key capabilities

- [**Local Agents**](199-agent-platform-warp-agents-warp-agents.md) — interactive Oz agents embedded in Warp with natural language coding, debugging, and terminal access
- [**Third-Party CLI Agents**](https://docs.warp.dev/agent-platform/third-party-agents/overview) — use Claude Code, Codex, OpenCode, and other CLI coding agents in Warp with rich input and notifications
- [**Oz Cloud Agents**](https://docs.warp.dev/agent-platform/cloud-agents/overview) — autonomous agents that run in the cloud in response to system events, schedules, or integrations
- [**Integrations**](https://docs.warp.dev/agent-platform/cloud-agents/integrations) — connect external events to autonomous agent execution via [Slack](https://docs.warp.dev/agent-platform/cloud-agents/integrations/slack), [Linear](https://docs.warp.dev/agent-platform/cloud-agents/integrations/linear), [GitHub Actions](https://docs.warp.dev/agent-platform/cloud-agents/integrations/github-actions), and more
- [**Oz Platform**](https://docs.warp.dev/agent-platform/cloud-agents/platform) — CLI, API/SDK, orchestration, environments, secrets, and management/observability

---

## Getting started

- [**Agents in Warp**](https://docs.warp.dev/agent-platform/getting-started/agents-in-warp) — start using Oz agents interactively in Warp
- [**Oz web app**](https://oz.warp.dev) — create runs, manage schedules, browse skills, and configure integrations
- [**Oz CLI**](https://docs.warp.dev/reference/cli) — run agents from the command line, in CI, or on remote machines

---

## Learn more

- [Oz Platform](https://docs.warp.dev/agent-platform/cloud-agents/platform) — CLI, API/SDK, orchestration, environments, and hosts
- [Environments](https://docs.warp.dev/agent-platform/cloud-agents/environments) — configure execution context for cloud agents
- [Integrations](https://docs.warp.dev/agent-platform/cloud-agents/integrations) — Slack, Linear, GitHub Actions, and custom integrations
