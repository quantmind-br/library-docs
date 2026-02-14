---
title: Discord | Dokploy
url: https://docs.dokploy.com/docs/core/discord
source: crawler
fetched_at: 2026-02-14T14:13:35.908672-03:00
rendered_js: true
word_count: 153
summary: This guide provides instructions for setting up and configuring Discord webhook notifications within the Dokploy panel to receive real-time application alerts.
tags:
    - discord
    - notifications
    - dokploy
    - webhook-integration
    - monitoring
    - server-alerts
category: configuration
---

Notifications

Configure discord notifications for your applications.

Discord notifications are a great way to stay up to date with important events in your Dokploy panel. You can choose to receive notifications for specific events or all events.

For start receiving discord notifications, you need to fill the form with the following details:

- **Name**: Enter any name you want.
- **Webhook URL**: Enter the webhook URL. eg. `https://discord.com/api/webhooks/000000000000000/00000000-0000-0000-0000-000000000000`

To Setup the Discord notifications, follow these steps:

1. Go to Discord, and search your Discord server.
2. Go to `Server Settings` and click on `Integrations`.
3. Click on `Create a Webhook`.
4. Set a name for your webhook, eg. `dokploy_webhook`.
5. Click on the `Webhook` you've created and click on copy the `Webhook URL`.
6. Go to Dokploy `Notifications` and select `Discord` as the notification provider.
7. Use the `Webhook URL` you copied in the previous step.
8. Click on `Test` to make sure everything is working.
9. Click on `Create` to save the notification.