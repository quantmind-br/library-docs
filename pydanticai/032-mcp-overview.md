---
title: Overview - Pydantic AI
url: https://ai.pydantic.dev/mcp/overview/
source: sitemap
fetched_at: 2026-01-22T22:26:01.561874995-03:00
rendered_js: false
word_count: 252
summary: This document explains how Pydantic AI integrates with the Model Context Protocol (MCP), outlining different methods for agents to connect with MCP servers as clients or tools.
tags:
    - model-context-protocol
    - mcp
    - pydantic-ai
    - ai-agents
    - mcp-client
    - mcp-server
category: concept
---

## Model Context Protocol (MCP)

Pydantic AI supports [Model Context Protocol (MCP)](https://modelcontextprotocol.io) in multiple ways:

1. [Agents](https://ai.pydantic.dev/agents/) can connect to MCP servers and use their tools using three different methods:
   
   1. Pydantic AI can act as an MCP client and connect directly to local and remote MCP servers. [Learn more](https://ai.pydantic.dev/mcp/client/) about [`MCPServer`](https://ai.pydantic.dev/api/mcp/#pydantic_ai.mcp.MCPServer "MCPServer").
   2. Pydantic AI can use the [FastMCP Client](https://gofastmcp.com/clients/client/) to connect to local and remote MCP servers, whether or not they're built using [FastMCP Server](https://gofastmcp.com/servers). [Learn more](https://ai.pydantic.dev/mcp/fastmcp-client/) about [`FastMCPToolset`](https://ai.pydantic.dev/api/toolsets/#pydantic_ai.toolsets.fastmcp.FastMCPToolset "FastMCPToolset            dataclass   ").
   3. Some model providers can themselves connect to remote MCP servers using a "built-in tool". [Learn more](https://ai.pydantic.dev/builtin-tools/#mcp-server-tool) about [`MCPServerTool`](https://ai.pydantic.dev/api/builtin_tools/#pydantic_ai.builtin_tools.MCPServerTool "MCPServerTool            dataclass   ").
2. Agents can be used within MCP servers. [Learn more](https://ai.pydantic.dev/mcp/server/)

## What is MCP?

The Model Context Protocol is a standardized protocol that allow AI applications (including programmatic agents like Pydantic AI, coding agents like [cursor](https://www.cursor.com/), and desktop applications like [Claude Desktop](https://claude.ai/download)) to connect to external tools and services using a common interface.

As with other protocols, the dream of MCP is that a wide range of applications can speak to each other without the need for specific integrations.

There is a great list of MCP servers at [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers).

Some examples of what this means:

- Pydantic AI could use a web search service implemented as an MCP server to implement a deep research agent
- Cursor could connect to the [Pydantic Logfire](https://github.com/pydantic/logfire-mcp) MCP server to search logs, traces and metrics to gain context while fixing a bug
- Pydantic AI, or any other MCP client could connect to our [Run Python](https://github.com/pydantic/mcp-run-python) MCP server to run arbitrary Python code in a sandboxed environment