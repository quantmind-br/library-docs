---
title: Promptlayer Tutorial | liteLLM
url: https://docs.litellm.ai/docs/observability/promptlayer_integration
source: sitemap
fetched_at: 2026-01-21T19:46:27.731730144-03:00
rendered_js: false
word_count: 62
summary: This document explains how to integrate liteLLM with Promptlayer using success callbacks to log and track LLM requests and metadata across multiple providers.
tags:
    - litellm
    - promptlayer
    - logging
    - callbacks
    - llm-monitoring
    - integration
category: guide
---

Promptlayer is a platform for prompt engineers. Log OpenAI requests. Search usage history. Track performance. Visually manage prompt templates.

liteLLM provides `callbacks`, making it easy for you to log data depending on the status of your responses.

Use just 2 lines of code, to instantly log your responses **across all providers** with promptlayer:

```
from litellm import completion

## set env variables
os.environ["PROMPTLAYER_API_KEY"]="your-promptlayer-key"

os.environ["OPENAI_API_KEY"], os.environ["COHERE_API_KEY"]="",""

# set callbacks
litellm.success_callback =["promptlayer"]

#openai call
response = completion(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hi 👋 - i'm openai"}])

#cohere call
response = completion(model="command-nightly", messages=[{"role":"user","content":"Hi 👋 - i'm cohere"}])
```

You can also log completion call metadata to Promptlayer.

```
from litellm import completion

## set env variables
os.environ["PROMPTLAYER_API_KEY"]="your-promptlayer-key"

os.environ["OPENAI_API_KEY"], os.environ["COHERE_API_KEY"]="",""

# set callbacks
litellm.success_callback =["promptlayer"]

#openai call - log llm provider is openai
response = completion(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hi 👋 - i'm openai"}], metadata={"provider":"openai"})

#cohere call - log llm provider is cohere
response = completion(model="command-nightly", messages=[{"role":"user","content":"Hi 👋 - i'm cohere"}], metadata={"provider":"cohere"})
```