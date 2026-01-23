---
title: Azure AI Image Editing | liteLLM
url: https://docs.litellm.ai/docs/providers/azure_ai_img_edit
source: sitemap
fetched_at: 2026-01-21T19:48:07.833933243-03:00
rendered_js: false
word_count: 261
summary: This document provides a comprehensive guide on using Azure AI's FLUX models for image editing via the LiteLLM SDK and Proxy Server. It covers configuration steps, model-specific details, and API parameters for modifying images based on text descriptions.
tags:
    - azure-ai
    - flux-models
    - image-editing
    - litellm
    - python-sdk
    - api-configuration
    - image-processing
category: guide
---

Azure AI provides powerful image editing capabilities using FLUX models from Black Forest Labs to modify existing images based on text descriptions.

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionAzure AI Image Editing uses FLUX models to modify existing images based on text prompts.Provider Route on LiteLLM`azure_ai/`Provider Doc[Azure AI FLUX Models ↗](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/black-forest-labs-flux-1-kontext-pro-and-flux1-1-pro-now-available-in-azure-ai-f/4434659)Supported Operations[`/images/edits`](#image-editing)

## Setup[​](#setup "Direct link to Setup")

### API Key & Base URL & API Version[​](#api-key--base-url--api-version "Direct link to API Key & Base URL & API Version")

```
# Set your Azure AI API credentials
import os
os.environ["AZURE_AI_API_KEY"]="your-api-key-here"
os.environ["AZURE_AI_API_BASE"]="your-azure-ai-endpoint"# e.g., https://your-endpoint.eastus2.inference.ai.azure.com/
os.environ["AZURE_AI_API_VERSION"]="2025-04-01-preview"# Example API version
```

Get your API key and endpoint from [Azure AI Studio](https://ai.azure.com/).

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model NameDescriptionCost per Image`azure_ai/FLUX.1-Kontext-pro`FLUX 1 Kontext Pro model with enhanced context understanding for editing$0.04

## Image Editing[​](#image-editing "Direct link to Image Editing")

### Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

- Basic Usage
- Async Usage
- Advanced Parameters

Basic Image Editing

```
import os
import base64
from pathlib import Path

import litellm

# Set your API credentials
os.environ["AZURE_AI_API_KEY"]="your-api-key-here"
os.environ["AZURE_AI_API_BASE"]="your-azure-ai-endpoint"
os.environ["AZURE_AI_API_VERSION"]="2025-04-01-preview"

# Edit an image with a prompt
response = litellm.image_edit(
    model="azure_ai/FLUX.1-Kontext-pro",
    image=open("path/to/your/image.png","rb"),
    prompt="Add a winter theme with snow and cold colors",
    api_base=os.environ["AZURE_AI_API_BASE"],
    api_key=os.environ["AZURE_AI_API_KEY"],
    api_version=os.environ["AZURE_AI_API_VERSION"]
)

img_base64 = response.data[0].get("b64_json")
img_bytes = base64.b64decode(img_base64)
path = Path("edited_image.png")
path.write_bytes(img_bytes)
```

### Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

#### 1. Configure your config.yaml[​](#1-configure-your-configyaml "Direct link to 1. Configure your config.yaml")

Azure AI Image Editing Configuration

```
model_list:
-model_name: azure-flux-kontext-edit
litellm_params:
model: azure_ai/FLUX.1-Kontext-pro
api_key: os.environ/AZURE_AI_API_KEY
api_base: os.environ/AZURE_AI_API_BASE
api_version: os.environ/AZURE_AI_API_VERSION
model_info:
mode: image_edit

general_settings:
master_key: sk-1234
```

#### 2. Start LiteLLM Proxy Server[​](#2-start-litellm-proxy-server "Direct link to 2. Start LiteLLM Proxy Server")

Start LiteLLM Proxy Server

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

#### 3. Make image editing requests with OpenAI Python SDK[​](#3-make-image-editing-requests-with-openai-python-sdk "Direct link to 3. Make image editing requests with OpenAI Python SDK")

- OpenAI SDK
- LiteLLM SDK
- cURL

Azure AI Image Editing via Proxy - OpenAI SDK

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="sk-1234"# Your proxy API key
)

# Edit image with FLUX Kontext Pro
response = client.images.edit(
    model="azure-flux-kontext-edit",
    image=open("path/to/your/image.png","rb"),
    prompt="Transform this image into a beautiful oil painting style",
)

img_base64 = response.data[0].b64_json
img_bytes = base64.b64decode(img_base64)
path = Path("proxy_edited_image.png")
path.write_bytes(img_bytes)
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

Azure AI Image Editing supports the following OpenAI-compatible parameters:

ParameterTypeDescriptionDefaultExample`image`fileThe image file to editRequiredFile object or binary data`prompt`stringText description of the desired changesRequired`"Add snow and winter elements"``model`stringThe FLUX model to use for editingRequired`"azure_ai/FLUX.1-Kontext-pro"``n`integerNumber of edited images to generate (You can specify only 1)`1``1``api_base`stringYour Azure AI endpoint URLRequired`"https://your-endpoint.eastus2.inference.ai.azure.com/"``api_key`stringYour Azure AI API keyRequiredEnvironment variable or direct value`api_version`stringAPI version for Azure AIRequired`"2025-04-01-preview"`

## Getting Started[​](#getting-started "Direct link to Getting Started")

1. Create an account at [Azure AI Studio](https://ai.azure.com/)
2. Deploy a FLUX model in your Azure AI Studio workspace
3. Get your API key and endpoint from the deployment details
4. Set your `AZURE_AI_API_KEY`, `AZURE_AI_API_BASE` and `AZURE_AI_API_VERSION` environment variables
5. Prepare your source image
6. Use `litellm.image_edit()` to modify your images with text instructions

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Azure AI Studio Documentation](https://docs.microsoft.com/en-us/azure/ai-services/)
- [FLUX Models Announcement](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/black-forest-labs-flux-1-kontext-pro-and-flux1-1-pro-now-available-in-azure-ai-f/4434659)