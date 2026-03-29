---
title: Subdomains · Cloudflare Email Routing docs
url: https://developers.cloudflare.com/email-routing/setup/subdomains/index.md
source: llms
fetched_at: 2026-01-24T15:13:59.295353027-03:00
rendered_js: false
word_count: 153
summary: This document provides instructions on how to enable and configure Cloudflare Email Routing for specific subdomains within a zone.
tags:
    - cloudflare
    - email-routing
    - subdomain-management
    - dns-configuration
    - routing-rules
category: tutorial
---

Email Routing is a [zone-level](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/#zones) feature. A zone has a top-level domain (the same as the zone name) and it can have subdomains (managed under the DNS feature.) As an example, you can have the `example.com` zone, and then the `mail.example.com` and `corp.example.com` sub-domains under it.

You can use Email Routing with any subdomain of any zone in your account. Follow these steps to add Email Routing features to a new subdomain:

1. In the Cloudflare dashboard, go to the **Email Routing** page.

   [Go to **Email Routing**](https://dash.cloudflare.com/?to=/:account/:zone/email/routing)

2. Go to **Settings**, and select **Add subdomain**.

Once the subdomain is added and the DNS records are configured, you can see it in the **Settings** list under the **Subdomains** section.

Now you can go to **Email** > **Email Routing** > **Routing rules** and create new custom addresses that will show you the option of using either the top domain of the zone or any other configured subdomain.