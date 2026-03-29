---
title: provider_specific_params | liteLLM
url: https://docs.litellm.ai/docs/tutorials/provider_specific_params
source: sitemap
fetched_at: 2026-01-21T19:55:49.472723835-03:00
rendered_js: false
word_count: 85
summary: This document explains how LiteLLM automatically maps and translates model parameters like max_tokens across different providers using its completion function and provider-specific configurations.
tags:
    - litellm
    - parameter-mapping
    - max-tokens
    - llm-integration
    - python-library
    - model-configuration
category: guide
---

**1. via completion**

LiteLLM will automatically translate max\_tokens to the naming convention followed by that specific model provider.

```
from litellm import completion
import os

## set ENV variables 
os.environ["OPENAI_API_KEY"]="your-openai-key"
os.environ["COHERE_API_KEY"]="your-cohere-key"

messages =[{"content":"Hello, how are you?","role":"user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages, max_tokens=100)

# cohere call
response = completion(model="command-nightly", messages=messages, max_tokens=100)
print(response)
```

**2. via provider-specific config**

For every provider on LiteLLM, we've gotten their specific params (following their naming conventions, etc.). You can just set it for that provider by pulling up that provider via `litellm.<provider_name>Config`.

All provider configs are typed and have docstrings, so you should see them autocompleted for you in VSCode with an explanation of what it means.

Here's an example of setting max tokens through provider configs.