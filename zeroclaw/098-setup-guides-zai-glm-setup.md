---
title: Zai glm setup
authors:
  - ZeroClaw Team
tags:
  - zeroclaw
  - z-ai
  - glm-setup
  - api-configuration
  - llm-integration
  - openai-compatible
  - ai-provider
  - model-configuration
category: configuration
optimized: true
optimized_at: 2026-05-05T10:00:00Z
word_count: 875
---
# ZeroClaw Z.AI GLM Provider Setup Guide

> ZeroClaw supports Z.AI's GLM models through OpenAI-compatible endpoints.

## Quick Start

Configure ZeroClaw to use Z.AI GLM models in 2 minutes:

```bash
zeroclaw onboard \
  --provider "zai" \
  --api-key "YOUR_ZAI_API_KEY"
```

## Overview

ZeroClaw provides built-in support for Z.AI GLM models with OpenAI-compatible endpoints:

| Provider Alias | Endpoint | Region | Status |
|----------------|----------|--------|--------|
| `zai` | `https://api.z.ai/api/coding/paas/v4` | Global | ✅ Recommended |
| `zai-cn` | `https://open.bigmodel.cn/api/paas/v4` | China | ✅ Available |

> **Note**: For custom base URLs, see [[151-contributing-custom-providers|custom-providers]].

## Available Models

ZeroClaw supports these Z.AI GLM models:

| Model ID | Description | Use Case | Default |
|----------|-------------|----------|---------|
| `glm-5` | Strongest reasoning capabilities | Complex tasks, production | ✅ |
| `glm-4.7` | High-quality general-purpose model | Balanced performance | ❌ |
| `glm-4.6` | Basic balanced model | Cost-effective | ❌ |
| `glm-4.5-air` | Lower latency option | Fast responses | ❌ |

> **Important**: Model availability varies by account and region. Use the `/models` API to check available models in your account.

## Configuration

### Method 1: Quick Onboarding (Recommended)

```bash
# Global endpoint (recommended for most users)
zeroclaw onboard \
  --provider "zai" \
  --api-key "YOUR_ZAI_API_KEY"

# China endpoint (for users in China)
zeroclaw onboard \
  --provider "zai-cn" \
  --api-key "YOUR_ZAI_API_KEY"
```

### Method 2: Manual Configuration

Edit `~/.zeroclaw/config.toml`:

```toml
# Provider configuration
[providers.zai]
enabled = true
api_key = "YOUR_ZAI_API_KEY"
default_model = "glm-5"
default_temperature = 0.7
base_url = "https://api.z.ai/api/coding/paas/v4"

# Default agent configuration
[agents.default]
provider = "zai"
model = "glm-5"

# Set default provider
[providers.default]
provider = "zai"
```

### Method 3: Environment Variables

Add to your `.env` file:

```bash
# Primary Z.AI API Key (recommended)
ZAI_API_KEY=your-id.secret

# Generic fallback (used by many providers)
API_KEY=your-id.secret
```

> **Key format**: `id.secret` (e.g., `abc123.xyz789`)

## Verification

### Test with curl

Verify your API key and endpoint:

```bash
# Test OpenAI-compatible endpoint
curl -X POST "https://api.z.ai/api/coding/paas/v4/chat/completions" \
  -H "Authorization: Bearer YOUR_ZAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-5",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

**Expected successful response:**

```json
{
  "object": "chat.completion",
  "model": "glm-5",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "Hello! How can I help you today?"
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 12,
    "total_tokens": 22
  }
}
```

### Test with ZeroClaw CLI

```bash
# Test agent directly
echo "Hello from ZeroClaw!" | zeroclaw agent

# Check provider status
zeroclaw providers list
zeroclaw providers status zai

# Test specific model
zeroclaw chat --model glm-5 --message "What is Rust programming language?"

# Check configuration
zeroclaw config show
```

## Advanced Configuration

### Multiple Providers

Configure both global and China endpoints:

```toml
[providers.zai]
enabled = true
api_key = "${ZAI_API_KEY}"
default_model = "glm-5"
base_url = "https://api.z.ai/api/coding/paas/v4"

[providers.zai-cn]
enabled = true
api_key = "${ZAI_CN_API_KEY}"
default_model = "glm-4.7"
base_url = "https://open.bigmodel.cn/api/paas/v4"

# Use different models for different agents
[agents.default]
provider = "zai"
model = "glm-5"

[agents.china]
provider = "zai-cn"
model = "glm-4.7"
```

### Provider-Specific Settings

```toml
[providers.zai]
api_key = "YOUR_API_KEY"
base_url = "https://api.z.ai/api/coding/paas/v4"
default_model = "glm-5"

# Model parameters
max_tokens = 4096
temperature = 0.7
top_p = 0.9
frequency_penalty = 0.1
presence_penalty = 0.1

# Retry configuration
max_retries = 3
retry_delay_ms = 1000

# Timeout settings
request_timeout_sec = 30
connect_timeout_sec = 10
```

## Troubleshooting

### Rate Limiting Errors

**Symptoms:**
- `rate_limited` errors in logs
- Slow responses
- Requests being rejected with 429 status

**Solutions:**

1. **Wait and retry**: Rate limits reset periodically
2. **Check your Z.AI plan**: Upgrade if needed
3. **Use lower-latency model**: Switch to `glm-4.5-air`
4. **Reduce request frequency**: Implement exponential backoff
5. **Monitor usage**: Check Z.AI dashboard for usage metrics

**Configuration example:**

```toml
[providers.zai]
max_retries = 5
retry_delay_ms = 2000
```

### Authentication Errors (401/403)

**Symptoms:**
- `401 Unauthorized` errors
- `403 Forbidden` errors
- "Invalid API key" messages

**Solutions:**

1. **Verify API key format**: Must be `id.secret` (e.g., `abc123.xyz789`)
2. **Check for whitespace**: Ensure no spaces or newlines in key
3. **Verify key hasn't expired**: Regenerate if needed
4. **Check key permissions**: Ensure key has coding/model access
5. **Test authentication directly:**

```bash
curl -I "https://api.z.ai/api/coding/paas/v4/models" \
  -H "Authorization: Bearer YOUR_ZAI_API_KEY"
```

### Model Not Found Errors

**Symptoms:**
- "Model not found" errors
- Model appears unavailable in your account
- 404 responses for specific models

**Solutions:**

1. **List available models:**

```bash
curl -s "https://api.z.ai/api/coding/paas/v4/models" \
  -H "Authorization: Bearer YOUR_ZAI_API_KEY" | jq '.data[].id'
```

2. **Check your plan**: Some models require specific subscription tiers
3. **Use fallback model**: Switch to `glm-4.6` or `glm-4.5-air`
4. **Verify region**: Ensure you're using correct endpoint for your region

### Connection Issues

**Symptoms:**
- Connection timeouts
- DNS resolution failures
- SSL certificate errors
- Unable to reach Z.AI endpoints

**Solutions:**

1. **Check network connectivity:**

```bash
ping api.z.ai
curl -v https://api.z.ai
nslookup api.z.ai
```

2. **Verify SSL certificates**: Ensure your system trusts Z.AI certificates
3. **Check firewall/proxy**: Ensure outbound HTTPS (port 443) is allowed
4. **Test with different region**: Try `zai-cn` endpoint if global has issues
5. **Check DNS resolution**: Ensure DNS servers can resolve Z.AI domains

## Getting API Keys

### Step-by-Step Guide

1. **Visit Z.AI website:**

   [https://z.ai](https://z.ai)

2. **Sign up for Coding Plan:**

   - Choose "Coding Plan" or appropriate tier
   - Complete registration and email verification

3. **Access API Dashboard:**

   - Log in to your account
   - Navigate to "API Keys" or "Developer" section
   - Click "Create API Key" or "Generate New Key"

4. **Copy your API key:**

   - Format: `id.secret` (e.g., `abc123.xyz789`)
   - **Store securely**: Treat as password
   - **Never commit to version control**

5. **Configure ZeroClaw:**

   ```bash
   zeroclaw onboard --provider zai --api-key YOUR_API_KEY
   ```

## Best Practices

### Security

- **Use environment variables** for API keys:
  ```bash
  export ZAI_API_KEY="your-id.secret"
  ```

- **Rotate keys regularly**: Every 90 days or when compromised

- **Use different keys** for different environments:
  - Development key
  - Staging key
  - Production key

- **Restrict key permissions**: Use Z.AI dashboard to limit key scope

- **Monitor key usage**: Set up alerts for unusual activity

### Performance

- **Choose appropriate model**:
  - `glm-5`: Use for complex reasoning tasks
  - `glm-4.7`: Balanced performance
  - `glm-4.6`: Cost-effective for simple tasks
  - `glm-4.5-air`: Fast responses, higher quota tolerance

- **Set temperature wisely**:
  - `0.0-0.3`: Deterministic, reproducible outputs
  - `0.3-0.7`: Balanced creativity
  - `0.7-1.0`: Creative, exploratory outputs

- **Use max_tokens** to limit response length and costs

### Cost Optimization

- **Cache responses** for repeated queries
- **Batch requests** where possible
- **Monitor usage** via Z.AI dashboard
- **Set up billing alerts** in Z.AI account
- **Use lower-cost models** for simple tasks

## Configuration Examples

### Minimal Configuration

```toml
[providers.zai]
enabled = true
api_key = "YOUR_API_KEY"
```

### Production Configuration

```toml
[providers.zai]
enabled = true
api_key = "${ZAI_API_KEY}"  # From environment variable
default_model = "glm-5"
base_url = "https://api.z.ai/api/coding/paas/v4"
max_tokens = 4096
temperature = 0.7
max_retries = 3
retry_delay_ms = 1000

[agents.default]
provider = "zai"
model = "glm-5"
```

### Development Configuration

```toml
[providers.zai]
enabled = true
api_key = "dev-key.secret"
default_model = "glm-4.5-air"  # Lower latency for dev
temperature = 0.5

[providers.zai-cn]
enabled = true
api_key = "china-dev-key.secret"
base_url = "https://open.bigmodel.cn/api/paas/v4"
```

## Model Comparison

| Model | Reasoning | Creativity | Cost | Latency | Best For |
|-------|-----------|------------|------|---------|----------|
| `glm-5` | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | High | Medium | Production, complex tasks |
| `glm-4.7` | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Medium | Medium | General purpose |
| `glm-4.6` | ⭐⭐⭐ | ⭐⭐⭐ | Low | Low | Simple tasks, cost-sensitive |
| `glm-4.5-air` | ⭐⭐ | ⭐⭐ | Low | Very Low | Fast responses, high volume |

## Related Documents

- [[096-i18n-vi-zai-glm-setup|zai-glm-setup-vi]] — Vietnamese setup guide
- [[100-vi-zai-glm-setup|zai-glm-setup-vi-alt]] — Alternative Vietnamese guide
- [[151-contributing-custom-providers|custom-providers]] — Custom provider configuration
- [[118-i18n-vi-providers-reference|providers-reference]] — Provider configuration reference
- [[114-i18n-vi-config-reference|config-reference]] — Full configuration schema
- [[002-setup-guides-readme|setup-guides-readme]] — Setup guides overview

## References

- [Z.AI Official Website](https://z.ai)
- [Z.AI API Documentation](https://z.ai/docs)
- [OpenAI API Compatibility](https://platform.openai.com/docs/api-reference)
- [ZeroClaw Provider System](https://github.com/openagen/zeroclaw/blob/main/docs/providers/README.md)
- [GLM Model Documentation](https://github.com/THUDM/GLM)
