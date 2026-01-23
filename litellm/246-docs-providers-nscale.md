---
title: Nscale (EU Sovereign) | liteLLM
url: https://docs.litellm.ai/docs/providers/nscale
source: sitemap
fetched_at: 2026-01-21T19:49:50.691331723-03:00
rendered_js: false
word_count: 200
summary: This document provides instructions for integrating Nscale's AI inference services with LiteLLM to perform text and image generation using the Python SDK or Proxy server.
tags:
    - nscale
    - litellm
    - text-generation
    - image-generation
    - api-integration
    - serverless-inference
    - python-sdk
category: guide
---

[https://docs.nscale.com/docs/inference/chat](https://docs.nscale.com/docs/inference/chat)

tip

**We support ALL Nscale models, just set `model=nscale/<any-model-on-nscale>` as a prefix when sending litellm requests**

PropertyDetailsDescriptionEuropean-domiciled full-stack AI cloud platform for LLMs and image generation.Provider Route on LiteLLM`nscale/`Supported Endpoints`/chat/completions`, `/images/generations`API Reference[Nscale docs](https://docs.nscale.com/docs/getting-started/overview)

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["NSCALE_API_KEY"]=""# your Nscale API key
```

## Explore Available Models[​](#explore-available-models "Direct link to Explore Available Models")

Explore our full list of text and multimodal AI models — all available at highly competitive pricing: 📚 [Full List of Models](https://docs.nscale.com/docs/inference/serverless-models/current)

## Key Features[​](#key-features "Direct link to Key Features")

- **EU Sovereign**: Full data sovereignty and compliance with European regulations
- **Ultra-Low Cost (starting at $0.01 / M tokens)**: Extremely competitive pricing for both text and image generation models
- **Production Grade**: Reliable serverless deployments with full isolation
- **No Setup Required**: Instant access to compute without infrastructure management
- **Full Control**: Your data remains private and isolated

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Text Generation[​](#text-generation "Direct link to Text Generation")

Nscale Text Generation

```
from litellm import completion
import os

os.environ["NSCALE_API_KEY"]=""# your Nscale API key
response = completion(
    model="nscale/meta-llama/Llama-4-Scout-17B-16E-Instruct",
    messages=[{"role":"user","content":"What is LiteLLM?"}]
)
print(response)
```

Nscale Text Generation - Streaming

```
from litellm import completion
import os

os.environ["NSCALE_API_KEY"]=""# your Nscale API key
stream = completion(
    model="nscale/meta-llama/Llama-4-Scout-17B-16E-Instruct",
    messages=[{"role":"user","content":"What is LiteLLM?"}],
    stream=True
)

for chunk in stream:
if chunk.choices[0].delta.content isnotNone:
print(chunk.choices[0].delta.content, end="")
```

### Image Generation[​](#image-generation "Direct link to Image Generation")

Nscale Image Generation

```
from litellm import image_generation
import os

os.environ["NSCALE_API_KEY"]=""# your Nscale API key
response = image_generation(
    model="nscale/stabilityai/stable-diffusion-xl-base-1.0",
    prompt="A beautiful sunset over mountains",
    n=1,
    size="1024x1024"
)
print(response)
```

## Usage - LiteLLM Proxy[​](#usage---litellm-proxy "Direct link to Usage - LiteLLM Proxy")

Add the following to your LiteLLM Proxy configuration file:

config.yaml

```
model_list:
-model_name: nscale/meta-llama/Llama-4-Scout-17B-16E-Instruct
litellm_params:
model: nscale/meta-llama/Llama-4-Scout-17B-16E-Instruct
api_key: os.environ/NSCALE_API_KEY
-model_name: nscale/meta-llama/Llama-3.3-70B-Instruct
litellm_params:
model: nscale/meta-llama/Llama-3.3-70B-Instruct
api_key: os.environ/NSCALE_API_KEY
-model_name: nscale/stabilityai/stable-diffusion-xl-base-1.0
litellm_params:
model: nscale/stabilityai/stable-diffusion-xl-base-1.0
api_key: os.environ/NSCALE_API_KEY
```

Start your LiteLLM Proxy server:

Start LiteLLM Proxy

```
litellm --config config.yaml

# RUNNING on http://0.0.0.0:4000
```

- OpenAI SDK
- LiteLLM SDK
- cURL

Nscale via Proxy - Non-streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Non-streaming response
response = client.chat.completions.create(
    model="nscale/meta-llama/Llama-4-Scout-17B-16E-Instruct",
    messages=[{"role":"user","content":"What is LiteLLM?"}]
)

print(response.choices[0].message.content)
```

## Getting Started[​](#getting-started "Direct link to Getting Started")

1. Create an account at [console.nscale.com](https://console.nscale.com)
2. Claim free credit
3. Create an API key in settings
4. Start making API calls using LiteLLM

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Nscale Documentation](https://docs.nscale.com/docs/getting-started/overview)
- [Blog: Sovereign Serverless](https://www.nscale.com/blog/sovereign-serverless-how-we-designed-full-isolation-without-sacrificing-performance)