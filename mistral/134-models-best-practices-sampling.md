---
title: Sampling | Mistral Docs
url: https://docs.mistral.ai/models/best-practices/sampling
source: sitemap
fetched_at: 2026-04-26T04:08:43.075074263-03:00
rendered_js: false
word_count: 204
summary: This document provides an overview of LLM sampling parameters, including temperature, top-p, and penalties, and explains how to configure the N parameter to generate multiple responses.
tags:
    - llm-parameters
    - sampling-settings
    - model-configuration
    - generative-ai
    - n-parameter
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Sampling settings influence LLM output. Parameters: **Temperature**, **N**, **Top P**, **Presence Penalty**, **Frequency Penalty**.

> [!warning]
> `mistral-large-2512` does not support N completions.

## N Parameter

Number of completions per request. Each completion unique, providing variety.

**Benefits:**
- **Multiple responses**: Set `N > 1` for different outputs
- **Cost efficiency**: Input tokens billed once regardless of completions

**Example** — generate 10 responses:
```python
response = client.chat.complete(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Your prompt"}],
    n=10
)
```

## When to Use Multiple Completions

- Evaluate responses across different temperature/top-p settings
- Generate options for human selection
- Parallel exploration of different answer paths #llm-parameters #sampling-settings