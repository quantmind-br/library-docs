---
title: Browser TTL · Cloudflare Images docs
url: https://developers.cloudflare.com/images/manage-images/browser-ttl/index.md
source: llms
fetched_at: 2026-01-24T15:15:17.63206474-03:00
rendered_js: false
word_count: 235
summary: This document explains how to configure Browser TTL settings for Cloudflare Images to control browser caching durations at both account and named variant levels.
tags:
    - cloudflare-images
    - caching
    - browser-ttl
    - cache-control
    - image-variants
    - api-config
category: configuration
---

Browser TTL controls how long an image stays in a browser's cache and specifically configures the `cache-control` response header.

### Default TTL

By default, an image's TTL is set to two days to meet user needs, such as re-uploading an image under the same [Custom ID](https://developers.cloudflare.com/images/upload-images/upload-custom-path/).

## Custom setting

You can use two custom settings to control the Browser TTL, an account or a named variant. To adjust how long a browser should keep an image in the cache, set the TTL in seconds, similar to how the `max-age` header is set. The value should be an interval between one hour to one year.

### Browser TTL for an account

Setting the Browser TTL per account overrides the default TTL.

```bash
curl --request PATCH 'https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config' \
--header "Authorization: Bearer <API_TOKEN>" \
--header "Content-Type: application/json" \
--data '{
  "browser_ttl": 31536000
}'
```

When the Browser TTL is set to one year for all images, the response for the `cache-control` header is essentially `public`, `max-age=31536000`, `stale-while-revalidate=7200`.

### Browser TTL for a named variant

Setting the Browser TTL for a named variant is a more granular option that overrides all of the above when creating or updating an image variant, specifically the `browser_ttl` option in seconds.

```bash
curl 'https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_TAG>/images/v1/variants' \
--header "Authorization: Bearer <API_TOKEN>" \
--header "Content-Type: application/json" \
--data '{
  "id":"avatar",
  "options": {
    "width":100,
    "browser_ttl": 86400
  }
}'
```

When the Browser TTL is set to one day for images requested with this variant, the response for the `cache-control` header is essentially `public`, `max-age=86400`, `stale-while-revalidate=7200`.

Note

[Private images](https://developers.cloudflare.com/images/manage-images/serve-images/serve-private-images/) do not respect default or custom TTL settings. The private images cache time is set according to the expiration time and can be as short as one hour.