---
title: Calling Finetuned Models | liteLLM
url: https://docs.litellm.ai/docs/guides/finetuned_models
source: sitemap
fetched_at: 2026-01-21T19:45:23.480407964-03:00
rendered_js: false
word_count: 43
summary: This document provides the syntax and configuration details for calling fine-tuned models from OpenAI and Vertex AI using the LiteLLM library.
tags:
    - litellm
    - openai
    - vertex-ai
    - fine-tuning
    - model-configuration
    - python-sdk
category: reference
---

## OpenAI[​](#openai "Direct link to OpenAI")

Model NameFunction Callfine tuned `gpt-4-0613``response = completion(model="ft:gpt-4-0613", messages=messages)`fine tuned `gpt-4o-2024-05-13``response = completion(model="ft:gpt-4o-2024-05-13", messages=messages)`fine tuned `gpt-3.5-turbo-0125``response = completion(model="ft:gpt-3.5-turbo-0125", messages=messages)`fine tuned `gpt-3.5-turbo-1106``response = completion(model="ft:gpt-3.5-turbo-1106", messages=messages)`fine tuned `gpt-3.5-turbo-0613``response = completion(model="ft:gpt-3.5-turbo-0613", messages=messages)`

## Vertex AI[​](#vertex-ai "Direct link to Vertex AI")

Fine tuned models on vertex have a numerical model/endpoint id.

- SDK
- PROXY

```
from litellm import completion
import os

## set ENV variables
os.environ["VERTEXAI_PROJECT"]="hardy-device-38811"
os.environ["VERTEXAI_LOCATION"]="us-central1"

response = completion(
  model="vertex_ai/<your-finetuned-model>",# e.g. vertex_ai/4965075652664360960
  messages=[{"content":"Hello, how are you?","role":"user"}],
  base_model="vertex_ai/gemini-1.5-pro"# the base model - used for routing
)
```