---
title: Models
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/models.md
source: git
fetched_at: 2026-04-26T05:48:14.154721504-03:00
rendered_js: false
word_count: 1683
summary: This document explains how to configure custom AI models and providers for the pi agent by modifying the models.json configuration file.
tags:
    - configuration
    - custom-models
    - api-integration
    - local-llm
    - proxy-settings
category: configuration
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Custom Models

Add custom providers and models (Ollama, vLLM, LM Studio, proxies) via `~/.pi/agent/models.json`. The file reloads on each `/model` open; no restart needed.

## Minimal Example

Local models (Ollama, LM Studio, vLLM) require only `id` per model:

```json
{
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "models": [
        { "id": "llama3.1:8b" },
        { "id": "qwen2.5-coder:7b" }
      ]
    }
  }
}
```

`apiKey` is required but Ollama ignores it — any value works.

### Compatibility Flags

Some OpenAI-compatible servers reject the `developer` role or `reasoning_effort`. Set `compat` at provider level (all models) or model level (per-model override):

```json
{
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false
      },
      "models": [
        {
          "id": "gpt-oss:20b",
          "reasoning": true
        }
      ]
    }
  }
}
```

Commonly applies to Ollama, vLLM, SGLang, and similar OpenAI-compatible servers.

## Full Example

Override defaults when needed:

```json
{
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "models": [
        {
          "id": "llama3.1:8b",
          "name": "Llama 3.1 8B (Local)",
          "reasoning": false,
          "input": ["text"],
          "contextWindow": 128000,
          "maxTokens": 32000,
          "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 }
        }
      ]
    }
  }
}
```

## Google AI Studio Example

Use `google-generative-ai` with a `baseUrl` to add models from Google AI Studio, including custom Gemma 4 entries:

```json
{
  "providers": {
    "my-google": {
      "baseUrl": "https://generativelanguage.googleapis.com/v1beta",
      "api": "google-generative-ai",
      "apiKey": "GEMINI_API_KEY",
      "models": [
        {
          "id": "gemma-4-31b-it",
          "name": "Gemma 4 31B",
          "input": ["text", "image"],
          "contextWindow": 262144,
          "reasoning": true
        }
      ]
    }
  }
}
```

> [!note] `baseUrl` is required when adding custom models to the `google-generative-ai` API type.

## Supported APIs

| API | Description |
|-----|-------------|
| `openai-completions` | OpenAI Chat Completions (most compatible) |
| `openai-responses` | OpenAI Responses API |
| `anthropic-messages` | Anthropic Messages API |
| `google-generative-ai` | Google Generative AI |

Set `api` at provider level (default) or model level (override).

## Provider Configuration

| Field | Description |
|-------|-------------|
| `baseUrl` | API endpoint URL |
| `api` | API type (see above) |
| `apiKey` | API key (see value resolution below) |
| `headers` | Custom headers (see value resolution below) |
| `authHeader` | Set `true` to add `Authorization: Bearer <apiKey>` automatically |
| `models` | Array of model configurations |
| `modelOverrides` | Per-model overrides for built-in models on this provider |

### Value Resolution

`apiKey` and `headers` support three formats:

| Format | Syntax | Example |
|--------|--------|---------|
| Shell command | `"!command"` | `"!security find-generic-password -ws 'anthropic'"`, `"!op read 'op://vault/item/credential'"` |
| Environment variable | Variable name | `"MY_API_KEY"` |
| Literal value | Used directly | `"sk-..."` |

> [!warning] Shell commands in `models.json` are resolved at request time. pi does not apply built-in TTL, stale reuse, or recovery logic for arbitrary commands. If your command is slow, rate-limited, or should keep a previous value on transient failures, wrap it in your own caching script.

`/model` availability checks use configured auth presence and do **not** execute shell commands.

### Custom Headers

```json
{
  "providers": {
    "custom-proxy": {
      "baseUrl": "https://proxy.example.com/v1",
      "apiKey": "MY_API_KEY",
      "api": "anthropic-messages",
      "headers": {
        "x-portkey-api-key": "PORTKEY_API_KEY",
        "x-secret": "!op read 'op://vault/item/secret'"
      },
      "models": [...]
    }
  }
}
```

## Model Configuration

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `id` | Yes | — | Model identifier (passed to the API) |
| `name` | No | `id` | Human-readable label; used for matching (`--model` patterns) and status text |
| `api` | No | provider's `api` | Override provider API for this model |
| `reasoning` | No | `false` | Supports extended thinking |
| `input` | No | `["text"]` | `["text"]` or `["text", "image"]` |
| `contextWindow` | No | `128000` | Context window in tokens |
| `maxTokens` | No | `16384` | Maximum output tokens |
| `cost` | No | all zeros | `{"input":0,"output":0,"cacheRead":0,"cacheWrite":0}` per million tokens |
| `compat` | No | provider `compat` | Compatibility overrides; merged with provider-level `compat` |

- `/model` and `--list-models` list entries by model `id`.
- Configured `name` is used for model matching and detail/status text.

## Overriding Built-in Providers

Route a built-in provider through a proxy without redefining models:

```json
{
  "providers": {
    "anthropic": {
      "baseUrl": "https://my-proxy.example.com/v1"
    }
  }
}
```

All built-in Anthropic models remain available. Existing OAuth or API key auth continues to work.

Merge custom models into a built-in provider by including `models`:

```json
{
  "providers": {
    "anthropic": {
      "baseUrl": "https://my-proxy.example.com/v1",
      "apiKey": "ANTHROPIC_API_KEY",
      "api": "anthropic-messages",
      "models": [...]
    }
  }
}
```

**Merge semantics:**
- Built-in models are kept.
- Custom models are upserted by `id`.
- Matching `id` replaces the built-in model.
- New `id` is added alongside built-in models.

## Per-model Overrides

Use `modelOverrides` to customize specific built-in models without replacing the full model list:

```json
{
  "providers": {
    "openrouter": {
      "modelOverrides": {
        "anthropic/claude-sonnet-4": {
          "name": "Claude Sonnet 4 (Bedrock Route)",
          "compat": {
            "openRouterRouting": {
              "only": ["amazon-bedrock"]
            }
          }
        }
      }
    }
  }
}
```

`modelOverrides` supports per model: `name`, `reasoning`, `input`, `cost` (partial), `contextWindow`, `maxTokens`, `headers`, `compat`.

- Applied to built-in provider models; unknown IDs are ignored.
- Combine with provider-level `baseUrl`/`headers`.
- If `models` is also defined, custom models merge after built-in overrides. A custom model with the same `id` replaces the overridden entry.

## Anthropic Messages Compatibility

For `api: "anthropic-messages"` providers/proxies, control fine-grained tool streaming with `compat`:

| Field | Description |
|-------|-------------|
| `supportsEagerToolInputStreaming` | Whether the provider accepts per-tool `eager_input_streaming`. Default `true`. Set `false` to omit that field and use the legacy `fine-grained-tool-streaming-2025-05-14` beta header instead. |
| `supportsLongCacheRetention` | Whether the provider accepts `cache_control.ttl: "1h"` when cache retention is `long`. Default `true`. |

```json
{
  "providers": {
    "anthropic-proxy": {
      "baseUrl": "https://proxy.example.com",
      "api": "anthropic-messages",
      "apiKey": "ANTHROPIC_PROXY_KEY",
      "compat": {
        "supportsEagerToolInputStreaming": false,
        "supportsLongCacheRetention": true
      },
      "models": [
        {
          "id": "claude-opus-4-7",
          "reasoning": true,
          "input": ["text", "image"]
        }
      ]
    }
  }
}
```

## OpenAI Compatibility

For providers with partial OpenAI compatibility, use `compat`. Provider-level `compat` applies defaults to all models; model-level overrides per model.

```json
{
  "providers": {
    "local-llm": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "compat": {
        "supportsUsageInStreaming": false,
        "maxTokensField": "max_tokens"
      },
      "models": [...]
    }
  }
}
```

| Field | Description |
|-------|-------------|
| `supportsStore` | Provider supports `store` field |
| `supportsDeveloperRole` | Use `developer` vs `system` role |
| `supportsReasoningEffort` | Support for `reasoning_effort` parameter |
| `reasoningEffortMap` | Map pi thinking levels to provider-specific `reasoning_effort` values |
| `supportsUsageInStreaming` | Supports `stream_options: { include_usage: true }` (default `true`) |
| `maxTokensField` | Use `max_completion_tokens` or `max_tokens` |
| `requiresToolResultName` | Include `name` on tool result messages |
| `requiresAssistantAfterToolResult` | Insert assistant message before user message after tool results |
| `requiresThinkingAsText` | Convert thinking blocks to plain text |
| `requiresReasoningContentOnAssistantMessages` | Include empty `reasoning_content` on all replayed assistant messages when reasoning enabled |
| `thinkingFormat` | `reasoning_effort`, `deepseek`, `zai`, `qwen`, or `qwen-chat-template` thinking parameters |
| `cacheControlFormat` | Anthropic-style `cache_control` markers on system prompt, last tool definition, and last user/assistant text content. Only `anthropic` supported. |
| `supportsStrictMode` | Include `strict` field in tool definitions |
| `supportsLongCacheRetention` | Whether provider accepts long cache retention when `long`: `prompt_cache_retention: "24h"` for OpenAI, or `cache_control.ttl: "1h"` when `cacheControlFormat` is `anthropic`. Default `true`. |
| `openRouterRouting` | Sent as-is in `provider` field of [OpenRouter API request](https://openrouter.ai/docs/guides/routing/provider-selection) |
| `vercelGatewayRouting` | Vercel AI Gateway routing config (`only`, `order`) |

> [!note] `qwen` uses top-level `enable_thinking`. Use `qwen-chat-template` for local Qwen-compatible servers requiring `chat_template_kwargs.enable_thinking`.
>
> `cacheControlFormat: "anthropic"` is for OpenAI-compatible providers that expose Anthropic-style prompt caching through `cache_control` markers.

### OpenRouter Example

```json
{
  "providers": {
    "openrouter": {
      "baseUrl": "https://openrouter.ai/api/v1",
      "apiKey": "OPENROUTER_API_KEY",
      "api": "openai-completions",
      "models": [
        {
          "id": "openrouter/anthropic/claude-3.5-sonnet",
          "name": "OpenRouter Claude 3.5 Sonnet",
          "compat": {
            "openRouterRouting": {
              "allow_fallbacks": true,
              "require_parameters": false,
              "data_collection": "deny",
              "zdr": true,
              "enforce_distillable_text": false,
              "order": ["anthropic", "amazon-bedrock", "google-vertex"],
              "only": ["anthropic", "amazon-bedrock"],
              "ignore": ["gmicloud", "friendli"],
              "quantizations": ["fp16", "bf16"],
              "sort": {
                "by": "price",
                "partition": "model"
              },
              "max_price": {
                "prompt": 10,
                "completion": 20
              },
              "preferred_min_throughput": {
                "p50": 100,
                "p90": 50
              },
              "preferred_max_latency": {
                "p50": 1,
                "p90": 3,
                "p99": 5
              }
            }
          }
        }
      ]
    }
  }
}
```

### Vercel AI Gateway Example

```json
{
  "providers": {
    "vercel-ai-gateway": {
      "baseUrl": "https://ai-gateway.vercel.sh/v1",
      "apiKey": "AI_GATEWAY_API_KEY",
      "api": "openai-completions",
      "models": [
        {
          "id": "moonshotai/kimi-k2.5",
          "name": "Kimi K2.5 (Fireworks via Vercel)",
          "reasoning": true,
          "input": ["text", "image"],
          "cost": { "input": 0.6, "output": 3, "cacheRead": 0, "cacheWrite": 0 },
          "contextWindow": 262144,
          "maxTokens": 262144,
          "compat": {
            "vercelGatewayRouting": {
              "only": ["fireworks", "novita"],
              "order": ["fireworks", "novita"]
            }
          }
        }
      ]
    }
  }
}
```

#configuration #custom-models #api-integration #local-llm #proxy-settings
