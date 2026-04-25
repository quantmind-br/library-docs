---
title: Update Profile Name - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/profile-settings/update-profile-name
source: sitemap
fetched_at: 2026-04-12T18:47:09.559523995-03:00
rendered_js: false
word_count: 20
summary: This document details the cURL command necessary to update a user's profile name via an API endpoint, requiring authentication and sending a JSON payload.
tags:
    - api-call
    - update-profile
    - http-request
    - curl-example
    - rest-api
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/updateProfileName/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "name": "<string>"
}
'

This response has no body data.
```

POST

/

chat

/

updateProfileName

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/updateProfileName/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "name": "<string>"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

#### Response

[Fetch Profile](https://doc.evolution-api.com/v2/api-reference/profile-settings/fetch-profile)[Update Profile Status](https://doc.evolution-api.com/v2/api-reference/profile-settings/update-profile-status)