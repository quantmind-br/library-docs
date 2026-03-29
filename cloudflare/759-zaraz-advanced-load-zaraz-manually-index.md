---
title: Load Zaraz manually · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/advanced/load-zaraz-manually/index.md
source: llms
fetched_at: 2026-01-24T15:34:39.889012138-03:00
rendered_js: false
word_count: 125
summary: This guide explains how to manually load the Zaraz script on Cloudflare-proxied websites by disabling auto-injection and adding a specific script tag to the HTML head.
tags:
    - cloudflare-zaraz
    - manual-injection
    - script-loading
    - web-analytics
    - html-integration
category: guide
---

By default, if your domain is proxied by Cloudflare, Zaraz will automatically inject itself to HTML pages in your site. This makes it easier to get up and running quickly. However, you might want to load Zaraz manually, for example to test Zaraz on specific pages first.

After you turn off the [Auto-inject script](https://developers.cloudflare.com/zaraz/reference/settings/#auto-inject-script) option, you will have to manually include the Zaraz script in your HTML, immediately before the `</head>` tag closes. The path to your script would be `/cdn-cgi/zaraz/i.js`. Your script tag should look like this:

```html
<script src="/cdn-cgi/zaraz/i.js" referrerpolicy="origin"></script>
```

With the script, your page HTML should be similar to the following:

```html
<html>
  <head>
    ….
    <script src="/cdn-cgi/zaraz/i.js" referrerpolicy="origin"></script>
  </head>
  <body>
    …
  </body>
</html>
```

Note that if your site is not proxied by Cloudflare, you should refer to the section about [Using Zaraz on domains not proxied by Cloudflare](https://developers.cloudflare.com/zaraz/advanced/domains-not-proxied/).