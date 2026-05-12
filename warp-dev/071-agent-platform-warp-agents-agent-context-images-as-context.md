---
title: Images as context | Agents | Warp
url: https://docs.warp.dev/agent-platform/warp-agents/agent-context/images-as-context
source: sitemap
fetched_at: 2026-04-29T15:04:05.856105628-03:00
rendered_js: false
word_count: 184
summary: This document explains how to attach images to agent prompts in Warp for visual context, including supported formats, constraints, and platform limitations.
tags:
    - image-attachments
    - ai-agents
    - user-interface
    - visual-context
    - multimodal-input
    - warp-terminal
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
# Images as Context

Attach images directly to an agent prompt to provide visual context such as screenshots, diagrams, or other visual references.

## Attaching Images

Attach images via:
- **Image upload button** on the toolbelt (bottom-left for Universal input, bottom-right for Classic input)
- Copy and paste images directly into Warp
- Drag and drop images from a file manager or screenshot utility

> [!info]
> Supported formats: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`

Limits: **5 images per request**, **20 images per conversation**. Images are sent to the model provider and immediately discarded — nothing stored on Warp servers.

> [!warning]
> **Cloud agent conversations do not support image attachments.** Image attachment is only available in local agent conversations. For cloud agents, describe image contents in your prompt or reference the file path in the cloud agent's [environment](https://docs.warp.dev/agent-platform/cloud-agents/environments).

## Model Behavior and Image Handling

All models listed in [Model Choice](https://docs.warp.dev/agent-platform/warp-agents/capabilities-overview/model-choice) can interpret image input.

Attaching images consumes additional requests proportional to the number of images. Warp intelligently resizes images before passing them as context to minimize token usage and respect model maximum image dimensions.
