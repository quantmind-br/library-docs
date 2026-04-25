---
title: Using MCP via API
url: https://lmstudio.ai/docs/developer/core/mcp
source: sitemap
fetched_at: 2026-04-07T21:30:01.792978869-03:00
rendered_js: false
word_count: 334
summary: This document details how LM Studio supports Model Context Protocol (MCP) for enabling models to interact with external tools via standardized servers. It compares and explains the use cases for defining these servers either ephemerally per request or pre-configuring them in an mcp.json file.
tags:
    - mcp-protocol
    - model-interaction
    - tool-calling
    - lm-studio
    - api-integration
    - configuration
category: guide
---

##### Requires [LM Studio 0.4.0](https://lmstudio.ai/download) or newer.

LM Studio supports Model Context Protocol (MCP) usage via API. MCP allows models to interact with external tools and services through standardized servers.

## How it works[](#how-it-works "Link to 'How it works'")

MCP servers provide tools that models can call during chat requests. You can enable MCP servers in two ways: as ephemeral servers defined per-request, or as pre-configured servers in your `mcp.json` file.

## Ephemeral vs mcp.json servers[](#ephemeral-vs-mcpjson-servers "Link to 'Ephemeral vs mcp.json servers'")

FeatureEphemeralmcp.jsonHow to specify in request`integrations` → `"type": "ephemeral_mcp"``integrations` → `"type": "plugin"`ConfigurationOnly defined per-requestPre-configured in `mcp.json`Use caseOne-off requests, remote MCP tool executionMCP servers that require `command`, frequently used serversServer IDSpecified via `server_label` in integrationSpecified via `id` (e.g., `mcp/playwright`) in integrationCustom headersSupported via `headers` fieldConfigured in `mcp.json`

## Ephemeral MCP servers[](#ephemeral-mcp-servers "Link to 'Ephemeral MCP servers'")

Ephemeral MCP servers are defined on-the-fly in each request. This is useful for testing or when you don't want to pre-configure servers.

Ephemeral MCP servers require the "Allow per-request MCPs" setting to be enabled in [Server Settings](https://lmstudio.ai/docs/developer/core/server/settings).

The model can now call tools from the specified MCP server:

## MCP servers from mcp.json[](#mcp-servers-from-mcpjson "Link to 'MCP servers from mcp.json'")

MCP servers can be pre-configured in your `mcp.json` file. This is the recommended approach for using MCP servers that take actions on your computer (like [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)) and servers that you use frequently.

MCP servers from mcp.json require the "Allow calling servers from mcp.json" setting to be enabled in [Server Settings](https://lmstudio.ai/docs/developer/core/server/settings).

![undefined](https://lmstudio.ai/assets/docs/mcp-editor.png)

Editing mcp.json in LM Studio

The response includes tool calls from the configured MCP server:

For both ephemeral and mcp.json servers, you can limit which tools the model can call using the `allowed_tools` field. This is useful if you do not want certain tools from an MCP server to be used, and can speed up prompt processing due to the model receiving fewer tool definitions.

If `allowed_tools` is not provided, all tools from the server are available to the model.

When using ephemeral MCP servers that require authentication, you can pass custom headers: