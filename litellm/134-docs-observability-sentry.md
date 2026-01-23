---
title: Sentry - Log LLM Exceptions | liteLLM
url: https://docs.litellm.ai/docs/observability/sentry
source: sitemap
fetched_at: 2026-01-21T19:46:32.555929112-03:00
rendered_js: false
word_count: 60
summary: This document explains how to integrate LiteLLM with Sentry for error monitoring, breadcrumbing, and transaction logging in production applications.
tags:
    - litellm
    - sentry
    - error-monitoring
    - integration
    - exception-handling
    - logging-configuration
category: guide
---

[Sentry](https://sentry.io/) provides error monitoring for production. LiteLLM can add breadcrumbs and send exceptions to Sentry with this integration

```
import litellm
from litellm import completion 

litellm.input_callback=["sentry"]# adds sentry breadcrumbing
litellm.failure_callback=["sentry"]# [OPTIONAL] if you want litellm to capture -> send exception to sentry

import os 
os.environ["SENTRY_DSN"]="your-sentry-url"
os.environ["OPENAI_API_KEY"]="your-openai-key"

# set bad key to trigger error 
api_key="bad-key"
response = completion(model="gpt-3.5-turbo", messages=[{"role":"user","content":"Hey!"}], stream=True, api_key=api_key)

print(response)
```

These options are useful for high-volume applications where sampling a subset of errors and transactions provides sufficient visibility while managing costs.

Set `litellm.turn_off_message_logging=True` This will prevent the messages and responses from being logged to sentry, but request metadata will still be logged.