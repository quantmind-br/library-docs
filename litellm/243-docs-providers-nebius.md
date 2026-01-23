---
title: Nebius AI Studio | liteLLM
url: https://docs.litellm.ai/docs/providers/nebius
source: sitemap
fetched_at: 2026-01-21T19:49:48.331400968-03:00
rendered_js: false
word_count: 52
summary: This document provides code examples for performing standard and streaming chat completions using the LiteLLM library with the Nebius AI Studio provider.
tags:
    - litellm
    - nebius-ai-studio
    - python
    - chat-completion
    - streaming-api
    - ai-integration
category: tutorial
---

```
from litellm import completion
import os

os.environ['NEBIUS_API_KEY']="insert-your-nebius-ai-studio-api-key"
response = completion(
    model="nebius/Qwen/Qwen3-235B-A22B",
    messages=[
{
"role":"user",
"content":"What character was Wall-e in love with?",
}
],
    max_tokens=10,
    response_format={"type":"json_object"},
    seed=123,
    stop=["\n\n"],
    temperature=0.6,# either set temperature or `top_p`
    top_p=0.01,# to get as deterministic results as possible
    tool_choice="auto",
    tools=[],
    user="user",
)
print(response)
```

```
from litellm import completion
import os

os.environ['NEBIUS_API_KEY']=""
response = completion(
    model="nebius/Qwen/Qwen3-235B-A22B",
    messages=[
{
"role":"user",
"content":"What character was Wall-e in love with?",
}
],
    stream=True,
    max_tokens=10,
    response_format={"type":"json_object"},
    seed=123,
    stop=["\n\n"],
    temperature=0.6,# either set temperature or `top_p`
    top_p=0.01,# to get as deterministic results as possible
    tool_choice="auto",
    tools=[],
    user="user",
)

for chunk in response:
print(chunk)
```