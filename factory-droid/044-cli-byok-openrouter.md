---
title: OpenRouter
url: https://docs.factory.ai/cli/byok/openrouter.md
source: llms
fetched_at: 2026-02-05T21:41:07.839000941-03:00
rendered_js: false
word_count: 91
summary: This document explains how to integrate OpenRouter with the Factory platform by configuring custom model settings in the JSON configuration file.
tags:
    - openrouter
    - custom-models
    - api-integration
    - factory-settings
    - llm-provider
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenRouter

> Access models from multiple providers through a unified interface

Connect to OpenRouter for access to models from multiple providers through a single API interface.

## Configuration

Add to `~/.factory/settings.json`:

```json  theme={null}
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

* OpenRouter uses the `generic-chat-completion-api` provider type
* Some models may have usage restrictions or require additional permissions