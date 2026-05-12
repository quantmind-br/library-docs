---
title: Connect Agents to MCP Servers | Guides | Warp
url: https://docs.warp.dev/guides/external-tools-and-integrations/using-mcp-servers-with-warp
source: sitemap
fetched_at: 2026-04-29T15:06:57.610965397-03:00
rendered_js: false
word_count: 238
summary: This document explains how to integrate Model Context Protocol (MCP) servers into the Warp agent to enable interaction with external systems like GitHub and Linear for enhanced task automation.
tags:
    - mcp
    - warp-agent
    - context-protocol
    - system-integration
    - automation
    - dynamic-context
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
## What Are MCP Servers?

MCP (Model Context Protocol) servers let Warp agents connect to external systems — GitHub, Linear, Jira — to read, write, and reason about those systems natively.

Each MCP server adds its own tools to Warp's agent. For example:

- The **Linear MCP Server** handles tickets.
- The **GitHub MCP Server** handles pull requests and issues.

## Adding the Linear MCP Server

1. Open the **MCP Panel** in Warp.
2. Click **Add Server**.
3. Paste the JSON configuration for the Linear MCP Server.

Once added, Warp:
- Starts the MCP server.
- Loads its tools (e.g., `get_ticket`, `update_ticket`, `create_ticket`).
- Makes them available to the agent instantly.

## Using Rules with MCP Servers

Add a rule (e.g., `check-linear`) to help the agent automatically associate "tickets" with the Linear MCP Server:

> **Rule:** "When the user says 'ticket,' check Linear."

Rules make context switching seamless — the agent doesn't need reminders.

## Dynamic Context Loading

Warp's MCP support is **dynamic**:
- Start a conversation without any connected MCPs.
- Add one mid-session — the agent updates its context on the next message.
- No restart or session reset required.

## Running the Task

After connecting Linear:

> "Help me solve this ticket."

The agent:
1. Queries Linear for the ticket.
2. Pulls all related context.
3. Reads the codebase for linked references.
4. Generates the appropriate fix.

Verify the output by running the suggested command.
