---
title: エージェントアクション - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/webhook-agent-action
source: sitemap
fetched_at: 2026-03-23T07:13:15.21979-03:00
rendered_js: false
word_count: 22
summary: This document describes the structure, authentication headers, and response requirements for webhook events triggered by agent actions.
tags:
    - webhook
    - hmac-signature
    - api-integration
    - event-payload
    - security-validation
category: reference
---

#### ヘッダー

生のリクエスト本文の HMAC-SHA256 署名。形式は `sha256=<hex>` です。[アカウント設定](https://www.firecrawl.dev/app/settings?tab=advanced)で HMAC シークレットが設定されている場合に含まれます。検証の詳細は [Webhook Security](https://docs.firecrawl.dev/webhooks/security) を参照してください。

例:

`"sha256=abc123def456789..."`

#### ボディ

Allowed value: `"agent.action"`

実行されたアクションを記述する単一のオブジェクトを含む配列です。

webhook 設定で指定したカスタムメタデータオブジェクト。すべての配信でそのまま返されます。

#### レスポンス

受信を確認するには、任意の`2xx`ステータスコードを返してください。