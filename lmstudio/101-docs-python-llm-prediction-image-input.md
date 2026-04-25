---
title: Image Input
url: https://lmstudio.ai/docs/python/llm-prediction/image-input
source: sitemap
fetched_at: 2026-04-07T21:31:02.812304207-03:00
rendered_js: false
word_count: 218
summary: This guide details the process of using Vision-Language Models (VLMs) with an SDK, covering prerequisites like obtaining a VLM, preparing an image handle from various inputs, and finally passing the image to the model using the `.respond()` method.
tags:
    - vlm
    - image-input
    - model-interaction
    - python-sdk
    - api-usage
    - multimodal
category: guide
---

*Required Python SDK version*: **1.1.0**

Some models, known as VLMs (Vision-Language Models), can accept images as input. You can pass images to the model using the `.respond()` method.

### Prerequisite: Get a VLM (Vision-Language Model)[](#prerequisite-get-a-vlm-vision-language-model)

If you don't yet have a VLM, you can download a model like `qwen2-vl-2b-instruct` using the following command:

```

lms get qwen2-vl-2b-instruct
```

## 1. Instantiate the Model[](#1-instantiate-the-model "Link to '1. Instantiate the Model'")

Connect to LM Studio and obtain a handle to the VLM (Vision-Language Model) you want to use.

## 2. Prepare the Image[](#2-prepare-the-image "Link to '2. Prepare the Image'")

Use the `prepare_image()` function or `files` namespace method to get a handle to the image that can subsequently be passed to the model.

If you only have the raw data of the image, you can supply the raw data directly as a bytes object without having to write it to disk first. Due to this feature, binary filesystem paths are *not* supported (as they will be handled as malformed image data rather than as filesystem paths).

Binary IO objects are also accepted as local file inputs.

The LM Studio server supports JPEG, PNG, and WebP image formats.

## 3. Pass the Image to the Model in `.respond()`[](#3-pass-the-image-to-the-model-in-respond "Link to '3. Pass the Image to the Model in ,[object Object]'")

Generate a prediction by passing the image to the model in the `.respond()` method.