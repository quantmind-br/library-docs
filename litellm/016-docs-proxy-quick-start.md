---
title: CLI - Quick Start | liteLLM
url: https://docs.litellm.ai/docs/proxy/quick_start
source: sitemap
fetched_at: 2026-01-21T19:53:24.441068088-03:00
rendered_js: false
word_count: 317
summary: This document provides a comprehensive guide for setting up and using the LiteLLM Proxy to manage multiple LLM providers through a unified OpenAI-compatible interface. It explains installation via CLI, configuration using YAML files, load balancing, and debugging procedures.
tags:
    - litellm-proxy
    - llm-gateway
    - cli-setup
    - model-routing
    - load-balancing
    - openai-interface
    - api-gateway
category: guide
---

Setup LiteLLM Proxy quickly via CLI.

LiteLLM Server (LLM Gateway) manages:

- **Unified Interface**: Calling 100+ LLMs [Huggingface/Bedrock/TogetherAI/etc.](#other-supported-models) in the OpenAI `ChatCompletions` & `Completions` format
- **Cost tracking**: Authentication, Spend Tracking & Budgets [Virtual Keys](https://docs.litellm.ai/docs/proxy/virtual_keys)
- **Load Balancing**: between [Multiple Models](#multiple-models---quick-start) + [Deployments of the same model](#multiple-instances-of-1-model) - LiteLLM proxy can handle 1.5k+ requests/second during load tests.

```
$ pip install 'litellm[proxy]'
```

## Quick Start - LiteLLM Proxy CLI[​](#quick-start---litellm-proxy-cli "Direct link to Quick Start - LiteLLM Proxy CLI")

Run the following command to start the litellm proxy

```
$ litellm --model huggingface/bigcode/starcoder

#INFO: Proxy running on http://0.0.0.0:4000
```

info

Run with `--detailed_debug` if you need detailed debug logs

```
$ litellm --model huggingface/bigcode/starcoder --detailed_debug
```

### Test[​](#test "Direct link to Test")

In a new shell, run, this will make an `openai.chat.completions` request. Ensure you're using openai v1.0.0+

This will now automatically route any requests for gpt-3.5-turbo to bigcode starcoder, hosted on huggingface inference endpoints.

### Supported LLMs[​](#supported-llms "Direct link to Supported LLMs")

All LiteLLM supported LLMs are supported on the Proxy. Seel all [supported llms](https://docs.litellm.ai/docs/providers)

- AWS Bedrock
- Azure OpenAI
- OpenAI
- Ollama
- OpenAI Compatible Endpoint
- Vertex AI \[Gemini]
- Huggingface (TGI) Deployed
- Huggingface (TGI) Local
- AWS Sagemaker
- Anthropic
- VLLM
- TogetherAI
- Replicate
- Petals
- Palm
- AI21
- Cohere

```
$ export AWS_ACCESS_KEY_ID=
$ export AWS_REGION_NAME=
$ export AWS_SECRET_ACCESS_KEY=
```

```
$ litellm --model bedrock/anthropic.claude-v2
```

## Quick Start - LiteLLM Proxy + Config.yaml[​](#quick-start---litellm-proxy--configyaml "Direct link to Quick Start - LiteLLM Proxy + Config.yaml")

The config allows you to create a model list and set `api_base`, `max_tokens` (all litellm params). See more details about the config [here](https://docs.litellm.ai/docs/proxy/configs)

### Create a Config for LiteLLM Proxy[​](#create-a-config-for-litellm-proxy "Direct link to Create a Config for LiteLLM Proxy")

Example config

```
model_list:
-model_name: gpt-3.5-turbo # user-facing model alias
litellm_params:# all params accepted by litellm.completion() - https://docs.litellm.ai/docs/completion/input
model: azure/<your-deployment-name>
api_base: <your-azure-api-endpoint>
api_key: <your-azure-api-key>
-model_name: gpt-3.5-turbo
litellm_params:
model: azure/gpt-turbo-small-ca
api_base: https://my-endpoint-canada-berri992.openai.azure.com/
api_key: <your-azure-api-key>
-model_name: vllm-model
litellm_params:
model: openai/<your-model-name>
api_base: <your-vllm-api-base># e.g. http://0.0.0.0:3000/v1
api_key: <your-vllm-api-key|none>
```

### Run proxy with config[​](#run-proxy-with-config "Direct link to Run proxy with config")

```
litellm --config your_config.yaml
```

## Using LiteLLM Proxy - Curl Request, OpenAI Package, Langchain[​](#using-litellm-proxy---curl-request-openai-package-langchain "Direct link to Using LiteLLM Proxy - Curl Request, OpenAI Package, Langchain")

info

LiteLLM is compatible with several SDKs - including OpenAI SDK, Anthropic SDK, Mistral SDK, LLamaIndex, Langchain (Js, Python)

[More examples here](https://docs.litellm.ai/docs/proxy/user_keys)

- Curl Request
- OpenAI v1.0.0+
- Langchain
- Langchain Embeddings
- LiteLLM SDK
- Anthropic Python SDK

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ]
    }
'
```

[**More Info**](https://docs.litellm.ai/docs/proxy/configs)

## 📖 Proxy Endpoints - [Swagger Docs](https://litellm-api.up.railway.app/)[​](#-proxy-endpoints---swagger-docs "Direct link to -proxy-endpoints---swagger-docs")

- POST `/chat/completions` - chat completions endpoint to call 100+ LLMs
- POST `/completions` - completions endpoint
- POST `/embeddings` - embedding endpoint for Azure, OpenAI, Huggingface endpoints
- GET `/models` - available models on server
- POST `/key/generate` - generate a key to access the proxy

## Debugging Proxy[​](#debugging-proxy "Direct link to Debugging Proxy")

Events that occur during normal operation

```
litellm --model gpt-3.5-turbo --debug
```

Detailed information

```
litellm --model gpt-3.5-turbo --detailed_debug
```

### Set Debug Level using env variables[​](#set-debug-level-using-env-variables "Direct link to Set Debug Level using env variables")

Events that occur during normal operation

Detailed information

No Logs