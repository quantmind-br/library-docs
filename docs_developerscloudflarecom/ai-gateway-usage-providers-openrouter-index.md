---
title: OpenRouter · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter/index.md
source: llms
fetched_at: 2026-01-24T14:03:28.686235717-03:00
rendered_js: false
word_count: 103
summary: This document explains how to route OpenRouter API requests through Cloudflare AI Gateway by modifying the endpoint URL and provides integration examples using cURL and the OpenAI SDK.
tags:
    - cloudflare-ai-gateway
    - openrouter
    - llm-integration
    - api-configuration
    - openai-sdk
    - request-routing
category: configuration
---

[OpenRouter](https://openrouter.ai/) is a platform that provides a unified interface for accessing and using large language models (LLMs).

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter
```

## URL structure

When making requests to [OpenRouter](https://openrouter.ai/), replace `https://openrouter.ai/api/v1/chat/completions` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter/chat/completions`.

## Prerequisites

When making requests to OpenRouter, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active OpenRouter API token or a token from the original model provider.
* The name of the OpenRouter model you want to use.

## Examples

### cURL

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openrouter/v1/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer OPENROUTER_TOKEN' \
 --data '{
    "model": "openai/gpt-5-mini",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

### Use OpenAI SDK with JavaScript

If you are using the OpenAI SDK with JavaScript, you can set your endpoint like this:

```js
import OpenAI from "openai";


const openai = new OpenAI({
  apiKey: env.OPENROUTER_TOKEN,
  baseURL:
    "https://gateway.ai.cloudflare.com/v1/ACCOUNT_TAG/GATEWAY/openrouter",
});


try {
  const chatCompletion = await openai.chat.completions.create({
    model: "openai/gpt-5-mini",
    messages: [{ role: "user", content: "What is Cloudflare?" }],
  });


  const response = chatCompletion.choices[0].message;


  return new Response(JSON.stringify(response));
} catch (e) {
  return new Response(e);
}
```