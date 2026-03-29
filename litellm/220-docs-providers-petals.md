---
title: Petals | liteLLM
url: https://docs.litellm.ai/docs/providers/petals
source: sitemap
fetched_at: 2026-01-21T19:50:07.252165738-03:00
rendered_js: false
word_count: 39
summary: This document provides instructions and code examples for integrating and running Petals large language models using the LiteLLM library, including support for streaming responses.
tags:
    - petals
    - litellm
    - python
    - llm-integration
    - streaming
    - decentralized-inference
category: guide
---

Petals: [https://github.com/bigscience-workshop/petals](https://github.com/bigscience-workshop/petals)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/LiteLLM_Petals.ipynb)

## Pre-Requisites[​](#pre-requisites "Direct link to Pre-Requisites")

Ensure you have `petals` installed

```
pip install git+https://github.com/bigscience-workshop/petals
```

## Usage[​](#usage "Direct link to Usage")

Ensure you add `petals/` as a prefix for all petals LLMs. This sets the custom\_llm\_provider to petals

```
from litellm import completion

response = completion(
    model="petals/petals-team/StableBeluga2",
    messages=[{"content":"Hello, how are you?","role":"user"}]
)

print(response)
```

## Usage with Streaming[​](#usage-with-streaming "Direct link to Usage with Streaming")

```
response = completion(
    model="petals/petals-team/StableBeluga2",
    messages=[{"content":"Hello, how are you?","role":"user"}],
    stream=True
)

print(response)
for chunk in response:
print(chunk)
```

### Model Details[​](#model-details "Direct link to Model Details")

Model NameFunction Callpetals-team/StableBeluga`completion('petals/petals-team/StableBeluga2', messages)`huggyllama/llama-65b`completion('petals/huggyllama/llama-65b', messages)`