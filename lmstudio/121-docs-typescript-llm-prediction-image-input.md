---
title: Image Input
url: https://lmstudio.ai/docs/typescript/llm-prediction/image-input
source: sitemap
fetched_at: 2026-04-07T21:31:46.63819085-03:00
rendered_js: false
word_count: 166
summary: This document provides a step-by-step guide on how to use Vision-Language Models (VLMs) by first ensuring a VLM is available, then preparing an input image using specific client methods, and finally passing both the image and prompt to the model's respond method.
tags:
    - vlm
    - vision-language-models
    - image-input
    - api-usage
    - model-interaction
    - base64
category: tutorial
---

Some models, known as VLMs (Vision-Language Models), can accept images as input. You can pass images to the model using the `.respond()` method.

### Prerequisite: Get a VLM (Vision-Language Model)[](#prerequisite-get-a-vlm-vision-language-model)

If you don't yet have a VLM, you can download a model like `qwen2-vl-2b-instruct` using the following command:

```

lms get qwen2-vl-2b-instruct
```

## 1. Instantiate the Model[](#1-instantiate-the-model "Link to '1. Instantiate the Model'")

Connect to LM Studio and obtain a handle to the VLM (Vision-Language Model) you want to use.

## 2. Prepare the Image[](#2-prepare-the-image "Link to '2. Prepare the Image'")

Use the `client.files.prepareImage()` method to get a handle to the image that can be subsequently passed to the model.

If you only have the image in the form of a base64 string, you can use the `client.files.prepareImageBase64()` method instead.

The LM Studio server supports JPEG, PNG, and WebP image formats.

## 3. Pass the Image to the Model in `.respond()`[](#3-pass-the-image-to-the-model-in-respond "Link to '3. Pass the Image to the Model in ,[object Object]'")

Generate a prediction by passing the image to the model in the `.respond()` method.