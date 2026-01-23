---
title: RunwayML - Image Generation | liteLLM
url: https://docs.litellm.ai/docs/providers/runwayml/images
source: sitemap
fetched_at: 2026-01-21T19:50:19.257202127-03:00
rendered_js: false
word_count: 257
summary: This document provides a comprehensive guide for integrating and using RunwayML's Gen-4 image generation API through LiteLLM, including setup, parameter support, and cost tracking.
tags:
    - litellm
    - runwayml
    - image-generation
    - api-integration
    - python
    - asynchronous-processing
    - image-api
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionRunwayML provides advanced AI-powered image generation with high-quality resultsProvider Route on LiteLLM`runwayml/`Supported Operations[`/images/generations`](#quick-start)Link to Provider Doc[RunwayML API ↗](https://docs.dev.runwayml.com/)

LiteLLM supports RunwayML's Gen-4 image generation API, allowing you to generate high-quality images from text prompts.

## Quick Start[​](#quick-start "Direct link to Quick Start")

Basic Image Generation

```
from litellm import image_generation
import os

os.environ["RUNWAYML_API_KEY"]="your-api-key"

response = image_generation(
    model="runwayml/gen4_image",
    prompt="A serene mountain landscape at sunset",
    size="1920x1080"
)

print(response.data[0].url)
```

## Authentication[​](#authentication "Direct link to Authentication")

Set your RunwayML API key:

Set API Key

```
import os

os.environ["RUNWAYML_API_KEY"]="your-api-key"
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

ParameterTypeRequiredDescription`model`stringYesModel to use (e.g., `runwayml/gen4_image`)`prompt`stringYesText description for the image`size`stringNoImage dimensions (default: `1920x1080`)

### Supported Sizes[​](#supported-sizes "Direct link to Supported Sizes")

- `1024x1024`
- `1792x1024`
- `1024x1792`
- `1920x1080` (default)
- `1080x1920`

## Async Usage[​](#async-usage "Direct link to Async Usage")

Async Image Generation

```
from litellm import aimage_generation
import os
import asyncio

os.environ["RUNWAYML_API_KEY"]="your-api-key"

asyncdefgenerate_image():
    response =await aimage_generation(
        model="runwayml/gen4_image",
        prompt="A futuristic city skyline at night",
        size="1920x1080"
)

print(response.data[0].url)

asyncio.run(generate_image())
```

## LiteLLM Proxy Usage[​](#litellm-proxy-usage "Direct link to LiteLLM Proxy Usage")

Add RunwayML to your proxy configuration:

config.yaml

```
model_list:
-model_name: gen4-image
litellm_params:
model: runwayml/gen4_image
api_key: os.environ/RUNWAYML_API_KEY
```

Start the proxy:

```
litellm --config /path/to/config.yaml
```

Generate images through the proxy:

Proxy Request

```
curl --location 'http://localhost:4000/v1/images/generations' \
--header 'Content-Type: application/json' \
--header 'x-litellm-api-key: sk-1234' \
--data '{
    "model": "runwayml/gen4_image",
    "prompt": "A serene mountain landscape at sunset",
    "size": "1920x1080"
}'
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

ModelDescriptionDefault Size`runwayml/gen4_image`High-quality image generation1920x1080

## Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

LiteLLM automatically tracks RunwayML image generation costs:

Cost Tracking

```
from litellm import image_generation, completion_cost

response = image_generation(
    model="runwayml/gen4_image",
    prompt="A serene mountain landscape at sunset",
    size="1920x1080"
)

cost = completion_cost(completion_response=response)
print(f"Image generation cost: ${cost}")
```

## Supported Features[​](#supported-features "Direct link to Supported Features")

FeatureSupportedImage Generation✅Cost Tracking✅Logging✅Fallbacks✅Load Balancing✅

## How It Works[​](#how-it-works "Direct link to How It Works")

RunwayML uses an asynchronous task-based API pattern. LiteLLM handles the polling and response transformation automatically.

### Complete Flow Diagram[​](#complete-flow-diagram "Direct link to Complete Flow Diagram")

### What LiteLLM Does For You[​](#what-litellm-does-for-you "Direct link to What LiteLLM Does For You")

When you call `litellm.image_generation()` or `/v1/images/generations`:

1. **Request Transformation**: Converts OpenAI image generation format → RunwayML format
2. **Submits Task**: Sends transformed request to RunwayML API
3. **Receives Task ID**: Captures the task ID from the initial response
4. **Automatic Polling**:
   
   - Polls the task status endpoint every 2 seconds
   - Continues until status is `SUCCEEDED` or `FAILED`
   - Default timeout: 10 minutes (configurable via `RUNWAYML_POLLING_TIMEOUT`)
5. **Response Transformation**: Converts RunwayML format → OpenAI format
6. **Returns Result**: Sends unified OpenAI format response to client

**Polling Configuration:**

- Default timeout: 600 seconds (10 minutes)
- Configurable via `RUNWAYML_POLLING_TIMEOUT` environment variable
- Uses sync (`time.sleep()`) or async (`await asyncio.sleep()`) based on call type

info

**Typical processing time**: 10-30 seconds depending on image size and complexity