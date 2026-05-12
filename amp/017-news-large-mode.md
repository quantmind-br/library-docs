---
title: Large Mode
url: https://ampcode.com/news/large-mode
source: crawler
fetched_at: 2026-02-06T02:07:53.651763892-03:00
rendered_js: false
word_count: 198
summary: This document introduces Amp's new 'large' agent mode featuring a 1-million-token context window and provides instructions on how to enable and use it effectively.
tags:
    - amp-mode
    - claude-sonnet
    - long-context
    - agent-configuration
    - model-selection
category: guide
---

Amp has a new [agent mode](https://ampcode.com/models): `large`. It uses Claude Sonnet 4.5 with 1M tokens of context.

To use it, run `amp --mode large`, or set `"amp.internal.visibleModes": ["large"]` to be able to select it in the UI.

Use `large` mode sparingly. Using it *never* is totally fine, and we made this news post undiscoverable since we don't want most people stumbling across it and using it. [200k tokens is plenty!](https://ampcode.com/200k-tokens-is-plenty)

Don't use `large` mode for meandering conversations. Models provide better results with less context, so [keep your conversations short and focused](https://ampcode.com/guides/context-management).

Don't use `large` mode to save money. Even though Sonnet is cheaper token-by-token than Opus, Opus [often ends up cheaper overall](https://ampcode.com/news/opus-4.5) because it needs fewer tokens and makes fewer mistakes. Also, LLM inference cost is exponential as the thread gets longer, and on top of that, [Anthropic charges ~2x](https://platform.claude.com/docs/en/about-claude/pricing#long-context-pricing) for long-context tokens.

So, why are we even shipping `large` mode? We've seen it work well for some large-scale refactors, and we want to learn where else long-context might be useful. Also, it lets us artificially constrain `smart` mode to use only the high-quality portion of the context window, even if, say, Opus 4.5 eventually gains 1M-token context.