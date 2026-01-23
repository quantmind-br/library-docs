---
title: Cerebras | liteLLM
url: https://docs.litellm.ai/docs/providers/cerebras
source: sitemap
fetched_at: 2026-01-21T19:48:37.135524858-03:00
rendered_js: false
word_count: 0
summary: This document provides examples of using LiteLLM to perform synchronous and streaming completions with Cerebras models, including how to request JSON-formatted outputs.
tags:
    - litellm
    - cerebras
    - python
    - json-mode
    - streaming
    - llm-api
category: guide
---

```
from litellm import completion
import os

os.environ['CEREBRAS_API_KEY']=""
response = completion(
    model="cerebras/llama3-70b-instruct",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit? (Write in JSON)",
}
],
    max_tokens=10,

# The prompt should include JSON if 'json_object' is selected; otherwise, you will get error code 400.
    response_format={"type":"json_object"},
    seed=123,
    stop=["\n\n"],
    temperature=0.2,
    top_p=0.9,
    tool_choice="auto",
    tools=[],
    user="user",
)
print(response)
```

```
from litellm import completion
import os

os.environ['CEREBRAS_API_KEY']=""
response = completion(
    model="cerebras/llama3-70b-instruct",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit? (Write in JSON)",
}
],
    stream=True,
    max_tokens=10,

# The prompt should include JSON if 'json_object' is selected; otherwise, you will get error code 400.
    response_format={"type":"json_object"},
    seed=123,
    stop=["\n\n"],
    temperature=0.2,
    top_p=0.9,
    tool_choice="auto",
    tools=[],
    user="user",
)

for chunk in response:
print(chunk)
```