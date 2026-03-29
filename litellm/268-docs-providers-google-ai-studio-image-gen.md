---
title: Google AI Studio Image Generation | liteLLM
url: https://docs.litellm.ai/docs/providers/google_ai_studio/image_gen
source: sitemap
fetched_at: 2026-01-21T19:49:16.945985725-03:00
rendered_js: false
word_count: 189
summary: This document explains how to integrate and use Google AI Studio's Imagen models for image generation through the LiteLLM library and proxy server. It covers API configuration, environment setup, and code examples for both the LiteLLM and OpenAI Python SDKs.
tags:
    - google-ai-studio
    - imagen
    - litellm
    - image-generation
    - text-to-image
    - api-setup
    - python
category: guide
---

Google AI Studio provides powerful image generation capabilities using Google's Imagen models to create high-quality images from text descriptions.

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionGoogle AI Studio Image Generation uses Google's Imagen models to generate high-quality images from text descriptions.Provider Route on LiteLLM`gemini/`Provider Doc[Google AI Studio Image Generation ↗](https://ai.google.dev/gemini-api/docs/imagen)Supported Operations[`/images/generations`](#image-generation)

## Setup[​](#setup "Direct link to Setup")

### API Key[​](#api-key "Direct link to API Key")

```
# Set your Google AI Studio API key
import os
os.environ["GEMINI_API_KEY"]="your-api-key-here"
```

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Image Generation[​](#image-generation "Direct link to Image Generation")

### Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

- Basic Usage
- Async Usage
- Advanced Parameters

Basic Image Generation

```
import litellm
import os

# Set your API key
os.environ["GEMINI_API_KEY"]="your-api-key-here"

# Generate a single image
response = litellm.image_generation(
    model="gemini/imagen-4.0-generate-001",
    prompt="A cute baby sea otter swimming in crystal clear water"
)

print(response.data[0].url)
```

### Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

#### 1. Configure your config.yaml[​](#1-configure-your-configyaml "Direct link to 1. Configure your config.yaml")

Google AI Studio Image Generation Configuration

```
model_list:
-model_name: google-imagen
litellm_params:
model: gemini/imagen-4.0-generate-001
api_key: os.environ/GEMINI_API_KEY
model_info:
mode: image_generation

general_settings:
master_key: sk-1234
```

#### 2. Start LiteLLM Proxy Server[​](#2-start-litellm-proxy-server "Direct link to 2. Start LiteLLM Proxy Server")

Start LiteLLM Proxy Server

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

#### 3. Make requests with OpenAI Python SDK[​](#3-make-requests-with-openai-python-sdk "Direct link to 3. Make requests with OpenAI Python SDK")

- OpenAI SDK
- LiteLLM SDK
- cURL

Google AI Studio Image Generation via Proxy - OpenAI SDK

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="sk-1234"# Your proxy API key
)

# Generate image
response = client.images.generate(
    model="google-imagen",
    prompt="A majestic eagle soaring over snow-capped mountains",
    n=1,
    size="1024x1024"
)

print(response.data[0].url)
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

Google AI Studio Image Generation supports the following OpenAI-compatible parameters:

ParameterTypeDescriptionDefaultExample`prompt`stringText description of the image to generateRequired`"A sunset over the ocean"``model`stringThe model to use for generationRequired`"gemini/imagen-4.0-generate-001"``n`integerNumber of images to generate (1-4)`1``2``size`stringImage dimensions`"1024x1024"``"512x512"`, `"1024x1024"`

1. Create an account at [Google AI Studio](https://aistudio.google.com/)
2. Generate an API key from [API Keys section](https://aistudio.google.com/app/apikey)
3. Set your `GEMINI_API_KEY` environment variable
4. Start generating images using LiteLLM

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Google AI Studio Documentation](https://ai.google.dev/gemini-api/docs)
- [Imagen Model Overview](https://ai.google.dev/gemini-api/docs/imagen)
- [LiteLLM Image Generation Guide](https://docs.litellm.ai/docs/completion/image_generation)