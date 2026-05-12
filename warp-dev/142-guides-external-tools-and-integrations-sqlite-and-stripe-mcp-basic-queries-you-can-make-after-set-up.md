---
title: 'SQLite and Stripe MCP: Basic Queries | Guides | Warp'
url: https://docs.warp.dev/guides/external-tools-and-integrations/sqlite-and-stripe-mcp-basic-queries-you-can-make-after-set-up
source: sitemap
fetched_at: 2026-04-29T15:06:57.099387804-03:00
rendered_js: false
word_count: 228
summary: This document explains how to configure and use Model Context Protocol (MCP) servers within the Warp terminal to enable conversational querying of external APIs and local databases.
tags:
    - warp-terminal
    - mcp-servers
    - ai-agent
    - data-querying
    - sqlite-integration
    - stripe-api
category: tutorial
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
This tutorial shows how to use **MCP servers** to connect Warp to **Stripe** and **SQLite**, transforming the terminal into a connected, conversational workspace.

## Enable MCP in Warp

1. Open **Settings → AI → MCP Servers**.
2. Click **Add Server** and choose from available MCP configurations.
3. Warp automatically connects and authorizes the agent to use those tools.

This demo enables two servers:
- **SQLite Server** — local database queries
- **Stripe Server** — payment data retrieval and analysis

## Query Stripe

Issue conversational prompts — no manual API calls:

```
How many customers do I have in Stripe?
```

> "You have 3 customers."

Follow up naturally:

```
List the payments made by the first customer.
```

The agent retrieves payment intents — one successful, six canceled — all live from the Stripe test account.

> [!note]
> MCP's confirmation prompts can be disabled once you trust a given server or agent.

## Query SQLite

The same workflow applies to databases:

```
What SQL tables do I have access to?
```

```
Break down female penguins by island.
```

> "Bisco Island — 51 female penguins; Dream Island — ..."

Follow up contextually:

```
Do the same with male penguins.
```

Warp translates to SQL, executes it, and displays results inline.

## Why This Matters

Warp's AI and MCP support make the terminal:

- **Connected** — Access cloud APIs, local data, or enterprise tools instantly.
- **Conversational** — Run natural language prompts for structured data retrieval.

> [!info]
> "Even two years ago, no one could've imagined a terminal capable of this. Warp has officially redefined what a terminal can be." — Santiago
