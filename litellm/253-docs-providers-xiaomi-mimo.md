---
title: Xiaomi MiMo | liteLLM
url: https://docs.litellm.ai/docs/providers/xiaomi_mimo
source: sitemap
fetched_at: 2026-01-21T19:51:01.212898682-03:00
rendered_js: false
word_count: 67
summary: This document provides instructions for integrating Xiaomi MiMo models using LiteLLM, covering API key configuration, streaming implementation, and proxy server setup.
tags:
    - xiaomi-mimo
    - litellm
    - api-integration
    - python
    - streaming
    - proxy-server
category: guide
---

[https://platform.xiaomimimo.com/#/docs](https://platform.xiaomimimo.com/#/docs)

tip

**We support ALL Xiaomi MiMo models, just set `model=xiaomi_mimo/<any-model-on-xiaomi-mimo>` as a prefix when sending litellm requests**

## API Key[​](#api-key "Direct link to API Key")

```
# env variable
os.environ['XIAOMI_MIMO_API_KEY']
```

## Sample Usage[​](#sample-usage "Direct link to Sample Usage")

```
from litellm import completion
import os

os.environ['XIAOMI_MIMO_API_KEY']=""
response = completion(
    model="xiaomi_mimo/mimo-v2-flash",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit?",
}
],
    max_tokens=1024,
    temperature=0.3,
    top_p=0.95,
)
print(response)
```

## Sample Usage - Streaming[​](#sample-usage---streaming "Direct link to Sample Usage - Streaming")

```
from litellm import completion
import os

os.environ['XIAOMI_MIMO_API_KEY']=""
response = completion(
    model="xiaomi_mimo/mimo-v2-flash",
    messages=[
{
"role":"user",
"content":"What's the weather like in Boston today in Fahrenheit?",
}
],
    stream=True,
    max_tokens=1024,
    temperature=0.3,
    top_p=0.95,
)

for chunk in response:
print(chunk)
```

## Usage with LiteLLM Proxy Server[​](#usage-with-litellm-proxy-server "Direct link to Usage with LiteLLM Proxy Server")

Here's how to call a Xiaomi MiMo model with the LiteLLM Proxy Server

1. Modify the config.yaml

```
model_list:
-model_name: my-model
litellm_params:
model: xiaomi_mimo/<your-model-name># add xiaomi_mimo/ prefix to route as Xiaomi MiMo provider
api_key: api-key                      # api key to send your model
```

2. Start the proxy

```
$ litellm --config /path/to/config.yaml
```

3. Send Request to LiteLLM Proxy Server

<!--THE END-->

- OpenAI Python v1.0.0+
- curl

```
import openai
client = openai.OpenAI(
    api_key="sk-1234",# pass litellm proxy key, if you're using virtual keys
    base_url="http://0.0.0.0:4000"# litellm-proxy-base url
)

response = client.chat.completions.create(
    model="my-model",
    messages =[
{
"role":"user",
"content":"what llm are you"
}
],
)

print(response)
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

Model NameUsagemimo-v2-flash`completion(model="xiaomi_mimo/mimo-v2-flash", messages)`