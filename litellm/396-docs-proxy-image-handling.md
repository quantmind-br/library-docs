---
title: Image URL Handling | liteLLM
url: https://docs.litellm.ai/docs/proxy/image_handling
source: sitemap
fetched_at: 2026-01-21T19:52:42.907580261-03:00
rendered_js: false
word_count: 61
summary: Explains how LiteLLM automatically converts image URLs to base64 strings for incompatible LLM APIs and manages this process using in-memory caching.
tags:
    - litellm
    - image-processing
    - base64-conversion
    - caching
    - multimodal-api
category: concept
---

Some LLM API's don't support url's for images, but do support base-64 strings.

For those, LiteLLM will:

1. Detect a URL being passed
2. Check if the LLM API supports a URL
3. Else, will download the base64
4. Send the provider a base64 string.

LiteLLM also caches this result, in-memory to reduce latency for subsequent calls.

The limit for an in-memory cache is 1MB.