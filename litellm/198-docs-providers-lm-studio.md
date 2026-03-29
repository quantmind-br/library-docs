---
title: LM Studio | liteLLM
url: https://docs.litellm.ai/docs/providers/lm_studio
source: sitemap
fetched_at: 2026-01-21T19:49:35.923181728-03:00
rendered_js: false
word_count: 122
summary: This document provides instructions for integrating LM Studio models with LiteLLM, covering configuration, chat completions, streaming, embeddings, and structured outputs.
tags:
    - lm-studio
    - litellm
    - local-llm
    - python-sdk
    - embeddings
    - structured-outputs
    - api-proxy
category: guide
---

[https://lmstudio.ai/docs/basics/server](https://lmstudio.ai/docs/basics/server)

tip

**We support ALL LM Studio models, just set `model=lm_studio/<any-model-on-lmstudio>` as a prefix when sending litellm requests**

PropertyDetailsDescriptionDiscover, download, and run local LLMs.Provider Route on LiteLLM`lm_studio/`Provider Doc[LM Studio ↗](https://lmstudio.ai/docs/api/openai-api)Supported OpenAI Endpoints`/chat/completions`, `/embeddings`, `/completions`

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['LM_STUDIO_API_BASE']
os.environ['LM_STUDIO_API_KEY']# optional, default is empty
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['LM_STUDIO_API_BASE']=""

response = completion(
    model="lm_studio/llama-3-8b-instruct",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit?",
}
]
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['LM_STUDIO_API_KEY']=""
response = completion(
    model="lm_studio/llama-3-8b-instruct",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit?",
}
],
    stream=True,
)

for chunk in response:
print(chunk)
```

## Usage with LiteLLM Proxy Server[​](#usage-with-litellm-proxy-server "Direct link to Usage with LiteLLM Proxy Server")

Here's how to call a LM Studio model with the LiteLLM Proxy Server

1. Modify the config.yaml

```
model_list:
-model_name: my-model
litellm_params:
model: lm_studio/<your-model-name># add lm_studio/ prefix to route as LM Studio provider
api_key: api-key                 # api key to send your model
```

2. Start the proxy

```
$ litellm --config /path/to/config.yaml
```

3. Send Request to LiteLLM Proxy Server

<!--THE END-->

- OpenAI Python v1.0.0+
- curl

```
import openai
client = openai.OpenAI(
    api_key="sk-1234",# pass litellm proxy key, if you're using virtual keys
    base_url="http://0.0.0.0:4000"# litellm-proxy-base url
)

response = client.chat.completions.create(
    model="my-model",
    messages =[
{
"role":"user",
"content":"what llm are you"
}
],
)

print(response)
```

## Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

See [Supported Parameters](https://docs.litellm.ai/docs/completion/input#translated-openai-params) for supported parameters.

## Embedding[​](#embedding "Direct link to Embedding")

```
from litellm import embedding
import os 

os.environ['LM_STUDIO_API_BASE']="http://localhost:8000"
response = embedding(
    model="lm_studio/jina-embeddings-v3",
input=["Hello world"],
)
print(response)
```

## Structured Output[​](#structured-output "Direct link to Structured Output")

LM Studio supports structured outputs via JSON Schema. You can pass a pydantic model or a raw schema using `response_format`. LiteLLM sends the schema as `{ "type": "json_schema", "json_schema": {"schema": <your schema>} }`.

```
from pydantic import BaseModel
from litellm import completion

classBook(BaseModel):
    title:str
    author:str
    year:int

response = completion(
    model="lm_studio/llama-3-8b-instruct",
    messages=[{"role":"user","content":"Tell me about The Hobbit"}],
    response_format=Book,
)
print(response.choices[0].message.content)
```