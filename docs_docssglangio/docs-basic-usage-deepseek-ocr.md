---
title: DeepSeek OCR (OCR-1 / OCR-2) - SGLang Documentation
url: https://docs.sglang.io/docs/basic_usage/deepseek_ocr
source: sitemap
fetched_at: 2026-05-11T05:49:23.872079785-03:00
rendered_js: false
word_count: 54
summary: This document provides instructions on how to launch the DeepSeek OCR multimodal model server and perform inference requests using the OpenAI-compatible API.
tags:
    - sglang
    - deepseek-ocr
    - multimodal-models
    - server-deployment
    - ocr-processing
    - api-integration
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

DeepSeek OCR models are multimodal (image + text) models for OCR and document understanding.

## Launch server

```
python -m sglang.launch_server \
  --model-path deepseek-ai/DeepSeek-OCR-2 \
  --trust-remote-code \
  --host 0.0.0.0 \
  --port 30000
```

> You can replace `deepseek-ai/DeepSeek-OCR-2` with `deepseek-ai/DeepSeek-OCR`.

## Prompt examples

Recommended prompts from the model card:

```
<image>
<|grounding|>Convert the document to markdown.
```

## OpenAI-compatible request example

```
import requests

url = "http://localhost:30000/v1/chat/completions"

data = {
    "model": "deepseek-ai/DeepSeek-OCR-2",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "<image>\n<|grounding|>Convert the document to markdown."},
                {"type": "image_url", "image_url": {"url": "https://example.com/your_image.jpg"}},
            ],
        }
    ],
    "max_tokens": 512,
}

response = requests.post(url, json=data)
print(response.text)
```