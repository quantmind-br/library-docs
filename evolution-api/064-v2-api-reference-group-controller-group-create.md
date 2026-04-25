---
title: Create Group - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/group-create
source: sitemap
fetched_at: 2026-04-12T18:50:37.400059198-03:00
rendered_js: false
word_count: 21
summary: This document provides the cURL command structure for making a POST request to create a group resource at a specified instance, detailing the required headers and JSON body payload.
tags:
    - curl
    - api-request
    - group-creation
    - post-method
    - json-payload
category: reference
---

```
curl --request POST \
  --url https://evolution-example/group/create/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "subject": {},
  "description": "<string>",
  "participants": [
    "<string>"
  ]
}
'

This response has no body data.

curl --request POST \
  --url https://evolution-example/group/create/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "subject": {},
  "description": "<string>",
  "participants": [
    "<string>"
  ]
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Group members phone numbers with country code

#### Response

[Update Privacy Settings](https://doc.evolution-api.com/v2/api-reference/profile-settings/update-privacy-settings)[Update Group Picture](https://doc.evolution-api.com/v2/api-reference/group-controller/update-group-picture)