---
title: Vision Models
url: https://docs.fireworks.ai/guides/querying-vision-language-models
source: sitemap
fetched_at: 2026-04-27T20:18:27.422436089-03:00
rendered_js: false
word_count: 217
summary: Guide for using Vision-Language Models (VLMs) via the Chat Completions API, covering image input via URL/base64, PDF analysis, and performance optimization.
tags:
    - vlm-integration
    - chat-completions-api
    - image-processing
    - pdf-analysis
    - api-reference
    - multimodal-ai
category: guide
optimized: true
optimized_at: 2026-04-27T23:00:00Z
---
Vision-language models (VLMs) process text and images in a single request for captioning, visual QA, document analysis, chart interpretation, OCR, and content moderation. Use via serverless inference or [[008-getting-started-ondemand-quickstart|ondemand deployments]]. [Browse available vision models →](https://app.fireworks.ai/models?filter=Vision)

## Chat Completions API

Provide images via URL or base64 encoding. Request structure matches OpenAI's vision API.

- Python
- JavaScript
- curl

```python
from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2p5",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you describe this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?w=800"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/kimi-k2p5",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "Can you describe this image?" },
        {
          type: "image_url",
          image_url: {
            url: "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?w=800"
          }
        }
      ]
    }
  ]
});

console.log(response.choices[0].message.content);
```

```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/kimi-k2p5",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "Can you describe this image?"},
          {
            "type": "image_url",
            "image_url": {
              "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?w=800"
            }
          }
        ]
      }
    ]
  }'
```

## Base64-encoded Images

For local files, encode with MIME type prefix:

```python
import base64
from fireworks import Fireworks

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_base64 = encode_image("your_image.jpg")

client = Fireworks()

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2p5",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you describe this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
```

```javascript
import OpenAI from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const imageBase64 = fs.readFileSync("your_image.jpg").toString("base64");

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/kimi-k2p5",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "Can you describe this image?" },
        {
          type: "image_url",
          image_url: {
            url: `data:image/jpeg;base64,${imageBase64}`
          }
        }
      ]
    }
  ]
});

console.log(response.choices[0].message.content);
```

## Image Performance

VLMs support [[072-guides-prompt-caching|Prompt Caching]] to reduce TTFT by up to 80%.

- **Use URLs for long conversations** — lower latency than base64
- **Downsize images** — smaller images use fewer tokens
- **Structure prompts for caching** — static instructions first, variable content last
- **Include metadata in prompts** — add context about the image in your text

## PDFs

VLMs do not natively accept PDFs. Convert each page to an image and pass via base64.

Install dependencies: [PyMuPDF](https://pymupdf.readthedocs.io/) or [pdf-to-img](https://www.npmjs.com/package/pdf-to-img).

```python
pip install pymupdf fireworks-ai

import base64
import fitz
from fireworks.client import Fireworks


def pdf_pages_to_base64(pdf_path, dpi=200):
    doc = fitz.open(pdf_path)
    images = []
    for page in doc:
        pix = page.get_pixmap(dpi=dpi)
        images.append(base64.b64encode(pix.tobytes("png")).decode("utf-8"))
    doc.close()
    return images


page_images = pdf_pages_to_base64("document.pdf")

client = Fireworks()

content = [{"type": "text", "text": "Summarize this document."}]
for img in page_images:
    content.append({
        "type": "image_url",
        "image_url": {"url": f"data:image/png;base64,{img}"}
    })

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2p5",
    messages=[{"role": "user", "content": content}]
)

print(response.choices[0].message.content)
```

```javascript
npm install pdf-to-img openai

import { pdf } from "pdf-to-img";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FIREWORKS_API_KEY,
  baseURL: "https://api.fireworks.ai/inference/v1",
});

const pages = [];
for await (const page of await pdf("document.pdf", { scale: 2.0 })) {
  pages.push(Buffer.from(page).toString("base64"));
}

const content = [
  { type: "text", text: "Summarize this document." },
  ...pages.map((base64) => ({
    type: "image_url",
    image_url: { url: `data:image/png;base64,${base64}` },
  })),
];

const response = await client.chat.completions.create({
  model: "accounts/fireworks/models/kimi-k2p5",
  messages: [{ role: "user", content }],
});

console.log(response.choices[0].message.content);
```

## Alternative Query Methods

For the Completions API, insert `<image>` token manually and supply images as an ordered list:

```python
response = client.completions.create(
    model="accounts/fireworks/models/kimi-k2p5",
    prompt="SYSTEM: Hello\n\nUSER:<image>\ntell me about the image\n\nASSISTANT:",
    extra_body={
        "images": ["https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"]
    }
)

print(response.choices[0].text)
```

## Known Limitations

- **Max images per request**: 30
- **Base64 size limit**: <10MB total
- **URL size/timeout**: <5MB, must download within 1.5s
- **Supported formats**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff`, `.ppm`
- **Llama 3.2 Vision**: Pass images before text in content field (temporary limitation)