---
title: Using Fine-Tuned gpt-3.5-turbo | liteLLM
url: https://docs.litellm.ai/docs/tutorials/finetuned_chat_gpt
source: sitemap
fetched_at: 2026-01-21T19:55:20.916584779-03:00
rendered_js: false
word_count: 40
summary: This document explains how to use the LiteLLM library to call fine-tuned OpenAI models and configure environment variables such as the API key and Organization ID.
tags:
    - litellm
    - openai
    - fine-tuned-models
    - api-configuration
    - python-sdk
    - environment-variables
category: guide
---

Once you've created your fine-tuned model, you can call it with `litellm.completion()`

```
import os
from litellm import completion

# LiteLLM reads from your .env
os.environ["OPENAI_API_KEY"]="your-api-key"

response = completion(
  model="ft:gpt-3.5-turbo:my-org:custom_suffix:id",
  messages=[
{"role":"system","content":"You are a helpful assistant."},
{"role":"user","content":"Hello!"}
]
)

print(response.choices[0].message)
```

LiteLLM allows you to specify your OpenAI Organization when calling OpenAI LLMs. More details here: [setting Organization ID](https://docs.litellm.ai/docs/providers/openai#setting-organization-id-for-completion-calls) This can be set in one of the following ways:

```
import os
from litellm import completion

# LiteLLM reads from your .env
os.environ["OPENAI_API_KEY"]="your-api-key"
os.environ["OPENAI_ORGANIZATION"]="your-org-id"# Optional

response = completion(
  model="ft:gpt-3.5-turbo:my-org:custom_suffix:id",
  messages=[
{"role":"system","content":"You are a helpful assistant."},
{"role":"user","content":"Hello!"}
]
)

print(response.choices[0].message)
```