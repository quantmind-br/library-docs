---
title: Update Group Members - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/update-participant
source: sitemap
fetched_at: 2026-04-12T18:50:07.784482981-03:00
rendered_js: false
word_count: 36
summary: This document provides a cURL example and details the endpoint for updating group participants, outlining the required method, URL structure, headers, and request body options.
tags:
    - group-api
    - update-participant
    - curl-example
    - http-post
    - authorization
category: reference
---

```
curl --request POST \
  --url https://evolution-example/group/updateParticipant/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "action": "add",
  "participants": [
    "<string>"
  ]
}
'

This response has no body data.
```

POST

/

group

/

updateParticipant

/

{instance}

```
curl --request POST \
  --url https://evolution-example/group/updateParticipant/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "action": "add",
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

#### Query Parameters

#### Body

Available options:

`add`,

`remove`,

`promote`,

`demote`

Group members phone numbers with country code

#### Response

[Find Group Members](https://doc.evolution-api.com/v2/api-reference/group-controller/find-participants)[Update Group Setting](https://doc.evolution-api.com/v2/api-reference/group-controller/update-setting)