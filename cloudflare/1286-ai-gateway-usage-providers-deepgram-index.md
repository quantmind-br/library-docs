---
title: Deepgram · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/deepgram/index.md
source: llms
fetched_at: 2026-01-24T15:08:09.057438212-03:00
rendered_js: false
word_count: 70
summary: This document explains how to integrate Deepgram's Voice AI services with Cloudflare AI Gateway, providing instructions on endpoint configuration and authentication.
tags:
    - deepgram
    - cloudflare-ai-gateway
    - voice-ai
    - api-integration
    - websockets
    - speech-to-text
category: guide
---

[Deepgram](https://developers.deepgram.com/home) provides Voice AI APIs for speech-to-text, text-to-speech, and voice agents.

Note

Deepgram is also available through Workers AI, see [Deepgram Workers AI](https://developers.cloudflare.com/ai-gateway/usage/websockets-api/realtime-api/#deepgram-workers-ai).

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram
```

## URL Structure

When making requests to Deepgram, replace `https://api.deepgram.com/` in the URL you are currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/`.

## Prerequisites

When making requests to Deepgram, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active Deepgram API token.

## Example

### SDK

```ts
import { createClient, LiveTranscriptionEvents } from "@deepgram/sdk";




const deepgram = createClient("{deepgram_api_key}", {
    global: {
      websocket: {
        options: {
          url: "wss://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/deepgram/",
          _nodeOnlyHeaders: {
            "cf-aig-authorization": "Bearer {CF_AIG_TOKEN}"
          }
        }
      }
    }
});




const connection = deepgram.listen.live({
    model: "nova-3",
    language: "en-US",
    smart_format: true,
});


connection.send(...);
```