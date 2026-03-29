---
title: CLI Authentication | liteLLM
url: https://docs.litellm.ai/docs/proxy/cli_sso
source: sitemap
fetched_at: 2026-01-21T19:51:22.163949614-03:00
rendered_js: false
word_count: 183
summary: This guide explains how to install and use the LiteLLM CLI to authenticate to the LiteLLM Gateway via SSO for self-serve access.
tags:
    - litellm-cli
    - sso-authentication
    - gateway-access
    - cli-tool
    - proxy-setup
category: tutorial
---

Use the litellm cli to authenticate to the LiteLLM Gateway. This is great if you're trying to give a large number of developers self-serve access to the LiteLLM Gateway.

## Demo[​](#demo "Direct link to Demo")

## Usage[​](#usage "Direct link to Usage")

### Prerequisites - Start LiteLLM Proxy with Beta Flag[​](#prerequisites---start-litellm-proxy-with-beta-flag "Direct link to Prerequisites - Start LiteLLM Proxy with Beta Flag")

Beta Feature - Required

CLI SSO Authentication is currently in beta. You must set this environment variable **when starting up your LiteLLM Proxy**:

```
export EXPERIMENTAL_UI_LOGIN="True"
litellm --config config.yaml
```

Or add it to your proxy startup command:

```
EXPERIMENTAL_UI_LOGIN="True" litellm --config config.yaml
```

### Steps[​](#steps "Direct link to Steps")

1. **Install the CLI**
   
   If you have [uv](https://github.com/astral-sh/uv) installed, you can try this:
   
   ```
   uv tool install 'litellm[proxy]'
   ```
   
   If that works, you'll see something like this:
   
   ```
   ...
   Installed 2 executables: litellm, litellm-proxy
   ```
   
   and now you can use the tool by just typing `litellm-proxy` in your terminal:
2. **Set up environment variables**
   
   On your local machine, set the proxy URL:
   
   ```
   export LITELLM_PROXY_URL=http://localhost:4000
   ```
   
   *(Replace with your actual proxy URL)*
3. **Login**
   
   This will open a browser window to authenticate. If you have connected LiteLLM Proxy to your SSO provider, you should be able to login with your SSO credentials. Once logged in, you can use the CLI to make requests to the LiteLLM Gateway.
4. **Make a test request to view models**
   
   ```
   litellm-proxy models list
   ```
   
   This will list all the models available to you.