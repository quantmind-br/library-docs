---
title: GigaChat | liteLLM
url: https://docs.litellm.ai/docs/providers/gigachat
source: sitemap
fetched_at: 2026-01-21T19:49:11.205770941-03:00
rendered_js: false
word_count: 212
summary: This document provides technical instructions for integrating Sber AI's GigaChat models with the LiteLLM library, covering authentication, SSL configuration, and specific API features.
tags:
    - gigachat
    - litellm
    - sber-ai
    - python-sdk
    - llm-api
    - embeddings
    - vision-api
category: api
---

[https://developers.sber.ru/docs/ru/gigachat/api/overview](https://developers.sber.ru/docs/ru/gigachat/api/overview)

GigaChat is Sber AI's large language model, Russia's leading LLM provider.

tip

**We support ALL GigaChat models, just set `model=gigachat/<any-model-on-gigachat>` as a prefix when sending litellm requests**

warning

GigaChat API uses self-signed SSL certificates. You must pass `ssl_verify=False` in your requests.

## Supported Features[​](#supported-features "Direct link to Supported Features")

FeatureSupportedChat CompletionYesStreamingYesAsyncYesFunction Calling / ToolsYesStructured Output (JSON Schema)Yes (via function call emulation)Image InputYes (base64 and URL) - GigaChat-2-Max, GigaChat-2-Pro onlyEmbeddingsYes

## API Key[​](#api-key "Direct link to API Key")

GigaChat uses OAuth authentication. Set your credentials as environment variables:

```
import os

# Required: Set credentials (base64-encoded client_id:client_secret)
os.environ['GIGACHAT_CREDENTIALS']="your-credentials-here"

# Optional: Set scope (default is GIGACHAT_API_PERS for personal use)
os.environ['GIGACHAT_SCOPE']="GIGACHAT_API_PERS"# or GIGACHAT_API_B2B for business
```

Get your credentials at: [https://developers.sber.ru/studio/](https://developers.sber.ru/studio/)

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['GIGACHAT_CREDENTIALS']="your-credentials-here"

response = completion(
    model="gigachat/GigaChat-2-Max",
    messages=[
{"role":"user","content":"Hello from LiteLLM!"}
],
    ssl_verify=False,# Required for GigaChat
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['GIGACHAT_CREDENTIALS']="your-credentials-here"

response = completion(
    model="gigachat/GigaChat-2-Max",
    messages=[
{"role":"user","content":"Hello from LiteLLM!"}
],
    stream=True,
    ssl_verify=False,# Required for GigaChat
)

for chunk in response:
print(chunk)
```

## Sample Usage - Function Calling[​](#sample-usage---function-calling "Direct link to Sample Usage - Function Calling")

```
from litellm import completion
import os

os.environ['GIGACHAT_CREDENTIALS']="your-credentials-here"

tools =[{
"type":"function",
"function":{
"name":"get_weather",
"description":"Get weather for a city",
"parameters":{
"type":"object",
"properties":{
"city":{"type":"string","description":"City name"}
},
"required":["city"]
}
}
}]

response = completion(
    model="gigachat/GigaChat-2-Max",
    messages=[{"role":"user","content":"What's the weather in Moscow?"}],
    tools=tools,
    ssl_verify=False,# Required for GigaChat
)
print(response)
```

## Sample Usage - Structured Output[​](#sample-usage---structured-output "Direct link to Sample Usage - Structured Output")

GigaChat supports structured output via JSON schema (emulated through function calling):

```
from litellm import completion
import os

os.environ['GIGACHAT_CREDENTIALS']="your-credentials-here"

response = completion(
    model="gigachat/GigaChat-2-Max",
    messages=[{"role":"user","content":"Extract info: John is 30 years old"}],
    response_format={
"type":"json_schema",
"json_schema":{
"name":"person",
"schema":{
"type":"object",
"properties":{
"name":{"type":"string"},
"age":{"type":"integer"}
}
}
}
},
    ssl_verify=False,# Required for GigaChat
)
print(response)# Returns JSON: {"name": "John", "age": 30}
```

## Sample Usage - Image Input[​](#sample-usage---image-input "Direct link to Sample Usage - Image Input")

GigaChat supports image input via base64 or URL (GigaChat-2-Max and GigaChat-2-Pro only):

```
from litellm import completion
import os

os.environ['GIGACHAT_CREDENTIALS']="your-credentials-here"

response = completion(
    model="gigachat/GigaChat-2-Max",# Vision requires GigaChat-2-Max or GigaChat-2-Pro
    messages=[{
"role":"user",
"content":[
{"type":"text","text":"What's in this image?"},
{"type":"image_url","image_url":{"url":"https://example.com/image.jpg"}}
]
}],
    ssl_verify=False,# Required for GigaChat
)
print(response)
```

## Sample Usage - Embeddings[​](#sample-usage---embeddings "Direct link to Sample Usage - Embeddings")

```
from litellm import embedding
import os

os.environ['GIGACHAT_CREDENTIALS']="your-credentials-here"

response = embedding(
    model="gigachat/Embeddings",
input=["Hello world","How are you?"],
    ssl_verify=False,# Required for GigaChat
)
print(response)
```

## Usage with LiteLLM Proxy[​](#usage-with-litellm-proxy "Direct link to Usage with LiteLLM Proxy")

### 1. Set GigaChat Models on config.yaml[​](#1-set-gigachat-models-on-configyaml "Direct link to 1. Set GigaChat Models on config.yaml")

```
model_list:
-model_name: gigachat
litellm_params:
model: gigachat/GigaChat-2-Max
api_key:"os.environ/GIGACHAT_CREDENTIALS"
ssl_verify:false
-model_name: gigachat-lite
litellm_params:
model: gigachat/GigaChat-2-Lite
api_key:"os.environ/GIGACHAT_CREDENTIALS"
ssl_verify:false
-model_name: gigachat-embeddings
litellm_params:
model: gigachat/Embeddings
api_key:"os.environ/GIGACHAT_CREDENTIALS"
ssl_verify:false
```

### 2. Start Proxy[​](#2-start-proxy "Direct link to 2. Start Proxy")

```
litellm --config config.yaml
```

### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

- Curl Request
- OpenAI v1.0.0+

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data '{
    "model": "gigachat",
    "messages": [
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}'
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

### Chat Models[​](#chat-models "Direct link to Chat Models")

Model NameContext WindowVisionDescriptiongigachat/GigaChat-2-Lite128KNoFast, lightweight modelgigachat/GigaChat-2-Pro128KYesProfessional model with visiongigachat/GigaChat-2-Max128KYesMaximum capability model

### Embedding Models[​](#embedding-models "Direct link to Embedding Models")

Model NameMax InputDimensionsDescriptiongigachat/Embeddings5121024Standard embeddingsgigachat/Embeddings-25121024Updated embeddingsgigachat/EmbeddingsGigaR40962560High-dimensional embeddings

note

Available models may vary depending on your API access level (personal or business).

## Limitations[​](#limitations "Direct link to Limitations")

- Only one function call per request (GigaChat API limitation)
- Maximum 1 image per message, 10 images total per conversation
- GigaChat API uses self-signed SSL certificates - `ssl_verify=False` is required