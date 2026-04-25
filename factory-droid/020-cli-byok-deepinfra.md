---
title: DeepInfra - Factory Documentation
url: https://docs.factory.ai/cli/byok/deepinfra
source: sitemap
fetched_at: 2026-04-15T09:00:59.114606793-03:00
rendered_js: false
word_count: 73
summary: This document provides instructions on how to configure and integrate DeepInfra's open-source model inference services into the local factory settings environment.
tags:
    - deepinfra
    - inference
    - api-configuration
    - model-integration
    - openai-compatible
    - llm
category: configuration
---

- [Configuration](#configuration)
- [Getting Started](#getting-started)
- [Notes](#notes)

Access cost-effective inference for a wide variety of open-source models with DeepInfra’s optimized infrastructure.

## Configuration

Add to `~/.factory/settings.json`:

```
{
  "customModels": [
    {
      "model": "zai-org/GLM-4.7",
      "displayName": "GLM-4.7 [DeepInfra]",
      "baseUrl": "https://api.deepinfra.com/v1/openai",
      "apiKey": "YOUR_DEEPINFRA_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    },
    {
      "model": "deepseek-ai/DeepSeek-V3.1-Terminus",
      "displayName": "DeepSeek V3.1 Terminus [DeepInfra]",
      "baseUrl": "https://api.deepinfra.com/v1/openai",
      "apiKey": "YOUR_DEEPINFRA_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    },
    {
      "model": "moonshotai/Kimi-K2-Instruct-0905",
      "displayName": "Kimi K2 Instruct [DeepInfra]",
      "baseUrl": "https://api.deepinfra.com/v1/openai",
      "apiKey": "YOUR_DEEPINFRA_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32768
    },
    {
      "model": "Qwen/Qwen3-Coder-480B-A35B-Instruct-Turbo",
      "displayName": "Qwen3 Coder 480B [DeepInfra]",
      "baseUrl": "https://api.deepinfra.com/v1/openai",
      "apiKey": "YOUR_DEEPINFRA_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32768
    }
  ]
}
```

## Getting Started

1. Sign up at [deepinfra.com](https://deepinfra.com)
2. Get your API token from the dashboard
3. View available models at their [model list](https://deepinfra.com/models)
4. Add desired models to your configuration

## Notes

- Base URL format: `https://api.deepinfra.com/v1/openai`
- Model names match Hugging Face repository format
- Supports OpenAI-compatible API
- Automatic model updates when new versions are released

[Baseten](https://docs.factory.ai/cli/byok/baseten)[Fireworks AI](https://docs.factory.ai/cli/byok/fireworks)