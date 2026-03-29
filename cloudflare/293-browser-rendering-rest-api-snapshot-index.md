---
title: /snapshot - Take a webpage snapshot · Cloudflare Browser Rendering docs
url: https://developers.cloudflare.com/browser-rendering/rest-api/snapshot/index.md
source: llms
fetched_at: 2026-01-24T15:09:00.851405725-03:00
rendered_js: false
word_count: 419
summary: This document explains how to use the Cloudflare Browser Rendering snapshot endpoint to capture both rendered HTML and screenshots of a webpage in a single request. It covers configuration options for custom scripts, viewport settings, and handling JavaScript-heavy content.
tags:
    - cloudflare-api
    - browser-rendering
    - snapshot
    - screenshot
    - html-capture
    - headless-browser
category: api
---

The `/snapshot` endpoint captures both the HTML content and a screenshot of the webpage in one request. It returns the HTML as a text string and the screenshot as a Base64-encoded image.

## Endpoint

```txt
https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/snapshot
```

## Required fields

You must provide either `url` or `html`:

* `url` (string)
* `html` (string)

## Common use cases

* Capture both the rendered HTML and a visual screenshot in a single API call
* Archive pages with visual and structural data together
* Build monitoring tools that compare visual and DOM differences over time

## Basic usage

### Capture a snapshot from a URL

* curl

  1. Go to `https://example.com/`.
  2. Inject custom JavaScript.
  3. Capture the rendered HTML.
  4. Take a screenshot.

  ```bash
  curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/snapshot' \
    -H 'Authorization: Bearer <apiToken>' \
    -H 'Content-Type: application/json' \
    -d '{
      "url": "https://example.com/",
      "addScriptTag": [
        { "content": "document.body.innerHTML = \"Snapshot Page\";" }
      ]
    }'
  ```

  ```json
  {
    "success": true,
    "result": {
      "screenshot": "Base64EncodedScreenshotString",
      "content": "<html>...</html>"
    }
  }
  ```

* TypeScript SDK

  ```typescript
  import Cloudflare from "cloudflare";


  const client = new Cloudflare({
    apiToken: process.env["CLOUDFLARE_API_TOKEN"],
  });


  const snapshot = await client.browserRendering.snapshot.create({
    account_id: process.env["CLOUDFLARE_ACCOUNT_ID"],
    url: "https://example.com/",
    addScriptTag: [
          { content: "document.body.innerHTML = \"Snapshot Page\";" }
      ]
  });


  console.log(snapshot.content);
  ```

## Advanced usage

Looking for more parameters?

Visit the [Browser Rendering API reference](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/snapshot/methods/create/) for all available parameters, such as setting HTTP credentials using `authenticate`, setting `cookies`, and customizing load behavior using `gotoOptions`.

### Create a snapshot from custom HTML

The `html` property in the JSON payload, it sets the html to `<html><body>Advanced Snapshot</body></html>` then does the following steps:

1. Disable JavaScript.
2. Sets the screenshot to `fullPage`.
3. Changes the page size `(viewport)`.
4. Waits up to `30000ms` or until the `DOMContentLoaded` event fires.
5. Returns the rendered HTML content and a base-64 encoded screenshot of the page.

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/snapshot' \
  -H 'Authorization: Bearer <apiToken>' \
  -H 'Content-Type: application/json' \
  -d '{
    "html": "<html><body>Advanced Snapshot</body></html>",
    "setJavaScriptEnabled": false,
    "screenshotOptions": {
       "fullPage": true
    },
    "viewport": {
      "width": 1200,
      "height": 800
    },
    "gotoOptions": {
      "waitUntil": "domcontentloaded",
      "timeout": 30000
    }
  }'
```

```json
{
  "success": true,
  "result": {
    "screenshot": "AdvancedBase64Screenshot",
    "content": "<html><body>Advanced Snapshot</body></html>"
  }
}
```

### Improve blurry screenshot resolution

If you set a large viewport width and height, your screenshot may appear blurry or pixelated. This can happen if your browser's default `deviceScaleFactor` (which defaults to 1) is not high enough for the viewport.

To fix this, increase the value of the `deviceScaleFactor`.

```json
{
  "url": "https://cloudflare.com/",
  "viewport": {
    "width": 3600,
    "height": 2400,
    "deviceScaleFactor": 2
  }
}
```

### Handling JavaScript-heavy pages

For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.

The simplest solution is to use the `gotoOptions.waitUntil` parameter set to `networkidle0` or `networkidle2`:

```json
{
  "url": "https://example.com",
  "gotoOptions": {
    "waitUntil": "networkidle0"
  }
}
```

For faster responses, advanced users can use `waitForSelector` to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to [REST API timeouts](https://developers.cloudflare.com/browser-rendering/reference/timeouts/).

### Set a custom user agent

You can change the user agent at the page level by passing `userAgent` as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.

Note

The `userAgent` parameter does not bypass bot protection. Requests from Browser Rendering will always be identified as a bot.

## Troubleshooting

If you have questions or encounter an error, see the [Browser Rendering FAQ and troubleshooting guide](https://developers.cloudflare.com/browser-rendering/faq/).