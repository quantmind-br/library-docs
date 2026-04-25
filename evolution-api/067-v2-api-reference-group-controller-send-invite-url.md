---
title: Send Group Invite - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/send-invite-url
source: sitemap
fetched_at: 2026-04-12T18:50:25.574249856-03:00
rendered_js: false
word_count: 48
summary: This document demonstrates how to use the API endpoint for sending an invitation to a WhatsApp group, detailing required headers, request body parameters, and the expected response.
tags:
    - api
    - whatsapp
    - group-invite
    - post-request
    - sending-invitation
category: reference
---

```
curl --request POST \
  --url https://evolution-example/group/sendInvite/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "groupJid": "<string>",
  "description": "<string>",
  "numbers": [
    "<string>"
  ]
}
'

{
  "send": true,
  "inviteUrl": "https://chat.whatsapp.com/DgQvyfXzY01B6rGrpZpYze"
}
```

POST

/

group

/

sendInvite

/

{instance}

```
curl --request POST \
  --url https://evolution-example/group/sendInvite/{instance} \
  --header 'Content-Type: application/json' \
  --header 'apikey: <api-key>' \
  --data '
{
  "groupJid": "<string>",
  "description": "<string>",
  "numbers": [
    "<string>"
  ]
}
'

{
  "send": true,
  "inviteUrl": "https://chat.whatsapp.com/DgQvyfXzY01B6rGrpZpYze"
}
```

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Description to send with the invitation

Numbers to receive the invitation

#### Response

Indicates if the invite was sent successfully.

The URL for the WhatsApp group invite.

[Revoke Invite Code](https://doc.evolution-api.com/v2/api-reference/group-controller/revoke-invite-code)[Find Group by Invite Code](https://doc.evolution-api.com/v2/api-reference/group-controller/find-group-by-invite-code)