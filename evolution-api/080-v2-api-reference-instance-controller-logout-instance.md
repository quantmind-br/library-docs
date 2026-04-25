---
title: Logout Instance - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/instance-controller/logout-instance
source: sitemap
fetched_at: 2026-04-12T18:50:04.092529882-03:00
rendered_js: false
word_count: 34
summary: This documentation details the API endpoint and required steps to perform a DELETE request to log out a specified instance using an authorization key.
tags:
    - api-endpoint
    - logout
    - delete
    - instance-management
    - rest-api
    - curl
category: reference
---

```
curl --request DELETE \
  --url https://evolution-example/instance/logout/{instance} \
  --header 'apikey: <api-key>'

{
  "status": "SUCCESS",
  "error": false,
  "response": {
    "message": "Instance logged out"
  }
}
```

DELETE

/

instance

/

logout

/

{instance}

```
curl --request DELETE \
  --url https://evolution-example/instance/logout/{instance} \
  --header 'apikey: <api-key>'

{
  "status": "SUCCESS",
  "error": false,
  "response": {
    "message": "Instance logged out"
  }
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

Name of the instance to logout

#### Response

The status of the response.

Indicates whether an error occurred.

[Connection State](https://doc.evolution-api.com/v2/api-reference/instance-controller/connection-state)[Delete Instance](https://doc.evolution-api.com/v2/api-reference/instance-controller/delete-instance)