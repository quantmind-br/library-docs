---
title: How do I control output image sizes when using SDXL ControlNet? - Fireworks AI Docs
url: https://docs.fireworks.ai/faq-new/models-inference/how-do-i-control-output-image-sizes-when-using-sdxl-controlnet
source: sitemap
fetched_at: 2026-04-27T20:12:53.953754016-03:00
rendered_js: false
word_count: 77
summary: Output image dimensions for SDXL ControlNet are controlled via explicit width and height parameters in the API request.
tags:
    - sdxl-controlnet
    - api-parameters
    - image-sizing
    - width-height
    - resizing-cropping
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# How do I control output image sizes when using SDXL ControlNet?

When using **SDXL ControlNet** (e.g., canny control), the output image size is determined by explicit **width** and **height** parameters in your API request. The input control signal image will be automatically:

- **Resized** to fit your specified dimensions
- **Cropped** to preserve aspect ratio

```json
{
    "width": 768,
    "height": 1344
}
```

> [!note]
> While these parameters may not appear in web interface examples, they are supported API parameters.

#sdxl-controlnet #image-sizing #api-parameters
