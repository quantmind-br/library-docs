---
title: Fetch Typebot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/typebot/fetch-typebot
source: sitemap
fetched_at: 2026-04-12T18:47:56.196414248-03:00
rendered_js: false
word_count: 56
summary: This documentation page serves as the main entry point for the Evolution API, providing links to resources such as API references and getting started guides.
tags:
    - evolution-api
    - api-documentation
    - get-started
    - api-reference
category: guide
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find Typebot

```
curl --request GET \
  --url https://evolution-example/typebot/fetch/:typebotId/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

typebot

/

fetch

/

:typebotId

/

{instance}

Find Typebot

```
curl --request GET \
  --url https://evolution-example/typebot/fetch/:typebotId/{instance} \
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

[Find Typebot](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/find-typebot)[Update Typebot](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/update-typebot)