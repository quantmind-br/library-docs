---
title: '''Thinking'' / ''Reasoning Content'' | liteLLM'
url: https://docs.litellm.ai/docs/reasoning_content
source: sitemap
fetched_at: 2026-01-21T19:54:10.846921519-03:00
rendered_js: false
word_count: 0
summary: This document provides a code implementation for executing function calls using the LiteLLM library, demonstrating the workflow of defining tools and processing their results.
tags:
    - litellm
    - function-calling
    - tool-use
    - python-sdk
    - llm-integration
category: tutorial
---

```
litellm._turn_on_debug()
litellm.modify_params =True
model ="anthropic/claude-3-7-sonnet-20250219"# works across Anthropic, Bedrock, Vertex AI
# Step 1: send the conversation and available functions to the model
messages =[
{
"role":"user",
"content":"What's the weather like in San Francisco, Tokyo, and Paris? - give me 3 responses",
}
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
"description":"The city and state",
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
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto",# auto is default, but we'll be explicit
    reasoning_effort="low",
)
print("Response\n", response)
response_message = response.choices[0].message
tool_calls = response_message.tool_calls

print("Expecting there to be 3 tool calls")
assert(
len(tool_calls)>0
)# this has to call the function for SF, Tokyo and paris

# Step 2: check if the model wanted to call a function
print(f"tool_calls: {tool_calls}")
if tool_calls:
# Step 3: call the function
# Note: the JSON response may not always be valid; be sure to handle errors
    available_functions ={
"get_current_weather": get_current_weather,
}# only one function in this example, but you can have multiple
    messages.append(
        response_message
)# extend conversation with assistant's reply
print("Response message\n", response_message)
# Step 4: send the info for each function call and function response to the model
for tool_call in tool_calls:
        function_name = tool_call.function.name
if function_name notin available_functions:
# the model called a function that does not exist in available_functions - don't try calling anything
return
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
        model=model,
        messages=messages,
        seed=22,
        reasoning_effort="low",
# tools=tools,
        drop_params=True,
)# get a new response from the model where it can see the function response
print("second response\n", second_response)
```