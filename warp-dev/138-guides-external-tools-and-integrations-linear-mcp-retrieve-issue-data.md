---
title: 'Linear MCP: Retrieve Issue Data | Guides | Warp'
url: https://docs.warp.dev/guides/external-tools-and-integrations/linear-mcp-retrieve-issue-data
source: sitemap
fetched_at: 2026-04-29T15:06:46.705939318-03:00
rendered_js: false
word_count: 193
summary: This document provides instructions on configuring and connecting a Linear MCP server within the Warp terminal to enable AI agents to interact with Linear workspace data.
tags:
    - warp-terminal
    - linear-integration
    - mcp-server
    - ai-agent
    - workflow-automation
category: tutorial
optimized: true
optimized_at: 2026-04-29T15:06:46.705939318-03:00
---
Connect the Linear MCP server in Warp so your AI agent can access live data — issues, tickets, and user assignments — directly from your Linear workspace.

## Overview

This tutorial covers:

- Adding and configuring a Linear MCP server in Warp
- Using MCP to query and retrieve issue data

## 1. Adding the Linear MCP Server

### Add a new server in Warp

1. Open Warp Drive → Personal → MCP Servers. Alternatively, press `⌘P` and type **MCP servers** to open the palette
2. Click **Add New Server**
3. Paste in this JSON:

```json
{
  "linear": {
    "command": "npx",
    "args": ["-y", "mcp-remote", "https://mcp.linear.app/sse"],
    "env": {},
    "working_directory": null
  }
}
```

4. Click **Save**
5. Warp starts the server immediately; you should see Linear MCP listed as **Running**

## 2. Testing the Connection

After saving, retry your earlier query:

```
Show me all Linear tasks assigned to me.
```

Warp's agent calls the Linear MCP server to fetch your data. Click inside the response panel to inspect the **raw API response** — ideal for debugging or understanding what's being fetched.

If the server can't find your user, it may be due to your Linear login address. Try querying a teammate to confirm the connection:

```
Show tasks assigned to [teammate name].
```

Once verified, the agent displays a full list of tasks.

#warp-terminal #linear-integration #mcp-server #ai-agent #workflow-automation
