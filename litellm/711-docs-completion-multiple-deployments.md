---
title: Multiple Deployments | liteLLM
url: https://docs.litellm.ai/docs/completion/multiple_deployments
source: sitemap
fetched_at: 2026-01-21T19:44:35.790454018-03:00
rendered_js: false
word_count: 27
summary: This document explains how to configure LiteLLM with multiple model deployments to retrieve the first successful response from a list of providers.
tags:
    - litellm
    - model-deployments
    - multi-provider
    - python-sdk
    - completion-api
category: guide
---

If you have multiple deployments of the same model, you can pass the list of deployments, and LiteLLM will return the first result.

Multiple providers offer Mistral-7B-Instruct.

```
from litellm import completion

messages=[{"role":"user","content":"Hey, how's it going?"}]

## All your mistral deployments ##
model_list =[{
"model_name":"mistral-7b-instruct",
"litellm_params":{# params for litellm completion/embedding call 
"model":"replicate/mistralai/mistral-7b-instruct-v0.1:83b6a56e7c828e667f21fd596c338fd4f0039b46bcfa18d973e8e70e455fda70",
"api_key":"replicate_api_key",
}
},{
"model_name":"mistral-7b-instruct",
"litellm_params":{# params for litellm completion/embedding call 
"model":"together_ai/mistralai/Mistral-7B-Instruct-v0.1",
"api_key":"togetherai_api_key",
}
},{
"model_name":"mistral-7b-instruct",
"litellm_params":{# params for litellm completion/embedding call 
"model":"together_ai/mistralai/Mistral-7B-Instruct-v0.1",
"api_key":"togetherai_api_key",
}
},{
"model_name":"mistral-7b-instruct",
"litellm_params":{# params for litellm completion/embedding call 
"model":"perplexity/mistral-7b-instruct",
"api_key":"perplexity_api_key"
}
},{
"model_name":"mistral-7b-instruct",
"litellm_params":{
"model":"deepinfra/mistralai/Mistral-7B-Instruct-v0.1",
"api_key":"deepinfra_api_key"
}
}]

## LiteLLM completion call ## returns first response 
response = completion(model="mistral-7b-instruct", messages=messages, model_list=model_list)

print(response)
```