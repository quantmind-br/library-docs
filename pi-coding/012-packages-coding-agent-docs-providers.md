---
title: Providers
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/providers.md
source: git
fetched_at: 2026-04-26T05:48:17.33220982-03:00
rendered_js: false
word_count: 840
summary: This document details how to configure subscription-based providers and API keys for Pi, including authentication methods, environment variable setup, and credential resolution order.
tags:
    - authentication
    - api-keys
    - oauth
    - environment-variables
    - configuration
    - pi-cli
    - cloud-providers
category: configuration
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Providers

Pi supports subscription-based providers via OAuth and API key providers via environment variables or auth file. For each provider, pi knows all available models (list updated with every release).

## Subscriptions

Use `/login` in interactive mode, then select a provider:

- **Claude Pro/Max**
- **ChatGPT Plus/Pro (Codex)** — personal use only; for production, use OpenAI Platform API
- **GitHub Copilot** — press Enter for github.com, or enter GHES domain. If "model not supported", enable it in VS Code: Copilot Chat -> model selector -> select model -> "Enable"
- **Google Gemini CLI** — standard Gemini models via Cloud Code Assist; free with any Google account, subject to rate limits
- **Google Antigravity** — sandbox with Gemini 3, Claude, and GPT-OSS models; free with any Google account, subject to rate limits. For paid Cloud Code Assist: set `GOOGLE_CLOUD_PROJECT` env var

Use `/logout` to clear credentials. Tokens stored in `~/.pi/agent/auth.json`, auto-refresh when expired.

## API Keys

Use `/login` to store an API key in `auth.json`, or set credentials via environment variable:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pi
```

| Provider | Environment Variable | `auth.json` key |
|----------|----------------------|------------------|
| Anthropic | `ANTHROPIC_API_KEY` | `anthropic` |
| Azure OpenAI Responses | `AZURE_OPENAI_API_KEY` | `azure-openai-responses` |
| OpenAI | `OPENAI_API_KEY` | `openai` |
| DeepSeek | `DEEPSEEK_API_KEY` | `deepseek` |
| Google Gemini | `GEMINI_API_KEY` | `google` |
| Mistral | `MISTRAL_API_KEY` | `mistral` |
| Groq | `GROQ_API_KEY` | `groq` |
| Cerebras | `CEREBRAS_API_KEY` | `cerebras` |
| xAI | `XAI_API_KEY` | `xai` |
| OpenRouter | `OPENROUTER_API_KEY` | `openrouter` |
| Vercel AI Gateway | `AI_GATEWAY_API_KEY` | `vercel-ai-gateway` |
| ZAI | `ZAI_API_KEY` | `zai` |
| OpenCode Zen | `OPENCODE_API_KEY` | `opencode` |
| OpenCode Go | `OPENCODE_API_KEY` | `opencode-go` |
| Hugging Face | `HF_TOKEN` | `huggingface` |
| Fireworks | `FIREWORKS_API_KEY` | `fireworks` |
| Kimi For Coding | `KIMI_API_KEY` | `kimi-coding` |
| MiniMax | `MINIMAX_API_KEY` | `minimax` |
| MiniMax (China) | `MINIMAX_CN_API_KEY` | `minimax-cn` |

Reference: [`const envMap`](https://github.com/badlogic/pi-mono/blob/main/packages/ai/src/env-api-keys.ts) in `packages/ai/src/env-api-keys.ts`.

### Auth File

Store credentials in `~/.pi/agent/auth.json`:

```json
{
  "anthropic": { "type": "api_key", "key": "sk-ant-..." },
  "openai": { "type": "api_key", "key": "sk-..." },
  "deepseek": { "type": "api_key", "key": "sk-..." },
  "google": { "type": "api_key", "key": "..." },
  "opencode": { "type": "api_key", "key": "..." },
  "opencode-go": { "type": "api_key", "key": "..." }
}
```

Created with `0600` permissions. Auth file credentials take priority over environment variables.

### Key Resolution

The `key` field supports three formats:

- **Shell command:** `"!command"` — executes and uses stdout (cached for process lifetime)
  ```json
  { "type": "api_key", "key": "!security find-generic-password -ws 'anthropic'" }
  { "type": "api_key", "key": "!op read 'op://vault/item/credential'" }
  ```
- **Environment variable:** Uses the value of the named variable
  ```json
  { "type": "api_key", "key": "MY_ANTHROPIC_KEY" }
  ```
- **Literal value:** Used directly
  ```json
  { "type": "api_key", "key": "sk-ant-..." }
  ```

OAuth credentials are also stored here after `/login` and managed automatically.

## Cloud Providers

### Azure OpenAI

```bash
export AZURE_OPENAI_API_KEY=...
export AZURE_OPENAI_BASE_URL=https://your-resource.openai.azure.com
# or use resource name instead of base URL
export AZURE_OPENAI_RESOURCE_NAME=your-resource

# Optional
export AZURE_OPENAI_API_VERSION=2024-02-01
export AZURE_OPENAI_DEPLOYMENT_NAME_MAP=gpt-4=my-gpt4,gpt-4o=my-gpt4o
```

### Amazon Bedrock

```bash
# Option 1: AWS Profile
export AWS_PROFILE=your-profile

# Option 2: IAM Keys
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...

# Option 3: Bearer Token
export AWS_BEARER_TOKEN_BEDROCK=...

# Optional region (defaults to us-east-1)
export AWS_REGION=us-west-2
```

Also supports ECS task roles (`AWS_CONTAINER_CREDENTIALS_*`) and IRSA (`AWS_WEB_IDENTITY_TOKEN_FILE`).

```bash
pi --provider amazon-bedrock --model us.anthropic.claude-sonnet-4-20250514-v1:0
```

> [!info] Prompt caching is enabled automatically for Claude models whose ID contains a recognizable model name (base models and system-defined inference profiles). For application inference profiles (ARNs without model name), set `AWS_BEDROCK_FORCE_CACHE=1`:
>
> ```bash
> export AWS_BEDROCK_FORCE_CACHE=1
> pi --provider amazon-bedrock --model arn:aws:bedrock:us-east-1:123456789012:application-inference-profile/abc123
> ```

Bedrock API proxy environment variables:

```bash
# Set the URL for the Bedrock proxy (standard AWS SDK env var)
export AWS_ENDPOINT_URL_BEDROCK_RUNTIME=https://my.corp.proxy/bedrock

# Set if your proxy does not require authentication
export AWS_BEDROCK_SKIP_AUTH=1

# Set if your proxy only supports HTTP/1.1
export AWS_BEDROCK_FORCE_HTTP1=1
```

### Google Vertex AI

Uses Application Default Credentials:

```bash
gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT=your-project
export GOOGLE_CLOUD_LOCATION=us-central1
```

Or set `GOOGLE_APPLICATION_CREDENTIALS` to a service account key file.

## Custom Providers

- **Via models.json:** Add Ollama, LM Studio, vLLM, or any provider speaking a supported API (OpenAI Completions, OpenAI Responses, Anthropic Messages, Google Generative AI). See [models.md](models.md).
- **Via extensions:** For providers needing custom API implementations or OAuth flows, create an extension. See [custom-provider.md](custom-provider.md) and [examples/extensions/custom-provider-gitlab-duo](../examples/extensions/custom-provider-gitlab-duo/).

## Resolution Order

When resolving credentials for a provider:

1. CLI `--api-key` flag
2. `auth.json` entry (API key or OAuth token)
3. Environment variable
4. Custom provider keys from `models.json`

#authentication #api-keys #cloud-providers #configuration
