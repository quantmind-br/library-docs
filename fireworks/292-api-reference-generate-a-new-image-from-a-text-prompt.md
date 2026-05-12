---
title: Generate an image with FLUX.1 [schnell] FP8 - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/generate-a-new-image-from-a-text-prompt
source: sitemap
fetched_at: 2026-04-27T20:14:34.257173236-03:00
rendered_js: false
word_count: 281
summary: This document details how to call the Fireworks AI inference endpoint for text-to-image generation using a REST API. It explains the required request headers and body parameters, along with the structure of the expected JSON or binary response.
tags:
    - api-inference
    - text-to-image
    - flux-model
    - rest-client
    - workflow-api
    - json-response
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Generate an image with FLUX.1 [schnell] FP8

[FLUX.1 [schnell]](https://huggingface.co/fireworks-ai/FLUX.1-schnell-fp8-flumina) is a 12 billion parameter rectified flow transformer for text-to-image generation. The FP8 version uses reduced precision numerics for 2x faster inference.

## Endpoint

```
POST /inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image
```

## Headers

| Header | Type | Description |
|--------|------|-------------|
| `Content-Type` | string | Media type of the request body. |
| `Accept` | string | Response format: `image/png`, `image/jpeg`, or `application/json`. |
| `Authorization` | string | Bearer with Fireworks API Key. |

## Request Body

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `prompt` | string | required | Prompt for image generation. |
| `aspect_ratio` | string | `1:1` | Aspect ratio. Options: `1:1`, `21:9`, `16:9`, `3:2`, `5:4`, `4:5`, `2:3`, `9:16`, `9:21`, `4:3`, `3:4` |
| `guidance_scale` | number | `3.5` | Classifier-free guidance scale for the diffusion process. |
| `num_inference_steps` | integer | `4` | Number of denoising steps. |
| `seed` | integer | `0` | Random seed. `0` generates a random seed. |

## Response

Returns either a binary image or JSON based on the `Accept` header.

### JSON Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the request. |
| `base64` | array | Base64-encoded PNG image strings. |
| `finishReason` | string | `SUCCESS` or `CONTENT_FILTERED`. |
| `seed` | integer | Random seed used for generation. |

### Binary Response Headers

When `Accept` is `image/jpeg` or `image/png`:
- **Content-Length** — Length of the binary image
- **Seed** — Random seed used
- **Finish-Reason** — `CONTENT_FILTERED` or `SUCCESS`

## Example

```python
import requests

url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image"
headers = {
    "Content-Type": "application/json",
    "Accept": "image/jpeg",
    "Authorization": "Bearer $API_KEY",
}
data = {
    "prompt": "A beautiful sunset over the ocean"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    with open("a.jpg", "wb") as f:
        f.write(response.content)
    print("Image saved as a.jpg")
else:
    print("Error:", response.status_code, response.text)
```

## Try it out

Use the [Playground](https://app.fireworks.ai/playground?model=accounts%2Ffireworks%2Fmodels%2Fflux-1-schnell-fp8) to try FLUX.1 schnell in your browser.
