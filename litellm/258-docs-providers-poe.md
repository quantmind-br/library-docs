---
title: Poe | liteLLM
url: https://docs.litellm.ai/docs/providers/poe
source: sitemap
fetched_at: 2026-01-21T19:50:09.55242852-03:00
rendered_js: false
word_count: 309
summary: This document explains how to integrate and use Quora's Poe AI platform with LiteLLM, covering environment setup, Python SDK usage, and proxy server configuration.
tags:
    - poe-api
    - litellm-integration
    - python-sdk
    - proxy-server
    - ai-models
    - environment-variables
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionPoe is Quora's AI platform that provides access to more than 100 models across text, image, video, and voice modalities through a developer-friendly API.Provider Route on LiteLLM`poe/`Link to Provider Doc[Poe Website ↗](https://poe.com)Base URL`https://api.poe.com/v1`Supported Operations[`/chat/completions`](#sample-usage)

## What is Poe?[​](#what-is-poe "Direct link to What is Poe?")

Poe is Quora's comprehensive AI platform that offers:

- **100+ Models**: Access to a wide variety of AI models
- **Multiple Modalities**: Text, image, video, and voice AI
- **Popular Models**: Including OpenAI's GPT series and Anthropic's Claude
- **Developer API**: Easy integration for applications
- **Extensive Reach**: Benefits from Quora's 400M monthly unique visitors

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["POE_API_KEY"]=""# your Poe API key
```

Get your Poe API key from the [Poe platform](https://poe.com).

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

Poe Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["POE_API_KEY"]=""# your Poe API key

messages =[{"content":"What is the capital of France?","role":"user"}]

# Poe call
response = completion(
    model="poe/model-name",# Replace with actual model name
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

Poe Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["POE_API_KEY"]=""# your Poe API key

messages =[{"content":"Write a short poem about AI","role":"user"}]

# Poe call with streaming
response = completion(
    model="poe/model-name",# Replace with actual model name
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
-model_name: poe-model
litellm_params:
model: poe/model-name  # Replace with actual model name
api_key: os.environ/POE_API_KEY
```

## Supported OpenAI Parameters[​](#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

Poe supports all standard OpenAI-compatible parameters:

ParameterTypeDescription`messages`array**Required**. Array of message objects with 'role' and 'content'`model`string**Required**. Model ID from 100+ available models`stream`booleanOptional. Enable streaming responses`temperature`floatOptional. Sampling temperature`top_p`floatOptional. Nucleus sampling parameter`max_tokens`integerOptional. Maximum tokens to generate`frequency_penalty`floatOptional. Penalize frequent tokens`presence_penalty`floatOptional. Penalize tokens based on presence`stop`string/arrayOptional. Stop sequences`tools`arrayOptional. List of available tools/functions`tool_choice`string/objectOptional. Control tool/function calling`response_format`objectOptional. Response format specification`user`stringOptional. User identifier

## Available Model Categories[​](#available-model-categories "Direct link to Available Model Categories")

Poe provides access to models across multiple providers:

- **OpenAI Models**: Including GPT-4, GPT-4 Turbo, GPT-3.5 Turbo
- **Anthropic Models**: Including Claude 3 Opus, Sonnet, Haiku
- **Other Popular Models**: Various provider models available
- **Multi-Modal**: Text, image, video, and voice models

## Platform Benefits[​](#platform-benefits "Direct link to Platform Benefits")

Using Poe through LiteLLM offers several advantages:

- **Unified Access**: Single API for many different models
- **Quora Integration**: Access to large user base and content ecosystem
- **Content Sharing**: Capabilities to share model outputs with followers
- **Content Distribution**: Best AI content distributed to all users
- **Model Discovery**: Efficient way to explore new AI models

## Developer Resources[​](#developer-resources "Direct link to Developer Resources")

Poe is actively building developer features and welcomes early access requests for API integration.

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Poe Website](https://poe.com)
- [Poe AI Quora Space](https://poeai.quora.com)
- [Quora Blog Post about Poe](https://quorablog.quora.com/Poe)