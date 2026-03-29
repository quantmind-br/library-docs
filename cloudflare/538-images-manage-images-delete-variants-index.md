---
title: Delete variants · Cloudflare Images docs
url: https://developers.cloudflare.com/images/manage-images/delete-variants/index.md
source: llms
fetched_at: 2026-01-24T15:15:23.908252301-03:00
rendered_js: false
word_count: 94
summary: This document explains how to delete image variants through the Cloudflare dashboard or via an API request, including a warning about global impact and restrictions on the public variant.
tags:
    - cloudflare-images
    - image-variants
    - api-delete
    - dashboard-management
    - data-removal
category: guide
---

You can delete variants via the Images dashboard or API. The only variant you cannot delete is public.

Warning

Deleting a variant is a global action that will affect other images that contain that variant.

## Delete variants via the Cloudflare dashboard

1. In the Cloudflare dashboard, got to the **Hosted Images** page.

   [Go to **Hosted images**](https://dash.cloudflare.com/?to=/:account/images/hosted)

2. Select the **Delivery** tab.

3. Find the variant you want to remove and select **Delete**.

## Delete variants via the API

Make a `DELETE` request to the delete variant endpoint.

```bash
curl --request DELETE https://api.cloudflare.com/client/v4/account/{account_id}/images/v1/variants/{variant_name} \
--header "Authorization: Bearer <API_TOKEN>"
```

After the variant has been deleted, the response returns `"success": true.`