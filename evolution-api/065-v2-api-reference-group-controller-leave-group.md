---
title: Leave Group - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/leave-group
source: sitemap
fetched_at: 2026-04-12T18:50:29.566616658-03:00
rendered_js: false
word_count: 55
summary: This documentation page provides a reference for using the API endpoint to leave a group, detailing the necessary request structure, required headers like the apikey, and path parameters.
tags:
    - api-reference
    - group-management
    - delete-request
    - authorization
    - rest-api
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Leave Group

```
curl --request DELETE \
  --url https://evolution-example/group/leaveGroup/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

DELETE

/

group

/

leaveGroup

/

{instance}

Leave Group

```
curl --request DELETE \
  --url https://evolution-example/group/leaveGroup/{instance} \
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

[Toggle Ephemeral](https://doc.evolution-api.com/v2/api-reference/group-controller/toggle-ephemeral)[Create Typebot](https://doc.evolution-api.com/v2/api-reference/integrations/typebot/set-typebot)