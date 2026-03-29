---
title: 1,000,000 Tokens
url: https://ampcode.com/news/1m-tokens
source: crawler
fetched_at: 2026-02-06T02:08:33.870677688-03:00
rendered_js: false
word_count: 135
summary: This document announces Amp's expanded 1 million token context window for Claude Sonnet 4 and provides recommendations for optimizing performance and cost through small, task-specific threads.
tags:
    - context-window
    - claude-sonnet-4
    - token-usage
    - pricing
    - performance-optimization
category: guide
---

Amp can now use [1 million tokens of context](https://docs.anthropic.com/en/docs/build-with-claude/context-windows#1m-token-context-window) with Claude Sonnet 4, up from [432,000 tokens](https://ampcode.com/news/432k-tokens) two weeks ago.

You should not use the full context window for most tasks in Amp. Instead, use [small threads](https://ampcode.com/how-i-use-amp#small-threads) that are scoped to a single task. Amp is better, faster, and cheaper when used this way. A notice will appear when you hit 20% of the context window to remind you of this.

Longer threads are more expensive, both because each iteration of the agentic loop sends more and more tokens, and because requests with more than 200k tokens are roughly [twice as expensive](https://docs.anthropic.com/en/docs/about-claude/pricing#long-context-pricing) per token in Anthropic's API pricing.

![Amp thread with 1,000,000 tokens of context](https://static.ampcode.com/news/1m-context.png)

*Note: the screenshot shows 968k tokens because the context window is composed of 968k input tokens and 32k output tokens.*