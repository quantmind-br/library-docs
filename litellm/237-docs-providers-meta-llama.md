---
title: Meta Llama | liteLLM
url: https://docs.litellm.ai/docs/providers/meta_llama
source: sitemap
fetched_at: 2026-01-21T19:49:38.741929382-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to implement tool use and function calling with Meta Llama models using the LiteLLM library.
tags:
    - litellm
    - meta-llama
    - function-calling
    - tool-use
    - python-sdk
    - llm-api
category: tutorial
---

```
import os
import litellm
from litellm import completion

os.environ["LLAMA_API_KEY"]=""# your Meta Llama API key

messages =[{"content":"Create a chart showing the population growth of New York City from 2010 to 2020","role":"user"}]

# Define the tools
tools =[
{
"type":"function",
"function":{
"name":"create_chart",
"description":"Create a chart with the provided data",
"parameters":{
"type":"object",
"properties":{
"chart_type":{
"type":"string",
"enum":["bar","line","pie","scatter"],
"description":"The type of chart to create"
},
"title":{
"type":"string",
"description":"The title of the chart"
},
"data":{
"type":"object",
"description":"The data to plot in the chart"
}
},
"required":["chart_type","title","data"]
}
}
}
]

# Meta Llama call with tool use
response = completion(
    model="meta_llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

print(response.choices[0].message.content)
```