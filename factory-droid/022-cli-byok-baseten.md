---
title: Baseten - Factory Documentation
url: https://docs.factory.ai/cli/byok/baseten
source: sitemap
fetched_at: 2026-04-15T09:01:28.464839693-03:00
rendered_js: false
word_count: 84
summary: This document provides instructions on how to integrate and configure custom machine learning models hosted on Baseten into a local environment using the Factory settings file.
tags:
    - baseten
    - ml-serving
    - model-deployment
    - api-configuration
    - machine-learning
category: configuration
---

Deploy and serve custom models with Baseten’s enterprise-grade infrastructure for ML model serving.

## Configuration

Add to `~/.factory/settings.json`:

```
{
  "customModels": [
    {
      "model": "Qwen/Qwen3-Coder-480B-A35B-Instruct",
      "displayName": "Qwen3-Coder-480B [Baseten]",
      "baseUrl": "https://inference.baseten.co/v1",
      "apiKey": "YOUR_BASETEN_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 8192
    }
  ]
}
```

## Getting Started

1. Sign up at [baseten.co](https://baseten.co)
2. Deploy a model from their model library or upload your own
3. Get your API key from the settings page
4. Find your model ID in the deployment dashboard
5. Add the configuration to your Factory config

## Notes

- Base URL format: `https://inference.baseten.co/v1`
- Replace `YOUR_MODEL_ID` with your deployed model’s ID from Baseten dashboard
- Supports OpenAI-compatible API format
- Contact Baseten for enterprise features and custom deployments