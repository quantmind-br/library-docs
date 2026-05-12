---
title: Supervised Fine Tuning - Vision - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/fine-tuning-vlm
source: sitemap
fetched_at: 2026-04-27T20:15:55.36351266-03:00
rendered_js: false
word_count: 119
summary: This document explains the process of fine-tuning Vision-language models (VLMs) to adapt pre-trained text and image understanding models for specific applications, and provides links and tutorials for advanced configuration and hands-on walkthroughs.
tags:
    - vlm-fine-tuning
    - vision-model
    - lora
    - model-adaptation
    - dataset-preparation
    - api-cookbook
category: tutorial
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Vision-language model (VLM) fine-tuning adapts pre-trained text+image models to specific use cases like document analysis, visual question answering, and image captioning. See the [Model Library for vision models](https://app.fireworks.ai/models?filter=vision&tunable=true) to find all tunable vision models.

## Fine-tuning a VLM using LoRA

## Advanced Configuration

For additional parameters (custom learning rates, batch sizes, optimization options), see [[040-fine-tuning-fine-tuning-models#additional-sft-job-settings|Additional SFT job settings]].

## Interactive Tutorials

Two cookbooks walk through the complete VLM fine-tuning process:

- **Cookbook 1** (link in source) — dataset preparation, job launching, monitoring, testing
- **Cookbook 2** (link in source) — best practices, serverless VLMs, evals showing performance gains

Both cover: environment setup, vision dataset formatting, job lifecycle, inference, and eval.

## Testing Your Fine-tuned VLM

```python
import openai

client = openai.OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<FIREWORKS_API_KEY>",
)
response = client.chat.completions.create(
    model="accounts/your-account/models/my-custom-vlm",
    messages=[{
        "role": "user",
        "content": [{
            "type": "image_url",
            "image_url": {"url": "https://raw.githubusercontent.com/fw-ai/cookbook/refs/heads/main/learn/vlm-finetuning/images/icecream.jpeg"},
        }, {
            "type": "text",
            "text": "What's in this image?",
        }],
    }]
)
print(response.choices[0].message.content)
```

#vlm-fine-tuning #vision-model #lora #dataset-preparation
