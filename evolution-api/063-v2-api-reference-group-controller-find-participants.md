---
title: Find Group Members - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/find-participants
source: sitemap
fetched_at: 2026-04-12T18:50:41.718935278-03:00
rendered_js: false
word_count: 28
summary: This document details the API endpoint and method for retrieving a list of participants belonging to a specific group instance.
tags:
    - api-endpoint
    - group-participants
    - get-request
    - authorization
    - rest-api
category: reference
---

```
curl --request GET \
  --url https://evolution-example/group/participants/{instance} \
  --header 'apikey: <api-key>'

{
  "participants": [
    {
      "id": "553198296801@s.whatsapp.net",
      "admin": "superadmin"
    }
  ]
}
```

GET

/

group

/

participants

/

{instance}

```
curl --request GET \
  --url https://evolution-example/group/participants/{instance} \
  --header 'apikey: <api-key>'

{
  "participants": [
    {
      "id": "553198296801@s.whatsapp.net",
      "admin": "superadmin"
    }
  ]
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Query Parameters

#### Response

List of participants in the group.

[Fetch All Groups](https://doc.evolution-api.com/v2/api-reference/group-controller/fetch-all-groups)[Update Group Members](https://doc.evolution-api.com/v2/api-reference/group-controller/update-participant)