---
title: NLP Cloud | liteLLM
url: https://docs.litellm.ai/docs/providers/nlp_cloud
source: sitemap
fetched_at: 2026-01-21T19:49:49.059291066-03:00
rendered_js: false
word_count: 54
summary: This document provides instructions on how to integrate and use LiteLLM with NLP Cloud, covering API key configuration, basic usage, streaming, and custom model mapping.
tags:
    - litellm
    - nlp-cloud
    - python-sdk
    - api-integration
    - streaming
    - llm-provider
category: guide
---

LiteLLM supports all LLMs on NLP Cloud.

## API Keys[​](#api-keys "Direct link to API Keys")

```
import os 

os.environ["NLP_CLOUD_API_KEY"]="your-api-key"
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
import os
from litellm import completion 

# set env
os.environ["NLP_CLOUD_API_KEY"]="your-api-key"

messages =[{"role":"user","content":"Hey! how's it going?"}]
response = completion(model="dolphin", messages=messages)
print(response)
```

## streaming[​](#streaming "Direct link to streaming")

Just set `stream=True` when calling completion.

```
import os
from litellm import completion 

# set env
os.environ["NLP_CLOUD_API_KEY"]="your-api-key"

messages =[{"role":"user","content":"Hey! how's it going?"}]
response = completion(model="dolphin", messages=messages, stream=True)
for chunk in response:
print(chunk["choices"][0]["delta"]["content"])# same as openai format
```

## non-dolphin models[​](#non-dolphin-models "Direct link to non-dolphin models")

By default, LiteLLM will map `dolphin` and `chatdolphin` to nlp cloud.

If you're trying to call any other model (e.g. GPT-J, Llama-2, etc.) with nlp cloud, just set it as your custom llm provider.

```
import os
from litellm import completion 

# set env - [OPTIONAL] replace with your nlp cloud key
os.environ["NLP_CLOUD_API_KEY"]="your-api-key"

messages =[{"role":"user","content":"Hey! how's it going?"}]

# e.g. to call Llama2 on NLP Cloud
response = completion(model="nlp_cloud/finetuned-llama-2-70b", messages=messages, stream=True)
for chunk in response:
print(chunk["choices"][0]["delta"]["content"])# same as openai format
```