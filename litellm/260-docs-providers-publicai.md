---
title: PublicAI | liteLLM
url: https://docs.litellm.ai/docs/providers/publicai
source: sitemap
fetched_at: 2026-01-21T19:50:09.868431476-03:00
rendered_js: false
word_count: 114
summary: This document provides instructions for integrating PublicAI models into LiteLLM using the Python SDK or the LiteLLM Proxy. It details the required environment variables, model prefixes, and configuration steps for both streaming and non-streaming requests.
tags:
    - publicai
    - litellm
    - python-sdk
    - llm-api
    - streaming
    - proxy-configuration
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionPublicAI provides large language models including essential models like the swiss-ai apertus model.Provider Route on LiteLLM`publicai/`Link to Provider Doc[PublicAI ↗](https://platform.publicai.co/)Base URL`https://platform.publicai.co/`Supported Operations[`/chat/completions`](#sample-usage)

[https://platform.publicai.co/](https://platform.publicai.co/)

**We support ALL PublicAI models, just set `publicai/` as a prefix when sending completion requests**

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["PUBLICAI_API_KEY"]=""# your PublicAI API key
```

You can overwrite the base url with:

```
os.environ["PUBLICAI_API_BASE"] = "https://platform.publicai.co/v1"
```

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

PublicAI Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["PUBLICAI_API_KEY"]=""# your PublicAI API key

messages =[{"content":"Hello, how are you?","role":"user"}]

# PublicAI call
response = completion(
    model="publicai/swiss-ai/apertus-8b-instruct",
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

PublicAI Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["PUBLICAI_API_KEY"]=""# your PublicAI API key

messages =[{"content":"Hello, how are you?","role":"user"}]

# PublicAI call with streaming
response = completion(
    model="publicai/swiss-ai/apertus-8b-instruct",
    messages=messages,
    stream=True
)

for chunk in response:
print(chunk)
```

## Usage - LiteLLM Proxy[​](#usage---litellm-proxy "Direct link to Usage - LiteLLM Proxy")

Add the following to your LiteLLM Proxy configuration file:

config.yaml

```
model_list:
-model_name: swiss-ai-apertus-8b
litellm_params:
model: publicai/swiss-ai/apertus-8b-instruct
api_key: os.environ/PUBLICAI_API_KEY

-model_name: swiss-ai-apertus-70b
litellm_params:
model: publicai/swiss-ai/apertus-70b-instruct
api_key: os.environ/PUBLICAI_API_KEY
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

PublicAI via Proxy - Non-streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Non-streaming response
response = client.chat.completions.create(
    model="swiss-ai-apertus-8b",
    messages=[{"role":"user","content":"hello from litellm"}]
)

print(response.choices[0].message.content)
```

PublicAI via Proxy - Streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Streaming response
response = client.chat.completions.create(
    model="swiss-ai-apertus-8b",
    messages=[{"role":"user","content":"hello from litellm"}],
    stream=True
)

for chunk in response:
if chunk.choices[0].delta.content isnotNone:
print(chunk.choices[0].delta.content, end="")
```

For more detailed information on using the LiteLLM Proxy, see the [LiteLLM Proxy documentation](https://docs.litellm.ai/docs/providers/litellm_proxy).