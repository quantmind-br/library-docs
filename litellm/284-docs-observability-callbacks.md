---
title: Callbacks | liteLLM
url: https://docs.litellm.ai/docs/observability/callbacks
source: sitemap
fetched_at: 2026-01-21T19:45:57.657870397-03:00
rendered_js: false
word_count: 39
summary: This document explains how to configure input, success, and failure callbacks in liteLLM to integrate with various monitoring and logging providers.
tags:
    - litellm
    - callbacks
    - logging
    - monitoring
    - integrations
    - error-handling
category: configuration
---

liteLLM provides `input_callbacks`, `success_callbacks` and `failure_callbacks`, making it easy for you to send data to a particular provider depending on the status of your responses.

This is **not** an extensive list. Please check the dropdown for all logging integrations.

```
from litellm import completion

# set callbacks
litellm.input_callback=["sentry"]# for sentry breadcrumbing - logs the input being sent to the api
litellm.success_callback=["posthog","helicone","langfuse","lunary","athina"]
litellm.failure_callback=["sentry","lunary","langfuse"]

## set env variables
os.environ['LUNARY_PUBLIC_KEY']=""
os.environ['SENTRY_DSN'], os.environ['SENTRY_API_TRACE_RATE']=""
os.environ['POSTHOG_API_KEY'], os.environ['POSTHOG_API_URL']="api-key","api-url"
os.environ["HELICONE_API_KEY"]=""
os.environ["TRACELOOP_API_KEY"]=""
os.environ["LUNARY_PUBLIC_KEY"]=""
os.environ["ATHINA_API_KEY"]=""
os.environ["LANGFUSE_PUBLIC_KEY"]=""
os.environ["LANGFUSE_SECRET_KEY"]=""
os.environ["LANGFUSE_HOST"]=""

response = completion(model="gpt-3.5-turbo", messages=messages)
```