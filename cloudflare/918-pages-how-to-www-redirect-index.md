---
title: Redirecting www to domain apex · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/how-to/www-redirect/index.md
source: llms
fetched_at: 2026-01-24T15:18:26.163259222-03:00
rendered_js: false
word_count: 213
summary: This document provides a step-by-step guide on how to configure a redirect from a www subdomain to an apex domain using Cloudflare Bulk Redirects and DNS settings.
tags:
    - cloudflare-pages
    - bulk-redirects
    - dns-configuration
    - subdomain-redirect
    - apex-domain
category: tutorial
---

Learn how to redirect a `www` subdomain to your apex domain (`example.com`).

This setup assumes that you already have a [custom domain](https://developers.cloudflare.com/pages/configuration/custom-domains/) attached to your Pages project.

## Setup

To redirect your `www` subdomain to your domain apex:

1. In the Cloudflare dashboard, go to the **Bulk Redirects** page.

   [Go to **Bulk redirects**](https://dash.cloudflare.com/?to=/:account/bulk-redirects)

2. [Create a bulk redirect list](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list) modeled after the following (but replacing the values as appropriate):

| Source URL | Target URL | Status | Parameters |
| - | - | - | - |
| `www.example.com` | `https://example.com` | `301` | * Preserve query string
* Subpath matching
* Preserve path suffix
* Include subdomains |

1. [Create a bulk redirect rule](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/#2-create-a-bulk-redirect-rule) using the list you just created.
2. Go to **DNS**.
3. [Create a DNS record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records) for the `www` subdomain using the following values:

| Type | Name | IPv4 address | Proxy status |
| - | - | - | - |
| `A` | `www` | `192.0.2.1` | Proxied |

It may take a moment for this DNS change to propagate, but once complete, you can run the following command in your terminal.

```sh
curl --head -i https://www.example.com/
```

Then, inspect the output to verify that the `location` header and status code are being set as configured.

## Related resources

* [Redirect `*.pages.dev` to a custom domain](https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/)
* [Handle redirects with Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)