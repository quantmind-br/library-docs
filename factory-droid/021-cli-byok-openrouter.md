---
title: OpenRouter - Factory Documentation
url: https://docs.factory.ai/cli/byok/openrouter
source: sitemap
fetched_at: 2026-04-15T09:01:24.581748228-03:00
rendered_js: false
word_count: 60
summary: This document provides instructions for configuring and connecting external AI models from OpenRouter to the factory environment using a unified API interface.
tags:
    - openrouter
    - api-configuration
    - model-integration
    - generic-chat-completion
    - llm-setup
category: configuration
---

Connect to OpenRouter for access to models from multiple providers through a single API interface.

## Configuration

Add to `~/.factory/settings.json`:

```
{
  "customModels": [
    {
      "model": "openai/gpt-oss-20b",
      "displayName": "GPT-OSS-20B [OpenRouter]",
      "baseUrl": "https://openrouter.ai/api/v1",
      "apiKey": "YOUR_OPENROUTER_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32000
    }
  ]
}
```

## Getting Started

1. Sign up at [openrouter.ai](https://openrouter.ai)
2. Get your API key from the dashboard
3. Browse available models at [openrouter.ai/models](https://openrouter.ai/models)
4. Add desired models to your configuration

## Notes

- OpenRouter uses the `generic-chat-completion-api` provider type
- Some models may have usage restrictions or require additional permissions