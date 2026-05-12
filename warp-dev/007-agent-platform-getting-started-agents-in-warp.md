---
title: Agents in Warp | Agents | Warp
url: https://docs.warp.dev/agent-platform/getting-started/agents-in-warp
source: sitemap
fetched_at: 2026-04-29T15:03:43.920859773-03:00
rendered_js: false
word_count: 704
summary: This document provides an overview of Warp's Oz agent system, detailing how it assists with coding tasks, manages permissions and autonomy, and integrates with codebase context and external cloud workflows.
tags:
    - ai-coding-assistant
    - agent-autonomy
    - development-tools
    - workflow-automation
    - code-context
    - warp-terminal
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp includes Oz agents. These coding agents are designed to help you build, test, deploy, and debug while keeping you in control. Describe what you want to do in natural language (*you can even use your voice*), and Oz will take action using your environment, codebase, and saved context.

## What Oz agents can do

Oz agents understand your codebase and can execute tasks autonomously while keeping you in control:

- **Write and edit code** — Create new files, refactor existing code, or make changes across multiple files in your codebase
- **Debug and fix errors** — Analyze stack traces, interpret error output, and apply fixes
- **Run commands** — Execute shell commands and use the output to guide next steps
- **Recover from errors** — Automatically retry failed operations with adjustments
- **Learn tools** — Integrate with any CLI tool by reading its `--help` or public documentation

> [!example]
> **Try this prompt** — [open in Warp](https://app.warp.dev/drive/prompt/Clone-and-install-Warps-themes-repository-PkK9Zw16SCD3JKzOUoGuj4)

## Agent autonomy

Under **Settings** > **Agents** > **Profiles** > **Permissions**, you can control how much autonomy the agent has when performing different types of actions:

| Action | Description |
|--------|-------------|
| Reading files | |
| Creating plans | |
| Executing commands | |
| Calling MCP servers | |

For each action, set the autonomy level to:

- **Let the agent decide** — The agent chooses when to ask for confirmation
- **Always prompt for confirmation** — Require approval before each action
- **Always allow** — Execute without prompting
- **Never** — Disable this action entirely

You can also configure an **allowlist** and **denylist** for specific commands you always want to run—either with or without confirmation.

## Agent profiles

Profiles let you define different permission and model configurations for different contexts. Create and manage profiles in **Settings** > **Agents** > **Warp Agent**, then switch between them by clicking the profile icon in Warp's input area.

Common profile patterns:

| Pattern | Use Case |
|---------|----------|
| **Default** | Balanced permissions for everyday use |
| **YOLO mode** | Loose permissions for personal projects where you want the agent to move fast |
| **Prod mode** | Restrictive permissions ("Always Ask") for high-risk environments like production servers |

For more details, see [Agent Profiles & Permissions](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/agent-profiles-permissions).

## Managing agents

You can run multiple Oz agents simultaneously in Warp. All active agents—both local conversations and cloud agent runs—are tracked in the [management view](https://docs.warp.dev/agent-platform/cloud-agents/managing-cloud-agents).

Agents notify you when they need input, such as permission to run a command or approval to apply a code diff. This lets you focus on other work, knowing you'll be alerted when your attention is required.

To access conversations across devices, share them with teammates, or restore past conversations, enable [cloud-synced conversations](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/cloud-conversations).

## Context and knowledge

Oz agents work best when they understand your codebase and workflows. Warp provides several ways to give agents the context they need:

- [**Codebase Context**](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/codebase-context) — Warp indexes your Git-tracked files so agents can search and understand your code
- [**Rules**](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/rules) — Define global and project-level guidelines that shape agent behavior
- [**Skills**](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/skills) — Reusable instructions that teach agents how to perform specific tasks
- [**MCP Servers**](https://docs.warp.dev/agent-platform/warp-agents/agent-context/mcp) — Connect external tools and data sources (GitHub, Linear, databases) to your agents

## Third-Party CLI Agents

In addition to Warp's built-in Oz agent, Warp provides first-class support for third-party CLI coding agents like Claude Code, Codex, and OpenCode. Run any supported agent inside Warp and get rich input, code review, agent notifications, vertical tabs with agent metadata, and more.

→ [Learn about Third-Party CLI Agents](https://docs.warp.dev/agent-platform/third-party-agents/overview)

## From local to cloud

The same Oz agent capabilities that power interactive conversations in Warp also run in the cloud. Cloud agents can:

- React to events from Slack, Linear, or GitHub
- Run on schedules for recurring tasks like dependency updates
- Execute in parallel across repos or tasks
- Produce tracked, auditable, shareable runs

Cloud agents are ideal for work that doesn't need your immediate attention—PR reviews, issue triage, routine maintenance, and integration-driven workflows.

→ [Learn about Cloud Agents](https://docs.warp.dev/agent-platform/cloud-agents/overview)

## Resources

- [**Oz web app**](https://oz.warp.dev) — Create runs, manage schedules, browse skills, and configure integrations
- [**Capabilities**](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview) — All agent capabilities: planning, task lists, model choice, and more