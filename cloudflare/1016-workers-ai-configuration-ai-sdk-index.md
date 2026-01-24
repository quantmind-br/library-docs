---
title: Vercel AI SDK · Cloudflare Workers AI docs
url: https://developers.cloudflare.com/workers-ai/configuration/ai-sdk/index.md
source: llms
fetched_at: 2026-01-24T15:32:36.477118694-03:00
rendered_js: false
word_count: 92
summary: This document explains how to integrate Cloudflare Workers AI with the Vercel AI SDK to build AI-powered applications in JavaScript or TypeScript. It provides instructions for setup, model configuration, and implementing features like text generation, streaming, and structured data output.
tags:
    - cloudflare-workers
    - workers-ai
    - vercel-ai-sdk
    - generative-ai
    - javascript
    - typescript
    - llm-integration
category: guide
---

Workers AI can be used with the [Vercel AI SDK](https://sdk.vercel.ai/) for JavaScript and TypeScript codebases.

## Setup

Install the [`workers-ai-provider` provider](https://sdk.vercel.ai/providers/community-providers/cloudflare-workers-ai):

* npm

  ```sh
  npm i workers-ai-provider
  ```

* yarn

  ```sh
  yarn add workers-ai-provider
  ```

* pnpm

  ```sh
  pnpm add workers-ai-provider
  ```

Then, add an AI binding in your Workers project Wrangler file:

```toml
[ai]
binding = "AI"
```

## Models

The AI SDK can be configured to work with [any AI model](https://developers.cloudflare.com/workers-ai/models/).

```js
import { createWorkersAI } from "workers-ai-provider";


const workersai = createWorkersAI({ binding: env.AI });


// Choose any model: https://developers.cloudflare.com/workers-ai/models/
const model = workersai("@cf/meta/llama-3.1-8b-instruct", {});
```

## Generate Text

Once you have selected your model, you can generate text from a given prompt.

```js
import { createWorkersAI } from 'workers-ai-provider';
import { generateText } from 'ai';


type Env = {
  AI: Ai;
};


export default {
  async fetch(_: Request, env: Env) {
    const workersai = createWorkersAI({ binding: env.AI });
    const result = await generateText({
      model: workersai('@cf/meta/llama-2-7b-chat-int8'),
      prompt: 'Write a 50-word essay about hello world.',
    });


    return new Response(result.text);
  },
};
```

## Stream Text

For longer responses, consider streaming responses to provide as the generation completes.

```js
import { createWorkersAI } from 'workers-ai-provider';
import { streamText } from 'ai';


type Env = {
  AI: Ai;
};


export default {
  async fetch(_: Request, env: Env) {
    const workersai = createWorkersAI({ binding: env.AI });
    const result = streamText({
      model: workersai('@cf/meta/llama-2-7b-chat-int8'),
      prompt: 'Write a 50-word essay about hello world.',
    });


    return result.toTextStreamResponse({
      headers: {
        // add these headers to ensure that the
        // response is chunked and streamed
        'Content-Type': 'text/x-unknown',
        'content-encoding': 'identity',
        'transfer-encoding': 'chunked',
      },
    });
  },
};
```

## Generate Structured Objects

You can provide a Zod schema to generate a structured JSON response.

```js
import { createWorkersAI } from 'workers-ai-provider';
import { generateObject } from 'ai';
import { z } from 'zod';


type Env = {
  AI: Ai;
};


export default {
  async fetch(_: Request, env: Env) {
    const workersai = createWorkersAI({ binding: env.AI });
    const result = await generateObject({
      model: workersai('@cf/meta/llama-3.1-8b-instruct'),
      prompt: 'Generate a Lasagna recipe',
      schema: z.object({
        recipe: z.object({
          ingredients: z.array(z.string()),
          description: z.string(),
        }),
      }),
    });


    return Response.json(result.object);
  },
};
```