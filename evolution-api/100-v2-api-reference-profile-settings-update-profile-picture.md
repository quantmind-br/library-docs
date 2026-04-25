---
title: Update Profile Picture - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/profile-settings/update-profile-picture
source: sitemap
fetched_at: 2026-04-12T18:47:02.068903525-03:00
rendered_js: false
word_count: 21
summary: This document provides the necessary cURL command structure for making a POST request to update a user's profile picture via an API endpoint.
tags:
    - api-call
    - post-request
    - update-profile-picture
    - curl
    - authentication
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/updateProfilePicture/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "picture": "<string>"
}
'

This response has no body data.
```

POST

/

chat

/

updateProfilePicture

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/updateProfilePicture/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "picture": "<string>"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

#### Response

[Update Profile Status](https://doc.evolution-api.com/v2/api-reference/profile-settings/update-profile-status)[Remove Profile Picture](https://doc.evolution-api.com/v2/api-reference/profile-settings/remove-profile-picture)