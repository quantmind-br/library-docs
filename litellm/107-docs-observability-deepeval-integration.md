---
title: "\U0001F52D DeepEval - Open-Source Evals with Tracing | liteLLM"
url: https://docs.litellm.ai/docs/observability/deepeval_integration
source: sitemap
fetched_at: 2026-01-21T19:46:02.132676244-03:00
rendered_js: false
word_count: 26
summary: This document explains how to integrate the Confident AI observatory using deepeval to trace and monitor LLM applications via LiteLLM callbacks.
tags:
    - deepeval
    - llm-monitoring
    - llm-tracing
    - observability
    - litellm
    - confident-ai
category: guide
---

[Confident AI](https://documentation.confident-ai.com) (the ***deepeval*** platfrom) offers an Observatory for teams to trace and monitor LLM applications. Think Datadog for LLM apps. The observatory allows you to:

```
import os
import time
import litellm


os.environ['OPENAI_API_KEY']='<your-openai-api-key>'
os.environ['CONFIDENT_API_KEY']='<your-confident-api-key>'

litellm.success_callback =["deepeval"]
litellm.failure_callback =["deepeval"]

try:
    response = litellm.completion(
        model="gpt-3.5-turbo",
        messages=[
{"role":"user","content":"What's the weather like in San Francisco?"}
],
)
except Exception as e:
print(e)

print(response)
```