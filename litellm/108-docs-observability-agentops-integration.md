---
title: "\U0001F587️ AgentOps - LLM Observability Platform | liteLLM"
url: https://docs.litellm.ai/docs/observability/agentops_integration
source: sitemap
fetched_at: 2026-01-21T19:45:51.246535647-03:00
rendered_js: false
word_count: 64
summary: This document explains how to integrate AgentOps with LiteLLM using callback functions to enable comprehensive observability and tracing for LLM operations across various providers.
tags:
    - agentops
    - litellm
    - observability
    - llm-monitoring
    - tracing
    - callbacks
category: tutorial
---

[AgentOps](https://docs.agentops.ai) is an observability platform that enables tracing and monitoring of LLM calls, providing detailed insights into your AI operations.

LiteLLM provides `success_callbacks` and `failure_callbacks`, allowing you to easily integrate AgentOps for comprehensive tracing and monitoring of your LLM operations.

Use just a few lines of code to instantly trace your responses **across all providers** with AgentOps: Get your AgentOps API Keys from [https://app.agentops.ai/](https://app.agentops.ai/)

```
import litellm

# Configure LiteLLM to use AgentOps
litellm.success_callback =["agentops"]

# Make your LLM calls as usual
response = litellm.completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"Hello, how are you?"}],
)
```

```
import os
from litellm import completion

# Set env variables
os.environ["OPENAI_API_KEY"]="your-openai-key"
os.environ["AGENTOPS_API_KEY"]="your-agentops-api-key"

# Configure LiteLLM to use AgentOps
litellm.success_callback =["agentops"]

# OpenAI call
response = completion(
    model="gpt-4",
    messages=[{"role":"user","content":"Hi 👋 - I'm OpenAI"}],
)

print(response)
```