---
title: Hyperbolic | liteLLM
url: https://docs.litellm.ai/docs/providers/hyperbolic
source: sitemap
fetched_at: 2026-01-21T19:49:24.719786516-03:00
rendered_js: false
word_count: 352
summary: This document provides instructions for integrating Hyperbolic's AI models with LiteLLM, covering configuration, supported models like DeepSeek and Qwen, and usage via the Python SDK or Proxy.
tags:
    - hyperbolic-ai
    - litellm
    - llm-api
    - python-sdk
    - api-integration
    - function-calling
    - deepseek
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionHyperbolic provides access to the latest models at a fraction of legacy cloud costs, with OpenAI-compatible APIs for LLMs, image generation, and more.Provider Route on LiteLLM`hyperbolic/`Link to Provider Doc[Hyperbolic Documentation ↗](https://docs.hyperbolic.xyz)Base URL`https://api.hyperbolic.xyz/v1`Supported Operations[`/chat/completions`](#sample-usage)

[https://docs.hyperbolic.xyz](https://docs.hyperbolic.xyz)

**We support ALL Hyperbolic models, just set `hyperbolic/` as a prefix when sending completion requests**

## Available Models[​](#available-models "Direct link to Available Models")

### Language Models[​](#language-models "Direct link to Language Models")

ModelDescriptionContext WindowPricing per 1M tokens`hyperbolic/deepseek-ai/DeepSeek-V3`DeepSeek V3 - Fast and efficient131,072 tokens$0.25`hyperbolic/deepseek-ai/DeepSeek-V3-0324`DeepSeek V3 March 2024 version131,072 tokens$0.25`hyperbolic/deepseek-ai/DeepSeek-R1`DeepSeek R1 - Reasoning model131,072 tokens$2.00`hyperbolic/deepseek-ai/DeepSeek-R1-0528`DeepSeek R1 May 2028 version131,072 tokens$0.25`hyperbolic/Qwen/Qwen2.5-72B-Instruct`Qwen 2.5 72B Instruct131,072 tokens$0.40`hyperbolic/Qwen/Qwen2.5-Coder-32B-Instruct`Qwen 2.5 Coder 32B for code generation131,072 tokens$0.20`hyperbolic/Qwen/Qwen3-235B-A22B`Qwen 3 235B A22B variant131,072 tokens$2.00`hyperbolic/Qwen/QwQ-32B`Qwen QwQ 32B131,072 tokens$0.20`hyperbolic/meta-llama/Llama-3.3-70B-Instruct`Llama 3.3 70B Instruct131,072 tokens$0.80`hyperbolic/meta-llama/Meta-Llama-3.1-405B-Instruct`Llama 3.1 405B Instruct131,072 tokens$5.00`hyperbolic/moonshotai/Kimi-K2-Instruct`Kimi K2 Instruct131,072 tokens$2.00

## Required Variables[​](#required-variables "Direct link to Required Variables")

Environment Variables

```
os.environ["HYPERBOLIC_API_KEY"]=""# your Hyperbolic API key
```

Get your API key from [Hyperbolic dashboard](https://app.hyperbolic.ai).

## Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

Hyperbolic Non-streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["HYPERBOLIC_API_KEY"]=""# your Hyperbolic API key

messages =[{"content":"What is the capital of France?","role":"user"}]

# Hyperbolic call
response = completion(
    model="hyperbolic/Qwen/Qwen2.5-72B-Instruct",
    messages=messages
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

Hyperbolic Streaming Completion

```
import os
import litellm
from litellm import completion

os.environ["HYPERBOLIC_API_KEY"]=""# your Hyperbolic API key

messages =[{"content":"Write a short poem about AI","role":"user"}]

# Hyperbolic call with streaming
response = completion(
    model="hyperbolic/deepseek-ai/DeepSeek-V3",
    messages=messages,
    stream=True
)

for chunk in response:
print(chunk)
```

### Function Calling[​](#function-calling "Direct link to Function Calling")

Hyperbolic Function Calling

```
import os
import litellm
from litellm import completion

os.environ["HYPERBOLIC_API_KEY"]=""# your Hyperbolic API key

tools =[
{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get the current weather in a location",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state, e.g. San Francisco, CA"
},
"unit":{
"type":"string",
"enum":["celsius","fahrenheit"]
}
},
"required":["location"]
}
}
}
]

response = completion(
    model="hyperbolic/deepseek-ai/DeepSeek-V3",
    messages=[{"role":"user","content":"What's the weather like in New York?"}],
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
-model_name: deepseek-fast
litellm_params:
model: hyperbolic/deepseek-ai/DeepSeek-V3
api_key: os.environ/HYPERBOLIC_API_KEY

-model_name: qwen-coder
litellm_params:
model: hyperbolic/Qwen/Qwen2.5-Coder-32B-Instruct
api_key: os.environ/HYPERBOLIC_API_KEY

-model_name: deepseek-reasoning
litellm_params:
model: hyperbolic/deepseek-ai/DeepSeek-R1
api_key: os.environ/HYPERBOLIC_API_KEY
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

Hyperbolic via Proxy - Non-streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Non-streaming response
response = client.chat.completions.create(
    model="deepseek-fast",
    messages=[{"role":"user","content":"Explain quantum computing in simple terms"}]
)

print(response.choices[0].message.content)
```

Hyperbolic via Proxy - Streaming

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-proxy-api-key"# Your proxy API key
)

# Streaming response
response = client.chat.completions.create(
    model="qwen-coder",
    messages=[{"role":"user","content":"Write a Python function to sort a list"}],
    stream=True
)

for chunk in response:
if chunk.choices[0].delta.content isnotNone:
print(chunk.choices[0].delta.content, end="")
```

For more detailed information on using the LiteLLM Proxy, see the [LiteLLM Proxy documentation](https://docs.litellm.ai/docs/providers/litellm_proxy).

## Supported OpenAI Parameters[​](#supported-openai-parameters "Direct link to Supported OpenAI Parameters")

Hyperbolic supports the following OpenAI-compatible parameters:

ParameterTypeDescription`messages`array**Required**. Array of message objects with 'role' and 'content'`model`string**Required**. Model ID (e.g., deepseek-ai/DeepSeek-V3, Qwen/Qwen2.5-72B-Instruct)`stream`booleanOptional. Enable streaming responses`temperature`floatOptional. Sampling temperature (0.0 to 2.0)`top_p`floatOptional. Nucleus sampling parameter`max_tokens`integerOptional. Maximum tokens to generate`frequency_penalty`floatOptional. Penalize frequent tokens`presence_penalty`floatOptional. Penalize tokens based on presence`stop`string/arrayOptional. Stop sequences`n`integerOptional. Number of completions to generate`tools`arrayOptional. List of available tools/functions`tool_choice`string/objectOptional. Control tool/function calling`response_format`objectOptional. Response format specification`seed`integerOptional. Random seed for reproducibility`user`stringOptional. User identifier

## Advanced Usage[​](#advanced-usage "Direct link to Advanced Usage")

### Custom API Base[​](#custom-api-base "Direct link to Custom API Base")

If you're using a custom Hyperbolic deployment:

Custom API Base

```
import litellm

response = litellm.completion(
    model="hyperbolic/deepseek-ai/DeepSeek-V3",
    messages=[{"role":"user","content":"Hello"}],
    api_base="https://your-custom-hyperbolic-endpoint.com/v1",
    api_key="your-api-key"
)
```

### Rate Limits[​](#rate-limits "Direct link to Rate Limits")

Hyperbolic offers different tiers:

- **Basic**: 60 requests per minute (RPM)
- **Pro**: 600 RPM
- **Enterprise**: Custom limits

## Pricing[​](#pricing "Direct link to Pricing")

Hyperbolic offers competitive pay-as-you-go pricing with no hidden fees or long-term commitments. See the model table above for specific pricing per million tokens.

### Precision Options[​](#precision-options "Direct link to Precision Options")

- **BF16**: Best precision and performance, suitable for tasks where accuracy is critical
- **FP8**: Optimized for efficiency and speed, ideal for high-throughput applications at lower cost

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Hyperbolic Official Documentation](https://docs.hyperbolic.xyz)
- [Hyperbolic Dashboard](https://app.hyperbolic.ai)
- [API Reference](https://docs.hyperbolic.xyz/docs/rest-api)