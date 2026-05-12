---
title: Providers
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/providers.md
source: git
fetched_at: 2026-05-03T09:31:16.538924066-03:00
rendered_js: false
word_count: 620
summary: This document provides a comprehensive guide on configuring authentication, managing API keys, and setting up cloud provider integrations for the Pi agent.
tags:
    - authentication
    - api-keys
    - configuration
    - oauth
    - cloud-providers
    - environment-variables
category: configuration
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Providers

Pi supports subscription-based providers via OAuth and API key providers via environment variables or auth file. The provider/model list updates with every release.

## Subscriptions

Use `/login` in interactive mode to authenticate via OAuth:

| Provider | Notes |
|----------|-------|
| ChatGPT Plus/Pro (Codex) | Requires subscription; [Codex for OSS](https://developers.openai.com/community/codex-for-oss) |
| Claude Pro/Max | Extra usage billed per token, not against plan limits |
| GitHub Copilot | Press Enter for github.com, or enter your GitHub Enterprise Server domain |

Use `/logout` to clear credentials. Tokens stored in `~/.pi/agent/auth.json`, auto-refreshed when expired.

> [!note]
> If Copilot shows "model not supported", enable it in VS Code: Copilot Chat → model selector → select model → "Enable"

## API Keys

### Environment Variables

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pi
```

### Auth File

Store in `~/.pi/agent/auth.json` (0600 permissions):

```json
{
  "anthropic": { "type": "api_key", "key": "sk-ant-..." },
  "openai": { "type": "api_key", "key": "sk-..." }
}
```

Auth file takes priority over environment variables.

### Key Formats

| Format | Example |
|--------|--------|
| Shell command | `"key": "!security find-generic-password -ws 'anthropic'"` |
| Env var name | `"key": "MY_ANTHROPIC_KEY"` |
| Literal | `"key": "sk-ant-..."` |

### Provider Credentials

| Provider | Env Variable | `auth.json` key |
|----------|--------------|-----------------|
| Anthropic | `ANTHROPIC_API_KEY` | `anthropic` |
| Azure OpenAI Responses | `AZURE_OPENAI_API_KEY` | `azure-openai-responses` |
| OpenAI | `OPENAI_API_KEY` | `openai` |
| DeepSeek | `DEEPSEEK_API_KEY` | `deepseek` |
| Google Gemini | `GEMINI_API_KEY` | `google` |
| Mistral | `MISTRAL_API_KEY` | `mistral` |
| Groq | `GROQ_API_KEY` | `groq` |
| Cerebras | `CEREBRAS_API_KEY` | `cerebras` |
| Cloudflare AI Gateway | `CLOUDFLARE_API_KEY` + `CLOUDFLARE_ACCOUNT_ID` + `CLOUDFLARE_GATEWAY_ID` | `cloudflare-ai-gateway` |
| Cloudflare Workers AI | `CLOUDFLARE_API_KEY` + `CLOUDFLARE_ACCOUNT_ID` | `cloudflare-workers-ai` |
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
| Xiaomi MiMo | `XIAOMI_API_KEY` | `xiaomi` |
| Xiaomi MiMo Token Plan (CN/AMS/SGP) | `XIAOMI_TOKEN_PLAN_CN_API_KEY` / `_AMS_API_KEY` / `_SGP_API_KEY` | `xiaomi-token-plan-cn/ams/sgp` |

Reference: [`const envMap`](https://github.com/badlogic/pi-mono/blob/main/packages/ai/src/env-api-keys.ts) in `packages/ai/src/env-api-keys.ts`.

## Cloud Providers

### Azure OpenAI

```bash
export AZURE_OPENAI_API_KEY=...
export AZURE_OPENAI_BASE_URL=https://your-resource.openai.azure.com
# or: AZURE_OPENAI_RESOURCE_NAME=your-resource

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

**Prompt caching**: automatic for Claude models with recognizable names. For application inference profiles, set:

```bash
export AWS_BEDROCK_FORCE_CACHE=1
```

**Bedrock API proxy**:

```bash
export AWS_ENDPOINT_URL_BEDROCK_RUNTIME=https://my.corp.proxy/bedrock
export AWS_BEDROCK_SKIP_AUTH=1         # if proxy doesn't require auth
export AWS_BEDROCK_FORCE_HTTP1=1       # if proxy only supports HTTP/1.1
```

### Cloudflare AI Gateway

```bash
export CLOUDFLARE_API_KEY=...           # or /login
export CLOUDFLARE_ACCOUNT_ID=...
export CLOUDFLARE_GATEWAY_ID=...        # dash.cloudflare.com → AI → AI Gateway
pi --provider cloudflare-ai-gateway --model "claude-sonnet-4-5"
```

Routes OpenAI, Anthropic, and Workers AI through AI Gateway. Workers AI uses unified API (`/compat`) with prefixed model IDs (`workers-ai/@cf/...`). OpenAI uses passthrough (`/openai`), Anthropic uses (`/anthropic`).

**Upstream authentication modes**:

| Mode | Request auth | Upstream auth |
|------|--------------|---------------|
| Workers AI | Cloudflare token | Cloudflare-native |
| Unified billing | Cloudflare token | Cloudflare handles upstream |
| Stored BYOK | Cloudflare token | Cloudflare injects provider keys |
| Inline BYOK | Cloudflare token + `Authorization` header | Request supplies provider key |

> [!tip]
> For normal pi usage, prefer unified billing or stored BYOK.

### Cloudflare Workers AI

```bash
export CLOUDFLARE_API_KEY=...           # or /login
export CLOUDFLARE_ACCOUNT_ID=...
pi --provider cloudflare-workers-ai --model "@cf/moonshotai/kimi-k2.6"
```

Pi automatically sets `x-session-affinity` for [prefix caching](https://developers.cloudflare.com/workers-ai/features/prompt-caching/).

### Google Vertex AI

Uses Application Default Credentials:

```bash
gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT=your-project
export GOOGLE_CLOUD_LOCATION=us-central1
```

Or set `GOOGLE_APPLICATION_CREDENTIALS` to a service account key file.

## Custom Providers

**Via [[052-packages-coding-agent-docs-models|Custom Models]]**: Add Ollama, LM Studio, vLLM, or any provider that speaks a supported API (OpenAI Completions, Responses, Anthropic Messages, Google Generative AI).

**Via extensions**: For providers needing custom API implementations or OAuth flows. See [[022-packages-coding-agent-docs-custom-provider|Custom Providers]] and the [GitLab Duo example](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent/examples/extensions/custom-provider-gitlab-duo/).

## Resolution Order

1. CLI `--api-key` flag
2. `auth.json` entry
3. Environment variable
4. Custom provider keys from `models.json`

#providers #authentication #api-keys #configuration #oauth #cloud-providers