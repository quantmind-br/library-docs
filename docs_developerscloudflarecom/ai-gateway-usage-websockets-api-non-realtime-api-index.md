---
title: Non-realtime WebSockets API · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/websockets-api/non-realtime-api/index.md
source: llms
fetched_at: 2026-01-24T14:03:42.547914211-03:00
rendered_js: false
word_count: 230
summary: This document explains how to set up and utilize the Non-realtime WebSockets API for persistent AI request connections through Cloudflare AI Gateway. It covers authentication, endpoint configuration, and provides examples for both standard and streaming request-response patterns.
tags:
    - cloudflare-ai-gateway
    - websockets
    - streaming-api
    - persistent-connections
    - ai-infrastructure
category: api
---

The Non-realtime WebSockets API allows you to establish persistent connections for AI requests without requiring repeated handshakes. This approach is ideal for applications that do not require real-time interactions but still benefit from reduced latency and continuous communication.

## Set up WebSockets API

1. Generate an AI Gateway token with appropriate AI Gateway Run and opt in to using an authenticated gateway.

2. Modify your Universal Endpoint URL by replacing `https://` with `wss://` to initiate a WebSocket connection:

   ```plaintext
   wss://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}
   ```

3. Open a WebSocket connection authenticated with a Cloudflare token with the AI Gateway Run permission.

Note

Alternatively, we also support authentication via the `sec-websocket-protocol` header if you are using a browser WebSocket.

## Example request

```javascript
import WebSocket from "ws";


const ws = new WebSocket(
  "wss://gateway.ai.cloudflare.com/v1/my-account-id/my-gateway/",
  {
    headers: {
      "cf-aig-authorization": "Bearer AI_GATEWAY_TOKEN",
    },
  },
);


ws.on("open", () => {
  ws.send(
    JSON.stringify({
      type: "universal.create",
      request: {
        eventId: "my-request",
        provider: "workers-ai",
        endpoint: "@cf/meta/llama-3.1-8b-instruct",
        headers: {
          Authorization: "Bearer WORKERS_AI_TOKEN",
          "Content-Type": "application/json",
        },
        query: {
          prompt: "tell me a joke",
        },
      },
    }),
  );
})


ws.on("message", (message) => {
  console.log(message.toString());
});
```

## Example response

```json
{
  "type": "universal.created",
  "metadata": {
    "cacheStatus": "MISS",
    "eventId": "my-request",
    "logId": "01JC3R94FRD97JBCBX3S0ZAXKW",
    "step": "0",
    "contentType": "application/json"
  },
  "response": {
    "result": {
      "response": "Why was the math book sad? Because it had too many problems. Would you like to hear another one?"
    },
    "success": true,
    "errors": [],
    "messages": []
  }
}
```

## Example streaming request

For streaming requests, AI Gateway sends an initial message with request metadata indicating the stream is starting:

```json
{
  "type": "universal.created",
  "metadata": {
    "cacheStatus": "MISS",
    "eventId": "my-request",
    "logId": "01JC40RB3NGBE5XFRZGBN07572",
    "step": "0",
    "contentType": "text/event-stream"
  }
}
```

After this initial message, all streaming chunks are relayed in real-time to the WebSocket connection as they arrive from the inference provider. Only the `eventId` field is included in the metadata for these streaming chunks. The `eventId` allows AI Gateway to include a client-defined ID with each message, even in a streaming WebSocket environment.

```json
{
  "type": "universal.stream",
  "metadata": {
    "eventId": "my-request"
  },
  "response": {
    "response": "would"
  }
}
```

Once all chunks for a request have been streamed, AI Gateway sends a final message to signal the completion of the request. For added flexibility, this message includes all the metadata again, even though it was initially provided at the start of the streaming process.

```json
{
  "type": "universal.done",
  "metadata": {
    "cacheStatus": "MISS",
    "eventId": "my-request",
    "logId": "01JC40RB3NGBE5XFRZGBN07572",
    "step": "0",
    "contentType": "text/event-stream"
  }
}
```