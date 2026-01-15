---
title: Fireworks AI - Factory Documentation
url: https://docs.factory.ai/cli/byok/fireworks
source: sitemap
fetched_at: 2026-01-13T19:03:29.491459757-03:00
rendered_js: false
word_count: 62
summary: Instructions for integrating Fireworks AI's high-performance inference API into the Factory tool, including how to manually configure custom models via settings.json.
tags:
    - fireworks-ai
    - api-integration
    - model-configuration
    - inference-api
    - custom-models
    - json-config
category: configuration
---

Access high-performance inference for open-source models with Fireworks AI’s optimized serving infrastructure.

## Configuration

Add to `~/.factory/settings.json`:

```
{
  "customModels": [
    {
      "model": "accounts/fireworks/models/glm-4p5",
      "displayName": "GLM 4.5 [Fireworks]",
      "baseUrl": "https://api.fireworks.ai/inference/v1",
      "apiKey": "YOUR_FIREWORKS_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    },
    {
      "model": "accounts/fireworks/models/deepseek-v3p1-terminus",
      "displayName": "Deepseek V3.1 Terminus [Fireworks]",
      "baseUrl": "https://api.fireworks.ai/inference/v1",
      "apiKey": "YOUR_FIREWORKS_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 20480
    }
  ]
}
```

## Getting Started

1. Sign up at [fireworks.ai](https://fireworks.ai)
2. Get your API key from the dashboard
3. Browse available models in their [model catalog](https://fireworks.ai/models)
4. Add desired models to your configuration

## Notes

- Base URL format: `https://api.fireworks.ai/inference/v1`
- Model IDs typically start with `accounts/fireworks/models/`
- Supports streaming responses and function calling for compatible models