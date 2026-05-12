---
title: クロール開始 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/webhook-crawl-started
source: sitemap
fetched_at: 2026-03-23T07:12:46.371405-03:00
rendered_js: false
word_count: 33
summary: This document specifies the structure, security headers, and expected response format for webhook notifications sent by the service.
tags:
    - webhooks
    - hmac-security
    - webhook-payload
    - api-integration
    - event-notifications
category: reference
---

#### ヘッダー

生のリクエスト本文の HMAC-SHA256 署名。形式は `sha256=<hex>` です。[アカウント設定](https://www.firecrawl.dev/app/settings?tab=advanced)で HMAC シークレットが設定されている場合に含まれます。検証の詳細は [Webhook Security](https://docs.firecrawl.dev/webhooks/security) を参照してください。

例:

`"sha256=abc123def456789..."`

#### ボディ

イベントタイプ。

Allowed value: `"crawl.started"`

クロールジョブ ID。`POST /crawl` が返す `id` と一致します。

この webhook 配信の一意の識別子。重複排除に使用します。再試行時には同じ値が送信されます。

webhook 設定で指定したカスタムメタデータオブジェクト。すべての配信でそのまま返されます。

#### レスポンス

受信を確認するには、任意の `2xx` ステータスコードを返してください。