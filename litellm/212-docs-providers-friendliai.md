---
title: FriendliAI | liteLLM
url: https://docs.litellm.ai/docs/providers/friendliai
source: sitemap
fetched_at: 2026-01-21T19:49:04.54036515-03:00
rendered_js: false
word_count: 68
summary: This document provides instructions and code examples for integrating FriendliAI models with LiteLLM, covering authentication, model naming conventions, and both standard and streaming completion requests.
tags:
    - friendliai
    - litellm-integration
    - llm-inference
    - api-configuration
    - python-sdk
    - streaming-completions
category: guide
---

info

**We support ALL FriendliAI models, just set `friendliai/` as a prefix when sending completion requests**

PropertyDetailsDescriptionThe fastest and most efficient inference engine to build production-ready, compound AI systems.Provider Route on LiteLLM`friendliai/`Provider Doc[FriendliAI ↗](https://friendli.ai/docs/sdk/integrations/litellm)Supported OpenAI Endpoints`/chat/completions`, `/completions`

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['FRIENDLI_TOKEN']
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['FRIENDLI_TOKEN']=""
response = completion(
    model="friendliai/meta-llama-3.1-8b-instruct",
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

os.environ['FRIENDLI_TOKEN']=""
response = completion(
    model="friendliai/meta-llama-3.1-8b-instruct",
    messages=[
{"role":"user","content":"hello from litellm"}
],
    stream=True
)

for chunk in response:
print(chunk)
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

We support ALL FriendliAI AI models, just set `friendliai/` as a prefix when sending completion requests

Model NameFunction Callmeta-llama-3.1-8b-instruct`completion(model="friendliai/meta-llama-3.1-8b-instruct", messages)`meta-llama-3.1-70b-instruct`completion(model="friendliai/meta-llama-3.1-70b-instruct", messages)`