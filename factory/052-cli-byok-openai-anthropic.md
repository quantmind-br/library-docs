---
title: OpenAI & Anthropic - Factory Documentation
url: https://docs.factory.ai/cli/byok/openai-anthropic
source: sitemap
fetched_at: 2026-01-13T19:03:27.393530143-03:00
rendered_js: false
word_count: 98
summary: Instructions for configuring personal API keys to use official OpenAI and Anthropic models within the Factory application for cost tracking and billing transparency.
tags:
    - api-keys
    - custom-models
    - openai
    - anthropic
    - configuration
    - settings
category: configuration
---

Use your own API keys for cost control and billing transparency with official OpenAI and Anthropic models.

## Configuration

Add to `~/.factory/settings.json`:

```
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

- These configurations use the official APIs with full prompt caching support
- Factory automatically handles prompt caching when available
- Use `/cost` command in CLI to view cost breakdowns and cache hit rates