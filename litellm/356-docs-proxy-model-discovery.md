---
title: Model Discovery | liteLLM
url: https://docs.litellm.ai/docs/proxy/model_discovery
source: sitemap
fetched_at: 2026-01-21T19:53:01.403491619-03:00
rendered_js: false
word_count: 26
summary: This document explains how to configure and use a proxy to retrieve an accurate list of available models via the /v1/models endpoint.
tags:
    - proxy-configuration
    - api-endpoint
    - model-listing
    - v1-models
    - wildcard-models
category: guide
---

Use this to give users an accurate list of models available behind provider endpoint, when calling `/v1/models` for wildcard models.

**1. Setup config.yaml**

**2. Start proxy**

**3. Call `/v1/models`**

```
{
"data":[
{
"id":"xai/grok-2-1212",
"object":"model",
"created":1677610602,
"owned_by":"openai"
},
{
"id":"xai/grok-2-vision-1212",
"object":"model",
"created":1677610602,
"owned_by":"openai"
},
{
"id":"xai/grok-3-beta",
"object":"model",
"created":1677610602,
"owned_by":"openai"
},
{
"id":"xai/grok-3-fast-beta",
"object":"model",
"created":1677610602,
"owned_by":"openai"
},
{
"id":"xai/grok-3-mini-beta",
"object":"model",
"created":1677610602,
"owned_by":"openai"
},
{
"id":"xai/grok-3-mini-fast-beta",
"object":"model",
"created":1677610602,
"owned_by":"openai"
},
{
"id":"xai/grok-beta",
"object":"model",
"created":1677610602,
"owned_by":"openai"
},
{
"id":"xai/grok-vision-beta",
"object":"model",
"created":1677610602,
"owned_by":"openai"
},
{
"id":"xai/grok-2-image-1212",
"object":"model",
"created":1677610602,
"owned_by":"openai"
}
],
"object":"list"
}
```