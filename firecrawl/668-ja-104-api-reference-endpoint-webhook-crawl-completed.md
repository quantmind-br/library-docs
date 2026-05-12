---
title: クロール完了 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/webhook-crawl-completed
source: sitemap
fetched_at: 2026-03-23T07:12:35.567698-03:00
rendered_js: false
word_count: 28
summary: This document outlines the structure and security requirements for handling crawl completion webhooks, including HMAC signature validation and response expectations.
tags:
    - webhook-configuration
    - hmac-security
    - crawl-api
    - event-handling
    - api-integration
category: api
---

```
{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "a1b2c3d4-0003-0000-0000-000000000000",
  "data": [],
  "metadata": {}
}

{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "a1b2c3d4-0003-0000-0000-000000000000",
  "data": [],
  "metadata": {}
}
```

#### ヘッダー

生のリクエスト本文の HMAC-SHA256 署名。形式は `sha256=<hex>` です。[アカウント設定](https://www.firecrawl.dev/app/settings?tab=advanced)で HMAC シークレットが設定されている場合に含まれます。検証の詳細は [Webhook Security](https://docs.firecrawl.dev/webhooks/security) を参照してください。

例:

`"sha256=abc123def456789..."`

#### ボディ

イベントタイプ。

Allowed value: `"crawl.completed"`

空の配列。結果は `GET /crawl/{id}` で取得してください。

webhook 設定で指定したカスタムメタデータオブジェクト。すべての配信でそのまま返されます。

#### レスポンス

受信を確認するには、任意の `2xx` ステータスコードを返してください。