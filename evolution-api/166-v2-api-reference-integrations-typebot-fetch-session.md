---
title: Fetch Session Typebot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/typebot/fetch-session
source: sitemap
fetched_at: 2026-04-12T18:47:51.3983443-03:00
rendered_js: false
word_count: 59
summary: This documentation provides an endpoint reference for the Evolution API, detailing how to fetch sessions associated with a specific typebot using a GET request.
tags:
    - api-documentation
    - session-fetching
    - typebot-integration
    - rest-api
    - authorization
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find session typebot

```
curl --request GET \
  --url https://evolution-example/typebot/fetchSessions/:typebotId/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

typebot

/

fetchSessions

/

:typebotId

/

{instance}

Find session typebot

```
curl --request GET \
  --url https://evolution-example/typebot/fetchSessions/:typebotId/{instance} \
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

[​](#parameter-typebot-id)

typebotId

string

required

ID of the typebot

#### Response

200 - undefined

[Change Session Status](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/change-session-status)[Settings Typebot](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/settings-typebot)