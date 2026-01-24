---
title: Supported model types · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/features/guardrails/supported-model-types/index.md
source: llms
fetched_at: 2026-01-24T15:07:55.910231861-03:00
rendered_js: false
word_count: 81
summary: This document explains how AI Gateway Guardrails applies safety evaluations to prompts and responses based on the specific type of AI model being used.
tags:
    - ai-gateway
    - guardrails
    - content-moderation
    - text-generation
    - embedding-models
    - safety-checks
category: concept
---

AI Gateway's Guardrails detects the type of AI model being used and applies safety checks accordingly:

* **Text generation models**: Both prompts and responses are evaluated.
* **Embedding models**: Only the prompt is evaluated, as the response consists of numerical embeddings, which are not meaningful for moderation.
* **Unknown models**: If the model type cannot be determined, only the prompt is evaluated, while the response bypass Guardrails.

Note

Guardrails does not yet support streaming responses. Support for streaming is planned for a future update.