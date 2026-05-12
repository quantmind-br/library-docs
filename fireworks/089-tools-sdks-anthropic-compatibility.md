---
title: Anthropic compatibility - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/anthropic-compatibility
source: sitemap
fetched_at: 2026-04-27T20:18:09.978390974-03:00
rendered_js: false
word_count: 366
summary: This document provides a guide on how to interact with Fireworks using Anthropic SDKs (Python and TypeScript), detailing support for the Anthropic-compatible /v1/messages endpoint and outlining key differences, supported extensions, and unsupported features.
tags:
    - anthropic-sdk
    - fireworks
    - api-compatibility
    - quickstart
    - messages-endpoint
    - usage-tracking
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Use the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python) or [Anthropic TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript) to interact with Fireworks via the Anthropic-compatible `POST /v1/messages` endpoint.

## Quickstart

Install the SDK:

```bash
npm install @anthropic-ai/sdk
```

Then set `model` to a Fireworks model resource name such as `accounts/fireworks/models/kimi-k2p5`.

> [!tip]
> The [[009-getting-started-quickstart]] includes Anthropic SDK examples for: Messages, Streaming, Function calling, Structured outputs, Reasoning, and Vision.

## Supported Endpoint

Fireworks supports the Anthropic `/v1/messages` endpoint, including non-streaming and streaming (SSE) responses. See [[023-api-reference-anthropic-messages]] for the API reference.

### Deployment Support

Anthropic compatibility is supported for serverless and on-demand deployments. Requests must go through `api.fireworks.ai/inference` (direct route endpoints are not supported).

## Differences from Anthropic

| Parameter | Behavior |
|---|---|
| `model` | Must be a Fireworks identifier (e.g., `accounts/fireworks/models/deepseek-v3p2`) instead of an Anthropic model name. See the [Fireworks Model Library](https://app.fireworks.ai/models). |
| `max_tokens` | Optional on Fireworks (required on Anthropic). |
| `anthropic-version` header | Not required; Fireworks ignores this header. |
| `usage` field | Included in both non-streaming and streaming responses. |
| `service_tier` | Not supported. |
| `inference_geo` | Not supported. |

## Reasoning Effort Mapping

The `thinking` parameter with `output_config.effort` maps to Fireworks `reasoning_effort`:

| Anthropic effort | Fireworks mapping |
|---|---|
| `low` | `low` |
| `medium` | `medium` |
| `high` | `high` |
| `max` | `high` |

For more on reasoning, including interleaved thinking with tool use, see [[078-guides-reasoning]].

## Unsupported Features

> [!warning]
> The following Anthropic features are not available on Fireworks:

- **Server tools**: Server-side tool families (code execution, memory, web fetch, tool search, web search) are not supported.
- **Server-tool metadata**: Fields such as `caller` and `container` are not supported.
- **Tool schema fields**: `eager_input_streaming`, `cache_control`, `allowed_callers`, `defer_loading`, and `input_examples` are not supported.
- **`server_tool_use`**: Not included in usage tracking.
- **`speed`**: The `output_config.speed` option is not supported yet.

## Fireworks Extensions

- **`raw_output`**: A request parameter (boolean) that returns low-level details of what the model sees, including formatted prompts and function call data.

## Token Usage

Token usage (`input_tokens` and `output_tokens`) is included in both non-streaming and streaming responses.

- **Non-streaming**: Usage is returned on the response object.
- **Streaming**: Usage is included in the final `message_delta` event.

#anthropic-sdk #api-compatibility #messages-endpoint
