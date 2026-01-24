---
title: Ideogram · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/ideogram/index.md
source: llms
fetched_at: 2026-01-24T15:08:17.559010362-03:00
rendered_js: false
word_count: 97
summary: This document explains how to configure and use the Ideogram text-to-image generation API through Cloudflare AI Gateway.
tags:
    - cloudflare-ai-gateway
    - ideogram
    - text-to-image
    - api-integration
    - image-generation
category: api
---

[Ideogram](https://ideogram.ai/) provides advanced text-to-image generation models with exceptional text rendering capabilities and visual quality.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/ideogram
```

## Prerequisites

When making requests to Ideogram, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active Ideogram API key.
* The name of the Ideogram model you want to use (e.g., `V_3`).

## Examples

### cURL

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/ideogram/v1/ideogram-v3/generate \
  --header 'Api-Key: {ideogram_api_key}' \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": "A serene landscape with mountains and a lake at sunset",
    "model": "V_3"
  }'
```

### Use with JavaScript

```js
const accountId = "{account_id}";
const gatewayId = "{gateway_id}";
const ideogramApiKey = "{ideogram_api_key}";
const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/ideogram`;


const response = await fetch(`${baseURL}/v1/ideogram-v3/generate`, {
  method: "POST",
  headers: {
    "Api-Key": ideogramApiKey,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    prompt: "A serene landscape with mountains and a lake at sunset",
    model: "V_3",
  }),
});


const result = await response.json();
console.log(result);
```