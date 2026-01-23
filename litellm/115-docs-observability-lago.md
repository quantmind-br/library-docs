---
title: Lago - Usage Based Billing | liteLLM
url: https://docs.litellm.ai/docs/observability/lago
source: sitemap
fetched_at: 2026-01-21T19:46:10.531397992-03:00
rendered_js: false
word_count: 53
summary: This document provides instructions for integrating Lago with LiteLLM to enable usage-based billing and automated cost tracking via success callbacks.
tags:
    - lago
    - litellm
    - usage-based-billing
    - callbacks
    - cost-tracking
    - api-logging
category: guide
---

[Lago](https://www.getlago.com/) offers a self-hosted and cloud, metering and usage-based billing solution.

## Quick Start[​](#quick-start "Direct link to Quick Start")

Use just 1 lines of code, to instantly log your responses **across all providers** with Lago

Get your Lago [API Key](https://docs.getlago.com/guide/self-hosted/docker#find-your-api-key)

```
litellm.callbacks =["lago"]# logs cost + usage of successful calls to lago
```

- SDK
- PROXY

```
# pip install lago 
import litellm
import os

os.environ["LAGO_API_BASE"]=""# http://0.0.0.0:3000
os.environ["LAGO_API_KEY"]=""
os.environ["LAGO_API_EVENT_CODE"]=""# The billable metric's code - https://docs.getlago.com/guide/events/ingesting-usage#define-a-billable-metric

# LLM API Keys
os.environ['OPENAI_API_KEY']=""

# set lago as a callback, litellm will send the data to lago
litellm.success_callback =["lago"]

# openai call
response = litellm.completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
],
  user="your_customer_id"# 👈 SET YOUR CUSTOMER ID HERE
)
```

## Advanced - Lagos Logging object[​](#advanced---lagos-logging-object "Direct link to Advanced - Lagos Logging object")

This is what LiteLLM will log to Lagos

```
{
    "event": {
      "transaction_id": "<generated_unique_id>",
      "external_customer_id": <litellm_end_user_id>, # passed via `user` param in /chat/completion call - https://platform.openai.com/docs/api-reference/chat/create
      "code": os.getenv("LAGO_API_EVENT_CODE"), 
      "properties": {
          "input_tokens": <number>,
          "output_tokens": <number>,
          "model": <string>,
          "response_cost": <number>, # 👈 LITELLM CALCULATED RESPONSE COST - https://github.com/BerriAI/litellm/blob/d43f75150a65f91f60dc2c0c9462ce3ffc713c1f/litellm/utils.py#L1473
      }
    }
}
```