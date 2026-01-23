---
title: Google AI Studio SDK | liteLLM
url: https://docs.litellm.ai/docs/pass_through/google_ai_studio
source: sitemap
fetched_at: 2026-01-21T19:46:52.839626359-03:00
rendered_js: false
word_count: 252
summary: This document explains how to configure and use LiteLLM Proxy as a pass-through for Google AI Studio, enabling features like cost tracking and logging with native provider endpoints.
tags:
    - litellm-proxy
    - google-ai-studio
    - gemini-api
    - pass-through-api
    - usage-tracking
    - api-integration
category: guide
---

Pass-through endpoints for Google AI Studio - call provider-specific endpoint, in native format (no translation).

FeatureSupportedNotesCost Tracking✅supports all models on `/generateContent` endpointLogging✅works across all integrationsEnd-user Tracking❌[Tell us if you need this](https://github.com/BerriAI/litellm/issues/new)Streaming✅

Just replace `https://generativelanguage.googleapis.com` with `LITELLM_PROXY_BASE_URL/gemini`

#### **Example Usage**[​](#example-usage "Direct link to example-usage")

- curl
- Google AI Node.js SDK

```
curl 'http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:countTokens?key=sk-anything' \
-H 'Content-Type: application/json' \
-d '{
    "contents": [{
        "parts":[{
          "text": "The quick brown fox jumps over the lazy dog."
          }]
        }]
}'
```

Supports **ALL** Google AI Studio Endpoints (including streaming).

[**See All Google AI Studio Endpoints**](https://ai.google.dev/api)

## Quick Start[​](#quick-start "Direct link to Quick Start")

Let's call the Gemini [`/countTokens` endpoint](https://ai.google.dev/api/tokens#method:-models.counttokens)

1. Add Gemini API Key to your environment

<!--THE END-->

2. Start LiteLLM Proxy

```
litellm

# RUNNING on http://0.0.0.0:4000
```

3. Test it!

Let's call the Google AI Studio token counting endpoint

```
http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:countTokens?key=anything' \
-H 'Content-Type: application/json' \
-d '{
    "contents": [{
        "parts":[{
          "text": "The quick brown fox jumps over the lazy dog."
          }]
        }]
}'
```

## Examples[​](#examples "Direct link to Examples")

Anything after `http://0.0.0.0:4000/gemini` is treated as a provider-specific route, and handled accordingly.

Key Changes:

**Original Endpoint****Replace With**`https://generativelanguage.googleapis.com``http://0.0.0.0:4000/gemini` (LITELLM\_PROXY\_BASE\_URL="[http://0.0.0.0:4000](http://0.0.0.0:4000)")`key=$GOOGLE_API_KEY``key=anything` (use `key=LITELLM_VIRTUAL_KEY` if Virtual Keys are setup on proxy)

### **Example 1: Counting tokens**[​](#example-1-counting-tokens "Direct link to example-1-counting-tokens")

#### LiteLLM Proxy Call[​](#litellm-proxy-call "Direct link to LiteLLM Proxy Call")

```
curl http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:countTokens?key=anything \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[{
          "text": "The quick brown fox jumps over the lazy dog."
          }],
        }],
      }'
```

#### Direct Google AI Studio Call[​](#direct-google-ai-studio-call "Direct link to Direct Google AI Studio Call")

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:countTokens?key=$GOOGLE_API_KEY \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[{
          "text": "The quick brown fox jumps over the lazy dog."
          }],
        }],
      }'
```

### **Example 2: Generate content**[​](#example-2-generate-content "Direct link to example-2-generate-content")

#### LiteLLM Proxy Call[​](#litellm-proxy-call-1 "Direct link to LiteLLM Proxy Call")

```
curl "http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:generateContent?key=anything" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[{"text": "Write a story about a magic backpack."}]
        }]
       }' 2> /dev/null
```

#### Direct Google AI Studio Call[​](#direct-google-ai-studio-call-1 "Direct link to Direct Google AI Studio Call")

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[{"text": "Write a story about a magic backpack."}]
        }]
       }' 2> /dev/null
```

### **Example 3: Caching**[​](#example-3-caching "Direct link to example-3-caching")

```
curl -X POST "http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash-001:generateContent?key=anything" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
```

#### Direct Google AI Studio Call[​](#direct-google-ai-studio-call-2 "Direct link to Direct Google AI Studio Call")

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-001:generateContent?key=$GOOGLE_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [
        {
          "parts":[{
            "text": "Please summarize this transcript"
          }],
          "role": "user"
        },
      ],
      "cachedContent": "'$CACHE_NAME'"
    }'
```

## **Example 4: Video Generation with Veo**[​](#example-4-video-generation-with-veo "Direct link to example-4-video-generation-with-veo")

Generate videos using Google's Veo model through LiteLLM pass-through routes.

[**→ Complete Veo Video Generation Guide**](https://docs.litellm.ai/docs/proxy/veo_video_generation)

## Advanced[​](#advanced "Direct link to Advanced")

Pre-requisites

- [Setup proxy with DB](https://docs.litellm.ai/docs/proxy/virtual_keys#setup)

Use this, to avoid giving developers the raw Google AI Studio key, but still letting them use Google AI Studio endpoints.

### Use with Virtual Keys[​](#use-with-virtual-keys "Direct link to Use with Virtual Keys")

1. Setup environment

```
export DATABASE_URL=""
export LITELLM_MASTER_KEY=""
export GEMINI_API_KEY=""
```

```
litellm

# RUNNING on http://0.0.0.0:4000
```

2. Generate virtual key

```
curl -X POST 'http://0.0.0.0:4000/key/generate' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{}'
```

Expected Response

```
{
    ...
    "key": "sk-1234ewknldferwedojwojw"
}
```

3. Test it!

```
http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:countTokens?key=sk-1234ewknldferwedojwojw' \
-H 'Content-Type: application/json' \
-d '{
    "contents": [{
        "parts":[{
          "text": "The quick brown fox jumps over the lazy dog."
          }]
        }]
}'
```

Use this if you want `tags` to be tracked in the LiteLLM DB and on logging callbacks.

Pass tags in request headers as a comma separated list. In the example below the following tags will be tracked

```
tags: ["gemini-js-sdk", "pass-through-endpoint"]
```

- curl
- Google AI Node.js SDK

```
curl 'http://0.0.0.0:4000/gemini/v1beta/models/gemini-1.5-flash:generateContent?key=sk-anything' \
-H 'Content-Type: application/json' \
-H 'tags: gemini-js-sdk,pass-through-endpoint' \
-d '{
    "contents": [{
        "parts":[{
          "text": "The quick brown fox jumps over the lazy dog."
          }]
        }]
}'
```