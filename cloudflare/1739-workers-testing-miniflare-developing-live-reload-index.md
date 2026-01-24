---
title: ⚡️ Live Reload · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/testing/miniflare/developing/live-reload/index.md
source: llms
fetched_at: 2026-01-24T15:31:57.652986805-03:00
rendered_js: false
word_count: 47
summary: This document explains how to enable and use the live reload feature in Miniflare to automatically refresh the browser upon script changes.
tags:
    - miniflare
    - live-reload
    - cloudflare-workers
    - development-workflow
    - hot-reloading
category: configuration
---

Miniflare automatically refreshes your browser when your Worker script changes when `liveReload` is set to `true`.

```js
const mf = new Miniflare({
  liveReload: true,
});
```

Miniflare will only inject the `<script>` tag required for live-reload at the end of responses with the `Content-Type` header set to `text/html`:

```js
export default {
  fetch() {
    const body = `
      <!DOCTYPE html>
      <html>
      <body>
        <p>Try update me!</p>
      </body>
      </html>
    `;


    return new Response(body, {
      headers: { "Content-Type": "text/html; charset=utf-8" },
    });
  },
};
```