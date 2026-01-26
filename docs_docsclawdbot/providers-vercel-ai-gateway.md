---
title: Vercel AI Gateway
url: https://docs.clawd.bot/providers/vercel-ai-gateway.md
source: llms
fetched_at: 2026-01-26T09:53:29.714123546-03:00
rendered_js: false
word_count: 95
summary: This document provides instructions for integrating Vercel AI Gateway with ClawdBot, covering authentication, default model configuration, and environment setup.
tags:
    - vercel-ai-gateway
    - clawdbot
    - api-integration
    - authentication
    - configuration-guide
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# Vercel AI Gateway

# Vercel AI Gateway

The [Vercel AI Gateway](https://vercel.com/ai-gateway) provides a unified API to access hundreds of models through a single endpoint.

* Provider: `vercel-ai-gateway`
* Auth: `AI_GATEWAY_API_KEY`
* API: Anthropic Messages compatible

## Quick start

1. Set the API key (recommended: store it for the Gateway):

```bash  theme={null}
clawdbot onboard --auth-choice ai-gateway-api-key
```

2. Set a default model:

```json5  theme={null}
{
  agents: {
    defaults: {
      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.5" }
    }
  }
}
```

## Non-interactive example

```bash  theme={null}
clawdbot onboard --non-interactive \
  --mode local \
  --auth-choice ai-gateway-api-key \
  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
```

## Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `AI_GATEWAY_API_KEY`
is available to that process (for example, in `~/.clawdbot/.env` or via
`env.shellEnv`).