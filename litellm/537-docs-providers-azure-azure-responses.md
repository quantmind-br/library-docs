---
title: Azure Responses API | liteLLM
url: https://docs.litellm.ai/docs/providers/azure/azure_responses
source: sitemap
fetched_at: 2026-01-21T19:48:18.638224557-03:00
rendered_js: false
word_count: 131
summary: This document explains how to integrate and use the Azure OpenAI Responses API with LiteLLM, including instructions for streaming, cost tracking, and handling specific model types like Azure Codex.
tags:
    - azure-openai
    - litellm
    - responses-api
    - python-sdk
    - streaming
    - cost-tracking
    - codex-models
category: api
---

PropertyDetailsDescriptionAzure OpenAI Responses API`custom_llm_provider` on LiteLLM`azure/`Supported Operations`/v1/responses`Azure OpenAI Responses API[Azure OpenAI Responses API ↗](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/responses?tabs=python-secure)Cost Tracking, Logging Support✅ LiteLLM will log, track cost for Responses API RequestsSupported OpenAI Params✅ All OpenAI params are supported, [See here](https://github.com/BerriAI/litellm/blob/0717369ae6969882d149933da48eeb8ab0e691bd/litellm/llms/openai/responses/transformation.py#L23)

## Usage[​](#usage "Direct link to Usage")

## Create a model response[​](#create-a-model-response "Direct link to Create a model response")

- LiteLLM SDK
- OpenAI SDK with LiteLLM Proxy

#### Non-streaming[​](#non-streaming "Direct link to Non-streaming")

Azure Responses API

```
import litellm

# Non-streaming response
response = litellm.responses(
    model="azure/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn.",
    max_output_tokens=100,
    api_key=os.getenv("AZURE_RESPONSES_OPENAI_API_KEY"),
    api_base="https://litellm8397336933.openai.azure.com/",
    api_version="2023-03-15-preview",
)

print(response)
```

#### Streaming[​](#streaming "Direct link to Streaming")

Azure Responses API

```
import litellm

# Streaming response
response = litellm.responses(
    model="azure/o1-pro",
input="Tell me a three sentence bedtime story about a unicorn.",
    stream=True,
    api_key=os.getenv("AZURE_RESPONSES_OPENAI_API_KEY"),
    api_base="https://litellm8397336933.openai.azure.com/",
    api_version="2023-03-15-preview",
)

for event in response:
print(event)
```

## Azure Codex Models[​](#azure-codex-models "Direct link to Azure Codex Models")

Codex models use Azure's new [/v1/preview API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-lifecycle?tabs=key#next-generation-api) which provides ongoing access to the latest features with no need to update `api-version` each month.

**LiteLLM will send your requests to the `/v1/preview` endpoint when you set `api_version="preview"`.**

- LiteLLM SDK
- OpenAI SDK with LiteLLM Proxy

#### Non-streaming[​](#non-streaming-2 "Direct link to Non-streaming")

Azure Codex Models

```
import litellm

# Non-streaming response with Codex models
response = litellm.responses(
    model="azure/codex-mini",
input="Tell me a three sentence bedtime story about a unicorn.",
    max_output_tokens=100,
    api_key=os.getenv("AZURE_RESPONSES_OPENAI_API_KEY"),
    api_base="https://litellm8397336933.openai.azure.com",
    api_version="preview",# 👈 key difference
)

print(response)
```

#### Streaming[​](#streaming-2 "Direct link to Streaming")

Azure Codex Models

```
import litellm

# Streaming response with Codex models
response = litellm.responses(
    model="azure/codex-mini",
input="Tell me a three sentence bedtime story about a unicorn.",
    stream=True,
    api_key=os.getenv("AZURE_RESPONSES_OPENAI_API_KEY"),
    api_base="https://litellm8397336933.openai.azure.com",
    api_version="preview",# 👈 key difference
)

for event in response:
print(event)
```

## Calling via `/chat/completions`[​](#calling-via-chatcompletions "Direct link to calling-via-chatcompletions")

You can also call the Azure Responses API via the `/chat/completions` endpoint.

- LiteLLM SDK
- OpenAI SDK with LiteLLM Proxy

```
from litellm import completion
import os 

os.environ["AZURE_API_BASE"]="https://my-endpoint-sweden-berri992.openai.azure.com/"
os.environ["AZURE_API_VERSION"]="2023-03-15-preview"
os.environ["AZURE_API_KEY"]="my-api-key"

response = completion(
    model="azure/responses/my-custom-o1-pro",
    messages=[{"role":"user","content":"Hello world"}],
)

print(response)
```