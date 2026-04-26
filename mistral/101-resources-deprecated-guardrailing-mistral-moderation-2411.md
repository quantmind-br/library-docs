---
title: Mistral Moderation 2411 | Mistral Docs
url: https://docs.mistral.ai/resources/deprecated/guardrailing/mistral_moderation_2411
source: sitemap
fetched_at: 2026-04-26T04:11:33.598083879-03:00
rendered_js: false
word_count: 50
summary: This document provides instructions for migrating from the deprecated mistral-moderation-2411 model to the updated mistral-moderation-2603 model and its associated guardrail configurations.
tags:
    - model-migration
    - api-deprecation
    - moderation-guardrails
    - api-configuration
    - safety-updates
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

> [!danger]
> `mistral-moderation-2411` is deprecated. Migrate to [`mistral-moderation-2603`](https://docs.mistral.ai/studio-api/safety-moderation) and update `moderation_llm_v1` guardrail configs to `moderation_llm_v2`.

`mistral-moderation-2411` is superseded by `mistral-moderation-2603`, which introduces updated policy categories:
- **Dangerous**
- **Criminal**
- **Jailbreaking**

`moderation_llm_v1` is deprecated — use `moderation_llm_v2` instead.

A blocked request returns `403`. #model-migration #api-deprecation #moderation-guardrails