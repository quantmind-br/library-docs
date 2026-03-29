---
title: Oobabooga Text Web API Tutorial | liteLLM
url: https://docs.litellm.ai/docs/tutorials/oobabooga
source: sitemap
fetched_at: 2026-01-21T19:55:42.521082145-03:00
rendered_js: false
word_count: 23
summary: This document explains how to integrate LiteLLM with a local Oobabooga model server to perform text completion tasks. It covers installation, basic configuration, and API usage for calling local LLMs.
tags:
    - litellm
    - oobabooga
    - local-llm
    - python-api
    - text-generation
    - llm-inference
category: tutorial
---

### Install + Import LiteLLM[​](#install--import-litellm "Direct link to Install + Import LiteLLM")

```
!pip install litellm
from litellm import completion 
import os
```

### Call your oobabooga model[​](#call-your-oobabooga-model "Direct link to Call your oobabooga model")

Remember to set your api\_base

```
response = completion(
  model="oobabooga/WizardCoder-Python-7B-V1.0-GPTQ",
  messages=[{"content":"can you write a binary tree traversal preorder","role":"user"}],
  api_base="http://localhost:5000",
  max_tokens=4000
)
```

### See your response[​](#see-your-response "Direct link to See your response")

```
print(response)
```

Credits to [Shuai Shao](https://www.linkedin.com/in/shuai-sh/), for this tutorial.