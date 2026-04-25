---
title: Connection State - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/instance-controller/connection-state
source: sitemap
fetched_at: 2026-04-12T18:50:09.659458819-03:00
rendered_js: false
word_count: 26
summary: This document provides the technical details for using a GET request to check the connection state of a specific instance via an API endpoint.
tags:
    - api-call
    - get-request
    - connection-state
    - instance-management
    - http-api
category: reference
---

```
curl --request GET \
  --url https://evolution-example/instance/connectionState/{instance} \
  --header 'apikey: <api-key>'

{
  "instance": {
    "instanceName": "teste-docs",
    "state": "open"
  }
}
```

GET

/

instance

/

connectionState

/

{instance}

```
curl --request GET \
  --url https://evolution-example/instance/connectionState/{instance} \
  --header 'apikey: <api-key>'

{
  "instance": {
    "instanceName": "teste-docs",
    "state": "open"
  }
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

Name of the instance to get status connect

#### Response

[Restart Instance](https://doc.evolution-api.com/v2/api-reference/instance-controller/restart-instance)[Logout Instance](https://doc.evolution-api.com/v2/api-reference/instance-controller/logout-instance)