---
title: Fetch Instances - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/instance-controller/fetch-instances
source: sitemap
fetched_at: 2026-04-12T18:50:19.724472837-03:00
rendered_js: false
word_count: 0
summary: This document provides a structured collection of data instances, detailing various settings and configurations for WhatsApp integrations.
tags:
    - api-data
    - whatsapp-integration
    - instance-details
    - webhook-url
    - configuration
category: reference
---

```
[
  {
    "instance": {
      "instanceName": "example-name",
      "instanceId": "421a4121-a3d9-40cc-a8db-c3a1df353126",
      "owner": "553198296801@s.whatsapp.net",
      "profileName": "Guilherme Gomes",
      "profilePictureUrl": null,
      "profileStatus": "This is the profile status.",
      "status": "open",
      "serverUrl": "https://example.evolution-api.com",
      "apikey": "B3844804-481D-47A4-B69C-F14B4206EB56",
      "integration": {
        "integration": "WHATSAPP-BAILEYS",
        "webhook_wa_business": "https://example.evolution-api.com/webhook/whatsapp/db5e11d3-ded5-4d91-b3fb-48272688f206"
      }
    }
  },
  {
    "instance": {
      "instanceName": "teste-docs",
      "instanceId": "af6c5b7c-ee27-4f94-9ea8-192393746ddd",
      "status": "close",
      "serverUrl": "https://example.evolution-api.com",
      "apikey": "123456",
      "integration": {
        "token": "123456",
        "webhook_wa_business": "https://example.evolution-api.com/webhook/whatsapp/teste-docs"
      }
    }
  }
]
```