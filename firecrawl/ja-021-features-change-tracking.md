---
title: 変更追跡 | Firecrawl
url: https://docs.firecrawl.dev/ja/features/change-tracking
source: sitemap
fetched_at: 2026-03-23T07:22:56.906797-03:00
rendered_js: false
word_count: 302
summary: This document explains how to use the Change Tracking feature in Firecrawl to detect, compare, and analyze content updates between scrape iterations using git-diff or JSON-based field comparison modes.
tags:
    - change-tracking
    - web-scraping
    - data-monitoring
    - diff-analysis
    - api-integration
    - firecrawl
category: guide
---

![変更追跡](https://mintcdn.com/firecrawl/vlKm1oZYK3oSRVTM/images/launch-week/lw3d12.webp?fit=max&auto=format&n=vlKm1oZYK3oSRVTM&q=85&s=cc56c24d15e1b2ed4806ddb66d0f5c3f) Change Tracking (変更追跡) は、ページの現在のコンテンツを最後にスクレイプしたときの状態と比較します。ページが新規か、変更なし (`unchanged`) か、変更あり (`modified`) かを検出するために `changeTracking` を `formats` 配列に追加し、必要に応じて「何が変わったか」の構造化された差分を取得できます。

- `/scrape`、`/crawl`、`/batch/scrape` で動作
- 2 つの diff モード: 行単位の変更用 `git-diff`、フィールド単位の比較用 `json`
- チームごとにスコープされ、必要に応じて渡したタグごとにもスコープ可能

## 仕組み

`changeTracking` が有効なすべてのスクレイプ実行時にスナップショットが保存され、その URL に対する前回のスナップショットと比較されます。スナップショットは永続的に保存され、有効期限がないため、スクレイプ間でどれだけ時間が空いても比較結果の精度が維持されます。

ScrapeResultFirst time`changeStatus: "new"` (前のバージョンが存在しない)Content unchanged`changeStatus: "same"` (コンテンツに変更なし)Content modified`changeStatus: "changed"` (コンテンツが変更され、差分データあり)Page removed`changeStatus: "removed"` (ページが削除された)

レスポンスには、`changeTracking` オブジェクト内に次のフィールドが含まれます。

FieldTypeDescription`previousScrapeAt``string | null`前回スクレイプのタイムスタンプ (初回スクレイプ時は `null`)`changeStatus``string``"new"`、`"same"`、`"changed"`、または `"removed"``visibility``string``"visible"` (リンクやサイトマップ経由で検出可能) または `"hidden"` (URL は有効だが、もはやリンクされていない)`diff``object | undefined`行レベルの差分 (ステータスが `"changed"` のときに `git-diff` モードでのみ含まれる)`json``object | undefined`フィールドレベルの比較 (ステータスが `"changed"` のときに `json` モードでのみ含まれる)

## 基本的な使い方

`formats` 配列には `markdown` と `changeTracking` の両方を指定します。変更追跡ではページ同士を markdown コンテンツとして比較するため、`markdown` フォーマットは必須です。

### レスポンス

初回のスクレイプでは、`changeStatus` は `"new"`、`previousScrapeAt` は `null` になります。

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $9/mo\nPro: $29/mo...",
    "changeTracking": {
      "previousScrapeAt": null,
      "changeStatus": "new",
      "visibility": "visible"
    }
  }
}
```

以降のスクレイプでは、`changeStatus` にコンテンツが変更されたかどうかが反映されます。

```
{
  "success": true,
  "data": {
    "markdown": "# Pricing\n\nStarter: $12/mo\nPro: $39/mo...",
    "changeTracking": {
      "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible"
    }
  }
}
```

## Git-diff モード

`git-diff` モードは、`git diff` に似た形式で行単位の変更差分を返します。`formats` 配列内に `modes: ["git-diff"]` を含むオブジェクトを指定します。

### レスポンス

`diff` オブジェクトには、プレーンテキスト形式の diff と構造化された JSON 表現の両方が含まれます。

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-01T10:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "diff": {
      "text": "@@ -1,3 +1,3 @@\n # Pricing\n-Starter: $9/mo\n-Pro: $29/mo\n+Starter: $12/mo\n+Pro: $39/mo",
      "json": {
        "files": [{
          "chunks": [{
            "content": "@@ -1,3 +1,3 @@",
            "changes": [
              { "type": "normal", "content": "# Pricing" },
              { "type": "del", "ln": 2, "content": "Starter: $9/mo" },
              { "type": "del", "ln": 3, "content": "Pro: $29/mo" },
              { "type": "add", "ln": 2, "content": "Starter: $12/mo" },
              { "type": "add", "ln": 3, "content": "Pro: $39/mo" }
            ]
          }]
        }]
      }
    }
  }
}
```

構造化された `diff.json` オブジェクトには次の要素が含まれます:

- `files`: 変更されたファイルの配列 (通常はウェブページごとに1つ)
- `chunks`: ファイル内の変更箇所を表すセクション
- `changes`: 個々の行ごとの変更。`type` (`"add"`、`"del"`、または `"normal"`) 、行番号 (`ln`) 、および `content` を含む

## JSONモード

`json` モードは、定義したスキーマを使って、ページの現在のバージョンと前回のバージョンの両方から特定のフィールドを抽出します。これは、ページ全体の差分を解析することなく、価格、在庫レベル、メタデータなどの構造化データの変更を追跡するのに便利です。 抽出するフィールドを定義する `schema` とともに `modes: ["json"]` を渡します：

### レスポンス

スキーマ内の各フィールドは、`previous` と `current` の値を含めて返されます。

```
{
  "changeTracking": {
    "previousScrapeAt": "2025-06-05T08:00:00.000+00:00",
    "changeStatus": "changed",
    "visibility": "visible",
    "json": {
      "price": {
        "previous": "$19.99",
        "current": "$24.99"
      },
      "availability": {
        "previous": "在庫あり",
        "current": "在庫あり"
      }
    }
  }
}
```

また、任意の `prompt` を渡して、スキーマとあわせて LLM による抽出をガイドすることもできます。

デフォルトでは、変更追跡 (change tracking) は、チームによって同じ URL に対して実行された直近のスクレイプ結果と比較します。タグを使うと、同じ URL に対して**別々の追跡履歴**を維持できます。同じページを異なる間隔や異なるコンテキストで監視したい場合に便利です。

## change tracking を利用したクロール

サイト全体の変更を監視するために、クロール処理に change tracking を追加します。`scrapeOptions` 内で `changeTracking` フォーマットを指定します。

## changeTracking を使ったバッチスクレイプ

特定の URL 群を監視するには、[batch scrape](https://docs.firecrawl.dev/ja/features/batch-scrape) を使用します：

## 変更追跡のスケジュール設定

変更追跡は、定期的にスクレイピングを行う場合に最も効果を発揮します。cron、クラウドスケジューラ、ワークフローツールなどで自動化できます。

### Cronジョブ

URLをスクレイピングし、変更を検知したらアラートを送るスクリプトを作成します。

```
#!/bin/bash
RESPONSE=$(curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://competitor.com/pricing",
    "formats": [
      "markdown",
      {
        "type": "changeTracking",
        "modes": ["json"],
        "schema": {
          "type": "object",
          "properties": {
            "starter_price": { "type": "string" },
            "pro_price": { "type": "string" }
          }
        }
      }
    ]
  }')

STATUS=$(echo "$RESPONSE" | jq -r '.data.changeTracking.changeStatus')

if [ "$STATUS" = "changed" ]; then
  echo "$RESPONSE" | jq '.data.changeTracking.json'
  # メール、Slackなどでアラートを送信
fi
```

`crontab -e` でスケジュールを設定します：

```
0 */6 * * * /path/to/check-pricing.sh >> /var/log/price-monitor.log 2>&1
```

スケジュール表現毎時`0 * * * *`6時間ごと`0 */6 * * *`毎日午前9時`0 9 * * *`毎週月曜日午前8時`0 8 * * 1`

### クラウドおよびサーバーレスのスケジューラー

- **AWS**: EventBridge ルールによる Lambda 関数のトリガー
- **GCP**: Cloud Scheduler による Cloud Function のトリガー
- **Vercel / Netlify**: Cron によってトリガーされるサーバーレス関数
- **GitHub Actions**: `schedule` および `cron` トリガーによるスケジュールされたワークフロー

### ワークフロー自動化

**n8n**、**Zapier**、**Make** のようなノーコードプラットフォームから、スケジュール実行で Firecrawl API を呼び出し、結果を Slack、メール、データベースなどに送信できます。[ワークフロー自動化ガイド](https://docs.firecrawl.dev/ja/developer-guides/workflow-automation/n8n)も参照してください。

## Webhooks

crawl や batch scrape のような非同期処理では、ポーリングするのではなく [webhooks](https://docs.firecrawl.dev/ja/webhooks/overview) を使用して、到着しだい changeTracking の結果を受け取れます。

`crawl.page` イベントのペイロードには、各ページごとに `changeTracking` オブジェクトが含まれています。

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [{
    "markdown": "# Pricing\n\nStarter: $12/mo...",
    "metadata": {
      "title": "Pricing",
      "url": "https://example.com/pricing",
      "statusCode": 200
    },
    "changeTracking": {
      "previousScrapeAt": "2025-06-05T12:00:00.000+00:00",
      "changeStatus": "changed",
      "visibility": "visible",
      "diff": {
        "text": "@@ -2,1 +2,1 @@\n-Starter: $9/mo\n+Starter: $12/mo"
      }
    }
  }]
}
```

Webhook の構成の詳細 (ヘッダー、メタデータ、イベント、再試行、署名検証) については、[Webhook ドキュメント](https://docs.firecrawl.dev/ja/webhooks/overview)を参照してください。

## 設定リファレンス

`changeTracking` フォーマットオブジェクトを渡すときに利用できるオプション一覧:

ParameterTypeDefaultDescription`type``string`(required)`"changeTracking"` でなければなりません`modes``string[]``[]`有効化する差分モード: `"git-diff"`、`"json"`、またはその両方`schema``object`(none)フィールド単位の比較用の JSON Schema (`json` モードでは必須)`prompt``string`(none)LLM による抽出を制御するためのカスタムプロンプト (`json` モードで使用)`tag``string``null`独立したトラッキング履歴用の識別子

### データモデル

## 重要な詳細

- **スナップショットの保持**: スナップショットは永続的に保存され、有効期限はありません。前回のスクレイプから数か月後に再度スクレイプを実行しても、以前のスナップショットと正しく比較されます。
- **スコープ**: 比較はチーム内に限定されます。任意の URL をチームとして初めてスクレイプした場合は、他のユーザーが同じ URL をスクレイプしていても `"new"` が返されます。
- **URL のマッチング**: 過去のスクレイプは、ソース URL、チーム ID、`markdown` フォーマット、`tag` が完全一致したものと照合されます。スクレイプ間で URL を一貫させてください。
- **パラメータの一貫性**: 同じ URL に対して異なる `includeTags`、`excludeTags`、`onlyMainContent` 設定を使うと、比較結果が信頼できなくなります。
- **比較アルゴリズム**: このアルゴリズムは、空白やコンテンツ順序の変化に強く設計されています。CAPTCHA やボット対策によるランダム化に対応するため、iframe のソース URL は無視されます。
- **キャッシュ**: `changeTracking` を指定したリクエストは、インデックス キャッシュをバイパスします。`maxAge` パラメータは無視されます。
- **エラー処理**: レスポンス内の `warning` フィールドを監視し、`changeTracking` オブジェクトが存在しない可能性を考慮して処理してください (これは、前回スクレイプのデータベース検索がタイムアウトした場合に発生することがあります) 。

## 料金

モード料金基本的な変更追跡追加料金なし (通常のスクレイプクレジットを使用)`git-diff` モード追加料金なし`json` モード1ページあたり 5 クレジット

> Firecrawl API キーが必要な AI エージェントですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。