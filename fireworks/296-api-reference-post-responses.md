---
title: Create Response - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/post-responses
source: sitemap
fetched_at: 2026-04-27T20:19:02.702676527-03:00
rendered_js: false
word_count: 635
summary: This document details the structure and parameters for making requests to the Fireworks API, covering both the input model configuration required to generate a response and the resulting response object that contains output data and metadata.
tags:
    - api-request
    - response-model
    - bearer-auth
    - text-generation
    - tool-calls
    - conversation-state
category: reference
optimized: true
optimized_at: 2026-04-27T23:04:00Z
---
# Create Response

POST `/v1/responses`

Creates a new model response. Bearer authentication: `Bearer <API_KEY>`.

## Request

### Body

| Field | Type | Default | Description |
|---|---|---|---|
| `model` | `string` | required | Model ID, e.g. `accounts/<ACCOUNT_ID>/models/<MODEL_ID>` |
| `input` | `string \| object[]` | required | Text string or list of message objects |
| `previous_response_id` | `string` | — | ID of a previous response to continue the conversation from |
| `system` | `string \| object[]` | — | System instructions guiding model behavior |
| `max_output_tokens` | `integer` | — | Max tokens in response. Must be ≥ 1 |
| `max_tool_calls` | `integer` | — | Max tool calls per response. Must be ≥ 1 |
| `metadata` | `object` | — | Up to 16 key-value pairs attached to the response |
| `parallel_tool_calls` | `boolean \| null` | `true` | Enable parallel function calling |
| `reasoning` | `object` | — | Configuration for reasoning output |
| `store` | `boolean \| null` | `true` | Whether to store the response. `false` makes it non-retrievable |
| `stream` | `boolean \| null` | `false` | Stream response as Server-Sent Events (SSE) |
| `temperature` | `float \| null` | `1.0` | Sampling temperature. Range: `0–2` |
| `text` | `object` | — | Text generation configuration |
| `tools` | `object[]` | — | Tools the model may call. Supports `function`, `mcp`, `sse`, `python` types |
| `tool_choice` | `string \| object` | `"auto"` | Controls tool usage: `none`, `auto`, `required`, or a specific tool |
| `top_p` | `float \| null` | `1.0` | Nucleus sampling. Range: `0–1` |
| `truncation` | `string \| null` | `"disabled"` | Truncation strategy: `auto` or `disabled` |
| `user` | `string` | — | Unique end-user identifier for abuse monitoring |

### `tools` item

| Field | Type | Description |
|---|---|---|
| `type` | `string` | Tool type: `function`, `mcp`, `sse`, `python` |
| `name` | `string` | Tool name |
| `description` | `string` | Tool description |
| `parameters` | `object` | OpenAI-style function specification |

## Response

| Field | Type | Description |
|---|---|---|
| `id` | `string` | Response ID. `null` if `store=false` |
| `object` | `string` | Always `"response"` |
| `status` | `string` | `completed`, `in_progress`, `incomplete`, `failed`, or `cancelled` |
| `created_at` | `integer` | Unix timestamp (seconds) |
| `model` | `string` | Model used, e.g. `accounts/<ACCOUNT_ID>/models/<MODEL_ID>` |
| `previous_response_id` | `string \| null` | ID of the previous response in the conversation |
| `incomplete_details` | `object` | Details when `status=incomplete`. Field: `reason` (`max_output_tokens`, `max_tool_calls`, `content_filter`) |
| `output` | `array` | Array of `Message`, `ToolCall`, or `ToolOutput` objects |
| `usage` | `object` | Token usage: `prompt_tokens`, `completion_tokens`, `total_tokens` |
| `error` | `object` | Error info when `status=failed`. Fields: `type`, `code`, `message` |
| `reasoning` | `object` | Reasoning output when enabled. Fields: `content`, `type` |
| `system` | `string \| object[]` | System instructions |
| `max_output_tokens` | `integer` | Max tokens (read-only) |
| `max_tool_calls` | `integer` | Max tool calls. Must be ≥ 1 |
| `parallel_tool_calls` | `boolean` | Parallel tool call setting |
| `store` | `boolean` | Whether the response is stored |
| `temperature` | `float` | Temperature (read-only) |
| `text` | `object` | Text generation configuration |
| `tool_choice` | `string \| object` | Tool choice setting |
| `tools` | `object[]` | Available tools |
| `top_p` | `float` | Nucleus sampling (read-only) |
| `truncation` | `string` | Truncation strategy |
| `user` | `string` | End-user identifier |

### Output item types

- **Message**: A conversation message
- **ToolCall**: A tool invocation from the model
- **ToolOutput**: Output returned from a tool
