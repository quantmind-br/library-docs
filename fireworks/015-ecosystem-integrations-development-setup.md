---
title: Development Setup with Fireworks Docs MCP - Fireworks AI Docs
url: https://docs.fireworks.ai/ecosystem/integrations/development-setup
source: sitemap
fetched_at: 2026-04-27T20:15:47.773364415-03:00
rendered_js: false
word_count: 89
summary: This document explains various methods to add and utilize an MCP (Multi-Client Platform) server, specifically linking to Fireworks AI documentation, enabling AI coding agents to search that documentation.
tags:
    - mcp
    - claude
    - fireworks-docs
    - ai-agent
    - configuration
    - documentation
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
## Claude Code

Add the MCP server via CLI:

```bash
claude mcp add --transport http fireworks-docs https://docs.fireworks.ai/mcp
```

Or add to your project's `mcp.json`:

```json
{
  "mcpServers": {
    "fireworks-docs": {
      "url": "https://docs.fireworks.ai/mcp"
    }
  }
}
```

## Cursor

One-click install: [Install Fireworks Docs MCP](https://cursor.com/en/install-mcp?name=fireworks-docs&config=eyJ1cmwiOiJodHRwczovL2RvY3MuZmlyZXdvcmtzLmFpL21jcCJ9)

Or manually add to your workspace's `mcp.json`:

```json
{
  "mcpServers": {
    "fireworks-docs": {
      "url": "https://docs.fireworks.ai/mcp"
    }
  }
}
```

## Using the MCP Server

Once configured, your AI coding agent can search the full Fireworks AI documentation. Example queries:

- "How do I configure autoscaling for deployments?"
- "What parameters does the chat completions endpoint accept?"
- "Show me examples of function calling with Fireworks models"
- "Find the API reference for batch inference"

#mcp #claude #cursor #ai-agent
