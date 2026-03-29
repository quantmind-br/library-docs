---
title: LiteLLM - Getting Started | liteLLM
url: https://docs.litellm.ai/
source: sitemap
fetched_at: 2026-01-21T19:56:00.824340265-03:00
rendered_js: false
word_count: 539
summary: LiteLLM provides a unified interface and proxy server to call over 100 different LLMs using the OpenAI input/output format, featuring load balancing and cost tracking.
tags:
    - litellm
    - llm-gateway
    - openai-compatibility
    - python-sdk
    - observability
    - cost-tracking
    - multi-model-orchestration
category: guide
---

[https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)

## **Call 100+ LLMs using the OpenAI Input/Output Format**[​](#call-100-llms-using-the-openai-inputoutput-format "Direct link to call-100-llms-using-the-openai-inputoutput-format")

- Translate inputs to provider's `completion`, `embedding`, and `image_generation` endpoints
- [Consistent output](https://docs.litellm.ai/docs/completion/output), text responses will always be available at `['choices'][0]['message']['content']`
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
- Track spend & set budgets per project [LiteLLM Proxy Server](https://docs.litellm.ai/docs/simple_proxy)

## How to use LiteLLM[​](#how-to-use-litellm "Direct link to How to use LiteLLM")

You can use litellm through either:

1. [LiteLLM Proxy Server](#litellm-proxy-server-llm-gateway) - Server (LLM Gateway) to call 100+ LLMs, load balance, cost tracking across projects
2. [LiteLLM python SDK](#basic-usage) - Python Client to call 100+ LLMs, load balance, cost tracking

### **When to use LiteLLM Proxy Server (LLM Gateway)**[​](#when-to-use-litellm-proxy-server-llm-gateway "Direct link to when-to-use-litellm-proxy-server-llm-gateway")

tip

Use LiteLLM Proxy Server if you want a **central service (LLM Gateway) to access multiple LLMs**

Typically used by Gen AI Enablement / ML PLatform Teams

- LiteLLM Proxy gives you a unified interface to access multiple LLMs (100+ LLMs)
- Track LLM Usage and setup guardrails
- Customize Logging, Guardrails, Caching per project

### **When to use LiteLLM Python SDK**[​](#when-to-use-litellm-python-sdk "Direct link to when-to-use-litellm-python-sdk")

tip

Use LiteLLM Python SDK if you want to use LiteLLM in your **python code**

Typically used by developers building llm projects

- LiteLLM SDK gives you a unified interface to access multiple LLMs (100+ LLMs)
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)

## **LiteLLM Python SDK**[​](#litellm-python-sdk "Direct link to litellm-python-sdk")

### Basic usage[​](#basic-usage "Direct link to Basic usage")

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/liteLLM_Getting_Started.ipynb)

- OpenAI
- Anthropic
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI

```
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"]="your-api-key"

response = completion(
  model="gpt-3.5-turbo",
  messages=[{"content":"Hello, how are you?","role":"user"}]
)
```

### Responses API[​](#responses-api "Direct link to Responses API")

Use `litellm.responses()` for advanced models that support reasoning content like GPT-5, o3, etc.

- OpenAI
- Anthropic (Claude)
- VertexAI
- Azure OpenAI

```
from litellm import responses
import os

## set ENV variables
os.environ["OPENAI_API_KEY"]="your-api-key"

response = responses(
  model="gpt-5-mini",
  messages=[{"content":"What is the capital of France?","role":"user"}],
  reasoning_effort="medium"
)

print(response)
print(response.choices[0].message.content)# response
print(response.choices[0].message.reasoning_content)# reasoning

```

### Streaming[​](#streaming "Direct link to Streaming")

Set `stream=True` in the `completion` args.

- OpenAI
- Anthropic
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI

```
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"]="your-api-key"

response = completion(
  model="gpt-3.5-turbo",
  messages=[{"content":"Hello, how are you?","role":"user"}],
  stream=True,
)
```

### Exception handling[​](#exception-handling "Direct link to Exception handling")

LiteLLM maps exceptions across all supported providers to the OpenAI exceptions. All our exceptions inherit from OpenAI's exception types, so any error-handling you have for that, should work out of the box with LiteLLM.

```
from openai.error import OpenAIError
from litellm import completion

os.environ["ANTHROPIC_API_KEY"]="bad-key"
try:
# some code
    completion(model="claude-instant-1", messages=[{"role":"user","content":"Hey, how's it going?"}])
except OpenAIError as e:
print(e)
```

### Logging Observability - Log LLM Input/Output ([Docs](https://docs.litellm.ai/docs/observability/callbacks))[​](#logging-observability---log-llm-inputoutput-docs "Direct link to logging-observability---log-llm-inputoutput-docs")

LiteLLM exposes pre defined callbacks to send data to MLflow, Lunary, Langfuse, Helicone, Promptlayer, Traceloop, Slack

```
from litellm import completion

## set env variables for logging tools (API key set up is not required when using MLflow)
os.environ["LUNARY_PUBLIC_KEY"]="your-lunary-public-key"# get your key at https://app.lunary.ai/settings
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

Go here for a complete tutorial with keys + rate limits - [**here**](https://docs.litellm.ai/proxy/docker_quick_start.md)

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

- Chat Completions
- Responses API

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
- [E2E Tutorial for LiteLLM Proxy Server](https://docs.litellm.ai/docs/proxy/docker_quick_start)
- [proxy virtual keys & spend management](https://docs.litellm.ai/docs/proxy/virtual_keys)

<!--THE END-->

- [**Call 100+ LLMs using the OpenAI Input/Output Format**](#call-100-llms-using-the-openai-inputoutput-format)
- [How to use LiteLLM](#how-to-use-litellm)
  
  - [**When to use LiteLLM Proxy Server (LLM Gateway)**](#when-to-use-litellm-proxy-server-llm-gateway)
  - [**When to use LiteLLM Python SDK**](#when-to-use-litellm-python-sdk)
- [**LiteLLM Python SDK**](#litellm-python-sdk)
  
  - [Basic usage](#basic-usage)
  - [Responses API](#responses-api)
  - [Streaming](#streaming)
  - [Exception handling](#exception-handling)
  - [Logging Observability - Log LLM Input/Output (Docs)](#logging-observability---log-llm-inputoutput-docs)
  - [Track Costs, Usage, Latency for streaming](#track-costs-usage-latency-for-streaming)
- [**LiteLLM Proxy Server (LLM Gateway)**](#litellm-proxy-server-llm-gateway)
  
  - [📖 Proxy Endpoints - Swagger Docs](#-proxy-endpoints---swagger-docs)
  - [Quick Start Proxy - CLI](#quick-start-proxy---cli)
  - [Step 1. CREATE config.yaml](#step-1-create-configyaml)
  - [Step 2. RUN Docker Image](#step-2-run-docker-image)
- [More details](#more-details)