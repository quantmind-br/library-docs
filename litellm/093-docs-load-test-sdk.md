---
title: LiteLLM SDK vs OpenAI | liteLLM
url: https://docs.litellm.ai/docs/load_test_sdk
source: sitemap
fetched_at: 2026-01-21T19:45:38.851185311-03:00
rendered_js: false
word_count: 0
summary: This document provides a code implementation for performing asynchronous load testing across LiteLLM proxy, router, and Azure OpenAI clients. It demonstrates how to configure multiple LLM providers and execute concurrent chat completion requests to measure performance.
tags:
    - litellm
    - load-testing
    - python
    - asyncio
    - azure-openai
    - llm-proxy
    - concurrency
category: tutorial
---

```
from openai import AsyncOpenAI, AsyncAzureOpenAI
import random, uuid
import time, asyncio, litellm
# import logging
# logging.basicConfig(level=logging.DEBUG)
#### LITELLM PROXY #### 
litellm_client = AsyncOpenAI(
    api_key="sk-1234",# [CHANGE THIS]
    base_url="http://0.0.0.0:4000"
)

#### AZURE OPENAI CLIENT #### 
client = AsyncAzureOpenAI(
    api_key="my-api-key",# [CHANGE THIS]
    azure_endpoint="my-api-base",# [CHANGE THIS]
    api_version="2023-07-01-preview"
)


#### LITELLM ROUTER #### 
model_list =[
{
"model_name":"azure-canada",
"litellm_params":{
"model":"azure/my-azure-deployment-name",# [CHANGE THIS]
"api_key":"my-api-key",# [CHANGE THIS]
"api_base":"my-api-base",# [CHANGE THIS]
"api_version":"2023-07-01-preview"
}
}
]

router = litellm.Router(model_list=model_list)

asyncdefopenai_completion():
try:
    response =await client.chat.completions.create(
              model="gpt-35-turbo",
              messages=[{"role":"user","content":f"This is a test: {uuid.uuid4()}"}],
              stream=True
)
return response
except Exception as e:
print(e)
returnNone


asyncdefrouter_completion():
try:
    response =await router.acompletion(
              model="azure-canada",# [CHANGE THIS]
              messages=[{"role":"user","content":f"This is a test: {uuid.uuid4()}"}],
              stream=True
)
return response
except Exception as e:
print(e)
returnNone

asyncdefproxy_completion_non_streaming():
try:
    response =await litellm_client.chat.completions.create(
              model="sagemaker-models",# [CHANGE THIS] (if you call it something else on your proxy)
              messages=[{"role":"user","content":f"This is a test: {uuid.uuid4()}"}],
)
return response
except Exception as e:
print(e)
returnNone

asyncdefloadtest_fn():
    start = time.time()
    n =500# Number of concurrent tasks
    tasks =[proxy_completion_non_streaming()for _ inrange(n)]
    chat_completions =await asyncio.gather(*tasks)
    successful_completions =[c for c in chat_completions if c isnotNone]
print(n, time.time()- start,len(successful_completions))

# Run the event loop to execute the async function
asyncio.run(loadtest_fn())

```