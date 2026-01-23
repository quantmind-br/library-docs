---
title: DataRobot | liteLLM
url: https://docs.litellm.ai/docs/providers/datarobot
source: sitemap
fetched_at: 2026-01-21T19:48:51.815390536-03:00
rendered_js: false
word_count: 83
summary: This document provides instructions and code examples for integrating LiteLLM with DataRobot models via an OpenAI-compatible endpoint.
tags:
    - litellm
    - datarobot
    - llm-gateway
    - python-sdk
    - model-routing
    - api-configuration
category: guide
---

LiteLLM supports all models from [DataRobot](https://datarobot.com). Select `datarobot` as the provider to route your request through the `datarobot` OpenAI-compatible endpoint using the upstream [official OpenAI Python API library](https://github.com/openai/openai-python/blob/main/README.md).

````
import os
from litellm import completion
os.environ["DATAROBOT_API_KEY"]=""
os.environ["DATAROBOT_API_BASE"]=""# [OPTIONAL] defaults to https://app.datarobot.com

response = completion(
            model="datarobot/openai/gpt-4o-mini",
            messages=messages,
)


### Completion
```python
import litellm
import os

response = litellm.completion(
    model="datarobot/openai/gpt-4o-mini",# add `datarobot/` prefix to model so litellm knows to route through DataRobot
    messages=[
{
"role":"user",
"content":"Hey, how's it going?",
}
],
)
print(response)
````

🚨 LiteLLM supports *all* DataRobot LLM gateway models. To get a list for your installation and user account, send the following CURL command: `curl -X GET -H "Authorization: Bearer $DATAROBOT_API_TOKEN" "$DATAROBOT_ENDPOINT/genai/llmgw/catalog/" | jq | grep 'model":'DATAROBOT_ENDPOINT/genai/llmgw/catalog/`