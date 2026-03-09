---
title: Remote Server | Camoufox
url: https://camoufox.com/python/remote-server/
source: sitemap
fetched_at: 2026-03-09T16:48:00.230542-03:00
rendered_js: false
word_count: 89
summary: This document explains how to launch Camoufox as a remote websocket server and how clients using the Playwright API can connect to it from other devices or languages.
tags:
    - websocket-server
    - remote-access
    - playwright
    - launching
    - connecting
category: guide
---

Camoufox can be ran as a remote websocket server. It can be accessed from other devices, and languages other than Python supporting the Playwright API.

* * *

## [#](#launching)Launching

To launch a remote server, run the following CLI command:

```bash

python -m camoufox server
```

Or, configure the server with a launch script:

```python

from camoufox.server import launch_server

launch_server(
    headless=True,
    geoip=True,
    proxy={
        'server': 'http://example.com:8080',
        'username': 'username',
        'password': 'password'
    },
    port=1234,
    ws_path='hello'
)
```

The server's port and URL path will be defined using the `port` and `ws_path` parameters, or will be random if not defined.

```none

Websocket endpoint: ws://localhost:1234/hello 
```

All of the following parameters are also supported:

See parameters list

../usage/#parameters-list

* * *

## [#](#connecting)Connecting

To connect to the remote server, use Playwright's `connect` method:

```python

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Example endpoint
    browser = p.firefox.connect('ws://localhost:1234/hello')
    page = browser.new_page()
    ...
```