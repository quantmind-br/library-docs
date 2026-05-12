---
title: Speed
url: https://developers.openai.com/codex/speed.md
source: llms
fetched_at: 2026-04-30T10:16:08.586720627-03:00
rendered_js: false
word_count: 116
summary: This document describes how to configure and utilize performance-enhancing modes in Codex, including Fast mode for supported models and the dedicated Codex-Spark model for real-time iteration.
tags:
    - codex-performance
    - fast-mode
    - codex-spark
    - model-optimization
    - credit-usage
    - cli-configuration
category: configuration
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Speed

## Fast mode

Increases supported model speed by 1.5x at higher credit consumption.

| Model | Credit multiplier |
|-------|-------------------|
| GPT-5.5 | 2.5x Standard |
| GPT-5.4 | 2x Standard |

Control via CLI: `/fast on`, `/fast off`, `/fast status`. Persist default with `service_tier = "fast"` plus `[features].fast_mode = true` in `config.toml`.

Available in Codex IDE extension, CLI, and app (ChatGPT sign-in). Not available with API key — uses standard API pricing instead.

## Codex-Spark

GPT-5.3-Codex-Spark is a fast, less-capable model optimized for near-instant, real-time coding iteration. It has its own usage limits, unlike fast mode which speeds up existing models.

> [!info]
> Research preview, ChatGPT Pro subscribers only.

#performance #fast-mode #codex-spark