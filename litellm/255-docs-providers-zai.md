---
title: Z.AI (Zhipu AI) | liteLLM
url: https://docs.litellm.ai/docs/providers/zai
source: sitemap
fetched_at: 2026-01-21T19:51:02.365791104-03:00
rendered_js: false
word_count: 84
summary: This document provides instructions and code examples for integrating Z.AI GLM text and chat models with LiteLLM, covering API configuration, streaming, and model pricing.
tags:
    - z-ai
    - litellm
    - glm-models
    - api-integration
    - python-sdk
    - streaming
    - llm-pricing
category: guide
---

[https://z.ai/](https://z.ai/)

**We support Z.AI GLM text/chat models, just set `zai/` as a prefix when sending completion requests**

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['ZAI_API_KEY']
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['ZAI_API_KEY']=""
response = completion(
    model="zai/glm-4.7",
    messages=[
{"role":"user","content":"hello from litellm"}
],
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['ZAI_API_KEY']=""
response = completion(
    model="zai/glm-4.7",
    messages=[
{"role":"user","content":"hello from litellm"}
],
    stream=True
)

for chunk in response:
print(chunk)
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

We support ALL Z.AI GLM models, just set `zai/` as a prefix when sending completion requests.

Model NameFunction CallNotesglm-4.7`completion(model="zai/glm-4.7", messages)`**Latest flagship**, 200K context, **Reasoning**glm-4.6`completion(model="zai/glm-4.6", messages)`200K contextglm-4.5`completion(model="zai/glm-4.5", messages)`128K contextglm-4.5v`completion(model="zai/glm-4.5v", messages)`Vision modelglm-4.5-x`completion(model="zai/glm-4.5-x", messages)`Premium tierglm-4.5-air`completion(model="zai/glm-4.5-air", messages)`Lightweightglm-4.5-airx`completion(model="zai/glm-4.5-airx", messages)`Fast lightweightglm-4-32b-0414-128k`completion(model="zai/glm-4-32b-0414-128k", messages)`32B parameter modelglm-4.5-flash`completion(model="zai/glm-4.5-flash", messages)`**FREE tier**

## Model Pricing[​](#model-pricing "Direct link to Model Pricing")

ModelInput ($/1M tokens)Output ($/1M tokens)Cached Input ($/1M tokens)Context Windowglm-4.7$0.60$2.20$0.11200Kglm-4.6$0.60$2.20-200Kglm-4.5$0.60$2.20-128Kglm-4.5v$0.60$1.80-128Kglm-4.5-x$2.20$8.90-128Kglm-4.5-air$0.20$1.10-128Kglm-4.5-airx$1.10$4.50-128Kglm-4-32b-0414-128k$0.10$0.10-128Kglm-4.5-flash**FREE****FREE**-128K

## Using with LiteLLM Proxy[​](#using-with-litellm-proxy "Direct link to Using with LiteLLM Proxy")

- SDK
- PROXY

```
from litellm import completion
import os

os.environ['ZAI_API_KEY']=""
response = completion(
    model="zai/glm-4.7",
    messages=[{"role":"user","content":"Hello, how are you?"}],
)

print(response.choices[0].message.content)
```