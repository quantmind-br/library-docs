---
title: Enable flexible variants · Cloudflare Images docs
url: https://developers.cloudflare.com/images/manage-images/enable-flexible-variants/index.md
source: llms
fetched_at: 2026-01-24T15:15:21.996106333-03:00
rendered_js: false
word_count: 98
summary: This document explains how to enable and use flexible variants in Cloudflare Images to allow for dynamic resizing and transformations via URL parameters. It provides instructions for activation through both the Cloudflare dashboard and the API.
tags:
    - cloudflare-images
    - flexible-variants
    - image-transformation
    - dynamic-resizing
    - image-delivery
category: configuration
---

Flexible variants allow you to create variants with dynamic resizing which can provide more options than regular variants allow. This option is not enabled by default.

## Enable flexible variants via the Cloudflare dashboard

1. In the Cloudflare dashboard, got to the **Hosted Images** page.

   [Go to **Hosted images**](https://dash.cloudflare.com/?to=/:account/images/hosted)

2. Select the **Delivery** tab.

3. Enable **Flexible variants**.

## Enable flexible variants via the API

Make a `PATCH` request to the [Update a variant endpoint](https://developers.cloudflare.com/api/resources/images/subresources/v1/subresources/variants/methods/edit/).

```bash
curl --request PATCH https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config \
--header "Authorization: Bearer <API_TOKEN>" \
--header "Content-Type: application/json" \
--data '{"flexible_variants": true}'
```

After activation, you can use [transformation parameters](https://developers.cloudflare.com/images/transform-images/transform-via-url/#options) on any Cloudflare image. For example,

`https://imagedelivery.net/{account_hash}/{image_id}/w=400,sharpen=3`

Note

Flexible variants cannot be used for images that require a [signed delivery URL](https://developers.cloudflare.com/images/manage-images/serve-images/serve-private-images).