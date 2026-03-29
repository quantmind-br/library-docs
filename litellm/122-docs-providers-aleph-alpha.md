---
title: Aleph Alpha | liteLLM
url: https://docs.litellm.ai/docs/providers/aleph_alpha
source: sitemap
fetched_at: 2026-01-21T19:47:49.729827085-03:00
rendered_js: false
word_count: 36
summary: This document provides instructions for using Aleph Alpha models with LiteLLM, including API key configuration and a list of supported model identifiers.
tags:
    - litellm
    - aleph-alpha
    - llm-integration
    - model-support
category: reference
---

LiteLLM supports all models from [Aleph Alpha](https://www.aleph-alpha.com/).

Like AI21 and Cohere, you can use these models without a waitlist.

### API KEYS[​](#api-keys "Direct link to API KEYS")

```
import os
os.environ["ALEPHALPHA_API_KEY"]=""
```

### Aleph Alpha Models[​](#aleph-alpha-models "Direct link to Aleph Alpha Models")

[https://www.aleph-alpha.com/](https://www.aleph-alpha.com/)

Model NameFunction CallRequired OS Variablesluminous-base`completion(model='luminous-base', messages=messages)``os.environ['ALEPHALPHA_API_KEY']`luminous-base-control`completion(model='luminous-base-control', messages=messages)``os.environ['ALEPHALPHA_API_KEY']`luminous-extended`completion(model='luminous-extended', messages=messages)``os.environ['ALEPHALPHA_API_KEY']`luminous-extended-control`completion(model='luminous-extended-control', messages=messages)``os.environ['ALEPHALPHA_API_KEY']`luminous-supreme`completion(model='luminous-supreme', messages=messages)``os.environ['ALEPHALPHA_API_KEY']`luminous-supreme-control`completion(model='luminous-supreme-control', messages=messages)``os.environ['ALEPHALPHA_API_KEY']`