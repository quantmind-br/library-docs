---
title: Load Zaraz selectively · Cloudflare Zaraz docs
url: https://developers.cloudflare.com/zaraz/advanced/load-selectively/index.md
source: llms
fetched_at: 2026-01-24T15:34:38.030446987-03:00
rendered_js: false
word_count: 81
summary: This document explains how to use Cloudflare Configuration Rules to selectively load or block Zaraz on specific URLs, subdomains, or based on request parameters.
tags:
    - cloudflare-zaraz
    - configuration-rules
    - selective-loading
    - request-filtering
    - blocking-triggers
category: configuration
---

You can use [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/) to load Zaraz selectively on specific URLs or subdomains. Configuration Rules can also be used to block Zaraz from loading based on cookies, IP addresses or anything else related to a request.

Refer to [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/) documentation to learn more about this feature and how you can use it with Zaraz.

Note

If you need to block one or more actions from firing in a tool, Cloudflare recommends you use [Blocking Triggers](https://developers.cloudflare.com/zaraz/advanced/blocking-triggers/) instead of Configuration Rules.