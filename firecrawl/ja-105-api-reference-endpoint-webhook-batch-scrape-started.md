---
title: バッチスクレイプの開始 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/webhook-batch-scrape-started
source: sitemap
fetched_at: 2026-03-23T07:12:39.15984-03:00
rendered_js: false
word_count: 29
summary: This document describes the structure and security requirements for handling webhooks triggered by batch scraping jobs in Firecrawl.
tags:
    - webhook
    - batch-scraping
    - hmac-signature
    - api-integration
    - security-validation
category: api
---

```
{
  "success": true,
  "type": "batch_scrape.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "b2c3d4e5-0001-0000-0000-000000000000",
  "data": [],
  "metadata": {}
}

{
  "success": true,
  "type": "batch_scrape.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "b2c3d4e5-0001-0000-0000-000000000000",
  "data": [],
  "metadata": {}
}
```

#### ヘッダー

生のリクエスト本文の HMAC-SHA256 署名。形式は `sha256=<hex>` です。[アカウント設定](https://www.firecrawl.dev/app/settings?tab=advanced)で HMAC シークレットが設定されている場合に含まれます。検証の詳細は [Webhook Security](https://docs.firecrawl.dev/webhooks/security) を参照してください。

例:

`"sha256=abc123def456789..."`

#### ボディ

Allowed value: `"batch_scrape.started"`

バッチスクレイプジョブ ID。`POST /batch/scrape` で返される `id` と一致します。

webhook 設定で指定したカスタムメタデータオブジェクト。すべての配信でそのまま返されます。

#### レスポンス

受信を確認するには、任意の `2xx` ステータスコードを返してください。