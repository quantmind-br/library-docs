---
title: CompactifAI | liteLLM
url: https://docs.litellm.ai/docs/providers/compactifai
source: sitemap
fetched_at: 2026-01-21T19:48:47.010615886-03:00
rendered_js: false
word_count: 236
summary: This document provides a technical overview and integration guide for CompactifAI's OpenAI-compatible API, which offers compressed language models designed for low-latency and cost-effective inference. It covers API configuration, supported parameters, and implementation examples using the LiteLLM SDK.
tags:
    - compactifai
    - openai-compatibility
    - model-compression
    - litellm-integration
    - llm-inference
    - api-reference
    - cost-optimization
category: api
---

[https://docs.compactif.ai/](https://docs.compactif.ai/)

CompactifAI offers highly compressed versions of leading language models, delivering up to **70% lower inference costs**, **4x throughput gains**, and **low-latency inference** with minimal quality loss (under 5%). CompactifAI's OpenAI-compatible API makes integration straightforward, enabling developers to build ultra-efficient, scalable AI applications with superior concurrency and resource efficiency.

PropertyDetailsDescriptionCompactifAI offers compressed versions of leading language models with up to 70% cost reduction and 4x throughput gainsProvider Route on LiteLLM`compactifai/` (add this prefix to the model name - e.g. `compactifai/cai-llama-3-1-8b-slim`)Provider Doc[CompactifAI ↗](https://docs.compactif.ai/)API Endpoint for Provider[https://api.compactif.ai/v1](https://api.compactif.ai/v1)Supported Endpoints`/chat/completions`, `/completions`

## Supported OpenAI Parameters[​](#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

CompactifAI is fully OpenAI-compatible and supports the following parameters:

```
"stream",
"stop",
"temperature",
"top_p",
"max_tokens",
"presence_penalty",
"frequency_penalty",
"logit_bias",
"user",
"response_format",
"seed",
"tools",
"tool_choice",
"parallel_tool_calls",
"extra_headers"
```

## API Key Setup[​](#api-key-setup "Direct link to API Key Setup")

CompactifAI API keys are available through AWS Marketplace subscription:

1. Subscribe via [AWS Marketplace](https://aws.amazon.com/marketplace)
2. Complete subscription verification (24-hour review process)
3. Access MultiverseIAM dashboard with provided credentials
4. Retrieve your API key from the dashboard

```
import os

os.environ["COMPACTIFAI_API_KEY"]="your-api-key"
```

## Usage[​](#usage "Direct link to Usage")

- SDK
- Proxy

```
from litellm import completion
import os

os.environ['COMPACTIFAI_API_KEY']="your-api-key"

response = completion(
    model="compactifai/cai-llama-3-1-8b-slim",
    messages=[
{"role":"user","content":"Hello from LiteLLM!"}
],
)
print(response)
```

## Streaming[​](#streaming "Direct link to Streaming")

```
from litellm import completion
import os

os.environ['COMPACTIFAI_API_KEY']="your-api-key"

response = completion(
    model="compactifai/cai-llama-3-1-8b-slim",
    messages=[
{"role":"user","content":"Write a short story"}
],
    stream=True
)

for chunk in response:
print(chunk)
```

## Advanced Usage[​](#advanced-usage "Direct link to Advanced Usage")

### Custom Parameters[​](#custom-parameters "Direct link to Custom Parameters")

```
from litellm import completion

response = completion(
    model="compactifai/cai-llama-3-1-8b-slim",
    messages=[{"role":"user","content":"Explain quantum computing"}],
    temperature=0.7,
    max_tokens=500,
    top_p=0.9,
    stop=["Human:","AI:"]
)
```

### Function Calling[​](#function-calling "Direct link to Function Calling")

CompactifAI supports OpenAI-compatible function calling:

```
from litellm import completion

functions =[
{
"name":"get_weather",
"description":"Get current weather information",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state"
}
},
"required":["location"]
}
}
]

response = completion(
    model="compactifai/cai-llama-3-1-8b-slim",
    messages=[{"role":"user","content":"What's the weather in San Francisco?"}],
    tools=[{"type":"function","function": f}for f in functions],
    tool_choice="auto"
)
```

### Async Usage[​](#async-usage "Direct link to Async Usage")

```
import asyncio
from litellm import acompletion

asyncdefasync_call():
    response =await acompletion(
        model="compactifai/cai-llama-3-1-8b-slim",
        messages=[{"role":"user","content":"Hello async world!"}]
)
return response

# Run async function
response = asyncio.run(async_call())
print(response)
```

## Available Models[​](#available-models "Direct link to Available Models")

CompactifAI offers compressed versions of popular models. Use the `/models` endpoint to get the latest list:

```
import httpx

headers ={"Authorization":f"Bearer {your_api_key}"}
response = httpx.get("https://api.compactif.ai/v1/models", headers=headers)
models = response.json()
```

Common model formats:

- `compactifai/cai-llama-3-1-8b-slim`
- `compactifai/mistral-7b-compressed`
- `compactifai/codellama-7b-compressed`

## Benefits[​](#benefits "Direct link to Benefits")

- **Cost Efficient**: Up to 70% lower inference costs compared to standard models
- **High Performance**: 4x throughput gains with minimal quality loss (under 5%)
- **Low Latency**: Optimized for fast response times
- **Drop-in Replacement**: Full OpenAI API compatibility
- **Scalable**: Superior concurrency and resource efficiency

## Error Handling[​](#error-handling "Direct link to Error Handling")

CompactifAI returns standard OpenAI-compatible error responses:

```
from litellm import completion
from litellm.exceptions import AuthenticationError, RateLimitError

try:
    response = completion(
        model="compactifai/cai-llama-3-1-8b-slim",
        messages=[{"role":"user","content":"Hello"}]
)
except AuthenticationError:
print("Invalid API key")
except RateLimitError:
print("Rate limit exceeded")
```

## Support[​](#support "Direct link to Support")

- Documentation: [https://docs.compactif.ai/](https://docs.compactif.ai/)
- LinkedIn: [MultiverseComputing](https://www.linkedin.com/company/multiversecomputing)
- Analysis: [Artificial Analysis Provider Comparison](https://artificialanalysis.ai/providers/compactifai)