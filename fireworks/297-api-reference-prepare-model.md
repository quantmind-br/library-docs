---
title: Prepare Model for different precisions - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/prepare-model
source: sitemap
fetched_at: 2026-04-27T20:13:56.443238249-03:00
rendered_js: false
word_count: 225
summary: This document details the API endpoint and method for preparing a specific model under an account for different levels of computational precision. It outlines required parameters, including precision types and a read mask.
tags:
    - api
    - model-preparation
    - precision
    - http-post
    - fireworks-ai
    - rest-interface
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Prepare Model for different precisions

Prepares a model under an account for different computational precision levels.

## Endpoint

```
POST /v1/accounts/{account_id}/models/{model_id}:prepare
```

## Authorization

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `account_id` | string | Account identifier. |
| `model_id` | string | Model identifier. |

## Request Body

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `precision` | enum | `PRECISION_UNSPECIFIED` | Precision type (see options below). |
| `readMask` | string | — | Field mask for reading specific fields. |

### Precision Options

| Value | Description |
|-------|-------------|
| `PRECISION_UNSPECIFIED` | Unspecified (uses default). |
| `FP16` | Full precision 16-bit float. |
| `FP8` | 8-bit float. |
| `FP8_MM` | 8-bit float with matrix multiplication. |
| `FP8_AR` | 8-bit float with aspect ratio. |
| `FP8_MM_KV_ATTN` | 8-bit float MM with KV attention. |
| `FP8_MM_V2` | 8-bit float MM v2. |
| `FP8_V2` | 8-bit float v2. |
| `FP8_MM_KV_ATTN_V2` | 8-bit float MM KV attention v2. |
| `NF4` | Normal float 4-bit. |
| `FP4` | 4-bit float. |
| `BF16` | Bfloat16. |
| `FP4_BLOCKSCALED_MM` | 4-bit float block-scaled matrix multiplication. |
| `FP4_MX_MOE` | 4-bit float MX mixture of experts. |

## Response

Returns an `object`.

## Example

```bash
curl --request POST \
  --url https://api.fireworks.ai/v1/accounts/{account_id}/models/{model_id}:prepare \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "precision": "PRECISION_UNSPECIFIED",
  "readMask": "<string>"
}
'
```
