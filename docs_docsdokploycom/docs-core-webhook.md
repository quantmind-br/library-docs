---
title: Webhook | Dokploy
url: https://docs.dokploy.com/docs/core/webhook
source: crawler
fetched_at: 2026-02-14T14:12:53.538725-03:00
rendered_js: true
word_count: 226
summary: This document explains how to set up, test, and manage webhook notifications in Dokploy to receive real-time event updates via JSON payloads.
tags:
    - dokploy
    - webhook-notifications
    - http-endpoints
    - json-payload
    - event-handling
    - notification-configuration
category: guide
---

Notifications

Configure webhook notifications for your applications.

Webhook notifications are a generic way to receive notifications from Dokploy to any HTTP endpoint. You can choose to receive notifications for specific events or all events. Notifications are sent in JSON format.

To start receiving webhook notifications, you need to fill the form with the following details:

- **Name**: Enter any name you want.
- **Webhook URL**: Enter the webhook URL where you want to receive notifications. eg. `https://your-endpoint.com/webhook`

For testing purposes, you can use [Webhook.site](https://webhook.site) to generate a unique URL and inspect the JSON payload that Dokploy sends:

1. Go to [https://webhook.site](https://webhook.site)
2. Copy your unique webhook URL
3. Go to Dokploy **Notifications** and select **Webhook** as the notification provider
4. Enter a name for your notification configuration
5. Paste the webhook URL you copied
6. Click on **Test** to send a test notification
7. Check your Webhook.site page to see the JSON payload
8. Click on **Create** to save the notification

Dokploy sends notifications in JSON format. The payload structure includes information about the event type, timestamp, and relevant details about the action that triggered the notification.

**Example notification payload:**

```
{
  "title": "Test Notification",
  "message": "Hi, From Dokploy 👋",
  "timestamp": "2025-12-07T19:41:53.470Z"
}
```

For production use, ensure your webhook endpoint:

- Accepts POST requests
- Returns a 2xx HTTP status code for successful delivery
- Handles JSON payloads
- Is accessible from the internet (or from your Dokploy server's network)
- Implements proper authentication if needed (consider using HTTPS with API keys in headers)