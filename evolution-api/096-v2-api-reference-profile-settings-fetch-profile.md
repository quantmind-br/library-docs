---
title: Fetch Profile - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/profile-settings/fetch-profile
source: sitemap
fetched_at: 2026-04-12T18:47:21.517615427-03:00
rendered_js: false
word_count: 26
summary: This document provides the details for an API endpoint that allows fetching a business profile using a POST request and requires specific headers and body parameters.
tags:
    - api-endpoint
    - fetch-profile
    - rest-api
    - curl-command
    - authorization-header
category: reference
---

```
curl --request POST \
  --url https://evolution-example/chat/fetchProfile/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>"
}
'

This response has no body data.
```

POST

/

chat

/

fetchProfile

/

{instance}

```
curl --request POST \
  --url https://evolution-example/chat/fetchProfile/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "number": "<string>"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Phone number with country code

#### Response

[Fetch Business Profile](https://doc.evolution-api.com/v2/api-reference/profile-settings/fetch-business-profile)[Update Profile Name](https://doc.evolution-api.com/v2/api-reference/profile-settings/update-profile-name)