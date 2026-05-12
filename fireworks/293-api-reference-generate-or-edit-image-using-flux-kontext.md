---
title: Generate or edit an image with FLUX.1 Kontext - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/generate-or-edit-image-using-flux-kontext
source: sitemap
fetched_at: 2026-04-27T20:14:18.254919407-03:00
rendered_js: false
word_count: 280
summary: This document details the specifications for an asynchronous image generation API, outlining the available models (FLUX.1 Kontext Pro and FLUX.1 Kontext Max), the required request body parameters, and the expected response structure.
tags:
    - image-generation
    - api-specifications
    - flux-kontext
    - request-body
    - asynchronous
    - model-options
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Generate or edit an image with FLUX.1 Kontext

> [!note]
> This API is async and returns the **request_id** instead of the image. Call [[241-api-reference-get-generated-image-from-flux-kontex|get_result]] to retrieve the generated image.

## Available Models

| Model | Description |
|-------|-------------|
| **FLUX.1 Kontext Pro** | Specialized model for contextually-aware image generation. Designed for professional use cases. |
| **FLUX.1 Kontext Max** | Most advanced model in the Kontext series with maximum quality and context understanding. Ideal for enterprise applications. |

## Path

```
/inference/v1/workflows/accounts/fireworks/models/{model}/flux_kontext
```

Use `flux-kontext-pro` or `flux-kontext-max` as the model name.

## Headers

| Header | Type | Description |
|--------|------|-------------|
| `Content-Type` | string | Media type of the request body. |

## Request Body

| Field | Type | Description |
|-------|------|-------------|
| `prompt` | string | Prompt for image generation. |
| `input_image` | string | Base64 encoded image or URL for image-to-image. |
| `seed` | integer | Optional seed for reproducibility. |
| `aspect_ratio` | string | Image aspect ratio between `21:9` and `9:21`. |
| `output_format` | string | Output format: `jpeg` or `png`. |
| `webhook_url` | string | URL for webhook notifications. (1-2083 chars) |
| `webhook_secret` | string | Optional secret for webhook signature verification. |
| `prompt_upsampling` | boolean | Whether to perform upsampling on the prompt for more creative generation. |
| `moderation_tolerance` | integer | Tolerance level for moderation (0-6). 0 is most strict, 6 least strict. Limit of 2 for Image to Image. |

## Response

| Status | Description |
|--------|-------------|
| `200` | Request accepted. |
| `400` | Invalid request. |

## Try it out

- [FLUX Kontext Pro Playground](https://app.fireworks.ai/playground?model=accounts%2Ffireworks%2Fmodels%2Fflux-kontext-pro)
- [FLUX Kontext Max Playground](https://app.fireworks.ai/playground?model=accounts%2Ffireworks%2Fmodels%2Fflux-kontext-max)
