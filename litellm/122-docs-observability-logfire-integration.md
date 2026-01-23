---
title: Logfire | liteLLM
url: https://docs.litellm.ai/docs/observability/logfire_integration
source: sitemap
fetched_at: 2026-01-21T19:46:19.773955765-03:00
rendered_js: false
word_count: 22
summary: This document provides instructions for integrating Logfire with LiteLLM to enable observability, analytics, and production tracing for LLM applications.
tags:
    - logfire
    - litellm
    - observability
    - llm-monitoring
    - analytics
    - tracing
    - python-sdk
category: guide
---

Logfire is open Source Observability & Analytics for LLM Apps Detailed production traces and a granular view on quality, cost and latency

```
# pip install logfire
import litellm
import os

# from https://logfire.pydantic.dev/
os.environ["LOGFIRE_TOKEN"]=""

# Optionally customize the base url
# from https://logfire.pydantic.dev/
os.environ["LOGFIRE_BASE_URL"]=""

# LLM API Keys
os.environ['OPENAI_API_KEY']=""

# set logfire as a callback, litellm will send the data to logfire
litellm.success_callback =["logfire"]

# openai call
response = litellm.completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
]
)
```