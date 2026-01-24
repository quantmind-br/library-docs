---
title: DeepSeek · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/deepseek/index.md
source: llms
fetched_at: 2026-01-24T14:03:08.879458508-03:00
rendered_js: false
word_count: 133
summary: This document provides instructions for integrating DeepSeek AI models with Cloudflare AI Gateway, detailing the endpoint structure and required credentials.
tags:
    - cloudflare-ai-gateway
    - deepseek
    - api-integration
    - ai-models
    - proxy-configuration
category: configuration
---

[DeepSeek](https://www.deepseek.com/) helps you build quickly with DeepSeek's advanced AI models.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek
```

## Prerequisites

When making requests to DeepSeek, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active DeepSeek AI API token.
* The name of the DeepSeek AI model you want to use.

## URL structure

Your new base URL will use the data above in this structure:

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/`.

You can then append the endpoint you want to hit, for example: `chat/completions`.

So your final URL will come together as:

`https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions`.

## Examples

### cURL

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek/chat/completions \
 --header 'content-type: application/json' \
 --header 'Authorization: Bearer DEEPSEEK_TOKEN' \
 --data '{
    "model": "deepseek-chat",
    "messages": [
        {
            "role": "user",
            "content": "What is Cloudflare?"
        }
    ]
}'
```

### Use DeepSeek with JavaScript

If you are using the OpenAI SDK, you can set your endpoint like this:

```js
import OpenAI from "openai";


const openai = new OpenAI({
  apiKey: env.DEEPSEEK_TOKEN,
  baseURL:
    "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepseek",
});


try {
  const chatCompletion = await openai.chat.completions.create({
    model: "deepseek-chat",
    messages: [{ role: "user", content: "What is Cloudflare?" }],
  });


  const response = chatCompletion.choices[0].message;


  return new Response(JSON.stringify(response));
} catch (e) {
  return new Response(e);
}
```

## OpenAI-Compatible Endpoint

You can also use the [OpenAI-compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) (`/ai-gateway/usage/chat-completion/`) to access DeepSeek models using the OpenAI API schema. To do so, send your requests to:

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions
```

Specify:

```json
{
"model": "deepseek/{model}"
}
```