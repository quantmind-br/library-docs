---
title: Debugging | liteLLM
url: https://docs.litellm.ai/docs/proxy/debugging
source: sitemap
fetched_at: 2026-01-21T19:51:44.368580037-03:00
rendered_js: false
word_count: 105
summary: This document explains how to enable and use debugging features in LiteLLM to monitor raw API requests and responses or capture logs during errors.
tags:
    - litellm
    - debugging
    - logging
    - api-requests
    - troubleshooting
category: guide
---

2 levels of debugging supported.

When making requests you should see the POST request sent by LiteLLM to the LLM on the Terminal output

```
curl -L -X POST 'http://0.0.0.0:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{ 
    "model":"fake-openai-endpoint",
    "messages": [{"role": "user","content": "How many r in the word strawberry?"}],
    "litellm_request_debug": true
}'
```

This will emit the raw request sent by LiteLLM to the API Provider and raw response received from the API Provider for **just** this request in the logs.

```
INFO:     Uvicorn running on http://0.0.0.0:4000 (Press CTRL+C to quit)
20:14:06 - LiteLLM:WARNING: litellm_logging.py:938 - 

POST Request Sent from LiteLLM:
curl -X POST \
https://exampleopenaiendpoint-production.up.railway.app/chat/completions \
-H 'Authorization: Be****ey' -H 'Content-Type: application/json' \
-d '{'model': 'fake', 'messages': [{'role': 'user', 'content': 'How many r in the word strawberry?'}], 'stream': False}'


20:14:06 - LiteLLM:WARNING: litellm_logging.py:1015 - RAW RESPONSE:
{"id":"chatcmpl-817fc08f0d6c451485d571dab39b26a1","object":"chat.completion","created":1677652288,"model":"gpt-3.5-turbo-0301","system_fingerprint":"fp_44709d6fcb","choices":[{"index":0,"message":{"role":"assistant","content":"\n\nHello there, how may I assist you today?"},"logprobs":null,"finish_reason":"stop"}],"usage":{"prompt_tokens":9,"completion_tokens":12,"total_tokens":21}}


INFO:     127.0.0.1:56155 - "POST /chat/completions HTTP/1.1" 200 OK

```

The proxy will now all logs in json format.

Only get logs if an error occurs.

```
No deployments available for selected model, Try again in 60 seconds. Passed model=claude-3-5-sonnet. pre-call-checks=False, allowed_model_region=n/a.
```

This can be caused due to all your models hitting rate limit errors, causing the cooldown to kick in.

This is not recommended, as it will lead to requests being routed to deployments over their tpm/rpm limit.