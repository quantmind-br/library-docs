---
title: トークン使用量 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/token-usage
source: sitemap
fetched_at: 2026-03-23T07:13:07.511596-03:00
rendered_js: false
word_count: 27
summary: This document provides the API specification for retrieving the remaining token balance and plan usage details for an authenticated Firecrawl team.
tags:
    - api-reference
    - token-usage
    - authentication
    - billing-information
    - extract-service
category: api
---

認証済みのチームの残りトークン数を取得（Extract 専用）

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/token-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remainingTokens": 1000,
    "planTokens": 500000,
    "billingPeriodStart": "2025-01-01T00:00:00Z",
    "billingPeriodEnd": "2025-01-31T23:59:59Z"
  }
}
```

認証済みのチームの残りトークン数を取得（Extract 専用）

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/token-usage \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {
    "remainingTokens": 1000,
    "planTokens": 500000,
    "billingPeriodStart": "2025-01-01T00:00:00Z",
    "billingPeriodEnd": "2025-01-31T23:59:59Z"
  }
}
```

課金体系を見直し、Extract も他のすべてのエンドポイントと同様にクレジット制になりました。1クレジットは15トークンに相当します。報告されるトークン使用量には、すべてのエンドポイントでの使用分が含まれます。

> Firecrawl API キーが必要な AI エージェントですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### レスポンス