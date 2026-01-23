---
title: GradientAI | liteLLM
url: https://docs.litellm.ai/docs/providers/gradient_ai
source: sitemap
fetched_at: 2026-01-21T19:49:18.783191878-03:00
rendered_js: false
word_count: 20
summary: This document explains how to integrate and use GradientAI models within the LiteLLM framework, covering API key setup and basic request patterns.
tags:
    - litellm
    - gradient-ai
    - python-sdk
    - llm-integration
    - streaming-api
category: guide
---

LiteLLM provides native support for GradientAI models. To use a GradientAI model, specify it as `gradient_ai/<model-name>` in your LiteLLM requests.

```
from litellm import completion
import os

os.environ['GRADIENT_AI_API_KEY']="your-api-key"
response = completion(
    model="gradient_ai/model-name",
    messages=[
{"role":"user","content":"Hello, how are you?"}
],
)
print(response.choices[0].message.content)
```

```
from litellm import completion
import os

os.environ['GRADIENT_AI_API_KEY']="your-api-key"
response = completion(
    model="gradient_ai/model-name",
    messages=[
{"role":"user","content":"Write a story about a robot learning to love"}
],
    stream=True,
)

for chunk in response:
print(chunk.choices[0].delta.content or"", end="")
```