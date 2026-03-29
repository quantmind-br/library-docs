---
title: Mistral AI API | liteLLM
url: https://docs.litellm.ai/docs/providers/mistral
source: sitemap
fetched_at: 2026-01-21T19:49:41.848239533-03:00
rendered_js: false
word_count: 87
summary: This document provides code examples and instructions for integrating Mistral AI models with LiteLLM, covering chat completions, streaming, function calling, embeddings, and reasoning parameters.
tags:
    - litellm
    - mistral-ai
    - python
    - function-calling
    - embeddings
    - llm-reasoning
    - api-integration
category: guide
---

```
from litellm import completion
import os

os.environ['MISTRAL_API_KEY']=""
response = completion(
    model="mistral/mistral-tiny",
    messages=[
{"role":"user","content":"hello from litellm"}
],
)
print(response)
```

```
from litellm import completion
import os

os.environ['MISTRAL_API_KEY']=""
response = completion(
    model="mistral/mistral-tiny",
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

```
from litellm import completion

# set env
os.environ["MISTRAL_API_KEY"]="your-api-key"

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
    model="mistral/mistral-large-latest",
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

Mistral does not directly support reasoning, instead it recommends a specific [system prompt](https://docs.mistral.ai/capabilities/reasoning/) to use with their magistral models. By setting the `reasoning_effort` parameter, LiteLLM will prepend the system prompt to the request.

If an existing system message is provided, LiteLLM will send both as a list of system messages (you can verify this by enabling `litellm._turn_on_debug()`).

The `reasoning_effort` parameter controls how much effort the model puts into reasoning. When used with magistral models.

```
from litellm import completion
import os

os.environ['MISTRAL_API_KEY']="your-api-key"

response = completion(
    model="mistral/magistral-medium-2506",
    messages=[
{"role":"user","content":"What is 15 multiplied by 7?"}
],
    reasoning_effort="medium"# Options: "low", "medium", "high"
)

print(response)
```

If you already have a system message, LiteLLM will prepend the reasoning instructions:

```
response = completion(
    model="mistral/magistral-medium-2506",
    messages=[
{"role":"system","content":"You are a helpful math tutor."},
{"role":"user","content":"Explain how to solve quadratic equations."}
],
    reasoning_effort="high"
)

# The system message becomes:
# "When solving problems, think step-by-step in <think> tags before providing your final answer...
#  
#  You are a helpful math tutor."
```

```
from litellm import embedding
import os

os.environ['MISTRAL_API_KEY']=""
response = embedding(
    model="mistral/mistral-embed",
input=["good morning from litellm"],
)
print(response)
```