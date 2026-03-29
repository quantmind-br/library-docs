---
title: Vercel AI Gateway | liteLLM
url: https://docs.litellm.ai/docs/providers/vercel_ai_gateway
source: sitemap
fetched_at: 2026-01-21T19:50:36.222528276-03:00
rendered_js: false
word_count: 156
summary: This document explains how to integrate LiteLLM with Vercel AI Gateway to access multiple AI providers through a unified interface. It covers authentication setup, environment variable configuration, and implementation via both the Python SDK and the LiteLLM Proxy.
tags:
    - vercel-ai-gateway
    - litellm
    - api-integration
    - python-sdk
    - llm-proxy
    - environment-variables
category: reference
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionVercel AI Gateway provides a unified interface to access multiple AI providers through a single endpoint, with built-in caching, rate limiting, and analytics.Provider Route on LiteLLM`vercel_ai_gateway/`Link to Provider Doc[Vercel AI Gateway Documentation ↗](https://vercel.com/docs/ai-gateway)Base URL`https://ai-gateway.vercel.sh/v1`Supported Operations`/chat/completions`, `/models`

[https://vercel.com/docs/ai-gateway](https://vercel.com/docs/ai-gateway)

**We support ALL models available through Vercel AI Gateway, just set `vercel_ai_gateway/` as a prefix when sending completion requests**

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["VERCEL_AI_GATEWAY_API_KEY"]=""# your Vercel AI Gateway API key
# OR
os.environ["VERCEL_OIDC_TOKEN"]=""# your Vercel OIDC token for authentication
```

## Optional Variables[​](#optional-variables "Direct link to Optional Variables")

Environment Variables

```
os.environ["VERCEL_SITE_URL"]=""# your site url
# OR
os.environ["VERCEL_APP_NAME"]=""# your app name
```

Note: see the [Vercel AI Gateway docs](https://vercel.com/docs/ai-gateway#using-the-ai-gateway-with-an-api-key) for instructions on obtaining a key.

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

Vercel AI Gateway Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["VERCEL_AI_GATEWAY_API_KEY"]="your-api-key"

messages =[{"content":"Hello, how are you?","role":"user"}]

# Vercel AI Gateway call
response = completion(
    model="vercel_ai_gateway/openai/gpt-4o",
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

Vercel AI Gateway Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["VERCEL_AI_GATEWAY_API_KEY"]="your-api-key"

messages =[{"content":"Hello, how are you?","role":"user"}]

# Vercel AI Gateway call with streaming
response = completion(
    model="vercel_ai_gateway/openai/gpt-4o",
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
-model_name: gpt-4o-gateway
litellm_params:
model: vercel_ai_gateway/openai/gpt-4o
api_key: os.environ/VERCEL_AI_GATEWAY_API_KEY

-model_name: claude-4-sonnet-gateway
litellm_params:
model: vercel_ai_gateway/anthropic/claude-4-sonnet
api_key: os.environ/VERCEL_AI_GATEWAY_API_KEY
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

Vercel AI Gateway via Proxy - Non-streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Non-streaming response
response = client.chat.completions.create(
    model="gpt-4o-gateway",
    messages=[{"role":"user","content":"Hello, how are you?"}]
)

print(response.choices[0].message.content)
```

Vercel AI Gateway via Proxy - Streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Streaming response
response = client.chat.completions.create(
    model="gpt-4o-gateway",
    messages=[{"role":"user","content":"Hello, how are you?"}],
    stream=True
)

for chunk in response:
if chunk.choices[0].delta.content isnotNone:
print(chunk.choices[0].delta.content, end="")
```

For more detailed information on using the LiteLLM Proxy, see the [LiteLLM Proxy documentation](https://docs.litellm.ai/docs/providers/litellm_proxy).

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Vercel AI Gateway Documentation](https://vercel.com/docs/ai-gateway)