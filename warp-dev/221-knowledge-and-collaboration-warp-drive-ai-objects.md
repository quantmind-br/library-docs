---
title: AI-Integrated Objects | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/ai-objects
source: sitemap
fetched_at: 2026-04-29T15:03:32.845245461-03:00
rendered_js: false
word_count: 384
summary: This document describes the various Warp Drive objects—Rules, MCP Servers, Skills, and Prompts—that enhance Warp agents with personalized guidelines, external tool integrations, and reusable workflows.
tags:
    - warp-drive
    - ai-agents
    - mcp-servers
    - coding-standards
    - workflow-automation
    - agent-configuration
category: concept
optimized: true
optimized_at: 2026-04-29T15:04:00Z
---
Warp Drive includes several object types that integrate with Warp's agents to provide personalized, context-aware assistance.

## Rules

Rules are reusable guidelines that inform how agents respond to your prompts. They help tailor responses to match your coding standards, project conventions, and personal preferences.

**Access from Warp Drive:** **Personal** > **Rules**

Warp supports two types of rules:

- **Global Rules** — Apply across all projects and contexts
- **Project Rules** — Live in your codebase (as `AGENTS.md` or `WARP.md` files) and apply automatically when working within that project

## MCP Servers

MCP (Model Context Protocol) servers extend Warp's agents with custom tools and data sources through a standardized interface. They act as plugins that let agents access external services like GitHub, Sentry, Linear, Slack, and more.

**Access from Warp Drive:** **Personal** > **MCP Servers**

MCP servers can be:

- **CLI-based** — Local commands that Warp launches and manages
- **URL-based** — Remote endpoints using Streamable HTTP or SSE

## Skills

Skills are reusable instruction sets that teach agents how to perform specific tasks. Unlike Rules (which provide guidelines), Skills define complete workflows that agents can invoke when relevant.

Skills are file-based (stored as `SKILL.md` files in your project or home directory) rather than cloud-synced objects, but they integrate closely with Warp Drive workflows.

- **Project Skills** — Live in `.agents/skills/`, `.warp/skills/`, or similar directories in your repository
- **Global Skills** — Live in `~/.agents/skills/` or similar directories in your home folder

## Prompts

Prompts are parameterized natural language queries you can save and reuse with Agent Mode. They allow you to save complex AI workflows and execute them quickly from the Command Palette.

**Access from Warp Drive:** Click **+** and select "Prompt", or browse existing prompts in your personal or team workspace.

> [!info]
> For complete documentation on Prompts, see [Prompts](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/prompts).

## How agents use these objects

When you start an agent conversation, Warp automatically provides relevant context from your Warp Drive objects:

- **Rules** — Guide agent behavior and responses based on your preferences
- **MCP Servers** — Give agents access to external tools and data sources
- **Skills** — Provide task-specific instructions agents can invoke
- **Prompts** — Let you trigger predefined workflows quickly

When an object is used as context, it appears in the conversation under "References" or "Derived from."