---
title: Vision | Mistral Docs
url: https://docs.mistral.ai/capabilities/vision
source: crawler
fetched_at: 2026-01-29T07:33:07.398134767-03:00
rendered_js: false
word_count: 258
summary: This document introduces Mistral's vision-capable models and explains how to integrate image analysis into applications using the Chat Completions API.
tags:
    - mistral-ai
    - vision-models
    - multimodal
    - image-analysis
    - chat-completions-api
category: guide
---

Vision capabilities enable models to **analyze images and provide insights based on visual content** in addition to text. This multimodal approach opens up new possibilities for applications that require both textual and visual understanding.

We provide a variety of models with vision capabilities, all available via the Chat Completions API.

For more specific use cases regarding Document Parsing, OCR and Data Extraction we recommend taking a look at our Document AI stack [here](https://docs.mistral.ai/capabilities/document_ai).

### Recommended Models with Vision Capabilities

- **Mistral Large 3** via `mistral-large-2512`
- **Mistral Medium 3.1** via `mistral-medium-2508`
- **Mistral Small 3.2** via `mistral-small-2506`
- **Ministral 3**:
  
  - Ministral 3 14B via `ministral-14b-2512`
  - Ministral 3 8B via `ministral-8b-2512`
  - Ministral 3 3B via `ministral-3b-2512`

### Use Vision Models

There are two ways to send an image to the Chat Completions API, either by passing a URL or by passing a base64 encoded image.

Before continuing, we recommend reading the [Chat Competions](https://docs.mistral.ai/capabilities/completion) documentation to learn more about the chat completions API and how to use it before proceeding.

If the image is hosted online, you can simply provide the **publicaly accessible URL of the image** in the request. This method is straightforward and does not require any encoding.

Below you can find a few examples of use cases leveraging our models vision, from understanding graphs to extract data, the use cases are diverse.

These are simple examples you can use as inspiration to build your own use cases, for OCR and Structured Outputs, we recommend leveraging [Document AI](https://docs.mistral.ai/capabilities/document_ai/document_ai_overview) and [Document AI Annotations](https://docs.mistral.ai/capabilities/document_ai/annotations).

![Cat head](https://docs.mistral.ai/_next/image?url=%2Fassets%2Fsprites%2Fcat_head.png&w=48&q=75)

¡Meow! Click one of the tabs above to learn more.