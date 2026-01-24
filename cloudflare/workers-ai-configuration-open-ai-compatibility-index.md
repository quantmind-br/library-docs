---
title: OpenAI compatible API endpoints · Cloudflare Workers AI docs
url: https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/index.md
source: llms
fetched_at: 2026-01-24T15:32:41.453632105-03:00
rendered_js: false
word_count: 189
summary: This document explains how to use Workers AI with OpenAI-compatible endpoints for text generation and embeddings, allowing users to leverage the OpenAI SDK with Cloudflare's infrastructure.
tags:
    - workers-ai
    - openai-compatibility
    - text-generation
    - embeddings
    - cloudflare-api
category: guide
---

Workers AI supports OpenAI compatible endpoints for [text generation](https://developers.cloudflare.com/workers-ai/models/) (`/v1/chat/completions`) and [text embedding models](https://developers.cloudflare.com/workers-ai/models/) (`/v1/embeddings`). This allows you to use the same code as you would for your OpenAI commands, but swap in Workers AI easily.



## Usage

### Workers AI

Normally, Workers AI requires you to specify the model name in the cURL endpoint or within the `env.AI.run` function.

With OpenAI compatible endpoints, you can leverage the [openai-node sdk](https://github.com/openai/openai-node) to make calls to Workers AI. This allows you to use Workers AI by simply changing the base URL and the model name.

```js
import OpenAI from "openai";


const openai = new OpenAI({
  apiKey: env.CLOUDFLARE_API_KEY,
  baseURL: `https://api.cloudflare.com/client/v4/accounts/${env.CLOUDFLARE_ACCOUNT_ID}/ai/v1`,
});


// Use chat completions
const chatCompletion = await openai.chat.completions.create({
  messages: [{ role: "user", content: "Make some robot noises" }],
  model: "@cf/meta/llama-3.1-8b-instruct",
});


// Use responses
const response = await openai.responses.create({
  model: "@cf/openai/gpt-oss-120b",
  input: "Talk to me about open source",
});


const embeddings = await openai.embeddings.create({
  model: "@cf/baai/bge-large-en-v1.5",
  input: "I love matcha",
});
```

```bash
curl --request POST \
  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions \
  --header "Authorization: Bearer {api_token}" \
  --header "Content-Type: application/json" \
  --data '
    {
      "model": "@cf/meta/llama-3.1-8b-instruct",
      "messages": [
        {
          "role": "user",
          "content": "how to build a wooden spoon in 3 short steps? give as short as answer as possible"
        }
      ]
    }
'
```

### AI Gateway

These endpoints are also compatible with [AI Gateway](https://developers.cloudflare.com/ai-gateway/usage/providers/workersai/#openai-compatible-endpoints).