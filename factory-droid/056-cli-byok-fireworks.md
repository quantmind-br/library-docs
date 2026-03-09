---
title: Fireworks AI
url: https://docs.factory.ai/cli/byok/fireworks.md
source: llms
fetched_at: 2026-03-03T01:12:36.465049-03:00
rendered_js: false
word_count: 93
summary: This document provides instructions for integrating Fireworks AI models into the Factory environment by configuring settings and API keys for high-performance inference.
tags:
    - fireworks-ai
    - model-configuration
    - inference-serving
    - llm-integration
    - custom-models
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fireworks AI

> High-performance inference for open-source models with optimized serving

Access high-performance inference for open-source models with Fireworks AI's optimized serving infrastructure.

## Configuration

Add to `~/.factory/settings.json`:

```json  theme={null}
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

* Base URL format: `https://api.fireworks.ai/inference/v1`
* Model IDs typically start with `accounts/fireworks/models/`
* Supports streaming responses and function calling for compatible models