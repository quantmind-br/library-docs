---
title: '`lms server start`'
url: https://lmstudio.ai/docs/cli/serve/server-start
source: sitemap
fetched_at: 2026-04-07T21:28:25.581426839-03:00
rendered_js: false
word_count: 138
summary: This document details how to use the `lms server start` command to launch a local model inference server, providing instructions on setting custom ports and enabling Cross-Origin Resource Sharing (CORS) support.
tags:
    - lms-server
    - start-command
    - http-api
    - cors-support
    - local-server
    - cli-usage
category: guide
---

The `lms server start` command launches the LM Studio local server, allowing you to interact with loaded models via HTTP API calls.

### Flags[](#flags)

--port (optional) : number

Port to run the server on. If not provided, uses the last used port

--cors (optional) : flag

Enable CORS support for web application development. When not set, CORS is disabled

## Start the server[](#start-the-server "Link to 'Start the server'")

Start the server with default settings:


### Specify a custom port[](#specify-a-custom-port)

Run the server on a specific port:

```

lms server start --port 3000
```

### Enable CORS support[](#enable-cors-support)

For usage with web applications or some VS Code extensions, you may need to enable CORS support:


Note that enabling CORS may expose your server to security risks, so use it only when necessary.

### Check the server status[](#check-the-server-status)

See [`lms server status`](https://lmstudio.ai/docs/cli/serve/server-status) for more information on checking the status of the server.