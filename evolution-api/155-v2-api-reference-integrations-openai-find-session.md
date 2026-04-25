---
title: Find sessions OpenAI - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/openai/find-session
source: sitemap
fetched_at: 2026-04-12T18:48:24.630139927-03:00
rendered_js: false
word_count: 39
summary: This document provides a cURL example and endpoint details for fetching sessions associated with a specific OpenAI bot instance.
tags:
    - openai
    - fetch-sessions
    - api-endpoint
    - bot-instance
    - rest-api
category: reference
---

Fetch sessions of the OpenAI bot instance

```
curl --request GET \
  --url https://evolution-example/openai/fetchSessions/:openaiBotId/{instance} \
  --header 'apikey: <api-key>'
```

GET

/

openai

/

fetchSessions

/

:openaiBotId

/

{instance}

Fetch sessions of the OpenAI bot instance

```
curl --request GET \
  --url https://evolution-example/openai/fetchSessions/:openaiBotId/{instance} \
  --header 'apikey: <api-key>'
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Response

Successfully fetched sessions

[Change status OpenAI](https://doc.evolution-api.com/v2/api-reference/integrations/openai/change-status)[Create Evolution Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/create-bot)