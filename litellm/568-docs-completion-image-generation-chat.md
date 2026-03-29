---
title: Image Generation in Chat Completions, Responses API | liteLLM
url: https://docs.litellm.ai/docs/completion/image_generation_chat
source: sitemap
fetched_at: 2026-01-21T19:44:27.578924952-03:00
rendered_js: false
word_count: 160
summary: Explains how to use LiteLLM to generate images through the chat completions endpoint using supported models from Google AI Studio and Vertex AI.
tags:
    - litellm
    - image-generation
    - gemini
    - vertex-ai
    - chat-completions
    - python-sdk
    - streaming
category: guide
---

This guide covers how to generate images when using the `chat/completions`. Note - if you want this on Responses API please file a Feature Request [here](https://github.com/BerriAI/litellm/issues/new).

info

Requires LiteLLM v1.76.1+

Supported Providers:

- Google AI Studio (`gemini`)
- Vertex AI (`vertex_ai/`)

LiteLLM will standardize the `images` response in the assistant message for models that support image generation during chat completions.

Example response from litellm

```
"message":{
...
"content":"Here's the image you requested:",
"images":[
{
"image_url":{
"url":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
"detail":"auto"
},
"index":0,
"type":"image_url"
}
]
}
```

## Quick Start[​](#quick-start "Direct link to Quick Start")

- SDK
- PROXY

Image generation with chat completion

```
from litellm import completion
import os 

os.environ["GEMINI_API_KEY"]="your-api-key"

response = completion(
    model="gemini/gemini-2.5-flash-image-preview",
    messages=[
{"role":"user","content":"Generate an image of a banana wearing a costume that says LiteLLM"}
],
)

print(response.choices[0].message.content)# Text response
print(response.choices[0].message.images)# List of image objects
```

**Expected Response**

```
{
    "id": "chatcmpl-3b66124d79a708e10c603496b363574c",
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "Here's the image you requested:",
                "role": "assistant",
                "images": [
                    {
                        "image_url": {
                            "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
                            "detail": "auto"
                        },
                        "index": 0,
                        "type": "image_url"
                    }
                ]
            }
        }
    ],
    "created": 1723323084,
    "model": "gemini/gemini-2.5-flash-image-preview",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 12,
        "prompt_tokens": 16,
        "total_tokens": 28
    }
}
```

## Streaming Support[​](#streaming-support "Direct link to Streaming Support")

- SDK
- PROXY

Streaming image generation

```
from litellm import completion
import os 

os.environ["GEMINI_API_KEY"]="your-api-key"

response = completion(
    model="gemini/gemini-2.5-flash-image-preview",
    messages=[
{"role":"user","content":"Generate an image of a banana wearing a costume that says LiteLLM"}
],
    stream=True,
)

for chunk in response:
ifhasattr(chunk.choices[0].delta,"images")and chunk.choices[0].delta.images isnotNone:
print("Generated image:", chunk.choices[0].delta.images[0]["image_url"]["url"])
break
```

**Expected Streaming Response**

```
data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1723323084,"model":"gemini/gemini-2.5-flash-image-preview","choices":[{"index":0,"delta":{"role":"assistant"},"finish_reason":null}]}

data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1723323084,"model":"gemini/gemini-2.5-flash-image-preview","choices":[{"index":0,"delta":{"content":"Here's the image you requested:"},"finish_reason":null}]}

data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1723323084,"model":"gemini/gemini-2.5-flash-image-preview","choices":[{"index":0,"delta":{"images":[{"image_url":{"url":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...","detail":"auto"},"index":0,"type":"image_url"}]},"finish_reason":null}]}

data: {"id":"chatcmpl-123","object":"chat.completion.chunk","created":1723323084,"model":"gemini/gemini-2.5-flash-image-preview","choices":[{"index":0,"delta":{},"finish_reason":"stop"}]}

data: [DONE]
```

## Async Support[​](#async-support "Direct link to Async Support")

Async image generation

```
from litellm import acompletion
import asyncio
import os 

os.environ["GEMINI_API_KEY"]="your-api-key"

asyncdefgenerate_image():
    response =await acompletion(
        model="gemini/gemini-2.5-flash-image-preview",
        messages=[
{"role":"user","content":"Generate an image of a banana wearing a costume that says LiteLLM"}
],
)

print(response.choices[0].message.content)# Text response
print(response.choices[0].message.images)# List of image objects

return response

# Run the async function
asyncio.run(generate_image())
```

## Supported Models[​](#supported-models "Direct link to Supported Models")

ProviderModelGoogle AI Studio`gemini/gemini-2.0-flash-preview-image-generation`, `gemini/gemini-2.5-flash-image-preview`, `gemini/gemini-3-pro-image-preview`Vertex AI`vertex_ai/gemini-2.0-flash-preview-image-generation`, `vertex_ai/gemini-2.5-flash-image-preview`, `vertex_ai/gemini-3-pro-image-preview`

## Spec[​](#spec "Direct link to Spec")

The `images` field in the response follows this structure:

```
"images":[
{
"image_url":{
"url":"data:image/png;base64,<base64_encoded_image>",
"detail":"auto"
},
"index":0,
"type":"image_url"
}
]
```

- `images` - List\[ImageURLListItem]: Array of generated images
  
  - `image_url` - ImageURLObject: Container for image data
    
    - `url` - str: Base64 encoded image data in data URI format
    - `detail` - str: Image detail level (always "auto" for generated images)
  - `index` - int: Index of the image in the response
  - `type` - str: Type identifier (always "image\_url")

The images are returned as base64-encoded data URIs that can be directly used in HTML `<img>` tags or saved to files.