---
title: Find Settings Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evolution/find-settings
source: sitemap
fetched_at: 2026-04-12T18:49:13.521851036-03:00
rendered_js: false
word_count: 41
summary: This document details how to use the GET method on the fetchSettings endpoint for EvoBot, requiring an API key in the header and an instance name as a path parameter.
tags:
    - api-reference
    - get-request
    - evolutionbot
    - fetchsettings
    - api-key
    - path-parameter
category: reference
---

Find EvoBot

```
curl --request GET \
  --url https://evolution-example/evolutionBot/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

evolutionBot

/

fetchSettings

/

{instance}

Find EvoBot

```
curl --request GET \
  --url https://evolution-example/evolutionBot/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

#### Authorizations

[​](#authorization-apikey)

apikey

string

header

required

Your authorization key header

#### Path Parameters

[​](#parameter-instance)

instance

string

required

Name of the instance

#### Response

200 - undefined

[Set Settings Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/set-settings)[Change Evolution Bot status](https://doc.evolution-api.com/v2/api-reference/integrations/evolution/change-status-session)