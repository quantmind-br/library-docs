---
title: Amazon Nova | liteLLM
url: https://docs.litellm.ai/docs/providers/amazon_nova
source: sitemap
fetched_at: 2026-01-21T19:47:50.117898173-03:00
rendered_js: false
word_count: 132
summary: This document provides instructions and code examples for integrating Amazon Nova foundation models with LiteLLM, covering authentication, basic usage, streaming, and tool calling.
tags:
    - amazon-nova
    - litellm
    - api-integration
    - python-sdk
    - model-comparison
    - streaming
    - tool-calling
category: guide
---

PropertyDetailsDescriptionAmazon Nova is a family of foundation models built by Amazon that deliver frontier intelligence and industry-leading price performance.Provider Route on LiteLLM`amazon_nova/`Provider Doc[Amazon Nova ↗](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html)Supported OpenAI Endpoints`/chat/completions`, `v1/responses`Other Supported Endpoints`v1/messages`, `/generateContent`

## Authentication[​](#authentication "Direct link to Authentication")

Amazon Nova uses API key authentication. You can obtain your API key from the [Amazon Nova developer console ↗](https://nova.amazon.com/dev/documentation).

```
export AMAZON_NOVA_API_KEY="your-api-key"
```

## Usage[​](#usage "Direct link to Usage")

- SDK
- PROXY

```
import os
from litellm import completion

# Set your API key
os.environ["AMAZON_NOVA_API_KEY"]="your-api-key"

response = completion(
    model="amazon_nova/nova-micro-v1",
    messages=[
{"role":"system","content":"You are a helpful assistant"},
{"role":"user","content":"Hello, how are you?"}
]
)

print(response)
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model NameUsageContext WindowNova Micro`completion(model="amazon_nova/nova-micro-v1", messages=messages)`128K tokensNova Lite`completion(model="amazon_nova/nova-lite-v1", messages=messages)`300K tokensNova Pro`completion(model="amazon_nova/nova-pro-v1", messages=messages)`300K tokensNova Premier`completion(model="amazon_nova/nova-premier-v1", messages=messages)`1M tokens

## Usage - Streaming[​](#usage---streaming "Direct link to Usage - Streaming")

- SDK
- PROXY

```
import os
from litellm import completion

os.environ["AMAZON_NOVA_API_KEY"]="your-api-key"

response = completion(
    model="amazon_nova/nova-micro-v1",
    messages=[
{"role":"system","content":"You are a helpful assistant"},
{"role":"user","content":"Tell me about machine learning"}
],
    stream=True
)

for chunk in response:
print(chunk.choices[0].delta.content or"", end="")
```

- SDK
- PROXY

```
import os
from litellm import completion

os.environ["AMAZON_NOVA_API_KEY"]="your-api-key"

tools =[
{
"type":"function",
"function":{
"name":"getCurrentWeather",
"description":"Get the current weather in a given city",
"parameters":{
"type":"object",
"properties":{
"location":{
"type":"string",
"description":"City and country e.g. San Francisco, CA"
}
},
"required":["location"]
}
}
}
]

response = completion(
    model="amazon_nova/nova-micro-v1",
    messages=[
{"role":"user","content":"What's the weather like in San Francisco?"}
],
    tools=tools
)

print(response)
```

## Set temperature, top\_p, etc.[​](#set-temperature-top_p-etc "Direct link to Set temperature, top_p, etc.")

- SDK
- PROXY

```
import os
from litellm import completion

os.environ["AMAZON_NOVA_API_KEY"]="your-api-key"

response = completion(
    model="amazon_nova/nova-pro-v1",
    messages=[
{"role":"user","content":"Write a creative story"}
],
    temperature=0.8,
    max_tokens=500,
    top_p=0.9
)

print(response)
```

## Model Comparison[​](#model-comparison "Direct link to Model Comparison")

ModelBest ForSpeedCostContext**Nova Micro**Simple tasks, high throughputFastestLowest128K**Nova Lite**Balanced performanceFastLow300K**Nova Pro**Complex reasoningMediumMedium300K**Nova Premier**Most advanced tasksSlowerHigher1M

## Error Handling[​](#error-handling "Direct link to Error Handling")

Common error codes and their meanings:

- `401 Unauthorized`: Invalid API key
- `429 Too Many Requests`: Rate limit exceeded
- `400 Bad Request`: Invalid request format
- `500 Internal Server Error`: Service temporarily unavailable