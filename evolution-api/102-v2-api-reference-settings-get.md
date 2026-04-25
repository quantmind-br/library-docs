---
title: Find Settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/settings/get
source: sitemap
fetched_at: 2026-04-12T18:47:03.685415088-03:00
rendered_js: false
word_count: 66
summary: This document details the GET endpoint for retrieving settings for a specific instance via an API call, outlining required headers and interpreting the structure of the returned configuration data.
tags:
    - settings-api
    - instance-retrieval
    - get-request
    - authorization-key
    - api-endpoint
category: reference
---

GET

/

settings

/

find

/

{instance}

```
curl --request GET \
  --url https://evolution-example/settings/find/{instance} \
  --header 'apikey: <api-key>'

{
  "reject_call": true,
  "groups_ignore": true,
  "always_online": true,
  "read_messages": true,
  "read_status": true,
  "sync_full_history": false
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

Name of the instance to get settings

#### Response

Indicates whether to reject incoming calls.

Indicates whether to ignore group messages.

Indicates whether to always keep the instance online.

Indicates whether to mark messages as read.

Indicates whether to read status updates.

Indicates whether to synchronize full message history.

[Set Settings](https://doc.evolution-api.com/v2/api-reference/settings/set)[Send Plain Text](https://doc.evolution-api.com/v2/api-reference/message-controller/send-text)