---
title: Vertex AI Image Generation | liteLLM
url: https://docs.litellm.ai/docs/providers/vertex_image
source: sitemap
fetched_at: 2026-01-21T19:50:44.092588358-03:00
rendered_js: false
word_count: 223
summary: This document provides instructions and code examples for performing image generation through Google Vertex AI using LiteLLM with Gemini and Imagen models.
tags:
    - vertex-ai
    - image-generation
    - litellm
    - gemini
    - imagen
    - python
    - api-proxy
category: guide
---

Vertex AI supports two types of image generation:

1. **Gemini Image Generation Models** (Nano Banana 🍌) - Conversational image generation using `generateContent` API
2. **Imagen Models** - Traditional image generation using `predict` API

PropertyDetailsDescriptionVertex AI Image Generation supports both Gemini image generation modelsProvider Route on LiteLLM`vertex_ai/`Provider Doc[Google Cloud Vertex AI Image Generation ↗](https://cloud.google.com/vertex-ai/docs/generative-ai/image/generate-images)Gemini Image Generation Docs[Gemini Image Generation ↗](https://ai.google.dev/gemini-api/docs/image-generation)

## Quick Start[​](#quick-start "Direct link to Quick Start")

### Gemini Image Generation Models[​](#gemini-image-generation-models "Direct link to Gemini Image Generation Models")

Gemini image generation models support conversational image creation with features like:

- Text-to-Image generation
- Image editing (text + image → image)
- Multi-turn image refinement
- High-fidelity text rendering
- Up to 4K resolution (Gemini 3 Pro)

Gemini 2.5 Flash Image

```
import litellm

# Generate a single image
response =await litellm.aimage_generation(
    prompt="A nano banana dish in a fancy restaurant with a Gemini theme",
    model="vertex_ai/gemini-2.5-flash-image",
    vertex_ai_project="your-project-id",
    vertex_ai_location="us-central1",
    n=1,
    size="1024x1024",
)

print(response.data[0].b64_json)# Gemini returns base64 images
```

Gemini 3 Pro Image Preview (4K output)

```
import litellm

# Generate high-resolution image
response =await litellm.aimage_generation(
    prompt="Da Vinci style anatomical sketch of a dissected Monarch butterfly",
    model="vertex_ai/gemini-3-pro-image-preview",
    vertex_ai_project="your-project-id",
    vertex_ai_location="us-central1",
    n=1,
    size="1024x1024",
# Optional: specify image size for Gemini 3 Pro
# imageSize="4K",  # Options: "1K", "2K", "4K"
)

print(response.data[0].b64_json)
```

### Imagen Models[​](#imagen-models "Direct link to Imagen Models")

Imagen Image Generation

```
import litellm

# Generate a single image
response =await litellm.aimage_generation(
    prompt="An olympic size swimming pool with crystal clear water and modern architecture",
    model="vertex_ai/imagen-4.0-generate-001",
    vertex_ai_project="your-project-id",
    vertex_ai_location="us-central1",
    n=1,
    size="1024x1024",
)

print(response.data[0].b64_json)# Imagen also returns base64 images
```

### LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

#### 1. Configure your config.yaml[​](#1-configure-your-configyaml "Direct link to 1. Configure your config.yaml")

Vertex AI Image Generation Configuration

```
model_list:
-model_name: vertex-imagen
litellm_params:
model: vertex_ai/imagen-4.0-generate-001
vertex_ai_project:"your-project-id"
vertex_ai_location:"us-central1"
vertex_ai_credentials:"path/to/service-account.json"# Optional if using environment auth
```

#### 2. Start LiteLLM Proxy Server[​](#2-start-litellm-proxy-server "Direct link to 2. Start LiteLLM Proxy Server")

Start LiteLLM Proxy Server

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

#### 3. Make requests with OpenAI Python SDK[​](#3-make-requests-with-openai-python-sdk "Direct link to 3. Make requests with OpenAI Python SDK")

Basic Image Generation via Proxy

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Generate image
response = client.images.generate(
    model="vertex-imagen",
    prompt="An olympic size swimming pool with crystal clear water and modern architecture",
)

print(response.data[0].url)
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

### Gemini Image Generation Models[​](#gemini-image-generation-models-1 "Direct link to Gemini Image Generation Models")

- `vertex_ai/gemini-2.5-flash-image` - Fast, efficient image generation (1024px resolution)
- `vertex_ai/gemini-3-pro-image-preview` - Advanced model with 4K output, Google Search grounding, and thinking mode
- `vertex_ai/gemini-2.0-flash-preview-image` - Preview model
- `vertex_ai/gemini-2.5-flash-image-preview` - Preview model

### Imagen Models[​](#imagen-models-1 "Direct link to Imagen Models")

- `vertex_ai/imagegeneration@006` - Legacy Imagen model
- `vertex_ai/imagen-4.0-generate-001` - Latest Imagen model
- `vertex_ai/imagen-3.0-generate-001` - Imagen 3.0 model

tip

**We support ALL Vertex AI Image Generation models, just set `model=vertex_ai/<any-model-on-vertex_ai>` as a prefix when sending litellm requests**

For the complete and up-to-date list of supported models, visit: [https://models.litellm.ai/](https://models.litellm.ai/)