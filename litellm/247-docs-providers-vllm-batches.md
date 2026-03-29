---
title: vLLM - Batch + Files API | liteLLM
url: https://docs.litellm.ai/docs/providers/vllm_batches
source: sitemap
fetched_at: 2026-01-21T19:50:53.401437053-03:00
rendered_js: false
word_count: 52
summary: This document explains how LiteLLM integrates with vLLM's Batch and Files API to support asynchronous large-scale request processing and multi-tenant routing.
tags:
    - litellm
    - vllm
    - batch-api
    - asynchronous-processing
    - proxy-routing
    - multi-tenancy
category: guide
---

LiteLLM supports vLLM's Batch and Files API for processing large volumes of requests asynchronously.

Define your vLLM model in `config.yaml`. LiteLLM uses the model name to route batch requests to the correct vLLM server.

```
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "my-vllm-model", "messages": [{"role": "user", "content": "Hello!"}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "my-vllm-model", "messages": [{"role": "user", "content": "How are you?"}]}}
```

This enables multi-tenant batch processing where different teams can use different vLLM deployments through the same LiteLLM proxy.