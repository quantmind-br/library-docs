---
title: ブラウザーセッション一覧の取得 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/browser-list
source: sitemap
fetched_at: 2026-03-23T07:23:29.98332-03:00
rendered_js: false
word_count: 56
summary: This document provides the API reference for retrieving a list of browser sessions, including their connection URLs and status, using the Firecrawl API.
tags:
    - api-reference
    - browser-sessions
    - rest-api
    - firecrawl
    - session-management
category: api
---

ヘッダー値`Authorization``Bearer <API_KEY>`

## クエリパラメーター

パラメーター型必須説明`status`stringいいえセッションのステータスでフィルタリングします：`"active"` または `"destroyed"`

## レスポンス

フィールド型説明`success`booleanリクエストが成功したかどうか`sessions`arrayセッションオブジェクトのリスト

### セッションオブジェクト

FieldTypeDescription`id`string一意のセッション ID`status`string現在のセッションの状態（`"active"` または `"destroyed"`）`cdpUrl`stringCDP 接続用の WebSocket URL`liveViewUrl`stringセッションをリアルタイムでモニタリングするための URL`interactiveLiveViewUrl`stringセッションをリアルタイムで操作するための URL（クリック、入力、スクロール）`createdAt`stringセッション作成日時の ISO 8601 形式タイムスタンプ`lastActivity`string最終アクティビティ日時の ISO 8601 形式タイムスタンプ

### リクエスト例

```
curl -X GET "https://api.firecrawl.dev/v2/browser?status=active" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

### レスポンスの例

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
      "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true",
      "createdAt": "2025-06-01T12:00:00Z",
      "lastActivity": "2025-06-01T12:05:30Z"
    }
  ]
}
```

> Firecrawl API key が必要な AI agent の場合は、自動オンボーディング手順について [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### クエリパラメータ

セッションをステータスでフィルタリング

利用可能なオプション:

`active`,

`destroyed`

#### レスポンス