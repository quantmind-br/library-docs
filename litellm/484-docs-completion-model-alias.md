---
title: Model Alias | liteLLM
url: https://docs.litellm.ai/docs/completion/model_alias
source: sitemap
fetched_at: 2026-01-21T19:44:35.403810071-03:00
rendered_js: false
word_count: 39
summary: This document explains how to use LiteLLM's model alias mapping feature to link user-friendly display names to specific backend model identifiers. It allows developers to simplify model invocation and manage model versioning through a centralized mapping.
tags:
    - litellm
    - model-aliasing
    - python
    - llm-api
    - configuration-management
category: configuration
---

The model name you show an end-user might be different from the one you pass to LiteLLM - e.g. Displaying `GPT-3.5` while calling `gpt-3.5-turbo-16k` on the backend.

LiteLLM simplifies this by letting you pass in a model alias mapping.

```
import litellm 
from litellm import completion 


## set ENV variables
os.environ["OPENAI_API_KEY"]="openai key"
os.environ["REPLICATE_API_KEY"]="cohere key"

## set model alias map
model_alias_map ={
"GPT-3.5":"gpt-3.5-turbo-16k",
"llama2":"replicate/llama-2-70b-chat:2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf"
}

litellm.model_alias_map = model_alias_map

messages =[{"content":"Hello, how are you?","role":"user"}]

# call "gpt-3.5-turbo-16k"
response = completion(model="GPT-3.5", messages=messages)

# call replicate/llama-2-70b-chat:2796ee9483c3fd7aa2e171d38f4ca1...
response = completion("llama2", messages)
```