---
title: Provider specific Wildcard routing | liteLLM
url: https://docs.litellm.ai/docs/wildcard_routing
source: sitemap
fetched_at: 2026-01-21T19:55:59.052755392-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to configure the LiteLLM Router using wildcard patterns to dynamically route requests to different model providers based on naming conventions.
tags:
    - litellm
    - router-configuration
    - wildcard-routing
    - model-deployment
    - python-sdk
category: configuration
---

```
from litellm import Router

router = Router(
    model_list=[
{
"model_name":"anthropic/*",
"litellm_params":{
"model":"anthropic/*",
"api_key": os.environ["ANTHROPIC_API_KEY"]
}
},
{
"model_name":"groq/*",
"litellm_params":{
"model":"groq/*",
"api_key": os.environ["GROQ_API_KEY"]
}
},
{
"model_name":"fo::*:static::*",# all requests matching this pattern will be routed to this deployment, example: model="fo::hi::static::hi" will be routed to deployment: "openai/fo::*:static::*"
"litellm_params":{
"model":"openai/fo::*:static::*",
"api_key": os.environ["OPENAI_API_KEY"]
}
}
]
)
```