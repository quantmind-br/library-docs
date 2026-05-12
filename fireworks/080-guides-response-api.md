---
title: Responses API
url: https://docs.fireworks.ai/guides/response-api
source: sitemap
fetched_at: 2026-04-27T20:12:45.381133382-03:00
rendered_js: false
word_count: 277
summary: Guide to Fireworks.ai's Responses API for conversational applications, covering conversation continuation, tool integration (MCP/SSE/functions), streaming, and data retention.
tags:
    - responses-api
    - fireworks-ai
    - llm-interaction
    - conversational-ai
    - tool-calling
    - response-streaming
category: guide
optimized: true
optimized_at: 2026-04-27T23:00:00Z
---
The Responses API enables complex, stateful interactions with models. Key features:

- **Continue conversations** — maintain context across turns without resending history
- **External tools** — MCP/SSE tools (server-executed) or function tools (client-executed)
- **Streaming** — receive results in real-time
- **Control tool usage** — set `max_tool_calls` limit
- **Data retention** — default stores conversations; opt-out with `store=false`

## Creating a Response

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
)

response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="What is reward-kit and what are its 2 main features?",
    tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
)

print(response.output[-1].content[0].text.split("")[-1])
```

See the [MCP examples notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_examples.ipynb) for complete examples.

## Function Tools

Function tools follow OpenAI-compatible format and are returned to the client for execution:

```python
response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="What is the weather like in San Francisco?",
    tools=[{
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA"
                }
            },
            "required": ["location"]
        }
    }],
    tool_choice="auto"
)

# Check if the model wants to call a function
for item in response.output:
    if hasattr(item, 'type') and item.type == "tool_call":
        print(f"Function: {item.function.name}")
        print(f"Arguments: {item.function.arguments}")
```

## Continuing a Conversation

Use `previous_response_id` to continue a conversation without resending history:

```python
# First, create an initial response
initial_response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="What are the key features of reward-kit?",
    tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
)
initial_response_id = initial_response.id

# Continue the conversation
continuation_response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="How do I install it?",
    previous_response_id=initial_response_id,
    tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
)

print(continuation_response.output[-1].content[0].text.split("")[-1])
```

See the [previous response ID notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_previous_response_cookbook.ipynb) for complete examples.

## Streaming Responses

```python
stream = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="give me 5 interesting facts on modelcontextprotocol/python-sdk",
    stream=True,
    tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
)

for chunk in stream:
    print(chunk)
```

See the [streaming example notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_streaming_example.ipynb) for complete examples.

## Storing Responses

By default, responses are stored and can be referenced by ID. Disable with `store=False`. When disabled, you cannot use `previous_response_id` to continue the conversation:

```python
response = client.responses.create(
    model="accounts/fireworks/models/qwen3-235b-a22b",
    input="give me 5 interesting facts on modelcontextprotocol/python-sdk",
    store=False,
    tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
)

# This will fail because the previous response was not stored
try:
    continuation_response = client.responses.create(
        model="accounts/fireworks/models/qwen3-235b-a22b",
        input="Explain the second fact in more detail.",
        previous_response_id=response.id
    )
except Exception as e:
    print(e)
```

See the [store=False notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/mcp_server_with_store_false_argument.ipynb) for complete examples.

## Deleting Stored Responses

When responses are stored (default `store=True`), use the DELETE endpoint to permanently remove conversation data.

## Response Structure

All response objects include:

- `id` — unique identifier (e.g., `resp_abc123...`)
- `created_at` — Unix timestamp
- `status` — response status (typically `"completed"`)
- `model` — model used
- `output` — array of message objects, tool calls, and tool outputs
- `usage` — token usage information:
  - `prompt_tokens`, `completion_tokens`, `total_tokens`
  - `prompt_tokens_details.cached_tokens`
- `previous_response_id` — ID of previous response in conversation (if any)
- `store` — whether response was stored
- `max_tool_calls` — maximum tool calls allowed (if set)

### Example Response

```json
{
  "id": "resp_abc123...",
  "created_at": 1735000000,
  "status": "completed",
  "model": "accounts/fireworks/models/qwen3-235b-a22b",
  "output": [
    {
      "id": "msg_xyz789...",
      "role": "user",
      "content": [{"type": "input_text", "text": "What is 2+2?"}],
      "status": "completed"
    },
    {
      "id": "msg_def456...",
      "role": "assistant",
      "content": [{"type": "output_text", "text": "2 + 2 equals 4."}],
      "status": "completed"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 8,
    "total_tokens": 23,
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  },
  "previous_response_id": null,
  "store": true,
  "max_tool_calls": null
}
```

## Cookbook Examples

- [General MCP Examples](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_examples.ipynb)
- [Using `previous_response_id`](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_previous_response_cookbook.ipynb)
- [Streaming Responses](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_streaming_example.ipynb)
- [Using `store=False`](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/mcp_server_with_store_false_argument.ipynb)
- [MCP with Streaming](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_with_streaming.ipynb)