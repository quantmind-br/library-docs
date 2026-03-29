---
title: Humanloop | liteLLM
url: https://docs.litellm.ai/docs/observability/humanloop
source: sitemap
fetched_at: 2026-01-21T19:46:09.035597063-03:00
rendered_js: false
word_count: 132
summary: This document provides instructions on how to integrate Humanloop with LiteLLM for prompt management and model completions.
tags:
    - humanloop
    - litellm
    - prompt-management
    - llm-integration
    - python-sdk
category: guide
---

[Humanloop](https://humanloop.com/docs/v5/getting-started/overview) enables product teams to build robust AI features with LLMs, using best-in-class tooling for Evaluation, Prompt Management, and Observability.

## Getting Started[​](#getting-started "Direct link to Getting Started")

Use Humanloop to manage prompts across all LiteLLM Providers.

- SDK
- PROXY

```
import os 
import litellm

os.environ["HUMANLOOP_API_KEY"]=""# [OPTIONAL] set here or in `.completion`

litellm.set_verbose =True# see raw request to provider

resp = litellm.completion(
    model="humanloop/gpt-3.5-turbo",
    prompt_id="test-chat-prompt",
    prompt_variables={"user_message":"this is used"},# [OPTIONAL]
    messages=[{"role":"user","content":"<IGNORED>"}],
# humanloop_api_key="..." ## alternative to setting env var
)
```

**Expected Logs:**

```
POST Request Sent from LiteLLM:
curl -X POST \
https://api.openai.com/v1/ \
-d '{'model': 'gpt-3.5-turbo', 'messages': <YOUR HUMANLOOP PROMPT TEMPLATE>}'
```

## How to set model[​](#how-to-set-model "Direct link to How to set model")

## How to set model[​](#how-to-set-model-1 "Direct link to How to set model")

### Set the model on LiteLLM[​](#set-the-model-on-litellm "Direct link to Set the model on LiteLLM")

You can do `humanloop/<litellm_model_name>`

- SDK
- PROXY

```
litellm.completion(
    model="humanloop/gpt-3.5-turbo",# or `humanloop/anthropic/claude-3-5-sonnet`
...
)
```

### Set the model on Humanloop[​](#set-the-model-on-humanloop "Direct link to Set the model on Humanloop")

LiteLLM will call humanloop's `https://api.humanloop.com/v5/prompts/<your-prompt-id>` endpoint, to get the prompt template.

This also returns the template model set on Humanloop.

```
{
  "template": [
    {
      ... # your prompt template
    }
  ],
  "model": "gpt-3.5-turbo" # your template model
}
```