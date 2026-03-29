---
title: Apertis AI (Stima API) | liteLLM
url: https://docs.litellm.ai/docs/providers/apertis
source: sitemap
fetched_at: 2026-01-21T19:48:01.029813253-03:00
rendered_js: false
word_count: 256
summary: This document provides an overview and integration guide for Apertis AI, detailing how to access over 430 AI models using the LiteLLM Python SDK and proxy server.
tags:
    - apertis-ai
    - stima-api
    - litellm
    - api-integration
    - llm-models
    - python-usage
category: api
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionApertis AI (formerly Stima API) is a unified API platform providing access to 430+ AI models through a single interface, with cost savings of up to 50%.Provider Route on LiteLLM`apertis/`Link to Provider Doc[Apertis AI Website ↗](https://api.stima.tech)Base URL`https://api.stima.tech/v1`Supported Operations[`/chat/completions`](#sample-usage)

## What is Apertis AI?[​](#what-is-apertis-ai "Direct link to What is Apertis AI?")

Apertis AI is a unified API platform that lets developers:

- **Access 430+ AI Models**: All models through a single API
- **Save 50% on Costs**: Competitive pricing with significant discounts
- **Unified Billing**: Single bill for all model usage
- **Quick Setup**: Start with just $2 registration
- **GitHub Integration**: Link with your GitHub account

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["STIMA_API_KEY"]=""# your Apertis AI API key
```

Get your Apertis AI API key from [api.stima.tech](https://api.stima.tech).

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

Apertis AI Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["STIMA_API_KEY"]=""# your Apertis AI API key

messages =[{"content":"What is the capital of France?","role":"user"}]

# Apertis AI call
response = completion(
    model="apertis/model-name",# Replace with actual model name
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

Apertis AI Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["STIMA_API_KEY"]=""# your Apertis AI API key

messages =[{"content":"Write a short poem about AI","role":"user"}]

# Apertis AI call with streaming
response = completion(
    model="apertis/model-name",# Replace with actual model name
    messages=messages,
    stream=True
)

for chunk in response:
print(chunk)
```

## Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

### 1. Save key in your environment[​](#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
model_list:
-model_name: apertis-model
litellm_params:
model: apertis/model-name  # Replace with actual model name
api_key: os.environ/STIMA_API_KEY
```

## Supported OpenAI Parameters[​](#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

Apertis AI supports all standard OpenAI-compatible parameters:

ParameterTypeDescription`messages`array**Required**. Array of message objects with 'role' and 'content'`model`string**Required**. Model ID from 430+ available models`stream`booleanOptional. Enable streaming responses`temperature`floatOptional. Sampling temperature`top_p`floatOptional. Nucleus sampling parameter`max_tokens`integerOptional. Maximum tokens to generate`frequency_penalty`floatOptional. Penalize frequent tokens`presence_penalty`floatOptional. Penalize tokens based on presence`stop`string/arrayOptional. Stop sequences`tools`arrayOptional. List of available tools/functions`tool_choice`string/objectOptional. Control tool/function calling

## Cost Benefits[​](#cost-benefits "Direct link to Cost Benefits")

Apertis AI offers significant cost advantages:

- **50% Cost Savings**: Save money compared to direct provider costs
- **Unified Billing**: Single invoice for all your AI model usage
- **Low Entry**: Start with just $2 registration

## Model Availability[​](#model-availability "Direct link to Model Availability")

With access to 430+ AI models, Apertis AI provides:

- Multiple providers through one API
- Latest model releases
- Various model types (text, image, video)

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Apertis AI Website](https://api.stima.tech)
- [Apertis AI Enterprise](https://api.stima.tech/enterprise)