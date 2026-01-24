---
title: HuggingFace · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/usage/providers/huggingface/index.md
source: llms
fetched_at: 2026-01-24T14:03:20.651222724-03:00
rendered_js: false
word_count: 137
summary: This document provides instructions for routing HuggingFace Inference API requests through Cloudflare AI Gateway, including URL structure, prerequisites, and code examples.
tags:
    - huggingface
    - cloudflare-ai-gateway
    - inference-api
    - api-integration
    - machine-learning
category: guide
---

[HuggingFace](https://huggingface.co/) helps users build, deploy and train machine learning models.

## Endpoint

```txt
https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface
```

## URL structure

When making requests to HuggingFace Inference API, replace `https://api-inference.huggingface.co/models/` in the URL you're currently using with `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface`. Note that the model you're trying to access should come right after, for example `https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface/bigcode/starcoder`.

## Prerequisites

When making requests to HuggingFace, ensure you have the following:

* Your AI Gateway Account ID.
* Your AI Gateway gateway name.
* An active HuggingFace API token.
* The name of the HuggingFace model you want to use.

## Examples

### cURL

```bash
curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/huggingface/bigcode/starcoder \
  --header 'Authorization: Bearer {hf_api_token}' \
  --header 'Content-Type: application/json' \
  --data '{
    "inputs": "console.log"
}'
```

### Use HuggingFace.js library with JavaScript

If you are using the HuggingFace.js library, you can set your inference endpoint like this:

```js
import { HfInferenceEndpoint } from "@huggingface/inference";


const accountId = "{account_id}";
const gatewayId = "{gateway_id}";
const model = "gpt2";
const baseURL = `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/huggingface/${model}`;
const apiToken = env.HF_API_TOKEN;


const hf = new HfInferenceEndpoint(baseURL, apiToken);
```