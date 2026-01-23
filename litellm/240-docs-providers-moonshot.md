---
title: Moonshot AI | liteLLM
url: https://docs.litellm.ai/docs/providers/moonshot
source: sitemap
fetched_at: 2026-01-21T19:49:43.740541068-03:00
rendered_js: false
word_count: 257
summary: This document explains how to integrate and use Moonshot AI models with LiteLLM through the Python SDK and proxy, including configuration steps and automated limitation handling.
tags:
    - moonshot-ai
    - litellm
    - python-sdk
    - api-integration
    - llm-proxy
    - streaming
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionMoonshot AI provides large language models including the moonshot-v1 series and kimi models.Provider Route on LiteLLM`moonshot/`Link to Provider Doc[Moonshot AI ↗](https://platform.moonshot.ai/)Base URL`https://api.moonshot.ai/`Supported Operations[`/chat/completions`](#sample-usage)

[https://platform.moonshot.ai/](https://platform.moonshot.ai/)

**We support ALL Moonshot AI models, just set `moonshot/` as a prefix when sending completion requests**

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["MOONSHOT_API_KEY"]=""# your Moonshot AI API key
```

**ATTENTION:**

Moonshot AI offers two distinct API endpoints: a global one and a China-specific one.

- Global API Base URL: `https://api.moonshot.ai/v1` (This is the one currently implemented)
- China API Base URL: `https://api.moonshot.cn/v1`

You can overwrite the base url with:

```
os.environ["MOONSHOT_API_BASE"] = "https://api.moonshot.cn/v1"
```

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

Moonshot Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["MOONSHOT_API_KEY"]=""# your Moonshot AI API key

messages =[{"content":"Hello, how are you?","role":"user"}]

# Moonshot call
response = completion(
    model="moonshot/moonshot-v1-8k",
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

Moonshot Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["MOONSHOT_API_KEY"]=""# your Moonshot AI API key

messages =[{"content":"Hello, how are you?","role":"user"}]

# Moonshot call with streaming
response = completion(
    model="moonshot/moonshot-v1-8k",
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
-model_name: moonshot-v1-8k
litellm_params:
model: moonshot/moonshot-v1-8k
api_key: os.environ/MOONSHOT_API_KEY

-model_name: moonshot-v1-32k
litellm_params:
model: moonshot/moonshot-v1-32k
api_key: os.environ/MOONSHOT_API_KEY

-model_name: moonshot-v1-128k
litellm_params:
model: moonshot/moonshot-v1-128k
api_key: os.environ/MOONSHOT_API_KEY
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

Moonshot via Proxy - Non-streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Non-streaming response
response = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[{"role":"user","content":"hello from litellm"}]
)

print(response.choices[0].message.content)
```

Moonshot via Proxy - Streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Streaming response
response = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[{"role":"user","content":"hello from litellm"}],
    stream=True
)

for chunk in response:
if chunk.choices[0].delta.content isnotNone:
print(chunk.choices[0].delta.content, end="")
```

For more detailed information on using the LiteLLM Proxy, see the [LiteLLM Proxy documentation](https://docs.litellm.ai/docs/providers/litellm_proxy).

## Moonshot AI Limitations & LiteLLM Handling[​](#moonshot-ai-limitations--litellm-handling "Direct link to Moonshot AI Limitations & LiteLLM Handling")

LiteLLM automatically handles the following [Moonshot AI limitations](https://platform.moonshot.ai/docs/guide/migrating-from-openai-to-kimi#about-api-compatibility) to provide seamless OpenAI compatibility:

### Temperature Range Limitation[​](#temperature-range-limitation "Direct link to Temperature Range Limitation")

**Limitation**: Moonshot AI only supports temperature range \[0, 1] (vs OpenAI's \[0, 2])  
**LiteLLM Handling**: Automatically clamps any temperature &gt; 1 to 1

### Temperature + Multiple Outputs Limitation[​](#temperature--multiple-outputs-limitation "Direct link to Temperature + Multiple Outputs Limitation")

**Limitation**: If temperature &lt; 0.3 and n &gt; 1, Moonshot AI raises an exception  
**LiteLLM Handling**: Automatically sets temperature to 0.3 when this condition is detected

### Tool Choice "Required" Not Supported[​](#tool-choice-required-not-supported 'Direct link to Tool Choice "Required" Not Supported')

**Limitation**: Moonshot AI doesn't support `tool_choice="required"`  
**LiteLLM Handling**: Converts this by:

- Adding message: "Please select a tool to handle the current issue."
- Removing the `tool_choice` parameter from the request