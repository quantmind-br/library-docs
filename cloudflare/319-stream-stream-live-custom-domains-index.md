---
title: Add custom ingest domains · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/stream-live/custom-domains/index.md
source: llms
fetched_at: 2026-01-24T15:23:44.174499406-03:00
rendered_js: false
word_count: 134
summary: This document explains how to set up and manage custom ingest domains for RTMPS feeds, enabling users to use their own domain names for live stream inputs.
tags:
    - cloudflare-stream
    - rtmps
    - custom-domains
    - dns-settings
    - live-input
category: configuration
---

With custom ingest domains, you can configure your RTMPS feeds to use an ingest URL that you specify instead of using `live.cloudflare.com.`

Note

Custom Ingest Domains cannot be configured for domains with [zone holds](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/) enabled.

1. In the Cloudflare dashboard, go to the **Live inputs** page.

   [Go to **Live inputs**](https://dash.cloudflare.com/?to=/:account/stream/inputs)

2. Select **Settings**, above the list. The **Custom Input Domains** page displays.

3. Under **Domain**, add your domain and select **Add domain**.

4. At your DNS provider, add a CNAME record that points to `live.cloudflare.com`. If your DNS provider is Cloudflare, this step is done automatically.

If you are using Cloudflare for DNS, ensure the [**Proxy status**](https://developers.cloudflare.com/dns/proxy-status/) of your ingest domain is **DNS only** (grey-clouded).

## Delete a custom domain

1. From the **Custom Input Domains** page under **Hostnames**, locate the domain.
2. Select the menu icon under **Action**. Select **Delete**.