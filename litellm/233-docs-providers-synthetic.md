---
title: Synthetic | liteLLM
url: https://docs.litellm.ai/docs/providers/synthetic
source: sitemap
fetched_at: 2026-01-21T19:50:28.466357107-03:00
rendered_js: false
word_count: 203
summary: This document provides instructions for integrating Synthetic's privacy-focused AI models with LiteLLM, covering environment setup, Python SDK usage, and proxy server configuration.
tags:
    - synthetic
    - litellm
    - ai-integration
    - privacy-first
    - python-sdk
    - llm-proxy
    - api-configuration
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionSynthetic runs open-source AI models in secure datacenters within the US and EU, with a focus on privacy. They never train on your data and auto-delete API data within 14 days.Provider Route on LiteLLM`synthetic/`Link to Provider Doc[Synthetic Website ↗](https://synthetic.new)Base URL`https://api.synthetic.new/openai/v1`Supported Operations[`/chat/completions`](#sample-usage)

## What is Synthetic?[​](#what-is-synthetic "Direct link to What is Synthetic?")

Synthetic is a privacy-focused AI platform that provides access to open-source LLMs with the following guarantees:

- **Privacy-First**: Data never used for training
- **Secure Hosting**: Models run in secure datacenters in US and EU
- **Auto-Deletion**: API data automatically deleted within 14 days
- **Open Source**: Runs open-source AI models

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["SYNTHETIC_API_KEY"]=""# your Synthetic API key
```

Get your Synthetic API key from [synthetic.new](https://synthetic.new).

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

Synthetic Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["SYNTHETIC_API_KEY"]=""# your Synthetic API key

messages =[{"content":"What is the capital of France?","role":"user"}]

# Synthetic call
response = completion(
    model="synthetic/model-name",# Replace with actual model name
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

Synthetic Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["SYNTHETIC_API_KEY"]=""# your Synthetic API key

messages =[{"content":"Write a short poem about AI","role":"user"}]

# Synthetic call with streaming
response = completion(
    model="synthetic/model-name",# Replace with actual model name
    messages=messages,
    stream=True
)

for chunk in response:
print(chunk)
```

## Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

### 1. Save key in your environment[​](#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

```
export SYNTHETIC_API_KEY=""
```

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
model_list:
-model_name: synthetic-model
litellm_params:
model: synthetic/model-name  # Replace with actual model name
api_key: os.environ/SYNTHETIC_API_KEY
```

## Supported OpenAI Parameters[​](#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

Synthetic supports all standard OpenAI-compatible parameters:

ParameterTypeDescription`messages`array**Required**. Array of message objects with 'role' and 'content'`model`string**Required**. Model ID`stream`booleanOptional. Enable streaming responses`temperature`floatOptional. Sampling temperature`top_p`floatOptional. Nucleus sampling parameter`max_tokens`integerOptional. Maximum tokens to generate`frequency_penalty`floatOptional. Penalize frequent tokens`presence_penalty`floatOptional. Penalize tokens based on presence`stop`string/arrayOptional. Stop sequences

## Privacy & Security[​](#privacy--security "Direct link to Privacy & Security")

Synthetic provides enterprise-grade privacy protections:

- Data auto-deleted within 14 days
- No data used for model training
- Secure hosting in US and EU datacenters
- Compliance-friendly architecture

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Synthetic Website](https://synthetic.new)