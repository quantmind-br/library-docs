---
title: Google AI Studio · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/google-ai-studio/index.md
source: llms
fetched_at: 2026-01-24T14:03:15.475038511-03:00
rendered_js: false
word_count: 178
summary: This document explains how to route Google AI Studio requests through Cloudflare AI Gateway using REST API calls, the Google Generative AI SDK, and OpenAI-compatible endpoints. It provides specific configuration details for endpoint URLs and various authentication methods.
tags:
    - cloudflare-ai-gateway
    - google-ai-studio
    - gemini-models
    - api-integration
    - rest-api
    - javascript-sdk
category: configuration
---

[Google AI Studio](https://ai.google.dev/aistudio) helps you build quickly with Google Gemini models.

## Endpoint

**Base URL:**

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-ai-studio
```

Then you can append the endpoint you want to hit, for example: `v1/models/{model}:{generative_ai_rest_resource}`

So your final URL will come together as: `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/google-ai-studio/v1/models/{model}:{generative_ai_rest_resource}`.

## Examples

### cURL

With API Key in Request

* With Authenticated Gateway

  ```bash
  curl "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_name}/google-ai-studio/v1/models/gemini-2.5-flash:generateContent" \
   --header 'content-type: application/json' \
   --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
   --header 'x-goog-api-key: {google_studio_api_key}' \
   --data '{
        "contents": [
            {
              "role":"user",
              "parts": [
                {"text":"What is Cloudflare?"}
              ]
            }
          ]
        }'
  ```

* Unauthenticated Gateway

  ```bash
  curl "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_name}/google-ai-studio/v1/models/gemini-2.5-flash:generateContent" \
   --header 'content-type: application/json' \
   --header 'x-goog-api-key: {google_studio_api_key}' \
   --data '{
        "contents": [
            {
              "role":"user",
              "parts": [
                {"text":"What is Cloudflare?"}
              ]
            }
          ]
        }'
  ```

With Stored Keys (BYOK) / Unified Billing

```bash
curl "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_name}/google-ai-studio/v1/models/gemini-2.5-flash:generateContent" \
 --header 'content-type: application/json' \
 --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
 --data '{
      "contents": [
          {
            "role":"user",
            "parts": [
              {"text":"What is Cloudflare?"}
            ]
          }
        ]
      }'
```

### `@google/genai`

If you are using the `@google/genai` package, you can set your endpoint like this:

With Key in Request

* With Authenticated Gateway

  ```js
  import { GoogleGenAI } from "@google/genai";


  const ai = new GoogleGenAI({
    apiKey: "{google_studio_api_key}",
    httpOptions: {
      baseUrl: `https://gateway.ai.cloudflare.com/v1/${account_id}/${gateway_name}/google-ai-studio`,
      headers: {
        'cf-aig-authorization': 'Bearer {cf_aig_token}',
      }
    }
  });


  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "What is Cloudflare?",
  });


  console.log(response.text);
  ```

* Unauthenticated Gateway

  ```js
  import { GoogleGenAI } from "@google/genai";


  const ai = new GoogleGenAI({
    apiKey: "{google_studio_api_key}",
    httpOptions: {
      baseUrl: `https://gateway.ai.cloudflare.com/v1/${account_id}/${gateway_name}/google-ai-studio`,
    }
  });


  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "What is Cloudflare?",
  });


  console.log(response.text);
  ```

With Stored Keys (BYOK) / Unified Billing

```js
import { GoogleGenAI } from "@google/genai";


const ai = new GoogleGenAI({
  apiKey: "{cf_aig_token}",
  httpOptions: {
    baseUrl: `https://gateway.ai.cloudflare.com/v1/${account_id}/${gateway_name}/google-ai-studio`,
  }
});


const response = await ai.models.generateContent({
  model: "gemini-2.5-flash",
  contents: "What is Cloudflare?",
});


console.log(response.text);
```

## OpenAI-Compatible Endpoint

You can also use the [OpenAI-compatible endpoint](https://developers.cloudflare.com/ai-gateway/usage/chat-completion/) (`/ai-gateway/usage/chat-completion/`) to access Google AI Studio models using the OpenAI API schema. To do so, send your requests to:

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions
```

Specify:

```json
{
"model": "google-ai-studio/{model}"
}
```