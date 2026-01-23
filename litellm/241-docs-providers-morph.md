---
title: Morph | liteLLM
url: https://docs.litellm.ai/docs/providers/morph
source: sitemap
fetched_at: 2026-01-21T19:49:43.740217475-03:00
rendered_js: false
word_count: 114
summary: This document explains how to integrate and use Morph AI models with LiteLLM, covering environment setup, basic and streaming usage, and proxy server configuration.
tags:
    - litellm
    - morph-ai
    - api-integration
    - python-sdk
    - llm-proxy
    - model-deployment
category: guide
---

LiteLLM supports all models on [Morph](https://morphllm.com)

## Overview[​](#overview "Direct link to Overview")

Morph provides specialized AI models designed for agentic workflows, particularly excelling at precise code editing and manipulation. Their "Apply" models enable targeted code changes without full file rewrites, making them ideal for AI agents that need to make intelligent, context-aware code modifications.

## API Key[​](#api-key "Direct link to API Key")

```
import os 
os.environ["MORPH_API_KEY"]="your-api-key"
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion

# set env variable 
os.environ["MORPH_API_KEY"]="your-api-key"

messages =[
{"role":"user","content":"Write a Python function to calculate factorial"}
]

## Morph v3 Fast - Optimized for speed
response = completion(
    model="morph/morph-v3-fast",
    messages=messages,
)
print(response)

## Morph v3 Large - Most capable model
response = completion(
    model="morph/morph-v3-large",
    messages=messages,
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion

# set env variable
os.environ["MORPH_API_KEY"]="your-api-key"

messages =[
{"role":"user","content":"Write a Python function to calculate factorial"}
]

## Morph v3 Fast with streaming
response = completion(
    model="morph/morph-v3-fast",
    messages=messages,
    stream=True,
)

for chunk in response:
print(chunk)
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model NameFunction CallDescriptionContext Windowmorph-v3-fast`completion('morph/morph-v3-fast', messages)`Fastest model, optimized for quick responses16k tokensmorph-v3-large`completion('morph/morph-v3-large', messages)`Most capable model for complex tasks16k tokens

## Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

Here's how to use Morph with the LiteLLM Proxy Server:

1. Save API key in your environment

```
export MORPH_API_KEY="your-api-key"
```

2. Add model to config.yaml

```
model_list:
-model_name: morph-v3-fast
litellm_params:
model: morph/morph-v3-fast

-model_name: morph-v3-large
litellm_params:
model: morph/morph-v3-large
```

3. Start the proxy server

```
litellm --config config.yaml
```

## Advanced Usage[​](#advanced-usage "Direct link to Advanced Usage")

### Setting API Base[​](#setting-api-base "Direct link to Setting API Base")

```
import litellm 

# set custom api base
response = completion(
    model="morph/morph-v3-large",
    messages=[{"role":"user","content":"Hello, world!"}],
    api_base="https://api.morphllm.com/v1"
)
print(response)
```

### Setting API Key[​](#setting-api-key "Direct link to Setting API Key")

```
import litellm 

# set api key via completion
response = completion(
    model="morph/morph-v3-large",
    messages=[{"role":"user","content":"Hello, world!"}],
    api_key="your-api-key"
)
print(response)
```