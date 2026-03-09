---
title: Hugging Face
url: https://docs.factory.ai/cli/byok/huggingface.md
source: llms
fetched_at: 2026-03-03T01:12:40.647458-03:00
rendered_js: false
word_count: 155
summary: This document explains how to configure and integrate Hugging Face Inference Providers to access hosted language models within the platform.
tags:
    - hugging-face
    - inference-providers
    - custom-models
    - configuration-settings
    - llm-integration
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hugging Face

> Connect to models hosted on Hugging Face's Inference Providers

Connect to thousands of models hosted on Hugging Face's Inference Providers. Learn more in the [Inference Providers documentation](https://huggingface.co/docs/inference-providers/en/index).

<Note>
  **Model Performance**: Models below 30 billion parameters have shown significantly lower performance on agentic coding tasks. While HuggingFace hosts many smaller models that can be useful for experimentation, they are generally not recommended for production coding work. Consider using models with 30B+ parameters for complex software engineering tasks.
</Note>

## Configuration

Add to `~/.factory/settings.json`:

```json  theme={null}
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
3. Browse models at [huggingface.co/models](https://huggingface.co/models?pipeline_tag=text-generation\&inference_provider=all\&sort=trending)
4. Add desired models to your configuration

## Notes

* Model names must match the exact Hugging Face repository ID
* Some models require accepting license agreements on HF website first
* Large models may not be available on free tier