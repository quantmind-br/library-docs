---
title: Using Vision Models | liteLLM
url: https://docs.litellm.ai/docs/completion/vision
source: sitemap
fetched_at: 2026-01-21T19:44:48.146464171-03:00
rendered_js: false
word_count: 103
summary: This document explains how to use vision-capable models with LiteLLM, including instructions for passing images, checking model compatibility, and specifying image mime-types.
tags:
    - litellm
    - vision-models
    - multimodal
    - python-sdk
    - image-processing
    - api-proxy
category: guide
---

## Quick Start[​](#quick-start "Direct link to Quick Start")

Example passing images to a model

- LiteLLMPython SDK
- LiteLLM Proxy Server

```
import os 
from litellm import completion

os.environ["OPENAI_API_KEY"]="your-api-key"

# openai call
response = completion(
    model ="gpt-4-vision-preview",
    messages=[
{
"role":"user",
"content":[
{
"type":"text",
"text":"What’s in this image?"
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

## Checking if a model supports `vision`[​](#checking-if-a-model-supports-vision "Direct link to checking-if-a-model-supports-vision")

- LiteLLM Python SDK
- LiteLLM Proxy Server

Use `litellm.supports_vision(model="")` -&gt; returns `True` if model supports `vision` and `False` if not

```
assert litellm.supports_vision(model="openai/gpt-4-vision-preview")==True
assert litellm.supports_vision(model="vertex_ai/gemini-1.0-pro-vision")==True
assert litellm.supports_vision(model="openai/gpt-3.5-turbo")==False
assert litellm.supports_vision(model="xai/grok-2-vision-latest")==True
assert litellm.supports_vision(model="xai/grok-2-latest")==False
```

## Explicitly specify image type[​](#explicitly-specify-image-type "Direct link to Explicitly specify image type")

If you have images without a mime-type, or if litellm is incorrectly inferring the mime type of your image (e.g. calling `gs://` url's with vertex ai), you can set this explicitly via the `format` param.

```
"image_url":{
"url":"gs://my-gs-image",
"format":"image/jpeg"
}
```

LiteLLM will use this for any API endpoint, which supports specifying mime-type (e.g. anthropic/bedrock/vertex ai).

For others (e.g. openai), it will be ignored.

- SDK
- PROXY

```
import os 
from litellm import completion

os.environ["ANTHROPIC_API_KEY"]="your-api-key"

# openai call
response = completion(
    model ="claude-3-7-sonnet-latest",
    messages=[
{
"role":"user",
"content":[
{
"type":"text",
"text":"What’s in this image?"
},
{
"type":"image_url",
"image_url":{
"url":"https://awsmp-logos.s3.amazonaws.com/seller-xw5kijmvmzasy/c233c9ade2ccb5491072ae232c814942.png",
"format":"image/jpeg"
}
}
]
}
],
)

```

## Spec[​](#spec "Direct link to Spec")

```
"image_url": str

OR 

"image_url": {
  "url": "url OR base64 encoded str",
  "detail": "openai-only param", 
  "format": "specify mime-type of image"
}
```