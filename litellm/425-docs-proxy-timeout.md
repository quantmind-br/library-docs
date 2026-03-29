---
title: Timeouts | liteLLM
url: https://docs.litellm.ai/docs/proxy/timeout
source: sitemap
fetched_at: 2026-01-21T19:53:52.326432347-03:00
rendered_js: false
word_count: 151
summary: This document explains how to configure global, per-model, and per-request timeouts for synchronous and streaming calls using the LiteLLM Router, including methods for testing timeout handling.
tags:
    - litellm
    - router
    - timeout-configuration
    - stream-timeout
    - error-handling
    - python-sdk
category: configuration
---

The timeout set in router is for the entire length of the call, and is passed down to the completion() call level as well.

### Global Timeouts[​](#global-timeouts "Direct link to Global Timeouts")

- SDK
- PROXY

```
from litellm import Router 

model_list =[{...}]

router = Router(model_list=model_list,
                timeout=30)# raise timeout error if call takes > 30s 

print(response)
```

### Custom Timeouts & Stream Timeouts (Per Model)[​](#custom-timeouts--stream-timeouts-per-model "Direct link to Custom Timeouts & Stream Timeouts (Per Model)")

For each model, you can set `timeout` and `stream_timeout` under `litellm_params`:

- **`timeout`** → maximum time for the *complete response*.  
  Use this to cap long-running completions.
- **`stream_timeout`** → maximum time to wait for the *first chunk* (i.e., first token) in a streaming response.  
  Use this to abort “hanging” providers (e.g., Bedrock slow start) and retry another model.

<!--THE END-->

- SDK
- PROXY

```
from litellm import Router 
import asyncio

model_list =[{
"model_name":"gpt-3.5-turbo",
"litellm_params":{
"model":"azure/chatgpt-v-2",
"api_key": os.getenv("AZURE_API_KEY"),
"api_version": os.getenv("AZURE_API_VERSION"),
"api_base": os.getenv("AZURE_API_BASE"),
"timeout":300# sets a 5 minute timeout
"stream_timeout":30# sets a 30s timeout for streaming calls
}
}]

# init router
router = Router(model_list=model_list, routing_strategy="least-busy")
asyncdefrouter_acompletion():
    response =await router.acompletion(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":"Hey, how's it going?"}]
)
print(response)
return response

asyncio.run(router_acompletion())
```

### Setting Dynamic Timeouts - Per Request[​](#setting-dynamic-timeouts---per-request "Direct link to Setting Dynamic Timeouts - Per Request")

LiteLLM supports setting a `timeout` per request

**Example Usage**

- SDK
- PROXY

```
from litellm import Router 

model_list =[{...}]
router = Router(model_list=model_list)

response = router.completion(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":"what color is red"}],
    timeout=1
)
```

## Testing timeout handling[​](#testing-timeout-handling "Direct link to Testing timeout handling")

To test if your retry/fallback logic can handle timeouts, you can set `mock_timeout=True` for testing.

This is currently only supported on `/chat/completions` and `/completions` endpoints. Please [let us know](https://github.com/BerriAI/litellm/issues) if you need this for other endpoints.

```
curl -L -X POST 'http://0.0.0.0:4000/v1/chat/completions' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer sk-1234' \
    --data-raw '{
        "model": "gemini/gemini-1.5-flash",
        "messages": [
        {"role": "user", "content": "hi my email is ishaan@berri.ai"}
        ],
        "mock_timeout": true # 👈 KEY CHANGE
    }'
```