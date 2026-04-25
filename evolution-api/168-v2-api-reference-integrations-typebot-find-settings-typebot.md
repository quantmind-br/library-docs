---
title: Fetch Typebot Settings - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/typebot/find-settings-typebot
source: sitemap
fetched_at: 2026-04-12T18:47:59.593107835-03:00
rendered_js: false
word_count: 47
summary: This document serves as the main documentation hub for the Evolution API, providing access points to guides, API reference materials, and specific endpoint details like fetching Typebot settings.
tags:
    - api-documentation
    - evolution-api
    - get-started
    - api-reference
    - curl-examples
category: guide
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find Typebot

```
curl --request GET \
  --url https://evolution-example/typebot/fetchSettings/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

GET

/

typebot

/

fetchSettings

/

{instance}

Find Typebot

```
curl --request GET \
  --url https://evolution-example/typebot/fetchSettings/{instance} \
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

[Settings Typebot](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/settings-typebot)[Create OpenIA Bot](https://doc.evolution-api.com/v2/api-reference/integrations/openai/create-bot)