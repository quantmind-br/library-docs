---
title: Fallbacks · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/configuration/fallbacks/index.md
source: llms
fetched_at: 2026-01-24T14:01:36.977771496-03:00
rendered_js: false
word_count: 206
summary: This document explains how to configure model and provider fallbacks using the AI Gateway Universal endpoint to ensure request reliability and high availability. It describes the fallback logic triggered by failures or timeouts and explains how to track successful requests using the step response header.
tags:
    - cloudflare-ai-gateway
    - universal-endpoint
    - fallback-providers
    - error-handling
    - request-reliability
    - model-redundancy
category: configuration
---

Specify model or provider fallbacks with your [Universal endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) to handle request failures and ensure reliability.

Cloudflare can trigger your fallback provider in response to [request errors](#request-failures) or [predetermined request timeouts](https://developers.cloudflare.com/ai-gateway/configuration/request-handling#request-timeouts). The [response header `cf-aig-step`](#response-headercf-aig-step) indicates which step successfully processed the request.

## Request failures

By default, Cloudflare triggers your fallback if a model request returns an error.

### Example

In the following example, a request first goes to the [Workers AI](https://developers.cloudflare.com/workers-ai/) Inference API. If the request fails, it falls back to OpenAI. The response header `cf-aig-step` indicates which provider successfully processed the request.

1. Sends a request to Workers AI Inference API.
2. If that request fails, proceeds to OpenAI.

```mermaid
graph TD
    A[AI Gateway] --> B[Request to Workers AI Inference API]
    B -->|Success| C[Return Response]
    B -->|Failure| D[Request to OpenAI API]
    D --> E[Return Response]
```



You can add as many fallbacks as you need, just by adding another object in the array.

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id} \
  --header 'Content-Type: application/json' \
  --data '[
  {
    "provider": "workers-ai",
    "endpoint": "@cf/meta/llama-3.1-8b-instruct",
    "headers": {
      "Authorization": "Bearer {cloudflare_token}",
      "Content-Type": "application/json"
    },
    "query": {
      "messages": [
        {
          "role": "system",
          "content": "You are a friendly assistant"
        },
        {
          "role": "user",
          "content": "What is Cloudflare?"
        }
      ]
    }
  },
  {
    "provider": "openai",
    "endpoint": "chat/completions",
    "headers": {
      "Authorization": "Bearer {open_ai_token}",
      "Content-Type": "application/json"
    },
    "query": {
      "model": "gpt-4o-mini",
      "stream": true,
      "messages": [
        {
          "role": "user",
          "content": "What is Cloudflare?"
        }
      ]
    }
  }
]'
```

## Response header(cf-aig-step)

When using the [Universal endpoint](https://developers.cloudflare.com/ai-gateway/usage/universal/) with fallbacks, the response header `cf-aig-step` indicates which model successfully processed the request by returning the step number. This header provides visibility into whether a fallback was triggered and which model ultimately processed the response.

* `cf-aig-step:0` – The first (primary) model was used successfully.
* `cf-aig-step:1` – The request fell back to the second model.
* `cf-aig-step:2` – The request fell back to the third model.
* Subsequent steps – Each fallback increments the step number by 1.