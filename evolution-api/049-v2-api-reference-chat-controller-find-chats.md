---
title: Find Chats - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/chat-controller/find-chats
source: sitemap
fetched_at: 2026-04-12T18:51:02.129451669-03:00
rendered_js: false
word_count: 46
summary: This documentation page serves as a gateway to the Evolution API, providing entry points for developers to begin using its functionalities like finding chats.
tags:
    - api
    - documentation
    - chat-finding
    - rest-api
    - get-started
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Find Chats

```
curl --request POST \
  --url https://evolution-example/chat/findChats/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

POST

/

chat

/

findChats

/

{instance}

Find Chats

```
curl --request POST \
  --url https://evolution-example/chat/findChats/{instance} \
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

Name instance

#### Response

200 - undefined

[Find Status Message](https://doc.evolution-api.com/v2/api-reference/chat-controller/find-status-message)[Fetch Business Profile](https://doc.evolution-api.com/v2/api-reference/profile-settings/fetch-business-profile)