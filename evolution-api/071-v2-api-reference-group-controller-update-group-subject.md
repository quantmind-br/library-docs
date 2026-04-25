---
title: Update Group Subject - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/update-group-subject
source: sitemap
fetched_at: 2026-04-12T18:50:21.836610351-03:00
rendered_js: false
word_count: 23
summary: This document illustrates how to use a cURL command to make a POST request to update the subject of a specific group within an API endpoint.
tags:
    - api-call
    - post-request
    - group-update
    - curl
    - http-methods
category: reference
---

```
curl --request POST \
  --url https://evolution-example/group/updateGroupSubject/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "subject": "<string>"
}
'

This response has no body data.
```

POST

/

group

/

updateGroupSubject

/

{instance}

```
curl --request POST \
  --url https://evolution-example/group/updateGroupSubject/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "subject": "<string>"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Query Parameters

#### Body

#### Response

[Update Group Picture](https://doc.evolution-api.com/v2/api-reference/group-controller/update-group-picture)[Update Group Description](https://doc.evolution-api.com/v2/api-reference/group-controller/update-group-description)