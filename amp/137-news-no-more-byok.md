---
title: No More BYOK
url: https://ampcode.com/news/no-more-byok
source: crawler
fetched_at: 2026-02-06T02:08:52.000629716-03:00
rendered_js: false
word_count: 267
summary: This document explains the decision to remove Isolated Mode in Amp, detailing the technical challenges regarding API rate limits, connectivity, and model parity that led to the change.
tags:
    - amp
    - isolated-mode
    - product-updates
    - llm-inference
    - api-integration
    - anthropic-api
    - gemini-api
category: other
---

We removed Isolated Mode, which let you use Amp with your own API keys for LLM inference, because it's not possible for it to meet our quality bar. The intent was to make it easier to use Amp in locked-down environments, but we hit many issues that made the experience bad and slowed us down:

1. Anthropic rate limit issues: Individuals can't easily get Anthropic API keys with high enough [rate limits](https://docs.anthropic.com/en/api/rate-limits#rate-limits) to actually use Amp. (Anthropic is understandably strict here unless you are an enterprise customer of theirs.)
2. LLM proxy and connectivity issues: Many people tried to use Isolated Mode with custom LLM proxies that weren't fully API-compatible with Anthropic's API, which led to hard-to-debug issues.
3. Gemini API parity issues: We found that Gemini 2.5 Pro only works well via Google Cloud Vertex AI (a more enterprise-y offering) rather than Google AI Studio, which is how most people would generate API keys, because of differences in how they handle thinking.

Even though we *could* work around these specific issues, more will arise in the future because tool-calling agents need to [integrate more deeply into model capabilities](https://ampcode.com/fif#model-selector) and LLM APIs are getting more complex and differentiated.

We believe the best product is built by iterating fast at the model↔product frontier, and most devs and companies want the best coding agent *more* than they want a worse coding agent that satisfies other constraints.

*If you were using Isolated Mode*: When you update Amp in VS Code, you'll see a message informing you of this change and requiring you to disable Isolated Mode to continue. Your threads are preserved locally.