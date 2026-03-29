---
title: Amp Tab 30% Faster
url: https://ampcode.com/news/amp-tab-30-percent-faster
source: crawler
fetched_at: 2026-02-06T02:08:41.975748228-03:00
rendered_js: false
word_count: 97
summary: This document describes infrastructure optimizations and performance improvements to the Amp Tab in-editor completion engine, highlighting techniques like speculative decoding and TensorRT-LLM.
tags:
    - amp-tab
    - performance-optimization
    - inference-engine
    - speculative-decoding
    - latency-reduction
    - tensorrt-llm
category: other
---

Response times of [Amp Tab](https://ampcode.com/manual#amp-tab), our in-editor completion engine, are now 30% faster, with up to 50% improvements during peak usage.

We worked together with [Baseten](https://www.baseten.co/) to optimize our custom deployment. The new infrastructure delivers roughly 2x performance improvements by switching to TensorRT-LLM as the inference engine and implementing KV caching with speculative decoding.

This new infrastructure also includes a modified version of lookahead decoding that uses an improved n-gram candidate selection algorithm and variable-length speculations, which reduces both draft tokens and compute per iteration compared to standard implementations.

![Chart showing Amp Tab latency improvements over time](https://static.ampcode.com/news/next-cursor-latency-trend-dark.png)