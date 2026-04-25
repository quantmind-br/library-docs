---
title: Fetch Invite Code - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/fetch-invite-code
source: sitemap
fetched_at: 2026-04-12T18:50:39.785185703-03:00
rendered_js: false
word_count: 36
summary: This document illustrates the endpoint and method for retrieving a WhatsApp group's invite URL and associated invite code using an API request.
tags:
    - whatsapp
    - group-invitation
    - api-endpoint
    - get-request
    - invite-code
category: reference
---

```
curl --request GET \
  --url https://evolution-example/group/inviteCode/{instance} \
  --header 'apikey: <api-key>'

{
  "inviteUrl": "https://chat.whatsapp.com/DgQvyfXzY01B6rGrpZpYze",
  "inviteCode": "DgQvyfXzY01B6rGrpZpYze"
}
```

GET

/

group

/

inviteCode

/

{instance}

```
curl --request GET \
  --url https://evolution-example/group/inviteCode/{instance} \
  --header 'apikey: <api-key>'

{
  "inviteUrl": "https://chat.whatsapp.com/DgQvyfXzY01B6rGrpZpYze",
  "inviteCode": "DgQvyfXzY01B6rGrpZpYze"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Query Parameters

#### Response

The URL for the WhatsApp group invite.

The code for the WhatsApp group invite.

[Update Group Description](https://doc.evolution-api.com/v2/api-reference/group-controller/update-group-description)[Revoke Invite Code](https://doc.evolution-api.com/v2/api-reference/group-controller/revoke-invite-code)