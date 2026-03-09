---
title: DeepInfra
url: https://docs.factory.ai/cli/byok/deepinfra.md
source: llms
fetched_at: 2026-03-03T01:12:35.776992-03:00
rendered_js: false
word_count: 98
summary: This document provides instructions for integrating DeepInfra's open-source model inference services into the Factory platform through custom JSON configuration.
tags:
    - deepinfra
    - llm-inference
    - configuration
    - openai-compatible
    - model-integration
    - factory-ai
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# DeepInfra

> Cost-effective inference for a wide variety of open-source models

Access cost-effective inference for a wide variety of open-source models with DeepInfra's optimized infrastructure.

## Configuration

Add to `~/.factory/settings.json`:

```json  theme={null}
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

* Base URL format: `https://api.deepinfra.com/v1/openai`
* Model names match Hugging Face repository format
* Supports OpenAI-compatible API
* Automatic model updates when new versions are released