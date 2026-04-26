---
title: Human-in-the-loop | Mistral Docs
url: https://docs.mistral.ai/studio-api/knowledge-rag/connectors/confirmation
source: sitemap
fetched_at: 2026-04-26T04:12:56.349350778-03:00
rendered_js: false
word_count: 353
summary: This document explains how to implement a human-in-the-loop confirmation flow for tool execution, requiring user approval before sensitive actions are performed.
tags:
    - human-in-the-loop
    - tool-execution
    - confirmation-flow
    - api-security
    - python-sdk
    - function-calling
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Human-in-the-loop Confirmation

Some tool calls, like sending an email or modifying data, are safer with human approval. The `requires_confirmation` parameter lets you intercept these calls before they run.

This works for all tool types: Connectors, built-in tools (such as `web_search_premium`), and local functions (Python SDK only).

## Implementation Options

| Method | Use Case |
|--------|----------|
| **REST API** | Manage conversation IDs and tool call IDs yourself. Works with any language or HTTP client. |
| **Python SDK** | Use `RunContext` and `DeferredToolCallsException` for a higher-level flow. |

## How It Works

1. [Start the conversation](#start-conversation) and get a pending `function.call`.
2. [Approve](#approve) or [deny](#deny) the call to resume the conversation.

### Start Conversation

The API returns a pending `function.call` entry instead of running the tool.

### Approve

Send `"allow"` to run the tool and get the model response.

### Deny

Send `"deny"` to reject the call. The model handles the rejection gracefully.

> [!note]
> Multiple tool calls can be pending at once. You can approve or deny them individually or as a batch in a single request.

## Python SDK Flow

`DeferredToolCallsException` requires `mistralai` **v2.4+** and the `mcp` extra (`pip install mistralai[mcp]`).

The Python SDK provides `RunContext` and `DeferredToolCallsException` to handle confirmation flows:

- `run_async` runs the conversation loop and raises `DeferredToolCallsException` when a tool requires confirmation.
- Call `dc.confirm()` or `dc.reject()` on each deferred call, then loop back to resume.

Register local Python functions with `register_func` and set `requires_confirmation=True` for functions that need approval.

## Serialization

For web APIs where confirmation happens in a separate request, serialize the deferred state and reconstruct it later.

> [!warning]
> Always prepend `deferred.executed_results` (results from tools that ran before the deferral point) when resuming so the model has full context.

#human-in-the-loop #tool-execution #confirmation-flow #api-security
