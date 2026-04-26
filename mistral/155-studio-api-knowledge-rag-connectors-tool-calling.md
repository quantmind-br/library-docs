---
title: Direct tool calling with Connectors | Mistral Docs
url: https://docs.mistral.ai/studio-api/knowledge-rag/connectors/tool_calling
source: sitemap
fetched_at: 2026-04-26T04:13:01.605244881-03:00
rendered_js: false
word_count: 165
summary: This document explains how to invoke MCP tools directly on a connector using the call_tool method, bypassing model involvement for programmatic tool execution and pipeline construction.
tags:
    - mcp-tools
    - connector-integration
    - programmatic-access
    - api-documentation
    - tool-execution
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Direct Tool Calling with Connectors

The `call_tool` method lets you call a specific MCP tool on a Connector directly, **without starting a conversation or involving the model**.

Use this when you:
- Already know which tool to call and what arguments to pass
- Want the raw tool output for downstream processing
- Are building pipelines that chain tool calls programmatically
- Want to debug or verify Connector tools before using them in conversations

For scenarios where the model picks which tools to call, use [Connectors in conversations](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/conversations) instead.

## Prerequisites

If a Connector requires authentication, you must complete the [auth flow](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/management#get-auth-url) before calling its tools.

## Calling a Tool

Pass the Connector name (or UUID), the tool name, and the arguments the tool expects.

The response `content` array contains typed content blocks (text, image, audio, or resource) returned by the MCP server.

> [!warning]
> Tool names must match exactly. Use [list tools](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/management#list-tools) to check what a Connector exposes.

You can call multiple tools in sequence to build a pipeline **without involving the model at each step**.

#mcp-tools #connector-integration #programmatic-access #tool-execution
