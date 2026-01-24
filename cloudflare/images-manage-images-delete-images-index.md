---
title: Delete images · Cloudflare Images docs
url: https://developers.cloudflare.com/images/manage-images/delete-images/index.md
source: llms
fetched_at: 2026-01-24T15:15:21.067345409-03:00
rendered_js: false
word_count: 109
summary: This document provides instructions for deleting images from Cloudflare Images using either the dashboard interface or the API.
tags:
    - cloudflare-images
    - image-management
    - delete-operation
    - api-endpoint
    - dashboard
category: guide
---

You can delete an image from the Cloudflare Images storage using the dashboard or the API.

## Delete images via the Cloudflare dashboard

1. In the Cloudflare dashboard, go to **Transformations** page.

   [Go to **Transformations**](https://dash.cloudflare.com/?to=/:account/images/transformations)

2. Find the image you want to remove and select **Delete**.

3. (Optional) To delete more than one image, select the checkbox next to the images you want to delete and then **Delete selected**.

Your image will be deleted from your account.

## Delete images via the API

Make a `DELETE` request to the [delete image endpoint](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/delete/). `{image_id}` must be fully URL encoded in the API call URL.

```bash
curl --request DELETE https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/{image_id} \
--header "Authorization: Bearer <API_TOKEN>"
```

After the image has been deleted, the response returns `"success": true`.