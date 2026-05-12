---
title: ブラウザセッションの削除 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/browser-delete
source: sitemap
fetched_at: 2026-03-23T07:23:21.880569-03:00
rendered_js: false
word_count: 32
summary: This document provides the technical specifications for an API endpoint designed to terminate or discard a specific browser session.
tags:
    - api-endpoint
    - session-management
    - rest-api
    - authentication
    - firecrawl
category: api
---

ヘッダー値`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## リクエストボディ

パラメーター型必須説明`id`string必須破棄するセッションの ID

## レスポンス

フィールド型説明`success`booleanセッションが正常に破棄されたかどうか

### リクエスト例

```
curl -X DELETE "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }'
```

### レスポンス例

> Firecrawl APIキーが必要な AI agent ですか？自動オンボーディングの手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス