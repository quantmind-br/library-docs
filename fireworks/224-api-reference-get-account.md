---
title: Get Account - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/get-account
source: sitemap
fetched_at: 2026-04-27T20:14:23.068242424-03:00
rendered_js: false
word_count: 10
summary: This document outlines the structure of an email object, detailing various attributes such as name, account type, status codes, and notification settings.
tags:
    - email-object
    - user-data
    - notification-settings
    - account-type
    - api-structure
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# Get Account

Response schema for account details.

```json
{
  "email": "<string>",
  "name": "<string>",
  "displayName": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "accountType": "ACCOUNT_TYPE_UNSPECIFIED",
  "state": "STATE_UNSPECIFIED",
  "status": {
    "code": "OK",
    "message": "<string>"
  },
  "suspendState": "UNSUSPENDED",
  "updateTime": "2023-11-07T05:31:56Z",
  "notificationSettings": {
    "monthlySpendThresholds": [
      {
        "currencyCode": "<string>",
        "units": "<string>",
        "nanos": 123
      }
    ]
  }
}
```

#api-reference #accounts
