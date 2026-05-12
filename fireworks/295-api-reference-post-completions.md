---
title: Create Completion
url: https://docs.fireworks.ai/api-reference/post-completions
source: sitemap
fetched_at: 2026-04-27T20:15:22.070989588-03:00
rendered_js: false
word_count: 1026
summary: This document details the parameters available for making requests to a Fireworks API endpoint, covering various configuration options for authorization, model selection, prompt input, output generation control, and performance metric inclusion.
tags:
    - api-parameters
    - bearer-authentication
    - prompt-configuration
    - generation-settings
    - perf-metrics
    - sampling-control
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Create Completion

> [!note]
> Bearer authentication: `Authorization: Bearer <API_KEY>`

## Body Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `model` | string | required | Model name (e.g., `accounts/fireworks/models/kimi-k2-instruct-0905`) |
| `prompt` | string\|string[]\|int[] | required | Single string, string array, or tokenized array. Multiple prompts return multiple choices with corresponding indices. |
| `user` | string | — | End-user ID for monitoring |
| `prompt_cache_key` | string | — | Prompt caching session affinity (takes priority over `user`) |
| `prompt_cache_isolation_key` | string | — | Prompt caching isolation key |
| `raw_output` | boolean | `false` | Return raw model output |
| `perf_metrics_in_response` | boolean | `false` | Include performance metrics in response body |
| `stream` | boolean | `false` | Stream tokens as [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) |
| `n` | integer | `1` | Number of completions `1–128` |
| `service_tier` | enum | `default` | `auto`, `default`, `flex`, `priority` |
| `stop` | string[] | — | Up to 4 stop sequences (not included in output) |
| `max_tokens` | integer | — | Max tokens to generate |
| `max_completion_tokens` | integer | — | Alias for `max_tokens` (mutually exclusive) |
| `temperature` | number | `1` | Sampling temperature `0–2` |
| `top_k` | integer | `50` | Top-k candidates `0–100` |
| `top_p` | number | `1` | Nucleus sampling `0–1` |
| `min_p` | number | — | Minimum token probability threshold `0–1` |
| `typical_p` | number | — | Typical-p sampling `0–1` |
| `frequency_penalty` | number | `0` | Repetition penalty `-2–2` (OpenAI-compatible) |
| `presence_penalty` | number | `0` | Token novelty penalty `-2–2` (OpenAI-compatible) |
| `repetition_penalty` | number | `1` | `0.0–1.0` rewards repetition; `>1.0` penalizes |
| `mirostat_tau` | number | — | Target perplexity (Mirostat) |
| `mirostat_eta` | number | — | Mirostat learning rate |
| `seed` | integer | — | Random seed for deterministic sampling |
| `logprobs` | boolean\|integer | — | `true` (OpenAI logprobs) or integer `0–5` (legacy) |
| `top_logprobs` | integer | — | Most likely tokens to return per position `0–5` |
| `echo` | boolean | `false` | Echo prompt with completion |
| `echo_last` | integer | — | Echo last N prompt tokens |
| `ignore_eos` | boolean | `false` | Continue generating after EOS token |
| `context_length_exceeded_behavior` | enum | `truncate` | `truncate` or `error` |
| `response_format` | object | — | `{ "type": "json_object" }` or `{ "type": "json_schema", "json_schema": <schema> }` |
| `logit_bias` | object | — | Token ID → bias `-100–100` |
| `prompt_caching` | object | — | Speculative decoding prompt/token IDs |
| `metadata` | object | — | Request metadata |
| `reasoning_effort` | string\|boolean\|integer | varies | See [reasoning_effort](#reasoning_effort) |
| `reasoning_content_strategy` | string\|null | varies | See [model-specific table](#model-support) |
| `thinking` | `ThinkingConfigEnabled` | — | Anthropic-compatible extended thinking |
| `return_token_ids` | boolean | `false` | Return token IDs alongside text |
| `image_urls` | string[] | — | Base64-encoded images (MIME type, e.g., `data:image/jpeg;base64,...`). Number of images must match ` ` special tokens in prompt. |

## `response_format`

- `{ "type": "json_object" }` — JSON mode; guarantees valid JSON output
- `{ "type": "json_schema", "json_schema": <schema> }` — enforce a schema

> [!warning]
> In JSON mode, include a system/user message instructing the model to produce JSON. Without this, the model may generate endless whitespace until the token limit. If `finish_reason="length"`, the content may be truncated/invalid.

## `perf_metrics_in_response`

**Non-streaming**: always in headers. Set `true` to include in response body under `perf_metrics`.

**Streaming**: only in response body under `perf_metrics` (final chunk when `finish_reason` is set).

### Metrics included

| Deployment type | Metrics |
|---|---|
| All | `prompt-tokens`, `cached-prompt-tokens`, `server-time-to-first-token`, `server-processing-time` |
| Predicted outputs | `speculation-prompt-tokens`, `speculation-prompt-matched-tokens` |
| Dedicated only | `speculation-generated-tokens`, `speculation-acceptance`, `backend-host`, `num-concurrent-requests`, `deployment`, `tokenizer-queue-duration`, `tokenizer-duration`, `prefill-queue-duration`, `prefill-duration`, `generation-queue-duration`, `generation-duration` |

## `reasoning_effort`

Controls reasoning behavior for supported models. Reasoning output appears in `reasoning_content` (separate from `content`).

| Value type | Accepted values | Notes |
|---|---|---|
| String (OpenAI-compatible) | `'low'`, `'medium'`, `'high'`, `'max'`, `'none'` | Enable varying effort levels |
| Boolean (Fireworks) | `true` → `'medium'`, `false` → `'none'` | Normalized before model-specific validation |
| Integer (Fireworks) | Positive integer | Hard token limit on reasoning output (grammar-based reasoning models only) |

### Model-specific behavior

| Model | Default | Supported values |
|---|---|---|
| Qwen3-8B | Reasoning on | `'none'`, `false` to disable; integer token limits; `'low'` → ~3000 tokens |
| MiniMax M2 | `'medium'` | Only `'low'`, `'medium'`, `'high'`; `'none'`, booleans rejected |
| DeepSeek V3.1 | Off | Enable: `true`, `'low'`, `'medium'`, `'high'`; disable: `'none'`, `false` |
| DeepSeek V3.2 | On | Disable: `'none'`, `false`; effort levels/integers have no additional effect |
| DeepSeek V4 | `'high'` | `'none'`/`false` disables; `'max'` prepends thorough-reasoning preamble; `'low'`/`'medium'` promote to `'high'` |
| GLM 4.5, 4.5 Air, 4.6, 4.7 | On | Disable: `'none'`, `false`; effort levels/integers have no effect |
| Harmony (GPT-OSS 120B/20B) | `'medium'` | Only `'low'`, `'medium'`, `'high'`; `'none'`, `false`, integers → error |

## `reasoning_content_strategy`

Controls how historical `reasoning_content` is included in the prompt for multi-turn conversations.

| Value | Effect |
|---|---|
| `null` | Model/template default |
| `'disabled'` | Strip `reasoning_content` from all messages |
| `'interleaved'` | Strip through last user message (default for most models) |
| `'preserved'` | Preserve across conversation |

### Model support

| Model | Default | Supported values |
|---|---|---|
| Kimi K2 Instruct | `'preserved'` | `'disabled'`, `'interleaved'`, `'preserved'` |
| MiniMax M2 | `'interleaved'` | `'disabled'`, `'interleaved'` |
| GLM-4.7 | `'interleaved'` | `'disabled'`, `'interleaved'`, `'preserved'` |
| GLM-4.6 | `'interleaved'` | `'disabled'`, `'interleaved'` |
| Qwen 3.6 | `'preserved'` | `'disabled'`, `'preserved'` |
| DeepSeek V4 | `'interleaved'` | `'interleaved'` |
| Other models | — | Refer to provider docs |

> [!info]
> This parameter controls prompt formatting only. To disable reasoning computation, use `reasoning_effort='none'`.

## Response Schema

```json
{
  "id": "string",
  "object": "text_completion",
  "created": "unix-timestamp",
  "model": "string",
  "choices": [
    {
      "index": "integer",
      "text": "string",
      "finish_reason": "string"
    }
  ],
  "usage": {
    "prompt_tokens": "integer",
    "completion_tokens": "integer",
    "total_tokens": "integer"
  },
  "perf_metrics": { ... },     // if perf_metrics_in_response=true
  "prompt_token_ids": [...]   // if return_token_ids=true
}
```

#api-parameters #bearer-authentication #prompt-configuration #generation-settings #perf-metrics #sampling-control