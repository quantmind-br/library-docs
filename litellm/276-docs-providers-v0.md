---
title: v0 | liteLLM
url: https://docs.litellm.ai/docs/providers/v0
source: sitemap
fetched_at: 2026-01-21T19:50:36.053963198-03:00
rendered_js: false
word_count: 281
summary: This document provides instructions and code examples for integrating v0.dev AI models with LiteLLM, covering authentication, streaming, vision support, and function calling.
tags:
    - v0-dev
    - litellm
    - code-generation
    - python-sdk
    - api-integration
    - ai-models
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionv0 provides AI models optimized for code generation, particularly for creating Next.js applications, React components, and modern web development.Provider Route on LiteLLM`v0/`Link to Provider Doc[v0 API Documentation ↗](https://v0.dev/docs/v0-model-api)Base URL`https://api.v0.dev/v1`Supported Operations[`/chat/completions`](#sample-usage)

[https://v0.dev/docs/v0-model-api](https://v0.dev/docs/v0-model-api)

**We support ALL v0 models, just set `v0/` as a prefix when sending completion requests**

## Available Models[​](#available-models "Direct link to Available Models")

ModelDescriptionContext WindowMax Output`v0/v0-1.5-lg`Large model for advanced code generation and reasoning512,000 tokens512,000 tokens`v0/v0-1.5-md`Medium model for everyday code generation tasks128,000 tokens128,000 tokens`v0/v0-1.0-md`Legacy medium model128,000 tokens128,000 tokens

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["V0_API_KEY"]=""# your v0 API key from v0.dev
```

Note: v0 API access requires a Premium or Team plan. Visit [v0.dev/chat/settings/billing](https://v0.dev/chat/settings/billing) to upgrade.

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

v0 Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["V0_API_KEY"]=""# your v0 API key

messages =[{"content":"Create a React button component with hover effects","role":"user"}]

# v0 call
response = completion(
    model="v0/v0-1.5-md",
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

v0 Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["V0_API_KEY"]=""# your v0 API key

messages =[{"content":"Create a React button component with hover effects","role":"user"}]

# v0 call with streaming
response = completion(
    model="v0/v0-1.5-md",
    messages=messages,
    stream=True
)

for chunk in response:
print(chunk)
```

### Vision/Multimodal Support[​](#visionmultimodal-support "Direct link to Vision/Multimodal Support")

All v0 models support vision inputs, allowing you to send images along with text:

v0 Vision/Multimodal

```
import os
import litellm
from litellm import completion

os.environ["V0_API_KEY"]=""# your v0 API key

messages =[{
"role":"user",
"content":[
{
"type":"text",
"text":"Recreate this UI design in React"
},
{
"type":"image_url",
"image_url":{
"url":"https://example.com/ui-design.png"
}
}
]
}]

response = completion(
    model="v0/v0-1.5-lg",
    messages=messages
)

print(response)
```

### Function Calling[​](#function-calling "Direct link to Function Calling")

v0 supports function calling for structured outputs:

v0 Function Calling

```
import os
import litellm
from litellm import completion

os.environ["V0_API_KEY"]=""# your v0 API key

tools =[
{
"type":"function",
"function":{
"name":"create_component",
"description":"Create a React component",
"parameters":{
"type":"object",
"properties":{
"component_name":{
"type":"string",
"description":"The name of the component"
},
"props":{
"type":"array",
"items":{"type":"string"},
"description":"List of component props"
}
},
"required":["component_name"]
}
}
}
]

response = completion(
    model="v0/v0-1.5-md",
    messages=[{"role":"user","content":"Create a Button component with onClick and disabled props"}],
    tools=tools,
    tool_choice="auto"
)

print(response)
```

## Usage - LiteLLM Proxy[​](#usage---litellm-proxy "Direct link to Usage - LiteLLM Proxy")

Add the following to your LiteLLM Proxy configuration file:

config.yaml

```
model_list:
-model_name: v0-large
litellm_params:
model: v0/v0-1.5-lg
api_key: os.environ/V0_API_KEY

-model_name: v0-medium
litellm_params:
model: v0/v0-1.5-md
api_key: os.environ/V0_API_KEY

-model_name: v0-legacy
litellm_params:
model: v0/v0-1.0-md
api_key: os.environ/V0_API_KEY
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

v0 via Proxy - Non-streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Non-streaming response
response = client.chat.completions.create(
    model="v0-medium",
    messages=[{"role":"user","content":"Create a React card component"}]
)

print(response.choices[0].message.content)
```

v0 via Proxy - Streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Streaming response
response = client.chat.completions.create(
    model="v0-medium",
    messages=[{"role":"user","content":"Create a React card component"}],
    stream=True
)

for chunk in response:
if chunk.choices[0].delta.content isnotNone:
print(chunk.choices[0].delta.content, end="")
```

For more detailed information on using the LiteLLM Proxy, see the [LiteLLM Proxy documentation](https://docs.litellm.ai/docs/providers/litellm_proxy).

## Supported OpenAI Parameters[​](#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

v0 supports the following OpenAI-compatible parameters:

ParameterTypeDescription`messages`array**Required**. Array of message objects with 'role' and 'content'`model`string**Required**. Model ID (v0-1.5-lg, v0-1.5-md, v0-1.0-md)`stream`booleanOptional. Enable streaming responses`tools`arrayOptional. List of available tools/functions`tool_choice`string/objectOptional. Control tool/function calling

Note: v0 has a limited set of supported parameters compared to the full OpenAI API. Parameters like `temperature`, `max_tokens`, `top_p`, etc. are not supported.

## Advanced Usage[​](#advanced-usage "Direct link to Advanced Usage")

### Custom API Base[​](#custom-api-base "Direct link to Custom API Base")

If you're using a custom v0 deployment:

Custom API Base

```
import litellm

response = litellm.completion(
    model="v0/v0-1.5-md",
    messages=[{"role":"user","content":"Hello"}],
    api_base="https://your-custom-v0-endpoint.com/v1",
    api_key="your-api-key"
)
```

## Pricing[​](#pricing "Direct link to Pricing")

v0 models require a Premium or Team subscription. Visit [v0.dev/chat/settings/billing](https://v0.dev/chat/settings/billing) for current pricing information.

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [v0 Official Documentation](https://v0.dev/docs)
- [v0 Model API Reference](https://v0.dev/docs/v0-model-api)