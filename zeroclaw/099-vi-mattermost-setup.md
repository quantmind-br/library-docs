---
title: Mattermost setup
authors:
  - ZeroClaw Team
tags:
  - mattermost
  - integration
  - configuration
  - zeroclaw
  - self-hosted
  - api-integration
  - messaging-bot
  - team-collaboration
category: configuration
optimized: true
optimized_at: 2026-05-05T10:00:00Z
word_count: 1118
---
# ZeroClaw Mattermost Integration Setup Guide

> Native Mattermost integration for ZeroClaw bot via REST API v4.
> Ideal for self-hosted, private, or air-gapped environments requiring sovereign communication.

## Tóm tắt nhanh

Configure ZeroClaw to receive and respond to Mattermost messages with thread support and user filtering.

**Quick setup:**

```toml
[channels_config.mattermost]
url = "https://mm.your-domain.com"
bot_token = "your-bot-access-token"
channel_id = "your-channel-id"
allowed_users = ["*"]
thread_replies = true
mention_only = false
```

## Prerequisites

### 1. Mattermost Server

- **Self-hosted Mattermost** instance running
- **Version**: Mattermost v7.0+ recommended
- **Access**: Admin or sufficient permissions to create bot accounts

### 2. Create Bot Account

**Steps:**

1. Log in to Mattermost
2. Open **Main Menu** (top-left hamburger menu)
3. Navigate to **Integrations > Bot Accounts**
4. Click **Add Bot Account**
5. Configure bot:
   - **Username**: `zeroclaw-bot` (or your preferred name)
   - **Display Name**: ZeroClaw Bot
   - **Description**: AI assistant bot
6. Set permissions:
   - Enable **post:all** (Post to any channel)
   - Enable **channel:read** (Read channel messages)
   - Enable **user:read** (Read user information)
   - Enable **team:read** (Read team information)
7. Save bot account
8. **Copy Access Token** (save securely!)

### 3. Get Channel ID

**Steps to find channel ID:**

1. Open the Mattermost channel where bot should operate
2. Click channel header (top of channel)
3. Select **View Info**
4. Scroll to **Channel ID** section
5. Copy the ID (format: `7j8k9l...`)

**Alternative method (API):**

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "https://mm.your-domain.com/api/v4/channels/name/your-channel-name" | jq '.id'
```

### 4. Get User IDs (Optional)

For `allowed_users` configuration:

```bash
# Get your own user ID
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "https://mm.your-domain.com/api/v4/users/me" | jq '.id'

# Get all users in a team
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "https://mm.your-domain.com/api/v4/users" | jq '.[].id'
```

## Configuration

### Configuration File (config.toml)

Add to `~/.zeroclaw/config.toml`:

```toml
[channels_config.mattermost]
# Required: Mattermost server base URL
url = "https://mm.your-domain.com"

# Required: Bot access token
bot_token = "your-bot-access-token"

# Optional: Channel ID to listen on
# If not specified, bot listens to all channels it has access to
channel_id = "your-channel-id"

# Optional: Allowed users (Mattermost User IDs)
# ["*"] = allow all, [] = deny all, ["user1", "user2"] = specific users
allowed_users = ["*"]

# Optional: Thread behavior
thread_replies = true  # Default: true

# Optional: Mention-only mode
mention_only = false  # Default: false
```

### Environment Variables

```bash
# Override bot token
export ZEROCLAW_MATTERMOST_BOT_TOKEN="your-token"

# Override base URL
export ZEROCLAW_MATTERMOST_URL="https://mm.your-domain.com"
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `url` | string | Yes | Mattermost server base URL (e.g., `https://mm.your-domain.com`) |
| `bot_token` | string | Yes | Bot's personal access token for API authentication |
| `channel_id` | string | No | Specific channel ID to monitor (optional) |
| `allowed_users` | array | No | List of allowed Mattermost User IDs |
| `thread_replies` | boolean | No | Whether to reply in threads (default: `true`) |
| `mention_only` | boolean | No | Only respond to messages mentioning bot (default: `false`) |

## Thread Conversation Support

ZeroClaw supports Mattermost threads in both modes:

### Thread Behavior Matrix

| Scenario | thread_replies | Behavior |
|----------|----------------|----------|
| Message in existing thread | Any | Reply stays in same thread |
| Top-level message | `true` | Create new thread on message |
| Top-level message | `false` | Reply at channel level |

### Examples

**Scenario 1: Existing Thread**
- User sends message in existing thread
- ZeroClaw replies in same thread ✅

**Scenario 2: New Top-Level Message (thread_replies=true)**
- User sends: "Hello bot"
- ZeroClaw creates thread on that message
- ZeroClaw replies in the new thread ✅

**Scenario 3: New Top-Level Message (thread_replies=false)**
- User sends: "Hello bot"
- ZeroClaw replies at channel level (no thread) ✅

## Mention-Only Mode

When `mention_only = true`, ZeroClaw applies additional filtering:

### How It Works

1. **Message arrives** from Mattermost webhook
2. **Check allowed_users** (if configured)
3. **Check mention filter**: Does message contain `@bot_username`?
4. **Process message** only if both checks pass
5. **Remove mention token** before sending to model

### Example

**User message:**
```
Hey @zeroclaw-bot, what's the status of project X?
```

**After processing:**
```
what's the status of project X?
```

### Benefits

- **Reduces unnecessary model calls** in busy channels
- **Prevents accidental triggers** from unrelated conversations
- **Improves user experience** by requiring explicit mentions
- **Saves costs** by avoiding unnecessary API calls

### When to Use

✅ **Use mention_only=true when:**
- Bot operates in shared channels
- High message volume expected
- Cost optimization is important
- Channel contains diverse topics

❌ **Use mention_only=false when:**
- Bot operates in dedicated channel
- Low message volume expected
- Need to catch all messages

## Security Considerations

### Self-Hosted Sovereignty

> **ZeroClaw Mattermost integration is designed for internal communication.**

By self-hosting your Mattermost server, **all agent communication history remains within your infrastructure**, avoiding third-party logging or data retention.

### Token Security

- **Store bot token securely**: Use environment variables or secret management
- **Rotate tokens regularly**: Every 90 days or when compromised
- **Use dedicated bot account**: Don't use admin account
- **Limit permissions**: Only grant necessary permissions
- **Never commit to version control**

### Network Security

- **HTTPS only**: Always use HTTPS in production
- **IP allowlisting**: Restrict Mattermost server access
- **Rate limiting**: Implement at gateway level
- **Monitor access**: Watch for unusual API calls

## Webhook Configuration

### ZeroClaw Gateway Setup

```bash
# Start ZeroClaw gateway
zeroclaw daemon

# Or start with specific host/port
zeroclaw gateway --host 0.0.0.0 --port 8080
```

### Mattermost Webhook Setup

1. **Go to Mattermost** → Channel where bot should operate
2. **Click channel header** → **View Info** → **Webhooks**
3. **Create Outgoing Webhook**
4. **Configure webhook:**
   - **Callback URL**: `https://your-zeroclaw-domain/mattermost`
   - **Trigger Words**: (Optional) Add trigger words if needed
   - **Channel**: Select specific channel or all channels
   - **Content Type**: `application/json`
5. **Save webhook**

### Webhook Payload Example

**Incoming message:**
```json
{
  "token": "webhook-token",
  "team_id": "team123",
  "channel_id": "channel456",
  "channel_name": "general",
  "timestamp": 1234567890,
  "user_id": "user789",
  "user_name": "alice",
  "text": "Hello @zeroclaw-bot, what's the weather today?",
  "trigger_word": "@zeroclaw-bot"
}
```

**ZeroClaw response:**
```json
{
  "response_type": "comment",
  "channel_id": "channel456",
  "message": "The weather today is sunny with a high of 25°C.",
  "props": {
    "attachments": [...]
  }
}
```

## Troubleshooting

### Common Issues and Solutions

#### `401 Unauthorized` or `403 Forbidden`

**Causes:**
- Invalid bot token
- Insufficient permissions
- Mattermost server unreachable

**Solutions:**

1. **Verify bot token**: Ensure token is correct and not expired
2. **Check permissions**: Bot needs `post:all`, `channel:read`, `user:read`
3. **Test token**:
   ```bash
   curl -H "Authorization: Bearer YOUR_TOKEN" \
     "https://mm.your-domain.com/api/v4/users/me"
   ```
4. **Regenerate token**: If compromised

#### `404 Channel Not Found`

**Causes:**
- Incorrect channel_id
- Bot not in channel
- Channel doesn't exist

**Solutions:**

1. **Verify channel_id**: Double-check the ID
2. **Add bot to channel**: Invite bot to the channel
3. **Check channel access**: Ensure bot has read permissions
4. **List channels**:
   ```bash
   curl -H "Authorization: Bearer YOUR_TOKEN" \
     "https://mm.your-domain.com/api/v4/channels"
   ```

#### No Messages Received

**Causes:**
- Webhook not configured
- Mattermost not sending events
- ZeroClaw not processing events

**Solutions:**

1. **Check webhook configuration**: Verify callback URL
2. **Test webhook**: Use Mattermost's webhook test feature
3. **Enable debug logging**:
   ```bash
   RUST_LOG=debug zeroclaw gateway --host 0.0.0.0 --port 8080
   ```
4. **Check Mattermost logs**: Look for webhook delivery attempts

#### Bot Not Responding

**Causes:**
- Channel ID mismatch
- User not in allowed_users
- Message not mentioning bot (if mention_only=true)
- ZeroClaw agent not running

**Solutions:**

1. **Check allowed_users**: Ensure user is in the list
2. **Verify mention_only**: If true, ensure message mentions bot
3. **Check agent status**:
   ```bash
   zeroclaw status
   zeroclaw agents list
   ```
4. **Review logs**: Look for "Ignored message" entries

### Debugging Commands

```bash
# Test Mattermost API connectivity
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "https://mm.your-domain.com/api/v4/users/me"

# Check webhook delivery (Mattermost admin)
# Go to: System Console > Logs > Webhook Delivery

# View ZeroClaw logs
journalctl -u zeroclaw -f
RUST_LOG=debug zeroclaw gateway --host 0.0.0.0 --port 8080

# Test webhook endpoint manually
curl -X POST http://localhost:8080/mattermost \
  -H "Content-Type: application/json" \
  -d '{"text":"@zeroclaw-bot test"}'
```

## Best Practices

### Channel Organization

**Dedicated Channel:**
```toml
[channels_config.mattermost]
channel_id = "dedicated-channel-id"
allowed_users = ["*"]
```

**Shared Channel (mention-only):**
```toml
[channels_config.mattermost]
mention_only = true
allowed_users = ["alice", "bob", "charlie"]
thread_replies = true
```

### User Management

**Restrict to specific users:**
```toml
allowed_users = [
  "user1-id",
  "user2-id",
  "user3-id"
]
```

**Allow all team members:**
```toml
allowed_users = ["*"]
```

### Performance Optimization

**Reduce model calls:**
```toml
mention_only = true
thread_replies = true
```

**Dedicated channel for high volume:**
```toml
channel_id = "ai-assistant-channel"
allowed_users = ["*"]
```

## Monitoring and Metrics

### Key Metrics to Monitor

- **Message volume**: Messages per hour/day
- **Response times**: Average, p95, p99
- **Error rates**: 4xx, 5xx responses
- **User interactions**: Active users count
- **Thread usage**: Percentage of threaded conversations

### Logging Configuration

```bash
# Enable debug logging for Mattermost integration
RUST_LOG=zeroclaw=info,mattermost=debug zeroclaw gateway

# View specific logs
journalctl -u zeroclaw --grep "mattermost"

# Log to file
zeroclaw gateway > /var/log/zeroclaw/mattermost.log 2>&1
```

## Related Documents

- [[097-setup-guides-nextcloud-talk-setup|nextcloud-talk-setup]] — Nextcloud Talk integration
- [[111-i18n-vi-channels-reference|channels-reference]] — Channels configuration reference
- [[114-i18n-vi-config-reference|config-reference]] — Full configuration schema
- [[143-vi-troubleshooting|troubleshooting]] — Troubleshooting guide
- [[002-setup-guides-readme|setup-guides-readme]] — Setup guides overview

## References

- [Mattermost Documentation](https://docs.mattermost.com/)
- [Mattermost API v4](https://api.mattermost.com/)
- [Mattermost Outgoing Webhooks](https://docs.mattermost.com/developer/webhooks/outgoing-webhooks.html)
- [ZeroClaw Webhook Security](https://github.com/openagen/zeroclaw/blob/main/docs/security/webhook-security.md)
- [ZeroClaw Configuration Guide](https://github.com/openagen/zeroclaw/blob/main/docs/configuration/README.md)
