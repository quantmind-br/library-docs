---
title: Slash commands | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/slash-commands
source: sitemap
fetched_at: 2026-04-29T15:03:47.035896516-03:00
rendered_js: false
word_count: 199
summary: This document explains how to access and utilize slash commands within Warp's Agent and Auto-Detection modes to execute built-in tasks and custom agent prompts.
tags:
    - slash-commands
    - agent-mode
    - workflow-automation
    - productivity
    - terminal-tools
    - command-line-interface
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
In Agent Mode or Auto-Detection Mode, type `/` in the input field to open the Slash Commands menu. The menu filters results in real time as you type.

## Static slash commands

Warp supports the following built-in Slash Commands:

| Command | Description | Credits |
|---------|-------------|---------|
| `/init` | Initialize a new project | ✅ (consumes credits*) |
| `/review` | Review code changes | ✅ |
| `/test` | Generate tests for selected code | ✅ |
| `/fix` | Fix errors in selected code | ✅ |
| `/explain` | Explain selected code | ❌ |

> [!warning]
> Commands marked with `*` consume credits.

## Agent Prompts via Slash Commands

The menu also shows [Agent Prompts](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/prompts) saved in your [Warp Drive](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/) — custom prompts you've created or ones shared with you. Filter by typing after `/` to run them without leaving the input field.

## Tips

- **Context-aware** — Many slash commands use your current working directory or file selection as context.
- **Quick access** — Press `/` from anywhere in Agent Mode or Auto-Detection Mode.

## Example

Running `/init` opens the initialization flow with guided prompts for your project setup.

#slash-commands #agent-mode #workflow-automation #productivity
