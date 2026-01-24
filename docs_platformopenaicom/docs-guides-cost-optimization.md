---
title: Cost optimization
url: https://platform.openai.com/docs/guides/cost-optimization.md
source: llms
fetched_at: 2026-01-24T16:15:32.775020697-03:00
rendered_js: false
word_count: 222
summary: This document outlines various strategies and tools for reducing costs and latency when using OpenAI models, such as optimizing token usage and utilizing the Batch API or flex processing.
tags:
    - cost-optimization
    - latency-optimization
    - batch-api
    - flex-processing
    - token-usage
category: guide
---

Cost optimization
=================

Improve your efficiency and reduce costs.

There are several ways to reduce costs when using OpenAI models. Cost and latency are typically interconnected; reducing tokens and requests generally leads to faster processing. OpenAI's Batch API and flex processing are additional ways to lower costs.

Cost and latency
----------------

To reduce latency and cost, consider the following strategies:

*   **Reduce requests**: Limit the number of necessary requests to complete tasks.
*   **Minimize tokens**: Lower the number of input tokens and optimize for shorter model outputs.
*   **Select a smaller model**: Use models that balance reduced costs and latency with maintained accuracy.

To dive deeper into these, please refer to our guide on [latency optimization](/docs/guides/latency-optimization).

Batch API
---------

Process jobs asynchronously. The Batch API offers a straightforward set of endpoints that allow you to collect a set of requests into a single file, kick off a batch processing job to execute these requests, query for the status of that batch while the underlying requests execute, and eventually retrieve the collected results when the batch is complete.

[Get started with the Batch API →](/docs/guides/batch)

Flex processing
---------------

Get significantly lower costs for Chat Completions or Responses requests in exchange for slower response times and occasional resource unavailability. Ieal for non-production or lower-priority tasks such as model evaluations, data enrichment, or asynchronous workloads.

[Get started with flex processing →](/docs/guides/flex-processing)