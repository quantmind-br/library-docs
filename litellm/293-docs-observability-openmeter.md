---
title: OpenMeter - Usage-Based Billing | liteLLM
url: https://docs.litellm.ai/docs/observability/openmeter
source: sitemap
fetched_at: 2026-01-21T19:46:22.138846628-03:00
rendered_js: false
word_count: 65
summary: This document provides instructions on integrating OpenMeter with LiteLLM to automatically log LLM usage and costs for usage-based billing applications.
tags:
    - openmeter
    - litellm
    - billing
    - usage-tracking
    - callbacks
    - llm-monitoring
category: guide
---

[OpenMeter](https://openmeter.io/) is an Open Source Usage-Based Billing solution for AI/Cloud applications. It integrates with Stripe for easy billing.

info

We want to learn how we can make the callbacks better! Meet the LiteLLM [founders](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version) or join our [discord](https://discord.gg/wuPM9dRgDw)

## Quick Start[​](#quick-start "Direct link to Quick Start")

Use just 2 lines of code, to instantly log your responses **across all providers** with OpenMeter

Get your OpenMeter API Key from [https://openmeter.cloud/meters](https://openmeter.cloud/meters)

```
litellm.callbacks =["openmeter"]# logs cost + usage of successful calls to openmeter
```

- SDK
- PROXY

```
# pip install openmeter 
import litellm
import os

# from https://openmeter.cloud
os.environ["OPENMETER_API_ENDPOINT"]=""
os.environ["OPENMETER_API_KEY"]=""

# LLM API Keys
os.environ['OPENAI_API_KEY']=""

# set openmeter as a callback, litellm will send the data to openmeter
litellm.callbacks =["openmeter"]

# openai call
response = litellm.completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
]
)
```