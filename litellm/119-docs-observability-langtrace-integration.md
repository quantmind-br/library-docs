---
title: Langtrace AI | liteLLM
url: https://docs.litellm.ai/docs/observability/langtrace_integration
source: sitemap
fetched_at: 2026-01-21T19:46:15.351386766-03:00
rendered_js: false
word_count: 16
summary: Explains how to integrate Langtrace with LiteLLM to automatically log LLM responses from various providers using a simple callback configuration.
tags:
    - litellm
    - langtrace
    - logging
    - observability
    - integration
    - python
category: tutorial
---

Use just 2 lines of code, to instantly log your responses **across all providers** with langtrace

```
import litellm
import os
from langtrace_python_sdk import langtrace

# Langtrace API Keys
os.environ["LANGTRACE_API_KEY"]="<your-api-key>"

# LLM API Keys
os.environ['OPENAI_API_KEY']="<openai-api-key>"

# set langtrace as a callback, litellm will send the data to langtrace
litellm.callbacks =["langtrace"]

#  init langtrace
langtrace.init()

# openai call
response = completion(
    model="gpt-4o",
    messages=[
{"content":"respond only in Yoda speak.","role":"system"},
{"content":"Hello, how are you?","role":"user"},
],
)
print(response)
```