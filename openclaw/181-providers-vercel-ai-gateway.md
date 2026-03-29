---
title: Vercel AI Gateway - OpenClaw
url: https://docs.openclaw.ai/providers/vercel-ai-gateway
source: sitemap
fetched_at: 2026-01-30T20:25:13.631861187-03:00
rendered_js: false
word_count: 68
summary: This document explains how to configure and use the Vercel AI Gateway as a unified interface for accessing multiple AI models through a single endpoint.
tags:
    - ai-gateway
    - api-integration
    - authentication
    - model-access
    - configuration-guide
category: guide
---

The [Vercel AI Gateway](https://vercel.com/ai-gateway) provides a unified API to access hundreds of models through a single endpoint.

- Provider: `vercel-ai-gateway`
- Auth: `AI_GATEWAY_API_KEY`
- API: Anthropic Messages compatible

## Quick start

1. Set the API key (recommended: store it for the Gateway):

```
openclaw onboard --auth-choice ai-gateway-api-key
```

2. Set a default model:

```
{
  agents: {
    defaults: {
      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.5" }
    }
  }
}
```

## Non-interactive example

```
openclaw onboard --non-interactive \
  --mode local \
  --auth-choice ai-gateway-api-key \
  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
```

## Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `AI_GATEWAY_API_KEY` is available to that process (for example, in `~/.openclaw/.env` or via `env.shellEnv`).