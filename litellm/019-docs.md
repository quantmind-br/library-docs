---
title: LiteLLM - Getting Started | liteLLM
url: https://docs.litellm.ai/docs/
source: sitemap
fetched_at: 2026-01-21T19:43:48.507269062-03:00
rendered_js: false
word_count: 535
summary: LiteLLM provides a unified interface to call over 100 LLMs using the OpenAI input/output format via a Python SDK or a proxy server. It simplifies cross-provider integration by offering features like consistent response formats, retry logic, cost tracking, and observability.
tags:
    - llm-integration
    - openai-format
    - python-sdk
    - api-gateway
    - cost-tracking
    - observability
    - error-handling
category: guide
---

[https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)

## **Call 100+ LLMs using the OpenAI Input/Output Format**[​](#call-100-llms-using-the-openai-inputoutput-format "Direct link to call-100-llms-using-the-openai-inputoutput-format")

- Translate inputs to provider's endpoints (`/chat/completions`, `/responses`, `/embeddings`, `/images`, `/audio`, `/batches`, and more)
- [Consistent output](https://docs.litellm.ai/docs/supported_endpoints) - same response format regardless of which provider you use
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
- Track spend & set budgets per project [LiteLLM Proxy Server](https://docs.litellm.ai/docs/simple_proxy)

## How to use LiteLLM[​](#how-to-use-litellm "Direct link to How to use LiteLLM")

You can use LiteLLM through either the Proxy Server or Python SDK. Both gives you a unified interface to access multiple LLMs (100+ LLMs). Choose the option that best fits your needs:

[**LiteLLM Proxy Server**](#litellm-proxy-server-llm-gateway)[**LiteLLM Python SDK**](#basic-usage)**Use Case**Central service (LLM Gateway) to access multiple LLMsUse LiteLLM directly in your Python code**Who Uses It?**Gen AI Enablement / ML Platform TeamsDevelopers building LLM projects**Key Features**• Centralized API gateway with authentication & authorization  
• Multi-tenant cost tracking and spend management per project/user  
• Per-project customization (logging, guardrails, caching)  
• Virtual keys for secure access control  
• Admin dashboard UI for monitoring and management• Direct Python library integration in your codebase  
• Router with retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)  
• Application-level load balancing and cost tracking  
• Exception handling with OpenAI-compatible errors  
• Observability callbacks (Lunary, MLflow, Langfuse, etc.)

## **LiteLLM Python SDK**[​](#litellm-python-sdk "Direct link to litellm-python-sdk")

### Basic usage[​](#basic-usage "Direct link to Basic usage")

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/liteLLM_Getting_Started.ipynb)

- OpenAI
- Anthropic
- xAI
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI
- Vercel AI Gateway

```
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"]="your-api-key"

response = completion(
  model="openai/gpt-4o",
  messages=[{"content":"Hello, how are you?","role":"user"}]
)
```

### Response Format (OpenAI Chat Completions Format)[​](#response-format-openai-chat-completions-format "Direct link to Response Format (OpenAI Chat Completions Format)")

```
{
"id":"chatcmpl-565d891b-a42e-4c39-8d14-82a1f5208885",
"created":1734366691,
"model":"gpt-4o-2024-08-06",
"object":"chat.completion",
"system_fingerprint":null,
"choices":[
{
"finish_reason":"stop",
"index":0,
"message":{
"content":"Hello! As an AI language model, I don't have feelings, but I'm operating properly and ready to assist you with any questions or tasks you may have. How can I help you today?",
"role":"assistant",
"tool_calls":null,
"function_call":null
}
}
],
"usage":{
"completion_tokens":43,
"prompt_tokens":13,
"total_tokens":56,
"completion_tokens_details":null,
"prompt_tokens_details":{
"audio_tokens":null,
"cached_tokens":0
},
"cache_creation_input_tokens":0,
"cache_read_input_tokens":0
}
}
```

### Streaming[​](#streaming "Direct link to Streaming")

Set `stream=True` in the `completion` args.

- OpenAI
- Anthropic
- xAI
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI
- Vercel AI Gateway

```
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"]="your-api-key"

response = completion(
  model="openai/gpt-4o",
  messages=[{"content":"Hello, how are you?","role":"user"}],
  stream=True,
)
```

### Streaming Response Format (OpenAI Format)[​](#streaming-response-format-openai-format "Direct link to Streaming Response Format (OpenAI Format)")

```
{
"id":"chatcmpl-2be06597-eb60-4c70-9ec5-8cd2ab1b4697",
"created":1734366925,
"model":"claude-3-sonnet-20240229",
"object":"chat.completion.chunk",
"system_fingerprint":null,
"choices":[
{
"finish_reason":null,
"index":0,
"delta":{
"content":"Hello",
"role":"assistant",
"function_call":null,
"tool_calls":null,
"audio":null
},
"logprobs":null
}
]
}
```

### Exception handling[​](#exception-handling "Direct link to Exception handling")

LiteLLM maps exceptions across all supported providers to the OpenAI exceptions. All our exceptions inherit from OpenAI's exception types, so any error-handling you have for that, should work out of the box with LiteLLM.

```
import litellm
from litellm import completion
import os

os.environ["ANTHROPIC_API_KEY"]="bad-key"
try:
    completion(model="anthropic/claude-instant-1", messages=[{"role":"user","content":"Hey, how's it going?"}])
except litellm.AuthenticationError as e:
# Thrown when the API key is invalid
print(f"Authentication failed: {e}")
except litellm.RateLimitError as e:
# Thrown when you've exceeded your rate limit
print(f"Rate limited: {e}")
except litellm.APIError as e:
# Thrown for general API errors
print(f"API error: {e}")
```

### See How LiteLLM Transforms Your Requests[​](#see-how-litellm-transforms-your-requests "Direct link to See How LiteLLM Transforms Your Requests")

Want to understand how LiteLLM parses and normalizes your LLM API requests? Use the `/utils/transform_request` endpoint to see exactly how your request is transformed internally.

You can try it out now directly on our Demo App! Go to the [LiteLLM API docs for transform\_request](https://litellm-api.up.railway.app/#/llm%20utils/transform_request_utils_transform_request_post)

LiteLLM will show you the normalized, provider-agnostic version of your request. This is useful for debugging, learning, and understanding how LiteLLM handles different providers and options.

### Logging Observability - Log LLM Input/Output ([Docs](https://docs.litellm.ai/docs/observability/callbacks))[​](#logging-observability---log-llm-inputoutput-docs "Direct link to logging-observability---log-llm-inputoutput-docs")

LiteLLM exposes pre defined callbacks to send data to Lunary, MLflow, Langfuse, Helicone, Promptlayer, Traceloop, Slack

```
from litellm import completion

## set env variables for logging tools (API key set up is not required when using MLflow)
os.environ["LUNARY_PUBLIC_KEY"]="your-lunary-public-key"# get your public key at https://app.lunary.ai/settings
os.environ["HELICONE_API_KEY"]="your-helicone-key"
os.environ["LANGFUSE_PUBLIC_KEY"]=""
os.environ["LANGFUSE_SECRET_KEY"]=""

os.environ["OPENAI_API_KEY"]

# set callbacks
litellm.success_callback =["lunary","mlflow","langfuse","helicone"]# log input/output to lunary, mlflow, langfuse, helicone

#openai call
response = completion(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hi 👋 - i'm openai"}])
```

### Track Costs, Usage, Latency for streaming[​](#track-costs-usage-latency-for-streaming "Direct link to Track Costs, Usage, Latency for streaming")

Use a callback function for this - more info on custom callbacks: [https://docs.litellm.ai/docs/observability/custom\_callback](https://docs.litellm.ai/docs/observability/custom_callback)

```
import litellm

# track_cost_callback
deftrack_cost_callback(
    kwargs,# kwargs to completion
    completion_response,# response from completion
    start_time, end_time    # start/end time
):
try:
      response_cost = kwargs.get("response_cost",0)
print("streaming response_cost", response_cost)
except:
pass
# set callback
litellm.success_callback =[track_cost_callback]# set custom callback function

# litellm.completion() call
response = completion(
    model="gpt-3.5-turbo",
    messages=[
{
"role":"user",
"content":"Hi 👋 - i'm openai"
}
],
    stream=True
)
```

## **LiteLLM Proxy Server (LLM Gateway)**[​](#litellm-proxy-server-llm-gateway "Direct link to litellm-proxy-server-llm-gateway")

Track spend across multiple projects/people

![ui_3](https://github.com/BerriAI/litellm/assets/29436595/47c97d5e-b9be-4839-b28c-43d7f4f10033)

The proxy provides:

1. [Hooks for auth](https://docs.litellm.ai/docs/proxy/virtual_keys#custom-auth)
2. [Hooks for logging](https://docs.litellm.ai/docs/proxy/logging#step-1---create-your-custom-litellm-callback-class)
3. [Cost tracking](https://docs.litellm.ai/docs/proxy/virtual_keys#tracking-spend)
4. [Rate Limiting](https://docs.litellm.ai/docs/proxy/users#set-rate-limits)

### 📖 Proxy Endpoints - [Swagger Docs](https://litellm-api.up.railway.app/)[​](#-proxy-endpoints---swagger-docs "Direct link to -proxy-endpoints---swagger-docs")

Go here for a complete tutorial with keys + rate limits - [**here**](https://docs.litellm.ai/docs/proxy/docker_quick_start)

### Quick Start Proxy - CLI[​](#quick-start-proxy---cli "Direct link to Quick Start Proxy - CLI")

```
pip install 'litellm[proxy]'
```

#### Step 1: Start litellm proxy[​](#step-1-start-litellm-proxy "Direct link to Step 1: Start litellm proxy")

- pip package
- Docker container

```
$ litellm --model huggingface/bigcode/starcoder

#INFO: Proxy running on http://0.0.0.0:4000
```

#### Step 2: Make ChatCompletions Request to Proxy[​](#step-2-make-chatcompletions-request-to-proxy "Direct link to Step 2: Make ChatCompletions Request to Proxy")

```
import openai # openai v1.0.0+
client = openai.OpenAI(api_key="anything",base_url="http://0.0.0.0:4000")# set proxy to base_url
# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="gpt-3.5-turbo", messages =[
{
"role":"user",
"content":"this is a test request, write a short poem"
}
])

print(response)
```

## More details[​](#more-details "Direct link to More details")

- [exception mapping](https://docs.litellm.ai/docs/exception_mapping)
- [retries + model fallbacks for completion()](https://docs.litellm.ai/docs/completion/reliable_completions)
- [proxy virtual keys & spend management](https://docs.litellm.ai/docs/proxy/virtual_keys)
- [E2E Tutorial for LiteLLM Proxy Server](https://docs.litellm.ai/docs/proxy/docker_quick_start)