---
title: Slack | Dokploy
url: https://docs.dokploy.com/docs/core/slack
source: crawler
fetched_at: 2026-02-14T14:13:37.122782-03:00
rendered_js: true
word_count: 159
summary: This document provides step-by-step instructions for configuring Slack notifications in Dokploy to receive real-time updates on application events via webhooks.
tags:
    - dokploy
    - slack-integration
    - notifications
    - webhooks
    - event-monitoring
    - configuration-guide
category: configuration
---

Notifications

Configure slack notifications for your applications.

Slack notifications are a great way to stay up to date with important events in your Dokploy panel. You can choose to receive notifications for specific events or all events.

For start receiving slack notifications, you need to fill the form with the following details:

- **Name**: Enter any name you want.
- **Webhook URL**: Enter the webhook URL. eg. `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`
- **Channel**: Enter the channel name that you want to send the notifications to.

To Setup the slack notifications, follow these steps:

1. Go to `https://dokploy.slack.com/marketplace/A0F7XDUAZ-webhooks-entrantes` and click on `Add To Slack`.
2. Select the channel that you want to send the notifications to.
3. Click on `Add webhook to channel`.
4. Copy the `Webhook URL`.
5. Go to Dokploy `Notifications` and select `Slack` as the notification provider.
6. Use the `Webhook URL` you copied in the previous step.
7. In Channel section, select the channel that you want to send the notifications to.
8. Click on `Create` to save the notification.