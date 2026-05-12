---
title: Nextcloud talk setup
authors:
  - ZeroClaw Team
tags:
  - nextcloud-talk
  - zeroclaw
  - webhook-integration
  - api-configuration
  - bot-development
  - hmac-security
  - messaging-integration
  - nextcloud-bot
category: configuration
optimized: true
optimized_at: 2026-05-05T10:00:00Z
word_count: 1166
---
# ZeroClaw Nextcloud Talk Integration Setup

> Native Nextcloud Talk integration for ZeroClaw bot.

## Tóm tắt nhanh

Configure ZeroClaw to receive and respond to Nextcloud Talk bot webhook events with HMAC-SHA256 signature verification.

**Quick setup:**

```toml
[channels_config.nextcloud_talk]
base_url = "https://cloud.example.com"
app_token = "nextcloud-talk-app-token"
webhook_secret = "your-shared-secret"
allowed_users = ["*"]
```

## What This Integration Does

ZeroClaw's Nextcloud Talk integration provides:

- **Inbound webhook endpoint**: `POST /nextcloud-talk` receives Talk bot events
- **HMAC-SHA256 signature verification**: Validates webhook authenticity
- **Outbound messaging**: Sends bot replies back to Talk rooms via Nextcloud OCS API
- **Room-based routing**: Messages stay within the same Talk room
- **Security filtering**: Ignores bot-originated events and non-message events

## Configuration

### Configuration File (config.toml)

Add to `~/.zeroclaw/config.toml`:

```toml
[channels_config.nextcloud_talk]
# Required: Nextcloud base URL
base_url = "https://cloud.example.com"

# Required: Bot app token for OCS API authentication
app_token = "nextcloud-talk-app-token"

# Optional: Shared secret for webhook signature verification
webhook_secret = "your-shared-secret"

# Optional: Allowed users (actor IDs)
# [] = deny all, ["*"] = allow all, ["user1", "user2"] = specific users
allowed_users = ["*"]
```

### Environment Variables

Override configuration with environment variables:

```bash
# Override webhook secret
export ZEROCLAW_NEXTCLOUD_TALK_WEBHOOK_SECRET="your-secret"

# Override base URL
# (Note: Other fields require config file changes)
```

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `base_url` | string | Yes | Nextcloud server base URL (e.g., `https://cloud.example.com`) |
| `app_token` | string | Yes | Bot app token used as `Authorization: Bearer <token>` for OCS API |
| `webhook_secret` | string | No | Shared secret for HMAC-SHA256 signature verification |
| `allowed_users` | array | No | List of allowed Nextcloud actor IDs (`[]` denies all, `["*"]` allows all) |

## Gateway Endpoint

### Start ZeroClaw Gateway

```bash
# Option 1: Run as daemon
zeroclaw daemon

# Option 2: Run gateway with specific host/port
zeroclaw gateway --host 127.0.0.1 --port 3000
zeroclaw gateway --host 0.0.0.0 --port 8080
```

### Configure Webhook URL

Set your Nextcloud Talk bot webhook to:

```
https://<your-public-domain>/nextcloud-talk
```

**Example:**

```
https://chat.yourcompany.com/nextcloud-talk
```

### HTTPS Requirements

- **Production**: Use HTTPS with valid certificate
- **Development**: Use ngrok or similar for public HTTPS endpoint
- **Self-signed certs**: May require additional configuration in Nextcloud

## Signature Verification

### Webhook Security

When `webhook_secret` is configured, ZeroClaw verifies incoming webhook signatures using HMAC-SHA256.

### Required Headers

| Header | Description | Example |
|--------|-------------|---------|
| `X-Nextcloud-Talk-Random` | Random string for signature | `abc123xyz789` |
| `X-Nextcloud-Talk-Signature` | HMAC-SHA256 signature | `hex(hmac_sha256(secret, random + body))` |

### Verification Formula

```
signature = hex(hmac_sha256(webhook_secret, random_string + raw_request_body))
```

### Verification Process

1. Extract `X-Nextcloud-Talk-Random` header
2. Extract `X-Nextcloud-Talk-Signature` header
3. Concatenate: `random + raw_request_body`
4. Compute HMAC-SHA256 using `webhook_secret`
5. Compare hex-encoded result with signature header
6. **If mismatch**: Return `401 Unauthorized`

### Example (Python)

```python
import hmac
import hashlib

secret = b"your-shared-secret"
random = "abc123xyz789"
body = b'{"type":"message","content":"test"}'

# Compute signature
signature = hmac.new(secret, random.encode() + body, hashlib.sha256).hexdigest()

# Expected header value
print(f"X-Nextcloud-Talk-Signature: {signature}")
```

## Message Routing Behavior

### Event Filtering

ZeroClaw processes only relevant events:

✅ **Accepted**:
- User messages (`type: "message"`)
- Room mentions
- Direct messages to bot

❌ **Ignored**:
- Bot-originated events (`actorType: "bots"`)
- System messages (`type: "system"`)
- Non-message events
- Events from non-allowed users

### Reply Routing

- **Room token** extracted from webhook payload
- **Reply sent to same room** where message originated
- **Thread support**: Replies stay in correct thread if applicable

### Actor Identification

- **User ID**: Nextcloud user ID (e.g., `admin`, `user123`)
- **Actor type**: `users`, `guests`, `bots`
- **Display name**: Used for context in responses

## Quick Validation Checklist

### Phase 1: Basic Setup

- [ ] Add `[channels_config.nextcloud_talk]` to config.toml
- [ ] Set `base_url` to your Nextcloud instance
- [ ] Set `app_token` to your bot's app token
- [ ] Set `allowed_users = ["*"]` for testing
- [ ] Start ZeroClaw gateway
- [ ] Configure webhook URL in Nextcloud Talk bot settings

### Phase 2: Test Connection

- [ ] Send a test message in a Talk room
- [ ] Verify ZeroClaw receives the message
- [ ] Check ZeroClaw responds in the same room
- [ ] Review logs for errors

### Phase 3: Security Validation

- [ ] Configure `webhook_secret`
- [ ] Verify signature verification works
- [ ] Test with invalid signature (should get 401)
- [ ] Update `allowed_users` to specific user IDs

### Phase 4: Production Readiness

- [ ] Set up HTTPS with valid certificate
- [ ] Configure firewall rules
- [ ] Set up monitoring and alerts
- [ ] Document the integration

## Troubleshooting

### Common Issues and Solutions

#### `404 Nextcloud Talk not configured`

**Cause**: Missing `[channels_config.nextcloud_talk]` section in config.toml

**Solution**:

```toml
[channels_config.nextcloud_talk]
base_url = "https://your-nextcloud.example.com"
app_token = "your-app-token"
```

#### `401 Invalid signature`

**Causes**:
- Mismatch in `webhook_secret`
- Incorrect random header value
- Body not signed correctly
- Headers not sent by Nextcloud

**Solutions**:

1. **Verify webhook_secret** matches in both systems
2. **Check Nextcloud bot configuration** for correct secret
3. **Test with `allowed_users = ["*"]`** to eliminate permission issues
4. **Enable debug logging** to see raw headers and body

**Debug command:**

```bash
RUST_LOG=debug zeroclaw gateway --host 0.0.0.0 --port 8080
```

#### No reply but webhook returns 200

**Causes**:
- Event filtered (bot/system/non-allowed user)
- Non-message payload
- ZeroClaw not processing the event
- Network issue between systems

**Solutions**:

1. **Check event type**: Ensure it's a message event
2. **Verify actor type**: Not from a bot
3. **Check allowed_users**: User must be in the list
4. **Review logs**: Look for "Ignored event" messages

**Expected log entries:**

```
INFO Processing Nextcloud Talk webhook
DEBUG Event type: message, actorType: users
DEBUG Sending reply to room: abc123
```

#### Connection refused or timeout

**Causes**:
- ZeroClaw gateway not running
- Wrong host/port configuration
- Firewall blocking traffic
- HTTPS certificate issues

**Solutions**:

1. **Verify gateway is running:**
   ```bash
   ps aux | grep zeroclaw
   curl http://localhost:3000/health
   ```

2. **Check host/port:**
   ```bash
   zeroclaw gateway --host 0.0.0.0 --port 8080
   ```

3. **Test connectivity:**
   ```bash
   curl -v https://your-domain/nextcloud-talk
   ```

4. **Check firewall:**
   ```bash
   sudo ufw status
   sudo netstat -tulnp | grep 8080
   ```

### Debugging Commands

```bash
# Check gateway status
curl -v http://localhost:3000/health

# Test webhook endpoint manually
curl -X POST http://localhost:3000/nextcloud-talk \
  -H "Content-Type: application/json" \
  -H "X-Nextcloud-Talk-Random: test123" \
  -H "X-Nextcloud-Talk-Signature: expected-signature" \
  -d '{"type":"message","content":"test"}'

# View logs
journalctl -u zeroclaw -f
RUST_LOG=debug zeroclaw gateway --host 0.0.0.0 --port 8080
```

## Security Best Practices

### Webhook Secret Management

- **Use strong secrets**: 32+ character random strings
- **Rotate regularly**: Every 90 days
- **Store securely**: Use environment variables or secret management
- **Never commit to version control**

**Example secret generation:**

```bash
openssl rand -hex 32
```

### App Token Security

- **Use dedicated bot account**: Don't use admin account
- **Limit permissions**: Bot only needs Talk permissions
- **Rotate tokens**: When compromised or periodically
- **Store encrypted**: At rest and in transit

### Network Security

- **HTTPS only**: Never use HTTP in production
- **Rate limiting**: Implement at gateway level
- **IP allowlisting**: Restrict webhook sources
- **Monitor traffic**: Watch for unusual patterns

## Nextcloud Configuration

### Creating a Talk Bot

1. **Log in to Nextcloud** as admin
2. **Go to Talk settings** → Bots
3. **Create new bot:**
   - Name: ZeroClaw
   - Description: AI assistant
   - Webhook URL: `https://your-domain/nextcloud-talk`
   - Secret: Generate and configure in ZeroClaw
4. **Save bot** and note the app token

### Bot Permissions

Ensure bot has appropriate permissions:

- **Talk permissions**: Send/receive messages
- **Room access**: Access rooms where bot should operate
- **User mentions**: Allow @mentions of bot

### Testing in Nextcloud

1. **Start a conversation** with the bot
2. **Send a test message**
3. **Verify bot responds** in the same conversation
4. **Check bot logs** for errors

## Advanced Configuration

### Multiple Rooms

ZeroClaw automatically routes messages based on room token. No additional configuration needed for multiple rooms.

### User-Specific Settings

Use `allowed_users` to restrict which users can interact with the bot:

```toml
[channels_config.nextcloud_talk]
allowed_users = ["admin", "alice", "bob"]
```

### Custom Headers

For advanced integrations, you can add custom headers to OCS API requests:

```toml
[channels_config.nextcloud_talk]
custom_headers = {
  "X-Custom-Header" = "value"
}
```

### Rate Limiting

Configure rate limits for bot responses:

```toml
[channels_config.nextcloud_talk]
rate_limit = "10 per minute"
```

## Monitoring and Metrics

### Key Metrics to Monitor

- **Webhook requests**: Total, success, failure rates
- **Response times**: Average, p95, p99
- **Error rates**: 4xx, 5xx responses
- **Message volume**: Messages per hour/day
- **Signature verification failures**

### Logging Configuration

```bash
# Enable debug logging
RUST_LOG=zeroclaw=debug,nextcloud_talk=debug zeroclaw gateway

# View specific logs
journalctl -u zeroclaw --grep "nextcloud-talk"

# Log to file
zeroclaw gateway > /var/log/zeroclaw/nextcloud-talk.log 2>&1
```

## Related Documents

- [[099-vi-mattermost-setup|mattermost-setup]] — Mattermost integration guide
- [[111-i18n-vi-channels-reference|channels-reference]] — Channels configuration reference
- [[114-i18n-vi-config-reference|config-reference]] — Full configuration schema
- [[143-vi-troubleshooting|troubleshooting]] — Troubleshooting guide
- [[002-setup-guides-readme|setup-guides-readme]] — Setup guides overview

## References

- [Nextcloud Talk Documentation](https://nextcloud-talk.readthedocs.io/)
- [Nextcloud OCS API](https://docs.nextcloud.com/server/latest/developer_manual/client_apis/OCS/ocs-api-overview.html)
- [HMAC Specification (RFC 2104)](https://datatracker.ietf.org/doc/html/rfc2104)
- [ZeroClaw Webhook Security](https://github.com/openagen/zeroclaw/blob/main/docs/security/webhook-security.md)
- [ZeroClaw Configuration Guide](https://github.com/openagen/zeroclaw/blob/main/docs/configuration/README.md)
