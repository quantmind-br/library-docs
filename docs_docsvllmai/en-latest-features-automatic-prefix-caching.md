---
title: Automatic Prefix Caching - vLLM
url: https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/
source: sitemap
fetched_at: 2026-05-07T21:14:04.18600805-03:00
rendered_js: false
word_count: 320
summary: This document explains the automatic prefix caching (APC) feature in vLLM, which improves performance by reusing KV caches across queries that share common prefixes.
tags:
    - vllm
    - kv-cache
    - prefix-caching
    - performance-optimization
    - llm-inference
    - throughput-improvement
category: concept
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/automatic_prefix_caching.md "Edit this page")

## Introduction[¶](#introduction "Permanent link")

Automatic Prefix Caching (APC in short) caches the KV cache of existing queries, so that a new query can directly reuse the KV cache if it shares the same prefix with one of the existing queries, allowing the new query to skip the computation of the shared part.

Note

Technical details on how vLLM implements APC can be found [here](https://docs.vllm.ai/en/latest/design/prefix_caching/).

## Enabling APC in vLLM[¶](#enabling-apc-in-vllm "Permanent link")

Set `enable_prefix_caching=True` in vLLM engine to enable APC. Here is an example:

[examples/features/automatic\_prefix\_caching/automatic\_prefix\_caching\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/features/automatic_prefix_caching/automatic_prefix_caching_offline.py)

## Example workloads[¶](#example-workloads "Permanent link")

We describe two example workloads, where APC can provide huge performance benefit:

- Long document query, where the user repeatedly queries the same long document (e.g. software manual or annual report) with different queries. In this case, instead of processing the long document again and again, APC allows vLLM to process this long document *only once*, and all future requests can avoid recomputing this long document by reusing its KV cache. This allows vLLM to serve future requests with much higher throughput and much lower latency.
- Multi-round conversation, where the user may chat with the application multiple times in the same chatting session. In this case, instead of processing the whole chatting history again and again, APC allows vLLM to reuse the processing results of the chat history across all future rounds of conversation, allowing vLLM to serve future requests with much higher throughput and much lower latency.

## Limits[¶](#limits "Permanent link")

APC in general does not reduce the performance of vLLM. With that being said, APC only reduces the time of processing the queries (the prefilling phase) and does not reduce the time of generating new tokens (the decoding phase). So APC does not bring performance gain when vLLM spends most of the time generating answers to the queries (e.g. when the length of the answer is long), or new queries do not share the same prefix with any of existing queries (so that the computation cannot be reused).