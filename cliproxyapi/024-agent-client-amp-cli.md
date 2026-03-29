---
title: Amp CLI | CLIProxyAPI
url: https://help.router-for.me/agent-client/amp-cli
source: crawler
fetched_at: 2026-01-14T22:10:01.990535475-03:00
rendered_js: false
word_count: 1373
summary: This document explains how to integrate Amp CLI and IDE extensions with CLIProxyAPI, allowing you to use your existing AI provider subscriptions (like Google, ChatGPT, and Claude) through a single proxy server. It details configuration, authentication, and security settings for managing AI model requests.
tags:
    - ampt-cli
    - ide-extensions
    - cliproxyapi
    - oauth
    - ai-providers
    - configuration
    - security
category: guide
---

This guide explains how to use CLIProxyAPI with Amp CLI and Amp IDE extensions, enabling you to use your existing Google/ChatGPT/Claude subscriptions (via OAuth) with Amp's CLI.

## Overview [​](#overview)

The Amp CLI integration adds specialized routing to support Amp's API patterns while maintaining full compatibility with all existing CLIProxyAPI features. This allows you to use both traditional CLIProxyAPI features and Amp CLI with the same proxy server.

### Key Features [​](#key-features)

- **Provider route aliases**: Maps Amp's `/api/provider/{provider}/v1...` patterns to CLIProxyAPI handlers
- **Management proxy**: Forwards account management requests to Amp's control plane using a secure upstream API key.
- **Smart fallback**: Automatically routes unconfigured models to ampcode.com
- **Security-first**: Management routes require API key auth (optional localhost restriction)
- **Automatic gzip handling**: Decompresses responses from Amp upstream

### What You Can Do [​](#what-you-can-do)

- Use Amp CLI with your Google account (Gemini 3 Pro Preview, Gemini 2.5 Pro, Gemini 2.5 Flash)
- Use Amp CLI with your ChatGPT Plus/Pro subscription (GPT-5, GPT-5 Codex models)
- Use Amp CLI with your Claude Pro/Max subscription (Claude Sonnet 4.5, Opus 4.1)
- Use Amp IDE extensions (VS Code, Cursor, Windsurf, etc.) with the same proxy
- Run multiple CLI tools (Factory + Amp) through one proxy server
- Route unconfigured models automatically through ampcode.com

### Which Providers Should You Authenticate? [​](#which-providers-should-you-authenticate)

**Important**: The providers you need to authenticate depend on which models and features your installed version of Amp currently uses. Amp employs different providers for various agent modes and specialized subagents:

- **Smart mode**: Uses Google/Gemini models (Gemini 3 Pro)
- **Rush mode**: Uses Anthropic/Claude models (Claude Haiku 4.5)
- **Oracle subagent**: Uses OpenAI/GPT models (GPT-5 medium reasoning)
- **Librarian subagent**: Uses Anthropic/Claude models (Claude Sonnet 4.5)
- **Search subagent**: Uses Anthropic/Claude models (Claude Haiku 4.5)
- **Review feature**: Uses Google/Gemini models (Gemini 2.5 Flash-Lite)

For the most current information about which models Amp uses, see the [**Amp Models Documentation**](https://ampcode.com/models).

#### Fallback Behavior [​](#fallback-behavior)

CLIProxyAPI uses a smart fallback system:

1. **Provider authenticated locally** (`--login`, `--codex-login`, `--claude-login`):
   
   - Requests use **your OAuth subscription** (ChatGPT Plus/Pro, Claude Pro/Max, Google account)
   - You benefit from your subscription's included usage quotas
   - No Amp credits consumed
2. **Provider NOT authenticated locally**:
   
   - Requests automatically forward to **ampcode.com**
   - Uses Amp's backend provider connections
   - **Requires Amp credits** if the provider is paid (OpenAI, Anthropic paid tiers)
   - May result in errors if Amp credit balance is insufficient

**Recommendation**: Authenticate all providers you have subscriptions for to maximize value and minimize Amp credit usage. If you don't have subscriptions to all providers Amp uses, ensure you have sufficient Amp credits available for fallback requests.

## Architecture [​](#architecture)

### Request Flow [​](#request-flow)

```
Amp CLI/IDE
  ↓
  ├─ Provider API requests (/api/provider/{provider}/v1/...)
  │   ↓
  │   ├─ Model configured locally?
  │   │   YES → Use local OAuth tokens (OpenAI/Claude/Gemini handlers)
  │   │   NO  → Forward to ampcode.com (reverse proxy)
  │   ↓
  │   Response
  │
  └─ Management requests (/api/auth, /api/user, /api/threads, ...)
      ↓
      ├─ Authenticate with CLIProxyAPI's `api-keys`
      ↓
      ├─ Optional localhost restriction
      ↓
      └─ Reverse proxy to ampcode.com (using `upstream-api-key`)
          ↓
          Response (auto-decompressed if gzipped)
```

### Components [​](#components)

The Amp integration is implemented as a modular routing module (`internal/api/modules/amp/`) with these components:

1. **Route Aliases** (`routes.go`): Maps Amp-style paths to standard handlers
2. **Reverse Proxy** (`proxy.go`): Forwards management requests to ampcode.com
3. **Fallback Handler** (`fallback_handlers.go`): Routes unconfigured models to ampcode.com
4. **Secret Management** (`secret.go`): Multi-source API key resolution with caching
5. **Main Module** (`amp.go`): Orchestrates registration and configuration

## Configuration [​](#configuration)

### Basic Configuration [​](#basic-configuration)

Add the `ampcode` block to your `config.yaml` (as of v6.5.37, legacy `amp-upstream-*` keys are auto-migrated and rewritten to this structure on load):

yaml

```
# API keys for clients (e.g., Amp CLI, VS Code) to authenticate with CLIProxyAPI
api-keys:
  - "your-client-secret-key" # Example key for your clients

ampcode:
  # Amp upstream control plane (required for management routes)
  upstream-url: "https://ampcode.com"
  # API key for CLIProxyAPI to authenticate with ampcode.com
  # Get this from https://ampcode.com/settings
  upstream-api-key: "your-ampcode-api-key-goes-here"
  # Optional: restrict management routes to localhost (default: false)
  restrict-management-to-localhost: false
  # Optional: map missing Amp models to local ones
  # model-mappings:
  #   - from: "claude-opus-4.5"
  #     to: "claude-sonnet-4"
```

### Security Settings [​](#security-settings)

#### API Key Auth for Management Routes [​](#api-key-auth-for-management-routes)

As of v6.6.15, Amp management routes (`/api/auth`, `/api/user`, `/api/threads`, `/threads`, etc.) are protected by CLIProxyAPI's standard API key authentication middleware.

- If you configure `api-keys` in `config.yaml` (recommended), these routes require a valid API key in the request (`Authorization: Bearer <key>` or `X-Api-Key: <key>`), otherwise they return `401 Unauthorized`.
- After local authentication succeeds, the proxy strips the client's `Authorization`/`X-Api-Key` and uses `ampcode.upstream-api-key` to call the upstream ampcode.com service.

#### `ampcode.restrict-management-to-localhost` [​](#ampcode-restrict-management-to-localhost)

**Default: `false`**

When enabled, management routes (`/api/auth`, `/api/user`, `/api/threads`, etc.) only accept connections from localhost (127.0.0.1, ::1). This prevents:

- Drive-by browser attacks
- Remote access to management endpoints
- CORS-based attacks
- Header spoofing attacks (e.g., `X-Forwarded-For: 127.0.0.1`)

#### How It Works [​](#how-it-works)

This restriction uses the **actual TCP connection address** (`RemoteAddr`), not HTTP headers like `X-Forwarded-For`. This prevents header spoofing attacks but has important implications:

- ✅ **Works for direct connections**: Running CLIProxyAPI directly on your machine or server
- ⚠️ **May not work behind reverse proxies**: If deploying behind nginx, Cloudflare, or other proxies, the connection will appear to come from the proxy's IP, not localhost

#### Reverse Proxy Deployments [​](#reverse-proxy-deployments)

If you need to run CLIProxyAPI behind a reverse proxy (nginx, Caddy, Cloudflare Tunnel, etc.):

1. **Keep the localhost restriction disabled (default)**:
   
   yaml
   
   ```
   ampcode:
     restrict-management-to-localhost: false
   ```
2. **Ensure API key auth is enabled** (recommended):
   
   - Configure `api-keys` in `config.yaml` and have clients send the key
   - Combine with firewall/VPN/zero-trust controls to reduce exposure
3. **Example nginx configuration** (blocks external access to management routes):
   
   nginx
   
   ```
   location /api/auth { deny all; }
   location /api/user { deny all; }
   location /api/threads { deny all; }
   location /api/internal { deny all; }
   ```

**Note**: `ampcode.restrict-management-to-localhost` is an extra hardening option; behind reverse proxies it is typically kept `false`.

## Setup [​](#setup)

### 1. Configure CLIProxyAPI [​](#_1-configure-cliproxyapi)

Create or edit `config.yaml`. You will need two types of API keys:

1. `api-keys`: For clients like Amp CLI to connect to your CLIProxyAPI instance.
2. `ampcode.upstream-api-key`: For CLIProxyAPI to connect to the `ampcode.com` backend. Get this from [**https://ampcode.com/settings**](https://ampcode.com/settings).

yaml

```
port: 8317
auth-dir: "~/.cli-proxy-api"

# API keys for clients (e.g., Amp CLI) to use
api-keys:
  - "your-client-secret-key" # You can change this secret

# Amp integration
ampcode:
  upstream-url: "https://ampcode.com"
  # Your personal API key from ampcode.com
  upstream-api-key: "paste-your-ampcode-api-key-here"
  restrict-management-to-localhost: false

# Other standard settings...
debug: false
logging-to-file: true
```

### 2. Authenticate with Providers [​](#_2-authenticate-with-providers)

Run OAuth login for the providers you want to use:

**Google Account (Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 3 Pro Preview):**

bash

```
./cli-proxy-api --login
```

**ChatGPT Plus/Pro (GPT-5, GPT-5 Codex):**

bash

```
./cli-proxy-api --codex-login
```

**Claude Pro/Max (Claude Sonnet 4.5, Opus 4.1):**

bash

```
./cli-proxy-api --claude-login
```

Tokens are saved to:

- Gemini: `~/.cli-proxy-api/gemini-<email>.json`
- OpenAI Codex: `~/.cli-proxy-api/codex-<email>.json`
- Claude: `~/.cli-proxy-api/claude-<email>.json`

### 3. Start the Proxy [​](#_3-start-the-proxy)

bash

```
./cli-proxy-api --config config.yaml
```

### 4. Configure Amp CLI [​](#_4-configure-amp-cli)

#### Option A: Settings File [​](#option-a-settings-file)

Amp CLI uses two configuration files:

1. **Settings file**: `~/.config/amp/settings.json` - General settings
2. **Secrets file**: `~/.local/share/amp/secrets.json` - Sensitive credentials (API keys)

Edit `~/.config/amp/settings.json` for the URL:

json

```
{
  "amp.url": "http://localhost:8317"
}
```

Edit `~/.local/share/amp/secrets.json` for the API key:

json

```
{
  "apiKey@http://localhost:8317": "your-client-secret-key"
}
```

#### Option B: Environment Variable [​](#option-b-environment-variable)

bash

```
export AMP_URL=http://localhost:8317
export AMP_API_KEY=your-client-secret-key
```

With this configuration, the `amp login` command is no longer necessary.

### 5. Use Amp [​](#_5-use-amp)

You are now ready to use Amp. All requests will be routed through your proxy.

bash

```
amp "Write a hello world program in Python"
```

### 6. (Optional) Configure Amp IDE Extension [​](#_6-optional-configure-amp-ide-extension)

The proxy also works with Amp IDE extensions for VS Code, Cursor, Windsurf, etc.

1. Open Amp extension settings in your IDE.
2. Set **Amp URL** to `http://localhost:8317`.
3. Set **Amp API Key** to the key you configured (e.g., `your-client-secret-key`).
4. Start using Amp in your IDE. Both CLI and IDE can use the proxy simultaneously.

## Usage [​](#usage)

### Supported Routes [​](#supported-routes)

#### Provider Aliases (Always Available) [​](#provider-aliases-always-available)

These routes work even without `ampcode.upstream-url` configured:

- `/api/provider/openai/v1/chat/completions`
- `/api/provider/openai/v1/responses`
- `/api/provider/anthropic/v1/messages`
- `/api/provider/google/v1beta/models/:action`

Amp CLI calls these routes with your OAuth-authenticated models configured in CLIProxyAPI.

#### Management Routes (Require `ampcode.upstream-url`) [​](#management-routes-require-ampcode-upstream-url)

These routes are proxied to ampcode.com:

- `/api/auth` - Authentication
- `/api/user` - User profile
- `/api/meta` - Metadata
- `/api/threads` - Conversation threads
- `/api/telemetry` - Usage telemetry
- `/api/internal` - Internal APIs

**Security**: Requires an API key; `ampcode.restrict-management-to-localhost` is optional (default: false).

### Model Fallback Behavior [​](#model-fallback-behavior)

When Amp requests a model:

1. **Check local configuration**: Does CLIProxyAPI have OAuth tokens for this model's provider?
2. **If YES**: Route to local handler (use your OAuth subscription)
3. **If NO**: Forward to ampcode.com (use Amp's default routing)

This enables seamless mixed usage:

- Models you've configured (Gemini, ChatGPT, Claude) → Your OAuth subscriptions
- Models you haven't configured → Amp's default providers

### Example API Calls [​](#example-api-calls)

**Chat completion with local OAuth:**

bash

```
curl http://localhost:8317/api/provider/openai/v1/chat/completions \
  -H "Authorization: Bearer <your-cli-proxy-api-key>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

**Management endpoint (requires API key):**

bash

```
curl http://localhost:8317/api/user \
  -H "Authorization: Bearer <your-cli-proxy-api-key>"
```

## Troubleshooting [​](#troubleshooting)

### Common Issues [​](#common-issues)

SymptomLikely CauseFix404 on `/api/provider/...`Incorrect route pathEnsure exact path: `/api/provider/{provider}/v1...`401 on `/api/user`Missing/invalid API keyConfigure `api-keys` and send `Authorization: Bearer <key>` or `X-Api-Key: <key>`403 on `/api/user`Localhost restriction enabled and request is remoteRun from the same machine or set `ampcode.restrict-management-to-localhost` to `false`401/403 from providerMissing/expired OAuthRe-run `--codex-login` or `--claude-login`Amp gzip errorsResponse decompression issueUpdate to latest build; auto-decompression should handle thisModels not using proxyWrong Amp URLVerify `amp.url` setting or `AMP_URL` environment variableCORS errorsProtected management endpointUse CLI/terminal, not browser

### Diagnostics [​](#diagnostics)

**Check proxy logs:**

bash

```
# If logging-to-file: true
tail -f logs/requests.log

# If running in tmux
tmux attach-session -t proxy
```

**Enable debug mode** (temporarily):

**Test basic connectivity:**

bash

```
# Check if proxy is running
curl http://localhost:8317/v1/models

# Check Amp-specific route
curl http://localhost:8317/api/provider/openai/v1/models
```

**Verify Amp configuration:**

bash

```
# Check if Amp is using proxy
amp config get amp.url

# Or check environment
echo $AMP_URL
```

### Security Checklist [​](#security-checklist)

- ✅ Configure and protect `api-keys` (management routes require an API key)
- ✅ Enable `ampcode.restrict-management-to-localhost: true` for extra hardening when possible (default: false)
- ✅ Don't expose proxy publicly (bind to localhost or use firewall/VPN)
- ✅ Securely store your `ampcode.upstream-api-key` in the config file.
- ✅ Rotate OAuth tokens periodically by re-running login commands
- ✅ Store config and auth-dir on encrypted disk if handling sensitive data
- ✅ Keep proxy binary up to date for security fixes

## Additional Resources [​](#additional-resources)

- [Amp CLI Official Manual](https://ampcode.com/manual)