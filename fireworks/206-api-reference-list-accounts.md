---
title: List Accounts - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/list-accounts
source: sitemap
fetched_at: 2026-04-27T20:13:58.966934724-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - account-list
    - user-data
    - json-schema
    - pagination
    - notification-settings
category: reference
word_count: 60
---
# List Accounts

`GET /accounts` — Returns a paginated list of accounts in the organization.

## Response Schema

```json
{
  "accounts": [
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
  ],
  "nextPageToken": "<string>",
  "totalSize": 123
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `accounts` | array | List of account objects. |
| `nextPageToken` | string | Token for fetching the next page. |
| `totalSize` | integer | Total number of accounts. |