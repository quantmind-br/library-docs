---
title: Azure AI Image Generation (Black Forest Labs - Flux) | liteLLM
url: https://docs.litellm.ai/docs/providers/azure_ai_img
source: sitemap
fetched_at: 2026-01-21T19:48:06.853564813-03:00
rendered_js: false
word_count: 304
summary: This document provides a comprehensive guide for integrating Azure AI FLUX models for image generation and editing using the LiteLLM Python SDK and Proxy server. It includes configuration steps, supported model details, and code examples for both basic and advanced image operations.
tags:
    - azure-ai
    - flux-models
    - image-generation
    - litellm
    - image-editing
    - python-sdk
    - api-configuration
category: guide
---

Azure AI provides powerful image generation capabilities using FLUX models from Black Forest Labs to create high-quality images from text descriptions.

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionAzure AI Image Generation uses FLUX models to generate high-quality images from text descriptions.Provider Route on LiteLLM`azure_ai/`Provider Doc[Azure AI FLUX Models ↗](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/black-forest-labs-flux-1-kontext-pro-and-flux1-1-pro-now-available-in-azure-ai-f/4434659)Supported Operations[`/images/generations`](#image-generation), [`/images/edits`](#image-editing)

## Setup[​](#setup "Direct link to Setup")

### API Key & Base URL[​](#api-key--base-url "Direct link to API Key & Base URL")

```
# Set your Azure AI API credentials
import os
os.environ["AZURE_AI_API_KEY"]="your-api-key-here"
os.environ["AZURE_AI_API_BASE"]="your-azure-ai-endpoint"# e.g., https://your-endpoint.eastus2.inference.ai.azure.com/
```

Get your API key and endpoint from [Azure AI Studio](https://ai.azure.com/).

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model NameDescriptionCost per Image`azure_ai/FLUX-1.1-pro`Latest FLUX 1.1 Pro model for high-quality image generation$0.04`azure_ai/FLUX.1-Kontext-pro`FLUX 1 Kontext Pro model with enhanced context understanding$0.04`azure_ai/flux.2-pro`FLUX 2 Pro model for next-generation image generation$0.04

## Image Generation[​](#image-generation "Direct link to Image Generation")

### Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

- Basic Usage
- FLUX 1.1 Pro
- FLUX 2 Pro
- Async Usage
- Advanced Parameters

Basic Image Generation

```
import litellm
import os

# Set your API credentials
os.environ["AZURE_AI_API_KEY"]="your-api-key-here"
os.environ["AZURE_AI_API_BASE"]="your-azure-ai-endpoint"

# Generate a single image
response = litellm.image_generation(
    model="azure_ai/FLUX.1-Kontext-pro",
    prompt="A cute baby sea otter swimming in crystal clear water",
    api_base=os.environ["AZURE_AI_API_BASE"],
    api_key=os.environ["AZURE_AI_API_KEY"]
)

print(response.data[0].url)
```

### Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

#### 1. Configure your config.yaml[​](#1-configure-your-configyaml "Direct link to 1. Configure your config.yaml")

Azure AI Image Generation Configuration

```
model_list:
-model_name: azure-flux-kontext
litellm_params:
model: azure_ai/FLUX.1-Kontext-pro
api_key: os.environ/AZURE_AI_API_KEY
api_base: os.environ/AZURE_AI_API_BASE
model_info:
mode: image_generation

-model_name: azure-flux-11-pro
litellm_params:
model: azure_ai/FLUX-1.1-pro
api_key: os.environ/AZURE_AI_API_KEY
api_base: os.environ/AZURE_AI_API_BASE
model_info:
mode: image_generation

-model_name: azure-flux-2-pro
litellm_params:
model: azure_ai/flux.2-pro
api_key: os.environ/AZURE_AI_API_KEY
api_base: os.environ/AZURE_AI_API_BASE
api_version: preview
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

Azure AI Image Generation via Proxy - OpenAI SDK

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="sk-1234"# Your proxy API key
)

# Generate image with FLUX Kontext Pro
response = client.images.generate(
    model="azure-flux-kontext",
    prompt="A serene Japanese garden with cherry blossoms and a peaceful pond",
    n=1,
    size="1024x1024"
)

print(response.data[0].url)
```

## Image Editing[​](#image-editing "Direct link to Image Editing")

FLUX 2 Pro supports image editing by passing an input image along with a prompt describing the desired modifications.

### Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk-1 "Direct link to Usage - LiteLLM Python SDK")

- Basic Image Edit
- Async Image Edit

Basic Image Editing with FLUX 2 Pro

```
import litellm
import os

# Set your API credentials
os.environ["AZURE_AI_API_KEY"]="your-api-key-here"
os.environ["AZURE_AI_API_BASE"]="your-azure-ai-endpoint"# e.g., https://litellm-ci-cd-prod.services.ai.azure.com

# Edit an existing image
response = litellm.image_edit(
    model="azure_ai/flux.2-pro",
    prompt="Add a red hat to the subject",
    image=open("input_image.png","rb"),
    api_base=os.environ["AZURE_AI_API_BASE"],
    api_key=os.environ["AZURE_AI_API_KEY"],
    api_version="preview",
)

print(response.data[0].b64_json)# FLUX 2 returns base64 encoded images
```

### Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server-1 "Direct link to Usage - LiteLLM Proxy Server")

- cURL
- OpenAI SDK

Image Edit via Proxy - cURL

```
curl --location 'http://localhost:4000/v1/images/edits' \
--header 'Authorization: Bearer sk-1234' \
--form 'model="azure-flux-2-pro"' \
--form 'prompt="Add sunglasses to the person"' \
--form 'image=@"input_image.png"'
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

Azure AI Image Generation supports the following OpenAI-compatible parameters:

ParameterTypeDescriptionDefaultExample`prompt`stringText description of the image to generateRequired`"A sunset over the ocean"``model`stringThe FLUX model to use for generationRequired`"azure_ai/FLUX.1-Kontext-pro"``n`integerNumber of images to generate (1-4)`1``2``size`stringImage dimensions`"1024x1024"``"512x512"`, `"1024x1024"``api_base`stringYour Azure AI endpoint URLRequired`"https://your-endpoint.eastus2.inference.ai.azure.com/"``api_key`stringYour Azure AI API keyRequiredEnvironment variable or direct value

## Getting Started[​](#getting-started "Direct link to Getting Started")

1. Create an account at [Azure AI Studio](https://ai.azure.com/)
2. Deploy a FLUX model in your Azure AI Studio workspace
3. Get your API key and endpoint from the deployment details
4. Set your `AZURE_AI_API_KEY` and `AZURE_AI_API_BASE` environment variables
5. Start generating images using LiteLLM

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Azure AI Studio Documentation](https://docs.microsoft.com/en-us/azure/ai-services/)
- [FLUX Models Announcement](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/black-forest-labs-flux-1-kontext-pro-and-flux1-1-pro-now-available-in-azure-ai-f/4434659)