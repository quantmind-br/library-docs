---
title: Agent context | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/agent-context
source: sitemap
fetched_at: 2026-04-29T15:04:03.309241723-03:00
rendered_js: false
word_count: 152
summary: This document outlines the various methods for providing ad-hoc information to the Warp Agent to enhance response accuracy and context awareness.
tags:
    - agent-context
    - warp-agent
    - prompt-engineering
    - data-input
    - terminal-tools
category: concept
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
**Agent Context** is ad-hoc information you manually supply during a session to guide Agent behavior and improve response quality.

## Methods for adding context

| Method | Description |
|--------|-------------|
| [Blocks as Context](https://docs.warp.dev/agent-platform/warp-agents/agent-context/blocks-as-context) | Share terminal output to help Agent understand errors, logs, or previous commands |
| [Images as Context](https://docs.warp.dev/agent-platform/warp-agents/agent-context/images-as-context) | Include screenshots, diagrams, or visuals |
| [URLs as Context](https://docs.warp.dev/agent-platform/warp-agents/agent-context/urls-as-context) | Attach public webpages for Agent to extract and reference |
| [Selection as Context](https://docs.warp.dev/agent-platform/warp-agents/agent-context/selection-as-context) | Attach code snippets from editor or review panel |
| [Using @ to Add Context](https://docs.warp.dev/agent-platform/warp-agents/agent-context/using-to-add-context) | Reference files, folders, code symbols, or Warp Drive objects directly in prompts |

Commands run inside an agent conversation are automatically included as context for your next prompt.

## Distinct from persistent context sources

Agent Context is distinct from persistent or automatic sources:
- [Rules](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/rules)
- [Warp Drive as Agent Mode Context](https://docs.warp.dev/warp/knowledge-and-collaboration/warp-drive/agent-mode-context)
- [Model Context Protocol (MCP)](https://docs.warp.dev/agent-platform/warp-agents/agent-context/mcp)
