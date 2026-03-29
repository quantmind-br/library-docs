---
title: Cloudinary Asset Management Extension | goose
url: https://block.github.io/goose/docs/mcp/cloudinary-asset-management-mcp
source: github_pages
fetched_at: 2026-01-22T22:14:51.118963094-03:00
rendered_js: true
word_count: 309
summary: This tutorial explains how to integrate the Cloudinary Asset Management MCP Server with goose to automate image searching and complex visual transformations using natural language.
tags:
    - cloudinary
    - mcp-server
    - goose-extension
    - image-processing
    - automation
    - image-transformation
category: tutorial
---

This tutorial covers how to add the [Cloudinary Asset Management MCP Server](https://github.com/cloudinary/asset-management-js) as a goose extension to automate complex image processing workflows that would typically require specialized design software or manual editing.

Let's use the Cloudinary extension to find and transform product images with advanced visual effects. In this example, we'll demonstrate how goose can help you:

```
1. find shoe images in my Cloudinary samples that have 'shoe' in the filename or public ID.
2. Let's transform the first result and only extract just the shoes
3. Add a white text overlay that says I love shoes. Make sure it's above the shoes
4. Add a background to the image. It should be black
```

```
I'll help you find shoe images in your Cloudinary samples and apply the transformations you've requested. Let me start by searching for images with 'shoe' in the filename or public ID.

─── list-images | cloudinaryassetmanagement ──────────────────────────
maxResults: 50
prefix: samples
type: upload

Perfect! I found the shoe images in your Cloudinary samples. I can see:

1. **`samples/shoe`** - A single shoe image (publicId: `samples/shoe`)
2. **`samples/ecommerce/shoes`** - A pair of shoes (publicId: `samples/ecommerce/shoes`)

Let me use the first result (`samples/shoe`) as requested and apply all the transformations you want:

1. Extract just the shoes (using background removal)
2. Add white text overlay "I love shoes" above the shoes
3. Add a black background

Here's the transformed image URL with all your requested modifications:

https://res.cloudinary.com/dd8qwbjtv/image/upload/e_background_removal/b_black/l_text:Arial_60:I%20love%20shoes,co_white,g_north,y_50/samples/shoe

Let me break down what each transformation does:

- `e_background_removal` - Removes the background and extracts just the shoe
- `b_black` - Adds a black background to replace the removed background
- `l_text:Arial_60:I%20love%20shoes,co_white,g_north,y_50` - Adds white text overlay:
  - `Arial_60` - Arial font, size 60
  - `I%20love%20shoes` - The text (URL encoded)
  - `co_white` - White color
  - `g_north` - Positioned at the top (north)
  - `y_50` - 50 pixels offset from the top

Here are the images we found with "shoe" in the filename/public ID:

1. **First result (used for transformation)**: `samples/shoe`
   - Original: https://res.cloudinary.com/dd8qwbjtv/image/upload/v1708364167/samples/shoe.jpg
   - **Transformed**: https://res.cloudinary.com/dd8qwbjtv/image/upload/e_background_removal/b_black/l_text:Arial_60:I%20love%20shoes,co_white,g_north,y_50/samples/shoe

2. **Second result**: `samples/ecommerce/shoes`
   - Original: https://res.cloudinary.com/dd8qwbjtv/image/upload/v1708364144/samples/ecommerce/shoes.png

The transformed image now has:
✅ Just the shoes extracted (background removed)
✅ White text "I love shoes" positioned above the shoes
✅ Black background applied

You can click on the transformed URL to see the final result!
```