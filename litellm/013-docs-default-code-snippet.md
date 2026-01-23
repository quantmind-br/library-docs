---
title: Get Started | liteLLM
url: https://docs.litellm.ai/docs/default_code_snippet
source: sitemap
fetched_at: 2026-01-21T19:45:05.072037806-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to use the litellm library to make standardized completion calls across different LLM providers like OpenAI and Cohere using a unified Python interface.
tags:
    - litellm
    - python-sdk
    - llm-integration
    - openai
    - cohere
    - completion-api
category: tutorial
---

```
from litellm import completion

## set ENV variables
os.environ["OPENAI_API_KEY"] = "openai key"
os.environ["COHERE_API_KEY"] = "cohere key"


messages = [{ "content": "Hello, how are you?","role": "user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages)

# cohere call
response = completion("command-nightly", messages)
```