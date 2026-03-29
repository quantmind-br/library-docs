---
title: Stream OpenAI API Responses
url: https://developers.cloudflare.com/workers/examples/openai-sdk-streaming/index.md
source: llms
fetched_at: 2026-01-24T15:26:13.769712748-03:00
rendered_js: false
word_count: 99
summary: This document demonstrates how to implement streaming responses from the OpenAI API within Cloudflare Workers using the OpenAI SDK and provides code examples for both standard TypeScript and the Hono framework.
tags:
    - cloudflare-workers
    - openai-sdk
    - streaming-api
    - typescript
    - hono
    - serverless
    - ai-integration
category: tutorial
---

---
title: Stream OpenAI API Responses · Cloudflare Workers docs
description: Use the OpenAI v4 SDK to stream responses from OpenAI.
lastUpdated: 2025-08-19T11:42:14.000Z
chatbotDeprioritize: false
tags: AI,JavaScript,TypeScript
source_url:
  html: https://developers.cloudflare.com/workers/examples/openai-sdk-streaming/
  md: https://developers.cloudflare.com/workers/examples/openai-sdk-streaming/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/openai-sdk-streaming)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

In order to run this code, you must install the OpenAI SDK by running `npm i openai`.

Note

For analytics, caching, rate limiting, and more, you can also send requests like this through Cloudflare's [AI Gateway](https://developers.cloudflare.com/ai-gateway/usage/providers/openai/).

* TypeScript

  ```ts
  import OpenAI from "openai";


  export default {
    async fetch(request, env, ctx): Promise<Response> {
      const openai = new OpenAI({
        apiKey: env.OPENAI_API_KEY,
      });


      // Create a TransformStream to handle streaming data
      let { readable, writable } = new TransformStream();
      let writer = writable.getWriter();
      const textEncoder = new TextEncoder();


      ctx.waitUntil(
        (async () => {
          const stream = await openai.chat.completions.create({
            model: "gpt-4o-mini",
            messages: [{ role: "user", content: "Tell me a story" }],
            stream: true,
          });


          // loop over the data as it is streamed and write to the writeable
          for await (const part of stream) {
            writer.write(
              textEncoder.encode(part.choices[0]?.delta?.content || ""),
            );
          }
          writer.close();
        })(),
      );


      // Send the readable back to the browser
      return new Response(readable);
    },
  } satisfies ExportedHandler<Env>;
  ```

* Hono

  ```ts
  import { Hono } from "hono";
  import { streamText } from "hono/streaming";
  import OpenAI from "openai";


  interface Env {
    OPENAI_API_KEY: string;
  }


  const app = new Hono<{ Bindings: Env }>();


  app.get("*", async (c) => {
    const openai = new OpenAI({
      apiKey: c.env.OPENAI_API_KEY,
    });


    const chatStream = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: "Tell me a story" }],
      stream: true,
    });


    return streamText(c, async (stream) => {
      for await (const message of chatStream) {
        await stream.write(message.choices[0].delta.content || "");
      }
      stream.close();
    });
  });


  export default app;
  ```