---
title: Stream large JSON
url: https://developers.cloudflare.com/workers/examples/streaming-json/index.md
source: llms
fetched_at: 2026-01-24T15:26:26.576455843-03:00
rendered_js: false
word_count: 192
summary: This document explains how to use the Streams API and third-party parsers to process and transform large JSON payloads in Cloudflare Workers without exceeding memory limits.
tags:
    - cloudflare-workers
    - streams-api
    - json-parsing
    - javascript
    - typescript
    - performance-optimization
category: tutorial
---

---
title: Stream large JSON · Cloudflare Workers docs
description: Parse and transform large JSON request and response bodies using streaming.
lastUpdated: 2025-12-16T04:37:37.000Z
chatbotDeprioritize: false
tags: Middleware,JSON,JavaScript,TypeScript
source_url:
  html: https://developers.cloudflare.com/workers/examples/streaming-json/
  md: https://developers.cloudflare.com/workers/examples/streaming-json/index.md
---

Use the [Streams API](https://developers.cloudflare.com/workers/runtime-apis/streams/) to process JSON payloads that would exceed a Worker's 128 MB memory limit if fully buffered. Streaming allows you to parse and transform JSON data incrementally as it arrives. This is faster than buffering the entire payload into memory, as your Worker can start processing data incrementally, and allows your Worker to handle multi-gigabyte payloads or files within its memory limits.

The [`@streamparser/json-whatwg`](https://www.npmjs.com/package/@streamparser/json-whatwg) library provides a streaming JSON parser compatible with the Web Streams API.

Install the dependency:

```sh
npm install @streamparser/json-whatwg
```

## Stream a JSON request body

This example parses a large JSON request body and extracts specific fields without loading the entire payload into memory.

* TypeScript

  ```ts
  import { JSONParser } from "@streamparser/json-whatwg";


  export default {
    async fetch(request): Promise<Response> {
      const parser = new JSONParser({ paths: ["$.users.*"] });


      const users: string[] = [];


      // Pipe the request body through the JSON parser
      const reader = request.body
        .pipeThrough(parser)
        .getReader();


      // Process matching JSON values as they stream in
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        // Extract only the name field from each user object
        if (value.value?.name) {
          users.push(value.value.name);
        }
      }


      return Response.json({ userNames: users });
    },
  } satisfies ExportedHandler;
  ```

* JavaScript

  ```js
  import { JSONParser } from "@streamparser/json-whatwg";


  export default {
    async fetch(request) {
      const parser = new JSONParser({ paths: ["$.users.*"] });


      const users = [];


      // Pipe the request body through the JSON parser
      const reader = request.body
        .pipeThrough(parser)
        .getReader();


      // Process matching JSON values as they stream in
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        // Extract only the name field from each user object
        if (value.value?.name) {
          users.push(value.value.name);
        }
      }


      return Response.json({ userNames: users });
    },
  };
  ```

## Stream and transform a JSON response

This example fetches a large JSON response from an upstream API, transforms specific fields, and streams the modified response to the client.

* TypeScript

  ```ts
  import { JSONParser } from "@streamparser/json-whatwg";


  export default {
    async fetch(request): Promise<Response> {
      const response = await fetch("https://api.example.com/large-dataset.json");


      const parser = new JSONParser({ paths: ["$.items.*"] });


      const { readable, writable } = new TransformStream();
      const writer = writable.getWriter();
      const encoder = new TextEncoder();


      // Process the upstream response in the background
      (async () => {
        const reader = response.body
          .pipeThrough(parser)
          .getReader();


        await writer.write(encoder.encode('{"processedItems":['));
        let first = true;


        while (true) {
          const { done, value } = await reader.read();
          if (done) break;


          // Transform each item as it streams through
          const item = value.value;
          const transformed = {
            id: item.id,
            title: item.title.toUpperCase(),
            processed: true,
          };


          if (!first) await writer.write(encoder.encode(","));
          first = false;
          await writer.write(encoder.encode(JSON.stringify(transformed)));
        }


        await writer.write(encoder.encode("]}"));
        await writer.close();
      })();


      return new Response(readable, {
        headers: { "Content-Type": "application/json" },
      });
    },
  } satisfies ExportedHandler;
  ```

* JavaScript

  ```js
  import { JSONParser } from "@streamparser/json-whatwg";


  export default {
    async fetch(request) {
      const response = await fetch("https://api.example.com/large-dataset.json");


      const parser = new JSONParser({ paths: ["$.items.*"] });


      const { readable, writable } = new TransformStream();
      const writer = writable.getWriter();
      const encoder = new TextEncoder();


      // Process the upstream response in the background
      (async () => {
        const reader = response.body
          .pipeThrough(parser)
          .getReader();


        await writer.write(encoder.encode('{"processedItems":['));
        let first = true;


        while (true) {
          const { done, value } = await reader.read();
          if (done) break;


          // Transform each item as it streams through
          const item = value.value;
          const transformed = {
            id: item.id,
            title: item.title.toUpperCase(),
            processed: true,
          };


          if (!first) await writer.write(encoder.encode(","));
          first = false;
          await writer.write(encoder.encode(JSON.stringify(transformed)));
        }


        await writer.write(encoder.encode("]}"));
        await writer.close();
      })();


      return new Response(readable, {
        headers: { "Content-Type": "application/json" },
      });
    },
  };
  ```

## Related resources

* [Streams API](https://developers.cloudflare.com/workers/runtime-apis/streams/) - Learn more about streaming in Workers
* [TransformStream](https://developers.cloudflare.com/workers/runtime-apis/streams/transformstream/) - Create custom stream transformations
* [@streamparser/json-whatwg](https://www.npmjs.com/package/@streamparser/json-whatwg) - Streaming JSON parser documentation