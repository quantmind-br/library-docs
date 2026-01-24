---
title: Browser close reasons · Cloudflare Browser Rendering docs
url: https://developers.cloudflare.com/browser-rendering/reference/browser-close-reasons/index.md
source: llms
fetched_at: 2026-01-24T14:04:19.276398192-03:00
rendered_js: false
word_count: 129
summary: This document explains how to handle and troubleshoot browser session closures in Cloudflare Browser Rendering, including how to access logs and common reasons for termination.
tags:
    - cloudflare-browser-rendering
    - session-management
    - error-handling
    - troubleshooting
    - puppeteer
category: guide
---

A browser session may close for a variety of reasons, occasionally due to connection errors or errors in the headless browser instance. As a best practice, wrap `puppeteer.connect` or `puppeteer.launch` in a [`try/catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) statement.

To find the reason that a browser closed:

1. In the Cloudflare dashboard, go to the **Browser Rendering** page.

   [Go to **Browser Rendering**](https://dash.cloudflare.com/?to=/:account/workers/browser-rendering)

2. Select the **Logs** tab.

Browser Rendering sessions are billed based on [usage](https://developers.cloudflare.com/browser-rendering/pricing/). We do not charge for sessions that error due to underlying Browser Rendering infrastructure.

| Reasons a session may end |
| - |
| User opens and closes browser normally. |
| Browser is idle for 60 seconds. |
| Chromium instance crashes. |
| Error connecting with the client, server, or Worker. |
| Browser session is evicted. |