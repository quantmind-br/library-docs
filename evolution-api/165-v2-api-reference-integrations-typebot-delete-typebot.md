---
title: Delete Typebot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/typebot/delete-typebot
source: sitemap
fetched_at: 2026-04-12T18:47:55.751427287-03:00
rendered_js: false
word_count: 57
summary: This documentation provides the reference for using a DELETE request to delete a typebot status via an API endpoint.
tags:
    - delete-request
    - api-reference
    - typebot
    - authorization
    - http-methods
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Delete Status

```
curl --request DELETE \
  --url https://evolution-example/typebot/delete/:typebotId/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

DELETE

/

typebot

/

delete

/

:typebotId

/

{instance}

Delete Status

```
curl --request DELETE \
  --url https://evolution-example/typebot/delete/:typebotId/{instance} \
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

[Update Typebot](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/update-typebot)[Change Session Status](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/change-session-status)