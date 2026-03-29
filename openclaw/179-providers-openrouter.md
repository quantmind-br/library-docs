---
title: Openrouter - OpenClaw
url: https://docs.openclaw.ai/providers/openrouter
source: sitemap
fetched_at: 2026-01-30T20:24:56.753252998-03:00
rendered_js: false
word_count: 58
summary: This document explains how to use OpenRouter's unified API to access multiple AI models through a single endpoint with OpenAI compatibility, including setup instructions and configuration details.
tags:
    - unified-api
    - openai-compatible
    - model-routing
    - api-setup
    - configuration
category: guide
---

OpenRouter provides a **unified API** that routes requests to many models behind a single endpoint and API key. It is OpenAI-compatible, so most OpenAI SDKs work by switching the base URL.

## CLI setup

```
openclaw onboard --auth-choice apiKey --token-provider openrouter --token "$OPENROUTER_API_KEY"
```

## Config snippet

```
{
  env: { OPENROUTER_API_KEY: "sk-or-..." },
  agents: {
    defaults: {
      model: { primary: "openrouter/anthropic/claude-sonnet-4-5" }
    }
  }
}
```

## Notes

- Model refs are `openrouter/<provider>/<model>`.
- For more model/provider options, see [/concepts/model-providers](https://docs.openclaw.ai/concepts/model-providers).
- OpenRouter uses a Bearer token with your API key under the hood.