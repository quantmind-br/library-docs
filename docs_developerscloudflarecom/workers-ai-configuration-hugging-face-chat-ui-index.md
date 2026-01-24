---
title: Hugging Face Chat UI · Cloudflare Workers AI docs
url: https://developers.cloudflare.com/workers-ai/configuration/hugging-face-chat-ui/index.md
source: llms
fetched_at: 2026-01-24T15:32:40.495535274-03:00
rendered_js: false
word_count: 99
summary: This document provides instructions on how to integrate Cloudflare Workers AI with the Hugging Face Chat UI open-source interface.
tags:
    - cloudflare-workers-ai
    - hugging-face
    - chat-ui
    - llm-deployment
    - api-configuration
category: guide
---

Use Workers AI with [Chat UI](https://github.com/huggingface/chat-ui?tab=readme-ov-file#text-embedding-models), an open-source chat interface offered by Hugging Face.

## Prerequisites

You will need the following:

* A [Cloudflare account](https://dash.cloudflare.com)
* Your [Account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/)
* An [API token](https://developers.cloudflare.com/workers-ai/get-started/rest-api/#1-get-api-token-and-account-id) for Workers AI

## Setup

First, decide how to reference your Account ID and API token (either directly in your `.env.local` using the `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_API_TOKEN` variables or in the endpoint configuration).

Then, follow the rest of the setup instructions in the [Chat UI GitHub repository](https://github.com/huggingface/chat-ui?tab=readme-ov-file#text-embedding-models).

When setting up your models, specify the `cloudflare` endpoint.

```json
{
  "name" : "nousresearch/hermes-2-pro-mistral-7b",
  "tokenizer": "nousresearch/hermes-2-pro-mistral-7b",
  "parameters": {
    "stop": ["<|im_end|>"]
  },
  "endpoints" : [
    {
      "type": "cloudflare",
      // optionally specify these if not included in .env.local
      "accountId": "your-account-id",
      "apiToken": "your-api-token"
      //
    }
  ]
}
```

## Supported models

This template works with any [text generation models](https://developers.cloudflare.com/workers-ai/models/) that begin with the `@hf` parameter.