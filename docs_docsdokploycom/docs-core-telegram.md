---
title: Telegram | Dokploy
url: https://docs.dokploy.com/docs/core/telegram
source: crawler
fetched_at: 2026-02-14T14:13:35.810266-03:00
rendered_js: true
word_count: 181
summary: This document provides step-by-step instructions for configuring Telegram notifications in Dokploy, including how to obtain a bot token and chat ID.
tags:
    - dokploy
    - telegram
    - notifications
    - bot-setup
    - alerting
category: configuration
---

Notifications

Configure telegram notifications for your applications.

Telegram notifications are a great way to stay up to date with important events in your Dokploy panel. You can choose to receive notifications for specific events or all events.

For start receiving telegram notifications, you need to fill the form with the following details:

- **Name**: Enter any name you want.
- **Bot Token**: Enter the bot token. eg. `123456789:ABCdefGHIjklMNOPqrstUVWXYZ`
- **Chat ID**: Enter the chat ID. eg. `123456789`

To Setup the telegram notifications, follow these steps:

01. Go to `https://telegram.me/botfather` and click on `Start Bot`.
02. Type `/newbot` and click on `Start`.
03. Set a name for your bot, eg. `dokploy_bot` make sure the name ends with `_bot`.
04. Copy the `Bot Token` and paste it in Dokploy `Telegram` Modal section.
05. Now you need to get the Chat ID, or create a new Channel
06. Search this bot in the search bar `@userinfobot`.
07. Type `/start` and it will return the chat ID.
08. Copy the `Chat ID` and paste it in Dokploy `Telegram` Modal section.
09. Click on test to make sure everything is working.
10. Click on `Create` to save the notification.