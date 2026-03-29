---
title: Multi-Instance TPM/RPM (litellm.Router) | liteLLM
url: https://docs.litellm.ai/docs/load_test_rpm
source: sitemap
fetched_at: 2026-01-21T19:45:38.669428069-03:00
rendered_js: false
word_count: 137
summary: This document provides scripts and instructions for load testing the LiteLLM Router and Proxy to verify that RPM and TPM rate limits are correctly enforced across multiple instances.
tags:
    - litellm
    - load-testing
    - rate-limiting
    - router
    - proxy-testing
    - rpm-limits
    - tpm-limits
category: guide
---

Test if your defined tpm/rpm limits are respected across multiple instances of the Router object.

Let's hit the router with 600 requests per minute.

Copy this script 👇. Save it as `test_loadtest_router.py` AND run it with `python3 test_loadtest_router.py`

```
from litellm import Router 
import litellm
litellm.suppress_debug_info =True
litellm.set_verbose =False
import logging
logging.basicConfig(level=logging.CRITICAL)
import os, random, uuid, time, asyncio

# Model list for OpenAI and Anthropic models
model_list =[
{
"model_name":"fake-openai-endpoint",
"litellm_params":{
"model":"gpt-3.5-turbo",
"api_key":"my-fake-key",
"api_base":"http://0.0.0.0:8080",
"rpm":100
},
},
{
"model_name":"fake-openai-endpoint",
"litellm_params":{
"model":"gpt-3.5-turbo",
"api_key":"my-fake-key",
"api_base":"http://0.0.0.0:8081",
"rpm":100
},
},
]

router_1 = Router(model_list=model_list, num_retries=0, enable_pre_call_checks=True, routing_strategy="simple-shuffle", redis_host=os.getenv("REDIS_HOST"), redis_port=os.getenv("REDIS_PORT"), redis_password=os.getenv("REDIS_PASSWORD"))
router_2 = Router(model_list=model_list, num_retries=0, routing_strategy="simple-shuffle", enable_pre_call_checks=True, redis_host=os.getenv("REDIS_HOST"), redis_port=os.getenv("REDIS_PORT"), redis_password=os.getenv("REDIS_PASSWORD"))


asyncdefrouter_completion_non_streaming():
try:
    client: Router = random.sample([router_1, router_2],1)[0]# randomly pick b/w clients
# print(f"client={client}")
    response =await client.acompletion(
              model="fake-openai-endpoint",# [CHANGE THIS] (if you call it something else on your proxy)
              messages=[{"role":"user","content":f"This is a test: {uuid.uuid4()}"}],
)
return response
except Exception as e:
# print(e)
returnNone

asyncdefloadtest_fn():
    start = time.time()
    n =600# Number of concurrent tasks
    tasks =[router_completion_non_streaming()for _ inrange(n)]
    chat_completions =await asyncio.gather(*tasks)
    successful_completions =[c for c in chat_completions if c isnotNone]
print(n, time.time()- start,len(successful_completions))

defget_utc_datetime():
import datetime as dt
from datetime import datetime

ifhasattr(dt,"UTC"):
return datetime.now(dt.UTC)# type: ignore
else:
return datetime.utcnow()# type: ignore


# Run the event loop to execute the async function
asyncdefparent_fn():
for _ inrange(10):
    dt = get_utc_datetime()
    current_minute = dt.strftime("%H-%M")
print(f"triggered new batch - {current_minute}")
await loadtest_fn()
await asyncio.sleep(10)

asyncio.run(parent_fn())
```

Test if your defined tpm/rpm limits are respected across multiple instances.

The quickest way to do this is by testing the [proxy](https://docs.litellm.ai/docs/proxy/quick_start). The proxy uses the [router](https://docs.litellm.ai/docs/routing) under the hood, so if you're using either of them, this test should work for you.

So we'll send 600 requests per minute, but expect only 200 requests per minute to succeed.

Let's hit the proxy with 600 requests per minute.

Copy this script 👇. Save it as `test_loadtest_proxy.py` AND run it with `python3 test_loadtest_proxy.py`

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
litellm_client_2 = AsyncOpenAI(
    api_key="sk-1234",# [CHANGE THIS]
    base_url="http://0.0.0.0:4001"
)

asyncdefproxy_completion_non_streaming():
try:
    client = random.sample([litellm_client, litellm_client_2],1)[0]# randomly pick b/w clients
# print(f"client={client}")
    response =await client.chat.completions.create(
              model="fake-openai-endpoint",# [CHANGE THIS] (if you call it something else on your proxy)
              messages=[{"role":"user","content":f"This is a test: {uuid.uuid4()}"}],
)
return response
except Exception as e:
# print(e)
returnNone

asyncdefloadtest_fn():
    start = time.time()
    n =600# Number of concurrent tasks
    tasks =[proxy_completion_non_streaming()for _ inrange(n)]
    chat_completions =await asyncio.gather(*tasks)
    successful_completions =[c for c in chat_completions if c isnotNone]
print(n, time.time()- start,len(successful_completions))

defget_utc_datetime():
import datetime as dt
from datetime import datetime

ifhasattr(dt,"UTC"):
return datetime.now(dt.UTC)# type: ignore
else:
return datetime.utcnow()# type: ignore


# Run the event loop to execute the async function
asyncdefparent_fn():
for _ inrange(10):
    dt = get_utc_datetime()
    current_minute = dt.strftime("%H-%M")
print(f"triggered new batch - {current_minute}")
await loadtest_fn()
await asyncio.sleep(10)

asyncio.run(parent_fn())

```

Let's setup a fake openai server with a RPM limit of 100.

Let's call our file `fake_openai_server.py`.

```
# import sys, os
# sys.path.insert(
#     0, os.path.abspath("../")
# )  # Adds the parent directory to the system path
from fastapi import FastAPI, Request, status, HTTPException, Depends
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, HTTPException, UploadFile, File
import httpx, os, json
from openai import AsyncOpenAI
from typing import Optional
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse


class ProxyException(Exception):
    # NOTE: DO NOT MODIFY THIS
    # This is used to map exactly to OPENAI Exceptions
    def __init__(
        self,
        message: str,
        type: str,
        param: Optional[str],
        code: Optional[int],
    ):
        self.message = message
        self.type = type
        self.param = param
        self.code = code

    def to_dict(self) -> dict:
        """Converts the ProxyException instance to a dictionary."""
        return {
            "message": self.message,
            "type": self.type,
            "param": self.param,
            "code": self.code,
        }


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
async def _rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(status_code=429,
                        content={"detail": "Rate Limited!"})

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# for completion
@app.post("/chat/completions")
@app.post("/v1/chat/completions")
@limiter.limit("100/minute")
async def completion(request: Request):
    # raise HTTPException(status_code=429, detail="Rate Limited!")
    return {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677652288,
        "model": None,
        "system_fingerprint": "fp_44709d6fcb",
        "choices": [{
            "index": 0,
            "message": {
            "role": "assistant",
            "content": "\n\nHello there, how may I assist you today?",
            },
            "logprobs": None,
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": 9,
            "completion_tokens": 12,
            "total_tokens": 21
        }
    }

if __name__ == "__main__":
    import socket
    import uvicorn
    port = 8080
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('0.0.0.0', port))
        if result != 0:
            print(f"Port {port} is available, starting server...")
            break
        else:
            port += 1

    uvicorn.run(app, host="0.0.0.0", port=port)
```