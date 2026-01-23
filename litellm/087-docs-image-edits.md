---
title: /images/edits | liteLLM
url: https://docs.litellm.ai/docs/image_edits
source: sitemap
fetched_at: 2026-01-21T19:45:25.371773891-03:00
rendered_js: false
word_count: 491
summary: This document explains how to use LiteLLM's image editing capabilities across multiple providers like OpenAI and Gemini via the Python SDK and Proxy server.
tags:
    - image-editing
    - litellm
    - openai-api
    - gemini-api
    - python-sdk
    - api-proxy
category: guide
---

LiteLLM provides image editing functionality that maps to OpenAI's `/images/edits` API endpoint. Now supports both single and multiple image editing.

FeatureSupportedNotesCost Tracking✅Works with all supported modelsLogging✅Works across all integrationsEnd-user Tracking✅Fallbacks✅Works between supported modelsLoadbalancing✅Works between supported modelsSupported operationsCreate image editsSingle and multiple images supportedSupported LiteLLM SDK Versions1.63.8+Gemini support requires 1.79.3+Supported LiteLLM Proxy Versions1.71.1+Gemini support requires 1.79.3+Supported LLM providers**OpenAI**, **Gemini (Google AI Studio)**, **Vertex AI**, **Stability AI**, **AWS Bedrock (Stability)**Gemini supports the new `gemini-2.5-flash-image` family. Vertex AI supports both Gemini and Imagen models. Stability AI and Bedrock Stability support various image editing operations.

#### ⚡️See all supported models and providers at [models.litellm.ai](https://models.litellm.ai/)[​](#%EF%B8%8Fsee-all-supported-models-and-providers-at-modelslitellmai "Direct link to ️see-all-supported-models-and-providers-at-modelslitellmai")

## Usage[​](#usage "Direct link to Usage")

### LiteLLM Python SDK[​](#litellm-python-sdk "Direct link to LiteLLM Python SDK")

- OpenAI
- Vertex AI

#### Basic Image Edit[​](#basic-image-edit "Direct link to Basic Image Edit")

OpenAI Image Edit

```
import litellm

# Edit an image with a prompt
response = litellm.image_edit(
    model="gpt-image-1",
    image=open("original_image.png","rb"),
    prompt="Add a red hat to the person in the image",
    n=1,
    size="1024x1024"
)

print(response)
```

#### Multiple Images Edit[​](#multiple-images-edit "Direct link to Multiple Images Edit")

OpenAI Multiple Images Edit

```
import litellm

# Edit multiple images with a prompt
response = litellm.image_edit(
    model="gpt-image-1",
    image=[
open("image1.png","rb"),
open("image2.png","rb"),
open("image3.png","rb")
],
    prompt="Apply vintage filter to all images",
    n=1,
    size="1024x1024"
)

print(response)
```

#### Image Edit with Mask[​](#image-edit-with-mask "Direct link to Image Edit with Mask")

OpenAI Image Edit with Mask

```
import litellm

# Edit an image with a mask to specify the area to edit
response = litellm.image_edit(
    model="gpt-image-1",
    image=open("original_image.png","rb"),
    mask=open("mask_image.png","rb"),# Transparent areas will be edited
    prompt="Replace the background with a beach scene",
    n=2,
    size="512x512",
    response_format="url"
)

print(response)
```

#### Async Image Edit[​](#async-image-edit "Direct link to Async Image Edit")

Async OpenAI Image Edit

```
import litellm
import asyncio

asyncdefedit_image():
    response =await litellm.aimage_edit(
        model="gpt-image-1",
        image=open("original_image.png","rb"),
        prompt="Make the image look like a painting",
        n=1,
        size="1024x1024",
        response_format="b64_json"
)
return response

# Run the async function
response = asyncio.run(edit_image())
print(response)
```

#### Async Multiple Images Edit[​](#async-multiple-images-edit "Direct link to Async Multiple Images Edit")

Async OpenAI Multiple Images Edit

```
import litellm
import asyncio

asyncdefedit_multiple_images():
    response =await litellm.aimage_edit(
        model="gpt-image-1",
        image=[
open("portrait1.png","rb"),
open("portrait2.png","rb")
],
        prompt="Add professional lighting to the portraits",
        n=1,
        size="1024x1024",
        response_format="url"
)
return response

# Run the async function
response = asyncio.run(edit_multiple_images())
print(response)
```

#### Image Edit with Custom Parameters[​](#image-edit-with-custom-parameters "Direct link to Image Edit with Custom Parameters")

OpenAI Image Edit with Custom Parameters

```
import litellm

# Edit image with additional parameters
response = litellm.image_edit(
    model="gpt-image-1",
    image=open("portrait.png","rb"),
    prompt="Add sunglasses and a smile",
    n=3,
    size="1024x1024",
    response_format="url",
    user="user-123",
    timeout=60,
    extra_headers={"Custom-Header":"value"}
)

print(f"Generated {len(response.data)} image variations")
for i, image_data inenumerate(response.data):
print(f"Image {i+1}: {image_data.url}")
```

````

</TabItem>

<TabItem value="gemini" label="Gemini">

#### Basic Image Edit
```python showLineNumbers title="Gemini Image Edit"
import base64
import os
from litellm import image_edit

os.environ["GEMINI_API_KEY"] = "your-api-key"

response = image_edit(
    model="gemini/gemini-2.5-flash-image",
    image=open("original_image.png", "rb"),
    prompt="Add aurora borealis to the night sky",
    size="1792x1024",  # mapped to aspectRatio=16:9 for Gemini
)

edited_image_bytes = base64.b64decode(response.data[0].b64_json)
with open("edited_image.png", "wb") as f:
    f.write(edited_image_bytes)
````

#### Multiple Images Edit[​](#multiple-images-edit-1 "Direct link to Multiple Images Edit")

Gemini Multiple Images Edit

```
import base64
import os
from litellm import image_edit

os.environ["GEMINI_API_KEY"]="your-api-key"

response = image_edit(
    model="gemini/gemini-2.5-flash-image",
    image=[
open("scene.png","rb"),
open("style_reference.png","rb"),
],
    prompt="Blend the reference style into the scene while keeping the subject sharp.",
)

for idx, image_obj inenumerate(response.data):
withopen(f"gemini_edit_{idx}.png","wb")as f:
        f.write(base64.b64decode(image_obj.b64_json))
```

### LiteLLM Proxy with OpenAI SDK[​](#litellm-proxy-with-openai-sdk "Direct link to LiteLLM Proxy with OpenAI SDK")

- OpenAI
- Vertex AI

First, add this to your litellm proxy config.yaml:

OpenAI Proxy Configuration

```
model_list:
-model_name: gpt-image-1
litellm_params:
model: gpt-image-1
api_key: os.environ/OPENAI_API_KEY
```

Start the LiteLLM proxy server:

Start LiteLLM Proxy Server

```
litellm --config /path/to/config.yaml

# RUNNING on http://0.0.0.0:4000
```

#### Basic Image Edit via Proxy[​](#basic-image-edit-via-proxy "Direct link to Basic Image Edit via Proxy")

OpenAI Proxy Image Edit

```
from openai import OpenAI

# Initialize client with your proxy URL
client = OpenAI(
    base_url="http://localhost:4000",# Your proxy URL
    api_key="your-api-key"# Your proxy API key
)

# Edit an image
response = client.images.edit(
    model="gpt-image-1",
    image=open("original_image.png","rb"),
    prompt="Add a red hat to the person in the image",
    n=1,
    size="1024x1024"
)

print(response)
```

#### cURL Example[​](#curl-example "Direct link to cURL Example")

cURL Image Edit Request

```
curl -X POST "http://localhost:4000/v1/images/edits" \
  -H "Authorization: Bearer your-api-key" \
  -F "model=gpt-image-1" \
  -F "image=@original_image.png" \
  -F "mask=@mask_image.png" \
  -F "prompt=Add a beautiful sunset in the background" \
  -F "n=1" \
  -F "size=1024x1024" \
  -F "response_format=url"
```

#### cURL Multiple Images Example[​](#curl-multiple-images-example "Direct link to cURL Multiple Images Example")

cURL Multiple Images Edit Request

```
curl -X POST "http://localhost:4000/v1/images/edits" \
  -H "Authorization: Bearer your-api-key" \
  -F "model=gpt-image-1" \
  -F "image=@image1.png" \
  -F "image=@image2.png" \
  -F "image=@image3.png" \
  -F "prompt=Apply artistic filter to all images" \
  -F "n=1" \
  -F "size=1024x1024" \
  -F "response_format=url"
```

````

</TabItem>

<TabItem value="gemini" label="Gemini">

1. Add the Gemini image edit model to your `config.yaml`:
```yaml showLineNumbers title="Gemini Proxy Configuration"
model_list:
  - model_name: gemini-image-edit
    litellm_params:
      model: gemini/gemini-2.5-flash-image
      api_key: os.environ/GEMINI_API_KEY
````

2. Start the LiteLLM proxy server:

Start LiteLLM Proxy Server

```
litellm --config /path/to/config.yaml
```

3. Make an image edit request (Gemini responses are base64-only):

Gemini Proxy Image Edit

```
curl -X POST "http://0.0.0.0:4000/v1/images/edits" \
  -H "Authorization: Bearer <YOUR-LITELLM-KEY>" \
  -F "model=gemini-image-edit" \
  -F "image=@original_image.png" \
  -F "prompt=Add a warm golden-hour glow to the scene" \
  -F "size=1024x1024"
```

## Supported Image Edit Parameters[​](#supported-image-edit-parameters "Direct link to Supported Image Edit Parameters")

ParameterTypeDescriptionRequired`image``FileTypes`The image to edit. Must be a valid PNG file, less than 4MB, and square.✅`prompt``str`A text description of the desired image edit.✅`model``str`The model to use for image editingOptional (defaults to `dall-e-2`)`mask``str`An additional image whose fully transparent areas indicate where the original image should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as `image`.Optional`n``int`The number of images to generate. Must be between 1 and 10.Optional (defaults to 1)`size``str`The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.Optional (defaults to `1024x1024`)`response_format``str`The format in which the generated images are returned. Must be one of `url` or `b64_json`.Optional (defaults to `url`)`user``str`A unique identifier representing your end-user.Optional

## Response Format[​](#response-format "Direct link to Response Format")

The response follows the OpenAI Images API format:

Image Edit Response Structure

```
{
"created":1677649800,
"data":[
{
"url":"https://example.com/edited_image_1.png"
},
{
"url":"https://example.com/edited_image_2.png"
}
]
}
```

For `b64_json` format:

Base64 Response Structure

```
{
"created":1677649800,
"data":[
{
"b64_json":"iVBORw0KGgoAAAANSUhEUgAA..."
}
]
}
```