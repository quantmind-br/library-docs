---
title: Delete Instance - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/instance-controller/delete-instance
source: sitemap
fetched_at: 2026-04-12T18:50:17.573042394-03:00
rendered_js: false
word_count: 34
summary: This document details the API endpoint for deleting a specified instance, including the required DELETE method, URL structure, necessary headers, and expected successful response format.
tags:
    - delete
    - api-endpoint
    - instance-management
    - curl
    - authorization
category: reference
---

```
curl --request DELETE \
  --url https://evolution-example/instance/delete/{instance} \
  --header 'apikey: <api-key>'

{
  "status": "SUCCESS",
  "error": false,
  "response": {
    "message": "Instance deleted"
  }
}
```

DELETE

/

instance

/

delete

/

{instance}

```
curl --request DELETE \
  --url https://evolution-example/instance/delete/{instance} \
  --header 'apikey: <api-key>'

{
  "status": "SUCCESS",
  "error": false,
  "response": {
    "message": "Instance deleted"
  }
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

Name of the instance to delete

#### Response

The status of the response.

Indicates whether an error occurred.

[Logout Instance](https://doc.evolution-api.com/v2/api-reference/instance-controller/logout-instance)[Set Presence](https://doc.evolution-api.com/v2/api-reference/instance-controller/set-presence)