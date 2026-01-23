---
title: Raw Request/Response Logging | liteLLM
url: https://docs.litellm.ai/docs/observability/raw_request_response
source: sitemap
fetched_at: 2026-01-21T19:46:30.672638115-03:00
rendered_js: false
word_count: 0
summary: This document provides a code example for integrating LiteLLM with Langfuse to automatically log and track Large Language Model requests and responses using callbacks.
tags:
    - litellm
    - langfuse
    - llm-observability
    - logging
    - python
    - monitoring
category: tutorial
---

```
# pip install langfuse 
import litellm
import os

# log raw request/response
litellm.log_raw_request_response =True

# from https://cloud.langfuse.com/
os.environ["LANGFUSE_PUBLIC_KEY"]=""
os.environ["LANGFUSE_SECRET_KEY"]=""
# Optional, defaults to https://cloud.langfuse.com
os.environ["LANGFUSE_HOST"]# optional

# LLM API Keys
os.environ['OPENAI_API_KEY']=""

# set langfuse as a callback, litellm will send the data to langfuse
litellm.success_callback =["langfuse"]

# openai call
response = litellm.completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
]
)
```