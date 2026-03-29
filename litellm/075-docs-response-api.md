---
title: /responses | liteLLM
url: https://docs.litellm.ai/docs/response_api
source: sitemap
fetched_at: 2026-01-21T19:54:12.6517756-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to configure and use LiteLLM's Router to ensure consistent routing to the same model deployment across sequential requests using response IDs.
tags:
    - litellm
    - model-routing
    - azure-openai
    - sticky-sessions
    - responses-api
    - python-sdk
category: tutorial
---

```
import litellm

# Set up router with multiple deployments of the same model
router = litellm.Router(
    model_list=[
{
"model_name":"azure-gpt4-turbo",
"litellm_params":{
"model":"azure/gpt-4-turbo",
"api_key":"your-api-key-1",
"api_version":"2024-06-01",
"api_base":"https://endpoint1.openai.azure.com",
},
},
{
"model_name":"azure-gpt4-turbo",
"litellm_params":{
"model":"azure/gpt-4-turbo",
"api_key":"your-api-key-2",
"api_version":"2024-06-01",
"api_base":"https://endpoint2.openai.azure.com",
},
},
],
    optional_pre_call_checks=["responses_api_deployment_check"],
)

# Initial request
response =await router.aresponses(
    model="azure-gpt4-turbo",
input="Hello, who are you?",
    truncation="auto",
)

# Store the response ID
response_id = response.id

# Follow-up request - will be automatically routed to the same deployment
follow_up =await router.aresponses(
    model="azure-gpt4-turbo",
input="Tell me more about yourself",
    truncation="auto",
    previous_response_id=response_id  # This ensures routing to the same deployment
)
```