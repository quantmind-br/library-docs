---
title: Groq
url: https://docs.factory.ai/cli/byok/groq.md
source: llms
fetched_at: 2026-03-03T01:12:39.851436-03:00
rendered_js: false
word_count: 101
summary: This document explains how to configure and integrate Groq's LPU Inference Engine into Factory to enable high-speed inference for open-source models.
tags:
    - groq
    - lpu-inference
    - configuration
    - api-integration
    - factory-ai
    - model-setup
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Groq

> Ultra-fast inference with Groq's LPU™ Inference Engine

Access ultra-fast inference powered by Groq's LPU™ (Language Processing Unit) Inference Engine for various open-source models.

## Configuration

Add to `~/.factory/settings.json`:

```json  theme={null}
{
  "customModels": [
    {
      "model": "moonshotai/kimi-k2-instruct-0905",
      "displayName": "Kimi K2 [Groq]",
      "baseUrl": "https://api.groq.com/openai/v1",
      "apiKey": "YOUR_GROQ_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    }
  ]
}
```

## Getting Started

1. Sign up at [groq.com](https://groq.com)
2. Get your API key from [console.groq.com](https://console.groq.com)
3. Browse available models in the [Groq documentation](https://console.groq.com/docs/overview.md)
4. Add desired models to your configuration

## Notes

* Base URL format: `https://api.groq.com/openai/v1`
* Groq uses the `generic-chat-completion-api` provider type
* Known for extremely fast inference speeds thanks to LPU architecture
* Supports streaming responses for compatible models