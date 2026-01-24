---
title: Perplexity · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/perplexity/index.md
source: llms
fetched_at: 2026-01-24T14:03:30.603578038-03:00
rendered_js: false
word_count: 170
summary: This document explains how to configure and use Perplexity AI via the Cloudflare AI Gateway, providing endpoint details and authentication prerequisites.
tags:
    - cloudflare-ai-gateway
    - perplexity-ai
    - api-integration
    - openai-compatibility
    - llm-proxy
category: api
---

[Perplexity](https://www.perplexity.ai/) is an AI powered answer engine.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/perplexity-ai
```

## Prerequisites

When making requests to Perplexity, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active Perplexity API token.
* The name of the Perplexity model you want to use.

## Examples

### cURL

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/perplexity-ai/chat/completions \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'Authorization: Bearer {perplexity_token}' \
     --data '{
      "model": "mistral-7b-instruct",
      "messages": [
        {
          "role": "user",
          "content": "What is Cloudflare?"
        }
      ]
    }'
```

### Use Perplexity through OpenAI SDK with JavaScript

Perplexity does not have their own SDK, but they have compatibility with the OpenAI SDK. You can use the OpenAI SDK to make a Perplexity call through AI Gateway as follows:

```js
import OpenAI from "openai";


const apiKey = env.PERPLEXITY_API_KEY;
const accountId = "{account_id}";
const gatewayId = "{gateway_id}";
const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/perplexity-ai`;


const perplexity = new OpenAI({
  apiKey,
  baseURL,
});


const model = "mistral-7b-instruct";
const messages = [{ role: "user", content: "What is Cloudflare?" }];
const maxTokens = 20;


const chatCompletion = await perplexity.chat.completions.create({
  model,
  messages,
  max_tokens: maxTokens,
});
```

## OpenAI-Compatible Endpoint

You can also use the [OpenAI-compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) (`/ai-gateway/usage/chat-completion/`) to access Perplexity models using the OpenAI API schema. To do so, send your requests to:

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions
```

Specify:

```json
{
"model": "perplexity/{model}"
}
```