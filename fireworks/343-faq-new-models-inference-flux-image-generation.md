---
title: FLUX image generation - Fireworks AI Docs
url: https://docs.fireworks.ai/faq-new/models-inference/flux-image-generation
source: sitemap
fetched_at: 2026-04-27T20:12:59.357686336-03:00
rendered_js: false
word_count: 83
summary: FLUX serverless limitations and supported features including multi-image generation, image-to-image, and LoRA support.
tags:
    - flux-api
    - image-generation
    - lora-models
    - api-limitations
    - feature-support
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# FLUX image generation

## Can I generate multiple images in a single API call?

No, FLUX serverless supports only one image per API call. For multiple images, send separate parallel requests—they are automatically load-balanced across replicas.

## Does FLUX support image-to-image generation?

No, image-to-image generation is not currently supported. This feature is under evaluation.

## Can I create custom LoRA models with FLUX?

- **Inference on FLUX-LoRA adapters**: Supported
- **Managed training with FLUX**: Not currently supported (under development)

#flux-api #image-generation #lora-models
