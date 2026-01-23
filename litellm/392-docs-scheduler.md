---
title: '[BETA] Request Prioritization | liteLLM'
url: https://docs.litellm.ai/docs/scheduler
source: sitemap
fetched_at: 2026-01-21T19:54:22.20509491-03:00
rendered_js: false
word_count: 95
summary: This document explains how to implement request prioritization in LiteLLM to manage high-traffic LLM API calls using a priority queue system. It provides configuration instructions for both the Python SDK and LiteLLM Proxy, including advanced Redis-based setups for multi-instance environments.
tags:
    - litellm
    - request-prioritization
    - llm-api
    - priority-queue
    - redis-caching
    - load-balancing
    - api-proxy
category: guide
---

Prioritize LLM API requests in high-traffic.

- Add request to priority queue
- Poll queue, to check if request can be made. Returns 'True':
  
  - if there's healthy deployments
  - OR if request is at top of queue
- Priority - The lower the number, the higher the priority:
  
  - e.g. `priority=0` &gt; `priority=2000`

Supported Router endpoints:

- `acompletion` (`/v1/chat/completions` on Proxy)
- `atext_completion` (`/v1/completions` on Proxy)

## Quick Start[​](#quick-start "Direct link to Quick Start")

```
from litellm import Router

router = Router(
    model_list=[
{
"model_name":"gpt-3.5-turbo",
"litellm_params":{
"model":"gpt-3.5-turbo",
"mock_response":"Hello world this is Macintosh!",# fakes the LLM API call
"rpm":1,
},
},
],
    timeout=2,# timeout request if takes > 2s
    routing_strategy="simple-shuffle",# recommended for best performance
    polling_interval=0.03# poll queue every 3ms if no healthy deployments
)

try:
    _response =await router.acompletion(# 👈 ADDS TO QUEUE + POLLS + MAKES CALL
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":"Hey!"}],
        priority=0,# 👈 LOWER IS BETTER
)
except Exception as e:
print("didn't make request")
```

## LiteLLM Proxy[​](#litellm-proxy "Direct link to LiteLLM Proxy")

To prioritize requests on LiteLLM Proxy add `priority` to the request.

- curl
- OpenAI SDK

```
curl -X POST 'http://localhost:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-D '{
    "model": "gpt-3.5-turbo-fake-model",
    "messages": [
        {
        "role": "user",
        "content": "what is the meaning of the universe? 1234"
        }],
    "priority": 0 👈 SET VALUE HERE
}'
```

## Advanced - Redis Caching[​](#advanced---redis-caching "Direct link to Advanced - Redis Caching")

Use redis caching to do request prioritization across multiple instances of LiteLLM.

### SDK[​](#sdk "Direct link to SDK")

```
from litellm import Router

router = Router(
    model_list=[
{
"model_name":"gpt-3.5-turbo",
"litellm_params":{
"model":"gpt-3.5-turbo",
"mock_response":"Hello world this is Macintosh!",# fakes the LLM API call
"rpm":1,
},
},
],
### REDIS PARAMS ###
    redis_host=os.environ["REDIS_HOST"],
    redis_password=os.environ["REDIS_PASSWORD"],
    redis_port=os.environ["REDIS_PORT"],
)

try:
    _response =await router.acompletion(# 👈 ADDS TO QUEUE + POLLS + MAKES CALL
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":"Hey!"}],
        priority=0,# 👈 LOWER IS BETTER
)
except Exception as e:
print("didn't make request")
```

### PROXY[​](#proxy "Direct link to PROXY")

```
model_list:
-model_name: gpt-3.5-turbo-fake-model
litellm_params:
model: gpt-3.5-turbo
mock_response:"hello world!"
api_key: my-good-key

litellm_settings:
request_timeout:600# 👈 Will keep retrying until timeout occurs

router_settings:
    redis_host; os.environ/REDIS_HOST
redis_password: os.environ/REDIS_PASSWORD
redis_port: os.environ/REDIS_PORT
```

```
$ litellm --config /path/to/config.yaml 

# RUNNING on http://0.0.0.0:4000s
```

```
curl -X POST 'http://localhost:4000/queue/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-D '{
    "model": "gpt-3.5-turbo-fake-model",
    "messages": [
        {
        "role": "user",
        "content": "what is the meaning of the universe? 1234"
        }],
    "priority": 0 👈 SET VALUE HERE
}'
```