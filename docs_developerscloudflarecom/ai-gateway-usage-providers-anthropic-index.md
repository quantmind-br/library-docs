---
title: Anthropic · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/anthropic/index.md
source: llms
fetched_at: 2026-01-24T14:03:00.374300618-03:00
rendered_js: false
word_count: 148
summary: This document explains how to route Anthropic API requests through Cloudflare AI Gateway using cURL, the Anthropic SDK, or an OpenAI-compatible endpoint.
tags:
    - cloudflare-ai-gateway
    - anthropic
    - api-integration
    - claude
    - sdk
    - authentication
category: api
---

[Anthropic](https://www.anthropic.com/) helps build reliable, interpretable, and steerable AI systems.

## Endpoint

**Base URL**

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic
```

## Examples

### cURL

With API Key in Request

* With Authenticated Gateway

  ```bash
  curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic/v1/messages \
   --header 'x-api-key: {anthropic_api_key}' \
   --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
   --header 'anthropic-version: 2023-06-01' \
   --header 'Content-Type: application/json' \
   --data  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "What is Cloudflare?"}
      ]
    }'
  ```

* Unauthenticated Gateway

  ```bash
  curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic/v1/messages \
   --header 'x-api-key: {anthropic_api_key}' \
   --header 'anthropic-version: 2023-06-01' \
   --header 'Content-Type: application/json' \
   --data  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "What is Cloudflare?"}
      ]
    }'
  ```

With Stored Keys (BYOK) / Unified Billing

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic/v1/messages \
 --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
 --header 'anthropic-version: 2023-06-01' \
 --header 'Content-Type: application/json' \
 --data  '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "What is Cloudflare?"}
    ]
  }'
```

### Anthropic SDK

With Key in Request

* With Authenticated Gateway

  ```js
  import Anthropic from "@anthropic-ai/sdk";


  const baseURL = `https://gateway.ai.cloudflare.com/v1/{accountId}/{gatewayId}/anthropic`;


  const anthropic = new Anthropic({
    apiKey: "{ANTHROPIC_API_KEY}",
    baseURL,
    defaultHeaders: {
      Authorization: `Bearer {cf_api_token}`,
    },
  });


  const message = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    messages: [{ role: "user", content: "What is Cloudflare?" }],
    max_tokens: 1024,
  });
  ```

* Unauthenticated Gateway

  ```js
  import Anthropic from "@anthropic-ai/sdk";


  const baseURL = `https://gateway.ai.cloudflare.com/v1/{accountId}/{gatewayId}/anthropic`;


  const anthropic = new Anthropic({
    apiKey: "{ANTHROPIC_API_KEY}",
    baseURL,
  });


  const message = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    messages: [{ role: "user", content: "What is Cloudflare?" }],
    max_tokens: 1024,
  });
  ```

With Stored Keys (BYOK) / Unified Billing

```js
import Anthropic from "@anthropic-ai/sdk";


const baseURL = `https://gateway.ai.cloudflare.com/v1/{accountId}/{gatewayId}/anthropic`;


const anthropic = new Anthropic({
  baseURL,
  defaultHeaders: {
    Authorization: `Bearer {cf_api_token}`,
  },
});


const message = await anthropic.messages.create({
  model: "claude-sonnet-4-5",
  messages: [{ role: "user", content: "What is Cloudflare?" }],
  max_tokens: 1024,
});
```

## OpenAI-Compatible Endpoint

You can also use the [OpenAI-compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) (`/ai-gateway/usage/chat-completion/`) to access Anthropic models using the OpenAI API schema. To do so, send your requests to:

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions
```

Specify:

```json
{
  "model": "anthropic/{model}"
}
```