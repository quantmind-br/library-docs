---
title: Toggle Ephemeral - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/toggle-ephemeral
source: sitemap
fetched_at: 2026-04-12T18:50:12.123539661-03:00
rendered_js: false
word_count: 36
summary: This document provides the endpoint details and cURL example for toggling ephemeral group messages within an API structure.
tags:
    - group-messaging
    - ephemeral
    - api-call
    - post-request
    - instance-parameter
    - expiration
category: reference
---

Toggle Ephemeral Group Messages

```
curl --request POST \
  --url https://evolution-example/group/toggleEphemeral/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "expiration": 123
}
'

This response has no body data.
```

POST

/

group

/

toggleEphemeral

/

{instance}

Toggle Ephemeral Group Messages

```
curl --request POST \
  --url https://evolution-example/group/toggleEphemeral/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "expiration": 123
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Query Parameters

#### Body

Time to expire message (in seconds)

#### Response

[Update Group Setting](https://doc.evolution-api.com/v2/api-reference/group-controller/update-setting)[Leave Group](https://doc.evolution-api.com/v2/api-reference/group-controller/leave-group)