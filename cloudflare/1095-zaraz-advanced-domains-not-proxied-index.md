---
title: Use Zaraz on domains not proxied by Cloudflare · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/advanced/domains-not-proxied/index.md
source: llms
fetched_at: 2026-01-24T15:34:33.277398945-03:00
rendered_js: false
word_count: 72
summary: This document explains how to load Cloudflare Zaraz on domains that are not proxied by Cloudflare by routing the script through a separate proxied subdomain.
tags:
    - zaraz
    - cloudflare
    - external-domains
    - proxied-subdomain
    - orange-cloud
    - script-loading
category: guide
---

You can load Zaraz on domains that are not proxied through Cloudflare. However, you will need to create a separate domain, or subdomain, proxied by Cloudflare (also [known as orange-clouded](https://community.cloudflare.com/t/step-3-enabling-the-orange-cloud/52715) domains), and load the script from it:

1. Create a new subdomain like `my-subdomain.example.com` and proxy it through Cloudflare. Refer to [Enabling the Orange Cloud](https://community.cloudflare.com/t/step-3-enabling-the-orange-cloud/52715) for more information.
2. Add the following script to your main website’s HTML, immediately before the `</head>` tag closes:

```html
<script src="https://my-subdomain.example.com/cdn-cgi/zaraz/i.js"></script>
```