---
title: Image generation | Mistral Docs
url: https://docs.mistral.ai/le-chat/content-creation/image-generation
source: sitemap
fetched_at: 2026-04-26T04:07:39.372075812-03:00
rendered_js: false
word_count: 432
summary: This document provides instructions on how to use the image generation tool within Le Chat, including activation steps, prompting best practices, and methods for refining or editing images.
tags:
    - image-generation
    - ai-art
    - prompt-engineering
    - le-chat
    - multimodal-features
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Le Chat can **generate and edit images** directly in the chat interface. Describe what you need **in plain language** and get visuals for presentations, product mockups, marketing materials, and more.

Le Chat uses [Black Forest Labs](https://blackforestlabs.ai) models for image generation.

## Enable Image Generation

1. Click the `+` icon or type `/` in the chat window.
2. Select `Tools` then enable `Image generation`.

Image generation stays active for the current session. You can enable other tools at the same time.

> [!info]
> Daily generation limits apply based on your plan. [Pricing page](https://mistral.ai/pricing).

## Generate Images

Describe the image you want **in natural language**. No complex prompts or special syntax needed.

For best results, include:
- **Subject**: what the image shows
- **Style**: illustration, photorealistic, diagram, flat design, etc.
- **Constraints**: aspect ratio / orientation

Example prompt: *"Create a flat illustration of a modern office interior with natural light and plants."*

## Refine or Edit Images

### Continue in the Same Conversation

After generating an image, describe changes you want in a **follow-up message**. Le Chat understands you're referring to the previous image and produces an updated version.

Example: *"Add a whiteboard on the back wall. Keep the lighting and color palette unchanged."*

### Upload an Image in a New Conversation

Start a new conversation, then upload an image using the `+` button → `Upload Files`.

Describe the edits you want and Le Chat generates a new version.

## Best Practices

- **Be specific** — *"A photorealistic hero image for a fintech landing page, dark background, abstract light trails"* produces better results than *"make a banner"*
- **Iterate** — treat the first result as a starting point; refine with follow-up prompts
- **Pair with professional tools** — image generation works best alongside dedicated editing software for final adjustments
- **Download and reuse** — click the download button on any generated image to save locally

> [!warning]
> For charts, graphs, and data visualizations, use [Code Interpreter](https://docs.mistral.ai/le-chat/content-creation/code-interpreter) instead. It generates accurate visuals from your actual data using Python.

## Limitations

- Prompts or images containing copyrighted or inappropriate content may be blocked by safety filters
- Fine details (small text, complex patterns) can sometimes be lost or altered during editing

## Related Tools

- [**Canvas**](https://docs.mistral.ai/le-chat/content-creation/canvas): create and refine presentations, documents, code
- [**Files upload**](https://docs.mistral.ai/le-chat/research-analysis/files-upload): upload images and documents for Le Chat to analyze or edit

#image-generation #ai-art #prompt-engineering