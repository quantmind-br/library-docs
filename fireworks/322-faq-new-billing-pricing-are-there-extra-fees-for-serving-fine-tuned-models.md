---
title: Are there extra fees for serving fine-tuned models?
url: https://docs.fireworks.ai/faq-new/billing-pricing/are-there-extra-fees-for-serving-fine-tuned-models
source: sitemap
fetched_at: 2026-04-27T20:13:10.858089009-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
  - billing
  - fine-tuning
  - lora
  - deployment
word_count: 78
---
# Fine-tuned model serving fees

Fine-tuned (LoRA) models require a dedicated deployment to serve.

## What you pay for

- **Deployment costs**: per-GPU-second basis for hosting the model
- **Fine-tuning process**: if applicable

## Deployment options

- **Live-merge deployment**: Deploy your LoRA model with weights merged into the base model for optimal performance
- **Multi-LoRA deployment**: Deploy up to 100 LoRA models as addons on a single base model deployment

> [!tip]
> See [[038-fine-tuning-deploying-loras]] for deployment details.