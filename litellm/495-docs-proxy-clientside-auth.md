---
title: Clientside LLM Credentials | liteLLM
url: https://docs.litellm.ai/docs/proxy/clientside_auth
source: sitemap
fetched_at: 2026-01-21T19:51:22.275923083-03:00
rendered_js: false
word_count: 38
summary: This document demonstrates how to define and pass a custom configuration object to an LLM proxy to manage model routing, rate limits, and failover logic dynamically.
tags:
    - litellm
    - model-routing
    - fallback-logic
    - openai-api
    - configuration-management
    - rate-limiting
category: configuration
---

```
import os

user_config ={
'model_list':[
{
'model_name':'user-azure-instance',
'litellm_params':{
'model':'azure/chatgpt-v-2',
'api_key': os.getenv('AZURE_API_KEY'),
'api_version': os.getenv('AZURE_API_VERSION'),
'api_base': os.getenv('AZURE_API_BASE'),
'timeout':10,
},
'tpm':240000,
'rpm':1800,
},
{
'model_name':'user-openai-instance',
'litellm_params':{
'model':'gpt-3.5-turbo',
'api_key': os.getenv('OPENAI_API_KEY'),
'timeout':10,
},
'tpm':240000,
'rpm':1800,
},
],
'num_retries':2,
'allowed_fails':3,
'fallbacks':[
{
'user-azure-instance':['user-openai-instance']
}
]
}


```

```
import openai
client = openai.OpenAI(
    api_key="sk-1234",
    base_url="http://0.0.0.0:4000"
)

# send request to `user-azure-instance`
response = client.chat.completions.create(model="user-azure-instance", messages =[
{
"role":"user",
"content":"this is a test request, write a short poem"
}
],
    extra_body={
"user_config": user_config
}
)# 👈 User config

print(response)
```