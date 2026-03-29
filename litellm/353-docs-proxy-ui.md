---
title: Quick Start | liteLLM
url: https://docs.litellm.ai/docs/proxy/ui
source: sitemap
fetched_at: 2026-01-21T19:53:53.456643358-03:00
rendered_js: false
word_count: 230
summary: This document explains how to set up, access, and configure the LiteLLM Admin UI for managing models, API keys, and proxy server settings.
tags:
    - litellm
    - admin-ui
    - proxy-server
    - model-management
    - api-key-management
    - user-access-control
category: guide
---

Create keys, track spend, add models without worrying about the config / CRUD endpoints.

## Quick Start[​](#quick-start-1 "Direct link to Quick Start")

- Requires proxy master key to be set
- Requires db connected

Follow [setup](https://docs.litellm.ai/docs/proxy/virtual_keys#setup)

### 1. Start the proxy[​](#1-start-the-proxy "Direct link to 1. Start the proxy")

```
litellm --config /path/to/config.yaml

#INFO: Proxy running on http://0.0.0.0:4000
```

### 2. Go to UI[​](#2-go-to-ui "Direct link to 2. Go to UI")

```
http://0.0.0.0:4000/ui # <proxy_base_url>/ui
```

### 3. Get Admin UI Link on Swagger[​](#3-get-admin-ui-link-on-swagger "Direct link to 3. Get Admin UI Link on Swagger")

Your Proxy Swagger is available on the root of the Proxy: e.g.: `http://localhost:4000/`

### 4. Change default username + password[​](#4-change-default-username--password "Direct link to 4. Change default username + password")

Set the following in your .env on the Proxy

```
LITELLM_MASTER_KEY="sk-1234" # this is your master key for using the proxy server
UI_USERNAME=ishaan-litellm   # username to sign in on UI
UI_PASSWORD=langchain        # password to sign in on UI
```

On accessing the LiteLLM UI, you will be prompted to enter your username, password

### 5. Configure Root Redirect URL[​](#5-configure-root-redirect-url "Direct link to 5. Configure Root Redirect URL")

When `DOCS_URL` is set to something other than `"/"`, you can configure where the root path (`/`) redirects to using `ROOT_REDIRECT_URL`:

```
DOCS_URL="/docs"              # Set docs to a different path
ROOT_REDIRECT_URL="/ui"       # Redirect root path (/) to /ui
```

By default, `DOCS_URL` is `"/"`, so this setting is only needed when you've changed `DOCS_URL` to a different path.

## Invite-other users[​](#invite-other-users "Direct link to Invite-other users")

Allow others to create/delete their own keys.

[**Go Here**](https://docs.litellm.ai/docs/proxy/self_serve)

## Model Management[​](#model-management "Direct link to Model Management")

The Admin UI provides comprehensive model management capabilities:

- **Add Models**: Add new models through the UI without restarting the proxy
- **AI Hub**: Make models and agents public for developers to discover what's available
- **Price Data Sync**: Keep model pricing data up to date by syncing from GitHub

For detailed information on model management, see [Model Management](https://docs.litellm.ai/docs/proxy/model_management).

For information on sharing models and agents, see [AI Hub](https://docs.litellm.ai/docs/proxy/ai_hub).

## Disable Admin UI[​](#disable-admin-ui "Direct link to Disable Admin UI")

Set `DISABLE_ADMIN_UI="True"` in your environment to disable the Admin UI.

Useful, if your security team has additional restrictions on UI usage.

**Expected Response**