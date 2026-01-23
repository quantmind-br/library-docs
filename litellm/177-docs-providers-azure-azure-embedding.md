---
title: Azure OpenAI Embeddings | liteLLM
url: https://docs.litellm.ai/docs/providers/azure/azure_embedding
source: sitemap
fetched_at: 2026-01-21T19:48:17.932308889-03:00
rendered_js: false
word_count: 97
summary: This document provides instructions on how to configure and use Azure OpenAI embedding models using the LiteLLM library and its proxy server.
tags:
    - litellm
    - azure-openai
    - embeddings
    - proxy-server
    - python-sdk
    - api-configuration
category: guide
---

### API keys[​](#api-keys "Direct link to API keys")

This can be set as env variables or passed as **params to litellm.embedding()**

```
import os
os.environ['AZURE_API_KEY']=
os.environ['AZURE_API_BASE']=
os.environ['AZURE_API_VERSION']=
```

### Usage[​](#usage "Direct link to Usage")

```
from litellm import embedding
response = embedding(
    model="azure/<your deployment name>",
input=["good morning from litellm"],
    api_key=api_key,
    api_base=api_base,
    api_version=api_version,
)
print(response)
```

Model NameFunction Calltext-embedding-ada-002`embedding(model="azure/<your deployment name>", input=input)`

h/t to [Mikko](https://www.linkedin.com/in/mikkolehtimaki/) for this integration

## **Usage - LiteLLM Proxy Server**[​](#usage---litellm-proxy-server "Direct link to usage---litellm-proxy-server")

Here's how to call Azure OpenAI models with the LiteLLM Proxy Server

### 1. Save key in your environment[​](#1-save-key-in-your-environment "Direct link to 1. Save key in your environment")

### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
model_list:
-model_name: text-embedding-ada-002
litellm_params:
model: azure/my-deployment-name
api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
api_version:"2023-05-15"
api_key: os.environ/AZURE_API_KEY # The `os.environ/` prefix tells litellm to read this from the env.
```

### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

- Curl Request
- OpenAI v1.0.0+

```
curl --location 'http://0.0.0.0:4000/embeddings' \
  --header 'Content-Type: application/json' \
  --data ' {
  "model": "text-embedding-ada-002",
  "input": ["write a litellm poem"]
  }'
```