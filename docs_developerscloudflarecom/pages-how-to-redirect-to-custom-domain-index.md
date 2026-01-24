---
title: Redirecting *.pages.dev to a Custom Domain · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/how-to/redirect-to-custom-domain/index.md
source: llms
fetched_at: 2026-01-24T15:18:22.150519868-03:00
rendered_js: false
word_count: 207
summary: This guide provides step-by-step instructions for using Cloudflare Bulk Redirects to forward traffic from a default Pages subdomain to a custom domain.
tags:
    - cloudflare-pages
    - bulk-redirects
    - custom-domains
    - url-forwarding
    - redirect-rules
category: tutorial
---

Learn how to use [Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/) to redirect your `*.pages.dev` subdomain to your [custom domain](https://developers.cloudflare.com/pages/configuration/custom-domains/).

You may want to do this to ensure that your site's content is served only on the custom domain, and not the `<project>.pages.dev` site automatically generated on your first Pages deployment.

## Setup

To redirect a `<project>.pages.dev` subdomain to your custom domain:

1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

   [Go to **Workers & Pages**](https://dash.cloudflare.com/?to=/:account/workers-and-pages)

2. Select your Pages project.

3. Go to **Custom domains** and make sure that your custom domain is listed. If it is not, add it by clicking **Set up a custom domain**.

4. Go **Bulk Redirects**.

5. [Create a bulk redirect list](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list) modeled after the following (but replacing the values as appropriate):

| Source URL | Target URL | Status | Parameters |
| - | - | - | - |
| `<project>.pages.dev` | `https://example.com` | `301` | * Preserve query string
* Subpath matching
* Preserve path suffix
* Include subdomains |

1. [Create a bulk redirect rule](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/#2-create-a-bulk-redirect-rule) using the list you just created.

To test that your redirect worked, go to your `<project>.pages.dev` domain. If the URL is now set to your custom domain, then the rule has propagated.

## Related resources

* [Redirect www to domain apex](https://developers.cloudflare.com/pages/how-to/www-redirect/)
* [Handle redirects with Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)