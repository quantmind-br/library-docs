---
title: DeepInfra | liteLLM
url: https://docs.litellm.ai/docs/providers/deepinfra
source: sitemap
fetched_at: 2026-01-21T19:48:54.850617052-03:00
rendered_js: false
word_count: 118
summary: This document provides instructions and code examples for integrating DeepInfra's chat and rerank models using the LiteLLM library, covering configuration, streaming, and supported API parameters.
tags:
    - deepinfra
    - litellm
    - llm-integration
    - rerank-api
    - chat-completion
    - python-sdk
category: guide
---

[https://deepinfra.com/](https://deepinfra.com/)

tip

**We support ALL DeepInfra models, just set `model=deepinfra/<any-model-on-deepinfra>` as a prefix when sending litellm requests**

## Table of Contents[​](#table-of-contents "Direct link to Table of Contents")

- [API Key](#api-key)
- [Chat Models](#chat-models)
- [Rerank Endpoint](#rerank-endpoint)

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['DEEPINFRA_API_KEY']
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['DEEPINFRA_API_KEY']=""
response = completion(
    model="deepinfra/meta-llama/Llama-2-70b-chat-hf",
    messages=[{"role":"user","content":"write code for saying hi from LiteLLM"}]
)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['DEEPINFRA_API_KEY']=""
response = completion(
    model="deepinfra/meta-llama/Llama-2-70b-chat-hf",
    messages=[{"role":"user","content":"write code for saying hi from LiteLLM"}],
    stream=True
)

for chunk in response:
print(chunk)
```

## Chat Models[​](#chat-models "Direct link to Chat Models")

Model NameFunction Callmeta-llama/Meta-Llama-3-8B-Instruct`completion(model="deepinfra/meta-llama/Meta-Llama-3-8B-Instruct", messages)`meta-llama/Meta-Llama-3-70B-Instruct`completion(model="deepinfra/meta-llama/Meta-Llama-3-70B-Instruct", messages)`meta-llama/Llama-2-70b-chat-hf`completion(model="deepinfra/meta-llama/Llama-2-70b-chat-hf", messages)`meta-llama/Llama-2-7b-chat-hf`completion(model="deepinfra/meta-llama/Llama-2-7b-chat-hf", messages)`meta-llama/Llama-2-13b-chat-hf`completion(model="deepinfra/meta-llama/Llama-2-13b-chat-hf", messages)`codellama/CodeLlama-34b-Instruct-hf`completion(model="deepinfra/codellama/CodeLlama-34b-Instruct-hf", messages)`mistralai/Mistral-7B-Instruct-v0.1`completion(model="deepinfra/mistralai/Mistral-7B-Instruct-v0.1", messages)`jondurbin/airoboros-l2-70b-gpt4-1.4.1`completion(model="deepinfra/jondurbin/airoboros-l2-70b-gpt4-1.4.1", messages)`

## Rerank Endpoint[​](#rerank-endpoint "Direct link to Rerank Endpoint")

LiteLLM provides a Cohere API compatible `/rerank` endpoint for DeepInfra rerank models.

### Supported Rerank Models[​](#supported-rerank-models "Direct link to Supported Rerank Models")

Model NameDescription`deepinfra/Qwen/Qwen3-Reranker-0.6B`Lightweight rerank model (0.6B parameters)`deepinfra/Qwen/Qwen3-Reranker-4B`Medium rerank model (4B parameters)`deepinfra/Qwen/Qwen3-Reranker-8B`Large rerank model (8B parameters)

### Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

- SDK
- PROXY

```
from litellm import rerank
import os

os.environ["DEEPINFRA_API_KEY"]="your-api-key"

response = rerank(
    model="deepinfra/Qwen/Qwen3-Reranker-0.6B",
    query="What is the capital of France?",
    documents=[
"Paris is the capital of France.",
"London is the capital of the United Kingdom.",
"Berlin is the capital of Germany.",
"Madrid is the capital of Spain.",
"Rome is the capital of Italy."
]
)
print(response)
```

### Supported Cohere Rerank API Params[​](#supported-cohere-rerank-api-params "Direct link to Supported Cohere Rerank API Params")

ParamTypeDescription`query``str`The query to rerank the documents against`documents``list[str]`The documents to rerank

### Provider-specific parameters[​](#provider-specific-parameters "Direct link to Provider-specific parameters")

Pass any deepinfra specific parameters as a keyword argument to the rerank function, e.g.

```
response = rerank(
    model="deepinfra/Qwen/Qwen3-Reranker-0.6B",
    query="What is the capital of France?",
    documents=[
        "Paris is the capital of France.",
        "London is the capital of the United Kingdom.",
        "Berlin is the capital of Germany.",
        "Madrid is the capital of Spain.",
        "Rome is the capital of Italy."
    ],
    my_custom_param="my_custom_value", # any other deepinfra specific parameters
)
```

### Response Format[​](#response-format "Direct link to Response Format")

```
{
"id":"request-id",
"results":[
{
"index":0,
"relevance_score":0.9975274205207825
},
{
"index":1,
"relevance_score":0.011687257327139378
}
],
"meta":{
"billed_units":{
"total_tokens":427
},
"tokens":{
"input_tokens":427,
"output_tokens":0
}
}
}
```