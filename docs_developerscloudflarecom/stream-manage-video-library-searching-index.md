---
title: Search for videos · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/manage-video-library/searching/index.md
source: llms
fetched_at: 2026-01-24T15:23:39.9087665-03:00
rendered_js: false
word_count: 54
summary: Explains how to use the search query parameter with the Cloudflare Stream API to find specific media files by name.
tags:
    - cloudflare-stream
    - video-search
    - api-endpoint
    - media-management
    - query-parameters
category: api
---

You can search for videos by name through the Stream API by adding a `search` query parameter to the [list media files](https://developers.cloudflare.com/api/resources/stream/methods/list/) endpoint.

## What you will need

To make API requests you will need a [Cloudflare API token](https://www.cloudflare.com/a/account/my-account) and your Cloudflare [account ID](https://www.cloudflare.com/a/overview/).

## cURL example

This example lists media where the name matches `puppy.mp4`.

```bash
curl -X GET "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/stream?search=puppy" \
     -H "Authorization: Bearer <API_TOKEN>" \
     -H "Content-Type: application/json"
```