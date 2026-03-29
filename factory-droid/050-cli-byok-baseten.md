---
title: Baseten
url: https://docs.factory.ai/cli/byok/baseten.md
source: llms
fetched_at: 2026-02-05T21:40:45.990331566-03:00
rendered_js: false
word_count: 114
summary: This document provides instructions for integrating Baseten-hosted machine learning models into Factory using a configuration file and API credentials.
tags:
    - baseten
    - model-serving
    - configuration
    - api-integration
    - machine-learning
    - custom-models
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Baseten

> Deploy and serve custom models with enterprise-grade infrastructure

Deploy and serve custom models with Baseten's enterprise-grade infrastructure for ML model serving.

## Configuration

Add to `~/.factory/settings.json`:

```json  theme={null}
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

* Base URL format: `https://inference.baseten.co/v1`
* Replace `YOUR_MODEL_ID` with your deployed model's ID from Baseten dashboard
* Supports OpenAI-compatible API format
* Contact Baseten for enterprise features and custom deployments