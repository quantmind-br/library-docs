---
title: Configure webhooks · Cloudflare Images docs
url: https://developers.cloudflare.com/images/manage-images/configure-webhooks/index.md
source: llms
fetched_at: 2026-01-24T15:15:17.686917402-03:00
rendered_js: false
word_count: 135
summary: This document explains how to configure webhooks in the Cloudflare dashboard to receive automated notifications for image upload successes or failures.
tags:
    - cloudflare-images
    - webhooks
    - notifications
    - direct-creator-upload
    - event-notifications
category: guide
---

You can set up webhooks to receive notifications about your upload workflow. This will send an HTTP POST request to a specified endpoint when an image either successfully uploads or fails to upload.

Currently, webhooks are supported only for [direct creator uploads](https://developers.cloudflare.com/images/upload-images/direct-creator-upload/).

To receive notifications for direct creator uploads:

1. In the Cloudflare dashboard, go to the **Notifications** pages.

   [Go to **Notifications**](https://dash.cloudflare.com/?to=/:account/notifications)

2. Select **Destinations**.

3. From the Webhooks card, select **Create**.

4. Enter information for your webhook and select **Save and Test**. The new webhook will appear in the **Webhooks** card and can be attached to notifications.

5. Next, go to **Notifications** > **All Notifications** and select **Add**.

6. Under the list of products, locate **Images** and select **Select**.

7. Give your notification a name and optional description.

8. Under the **Webhooks** field, select the webhook that you recently created.

9. Select **Save**.