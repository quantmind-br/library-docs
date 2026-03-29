---
title: Early Hints for SaaS · Cloudflare for Platforms docs
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/early-hints-for-saas/index.md
source: llms
fetched_at: 2026-01-24T15:09:33.241695613-03:00
rendered_js: false
word_count: 260
summary: This document explains how to enable Early Hints for Cloudflare for SaaS custom hostnames using the API to improve loading speeds for end users.
tags:
    - early-hints
    - cloudflare-for-saas
    - custom-hostnames
    - api-configuration
    - performance-optimization
category: guide
---

[Early Hints](https://developers.cloudflare.com/cache/advanced-configuration/early-hints/) allows the browser to begin loading resources while the origin server is compiling the full response. This improves webpage’s loading speed for the end user. As a SaaS provider, you may prioritize speed for some of your custom hostnames. Using custom metadata, you can [enable Early Hints](https://developers.cloudflare.com/cache/advanced-configuration/early-hints/#enable-early-hints) per custom hostname.

***

## Prerequisites

Before you can employ Early Hints for SaaS, you need to create a custom hostname. Review [Get Started with Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/) if you have not already done so.

***

## Enable Early Hints per custom hostname via the API

1. [Locate your zone ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/), available in the Cloudflare dashboard.

2. Locate your Authentication Key on the [**API Tokens**](https://dash.cloudflare.com/?to=/:account/profile/api-tokens) page, under **Global API Key**.

3. If you are [creating a new custom hostname](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/create/), make an API call such as the example below, specifying `"early_hints": "on"`:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

* `SSL and Certificates Write`

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames" \
  --request POST \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --json '{
    "hostname": "<CUSTOM_HOSTNAME>",
    "ssl": {
        "method": "http",
        "type": "dv",
        "settings": {
            "http2": "on",
            "min_tls_version": "1.2",
            "tls_1_3": "on",
            "early_hints": "on"
        },
        "bundle_method": "ubiquitous",
        "wildcard": false
    }
  }'
```

1. For an existing custom hostname, locate the `id` of that hostname via a `GET` call:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

* `SSL and Certificates Write`
* `SSL and Certificates Read`

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames?hostname=%7Bhostname%7D" \
  --request GET \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

1. Then make an API call such as the example below, specifying `"early_hints": "on"`:

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

* `SSL and Certificates Write`

```bash
curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/custom_hostnames/$CUSTOM_HOSTNAME_ID" \
  --request PATCH \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --json '{
    "ssl": {
        "method": "http",
        "type": "dv",
        "settings": {
            "http2": "on",
            "min_tls_version": "1.2",
            "tls_1_3": "on",
            "early_hints": "on"
        }
    }
  }'
```

Currently, all options within `settings` are required in order to prevent those options from being set to default. You can pull the current settings state prior to updating Early Hints by leveraging the output that returns the `id` for the hostname.