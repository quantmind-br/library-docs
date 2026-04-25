---
title: Update Profile Status - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/profile-settings/update-profile-status
source: sitemap
fetched_at: 2026-04-12T18:46:56.537953303-03:00
rendered_js: false
word_count: 21
summary: This document illustrates how to use a POST request via cURL command line to update a user's profile status at the specified API endpoint.
tags:
    - rest-api
    - post-request
    - update-status
    - curl-command
    - api-endpoint
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/updateProfileStatus/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "status": "<string>"
}
'

This response has no body data.
```

POST

/

chat

/

updateProfileStatus

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/updateProfileStatus/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "status": "<string>"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

#### Response

[Update Profile Name](https://doc.evolution-api.com/v2/api-reference/profile-settings/update-profile-name)[Update Profile Picture](https://doc.evolution-api.com/v2/api-reference/profile-settings/update-profile-picture)