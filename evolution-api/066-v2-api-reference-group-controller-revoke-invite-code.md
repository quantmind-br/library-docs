---
title: Revoke Invite Code - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/revoke-invite-code
source: sitemap
fetched_at: 2026-04-12T18:50:31.422240142-03:00
rendered_js: false
word_count: 61
summary: This page serves as the main documentation hub for the Evolution API, providing access to guides and specific reference points for various functionalities.
tags:
    - evolution-api
    - api-reference
    - group-management
    - authorization
    - curl
category: guide
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Fetch Group Invite Code

```
curl --request POST \
  --url https://evolution-example/group/revokeInviteCode/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

POST

/

group

/

revokeInviteCode

/

{instance}

Fetch Group Invite Code

```
curl --request POST \
  --url https://evolution-example/group/revokeInviteCode/{instance} \
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

#### Query Parameters

[​](#parameter-group-jid)

groupJid

string

required

Group remote JID

#### Response

200 - undefined

[Fetch Invite Code](https://doc.evolution-api.com/v2/api-reference/group-controller/fetch-invite-code)[Send Group Invite](https://doc.evolution-api.com/v2/api-reference/group-controller/send-invite-url)