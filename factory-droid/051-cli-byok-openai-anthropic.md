---
title: OpenAI & Anthropic
url: https://docs.factory.ai/cli/byok/openai-anthropic.md
source: llms
fetched_at: 2026-03-03T01:12:43.472002-03:00
rendered_js: false
word_count: 133
summary: This document provides instructions for configuring custom OpenAI and Anthropic models in Factory using personal API keys for cost control and prompt caching.
tags:
    - openai
    - anthropic
    - api-configuration
    - custom-models
    - prompt-caching
    - factory-settings
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI & Anthropic

> Use your own API keys for official OpenAI and Anthropic models

Use your own API keys for cost control and billing transparency with official OpenAI and Anthropic models.

## Configuration

Add to `~/.factory/settings.json`:

```json  theme={null}
{
  "customModels": [
    {
      "model": "claude-sonnet-4-5-20250929",
      "displayName": "Sonnet 4.5 [Custom]",
      "baseUrl": "https://api.anthropic.com",
      "apiKey": "YOUR_ANTHROPIC_KEY",
      "provider": "anthropic",
      "maxOutputTokens": 8192
    },
    {
      "model": "gpt-5-codex",
      "displayName": "GPT5-Codex [Custom]",
      "baseUrl": "https://api.openai.com/v1",
      "apiKey": "YOUR_OPENAI_KEY",
      "provider": "openai",
      "maxOutputTokens": 16384
    }
  ]
}
```

## Getting API Keys

### Anthropic

1. Sign up at [console.anthropic.com](https://console.anthropic.com)
2. Navigate to API Keys section
3. Create a new API key
4. Copy and use in your configuration

### OpenAI

1. Sign up at [platform.openai.com](https://platform.openai.com)
2. Go to API Keys section
3. Create a new secret key
4. Copy and use in your configuration

## Notes

* These configurations use the official APIs with full prompt caching support
* Factory automatically handles prompt caching when available
* Use `/cost` command in CLI to view cost breakdowns and cache hit rates