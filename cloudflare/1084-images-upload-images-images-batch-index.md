---
title: Upload via batch API · Cloudflare Images docs
url: https://developers.cloudflare.com/images/upload-images/images-batch/index.md
source: llms
fetched_at: 2026-01-24T15:15:52.168396436-03:00
rendered_js: false
word_count: 170
summary: This document explains how to use the Cloudflare Images batch API to perform multiple image operations while bypassing standard global API rate limits. It provides instructions on obtaining a batch token and using it with specialized endpoints for high-throughput tasks.
tags:
    - cloudflare-images
    - batch-api
    - rate-limiting
    - api-token
    - image-management
    - high-throughput
category: api
---

The Images batch API lets you make several requests in sequence while bypassing Cloudflare’s global API rate limits.

To use the Images batch API, you will need to obtain a batch token and use the token to make several requests. The requests authorized by this batch token are made to a separate endpoint and do not count toward the global API rate limits. Each token is subject to a rate limit of 200 requests per second. You can use multiple tokens if you require higher throughput to the Cloudflare Images API.

To obtain a token, you can use the new `images/v1/batch_token` endpoint as shown in the example below.

```bash
curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/batch_token" \
--header "Authorization: Bearer <API_TOKEN>"


# Response:
{
  "result": {
    "token": "<BATCH_TOKEN>",
    "expiresAt": "2023-08-09T15:33:56.273411222Z"
  },
  "success": true,
  "errors": [],
  "messages": []
}
```

After getting your token, use it to make requests for:

* [Upload an image](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/create/) - `POST /images/v1`
* [Delete an image](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/delete/) - `DELETE /images/v1/{identifier}`
* [Image details](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/get/) - `GET /images/v1/{identifier}`
* [Update image](https://developers.cloudflare.com/api/resources/images/subresources/v1/methods/edit/) - `PATCH /images/v1/{identifier}`
* [List images V2](https://developers.cloudflare.com/api/resources/images/subresources/v2/methods/list/) - `GET /images/v2`
* [Direct upload V2](https://developers.cloudflare.com/api/resources/images/subresources/v2/subresources/direct_uploads/methods/create/) - `POST /images/v2/direct_upload`

These options use a different host and a different path with the same method, request, and response bodies.

```bash
curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v2" \
--header "Authorization: Bearer <API_TOKEN>"
```

```bash
curl "https://batch.imagedelivery.net/images/v1" \
--header "Authorization: Bearer <BATCH_TOKEN>"
```