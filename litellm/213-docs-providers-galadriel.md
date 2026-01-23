---
title: Galadriel | liteLLM
url: https://docs.litellm.ai/docs/providers/galadriel
source: sitemap
fetched_at: 2026-01-21T19:49:05.132134538-03:00
rendered_js: false
word_count: 52
summary: This document explains how to integrate Galadriel AI models with LiteLLM, including environment variable setup and model naming conventions.
tags:
    - litellm
    - galadriel
    - model-integration
    - python-sdk
    - api-key
category: tutorial
---

LiteLLM supports all models on Galadriel.

```
from litellm import completion
import os

os.environ['GALADRIEL_API_KEY']=""
response = completion(
    model="galadriel/llama3.1",
    messages=[
{"role":"user","content":"hello from litellm"}
],
    stream=True
)

for chunk in response:
print(chunk)
```

We support ALL Galadriel AI models, just set `galadriel/` as a prefix when sending completion requests

We support both the complete model name and the simplified name match.

You can specify the model name either with the full name or with a simplified version e.g. `llama3.1:70b`