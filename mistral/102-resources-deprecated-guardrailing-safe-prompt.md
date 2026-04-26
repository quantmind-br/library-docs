---
title: Safe Prompt | Mistral Docs
url: https://docs.mistral.ai/resources/deprecated/guardrailing/safe_prompt
source: sitemap
fetched_at: 2026-04-26T04:11:35.73110527-03:00
rendered_js: false
word_count: 312
summary: This document outlines methods for implementing content moderation and safety guardrails within Mistral models, including the use of custom guardrails and self-reflection prompting.
tags:
    - content-moderation
    - guardrails
    - safety-prompting
    - ai-safety
    - self-reflection
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

> [!warning]
> `safe_prompt` is deprecated. Use [Custom Guardrails](https://docs.mistral.ai/studio-api/safety-moderation#custom-guardrails) instead for more control over moderation categories and thresholds.

## Setup Guardrailing

Activate guardrails via `safe_prompt` boolean flag in API calls. See [[131-studio-api-document-processing-basic-ocr|Chat Completions]] docs first.

Toggling `safe_prompt` prepends your messages with a system prompt that declines inappropriate outputs.

With the recommended system prompt, Mistral models decline all adversarial prompts tested.

### Example Response

Question: "How to kill a linux process" with safety prompts activated → model declines.

## Content Moderation with Self-Reflection

Mistral models can classify user prompts or generated answers as:
- **Illegal activities**: terrorism, child abuse, fraud
- **Hateful/harassing/violent content**: discrimination, self-harm, bullying
- **Unqualified advice**: legal, medical, financial domains

### Self-Reflection Prompt Example

Design a prompt (e.g., for Mistral Large 2) to classify text into categories like physical harm, economic harm, and fraud.

Adjust the self-reflection prompt for your specific use cases. #content-moderation #guardrails #safety-prompting