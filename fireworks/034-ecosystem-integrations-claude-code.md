---
title: Claude Code - Fireworks AI Docs
url: https://docs.fireworks.ai/ecosystem/integrations/claude-code
source: sitemap
fetched_at: 2026-04-27T20:15:49.491296417-03:00
rendered_js: false
word_count: 337
summary: This document details how to integrate and configure Fireworks AI models (Kimi-2.5 and GLM-5) as drop-in replacements for Claude Code, providing setup instructions via settings.json files, environment variables, and integration guides for middleware like LiteLLM and Portkey.
tags:
    - fireworks-ai
    - claude-code
    - api-integration
    - kimi-2.5
    - glm-5
    - configuration
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Fireworks AI supports Claude Code through the Anthropic-compatible API, enabling open-source models as drop-in replacements for Claude's models.

## Choose your model

| Model | Description |
|---|---|
| **Kimi-2.5** (Moonshot) | Agent model optimized for coding, reasoning, and long-context tasks. 256k context window, native multimodal. |
| **GLM-5** (Zhipu AI) | Large-scale model for code generation, reasoning, and AI agents with tool use. Alternative to Claude Sonnet 4.5, GPT-5, and Gemini 3 Pro. |

## Quick setup

Create a `.claude/settings.json` file in your home directory or project directory:

```json
./.claude/settings.json
```

Add the following configuration:

> [!example]
> Replace `your-fireworks-api-key` with your actual key from [app.fireworks.ai](https://app.fireworks.ai).

### Kimi-2.5

```json
{
    "$schema": "https://json.schemastore.org/claude-code-settings.json",
    "apiKeyHelper": "bash -c 'echo your-fireworks-api-key'",
    "env": {
        "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
        "ANTHROPIC_MODEL": "accounts/fireworks/models/kimi-k2p5",
        "ANTHROPIC_SMALL_FAST_MODEL": "accounts/fireworks/models/kimi-k2p5",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "accounts/fireworks/models/kimi-k2p5",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "accounts/fireworks/models/kimi-k2p5",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "accounts/fireworks/models/kimi-k2p5"
    },
    "model": "accounts/fireworks/models/kimi-k2p5"
}
```

### GLM-5

```json
{
    "$schema": "https://json.schemastore.org/claude-code-settings.json",
    "apiKeyHelper": "bash -c 'echo your-fireworks-api-key'",
    "env": {
        "ANTHROPIC_BASE_URL": "https://api.fireworks.ai/inference",
        "ANTHROPIC_MODEL": "accounts/fireworks/models/glm-5",
        "ANTHROPIC_SMALL_FAST_MODEL": "accounts/fireworks/models/glm-5",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "accounts/fireworks/models/glm-5",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "accounts/fireworks/models/glm-5",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "accounts/fireworks/models/glm-5"
    },
    "model": "accounts/fireworks/models/glm-5"
}
```

Claude Code automatically detects the configuration and uses Fireworks models.

## Model IDs

Use Fireworks model IDs directly without the `fireworks_ai/` prefix:

| Model | Model ID |
|---|---|
| Kimi-2.5 | `accounts/fireworks/models/kimi-k2p5` |
| GLM-5 | `accounts/fireworks/models/glm-5` |

## Environment variables alternative

Use `ANTHROPIC_AUTH_TOKEN` (not `ANTHROPIC_API_KEY`) for proper authentication:

```bash
export ANTHROPIC_BASE_URL="https://api.fireworks.ai/inference"
export ANTHROPIC_AUTH_TOKEN="your-fireworks-api-key"
export ANTHROPIC_MODEL="accounts/fireworks/models/<MODEL>"
export ANTHROPIC_SMALL_FAST_MODEL="accounts/fireworks/models/<MODEL>"
export ANTHROPIC_DEFAULT_SONNET_MODEL="accounts/fireworks/models/<MODEL>"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="accounts/fireworks/models/<MODEL>"
export ANTHROPIC_DEFAULT_OPUS_MODEL="accounts/fireworks/models/<MODEL>"
```

## Middleware / proxy providers

### LiteLLM proxy (self-hosted)

**1. LiteLLM config.yaml:**

```yaml
general_settings:
  allow_client_side_credentials: true
  pass_through_endpoints:
    - path: "/fw-anthropic"
      target: "https://api.fireworks.ai/inference"
      include_subpath: true
      forward_headers: true
```

**2. Claude Code settings:**

> [!note]
> Replace `<YOUR_LITELLM_HOST_IP_OR_DOMAIN>` with your LiteLLM host. Use `fw-anthropic` as the base path.

### Portkey

[Portkey](https://portkey.ai) provides a managed gateway for routing requests to Fireworks with observability and control features.

**1. Portkey provider setup:** In your Portkey dashboard, create an Anthropic provider:

- **Provider**: Anthropic
- **Custom Host**: `https://api.fireworks.ai/inference/v1`
- **API Key**: Your Fireworks API key

**2. Claude Code settings:**

```json
{
    "$schema": "https://json.schemastore.org/claude-code-settings.json",
    "env": {
        "ANTHROPIC_BASE_URL": "https://api.portkey.ai",
        "ANTHROPIC_AUTH_TOKEN": "your-portkey-api-key",
        "ANTHROPIC_CUSTOM_HEADERS": "x-portkey-api-key: your-portkey-api-key\nx-portkey-provider: your-custom-fireworks-provider\nanthropic-version: 2023-06-01",
        "ANTHROPIC_MODEL": "accounts/fireworks/models/<MODEL>",
        "ANTHROPIC_SMALL_FAST_MODEL": "accounts/fireworks/models/<MODEL>",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "accounts/fireworks/models/<MODEL>",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "accounts/fireworks/models/<MODEL>",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "accounts/fireworks/models/<MODEL>"
    },
    "model": "accounts/fireworks/models/<MODEL>"
}
```

## Why use Fireworks with Claude Code?

- **Cost savings** — significantly lower cost per token vs. Claude's native pricing
- **No rate limits** — no hourly quotas or surprise throttling
- **Model choice** — access to the latest open-source models
- **Privacy** — your code stays within your chosen infrastructure
- **Transparent pricing** — clear per-token pricing without subscription tiers

## Next steps

- [[033-ecosystem-integrations-agent-frameworks|Agent Frameworks]] — explore other integrations
- [[069-guides-function-calling|Function Calling]] — tool use with Fireworks
- [[078-guides-reasoning|Reasoning Models]] — complex task handling

## Need help?

[Contact the team](https://fireworks.ai/contact) or join the [Discord community](https://discord.gg/fireworks-ai).

#claude-code #kimi-2.5 #glm-5 #api-integration
