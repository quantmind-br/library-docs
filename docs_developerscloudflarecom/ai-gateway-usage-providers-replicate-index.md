---
title: Replicate · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/replicate/index.md
source: llms
fetched_at: 2026-01-24T14:03:32.662914386-03:00
rendered_js: false
word_count: 73
summary: This document explains how to route Replicate API requests through Cloudflare AI Gateway by updating the base URL and providing necessary credentials.
tags:
    - cloudflare-ai-gateway
    - replicate
    - api-integration
    - machine-learning
    - model-hosting
category: guide
---

[Replicate](https://replicate.com/) runs and fine tunes open-source models.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate
```

## URL structure

When making requests to Replicate, replace `https://api.replicate.com/v1` in the URL you're currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate`.

## Prerequisites

When making requests to Replicate, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active Replicate API token. You can create one at [replicate.com/settings/api-tokens](https://replicate.com/settings/api-tokens)
* The name of the Replicate model you want to use, like `anthropic/claude-4.5-haiku` or `google/nano-banana`.

## Example

### cURL

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/replicate/predictions \
  --header 'Authorization: Bearer {replicate_api_token}' \
  --header 'Content-Type: application/json' \
  --data '{
    "version": "anthropic/claude-4.5-haiku",
    "input":
      {
        "prompt": "Write a haiku about Cloudflare"
      }
    }'
```