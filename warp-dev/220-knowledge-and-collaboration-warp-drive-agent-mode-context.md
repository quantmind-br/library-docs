---
title: Agent Mode context | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/agent-mode-context
source: sitemap
fetched_at: 2026-04-29T15:03:36.382100381-03:00
rendered_js: false
word_count: 125
summary: This document explains how Warp Agents can access and utilize Warp Drive contents such as workflows, notebooks, and environment variables as context to provide personalized responses.
tags:
    - warp-agents
    - warp-drive
    - context-management
    - developer-workflow
    - mcp-servers
    - agent-configuration
category: concept
optimized: true
optimized_at: 2026-04-29T15:04:00Z
---
[Agent Mode](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents) can leverage your [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive) contents to tailor responses to your personal and team developer workflows and environments.

## Objects used as context

Agents can automatically pull in relevant context from:

- **Workflows** — Saved commands and scripts
- **Notebooks** — Documentation and notes
- **Environment Variables** — Configuration values
- **MCP Servers** — External tools and data sources (see [MCP](https://docs.warp.dev/agent-platform/warp-agents/mcp))

When a Warp Drive object is pulled as context, it appears in the conversation as a citation under "References" or "Derived from".

## Settings

Enabled by default. Toggle in **Settings** > **Agents** > **Knowledge** > **Warp Drive as Agent Mode Context**.

## Related

- [AI-Integrated Objects](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/ai-objects) — Rules, MCP Servers, Skills, and Prompts
- [Prompts](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/prompts) — Save and reuse parameterized agent prompts