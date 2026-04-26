---
title: Vision | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/vision
source: sitemap
fetched_at: 2026-04-26T04:12:42.270913132-03:00
rendered_js: false
word_count: 227
summary: Utilize multimodal models with vision capabilities via the Chat Completions API, including supported model versions and image submission methods.
tags:
    - vision-models
    - multimodal-ai
    - image-analysis
    - chat-completions-api
    - ocr
    - data-extraction
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Vision

Analyze images and provide insights based on visual content using multimodal models.

> [!note] For document parsing, OCR, and data extraction, see [Document Processing](https://docs.mistral.ai/studio-api/document-processing/overview).

## Supported Models

| Model | Version | Description |
|-------|---------|-------------|
| Mistral Large 3 | `mistral-large-2512` | Highest vision capability |
| Mistral Medium 3.1 | `mistral-medium-2508` | Strong vision + efficiency |
| Mistral Small 3.2 | `mistral-small-2506` | Balanced vision + speed |
| Ministral 3 14B | `ministral-14b-2512` | On-premise capable |
| Ministral 3 8B | `ministral-8b-2512` | On-premise efficient |
| Ministral 3 3B | `ministral-3b-2512` | On-premise lightweight |

## Image Submission Methods

### Via URL

```python
response = client.chat(
    model="mistral-large-latest",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "What is in this image?"},
            {"type": "image_url", "image_url": "https://example.com/image.png"}
        ]}
    ]
)
```

### Via Base64

```python
import base64

with open("image.png", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode()

response = client.chat(
    model="mistral-large-latest",
    messages=[
        {"role": "user", "content": [
            {"type": "text", "text": "Describe this image"},
            {"type": "image_url", "image_url": f"data:image/png;base64,{image_base64}"}
        ]}
    ]
)
```

## Use Cases

| Use Case | Example |
|----------|---------|
| Graph understanding | Extract data from charts |
| Image description | Generate alt text |
| Document analysis | Parse visual documents |
| Data extraction | Pull structured data from images |

> [!tip] For OCR and structured outputs from documents, see [Document Processing](https://docs.mistral.ai/studio-api/document-processing).

#vision-models #multimodal-ai #image-analysis #chat-completions-api #ocr #data-extraction
