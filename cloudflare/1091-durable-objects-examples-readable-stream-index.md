---
title: Use ReadableStream with Durable Object and Workers · Cloudflare Durable Objects docs
url: https://developers.cloudflare.com/durable-objects/examples/readable-stream/index.md
source: llms
fetched_at: 2026-01-24T15:13:08.903467304-03:00
rendered_js: false
word_count: 144
summary: Demonstrates how to implement streaming between a Cloudflare Worker and a Durable Object, focusing on how stream cancellation propagates across the connection using AbortSignal.
tags:
    - cloudflare-workers
    - durable-objects
    - readable-stream
    - abort-signal
    - streaming
    - javascript
    - typescript
category: tutorial
---

This example demonstrates:

* A Worker receives a request, and forwards it to a Durable Object `my-id`.
* The Durable Object streams an incrementing number every second, until it receives `AbortSignal`.
* The Worker reads and logs the values from the stream.
* The Worker then cancels the stream after 5 values.

- JavaScript

  ```js
  import { DurableObject } from "cloudflare:workers";


  // Send incremented counter value every second
  async function* dataSource(signal) {
    let counter = 0;
    while (!signal.aborted) {
      yield counter++;
      await new Promise((resolve) => setTimeout(resolve, 1_000));
    }


    console.log("Data source cancelled");
  }


  export class MyDurableObject extends DurableObject {
    async fetch(request) {
      const abortController = new AbortController();


      const stream = new ReadableStream({
        async start(controller) {
          if (request.signal.aborted) {
            controller.close();
            abortController.abort();
            return;
          }


          for await (const value of dataSource(abortController.signal)) {
            controller.enqueue(new TextEncoder().encode(String(value)));
          }
        },
        cancel() {
          console.log("Stream cancelled");
          abortController.abort();
        },
      });


      const headers = new Headers({
        "Content-Type": "application/octet-stream",
      });


      return new Response(stream, { headers });
    }
  }


  export default {
    async fetch(request, env, ctx) {
      const stub = env.MY_DURABLE_OBJECT.getByName("foo");
      const response = await stub.fetch(request, { ...request });
      if (!response.ok || !response.body) {
        return new Response("Invalid response", { status: 500 });
      }


      const reader = response.body
        .pipeThrough(new TextDecoderStream())
        .getReader();


      let data = [];
      let i = 0;
      while (true) {
        // Cancel the stream after 5 messages
        if (i > 5) {
          reader.cancel();
          break;
        }
        const { value, done } = await reader.read();


        if (value) {
          console.log(`Got value ${value}`);
          data = [...data, value];
        }


        if (done) {
          break;
        }
        i++;
      }


      return Response.json(data);
    },
  };
  ```

- TypeScript

  ```ts
  import { DurableObject } from 'cloudflare:workers';


  // Send incremented counter value every second
  async function* dataSource(signal: AbortSignal) {
      let counter = 0;
      while (!signal.aborted) {
          yield counter++;
          await new Promise((resolve) => setTimeout(resolve, 1_000));
      }


      console.log('Data source cancelled');
  }


  export class MyDurableObject extends DurableObject<Env> {
      async fetch(request: Request): Promise<Response> {
          const abortController = new AbortController();


          const stream = new ReadableStream({
              async start(controller) {
                  if (request.signal.aborted) {
                      controller.close();
                      abortController.abort();
                      return;
                  }


                  for await (const value of dataSource(abortController.signal)) {
                      controller.enqueue(new TextEncoder().encode(String(value)));
                  }
              },
              cancel() {
                  console.log('Stream cancelled');
                  abortController.abort();
              },
          });


          const headers = new Headers({
              'Content-Type': 'application/octet-stream',
          });


          return new Response(stream, { headers });
      }


  }


  export default {
      async fetch(request, env, ctx): Promise<Response> {
          const stub = env.MY_DURABLE_OBJECT.getByName("foo");
          const response = await stub.fetch(request, { ...request });
          if (!response.ok || !response.body) {
              return new Response('Invalid response', { status: 500 });
          }


          const reader = response.body.pipeThrough(new TextDecoderStream()).getReader();


          let data = [] as string[];
          let i = 0;
          while (true) {
              // Cancel the stream after 5 messages
              if (i > 5) {
                  reader.cancel();
                  break;
              }
              const { value, done } = await reader.read();


              if (value) {
                  console.log(`Got value ${value}`);
                  data = [...data, value];
              }


              if (done) {
                  break;
              }
              i++;
          }


          return Response.json(data);
      },


  } satisfies ExportedHandler<Env>;
  ```

Note

In a setup where a Durable Object returns a readable stream to a Worker, if the Worker cancels the Durable Object's readable stream, the cancellation propagates to the Durable Object.