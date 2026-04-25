---
title: Change Evolution Bot status - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evolution/change-status-session
source: sitemap
fetched_at: 2026-04-12T18:49:17.637823346-03:00
rendered_js: false
word_count: 28
summary: This document provides the necessary cURL command and structure for making a POST request to change the status of an Evolution Bot instance.
tags:
    - rest-api
    - post-request
    - status-update
    - curl-command
    - bot-management
category: reference
---

```
curl --request POST \
  --url https://evolution-example/evolutionBot/changeStatus/{instance} \
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

evolutionBot

/

changeStatus

/

{instance}

```
curl --request POST \
  --url https://evolution-example/evolutionBot/changeStatus/{instance} \
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

[Find Settings Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/find-settings)[Fetch Evolution Bot Session](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/fetch-session)