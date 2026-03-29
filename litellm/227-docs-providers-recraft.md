---
title: Recraft | liteLLM
url: https://docs.litellm.ai/docs/providers/recraft
source: sitemap
fetched_at: 2026-01-21T19:50:16.700126543-03:00
rendered_js: false
word_count: 327
summary: This document provides a guide for integrating Recraft AI with LiteLLM to perform image generation and editing via Python SDK and Proxy Server. It details setup procedures, supported models, and the implementation of both OpenAI-compatible and Recraft-specific parameters.
tags:
    - litellm
    - recraft
    - image-generation
    - image-editing
    - python-sdk
    - api-integration
    - proxy-server
category: guide
---

[https://www.recraft.ai/](https://www.recraft.ai/)

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionRecraft is an AI-powered design tool that generates high-quality images with precise control over style and content.Provider Route on LiteLLM`recraft/`Link to Provider Doc[Recraft ↗](https://www.recraft.ai/docs)Supported Operations[`/images/generations`](#image-generation), [`/images/edits`](#image-edit)

LiteLLM supports Recraft Image Generation and Image Edit calls.

## API Base, Key[​](#api-base-key "Direct link to API Base, Key")

```
# env variable
os.environ['RECRAFT_API_KEY']="your-api-key"
os.environ['RECRAFT_API_BASE']="https://external.api.recraft.ai"# [optional] 
```

## Image Generation[​](#image-generation "Direct link to Image Generation")

### Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk "Direct link to Usage - LiteLLM Python SDK")

```
from litellm import image_generation
import os

os.environ['RECRAFT_API_KEY']="your-api-key"

# recraft image generation call
response = image_generation(
    model="recraft/recraftv3",
    prompt="A beautiful sunset over a calm ocean",
)
print(response)
```

### Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server "Direct link to Usage - LiteLLM Proxy Server")

#### 1. Setup config.yaml[​](#1-setup-configyaml "Direct link to 1. Setup config.yaml")

```
model_list:
-model_name: recraft-v3
litellm_params:
model: recraft/recraftv3
api_key: os.environ/RECRAFT_API_KEY
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
    "model": "recraft-v3",
    "prompt": "A beautiful sunset over a calm ocean",
}'
```

### Advanced Usage - With Additional Parameters[​](#advanced-usage---with-additional-parameters "Direct link to Advanced Usage - With Additional Parameters")

```
from litellm import image_generation
import os

os.environ['RECRAFT_API_KEY']="your-api-key"

response = image_generation(
    model="recraft/recraftv3",
    prompt="A beautiful sunset over a calm ocean",
)
print(response)
```

### Supported Parameters[​](#supported-parameters "Direct link to Supported Parameters")

Recraft supports the following OpenAI-compatible parameters:

ParameterTypeDescriptionExample`n`integerNumber of images to generate (1-4)`1``response_format`stringFormat of response (`url` or `b64_json`)`"url"``size`stringImage dimensions`"1024x1024"``style`stringImage style/artistic direction`"realistic"`

### Using Non-OpenAI Parameters[​](#using-non-openai-parameters "Direct link to Using Non-OpenAI Parameters")

If you want to pass parameters that are not supported by OpenAI, you can pass them in your request body, LiteLLM will automatically route it to recraft.

In this example we will pass `style_id` parameter to the recraft image generation call.

**Usage with LiteLLM Python SDK**

```
from litellm import image_generation
import os

os.environ['RECRAFT_API_KEY']="your-api-key"

response = image_generation(
    model="recraft/recraftv3",
    prompt="A beautiful sunset over a calm ocean",
    style_id="your-style-id",
)
```

**Usage with LiteLLM Proxy Server + OpenAI Python SDK**

```
from openai import OpenAI
import os

os.environ['RECRAFT_API_KEY']="your-api-key"

client = OpenAI(api_key=os.environ['RECRAFT_API_KEY'])

response = client.images.generate(
    model="recraft/recraftv3",
    prompt="A beautiful sunset over a calm ocean",
    extra_body={
"style_id":"your-style-id",
},
)
print(response)
```

### Supported Image Generation Models[​](#supported-image-generation-models "Direct link to Supported Image Generation Models")

**Note: All recraft models are supported by LiteLLM** Just pass the model name with `recraft/<model_name>` and litellm will route it to recraft.

Model NameFunction Callrecraftv3`image_generation(model="recraft/recraftv3", prompt="...")`recraftv2`image_generation(model="recraft/recraftv2", prompt="...")`

For more details on available models and features, see: [https://www.recraft.ai/docs](https://www.recraft.ai/docs)

## Image Edit[​](#image-edit "Direct link to Image Edit")

### Usage - LiteLLM Python SDK[​](#usage---litellm-python-sdk-1 "Direct link to Usage - LiteLLM Python SDK")

```
from litellm import image_edit
import os

os.environ['RECRAFT_API_KEY']="your-api-key"

# Open the image file
withopen("reference_image.png","rb")as image_file:
# recraft image edit call
    response = image_edit(
        model="recraft/recraftv3",
        prompt="Create a studio ghibli style image that combines all the reference images. Make sure the person looks like a CTO.",
        image=image_file,
)
print(response)
```

### Usage - LiteLLM Proxy Server[​](#usage---litellm-proxy-server-1 "Direct link to Usage - LiteLLM Proxy Server")

#### 1. Setup config.yaml[​](#1-setup-configyaml-1 "Direct link to 1. Setup config.yaml")

```
model_list:
-model_name: recraft-v3
litellm_params:
model: recraft/recraftv3
api_key: os.environ/RECRAFT_API_KEY
model_info:
mode: image_edit

general_settings:
master_key: sk-1234
```

#### 2. Start the proxy[​](#2-start-the-proxy-1 "Direct link to 2. Start the proxy")

```
litellm --config config.yaml

# RUNNING on http://0.0.0.0:4000
```

#### 3. Test it[​](#3-test-it-1 "Direct link to 3. Test it")

```
curl --location 'http://0.0.0.0:4000/v1/images/edits' \
--header 'Authorization: Bearer sk-1234' \
--form 'model="recraft-v3"' \
--form 'prompt="Create a studio ghibli style image that combines all the reference images. Make sure the person looks like a CTO."' \
--form 'image=@"reference_image.png"'
```

### Advanced Usage - With Additional Parameters[​](#advanced-usage---with-additional-parameters-1 "Direct link to Advanced Usage - With Additional Parameters")

```
from litellm import image_edit
import os

os.environ['RECRAFT_API_KEY']="your-api-key"

withopen("reference_image.png","rb")as image_file:
    response = image_edit(
        model="recraft/recraftv3",
        prompt="Create a studio ghibli style image",
        image=image_file,
        n=2,# Generate 2 variations
        response_format="url",# Return URLs instead of base64
        style="realistic_image",# Set artistic style
        strength=0.5# Control transformation strength (0-1)
)
print(response)
```

### Supported Image Edit Parameters[​](#supported-image-edit-parameters "Direct link to Supported Image Edit Parameters")

Recraft supports the following OpenAI-compatible parameters for image editing:

ParameterTypeDescriptionDefaultExample`n`integerNumber of images to generate (1-4)`1``2``response_format`stringFormat of response (`url` or `b64_json`)`"url"``"b64_json"``style`stringImage style/artistic direction-`"realistic_image"``strength`floatControls how much to transform the image (0.0-1.0)`0.2``0.5`

### Using Non-OpenAI Parameters[​](#using-non-openai-parameters-1 "Direct link to Using Non-OpenAI Parameters")

You can pass Recraft-specific parameters that are not part of the OpenAI API by including them in your request:

**Usage with LiteLLM Python SDK**

```
from litellm import image_edit
import os

os.environ['RECRAFT_API_KEY']="your-api-key"

withopen("reference_image.png","rb")as image_file:
    response = image_edit(
        model="recraft/recraftv3",
        prompt="Create a studio ghibli style image",
        image=image_file,
        style_id="your-style-id",# Recraft-specific parameter
        strength=0.7
)
```

**Usage with LiteLLM Proxy Server + OpenAI Python SDK**

```
from openai import OpenAI
import os

client = OpenAI(
    api_key="sk-1234",# your LiteLLM proxy master key
    base_url="http://0.0.0.0:4000"# your LiteLLM proxy URL
)

withopen("reference_image.png","rb")as image_file:
    response = client.images.edit(
        model="recraft-v3",
        prompt="Create a studio ghibli style image",
        image=image_file,
        extra_body={
"style_id":"your-style-id",
"strength":0.7
}
)
print(response)
```

### Supported Image Edit Models[​](#supported-image-edit-models "Direct link to Supported Image Edit Models")

**Note: All recraft models are supported by LiteLLM** Just pass the model name with `recraft/<model_name>` and litellm will route it to recraft.

Model NameFunction Callrecraftv3`image_edit(model="recraft/recraftv3", ...)`

## API Key Setup[​](#api-key-setup "Direct link to API Key Setup")

Get your API key from [Recraft's website](https://www.recraft.ai/) and set it as an environment variable:

```
export RECRAFT_API_KEY="your-api-key"
```