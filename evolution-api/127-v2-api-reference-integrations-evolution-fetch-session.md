---
title: Fetch Evolution Bot Session - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evolution/fetch-session
source: sitemap
fetched_at: 2026-04-12T18:49:11.657931406-03:00
rendered_js: false
word_count: 23
summary: This document provides the cURL command and endpoint structure for fetching sessions associated with a specific Evolution Bot instance.
tags:
    - curl
    - api-call
    - fetch-sessions
    - evolution-bot
    - endpoint
category: reference
---

```
curl --request GET \
  --url https://evolution-example/evolutionBot/fetchSessions/:evolutionBotId/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

evolutionBot

/

fetchSessions

/

:evolutionBotId

/

{instance}

```
curl --request GET \
  --url https://evolution-example/evolutionBot/fetchSessions/:evolutionBotId/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Response

[Change Evolution Bot status](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/change-status-session)[Create Dify Bot](https://doc.evolution-api.com/v2/api-reference/integrations/dify/create-dify)