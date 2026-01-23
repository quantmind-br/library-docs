---
title: Using MCP Apps and MCP-UI | goose
url: https://block.github.io/goose/docs/guides/interactive-chat/mcp-ui
source: github_pages
fetched_at: 2026-01-22T22:13:58.319556925-03:00
rendered_js: true
word_count: 225
summary: This document introduces interactive user experiences in goose Desktop using MCP Apps and MCP-UI, explaining how developers can build graphical, clickable elements for dynamic interactions.
tags:
    - goose-desktop
    - mcp-apps
    - mcp-ui
    - interactive-ui
    - extension-development
    - user-interface
category: guide
---

Extensions built with MCP Apps or MCP-UI allow goose Desktop to provide interactive and engaging user experiences. Imagine using a graphical, clickable UI instead of reading text responses and typing all your prompts. These extensions return content that goose can render as embedded UI elements for rich, dynamic, and streamlined interactions.

MCP Apps is the official specification

[MCP Apps](https://block.github.io/goose/docs/tutorials/building-mcp-apps) is now the official MCP specification for interactive UIs. MCP-UI extensions still work in goose, but MCP Apps is the recommended path for new extensions.

Your browser does not support the video tag.

## Try It Out[​](#try-it-out "Direct link to Try It Out")

See how interactive responses work in goose. For this exercise, we'll add an extension that connects to [MCP-UI Demos](https://mcp-aharvard.netlify.app/) provided by Andrew Harvard.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?type=streamable_http&url=https%3A%2F%2Fmcp-aharvard.netlify.app%2Fmcp&id=richdemo&name=Rich%20Demo&description=Demo%20interactive%20extension)
2. Click `Yes` to confirm the installation
3. Click the button in the top-left to open the sidebar
4. Navigate to the chat

In goose Desktop, ask:

- `Help me select seats for my flight`

Instead of just text, you'll see an interactive response with:

- A visual seat map with available and occupied seats
- Real-time, clickable selection capabilities
- A booking confirmation with flight details

Try out other demos:

- `Plan my next trip based on my mood`
- `What's the weather in Philadelphia?`

## For Extension Developers[​](#for-extension-developers "Direct link to For Extension Developers")

Add interactivity to your own extensions:

- [Building MCP Apps](https://block.github.io/goose/docs/tutorials/building-mcp-apps) - Step-by-step tutorial (recommended)
- [MCP-UI Documentation](https://mcpui.dev/guide/introduction) - MCP-UI specification