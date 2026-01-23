---
title: Github | liteLLM
url: https://docs.litellm.ai/docs/providers/github
source: sitemap
fetched_at: 2026-01-21T19:49:13.405824566-03:00
rendered_js: false
word_count: 15
summary: This document explains how to integrate GitHub-hosted models with LiteLLM, demonstrating basic completion, streaming, and tool-calling implementations.
tags:
    - litellm
    - github-models
    - function-calling
    - streaming
    - python
    - api-integration
category: guide
---

```
# env variable
os.environ['GITHUB_API_KEY']
```

```
from litellm import completion
import os

os.environ['GITHUB_API_KEY']=""
response = completion(
    model="github/Llama-3.2-11B-Vision-Instruct",
    messages=[
{"role":"user","content":"hello from litellm"}
],
)
print(response)
```

```
from litellm import completion
import os

os.environ['GITHUB_API_KEY']=""
response = completion(
    model="github/Llama-3.2-11B-Vision-Instruct",
    messages=[
{"role":"user","content":"hello from litellm"}
],
    stream=True
)

for chunk in response:
print(chunk)
```

```
litellm --config config.yaml
```

We support ALL Github models, just set `github/` as a prefix when sending completion requests

```
# Example dummy function hard coded to return the current weather
import json
defget_current_weather(location, unit="fahrenheit"):
"""Get the current weather in a given location"""
if"tokyo"in location.lower():
return json.dumps({"location":"Tokyo","temperature":"10","unit":"celsius"})
elif"san francisco"in location.lower():
return json.dumps(
{"location":"San Francisco","temperature":"72","unit":"fahrenheit"}
)
elif"paris"in location.lower():
return json.dumps({"location":"Paris","temperature":"22","unit":"celsius"})
else:
return json.dumps({"location": location,"temperature":"unknown"})


# Step 1: send the conversation and available functions to the model
messages =[
{
"role":"system",
"content":"You are a function calling LLM that uses the data extracted from get_current_weather to answer questions about the weather in San Francisco.",
},
{
"role":"user",
"content":"What's the weather like in San Francisco?",
},
]
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
"unit":{
"type":"string",
"enum":["celsius","fahrenheit"],
},
},
"required":["location"],
},
},
}
]
response = litellm.completion(
    model="github/Llama-3.2-11B-Vision-Instruct",
    messages=messages,
    tools=tools,
    tool_choice="auto",# auto is default, but we'll be explicit
)
print("Response\n", response)
response_message = response.choices[0].message
tool_calls = response_message.tool_calls


# Step 2: check if the model wanted to call a function
if tool_calls:
# Step 3: call the function
# Note: the JSON response may not always be valid; be sure to handle errors
    available_functions ={
"get_current_weather": get_current_weather,
}
    messages.append(
        response_message
)# extend conversation with assistant's reply
print("Response message\n", response_message)
# Step 4: send the info for each function call and function response to the model
for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
)
        messages.append(
{
"tool_call_id": tool_call.id,
"role":"tool",
"name": function_name,
"content": function_response,
}
)# extend conversation with function response
print(f"messages: {messages}")
    second_response = litellm.completion(
        model="github/Llama-3.2-11B-Vision-Instruct", messages=messages
)# get a new response from the model where it can see the function response
print("second response\n", second_response)
```