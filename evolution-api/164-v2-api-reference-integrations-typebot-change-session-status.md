---
title: Change Session Status - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/typebot/change-session-status
source: sitemap
fetched_at: 2026-04-12T18:48:03.629877878-03:00
rendered_js: false
word_count: 26
summary: This document provides the cURL command and details for using the POST method to change the status of a Typebot instance via an API endpoint.
tags:
    - api-endpoint
    - post-request
    - typebot-status
    - authorization
    - rest-api
category: reference
---

```
curl --request POST \
  --url https://evolution-example/typebot/changeStatus/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "remoteJid": "<string>",
  "status": "<string>"
}
'

This response has no body data.
```

POST

/

typebot

/

changeStatus

/

{instance}

```
curl --request POST \
  --url https://evolution-example/typebot/changeStatus/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "remoteJid": "<string>",
  "status": "<string>"
}
'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Typebot status, types: opened, paused, closed

#### Response

[Delete Typebot](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/delete-typebot)[Fetch Session Typebot](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/fetch-session)