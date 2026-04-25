---
title: Change status OpenAI - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/change-status
source: sitemap
fetched_at: 2026-04-12T18:48:44.3347331-03:00
rendered_js: false
word_count: 71
summary: This document describes the endpoint and usage details for programmatically changing the status of an OpenAI bot instance using a POST request.
tags:
    - api-endpoint
    - change-status
    - openai-bot
    - rest-api
    - post-request
category: reference
---

```
curl --request POST \
  --url https://evolution-example/openai/changeStatus/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "remoteJid": "<string>",
  "status": "opened"
}
'

{
  "success": true,
  "message": "<string>"
}
```

POST

/

openai

/

changeStatus

/

{instance}

```
curl --request POST \
  --url https://evolution-example/openai/changeStatus/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "remoteJid": "<string>",
  "status": "opened"
}
'

{
  "success": true,
  "message": "<string>"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Body for changing the status of the OpenAI bot

The JID (Jabber ID) of the remote contact

Status of the bot instance. Possible values: 'opened', 'paused', 'closed'

Available options:

`opened`,

`paused`,

`closed`

#### Response

Successfully changed the bot status

Indicates if the status change was successful

Details about the status change operation

[Find settings OpenAI](https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-settings)[Find sessions OpenAI](https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-session)