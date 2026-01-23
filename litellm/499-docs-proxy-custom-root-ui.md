---
title: UI - Custom Root Path | liteLLM
url: https://docs.litellm.ai/docs/proxy/custom_root_ui
source: sitemap
fetched_at: 2026-01-21T19:51:35.06719753-03:00
rendered_js: false
word_count: 113
summary: This guide explains how to configure and run the LiteLLM proxy on a custom base URL path using the SERVER_ROOT_PATH environment variable.
tags:
    - litellm
    - proxy-server
    - custom-root-path
    - environment-variables
    - server-configuration
category: configuration
---

💥 Use this when you want to serve LiteLLM on a custom base url path like `https://localhost:4000/api/v1`

info

Requires v1.72.3 or higher.

Limitations:

- This does not work in [litellm non-root](https://docs.litellm.ai/docs/proxy/deploy#non-root---without-internet-connection) images, as it requires write access to the UI files.

## Usage[​](#usage "Direct link to Usage")

### 1. Set `SERVER_ROOT_PATH` in your .env[​](#1-set-server_root_path-in-your-env "Direct link to 1-set-server_root_path-in-your-env")

👉 Set `SERVER_ROOT_PATH` in your .env and this will be set as your server root path

```
export SERVER_ROOT_PATH="/api/v1"
```

### 2. Run the Proxy[​](#2-run-the-proxy "Direct link to 2. Run the Proxy")

```
litellm proxy --config /path/to/config.yaml
```

After running the proxy you can access it on `http://0.0.0.0:4000/api/v1/` (since we set `SERVER_ROOT_PATH="/api/v1"`)

### 3. Verify Running on correct path[​](#3-verify-running-on-correct-path "Direct link to 3. Verify Running on correct path")

**That's it**, that's all you need to run the proxy on a custom root path

## Demo[​](#demo "Direct link to Demo")

[Here's a demo video](https://drive.google.com/file/d/1zqAxI0lmzNp7IJH1dxlLuKqX2xi3F_R3/view?usp=sharing) of running the proxy on a custom root path