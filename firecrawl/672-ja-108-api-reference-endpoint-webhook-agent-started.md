---
title: エージェントの開始 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/webhook-agent-started
source: sitemap
fetched_at: 2026-03-23T07:13:11.123419-03:00
rendered_js: false
word_count: 29
summary: This document describes the structure and security requirements for handling agent-started webhook notifications.
tags:
    - webhooks
    - api-reference
    - hmac-signature
    - event-notifications
    - agent-job
category: api
---

```
{
  "success": true,
  "type": "agent.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "d4e5f6a7-0001-0000-0000-000000000000",
  "data": [],
  "metadata": {}
}

{
  "success": true,
  "type": "agent.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "webhookId": "d4e5f6a7-0001-0000-0000-000000000000",
  "data": [],
  "metadata": {}
}
```

#### ヘッダー

生のリクエスト本文の HMAC-SHA256 署名。形式は `sha256=<hex>` です。[アカウント設定](https://www.firecrawl.dev/app/settings?tab=advanced)で HMAC シークレットが設定されている場合に含まれます。検証の詳細は [Webhook Security](https://docs.firecrawl.dev/webhooks/security) を参照してください。

例:

`"sha256=abc123def456789..."`

#### ボディ

Allowed value: `"agent.started"`

エージェントジョブ ID。`POST /agent` が返す `id` と一致します。

webhook 設定で指定したカスタムメタデータオブジェクト。すべての配信でそのまま返されます。

#### レスポンス

受信を確認するには、任意の `2xx` ステータスコードを返してください。