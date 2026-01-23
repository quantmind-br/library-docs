---
title: Perplexity AI (pplx-api) | liteLLM
url: https://docs.litellm.ai/docs/providers/perplexity
source: sitemap
fetched_at: 2026-01-21T19:50:06.33173901-03:00
rendered_js: false
word_count: 66
summary: This document provides instructions and code examples for integrating Perplexity AI models with the LiteLLM library, covering API key configuration, streaming, and reasoning parameters.
tags:
    - litellm
    - perplexity-ai
    - api-integration
    - python-sdk
    - streaming
    - reasoning-effort
    - llm-models
category: api
---

[https://www.perplexity.ai](https://www.perplexity.ai)

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['PERPLEXITYAI_API_KEY']
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['PERPLEXITYAI_API_KEY']=""
response = completion(
    model="perplexity/sonar-pro",
    messages=messages
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['PERPLEXITYAI_API_KEY']=""
response = completion(
    model="perplexity/sonar-pro",
    messages=messages,
    stream=True
)

for chunk in response:
print(chunk)
```

## Reasoning Effort[​](#reasoning-effort "Direct link to Reasoning Effort")

Requires v1.72.6+

info

See full guide on Reasoning with LiteLLM [here](https://docs.litellm.ai/docs/reasoning_content)

You can set the reasoning effort by setting the `reasoning_effort` parameter.

- SDK
- Proxy

```
from litellm import completion
import os

os.environ['PERPLEXITYAI_API_KEY']=""
response = completion(
    model="perplexity/sonar-reasoning",
    messages=messages,
    reasoning_effort="high"
)
print(response)
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

All models listed here [https://docs.perplexity.ai/docs/model-cards](https://docs.perplexity.ai/docs/model-cards) are supported. Just do `model=perplexity/<model-name>`.

Model NameFunction Callsonar-deep-research`completion(model="perplexity/sonar-deep-research", messages)`sonar-reasoning-pro`completion(model="perplexity/sonar-reasoning-pro", messages)`sonar-reasoning`completion(model="perplexity/sonar-reasoning", messages)`sonar-pro`completion(model="perplexity/sonar-pro", messages)`sonar`completion(model="perplexity/sonar", messages)`r1-1776`completion(model="perplexity/r1-1776", messages)`

info

For more information about passing provider-specific parameters, [go here](https://docs.litellm.ai/docs/completion/provider_specific_params)