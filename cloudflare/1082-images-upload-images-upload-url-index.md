---
title: Upload via URL · Cloudflare Images docs
url: https://developers.cloudflare.com/images/upload-images/upload-url/index.md
source: llms
fetched_at: 2026-01-24T15:15:54.022545116-03:00
rendered_js: false
word_count: 109
summary: This document explains how to use the Cloudflare Images API to upload images via a URL, including request formatting and response structure.
tags:
    - cloudflare-images
    - api-upload
    - url-upload
    - image-management
    - rest-api
category: api
---

Before you upload an image, check the list of [supported formats and dimensions](https://developers.cloudflare.com/images/upload-images/#supported-image-formats) to confirm your image will be accepted.

You can use the Images API to use a URL of an image instead of uploading the data.

Make a `POST` request using the example below as reference. Keep in mind that the `--form 'file=<FILE>'` and `--form 'url=<URL>'` fields are mutually exclusive.

Note

The `metadata` included in the request is never shared with end users.

```bash
curl --request POST \
https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1 \
--header "Authorization: Bearer <API_TOKEN>" \
--form 'url=https://[user:password@]example.com/<PATH_TO_IMAGE>' \
--form 'metadata={"key":"value"}' \
--form 'requireSignedURLs=false'
```

After successfully uploading the image, you will receive a response similar to the example below.

```json
{
    "result": {
        "id": "2cdc28f0-017a-49c4-9ed7-87056c83901",
        "filename": "image.jpeg",
        "metadata": {
            "key": "value"
        },
        "uploaded": "2022-01-31T16:39:28.458Z",
        "requireSignedURLs": false,
        "variants": [
            "https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/public",
            "https://imagedelivery.net/Vi7wi5KSItxGFsWRG2Us6Q/2cdc28f0-017a-49c4-9ed7-87056c83901/thumbnail"
        ]
    },
    "success": true,
    "errors": [],
    "messages": []
}
```

If your origin server returns an error while fetching the images, the API response will return a 4xx error.