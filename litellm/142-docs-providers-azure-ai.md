---
title: Azure AI Studio | liteLLM
url: https://docs.litellm.ai/docs/providers/azure_ai
source: sitemap
fetched_at: 2026-01-21T19:48:03.610471279-03:00
rendered_js: false
word_count: 0
summary: This document provides a code example for implementing tool use and function calling with LiteLLM using Azure AI hosted models.
tags:
    - litellm
    - azure-ai
    - function-calling
    - tool-use
    - python-sdk
category: tutorial
---

```
from litellm import completion

# set env
os.environ["AZURE_AI_API_KEY"]="your-api-key"
os.environ["AZURE_AI_API_BASE"]="your-api-base"

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
    model="azure_ai/mistral-large-latest",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)
# Add any assertions, here to check response args
print(response)
assertisinstance(response.choices[0].message.tool_calls[0].function.name,str)
assertisinstance(
    response.choices[0].message.tool_calls[0].function.arguments,str
)

```