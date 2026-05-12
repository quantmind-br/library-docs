---
title: Using Secrets - Fireworks AI Docs
url: https://docs.fireworks.ai/fine-tuning/using-secret-in-evaluator
source: sitemap
fetched_at: 2026-04-27T20:18:34.268615466-03:00
rendered_js: false
word_count: 80
summary: This document provides a comprehensive overview of features within Fireworks AI, including getting started guides for different deployments, details on various model types and inference methods, instructions for fine-tuning, administration tasks, security considerations, and integration options.
tags:
    - getting-started
    - models
    - fine-tuning
    - deployments
    - api
    - security
    - integration
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Using Secrets

Secrets allow you to store sensitive credentials (e.g., API keys) that are injected as environment variables into your [[096-fine-tuning-evaluators|Evaluators]].

## Creating Secrets

1. Navigate to the secrets page on your dashboard.

2. Create a new secret. All secrets created here are injected as environment variables for your Evaluator.

3. Update the Evaluator to reference the new secret.

## Learn More

- [[096-fine-tuning-evaluators|Evaluation]] and [Eval Protocol](https://evalprotocol.io/introduction) for evaluator authoring
- [[045-fine-tuning-rft-cost-estimator|Cost Estimator]]

#on-demand-deployments #gpu-management #deployment-creation #api-usage #fireworks-sdk #scaling-configuration
