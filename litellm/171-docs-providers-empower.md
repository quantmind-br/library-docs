---
title: Empower | liteLLM
url: https://docs.litellm.ai/docs/providers/empower
source: sitemap
fetched_at: 2026-01-21T19:48:59.207766116-03:00
rendered_js: false
word_count: 17
summary: This document provides instructions and code examples for integrating Empower models with LiteLLM, covering standard completions, streaming, and function calling.
tags:
    - litellm
    - empower
    - python-sdk
    - llm-integration
    - function-calling
    - streaming-api
category: guide
---

LiteLLM supports all models on Empower.

```
from litellm import completion 
import os

os.environ["EMPOWER_API_KEY"]="your-api-key"

messages =[{"role":"user","content":"Write me a poem about the blue sky"}]

response = completion(model="empower/empower-functions", messages=messages)
print(response)
```

```
from litellm import completion 
import os

os.environ["EMPOWER_API_KEY"]="your-api-key"

messages =[{"role":"user","content":"Write me a poem about the blue sky"}]

response = completion(model="empower/empower-functions", messages=messages, streaming=True)
for chunk in response:
print(chunk['choices'][0]['delta'])

```

```
from litellm import completion 
import os

os.environ["EMPOWER_API_KEY"]="your-api-key"

messages =[{"role":"user","content":"What's the weather like in San Francisco, Tokyo, and Paris?"}]
tools =[
{
"type":"function",
"function":{
"name":"get_current_weather",
"description":"Get the current weather in a given location",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"The city and state, e.g. San Francisco, CA",
},
"unit":{"type":"string","enum":["celsius","fahrenheit"]},
},
"required":["location"],
},
},
}
]

response = completion(
    model="empower/empower-functions-small",
    messages=messages,
    tools=tools,
    tool_choice="auto",# auto is default, but we'll be explicit
)
print("\nLLM Response:\n", response)
```

liteLLM supports `non-streaming` and `streaming` requests to all models on [https://empower.dev/](https://empower.dev/)