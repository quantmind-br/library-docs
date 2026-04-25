---
title: Instance Connect - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/instance-controller/instance-connect
source: sitemap
fetched_at: 2026-04-12T18:49:59.465263232-03:00
rendered_js: false
word_count: 72
summary: This documentation details the process and required parameters for using a GET request to connect to a specific instance endpoint via an API.
tags:
    - api
    - get-request
    - instance-connection
    - authorization
    - path-parameters
category: reference
---

```
curl --request GET \
  --url https://evolution-example/instance/connect/{instance} \
  --header 'apikey: <api-key>'

{
  "pairingCode": "WZYEH1YY",
  "code": "2@y8eK+bjtEjUWy9/FOM...",
  "count": 1
}
```

GET

/

instance

/

connect

/

{instance}

```
curl --request GET \
  --url https://evolution-example/instance/connect/{instance} \
  --header 'apikey: <api-key>'

{
  "pairingCode": "WZYEH1YY",
  "code": "2@y8eK+bjtEjUWy9/FOM...",
  "count": 1
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

Name of the instance to connect

#### Query Parameters

Phone number (with country code) to be connected

#### Response

The unique code used for pairing a device or account.

A specific code associated with the pairing process. This may include tokens or other identifiers.

The count or number of attempts or instances related to the pairing process.

[Fetch Instances](https://doc.evolution-api.com/v2/api-reference/instance-controller/fetch-instances)[Restart Instance](https://doc.evolution-api.com/v2/api-reference/instance-controller/restart-instance)