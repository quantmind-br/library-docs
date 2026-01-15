---
title: Factory Droid | CLIProxyAPI
url: https://help.router-for.me/cn/agent-client/droid
source: crawler
fetched_at: 2026-01-14T22:10:15.706529849-03:00
rendered_js: false
word_count: 1
summary: This document defines custom models for AI services, including model names, base URLs, API keys, and providers like OpenAI and Anthropic.
tags:
    - custom-models
    - ai-configuration
    - openai
    - anthropic
    - api-settings
category: configuration
---

json

```
{
  "custom_models": [
    {
      "model": "gemini-2.5-pro",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    },
    {
      "model": "claude-sonnet-4-5-20250929",
      "base_url": "http://127.0.0.1:8317",
      "api_key": "sk-dummy",
      "provider": "anthropic"
    },
    {
      "model": "claude-opus-4-1-20250805",
      "base_url": "http://127.0.0.1:8317",
      "api_key": "sk-dummy",
      "provider": "anthropic"
    },
    {
      "model": "claude-sonnet-4-20250514",
      "base_url": "http://127.0.0.1:8317",
      "api_key": "sk-dummy",
      "provider": "anthropic"
    },
    {
      "model": "gpt-5",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    },
    {
      "model": "gpt-5(minimal)",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    },
    {
      "model": "gpt-5(low)",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    },
    {
      "model": "gpt-5(medium)",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    },
    {
      "model": "gpt-5(high)",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    },
    {
      "model": "gpt-5-codex",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    },
    {
      "model": "gpt-5-codex(low)",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    },
    {
      "model": "gpt-5-codex(medium)",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    },
    {
      "model": "gpt-5-codex(high)",
      "base_url": "http://127.0.0.1:8317/v1",
      "api_key": "sk-dummy",
      "provider": "openai"
    }
  ]
}
```