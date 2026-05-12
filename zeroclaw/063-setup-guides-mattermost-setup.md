---
title: Mattermost Integration Guide
date: 2026-05-05T00:00:00Z
url: https://github.com/openagen/zeroclaw/blob/master/docs/setup-guides/mattermost-setup.md
source: git
fetched_at: 2026-05-02T14:52:15.614834088-03:00
rendered_js: false
word_count: 300
summary: This document provides instructions for integrating ZeroClaw with a Mattermost instance to enable private, sovereign communication via the Mattermost REST API.
tags:
    - mattermost
    - integration
    - bot-configuration
    - zeroclaw
    - messaging
    - sovereign-communication
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Mattermost Integration Guide

ZeroClaw supports native integration with Mattermost via REST API v4. Ideal for self-hosted, private, or air-gapped environments requiring sovereign communication.

## Prerequisites

1. **Mattermost Server:** Running Mattermost instance (self-hosted or cloud)
2. **Bot Account:**
   - Go to **Main Menu > Integrations > Bot Accounts**
   - Click **Add Bot Account**
   - Set username (e.g., `zeroclaw-bot`)
   - Enable **post:all** and **channel:read** permissions
   - Save **Access Token**
3. **Channel ID:**
   - Open target channel
   - Click channel header > **View Info**
   - Copy **ID** (e.g., `7j8k9l...`)

## Configuration

Add to `config.toml` under `[channels_config]`:

```toml
[channels_config.mattermost]
url = "https://mm.your-domain.com"
bot_token = "your-bot-access-token"
channel_id = "your-channel-id"
allowed_users = ["user-id-1", "user-id-2"]
thread_replies = true
mention_only = true
```

### Configuration Fields

| Field | Description |
|---|---|
| `url` | Base URL of Mattermost server |
| `bot_token` | Personal Access Token for bot account |
| `channel_id` | (Optional) Channel ID to listen to. Required for `listen` mode |
| `allowed_users` | (Optional) List of Mattermost User IDs permitted to interact. Use `["*"]` to allow everyone |
| `thread_replies` | (Optional) Whether top-level messages should be answered in a thread. Default: `true` |
| `mention_only` | (Optional) Process only messages explicitly mentioning bot. Default: `false` |

## Threaded Conversations

ZeroClaw supports Mattermost threads:
- Messages in existing threads → always replied within same thread
- If `thread_replies = true` (default), top-level messages answered by threading
- If `thread_replies = false`, top-level messages answered at channel root

## Mention-Only Mode

When `mention_only = true`, ZeroClaw applies extra filter after `allowed_users` authorization:
- Ignores messages without explicit bot mention
- Processes messages with `@bot_username`
- Strips `@bot_username` token before sending to model

Useful in busy shared channels to reduce unnecessary model calls.

## Security Note

Mattermost integration is designed for **sovereign communication**. Hosting your own Mattermost server keeps agent communication history entirely within your infrastructure, avoiding third-party cloud logging.

#mattermost #integration #bot-configuration #zeroclaw #messaging #sovereign-communication
