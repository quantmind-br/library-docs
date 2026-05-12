---
title: 432,000 Tokens
url: https://ampcode.com/news/432k-tokens
source: crawler
fetched_at: 2026-02-06T02:08:38.074402418-03:00
rendered_js: false
word_count: 156
summary: This document announces an update to the Amp coding tool that increases its context window capacity to 432,000 tokens using Claude Sonnet 4.
tags:
    - amp-update
    - context-window
    - claude-sonnet-4
    - token-limit
    - ai-coding-assistant
category: other
---

Amp can now use 432,000 tokens of context with [Claude Sonnet 4](https://docs.anthropic.com/en/docs/build-with-claude/context-windows#1m-token-context-window), more than 2x the previous limit imposed by the model. Your threads can keep going for longer, with more iterations, more context, more replies, and larger files, before you need to compact or start a new thread.

We've rolled it out to all Amp users in the [latest CLI and editor extension](https://ampcode.com/manual#getting-started). We'll ship support for 1 million tokens of context soon.

You should still start new threads for new tasks and use [small threads](https://ampcode.com/how-i-use-amp#small-threads) where possible.

![Amp thread with 432,000 tokens of context](https://static.ampcode.com/news/1m-tokens-2.png)

*Note 1: Why does it say 400k in this screenshot? Because the context window is made up of 400k input and 32k output tokens.*

*Note 2: It remains to be seen what those 400k tokens are made of. Quantity isn't quality, and we're not sure yet whether the model behaves the same at 360k tokens as it does at 60k.*