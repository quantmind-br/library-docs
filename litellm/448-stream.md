---
title: Streaming Responses & Async Completion | liteLLM
url: https://docs.litellm.ai/stream
source: sitemap
fetched_at: 2026-01-21T19:43:41.760331138-03:00
rendered_js: false
word_count: 121
summary: This document explains how to implement streaming responses, asynchronous completion, and token usage tracking within the LiteLLM library.
tags:
    - litellm
    - streaming
    - async-completion
    - token-usage
    - python-sdk
    - llm-api
category: guide
---

- [Streaming Responses](#streaming-responses)
- [Async Completion](#async-completion)

## Streaming Responses[​](#streaming-responses "Direct link to Streaming Responses")

LiteLLM supports streaming the model response back by passing `stream=True` as an argument to the completion function

### Usage[​](#usage "Direct link to Usage")

```
response = completion(model="gpt-3.5-turbo", messages=messages, stream=True)
for chunk in response:
print(chunk['choices'][0]['delta'])

```

## Async Completion[​](#async-completion "Direct link to Async Completion")

Asynchronous Completion with LiteLLM LiteLLM provides an asynchronous version of the completion function called `acompletion`

### Usage[​](#usage-1 "Direct link to Usage")

```
from litellm import acompletion
import asyncio

async def test_get_response():
    user_message = "Hello, how are you?"
    messages = [{"content": user_message, "role": "user"}]
    response = await acompletion(model="gpt-3.5-turbo", messages=messages)
    return response

response = asyncio.run(test_get_response())
print(response)

```

## Streaming Token Usage[​](#streaming-token-usage "Direct link to Streaming Token Usage")

Supported across all providers. Works the same as openai.

`stream_options={"include_usage": True}`

If set, an additional chunk will be streamed before the data: \[DONE] message. The usage field on this chunk shows the token usage statistics for the entire request, and the choices field will always be an empty array. All other chunks will also include a usage field, but with a null value.

### SDK[​](#sdk "Direct link to SDK")

```
from litellm import completion 
import os

os.environ["OPENAI_API_KEY"]=""

response = completion(model="gpt-3.5-turbo", messages=messages, stream=True, stream_options={"include_usage":True})
for chunk in response:
print(chunk['choices'][0]['delta'])
```

### PROXY[​](#proxy "Direct link to PROXY")

```
curl https://0.0.0.0:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ],
    "stream": true,
    "stream_options": {"include_usage": true}
  }'

```

- [Streaming Responses](#streaming-responses)
  
  - [Usage](#usage)
- [Async Completion](#async-completion)
  
  - [Usage](#usage-1)
- [Streaming Token Usage](#streaming-token-usage)
  
  - [SDK](#sdk)
  - [PROXY](#proxy)