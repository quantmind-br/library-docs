---
title: Embeds · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/embeds/index.md
source: llms
fetched_at: 2026-01-24T15:34:25.218139034-03:00
rendered_js: false
word_count: 188
summary: This document explains how to implement server-side rendered embeds using Cloudflare Zaraz to enhance website performance and security. It details the setup process in the Cloudflare dashboard and how to use HTML placeholders for external content.
tags:
    - cloudflare-zaraz
    - server-side-rendering
    - embeds
    - web-performance
    - third-party-scripts
    - security
category: tutorial
---

Embeds are tools for incorporating external content, like social media posts, directly onto webpages, enhancing user engagement without compromising site performance and security.

Cloudflare Zaraz introduces server-side rendering for embeds, avoiding third-party JavaScript to improve security, privacy, and page speed. This method processes content on the server side, removing the need for direct communication between the user's browser and third-party servers.

To add an Embed to Your Website:

1. In the Cloudflare dashboard, go to the **Tag Setup** page.

   [Go to **Tag setup**](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz)

2. Go to **Tools Configuration**.

3. Click "add new tool" and activate the desired tools on your Cloudflare Zaraz dashboard.

4. Add a placeholder in your HTML, specifying the necessary attributes. For a generic embed, the snippet looks like this:

```html
<componentName-embedName attribute="value"></componentName-embedName>
```

Replace `componentName`, `embedName` and `attribute="value"` with the specific Managed Component requirements. Zaraz automatically detects placeholders and replaces them with the content in a secure and efficient way.

## Examples

### X (Twitter) embed

```html
<twitter-post tweet-id="12345"></twitter-post>
```

Replace `tweet-id` with the actual tweet ID for the content you wish to embed.

### Instagram embed

```html
<instagram-post post-url="https://www.instagram.com/p/ABC/" captions="true"></instagram-post>
```

Replace `post-url` with the actual URL for the content you wish to embed. To include posts captions set captions attribute to `true`.