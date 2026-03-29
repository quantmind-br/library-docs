---
title: Using a dynamic route · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/usage/index.md
source: llms
fetched_at: 2026-01-24T15:07:54.048388316-03:00
rendered_js: false
word_count: 171
summary: This document provides instructions and code examples for using dynamic routes in Cloudflare AI Gateway via the OpenAI SDK, Fetch API, and Cloudflare Workers.
tags:
    - cloudflare-ai-gateway
    - dynamic-routes
    - openai-sdk
    - cloudflare-workers
    - api-integration
    - authentication
category: guide
---

Warning

Ensure your gateway has [authentication](https://developers.cloudflare.com/ai-gateway/configuration/authentication/) turned on and you have your upstream providers keys stored with [BYOK](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).

## Examples

### OpenAI SDK

```js
import OpenAI from "openai";


const cloudflareToken = "CF_AIG_TOKEN";
const accountId = "{account_id}";
const gatewayId = "{gateway_id}";
const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/compat`;


const openai = new OpenAI({
  apiKey: cloudflareToken,
  baseURL,
});


try {
  const model = "dynamic/<your-dynamic-route-name>";
  const messages = [{ role: "user", content: "What is a neuron?" }];
  const chatCompletion = await openai.chat.completions.create({
    model,
    messages,
  });
  const response = chatCompletion.choices[0].message;
  console.log(response);
} catch (e) {
  console.error(e);
}
```

### Fetch

```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
  --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "dynamic/<your-dynamic-route-name>",
    "messages": [
      {
        "role": "user",
        "content": "What is Cloudflare?"
      }
    ]
  }'
```

### Workers

```ts
export interface Env {
  AI: Ai;
}


export default {
  async fetch(request: Request, env: Env) {
    const response = await env.AI.gateway("default").run({
      provider: "compat",
      endpoint: "chat/completion",
      headers: {},
      query: {
        model: "dynamic/<your-dynamic-route-name>",
        messages: [
          {
            role: "user",
            content: "What is Cloudflare?",
          },
        ],
      },
    });
    return Response(response);
  },
};
```

## Response Metadata

The response from a dynamic route is the same as the response from a model. There is additional metadata used to notify the model and provider used, you can check the following headers

* `cf-aig-model` - The model used
* `cf-aig-provider` - The slug of provider used