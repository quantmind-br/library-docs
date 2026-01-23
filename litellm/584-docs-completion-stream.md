---
title: Streaming + Async | liteLLM
url: https://docs.litellm.ai/docs/completion/stream
source: sitemap
fetched_at: 2026-01-21T19:44:45.736660176-03:00
rendered_js: false
word_count: 0
summary: This document provides a technical example of how LiteLLM handles repeated streaming chunks and the logic for triggering error states when predefined limits are exceeded.
tags:
    - litellm
    - streaming
    - error-handling
    - api-limits
    - python-sdk
category: reference
---

```
import litellm 
import os 

litellm.set_verbose =False
loop_amount = litellm.REPEATED_STREAMING_CHUNK_LIMIT +1
chunks =[
    litellm.ModelResponse(**{
"id":"chatcmpl-123",
"object":"chat.completion.chunk",
"created":1694268190,
"model":"gpt-3.5-turbo-0125",
"system_fingerprint":"fp_44709d6fcb",
"choices":[
{"index":0,"delta":{"content":"How are you?"},"finish_reason":"stop"}
],
}, stream=True)
]* loop_amount
completion_stream = litellm.ModelResponseListIterator(model_responses=chunks)

response = litellm.CustomStreamWrapper(
    completion_stream=completion_stream,
    model="gpt-3.5-turbo",
    custom_llm_provider="cached_response",
    logging_obj=litellm.Logging(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":"Hey"}],
        stream=True,
        call_type="completion",
        start_time=time.time(),
        litellm_call_id="12345",
        function_id="1245",
),
)

for chunk in response:
continue# expect to raise InternalServerError 
```