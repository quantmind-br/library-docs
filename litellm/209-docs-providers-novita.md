---
title: Novita AI | liteLLM
url: https://docs.litellm.ai/docs/providers/novita
source: sitemap
fetched_at: 2026-01-21T19:49:50.357158596-03:00
rendered_js: false
word_count: 21
summary: This document provides a code example for implementing tool calling with Novita AI models using the LiteLLM library.
tags:
    - litellm
    - novita-ai
    - tool-calling
    - function-calling
    - python
    - api-integration
category: tutorial
---

```
from litellm import completion
import os
# set env
os.environ["NOVITA_API_KEY"]=""

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
messages =[{"role":"user","content":"What's the weather like in Boston today?"}]

response = completion(
    model="novita/deepseek/deepseek-r1-turbo",
    messages=messages,
    tools=tools,
)
# Add any assertions, here to check response args
print(response)
assertisinstance(response.choices[0].message.tool_calls[0].function.name,str)
assertisinstance(
    response.choices[0].message.tool_calls[0].function.arguments,str
)

```

🚨 LiteLLM supports ALL Novita AI models, send `model=novita/<your-novita-model>` to send it to Novita AI. See all Novita AI models [here](https://novita.ai/models/llm?utm_source=github_litellm&utm_medium=github_readme&utm_campaign=github_link)