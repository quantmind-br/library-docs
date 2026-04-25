---
title: Update Group Description - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/update-group-description
source: sitemap
fetched_at: 2026-04-12T18:50:15.457823166-03:00
rendered_js: false
word_count: 23
summary: This documentation provides the cURL request details and structure for making a POST request to update a group's description via an API endpoint.
tags:
    - api-call
    - post-request
    - group-update
    - rest-api
    - http-headers
category: reference
---

```
curl --request POST \
  --url https://evolution-example/group/updateGroupDescription/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "description": "<string>"
}
'

This response has no body data.
```

POST

/

group

/

updateGroupDescription

/

{instance}

```
curl --request POST \
  --url https://evolution-example/group/updateGroupDescription/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "description": "<string>"
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

[Update Group Subject](https://doc.evolution-api.com/v2/api-reference/group-controller/update-group-subject)[Fetch Invite Code](https://doc.evolution-api.com/v2/api-reference/group-controller/fetch-invite-code)