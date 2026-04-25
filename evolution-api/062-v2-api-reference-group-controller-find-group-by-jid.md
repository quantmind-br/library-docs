---
title: Find Group by JID - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/group-controller/find-group-by-jid
source: sitemap
fetched_at: 2026-04-12T18:50:35.582598912-03:00
rendered_js: false
word_count: 0
summary: This document provides a JSON structure detailing the metadata for a WhatsApp group, including its owner, participants, and administrative status.
tags:
    - whatsapp-group
    - metadata
    - json-structure
    - user-data
category: reference
---

```
{
  "id": "120363295648424210@g.us",
  "subject": "Example Group",
  "subjectOwner": "553198296801@s.whatsapp.net",
  "subjectTime": 1714769954,
  "pictureUrl": null,
  "size": 1,
  "creation": 1714769954,
  "owner": "553198296801@s.whatsapp.net",
  "desc": "optional",
  "descId": "BAE57E16498982ED",
  "restrict": false,
  "announce": false,
  "participants": [
    {
      "id": "553198296801@s.whatsapp.net",
      "admin": "superadmin"
    }
  ]
}
```