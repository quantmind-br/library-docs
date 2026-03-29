---
title: LLM Sampling - FastMCP
url: https://gofastmcp.com/clients/sampling
source: crawler
fetched_at: 2026-01-22T22:23:01.926918304-03:00
rendered_js: false
word_count: 160
summary: This document explains how to implement and configure sampling handlers in FastMCP to allow servers to request LLM completions from a client.
tags:
    - fastmcp
    - mcp-protocol
    - llm-sampling
    - python-client
    - openai-integration
    - anthropic-integration
category: guide
---

New in version `2.0.0` Use this when you need to respond to server requests for LLM completions. MCP servers can request LLM completions from clients during tool execution. This enables servers to delegate AI reasoning to the client, which controls which LLM is used and how requests are made.

## Handler Template

```
from fastmcp import Client
from fastmcp.client.sampling import SamplingMessage, SamplingParams, RequestContext

async def sampling_handler(
    messages: list[SamplingMessage],
    params: SamplingParams,
    context: RequestContext
) -> str:
    """
    Handle server requests for LLM completions.

    Args:
        messages: Conversation messages to send to the LLM
        params: Sampling parameters (temperature, max_tokens, etc.)
        context: Request context with metadata

    Returns:
        Generated text response from your LLM
    """
    # Extract message content
    conversation = []
    for message in messages:
        content = message.content.text if hasattr(message.content, 'text') else str(message.content)
        conversation.append(f"{message.role}: {content}")

    # Use the system prompt if provided
    system_prompt = params.systemPrompt or "You are a helpful assistant."

    # Integrate with your LLM service here
    return "Generated response based on the messages"

client = Client(
    "my_mcp_server.py",
    sampling_handler=sampling_handler,
)
```

## Handler Parameters

## Built-in Handlers

FastMCP provides built-in handlers for OpenAI and Anthropic APIs that support the full sampling API including tool use.

### OpenAI Handler

New in version `2.11.0`

```
from fastmcp import Client
from fastmcp.client.sampling.handlers.openai import OpenAISamplingHandler

client = Client(
    "my_mcp_server.py",
    sampling_handler=OpenAISamplingHandler(default_model="gpt-4o"),
)
```

For OpenAI-compatible APIs (like local models):

```
from openai import AsyncOpenAI

client = Client(
    "my_mcp_server.py",
    sampling_handler=OpenAISamplingHandler(
        default_model="llama-3.1-70b",
        client=AsyncOpenAI(base_url="http://localhost:8000/v1"),
    ),
)
```

### Anthropic Handler

New in version `2.14.1`

```
from fastmcp import Client
from fastmcp.client.sampling.handlers.anthropic import AnthropicSamplingHandler

client = Client(
    "my_mcp_server.py",
    sampling_handler=AnthropicSamplingHandler(default_model="claude-sonnet-4-5"),
)
```

## Sampling Capabilities

When you provide a `sampling_handler`, FastMCP automatically advertises full sampling capabilities to the server, including tool support. To disable tool support for simpler handlers:

```
from mcp.types import SamplingCapability

client = Client(
    "my_mcp_server.py",
    sampling_handler=basic_handler,
    sampling_capabilities=SamplingCapability(),  # No tool support
)
```

Tool execution happens on the server side. The client’s role is to pass tools to the LLM and return the LLM’s response (which may include tool use requests). The server then executes the tools and may send follow-up sampling requests with tool results.