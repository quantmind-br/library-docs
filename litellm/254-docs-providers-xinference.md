---
title: Xinference [Xorbits Inference] | liteLLM
url: https://docs.litellm.ai/docs/providers/xinference
source: sitemap
fetched_at: 2026-01-21T19:51:01.770141011-03:00
rendered_js: false
word_count: 133
summary: This document provides instructions and code examples for integrating LiteLLM with Xinference to perform text embedding and image generation tasks.
tags:
    - xinference
    - litellm
    - embeddings
    - image-generation
    - python-sdk
    - proxy-server
category: guide
---

[https://inference.readthedocs.io/en/latest/index.html](https://inference.readthedocs.io/en/latest/index.html)

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionXinference is an open-source platform to run inference with any open-source LLMs, image generation models, and more.Provider Route on LiteLLM`xinference/`Link to Provider Doc[Xinference ↗](https://inference.readthedocs.io/en/latest/index.html)Supported Operations[`/embeddings`](#sample-usage---embedding), [`/images/generations`](#image-generation)

LiteLLM supports Xinference Embedding + Image Generation calls.

## API Base, Key[​](#api-base-key "Direct link to API Base, Key")

```
# env variable
os.environ['XINFERENCE_API_BASE']="http://127.0.0.1:9997/v1"
os.environ['XINFERENCE_API_KEY']="anything"#[optional] no api key required
```

## Sample Usage - Embedding[​](#sample-usage---embedding "Direct link to Sample Usage - Embedding")

```
from litellm import embedding
import os

os.environ['XINFERENCE_API_BASE']="http://127.0.0.1:9997/v1"
response = embedding(
    model="xinference/bge-base-en",
input=["good morning from litellm"],
)
print(response)
```

## Sample Usage `api_base` param[​](#sample-usage-api_base-param "Direct link to sample-usage-api_base-param")

```
from litellm import embedding
import os

response = embedding(
    model="xinference/bge-base-en",
    api_base="http://127.0.0.1:9997/v1",
input=["good morning from litellm"],
)
print(response)
```

## Image Generation[​](#image-generation "Direct link to Image Generation")

### Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

```
from litellm import image_generation
import os

# xinference image generation call
response = image_generation(
    model="xinference/stabilityai/stable-diffusion-3.5-large",
    prompt="A beautiful sunset over a calm ocean",
    api_base="http://127.0.0.1:9997/v1",
)
print(response)
```

### Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

#### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

```
model_list:
-model_name: xinference-sd
litellm_params:
model: xinference/stabilityai/stable-diffusion-3.5-large
api_base: http://127.0.0.1:9997/v1
api_key: anything
model_info:
mode: image_generation

general_settings:
master_key: sk-1234
```

#### 2. Start the proxy[​](#2-start-the-proxy "Direct link to 2. Start the proxy")

```
litellm --config config.yaml

# RUNNING on http://0.0.0.0:4000
```

#### 3. Test it[​](#3-test-it "Direct link to 3. Test it")

```
curl --location 'http://0.0.0.0:4000/v1/images/generations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-1234' \
--data '{
    "model": "xinference-sd",
    "prompt": "A beautiful sunset over a calm ocean",
    "n": 1,
    "size": "1024x1024",
    "response_format": "url"
}'
```

### Advanced Usage - With Additional Parameters[​](#advanced-usage---with-additional-parameters "Direct link to Advanced Usage - With Additional Parameters")

```
from litellm import image_generation
import os

os.environ['XINFERENCE_API_BASE']="http://127.0.0.1:9997/v1"

response = image_generation(
    model="xinference/stabilityai/stable-diffusion-3.5-large",
    prompt="A beautiful sunset over a calm ocean",
    n=1,# number of images
    size="1024x1024",# image size
    response_format="b64_json",# return format
)
print(response)
```

### Supported Image Generation Models[​](#supported-image-generation-models "Direct link to Supported Image Generation Models")

Xinference supports various stable diffusion models. Here are some examples:

Model NameFunction Callstabilityai/stable-diffusion-3.5-large`image_generation(model="xinference/stabilityai/stable-diffusion-3.5-large", prompt="...")`stabilityai/stable-diffusion-xl-base-1.0`image_generation(model="xinference/stabilityai/stable-diffusion-xl-base-1.0", prompt="...")`runwayml/stable-diffusion-v1-5`image_generation(model="xinference/runwayml/stable-diffusion-v1-5", prompt="...")`

For a complete list of supported image generation models, see: [https://inference.readthedocs.io/en/latest/models/builtin/image/index.html](https://inference.readthedocs.io/en/latest/models/builtin/image/index.html)

## Supported Models[​](#supported-models "Direct link to Supported Models")

All models listed here [https://inference.readthedocs.io/en/latest/models/builtin/embedding/index.html](https://inference.readthedocs.io/en/latest/models/builtin/embedding/index.html) are supported

Model NameFunction Callbge-base-en`embedding(model="xinference/bge-base-en", input)`bge-base-en-v1.5`embedding(model="xinference/bge-base-en-v1.5", input)`bge-base-zh`embedding(model="xinference/bge-base-zh", input)`bge-base-zh-v1.5`embedding(model="xinference/bge-base-zh-v1.5", input)`bge-large-en`embedding(model="xinference/bge-large-en", input)`bge-large-en-v1.5`embedding(model="xinference/bge-large-en-v1.5", input)`bge-large-zh`embedding(model="xinference/bge-large-zh", input)`bge-large-zh-noinstruct`embedding(model="xinference/bge-large-zh-noinstruct", input)`bge-large-zh-v1.5`embedding(model="xinference/bge-large-zh-v1.5", input)`bge-small-en-v1.5`embedding(model="xinference/bge-small-en-v1.5", input)`bge-small-zh`embedding(model="xinference/bge-small-zh", input)`bge-small-zh-v1.5`embedding(model="xinference/bge-small-zh-v1.5", input)`e5-large-v2`embedding(model="xinference/e5-large-v2", input)`gte-base`embedding(model="xinference/gte-base", input)`gte-large`embedding(model="xinference/gte-large", input)`jina-embeddings-v2-base-en`embedding(model="xinference/jina-embeddings-v2-base-en", input)`jina-embeddings-v2-small-en`embedding(model="xinference/jina-embeddings-v2-small-en", input)`multilingual-e5-large`embedding(model="xinference/multilingual-e5-large", input)`