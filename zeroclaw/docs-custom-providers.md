---
title: Custom providers
url: https://github.com/zeroclaw-labs/zeroclaw/blob/main/docs/custom-providers.md
source: git
fetched_at: 2026-02-18T07:18:19.283979-03:00
rendered_js: false
word_count: 238
summary: This document explains how to configure ZeroClaw to use custom OpenAI and Anthropic-compatible API endpoints through configuration files and environment variables. It includes instructions for setting provider types, testing the setup, and troubleshooting common connection issues.
tags:
    - zeroclaw
    - api-configuration
    - custom-providers
    - openai-compatible
    - anthropic-compatible
    - troubleshooting
    - llm-integration
category: configuration
---

# Custom Provider Configuration

ZeroClaw supports custom API endpoints for both OpenAI-compatible and Anthropic-compatible providers.

## Provider Types

### OpenAI-Compatible Endpoints (`custom:`)

For services that implement the OpenAI API format:

```toml
default_provider = "custom:https://your-api.com"
api_key = "your-api-key"
default_model = "your-model-name"
```

### Anthropic-Compatible Endpoints (`anthropic-custom:`)

For services that implement the Anthropic API format:

```toml
default_provider = "anthropic-custom:https://your-api.com"
api_key = "your-api-key"
default_model = "your-model-name"
```

## Configuration Methods

### Config File

Edit `~/.zeroclaw/config.toml`:

```toml
api_key = "your-api-key"
default_provider = "anthropic-custom:https://api.example.com"
default_model = "claude-sonnet-4-6"
```

### Environment Variables

For `custom:` and `anthropic-custom:` providers, use the generic key env vars:

```bash
export API_KEY="your-api-key"
# or: export ZEROCLAW_API_KEY="your-api-key"
zeroclaw agent
```

## Testing Configuration

Verify your custom endpoint:

```bash
# Interactive mode
zeroclaw agent

# Single message test
zeroclaw agent -m "test message"
```

## Troubleshooting

### Authentication Errors

- Verify API key is correct
- Check endpoint URL format (must include `http://` or `https://`)
- Ensure endpoint is accessible from your network

### Model Not Found

- Confirm model name matches provider's available models
- Check provider documentation for exact model identifiers

### Connection Issues

- Test endpoint accessibility: `curl -I https://your-api.com`
- Verify firewall/proxy settings
- Check provider status page

## Examples

### Local LLM Server

```toml
default_provider = "custom:http://localhost:8080"
default_model = "local-model"
```

### Corporate Proxy

```toml
default_provider = "anthropic-custom:https://llm-proxy.corp.example.com"
api_key = "internal-token"
```

### Cloud Provider Gateway

```toml
default_provider = "custom:https://gateway.cloud-provider.com/v1"
api_key = "gateway-api-key"
default_model = "gpt-4"
```
