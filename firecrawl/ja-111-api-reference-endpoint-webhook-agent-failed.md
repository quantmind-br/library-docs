---
title: エージェント失敗 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/webhook-agent-failed
source: sitemap
fetched_at: 2026-03-23T07:12:59.104591-03:00
rendered_js: false
word_count: 24
summary: This document outlines the structure of webhook request headers, body parameters, and expected response codes for handling event notifications.
tags:
    - webhooks
    - api-integration
    - security-headers
    - event-notifications
    - hmac-signature
category: api
---

#### ヘッダー

生のリクエスト本文の HMAC-SHA256 署名。形式は `sha256=<hex>` です。[アカウント設定](https://www.firecrawl.dev/app/settings?tab=advanced)で HMAC シークレットが設定されている場合に含まれます。検証の詳細は [Webhook Security](https://docs.firecrawl.dev/webhooks/security) を参照してください。

例:

`"sha256=abc123def456789..."`

#### ボディ

Allowed value: `"agent.failed"`

失敗内容を説明する、可読性の高いエラーメッセージ。

webhook 設定で指定したカスタムメタデータオブジェクト。すべての配信でそのまま返されます。

#### レスポンス

受信を確認するには、任意の `2xx` ステータスコードを返してください。