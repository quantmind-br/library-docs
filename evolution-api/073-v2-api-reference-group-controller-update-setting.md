---
title: Update Group Setting - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/update-setting
source: sitemap
fetched_at: 2026-04-12T18:50:11.709116443-03:00
rendered_js: false
word_count: 58
summary: This document provides instructions for making a POST request to update group settings via an API endpoint, detailing required headers, path parameters, and accepted body actions.
tags:
    - api-call
    - group-settings
    - post-request
    - authorization
    - http-method
category: reference
---

```
curl --request POST \
  --url https://evolution-example/group/updateSetting/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "action": "announcement"
}
'

This response has no body data.
```

POST

/

group

/

updateSetting

/

{instance}

```
curl --request POST \
  --url https://evolution-example/group/updateSetting/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "action": "announcement"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Query Parameters

#### Body

Group setting (`announcement` = only admins can send messages; `not_announcement` = everyone can send messages; `locked` = only admins can edit group settings; `unlocked` = everyone can edit group settings

Available options:

`announcement`,

`not_announcement`,

`locked`,

`unlocked`

#### Response

[Update Group Members](https://doc.evolution-api.com/v2/api-reference/group-controller/update-participant)[Toggle Ephemeral](https://doc.evolution-api.com/v2/api-reference/group-controller/toggle-ephemeral)