---
title: Hugging Face - Factory Documentation
url: https://docs.factory.ai/cli/byok/huggingface
source: sitemap
fetched_at: 2026-01-13T19:03:27.166436655-03:00
rendered_js: false
word_count: 73
summary: This document explains how to configure and integrate Hugging Face Inference Providers to access a wide variety of hosted large language models.
tags:
    - hugging-face
    - llm-integration
    - model-configuration
    - api-keys
    - inference-providers
category: configuration
---

Connect to thousands of models hosted on Hugging Face’s Inference Providers. Learn more in the [Inference Providers documentation](https://huggingface.co/docs/inference-providers/en/index).

## Configuration

Add to `~/.factory/settings.json`:

```
{
  "customModels": [
    {
      "model": "openai/gpt-oss-120b:fireworks-ai",
      "displayName": "GPT OSS 120B [HF Router]",
      "baseUrl": "https://router.huggingface.co/v1",
      "apiKey": "YOUR_HF_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32768
    },
    {
      "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct:fireworks-ai",
      "displayName": "Llama 4 Scout 17B [HF Router]",
      "baseUrl": "https://router.huggingface.co/v1",
      "apiKey": "YOUR_HF_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    }
  ]
}
```

## Getting Started

1. Sign up at [huggingface.co](https://huggingface.co)
2. Get your token from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
3. Browse models at [huggingface.co/models](https://huggingface.co/models?pipeline_tag=text-generation&inference_provider=all&sort=trending)
4. Add desired models to your configuration

## Notes

- Model names must match the exact Hugging Face repository ID
- Some models require accepting license agreements on HF website first
- Large models may not be available on free tier