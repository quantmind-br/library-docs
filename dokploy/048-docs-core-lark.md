---
title: Lark | Dokploy
url: https://docs.dokploy.com/docs/core/lark
source: crawler
fetched_at: 2026-02-14T14:18:30.8084-03:00
rendered_js: true
word_count: 146
summary: This document provides step-by-step instructions for configuring Lark notifications in Dokploy using webhook URLs to receive application event alerts.
tags:
    - dokploy
    - lark
    - notifications
    - webhook-integration
    - alerting
    - notification-setup
category: configuration
---

Notifications

Configure Lark notifications for your applications.

Lark notifications are a great way to stay up to date with important events in your Dokploy panel. You can choose to receive notifications for specific events or all events.

To start receiving Lark notifications, you need to fill the form with the following details:

- **Name**: Enter any name you want.
- **Webhook URL**: Enter the webhook URL. eg. `https://open.larksuite.com/open-apis/bot/v2/hook/xxxxxxxxxxxxxxxxxxxxxxxx`

To setup Lark notifications, follow these steps:

1. Go to your Lark workspace and navigate to the bot configuration.
2. Create a new bot or use an existing one.
3. Copy the webhook URL from your Lark bot settings.
4. Go to Dokploy **Notifications** and select **Lark** as the notification provider.
5. Enter a name for your notification configuration.
6. Paste the webhook URL you copied in the previous step.
7. Click on **Test** to make sure everything is working.
8. Click on **Create** to save the notification.