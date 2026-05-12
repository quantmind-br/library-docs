---
title: Blocks as context | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/agent-context/blocks-as-context
source: sitemap
fetched_at: 2026-04-29T15:04:05.00060933-03:00
rendered_js: false
word_count: 299
summary: This document explains how to manage and attach terminal blocks as context in Warp's AI Agent to improve response accuracy. It covers keyboard shortcuts, UI interaction methods, and the distinction between terminal and conversation block visibility.
tags:
    - warp-terminal
    - ai-agent
    - context-management
    - developer-tools
    - terminal-workflow
    - command-line
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
The Agent uses terminal blocks as context to understand queries and generate more relevant responses. The most common use case is attaching an error to ask "fix it."

## Attaching blocks

Click the AI sparkles icon on any block and select **Attach as context**.

From within Agent Mode, use these shortcuts to attach or clear context:

| Shortcut | Action |
|----------|--------|
| `CMD-UP` | Attach previous block as context |
| `CMD-DOWN` | Clear blocks from context |
| `CMD` + click | Extend block selection |
| `CMD` + click attached | Remove from context |

> [!info]
> With "Pin to the top" [Input Position](https://docs.warp.dev/terminal/appearance/input-position), direction is reversed: `CMD-DOWN` attaches and `CMD-UP` clears.

## Block visibility across views

Blocks belong to either the terminal view or a specific agent conversation:

- **Terminal blocks** — Commands run directly in the terminal. Appear in the terminal blocklist and can be attached to multiple conversations.
- **Agent conversation blocks** — Commands executed within an agent conversation (by you or the agent). Visible only within that conversation, keeping the terminal view clean.

## Automatic context in agent conversations

Any shell command run inside an agent conversation is automatically included as context for your next query:

1. Run a command to see its output
2. Ask the agent about the results — the output is already part of the context

Manually attach terminal view blocks for commands run outside the conversation.

## Pending vs attached context

When you select blocks in terminal view and start a new conversation:

- **Pending context** — Blocks selected before the conversation starts. Deselect with `ESC` or `CMD-K` (macOS) / `CTRL-K` (Windows/Linux) to remove them.
- **Attached context** — Once you submit your first query, pending blocks become permanently attached to the conversation.

#ai-agent #context-management #terminal-workflow
