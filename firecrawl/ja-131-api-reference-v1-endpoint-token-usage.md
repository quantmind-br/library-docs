---
title: トークン使用量 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/token-usage
source: sitemap
fetched_at: 2026-03-23T07:12:21.886494-03:00
rendered_js: false
word_count: 26
summary: This document describes the API endpoint for retrieving the remaining token balance and billing period details for an authenticated team.
tags:
    - api-endpoint
    - token-usage
    - billing-information
    - firecrawl-api
    - authentication
category: api
---

認証済みのチームの残りトークン数を取得（Extract のみ）

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/token-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_tokens": 1000,
    "plan_tokens": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

認証済みのチームの残りトークン数を取得（Extract のみ）

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/team/token-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remaining_tokens": 1000,
    "plan_tokens": 500000,
    "billing_period_start": "2025-01-01T00:00:00Z",
    "billing_period_end": "2025-01-31T23:59:59Z"
  }
}
```

> 注記: 機能とパフォーマンスが向上した新しい [v2 版の API](https://docs.firecrawl.dev/ja/api-reference/endpoint/token-usage) が利用可能です。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### レスポンス