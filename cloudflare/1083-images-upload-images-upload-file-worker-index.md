---
title: Upload via a Worker · Cloudflare Images docs
url: https://developers.cloudflare.com/images/upload-images/upload-file-worker/index.md
source: llms
fetched_at: 2026-01-24T15:15:57.944711712-03:00
rendered_js: false
word_count: 116
summary: This document explains how to use Cloudflare Workers to upload images to Cloudflare Images, including methods for handling external image URLs and AI-generated assets.
tags:
    - cloudflare-workers
    - cloudflare-images
    - image-upload
    - workers-ai
    - typescript
    - fetch-api
category: guide
---

You can use a Worker to upload your image to Cloudflare Images.

Refer to the example below or refer to the [Workers documentation](https://developers.cloudflare.com/workers/) for more information.

```ts
const API_URL = "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/images/v1";
const TOKEN = "<YOUR_TOKEN_HERE>";


const image = await fetch("https://example.com/image.png");
const bytes = await image.bytes();


const formData = new FormData();
formData.append('file', new File([bytes], 'image.png'));


const response = await fetch(API_URL, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${TOKEN}`,
  },
  body: formData,
});
```

## Upload from AI generated images

You can use an AI Worker to generate an image and then upload that image to store it in Cloudflare Images. For more information about using Workers AI to generate an image, refer to the [SDXL-Lightning Model](https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-lightning).

```ts
const API_URL = "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/images/v1";
const TOKEN = "YOUR_TOKEN_HERE";


const stream = await env.AI.run(
  "@cf/bytedance/stable-diffusion-xl-lightning",
  {
    prompt: YOUR_PROMPT_HERE
  }
);
const bytes = await (new Response(stream)).bytes();


const formData = new FormData();
formData.append('file', new File([bytes], 'image.jpg');


const response = await fetch(API_URL, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${TOKEN}`,
  },
  body: formData,
});
```