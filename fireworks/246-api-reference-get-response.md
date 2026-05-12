---
title: Get Response - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-response
source: sitemap
fetched_at: 2026-04-27T20:14:08.544461227-03:00
rendered_js: false
word_count: 196
summary: Returns the response object schema for model inference results including output messages, usage metrics, and configuration.
tags:
    - json-schema
    - model-response
    - api-object
    - data-structure
    - configuration
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Response

Returns the response object schema for model inference.

```json
{
  "created_at": 123,
  "status": "<string>",
  "model": "<string>",
  "output": [
    {
      "id": "<string>",
      "role": "<string>",
      "content": [
        {
          "type": "<string>",
          "text": "<string>"
        }
      ],
      "status": "<string>",
      "type": "message"
    }
  ],
  "id": "<string>",
  "object": "response",
  "previous_response_id": "<string>",
  "usage": {},
  "error": {},
  "incomplete_details": {},
  "instructions": "<string>",
  "max_output_tokens": 123,
  "max_tool_calls": 2,
  "parallel_tool_calls": true,
  "reasoning": {},
  "store": true,
  "temperature": 1,
  "text": {},
  "tool_choice": "auto",
  "tools": [{}],
  "top_p": 1,
  "truncation": "disabled",
  "user": "<string>",
  "metadata": {}
}
```

## Key Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Response identifier. |
| `object` | string | Object type: `"response"`. |
| `created_at` | integer | Unix timestamp of creation. |
| `model` | string | Model used for the response. |
| `status` | string | Response status. |
| `output` | array | Array of output messages. |
| `usage` | object | Token usage metrics. |
| `error` | object | Error information if applicable. |
| `reasoning` | object | Reasoning content (for reasoning models). |
| `previous_response_id` | string | ID of the previous response for continuation. |
| `temperature` | number | Sampling temperature. |
| `top_p` | number | Top-p sampling parameter. |
| `max_output_tokens` | integer | Maximum output tokens. |
| `max_tool_calls` | integer | Maximum tool calls allowed. |
| `parallel_tool_calls` | boolean | Whether parallel tool calls are enabled. |
| `tools` | array | Available tools for function calling. |

> [!info]
> Schema for model response objects including messages, usage, and configuration. #json-schema #model-response #data-structure