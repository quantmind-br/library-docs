---
title: Groq | liteLLM
url: https://docs.litellm.ai/docs/providers/groq
source: sitemap
fetched_at: 2026-01-21T19:49:18.842337809-03:00
rendered_js: false
word_count: 129
summary: This document provides a comprehensive guide on integrating Groq models with LiteLLM, including setup for API keys, streaming, proxy configuration, function calling, vision, and speech-to-text.
tags:
    - litellm
    - groq
    - api-integration
    - llama-models
    - function-calling
    - streaming
    - vision-api
    - whisper-v3
category: guide
---

[https://groq.com/](https://groq.com/)

tip

**We support ALL Groq models, just set `model=groq/<any-model-on-groq>` as a prefix when sending litellm requests**

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['GROQ_API_KEY']
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['GROQ_API_KEY']=""
response = completion(
    model="groq/llama3-8b-8192",
    messages=[
{"role":"user","content":"hello from litellm"}
],
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['GROQ_API_KEY']=""
response = completion(
    model="groq/llama3-8b-8192",
    messages=[
{"role":"user","content":"hello from litellm"}
],
    stream=True
)

for chunk in response:
print(chunk)
```

## Usage with LiteLLM Proxy[​](#usage-with-litellm-proxy "Direct link to Usage with LiteLLM Proxy")

### 1. Set Groq Models on config.yaml[​](#1-set-groq-models-on-configyaml "Direct link to 1. Set Groq Models on config.yaml")

```
model_list:
-model_name: groq-llama3-8b-8192# Model Alias to use for requests
litellm_params:
model: groq/llama3-8b-8192
api_key:"os.environ/GROQ_API_KEY"# ensure you have `GROQ_API_KEY` in your .env
```

### 2. Start Proxy[​](#2-start-proxy "Direct link to 2. Start Proxy")

```
litellm --config config.yaml
```

### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

Make request to litellm proxy

- Curl Request
- OpenAI v1.0.0+
- Langchain

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "groq-llama3-8b-8192",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ]
    }
'
```

## Supported Models - ALL Groq Models Supported\![​](#supported-models---all-groq-models-supported "Direct link to Supported Models - ALL Groq Models Supported!")

We support ALL Groq models, just set `groq/` as a prefix when sending completion requests

Model NameUsagellama-3.3-70b-versatile`completion(model="groq/llama-3.3-70b-versatile", messages)`llama-3.1-8b-instant`completion(model="groq/llama-3.1-8b-instant", messages)`meta-llama/llama-4-scout-17b-16e-instruct`completion(model="groq/meta-llama/llama-4-scout-17b-16e-instruct", messages)`meta-llama/llama-4-maverick-17b-128e-instruct`completion(model="groq/meta-llama/llama-4-maverick-17b-128e-instruct", messages)`meta-llama/llama-guard-4-12b`completion(model="groq/meta-llama/llama-guard-4-12b", messages)`qwen/qwen3-32b`completion(model="groq/qwen/qwen3-32b", messages)`moonshotai/kimi-k2-instruct-0905`completion(model="groq/moonshotai/kimi-k2-instruct-0905", messages)`openai/gpt-oss-120b`completion(model="groq/openai/gpt-oss-120b", messages)`openai/gpt-oss-20b`completion(model="groq/openai/gpt-oss-20b", messages)`

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
    model="groq/llama3-8b-8192",
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
        model="groq/llama3-8b-8192", messages=messages
)# get a new response from the model where it can see the function response
print("second response\n", second_response)
```

## Groq - Vision Example[​](#groq---vision-example "Direct link to Groq - Vision Example")

Groq's Llama 4 models support vision. Check out their [model list](https://console.groq.com/docs/vision) for more details.

- SDK
- PROXY

```
import os
from litellm import completion

os.environ["GROQ_API_KEY"]="your-api-key"

response = completion(
    model ="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
{
"role":"user",
"content":[
{
"type":"text",
"text":"What's in this image?"
},
{
"type":"image_url",
"image_url":{
"url":"https://awsmp-logos.s3.amazonaws.com/seller-xw5kijmvmzasy/c233c9ade2ccb5491072ae232c814942.png"
}
}
]
}
],
)

```

## Speech to Text - Whisper[​](#speech-to-text---whisper "Direct link to Speech to Text - Whisper")

```
os.environ["GROQ_API_KEY"]=""
audio_file =open("/path/to/audio.mp3","rb")

transcript = litellm.transcription(
    model="groq/whisper-large-v3",
file=audio_file,
    prompt="Specify context or spelling",
    temperature=0,
    response_format="json"
)

print("response=", transcript)
```