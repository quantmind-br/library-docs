---
title: ブラウザーセッションの作成 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/browser-create
source: sitemap
fetched_at: 2026-03-23T07:23:19.987177-03:00
rendered_js: false
word_count: 65
summary: This document describes the API endpoint for initializing browser sessions, including parameters for session duration, inactivity timeouts, and persistent profile storage.
tags:
    - api-documentation
    - browser-session
    - web-scraping
    - session-management
    - cdp-integration
category: api
---

ヘッダー値`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## リクエストボディ

ParameterTypeRequiredDefaultDescription`ttl`numberNo600セッション全体の有効期間（秒）（30〜3600）`activityTtl`numberNo300セッションが破棄されるまでの非アクティブ状態の継続時間（秒）（10〜3600）`profile`objectNo—セッション間での永続的なストレージを有効化します。後述を参照してください。`profile.name`stringYes\*—プロファイルの名前（1〜128文字）。同じ名前のセッションはストレージを共有します。`profile.saveChanges`booleanNo`true``true` の場合、ブラウザの状態は終了時にプロファイルへ保存されます。既存データの読み込みのみを行いたい場合は `false` を設定してください。保存処理を行えるセッションは同時に 1 つだけです。

## レスポンス

フィールド型説明`success`booleanセッションが作成されたかどうか`id`stringセッションの一意の識別子`cdpUrl`stringCDP 接続用の WebSocket URL`liveViewUrl`stringセッションをリアルタイムで閲覧するための URL`interactiveLiveViewUrl`stringセッションをリアルタイムで操作（クリック、入力、スクロール）するための URL`expiresAt`stringTTL に基づいてセッションの有効期限が切れる時刻

### リクエストの例

```
curl -X POST "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": 120
  }'
```

### レスポンス例

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true"
}
```

> Firecrawl APIキーが必要なAI agentですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### ボディ

ブラウザセッションの総有効期間（秒）

必須範囲: `30 <= x <= 3600`

非アクティブ状態によりセッションが破棄されるまでの時間（秒）

必須範囲: `10 <= x <= 3600`

ブラウザのライブビューをストリーミングするかどうか

ブラウザセッションをまたいでデータを永続化します。あるセッションで保存したデータは、同じ名前を指定することで後続のセッションからも読み込むことができます。

#### レスポンス

Chrome DevTools Protocol にアクセスするための WebSocket URL

ブラウザーセッションをリアルタイムで表示するための URL

ブラウザセッションをリアルタイムに操作するためのURL（クリック、入力、スクロール）