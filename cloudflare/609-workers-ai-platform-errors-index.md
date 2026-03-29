---
title: Errors · Cloudflare Workers AI docs
url: https://developers.cloudflare.com/workers-ai/platform/errors/index.md
source: llms
fetched_at: 2026-01-24T15:32:56.734719414-03:00
rendered_js: false
word_count: 306
summary: This document provides a comprehensive list of error codes, internal identifiers, and HTTP status codes for troubleshooting Cloudflare Workers AI.
tags:
    - workers-ai
    - error-codes
    - troubleshooting
    - cloudflare-workers
    - api-reference
category: reference
---

Below is a list of Workers AI errors.

| **Name** | **Internal Code** | **HTTP Code** | **Description** |
| - | - | - | - |
| No such model | `5007` | `400` | No such model `${model}` or task |
| Invalid data | `5004` | `400` | Invalid data type for base64 input: `${type}` |
| Finetune missing required files | `3039` | `400` | Finetune is missing required files `(model.safetensors and config.json)` |
| Incomplete request | `3003` | `400` | Request is missing headers or body: `{what}` |
| Account not allowed for private model | `5018` | `403` | The account is not allowed to access this model |
| Model agreement | `5016` | `403` | User has not agreed to Llama3.2 model terms |
| Account blocked | `3023` | `403` | Service unavailable for account |
| Account not allowed for private model | `3041` | `403` | The account is not allowed to access this model |
| Deprecated SDK version | `5019` | `405` | Request trying to use deprecated SDK version |
| LoRa unsupported | `5005` | `405` | The model `${this.model}` does not support LoRa inference |
| Invalid model ID | `3042` | `404` | The model name is invalid |
| Request too large | `3006` | `413` | Request is too large |
| Timeout | `3007` | `408` | Request timeout |
| Aborted | `3008` | `408` | Request was aborted |
| Account limited | `3036` | `429` | You have used up your daily free allocation of 10,000 neurons. Please upgrade to Cloudflare's Workers Paid plan if you would like to continue usage. |
| Out of capacity | `3040` | `429` | No more data centers to forward the request to |