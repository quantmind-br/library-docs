---
title: Connectors | Mistral Docs
url: https://docs.mistral.ai/studio-api/knowledge-rag/connectors
source: sitemap
fetched_at: 2026-04-26T04:12:52.811359551-03:00
rendered_js: false
word_count: 166
summary: This document explains how to integrate Model Context Protocol (MCP) servers as Connectors to enable AI models to interact with external tools and data sources.
tags:
    - mcp
    - connectors
    - ai-agents
    - tool-calling
    - external-data
    - integration
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Connectors (API)

> [!warning]
> Connectors are a **beta** feature. The API interface can change.

Connectors are registered [MCP servers](https://modelcontextprotocol.io/) that you can use as **tools in conversations and Agents**, from any SDK or directly via the API, **without managing MCP transport locally**.

Once registered, a Connector **exposes its tools to the model** on demand: the model discovers them automatically and calls the right one **based on the user's request**.

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard for connecting AI models to external tools and data sources through a unified interface. Any **MCP-compatible server** can be registered as a Connector.

## Documentation

- [**Create and manage Connectors**](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/management) — register a Connector with the MCP server URL and visibility scope.
- [**Use Connectors in conversations**](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/conversations) — pass a Connector in the `tools` array and let the model pick the right tool.
- [**Call tools directly**](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/tool_calling) — invoke a specific tool when you already know which one and what arguments to use.
- [**Human-in-the-loop confirmation**](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/confirmation) — intercept tool calls for user approval before execution.

#mcp #connectors #ai-agents #tool-calling #integration
