---
title: 過去のトークン使用量 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:13:00.420473-03:00
rendered_js: false
word_count: 34
summary: This endpoint retrieves historical token usage data for an authenticated team, providing a breakdown of consumption across all API endpoints for billing purposes.
tags:
    - api-reference
    - token-usage
    - billing-metrics
    - historical-data
    - firecrawl-api
category: api
---

GET

/

team

/

token-usage

/

historical

認証済みチームの履歴トークン使用量を取得します（Extract のみ）

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/team/token-usage/historical \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "periods": [
    {
      "startDate": "2025-01-01T00:00:00Z",
      "endDate": "2025-01-31T23:59:59Z",
      "apiKey": "<string>",
      "totalTokens": 1000
    }
  ]
}
```

月ごとの過去のトークン使用量を返します。必要に応じて、APIキー別の内訳も取得できます。

請求を簡素化し、Extract も他のエンドポイントと同様にクレジット制に統一しました。1クレジットは15トークンに相当します。報告されるトークン使用量には、すべてのエンドポイントでの利用が含まれます。

> Firecrawl APIキーが必要なAI agentですか？ 自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### クエリパラメータ

#### レスポンス