---
title: Auto Routing | liteLLM
url: https://docs.litellm.ai/docs/proxy/auto_routing
source: sitemap
fetched_at: 2026-01-21T19:51:14.699148366-03:00
rendered_js: false
word_count: 122
summary: This document explains how to configure and implement auto routing in LiteLLM to automatically select the best model for a request based on semantic matching of input content.
tags:
    - litellm
    - auto-routing
    - model-selection
    - semantic-router
    - embeddings
    - python-sdk
category: guide
---

LiteLLM can auto select the best model for a request based on rules you define.

Auto routing allows you to define routing rules that automatically select the best model for a request based on the input content. This is useful for directing different types of queries to specialized models.

```
{
"encoder_type":"openai",
"encoder_name":"text-embedding-3-large",
"routes":[
{
"name":"litellm-gpt-4.1",
"utterances":[
"litellm is great"
],
"description":"positive affirmation",
"function_schemas":null,
"llm":null,
"score_threshold":0.5,
"metadata":{}
},
{
"name":"litellm-claude-35",
"utterances":[
"how to code a program in [language]"
],
"description":"coding assistant",
"function_schemas":null,
"llm":null,
"score_threshold":0.5,
"metadata":{}
}
]
}
```

```
from litellm import Router
import os

router = Router(
    model_list=[
# Embedding models for routing
{
"model_name":"custom-text-embedding-model",
"litellm_params":{
"model":"text-embedding-3-large",
"api_key": os.getenv("OPENAI_API_KEY"),
},
},
# Your target models
{
"model_name":"litellm-gpt-4.1",
"litellm_params":{
"model":"gpt-4.1",
},
"model_info":{"id":"openai-id"},
},
{
"model_name":"litellm-claude-35",
"litellm_params":{
"model":"claude-3-5-sonnet-latest",
},
"model_info":{"id":"claude-id"},
},
# Auto router configuration
{
"model_name":"auto_router1",
"litellm_params":{
"model":"auto_router/auto_router_1",
"auto_router_config_path":"router.json",
"auto_router_default_model":"gpt-4o-mini",
"auto_router_embedding_model":"custom-text-embedding-model",
},
},
],
)
```

Once configured, use the auto router by calling it with your auto router model name:

```
# This request will be routed to gpt-4.1 based on the utterance match
response =await router.acompletion(
    model="auto_router1",
    messages=[{"role":"user","content":"litellm is great"}],
)

# This request will be routed to claude-3-5-sonnet-latest for coding queries
response =await router.acompletion(
    model="auto_router1",
    messages=[{"role":"user","content":"how to code a program in python"}],
)
```

Navigate to the LiteLLM UI and go to **Models+Endpoints** &gt; **Add Model** &gt; **Auto Router Tab**.

Click **Add Route** to create a new routing rule. Each route consists of utterances that are matched against input messages to determine the target model.

Once added developers need to select the model=`auto_router1` in the `model` field of the LLM API request.