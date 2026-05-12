---
title: Speculative Decoding - Fireworks AI Docs
url: https://docs.fireworks.ai/deployments/speculative-decoding
source: sitemap
fetched_at: 2026-04-27T20:18:50.46477035-03:00
rendered_js: false
word_count: 117
summary: This document explains how to speed up text generation by configuring either a smaller draft model or using N-gram based speculation, detailing the necessary command-line flags and recommending specific model pairings.
tags:
    - text-generation
    - draft-model
    - ngram-speculation
    - configuration
    - speed-up
    - llm
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Speculative decoding speeds up text generation using a smaller "draft" model or N-gram based speculation.

## Configuration Flags

| Flag | Type | Description |
|------|------|-------------|
| `--draft-model` | string | Draft model name (Fireworks or custom). See recommendations below. |
| `--draft-token-count` | int32 | Tokens to generate per step. Required when using draft model or n-gram. Typically set to 4. |
| `--ngram-speculation-length` | int32 | Alternative to draft model: uses N-gram speculation from previous input. |

## Recommended Draft Models

| Draft Model | Use With |
|-------------|----------|
| `accounts/fireworks/models/llama-v3p2-1b-instruct` | All Llama models > 3B |
| `accounts/fireworks/models/qwen2p5-0p5b-instruct` | All Qwen models > 3B |

## Examples

### Draft Model

```bash
firectl deployment create accounts/fireworks/models/llama-v3p3-70b-instruct \
  --draft-model="accounts/fireworks/models/llama-v3p2-1b-instruct" \
  --draft-token-count=4
```

### N-gram Speculation

```bash
firectl deployment create accounts/fireworks/models/llama-v3p3-70b-instruct \
  --ngram-speculation-length=3 \
  --draft-token-count=4
```
