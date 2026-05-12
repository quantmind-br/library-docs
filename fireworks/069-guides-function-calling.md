---
title: Guides Function Calling
url: https://docs.fireworks.ai/guides/function-calling
source: sitemap
fetched_at: 2026-04-27T20:18:24.573447191-03:00
rendered_js: false
word_count: 213
summary: This document explains the concept of tool calling, detailing how language models can use external tools by accepting specifications defined in JSON Schema. It outlines the workflow and provides examples for defining, invoking, and controlling these tool calls.
tags:
    - tool-calling
    - function-calling
    - json-schema
    - agent-building
    - llm-tools
    - api-integration
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Tool calling (function calling) enables models to select and use external tools based on user input. Build agents that access APIs, retrieve real-time data, or perform actions—all through [OpenAI-compatible](https://platform.openai.com/docs/guides/function-calling) tool specifications.

## How it works

1. Define tools using [JSON Schema](https://json-schema.org/learn/getting-started-step-by-step) (name, description, parameters)
2. Model analyzes the query and decides whether to call a tool
3. If needed, model returns structured tool calls with parameters
4. Execute the tool and send results back for the final response

## Tool definition

Tools require:

- **name**: Function identifier (a-z, A-Z, 0-9, underscores, dashes; max 64 characters)
- **description**: Clear explanation of what the function does
- **parameters**: JSON Schema object describing parameters

Supported parameter types: `string`, `number`, `integer`, `object`, `array`, `boolean`, `null`. Use `enum` to restrict values and mark parameters as `required` or optional.

## Example

```python
from fireworks.client import Fireworks

client = Fireworks(api_key="<FIREWORKS_API_KEY>")

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name"}
            },
            "required": ["location"]
        }
    }
}]

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2-instruct-0905",
    messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
    tools=tools,
    temperature=0.1
)

print(response.choices[0].message.tool_calls)
# Output: [ChatCompletionMessageToolCall(id='call_abc123', function=Function(arguments='{"location":"San Francisco"}', name='get_weather'), type='function')]
```

## tool_choice parameter

Controls how the model uses tools:

| Value | Behavior |
|-------|----------|
| `auto` (default) | Model decides whether to call a tool or respond directly |
| `none` | Model will not call any tools |
| `required` | Model must call at least one tool |
| Specific function name | Force the model to call a particular function |

```python
# Force a specific tool
response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2-instruct-0905",
    messages=[{"role": "user", "content": "What's the weather?"}],
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "get_weather"}},
    temperature=0.1
)
```

> [!tip]
> For full API reference, see [[294-api-reference-post-chatcompletions|Post Chatcompletions]].

#tool-calling #function-calling #agent-building
