---
title: Weights & Biases - Logging LLM Input/Output | liteLLM
url: https://docs.litellm.ai/docs/observability/wandb_integration
source: sitemap
fetched_at: 2026-01-21T19:46:41.805082524-03:00
rendered_js: false
word_count: 89
summary: This document provides instructions on integrating Weights & Biases with LiteLLM to log model responses across multiple providers using success callbacks.
tags:
    - litellm
    - weights-and-biases
    - wandb
    - observability
    - llm-logging
    - callbacks
category: tutorial
---

Weights & Biases helps AI developers build better models faster [https://wandb.ai](https://wandb.ai)

info

We want to learn how we can make the callbacks better! Meet the LiteLLM [founders](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version) or join our [discord](https://discord.gg/wuPM9dRgDw)

## Pre-Requisites[​](#pre-requisites "Direct link to Pre-Requisites")

Ensure you have run `pip install wandb` for this integration

```
pip install wandb litellm
```

## Quick Start[​](#quick-start "Direct link to Quick Start")

Use just 2 lines of code, to instantly log your responses **across all providers** with Weights & Biases

```
litellm.success_callback =["wandb"]
```

```
# pip install wandb 
import litellm
import os

os.environ["WANDB_API_KEY"]=""
# LLM API Keys
os.environ['OPENAI_API_KEY']=""

# set wandb as a callback, litellm will send the data to Weights & Biases
litellm.success_callback =["wandb"]

# openai call
response = litellm.completion(
  model="gpt-3.5-turbo",
  messages=[
{"role":"user","content":"Hi 👋 - i'm openai"}
]
)
```

## Support & Talk to Founders[​](#support--talk-to-founders "Direct link to Support & Talk to Founders")

- [Schedule Demo 👋](https://calendly.com/d/4mp-gd3-k5k/berriai-1-1-onboarding-litellm-hosted-version)
- [Community Discord 💭](https://discord.gg/wuPM9dRgDw)
- Our numbers 📞 +1 (770) 8783-106 / ‭+1 (412) 618-6238‬
- Our emails ✉️ [ishaan@berri.ai](mailto:ishaan@berri.ai) / [krrish@berri.ai](mailto:krrish@berri.ai)