---
title: Writing to streams · Cloudflare Pipelines Docs
url: https://developers.cloudflare.com/pipelines/streams/writing-to-streams/index.md
source: llms
fetched_at: 2026-01-24T15:19:28.296966855-03:00
rendered_js: false
word_count: 251
summary: This document explains how to ingest event data into Cloudflare streams using Worker bindings for internal scripts and HTTP endpoints for external applications.
tags:
    - cloudflare-workers
    - pipelines
    - data-ingestion
    - event-streaming
    - wrangler-config
    - http-post
category: guide
---

Send events to streams using [Worker bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) or HTTP endpoints for client-side applications and external systems.

## Send via Workers

Worker bindings provide a secure way to send data to streams from [Workers](https://developers.cloudflare.com/workers/) without managing API tokens or credentials.

### Configure pipeline binding

Add a pipeline binding to your Wrangler file that points to your stream:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "pipelines": [
      {
        "pipeline": "<STREAM_ID>",
        "binding": "STREAM"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  [[pipelines]]
  pipeline = "<STREAM_ID>"
  binding = "STREAM"
  ```

### Workers API

The pipeline binding exposes a method for sending data to your stream:

#### `send(records)`

Sends an array of JSON-serializable records to the stream. Returns a Promise that resolves when records are confirmed as ingested.

* JavaScript

  ```js
  export default {
    async fetch(request, env, ctx) {
      const event = {
        user_id: "12345",
        event_type: "purchase",
        product_id: "widget-001",
        amount: 29.99,
      };


      await env.STREAM.send([event]);


      return new Response("Event sent");
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request, env, ctx): Promise<Response> {
      const event = {
        user_id: "12345",
        event_type: "purchase",
        product_id: "widget-001",
        amount: 29.99
      };


        await env.STREAM.send([event]);


        return new Response('Event sent');
      },


  } satisfies ExportedHandler<Env>;
  ```

## Send via HTTP

Each stream provides an optional HTTP endpoint for ingesting data from external applications, browsers, or any system that can make HTTP requests.

### Endpoint format

HTTP endpoints follow this format:

```plaintext
https://{stream-id}.ingest.cloudflare.com
```

Find your stream's endpoint URL in the Cloudflare dashboard under **Pipelines** > **Streams** or using the Wrangler CLI:

```bash
npx wrangler pipelines streams get <STREAM_ID>
```

### Making requests

Send events as JSON arrays via POST requests:

```bash
curl -X POST https://{stream-id}.ingest.cloudflare.com \
  -H "Content-Type: application/json" \
  -d '[
    {
      "user_id": "12345",
      "event_type": "purchase",
      "product_id": "widget-001",
      "amount": 29.99
    }
  ]'
```

### Authentication

When authentication is enabled for your stream, include the API token in the `Authorization` header:

```bash
curl -X POST https://{stream-id}.ingest.cloudflare.com \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -d '[{"event": "test"}]'
```

The API token must have **Workers Pipeline Send** permission. To learn more, refer to the [Create API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) documentation.

## Schema validation

Streams handle validation differently based on their configuration:

* **Structured streams**: Events must match the defined schema fields and types.
* **Unstructured streams**: Accept any valid JSON structure. Data is stored in a single `value` column.

For structured streams, ensure your events match the schema definition. Invalid events will be accepted but dropped, so validate your data before sending to avoid dropped events.