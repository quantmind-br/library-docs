---
title: Warp Drive prompts | Warp
url: https://docs.warp.dev/knowledge-and-collaboration/warp-drive/prompts
source: sitemap
fetched_at: 2026-04-29T15:03:31.021478723-03:00
rendered_js: false
word_count: 233
summary: This document explains how to create, manage, and execute parameterized natural language prompts within Warp to streamline AI-powered terminal workflows.
tags:
    - warp-terminal
    - ai-agents
    - prompt-engineering
    - workflow-automation
    - command-palette
    - parameterized-queries
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Prompts are parameterized natural language queries saved in Warp for use with [Agent Mode](https://docs.warp.dev/agent-platform/warp-agents/interacting-with-agents). They are searchable and accessible via the [Command Palette](https://docs.warp.dev/terminal/command-palette), enabling reusable AI workflows.

## Save and edit prompts

Create a prompt from Warp Drive by clicking `+` and selecting **Prompt**.

Fields:
- Name
- Natural language query with arguments (`{{argument}}`)
- Description indexed for search (optional)
- Arguments with descriptions and default values (optional)

Prompts can be edited anytime with an internet connection.

## Working with arguments

Add arguments manually via **New argument** or by typing `{{argument}}` in the command field. Selecting text and clicking **New argument** wraps it in curly braces.

**Rules:**
- Valid characters: `A-Za-z0-9`, hyphens `-`, underscores `_`
- First character cannot be a number

Arguments are **text** type by default. For **enum** type, see [Enum type arguments in Workflows](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/workflows#enum-type-arguments). Enum arguments show suggestions via `SHIFT-TAB`.

## Team editing

Shared prompts sync immediately for all team members. If edited by another member or device simultaneously, you must check out the latest version before saving.

## Execute prompts

Execute via:
- Warp Drive: click the prompt
- [Command Palette](https://docs.warp.dev/terminal/command-palette) or [Command Search](https://docs.warp.dev/terminal/entry/command-search): search by name or type `prompts:`
- `SHIFT-TAB` to cycle through arguments

The prompt is pasted into the active terminal input. Adjust arguments in the input editor before running.

## Import and export

See [Warp Drive Import and Export](https://docs.warp.dev/knowledge-and-collaboration/warp-drive#import-and-export).

#warp-terminal #ai-agents #prompt-engineering #workflow-automation #command-palette #parameterized-queries
