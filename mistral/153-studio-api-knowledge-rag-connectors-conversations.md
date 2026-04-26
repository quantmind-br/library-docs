---
title: Using Connectors in conversations | Mistral Docs
url: https://docs.mistral.ai/studio-api/knowledge-rag/connectors/conversations
source: sitemap
fetched_at: 2026-04-26T04:12:57.167839421-03:00
rendered_js: false
word_count: 289
summary: This document explains how to integrate, configure, and manage external connectors and tools within Mistral conversation agents.
tags:
    - connector-management
    - ai-agents
    - tool-configuration
    - model-tools
    - mcp-servers
    - integration-guide
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Using Connectors in Conversations

After a Connector is [registered](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/management) and [authenticated](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/management#get-auth-url), attach it to any conversation.

You can mix Connectors with built-in tools like `web_search`, filter which tools the model can use, and configure Connectors on Agents.

## Passing a Connector to a Conversation

Tools are [MCP server executable functions](https://modelcontextprotocol.io/docs/learn/architecture#primitives) the model can call. Pass any Connector as a `tool` using `type: "connector"` and the Connector's name or UUID as `connector_id`.

All tools the Connector exposes are available to the model. To restrict which tools the model can call, see [Filter tools](#filtering-tools).

## Filtering Tools

To control which tools from a Connector the model can use, add a `tool_configuration` object:

- `include`: allowlist specific tools
- `exclude`: block specific tools

You can use one or the other, but not both at the same time.

## Requiring Confirmation

Add `requires_confirmation` to the `tool_configuration` for sensitive actions. See [Human-in-the-loop](https://docs.mistral.ai/studio-api/knowledge-rag/connectors/confirmation).

## Built-in Tools

Mistral provides [built-in tools](https://docs.mistral.ai/studio-api/agents/agent-tools) such as `web_search`, `code_interpreter`, `image_generation`, and `document_library`. Pass them alongside Connectors in the same `tools` array. The model decides which tool to call **based on the query**.

## Attaching to an Agent

Attach Connectors directly to an Agent at creation time. Every conversation started with that Agent then has access to the Connector tools automatically.

> [!note]
> Use `agent_id` **instead of** `model` when starting a conversation. You cannot pass both.

#connector-management #ai-agents #tool-configuration #model-tools
