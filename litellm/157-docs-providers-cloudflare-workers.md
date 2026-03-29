---
title: Cloudflare Workers AI | liteLLM
url: https://docs.litellm.ai/docs/providers/cloudflare_workers
source: sitemap
fetched_at: 2026-01-21T19:48:43.666115279-03:00
rendered_js: false
word_count: 25
summary: This document provides instructions and code samples for integrating Cloudflare Workers AI text generation models using the LiteLLM library, covering environment setup and both standard and streaming usage.
tags:
    - cloudflare-workers-ai
    - litellm
    - text-generation
    - python
    - llm-streaming
    - api-configuration
category: tutorial
---

[https://developers.cloudflare.com/workers-ai/models/text-generation/](https://developers.cloudflare.com/workers-ai/models/text-generation/)

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['CLOUDFLARE_API_KEY']="3dnSGlxxxx"
os.environ['CLOUDFLARE_ACCOUNT_ID']="03xxxxx"
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['CLOUDFLARE_API_KEY']="3dnSGlxxxx"
os.environ['CLOUDFLARE_ACCOUNT_ID']="03xxxxx"

response = completion(
    model="cloudflare/@cf/meta/llama-2-7b-chat-int8",
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

os.environ['CLOUDFLARE_API_KEY']="3dnSGlxxxx"
os.environ['CLOUDFLARE_ACCOUNT_ID']="03xxxxx"

response = completion(
    model="cloudflare/@hf/thebloke/codellama-7b-instruct-awq",
    messages=[
{"role":"user","content":"hello from litellm"}
],
    stream=True
)

for chunk in response:
print(chunk)
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

All models listed here [https://developers.cloudflare.com/workers-ai/models/text-generation/](https://developers.cloudflare.com/workers-ai/models/text-generation/) are supported

Model NameFunction Call@cf/meta/llama-2-7b-chat-fp16`completion(model="mistral/mistral-tiny", messages)`@cf/meta/llama-2-7b-chat-int8`completion(model="mistral/mistral-small", messages)`@cf/mistral/mistral-7b-instruct-v0.1`completion(model="mistral/mistral-medium", messages)`@hf/thebloke/codellama-7b-instruct-awq`completion(model="codellama/codellama-medium", messages)`