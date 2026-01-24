---
title: Use KV API
url: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/kv/index.md
source: llms
fetched_at: 2026-01-24T15:33:32.031517895-03:00
rendered_js: false
word_count: 168
summary: This document demonstrates how to integrate Cloudflare Workers AI with KV storage using embedded function calling to enable persistent data handling within AI-driven applications.
tags:
    - cloudflare-workers-ai
    - kv-storage
    - function-calling
    - embedded-functions
    - serverless
    - data-persistence
category: tutorial
---

---
title: Use KV API · Cloudflare Workers AI docs
description: Learn how to use Cloudflare Workers AI to interact with KV storage,
  enabling persistent data handling with embedded function calling in a few
  lines of code.
lastUpdated: 2025-10-13T13:40:40.000Z
chatbotDeprioritize: false
tags: AI
source_url:
  html: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/kv/
  md: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/kv/index.md
---

Interact with persistent storage to retrieve or store information enables for powerful use cases.

In this example we show how embedded function calling can interact with other resources on the Cloudflare Developer Platform with a few lines of code.

## Pre-Requisites

For this example to work, you need to provision a [KV](https://developers.cloudflare.com/kv/) namespace first. To do so, follow the [KV - Get started ](https://developers.cloudflare.com/kv/get-started/)guide.

Importantly, your Wrangler file must be updated to include the `KV` binding definition to your respective namespace.

## Worker code

```ts
import { runWithTools } from "@cloudflare/ai-utils";


type Env = {
  AI: Ai;
  KV: KVNamespace;
};


export default {
  async fetch(request, env, ctx) {
    // Define function
    const updateKvValue = async ({
      key,
      value,
    }: {
      key: string;
      value: string;
    }) => {
      const response = await env.KV.put(key, value);
      return `Successfully updated key-value pair in database: ${response}`;
    };


    // Run AI inference with function calling
    const response = await runWithTools(
      env.AI,
      "@hf/nousresearch/hermes-2-pro-mistral-7b",
      {
        messages: [
          { role: "system", content: "Put user given values in KV" },
          { role: "user", content: "Set the value of banana to yellow." },
        ],
        tools: [
          {
            name: "KV update",
            description: "Update a key-value pair in the database",
            parameters: {
              type: "object",
              properties: {
                key: {
                  type: "string",
                  description: "The key to update",
                },
                value: {
                  type: "string",
                  description: "The value to update",
                },
              },
              required: ["key", "value"],
            },
            function: updateKvValue,
          },
        ],
      },
    );
    return new Response(JSON.stringify(response));
  },
} satisfies ExportedHandler<Env>;
```

## Verify results

To verify the results, run the following command

```sh
npx wrangler kv key get banana --binding KV --local
```