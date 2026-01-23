---
title: NanoGPT | liteLLM
url: https://docs.litellm.ai/docs/providers/nano-gpt
source: sitemap
fetched_at: 2026-01-21T19:49:47.685350912-03:00
rendered_js: false
word_count: 282
summary: This document provides instructions for integrating the NanoGPT model provider with LiteLLM, covering environment setup, Python SDK usage, and proxy server configuration.
tags:
    - nanogpt
    - litellm
    - openai-compatible
    - api-integration
    - python-sdk
    - llm-provider
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionNanoGPT is a pay-per-prompt and subscription based AI service providing instant access to over 200+ powerful AI models with no subscriptions or registration required.Provider Route on LiteLLM`nano-gpt/`Link to Provider Doc[NanoGPT Website ↗](https://nano-gpt.com)Base URL`https://nano-gpt.com/api/v1`Supported Operations[`/chat/completions`](#sample-usage), [`/completions`](#text-completion), [`/embeddings`](#embeddings)

## What is NanoGPT?[​](#what-is-nanogpt "Direct link to What is NanoGPT?")

NanoGPT is a flexible AI API service that offers:

- **Pay-Per-Prompt Pricing**: No subscriptions, pay only for what you use
- **200+ AI Models**: Access to text, image, and video generation models
- **No Registration Required**: Get started instantly
- **OpenAI-Compatible API**: Easy integration with existing code
- **Streaming Support**: Real-time response streaming
- **Tool Calling**: Support for function calling

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["NANOGPT_API_KEY"]=""# your NanoGPT API key
```

Get your NanoGPT API key from [nano-gpt.com](https://nano-gpt.com).

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

NanoGPT Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["NANOGPT_API_KEY"]=""# your NanoGPT API key

messages =[{"content":"What is the capital of France?","role":"user"}]

# NanoGPT call
response = completion(
    model="nano-gpt/model-name",# Replace with actual model name
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

NanoGPT Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["NANOGPT_API_KEY"]=""# your NanoGPT API key

messages =[{"content":"Write a short poem about AI","role":"user"}]

# NanoGPT call with streaming
response = completion(
    model="nano-gpt/model-name",# Replace with actual model name
    messages=messages,
    stream=True
)

for chunk in response:
print(chunk)
```

### Tool Calling[​](#tool-calling "Direct link to Tool Calling")

NanoGPT Tool Calling

```
import os
import litellm

os.environ["NANOGPT_API_KEY"]=""

tools =[
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get current weather",
"parameters":{
"type":"object",
"properties":{
"location":{"type":"string"}
}
}
}
}
]

response = litellm.completion(
    model="nano-gpt/model-name",
    messages=[{"role":"user","content":"What's the weather in Paris?"}],
    tools=tools
)
```

## Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

### 1. Save key in your environment[​](#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

```
export NANOGPT_API_KEY=""
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
model_list:
-model_name: nano-gpt-model
litellm_params:
model: nano-gpt/model-name  # Replace with actual model name
api_key: os.environ/NANOGPT_API_KEY
```

## Supported OpenAI Parameters[​](#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

NanoGPT supports all standard OpenAI-compatible parameters:

ParameterTypeDescription`messages`array**Required**. Array of message objects with 'role' and 'content'`model`string**Required**. Model ID from 200+ available models`stream`booleanOptional. Enable streaming responses`temperature`floatOptional. Sampling temperature`top_p`floatOptional. Nucleus sampling parameter`max_tokens`integerOptional. Maximum tokens to generate`frequency_penalty`floatOptional. Penalize frequent tokens`presence_penalty`floatOptional. Penalize tokens based on presence`stop`string/arrayOptional. Stop sequences`n`integerOptional. Number of completions to generate`tools`arrayOptional. List of available tools/functions`tool_choice`string/objectOptional. Control tool/function calling`response_format`objectOptional. Response format specification`user`stringOptional. User identifier

## Model Categories[​](#model-categories "Direct link to Model Categories")

NanoGPT provides access to multiple model categories:

- **Text Generation**: 200+ LLMs for chat, completion, and analysis
- **Image Generation**: AI models for creating images
- **Video Generation**: AI models for video creation
- **Embedding Models**: Text embedding models for vector search

## Pricing Model[​](#pricing-model "Direct link to Pricing Model")

NanoGPT offers a flexible pricing structure:

- **Pay-Per-Prompt**: No subscription required
- **No Registration**: Get started immediately
- **Transparent Pricing**: Pay only for what you use

## API Documentation[​](#api-documentation "Direct link to API Documentation")

For detailed API documentation, visit [docs.nano-gpt.com](https://docs.nano-gpt.com).

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [NanoGPT Website](https://nano-gpt.com)
- [NanoGPT API Documentation](https://nano-gpt.com/api)
- [NanoGPT Model List](https://docs.nano-gpt.com/api-reference/endpoint/models)