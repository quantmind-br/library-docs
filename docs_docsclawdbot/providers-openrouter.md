---
title: "null"
url: https://docs.clawd.bot/providers/openrouter.md
source: llms
fetched_at: 2026-01-26T10:15:00.771873515-03:00
rendered_js: false
word_count: 81
summary: This document explains how to integrate and configure OpenRouter as a model provider for ClawdBot through CLI commands and environment settings.
tags:
    - openrouter
    - model-providers
    - configuration
    - cli-setup
    - authentication
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# OpenRouter

OpenRouter provides a **unified API** that routes requests to many models behind a single
endpoint and API key. It is OpenAI-compatible, so most OpenAI SDKs work by switching the base URL.

## CLI setup

```bash  theme={null}
clawdbot onboard --auth-choice apiKey --token-provider openrouter --token "$OPENROUTER_API_KEY"
```

## Config snippet

```json5  theme={null}
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

* Model refs are `openrouter/<provider>/<model>`.
* For more model/provider options, see [/concepts/model-providers](/concepts/model-providers).
* OpenRouter uses a Bearer token with your API key under the hood.