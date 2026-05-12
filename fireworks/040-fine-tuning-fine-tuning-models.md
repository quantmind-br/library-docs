---
title: Supervised Fine Tuning - Text - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/fine-tuning-models
source: sitemap
fetched_at: 2026-04-27T20:12:45.995865781-03:00
rendered_js: false
word_count: 102
summary: This guide explains the process of using supervised fine-tuning (SFT) to tune a model and subsequently deploying that fine-tuned model via a dedicated deployment endpoint.
tags:
    - supervised-fine-tuning
    - model-deployment
    - sft-workflow
    - dedicated-serving
    - hyperparameter-tuning
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Use supervised fine-tuning (SFT) to tune a model, then deploy it to a dedicated on-demand deployment (the only supported method for serving fine-tuned models).

## Fine-tuning a Model

> [!example]
> See the [Complete Python SDK workflow example](https://github.com/fw-ai-external/python-sdk/blob/main/examples/sftj_workflow.py) for a code-only implementation.

## Deploying a Fine-tuned Model

```bash
firectl deployment create <FINE_TUNED_MODEL_ID>
```

This creates a dedicated deployment with performance matching the base model.

## Additional SFT Job Settings

All settings below are optional and have reasonable defaults. For quality-affecting parameters like `epochs` and `learning_rate`, use defaults unless results are unsatisfactory.

## See Also

- [[094-tools-sdks-python-sdk|Python SDK]] references
- [[001-api-reference-introduction|Restful API]] references
- [[092-tools-sdks-firectl-firectl|firectl]] references

#supervised-fine-tuning #model-deployment #sft-workflow
