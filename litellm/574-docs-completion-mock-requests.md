---
title: "Mock Completion() Responses - Save Testing Costs \U0001F4B0 | liteLLM"
url: https://docs.litellm.ai/docs/completion/mock_requests
source: sitemap
fetched_at: 2026-01-21T19:44:32.450201348-03:00
rendered_js: false
word_count: 53
summary: This document explains how to use the mock_response parameter in LiteLLM to simulate API responses for testing purposes without calling actual LLM endpoints. It covers standard completion, streaming, and integration with testing frameworks like pytest.
tags:
    - litellm
    - mock-response
    - unit-testing
    - python-sdk
    - llm-api
    - streaming
    - pytest
category: guide
---

For testing purposes, you can use `completion()` with `mock_response` to mock calling the completion endpoint.

This will return a response object with a default response (works for streaming as well), without calling the LLM APIs.

## quick start[​](#quick-start "Direct link to quick start")

```
from litellm import completion 

model ="gpt-3.5-turbo"
messages =[{"role":"user","content":"This is a test request"}]

completion(model=model, messages=messages, mock_response="It's simple to use and easy to get started")
```

## streaming[​](#streaming "Direct link to streaming")

```
from litellm import completion 
model ="gpt-3.5-turbo"
messages =[{"role":"user","content":"Hey, I'm a mock request"}]
response = completion(model=model, messages=messages, stream=True, mock_response="It's simple to use and easy to get started")
for chunk in response:
print(chunk)# {'choices': [{'delta': {'role': 'assistant', 'content': 'Thi'}, 'finish_reason': None}]}
    complete_response += chunk["choices"][0]["delta"]["content"]
```

## (Non-streaming) Mock Response Object[​](#non-streaming-mock-response-object "Direct link to (Non-streaming) Mock Response Object")

```
{
"choices":[
{
"finish_reason":"stop",
"index":0,
"message":{
"content":"This is a mock request",
"role":"assistant",
"logprobs":null
}
}
],
"created":1694459929.4496052,
"model":"MockResponse",
"usage":{
"prompt_tokens":null,
"completion_tokens":null,
"total_tokens":null
}
}
```

## Building a pytest function using `completion` with `mock_response`[​](#building-a-pytest-function-using-completion-with-mock_response "Direct link to building-a-pytest-function-using-completion-with-mock_response")

```
from litellm import completion
import pytest

deftest_completion_openai():
try:
        response = completion(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":"Why is LiteLLM amazing?"}],
            mock_response="LiteLLM is awesome"
)
# Add any assertions here to check the response
print(response)
assert(response['choices'][0]['message']['content']=="LiteLLM is awesome")
except Exception as e:
        pytest.fail(f"Error occurred: {e}")
```