---
title: "Custom LLM Providers in ForgeCode"
url: https://forgecode.dev/docs/custom-providers/
source: sitemap
fetched_at: 2026-04-30T14:09:04.319602625-03:00
rendered_js: false
word_count: 267
summary: "Configure custom LLM providers in ForgeCode via `.forge.toml` for self-hosted models, gateways, or regional endpoints."
tags:
  - forgecode
  - llm-provider
  - configuration
  - api-integration
  - custom-endpoints
category: configuration
optimized: true
---
# Custom LLM Providers in ForgeCode

> **TL;DR**
> Define custom providers in `.forge.toml` to connect to any OpenAI-compatible endpoint.

## Basics

### Provider Entry
```toml
[[providers]]
id = "my_provider"
url = "https://api.example.com/v1/chat/completions"
api_key_vars = ["MY_API_KEY"]
```

### Default Session
```toml
[session]
provider_id = "my_provider"
model = "my_model"
```

> **Switch providers**: Use `:provider` in ForgeCode.

## Configuration Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | Yes | Unique identifier (e.g., `my_provider`) |
| `url` | Yes | Chat completions endpoint (supports `{{VAR}}` placeholders) |
| `api_key_vars` | No | Environment variable for API key |
| `auth_methods` | No | Auth method (default: `["api_key"]`; use `["google_adc"]` for Google ADC) |
| `custom_headers` | No | Additional HTTP headers |
| `models` | No | Model source (URL or inline array) |
| `provider_type` | No | `llm` (default) or `context_engine` |
| `response_type` | No | Wire protocol (`OpenAI`, `Anthropic`, etc.) |
| `url_param_vars` | No | Environment variables for URL placeholders |

## Dynamic URLs
Use `{{VAR}}` placeholders in `url` and `models`:
```toml
url = "https://{{REGION}}.api.example.com/v1"
url_param_vars = ["REGION"]
```

## Model Definitions
### URL-Based
```toml
models = "https://api.example.com/v1/models"
```

### Inline Array
```toml
models = [
  { id = "model1", name = "My Model", context_length = 8192 },
  { id = "model2", name = "Another Model", tools_supported = true }
]
```

### Model Fields
| Field | Description |
|-------|-------------|
| `id` | API identifier |
| `name` | Display name |
| `description` | Short description |
| `context_length` | Max tokens |
| `tools_supported` | Supports tool calling |
| `supports_parallel_tool_calls` | Parallel tool execution |
| `supports_reasoning` | Extended reasoning |
| `input_modalities` | Input types (e.g., `["text", "image"]`) |

## Headers & Auth
### Custom Headers
```toml
[providers.custom_headers]
X-Gateway-Token = "{{GATEWAY_TOKEN}}"
```

### Google ADC
```toml
auth_methods = ["google_adc"]
```

## Proxy & Certificates
Configure in `[http]` section of `.forge.toml`:
```toml
[http]
proxy = "http://proxy.example.com:8080"
ca_bundle = "/path/to/ca.pem"
```

See [Proxy Configuration](https://forgecode.dev/docs/proxy-configuration/).

## Testing
1. Edit config:
   ```bash
   forge config edit
   ```
2. Switch provider:
   ```bash
   :provider my_provider
   ```
3. Test a prompt.

## Full Reference
See [`.forge.toml`](https://forgecode.dev/docs/forgecode-config/).