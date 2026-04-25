---
title: Token Caching and Cost Optimization
url: https://qwenlm.github.io/qwen-code-docs/en/users/features/token-caching
source: github_pages
fetched_at: 2026-04-09T09:04:04.332405111-03:00
rendered_js: true
word_count: 186
summary: This document explains that Qwen Code automatically optimizes API costs through token caching when using API key authentication by storing frequently used content, which leads to cost reduction and faster responses without requiring manual configuration.
tags:
    - api-cost-optimization
    - token-caching
    - api-key-authentication
    - qwen-code
    - usage-stats
category: guide
---

Qwen Code automatically optimizes API costs through token caching when using API key authentication. This feature stores frequently used content like system instructions and conversation history to reduce the number of tokens processed in subsequent requests.

## How It Benefits You[](#how-it-benefits-you)

- **Cost reduction**: Less tokens mean lower API costs
- **Faster responses**: Cached content is retrieved more quickly
- **Automatic optimization**: No configuration needed - it works behind the scenes

## Token caching is available for[](#token-caching-is-available-for)

- API key users (Qwen API key, OpenAI-compatible providers)

## Monitoring Your Savings[](#monitoring-your-savings)

Use the `/stats` command to see your cached token savings:

- When active, the stats display shows how many tokens were served from cache
- You’ll see both the absolute number and percentage of cached tokens
- Example: “10,500 (90.4%) of input tokens were served from the cache, reducing costs.”

This information is only displayed when cached tokens are being used, which occurs with API key authentication but not with OAuth authentication.

## Example Stats Display[](#example-stats-display)

![Qwen Code Stats Display](https://img.alicdn.com/imgextra/i3/O1CN01F1yzRs1juyZu63jdS_!!6000000004609-2-tps-1038-738.png)

The above image shows an example of the `/stats` command output, highlighting the cached token savings information.

Last updated on March 31, 2026

[LSP (Language Server Protocol)](https://qwenlm.github.io/qwen-code-docs/en/users/features/lsp/ "LSP (Language Server Protocol)")[Sandboxing](https://qwenlm.github.io/qwen-code-docs/en/users/features/sandbox/ "Sandboxing")