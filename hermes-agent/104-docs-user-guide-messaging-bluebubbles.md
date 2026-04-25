---
title: BlueBubbles (iMessage) | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles
source: crawler
fetched_at: 2026-04-24T17:00:17.288358351-03:00
rendered_js: false
word_count: 502
summary: This document provides a comprehensive guide on connecting the Hermes application to Apple iMessage by utilizing BlueBubbles Server as an intermediary bridge. It details prerequisites, step-by-step setup instructions including configuration options, and explains how inbound/outbound messaging works.
tags:
    - hermes-bluebubbles
    - imap-connection
    - imessage-integration
    - macos-setup
    - api-guide
    - webhook-config
category: guide
---

Connect Hermes to Apple iMessage via [BlueBubbles](https://bluebubbles.app/) — a free, open-source macOS server that bridges iMessage to any device.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- A **Mac** (always on) running [BlueBubbles Server](https://bluebubbles.app/)
- Apple ID signed into Messages.app on that Mac
- BlueBubbles Server v1.0.0+ (webhooks require this version)
- Network connectivity between Hermes and the BlueBubbles server

## Setup[​](#setup "Direct link to Setup")

### 1. Install BlueBubbles Server[​](#1-install-bluebubbles-server "Direct link to 1. Install BlueBubbles Server")

Download and install from [bluebubbles.app](https://bluebubbles.app/). Complete the setup wizard — sign in with your Apple ID and configure a connection method (local network, Ngrok, Cloudflare, or Dynamic DNS).

### 2. Get your Server URL and Password[​](#2-get-your-server-url-and-password "Direct link to 2. Get your Server URL and Password")

In BlueBubbles Server → **Settings → API**, note:

- **Server URL** (e.g., `http://192.168.1.10:1234`)
- **Server Password**

### 3. Configure Hermes[​](#3-configure-hermes "Direct link to 3. Configure Hermes")

Run the setup wizard:

Select **BlueBubbles (iMessage)** and enter your server URL and password.

Or set environment variables directly in `~/.hermes/.env`:

```bash
BLUEBUBBLES_SERVER_URL=http://192.168.1.10:1234
BLUEBUBBLES_PASSWORD=your-server-password
```

Choose one approach:

**DM Pairing (recommended):** When someone messages your iMessage, Hermes automatically sends them a pairing code. Approve it with:

```bash
hermes pairing approve bluebubbles <CODE>
```

Use `hermes pairing list` to see pending codes and approved users.

**Pre-authorize specific users** (in `~/.hermes/.env`):

```bash
BLUEBUBBLES_ALLOWED_USERS=user@icloud.com,+15551234567
```

**Open access** (in `~/.hermes/.env`):

```bash
BLUEBUBBLES_ALLOW_ALL_USERS=true
```

### 5. Start the Gateway[​](#5-start-the-gateway "Direct link to 5. Start the Gateway")

Hermes will connect to your BlueBubbles server, register a webhook, and start listening for iMessage messages.

## How It Works[​](#how-it-works "Direct link to How It Works")

```text
iMessage → Messages.app → BlueBubbles Server → Webhook → Hermes
Hermes → BlueBubbles REST API → Messages.app → iMessage
```

- **Inbound:** BlueBubbles sends webhook events to a local listener when new messages arrive. No polling — instant delivery.
- **Outbound:** Hermes sends messages via the BlueBubbles REST API.
- **Media:** Images, voice messages, videos, and documents are supported in both directions. Inbound attachments are downloaded and cached locally for the agent to process.

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

VariableRequiredDefaultDescription`BLUEBUBBLES_SERVER_URL`Yes—BlueBubbles server URL`BLUEBUBBLES_PASSWORD`Yes—Server password`BLUEBUBBLES_WEBHOOK_HOST`No`127.0.0.1`Webhook listener bind address`BLUEBUBBLES_WEBHOOK_PORT`No`8645`Webhook listener port`BLUEBUBBLES_WEBHOOK_PATH`No`/bluebubbles-webhook`Webhook URL path`BLUEBUBBLES_HOME_CHANNEL`No—Phone/email for cron delivery`BLUEBUBBLES_ALLOWED_USERS`No—Comma-separated authorized users`BLUEBUBBLES_ALLOW_ALL_USERS`No`false`Allow all users`BLUEBUBBLES_SEND_READ_RECEIPTS`No`true`Auto-mark messages as read

## Features[​](#features "Direct link to Features")

### Text Messaging[​](#text-messaging "Direct link to Text Messaging")

Send and receive iMessages. Markdown is automatically stripped for clean plain-text delivery.

### Rich Media[​](#rich-media "Direct link to Rich Media")

- **Images:** Photos appear natively in the iMessage conversation
- **Voice messages:** Audio files sent as iMessage voice messages
- **Videos:** Video attachments
- **Documents:** Files sent as iMessage attachments

### Tapback Reactions[​](#tapback-reactions "Direct link to Tapback Reactions")

Love, like, dislike, laugh, emphasize, and question reactions. Requires the BlueBubbles [Private API helper](https://docs.bluebubbles.app/helper-bundle/installation).

### Typing Indicators[​](#typing-indicators "Direct link to Typing Indicators")

Shows "typing..." in the iMessage conversation while the agent is processing. Requires Private API.

### Read Receipts[​](#read-receipts "Direct link to Read Receipts")

Automatically marks messages as read after processing. Requires Private API.

### Chat Addressing[​](#chat-addressing "Direct link to Chat Addressing")

You can address chats by email or phone number — Hermes resolves them to BlueBubbles chat GUIDs automatically. No need to use raw GUID format.

## Private API[​](#private-api "Direct link to Private API")

Some features require the BlueBubbles [Private API helper](https://docs.bluebubbles.app/helper-bundle/installation):

- Tapback reactions
- Typing indicators
- Read receipts
- Creating new chats by address

Without the Private API, basic text messaging and media still work.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### "Cannot reach server"[​](#cannot-reach-server 'Direct link to "Cannot reach server"')

- Verify the server URL is correct and the Mac is on
- Check that BlueBubbles Server is running
- Ensure network connectivity (firewall, port forwarding)

### Messages not arriving[​](#messages-not-arriving "Direct link to Messages not arriving")

- Check that the webhook is registered in BlueBubbles Server → Settings → API → Webhooks
- Verify the webhook URL is reachable from the Mac
- Check `hermes logs gateway` for webhook errors (or `hermes logs -f` to follow in real-time)

### "Private API helper not connected"[​](#private-api-helper-not-connected 'Direct link to "Private API helper not connected"')

- Install the Private API helper: [docs.bluebubbles.app](https://docs.bluebubbles.app/helper-bundle/installation)
- Basic messaging works without it — only reactions, typing, and read receipts require it