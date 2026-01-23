---
title: /interactions | liteLLM
url: https://docs.litellm.ai/docs/interactions
source: sitemap
fetched_at: 2026-01-21T19:45:32.643340008-03:00
rendered_js: false
word_count: 175
summary: This document provides technical specifications and implementation guides for the LiteLLM Interactions API, covering Python SDK usage, proxy configuration, and multi-provider integration.
tags:
    - litellm
    - interactions-api
    - python-sdk
    - ai-gateway
    - llm-integration
    - api-reference
    - streaming
category: api
---

FeatureSupportedNotesLogging✅Works across all integrationsStreaming✅Loadbalancing✅Between supported modelsSupported LLM providers**All LiteLLM supported CHAT COMPLETION providers**`openai`, `anthropic`, `bedrock`, `vertex_ai`, `gemini`, `azure`, `azure_ai` etc.

## **LiteLLM Python SDK Usage**[​](#litellm-python-sdk-usage "Direct link to litellm-python-sdk-usage")

### Quick Start[​](#quick-start "Direct link to Quick Start")

Create Interaction

```
from litellm import create_interaction
import os

os.environ["GEMINI_API_KEY"]="your-api-key"

response = create_interaction(
    model="gemini/gemini-2.5-flash",
input="Tell me a short joke about programming."
)

print(response.outputs[-1].text)
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

Async Create Interaction

```
from litellm import acreate_interaction
import os
import asyncio

os.environ["GEMINI_API_KEY"]="your-api-key"

asyncdefmain():
    response =await acreate_interaction(
        model="gemini/gemini-2.5-flash",
input="Tell me a short joke about programming."
)
print(response.outputs[-1].text)

asyncio.run(main())
```

### Streaming[​](#streaming "Direct link to Streaming")

Streaming Interaction

```
from litellm import create_interaction
import os

os.environ["GEMINI_API_KEY"]="your-api-key"

response = create_interaction(
    model="gemini/gemini-2.5-flash",
input="Write a 3 paragraph story about a robot.",
    stream=True
)

for chunk in response:
print(chunk)
```

## **LiteLLM AI Gateway (Proxy) Usage**[​](#litellm-ai-gateway-proxy-usage "Direct link to litellm-ai-gateway-proxy-usage")

### Setup[​](#setup "Direct link to Setup")

Add this to your litellm proxy config.yaml:

config.yaml

```
model_list:
-model_name: gemini-flash
litellm_params:
model: gemini/gemini-2.5-flash
api_key: os.environ/GEMINI_API_KEY
```

Start litellm:

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

### Test Request[​](#test-request "Direct link to Test Request")

- curl
- Google GenAI SDK

Create Interaction

```
curl -X POST "http://localhost:4000/v1beta/interactions" \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini/gemini-2.5-flash",
    "input": "Tell me a short joke about programming."
  }'
```

**Streaming:**

Streaming Interaction

```
curl -N -X POST "http://localhost:4000/v1beta/interactions" \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini/gemini-2.5-flash",
    "input": "Write a 3 paragraph story about a robot.",
    "stream": true
  }'
```

**Get Interaction:**

Get Interaction by ID

```
curl "http://localhost:4000/v1beta/interactions/{interaction_id}" \
  -H "Authorization: Bearer sk-1234"
```

## **Request/Response Format**[​](#requestresponse-format "Direct link to requestresponse-format")

### Request Parameters[​](#request-parameters "Direct link to Request Parameters")

ParameterTypeRequiredDescription`model`stringYesModel to use (e.g., `gemini/gemini-2.5-flash`)`input`stringYesThe input text for the interaction`stream`booleanNoEnable streaming responses`tools`arrayNoTools available to the model`system_instruction`stringNoSystem instructions for the model`generation_config`objectNoGeneration configuration`previous_interaction_id`stringNoID of previous interaction for context

### Response Format[​](#response-format "Direct link to Response Format")

```
{
"id":"interaction_abc123",
"object":"interaction",
"model":"gemini-2.5-flash",
"status":"completed",
"created":"2025-01-15T10:30:00Z",
"updated":"2025-01-15T10:30:05Z",
"role":"model",
"outputs":[
{
"type":"text",
"text":"Why do programmers prefer dark mode? Because light attracts bugs!"
}
],
"usage":{
"total_input_tokens":10,
"total_output_tokens":15,
"total_tokens":25
}
}
```

## **Calling non-Interactions API endpoints (`/interactions` to `/responses` Bridge)**[​](#calling-non-interactions-api-endpoints-interactions-to-responses-bridge "Direct link to calling-non-interactions-api-endpoints-interactions-to-responses-bridge")

LiteLLM allows you to call non-Interactions API models via a bridge to LiteLLM's `/responses` endpoint. This is useful for calling OpenAI, Anthropic, and other providers that don't natively support the Interactions API.

#### Python SDK Usage[​](#python-sdk-usage "Direct link to Python SDK Usage")

SDK Usage

```
import litellm
import os

# Set API key
os.environ["OPENAI_API_KEY"]="your-openai-api-key"

# Non-streaming interaction
response = litellm.interactions.create(
    model="gpt-4o",
input="Tell me a short joke about programming."
)

print(response.outputs[-1].text)
```

#### LiteLLM Proxy Usage[​](#litellm-proxy-usage "Direct link to LiteLLM Proxy Usage")

**Setup Config:**

Example Configuration

```
model_list:
-model_name: openai-model
litellm_params:
model: gpt-4o
api_key: os.environ/OPENAI_API_KEY
```

**Start Proxy:**

Start LiteLLM Proxy

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

**Make Request:**

non-Interactions API Model Request

```
curl http://localhost:4000/v1beta/interactions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234" \
  -d '{
    "model": "openai-model",
    "input": "Tell me a short joke about programming."
  }'
```

## **Supported Providers**[​](#supported-providers "Direct link to supported-providers")

ProviderLink to UsageGoogle AI Studio[Usage](#quick-start)All other LiteLLM providers[Bridge Usage](#calling-non-interactions-api-endpoints-interactions-to-responses-bridge)