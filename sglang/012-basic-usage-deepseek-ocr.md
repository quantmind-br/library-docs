---
title: DeepSeek OCR (OCR-1 / OCR-2) — SGLang
url: https://docs.sglang.io/basic_usage/deepseek_ocr.html
source: crawler
fetched_at: 2026-02-04T08:47:41.750418-03:00
rendered_js: false
word_count: 38
summary: This guide explains how to deploy DeepSeek OCR models and perform document understanding tasks using an OpenAI-compatible API server.
tags:
    - deepseek-ocr
    - ocr
    - document-understanding
    - multimodal
    - api-deployment
category: guide
---

## DeepSeek OCR (OCR-1 / OCR-2)[#](#deepseek-ocr-ocr-1-ocr-2 "Link to this heading")

DeepSeek OCR models are multimodal (image + text) models for OCR and document understanding.

## Launch server[#](#launch-server "Link to this heading")

```
python-msglang.launch_server\
--model-pathdeepseek-ai/DeepSeek-OCR-2\
--trust-remote-code\
--host0.0.0.0\
--port30000
```

> You can replace `deepseek-ai/DeepSeek-OCR-2` with `deepseek-ai/DeepSeek-OCR`.

## Prompt examples[#](#prompt-examples "Link to this heading")

Recommended prompts from the model card:

```
<image>
<|grounding|>Convert the document to markdown.
```

## OpenAI-compatible request example[#](#openai-compatible-request-example "Link to this heading")

```
importrequests

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