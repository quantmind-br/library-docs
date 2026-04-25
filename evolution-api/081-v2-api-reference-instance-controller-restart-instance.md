---
title: Restart Instance - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/instance-controller/restart-instance
source: sitemap
fetched_at: 2026-04-12T18:49:53.797159244-03:00
rendered_js: false
word_count: 24
summary: This document details the API endpoint and required parameters for restarting a specific instance using an HTTP PUT request.
tags:
    - api-endpoint
    - instance-restart
    - http-put
    - api-key
    - path-parameter
category: reference
---

```
curl --request PUT \
  --url https://evolution-example/instance/restart/{instance} \
  --header 'apikey: <api-key>'

{
  "instance": {
    "instanceName": "teste-docs",
    "state": "open"
  }
}
```

PUT

/

instance

/

restart

/

{instance}

```
curl --request PUT \
  --url https://evolution-example/instance/restart/{instance} \
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

Name of the instance to restart

#### Response

[Instance Connect](https://doc.evolution-api.com/v2/api-reference/instance-controller/instance-connect)[Connection State](https://doc.evolution-api.com/v2/api-reference/instance-controller/connection-state)