---
title: Update Group Picture - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/update-group-picture
source: sitemap
fetched_at: 2026-04-12T18:50:22.210686522-03:00
rendered_js: false
word_count: 27
summary: This document demonstrates the required cURL command structure for updating a group's picture via a POST request to the updateGroupPicture endpoint.
tags:
    - rest-api
    - post-request
    - curl-example
    - group-update
    - http-method
category: reference
---

```
curl --request POST \
  --url https://evolution-example/group/updateGroupPicture/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "image": "<string>"
}
'

This response has no body data.
```

POST

/

group

/

updateGroupPicture

/

{instance}

```
curl --request POST \
  --url https://evolution-example/group/updateGroupPicture/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "image": "<string>"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Query Parameters

#### Body

New profile picture image URL

#### Response

[Create Group](https://doc.evolution-api.com/v2/api-reference/group-controller/group-create)[Update Group Subject](https://doc.evolution-api.com/v2/api-reference/group-controller/update-group-subject)