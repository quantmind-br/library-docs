---
title: Authentication
url: https://developers.openai.com/codex/auth.md
source: llms
fetched_at: 2026-04-30T10:15:12.887123692-03:00
rendered_js: false
word_count: 684
summary: This document details the authentication methods, security configurations, and credential management options available for accessing Codex tools and services.
tags:
    - authentication
    - api-keys
    - security
    - multi-factor-authentication
    - cli-configuration
    - credential-storage
    - headless-authentication
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Authentication

## OpenAI authentication

Codex supports two sign-in methods for OpenAI models:

| Method | Best for | Notes |
|--------|----------|-------|
| **ChatGPT** | Subscription access | Follows ChatGPT workspace permissions, RBAC, retention, and residency settings |
| **API key** | Usage-based access | Follows API organization retention and data-sharing settings. Recommended for CI/CD workflows |

Codex cloud requires ChatGPT sign-in. CLI and IDE extension support both.

API key usage is billed through your OpenAI Platform account at standard API rates. See [API pricing](https://openai.com/api/pricing/).

> [!note]
> ChatGPT-credit features such as [[062-speed|fast mode]] are only available with ChatGPT sign-in.

### Sign in with ChatGPT

Opens a browser window to complete login. After sign-in, the browser returns an access token to the CLI or IDE extension.

### Sign in with an API key

Get your key from the [OpenAI dashboard](https://platform.openai.com/api-keys). Don't expose Codex execution in untrusted or public environments.

## Secure your Codex cloud account

Codex cloud interacts directly with your codebase. Enable MFA.

- Social login (Google, Microsoft, Apple): MFA not required on ChatGPT, but you can set it up with your provider.
- SSO: Your organization's SSO admin should enforce MFA.
- Email + password: MFA required before accessing Codex cloud.
- Mixed login methods including email + password: MFA required even if you sign in another way.

Setup guides: [Google](https://support.google.com/accounts/answer/185839), [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661), [Apple](https://support.apple.com/en-us/102660)

## Login caching

Codex caches login details locally and reuses them across CLI and extension restarts. Log out from either and you'll need to sign in again next time.

Cache location: `~/.codex/auth.json` (plaintext) or your OS credential store.

ChatGPT sessions refresh tokens automatically before expiration.

## Credential storage

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"
```

| Value | Behavior |
|-------|----------|
| `file` | `auth.json` under `CODEX_HOME` (default `~/.codex`) |
| `keyring` | OS credential store |
| `auto` | OS credential store when available; otherwise `file` |

> [!warning]
> If using file-based storage, treat `~/.codex/auth.json` like a password. Don't commit it, paste it into tickets, or share it in chat.

## Enforce a login method or workspace

In managed environments, admins may restrict authentication:

```toml
forced_login_method = "chatgpt"   # or "api"
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"
```

If active credentials don't match restrictions, Codex logs out and exits. Commonly applied via managed configuration. See [[018-enterprise-managed-configuration|Managed configuration]].

## Login diagnostics

`codex login` writes a dedicated `codex-login.log` under your configured log directory. Use it to debug browser-login or device-code failures.

## Custom CA bundles

For corporate TLS proxies or private root CAs:

```shell
export CODEX_CA_CERTIFICATE=/path/to/corporate-root-ca.pem
codex login
```

When `CODEX_CA_CERTIFICATE` is unset, Codex falls back to `SSL_CERT_FILE`. Applies to login, HTTPS requests, and secure websocket connections.

## Login on headless devices

Browser-based login may fail in remote/headless environments or when localhost callback is blocked. Prefer device code authentication (beta).

### Preferred: Device code authentication (beta)

1. Enable device code login in ChatGPT security settings (personal) or workspace permissions (admin).
2. In the terminal:
   - Interactive login UI: select **Sign in with Device Code**
   - Or run: `codex login --device-auth`
3. Open the link in your browser, sign in, enter the one-time code.

If not enabled server-side, Codex falls back to browser-based login.

### Fallback 1: Copy auth cache from a machine with a browser

1. On a machine with browser access: `codex login`
2. Confirm `~/.codex/auth.json` exists.
3. Copy it to the headless machine's `~/.codex/auth.json`.

If your OS uses a credential store instead of `auth.json`, configure file-based storage first (see [Credential storage](#credential-storage)).

Copy over SSH:
```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json
```

Or one-liner without `scp`:
```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json
```

Copy into Docker:
```shell
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"
```

For CI/CD runners, see [Maintain Codex account auth in CI/CD (advanced)](https://developers.openai.com/codex/auth/ci-cd-auth). API keys remain the recommended default for automation.

### Fallback 2: Forward localhost callback over SSH

If you can forward ports between local machine and remote host:

```shell
ssh -L 1455:localhost:1455 user@remote
```

In that SSH session, run `codex login` and follow the printed address on your local machine.

## Alternative model providers

When you define a [custom model provider](https://developers.openai.com/codex/config-advanced#custom-model-providers), choose authentication:

| Method | Config | Use case |
|--------|--------|----------|
| OpenAI auth | `requires_openai_auth = true` | Access OpenAI models through an LLM proxy. Ignores `env_key`. |
| Environment variable | `env_key = "<ENV_VARIABLE_NAME>"` | Provider-specific API key from local env |
| No authentication | omit both | Local models |

#authentication #security #api-keys #codex