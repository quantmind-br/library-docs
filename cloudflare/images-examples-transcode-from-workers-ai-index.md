---
title: Transcode images · Cloudflare Images docs
url: https://developers.cloudflare.com/images/examples/transcode-from-workers-ai/index.md
source: llms
fetched_at: 2026-01-24T15:15:13.025318928-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates a workflow for generating an image using Cloudflare Workers AI, converting it to AVIF format, and storing the resulting file in Cloudflare R2.
tags:
    - cloudflare-workers
    - workers-ai
    - stable-diffusion
    - image-processing
    - r2-storage
    - serverless
category: tutorial
---

```js
const stream = await env.AI.run(
  "@cf/bytedance/stable-diffusion-xl-lightning",
  {
    prompt: YOUR_PROMPT_HERE
  }
);


// Convert to AVIF
const image = (
  await env.IMAGES.input(stream)
    .output({format: "image/avif"})
).response();


const fileName = "image.avif";


// Upload to R2
await env.R2.put(fileName, image.body);
```