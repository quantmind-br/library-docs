---
title: バッチスクレイピング | Firecrawl
url: https://docs.firecrawl.dev/ja/features/batch-scrape
source: sitemap
fetched_at: 2026-03-23T07:23:19.586816-03:00
rendered_js: false
word_count: 125
summary: This document explains how to perform batch scraping with Firecrawl, enabling the parallel processing of multiple URLs either synchronously or asynchronously, along with configuration options for concurrency, structured data extraction, and webhook integration.
tags:
    - batch-scraping
    - firecrawl-api
    - parallel-processing
    - webhooks
    - structured-data-extraction
    - api-documentation
category: guide
---

バッチスクレイピングでは、1つのジョブで複数のURLをスクレイピングできます。URLのリストと任意のパラメータを渡すと、Firecrawl がそれらを並行して処理し、すべての結果をまとめて返します。

- 明示的に指定したURLのリストを対象とする点を除き、`/crawl` と同様に動作します
- 同期モードと非同期モードに対応
- 構造化抽出を含む、すべてのスクレイピングオプションをサポート
- ジョブごとに同時実行数を設定可能

## 仕組み

バッチスクレイプは、次の2つの方法で実行できます。

モードSDK メソッド (JS / Python)動作同期`batchScrape` / `batch_scrape`バッチを開始し、完了まで待機して、すべての結果を返します非同期`startBatchScrape` / `start_batch_scrape`バッチを開始し、ポーリングまたは Webhook 用のジョブ ID を返します

## 基本的な使い方

### レスポンス

`batchScrape` / `batch_scrape` を呼び出すと、バッチ完了時に完全な結果が返されます。

```
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Firecrawl Docs のホームページ![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Groq Llama 3 で「ウェブサイトと会話できる」機能を構築する | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Firecrawl、Groq Llama 3、LangChain を使って「自分のウェブサイトと会話できる」ボットを構築する方法を学びます。",
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

`startBatchScrape` / `start_batch_scrape` を呼び出すと、`getBatchScrapeStatus` / `get_batch_scrape_status`、API エンドポイント `/batch/scrape/{id}`、または Webhook を使って追跡できるジョブ ID が返されます。ジョブの結果は、完了後 24 時間まで API 経由で取得できます。この期間を過ぎても、[activity logs](https://www.firecrawl.dev/app/logs) からバッチスクレイプの履歴と結果を確認できます。

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## 並行実行数

デフォルトでは、バッチスクレイプジョブはチームのブラウザ同時実行数の上限をフルに使用します ([Rate Limits](https://docs.firecrawl.dev/ja/rate-limits) を参照) 。`maxConcurrency` パラメータでジョブごとにこの上限を下げることができます。 たとえば、`maxConcurrency: 50` とすると、そのジョブは同時に 50 件までしかスクレイプを実行しません。大規模なバッチでこの値を低くしすぎると処理が大幅に遅くなるため、他のジョブ用に同時実行枠を残す必要がある場合にのみ減らしてください。

バッチスクレイプを使用して、バッチ内のすべてのページから構造化データを抽出できます。これは、URLのリストに同じスキーマを適用したい場合に便利です。

### レスポンス

`batchScrape` / `batch_scrape` は完全な結果を返します：

```
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "json": {
        "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
        "description": "Firecrawl、Groq Llama 3、LangChain を使って「自分のウェブサイトとチャットできる」ボットの作り方を解説します。"
      }
    },
    ...
  ]
}
```

`startBatchScrape` / `start_batch_scrape` はジョブ ID を返します：

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Webhooks

バッチ内の各 URL がスクレイプされるたびにリアルタイムで通知を受け取れるよう、webhook を設定できます。これにより、バッチ全体の完了を待たずに結果を即時に処理できます。

```
curl -X POST https://api.firecrawl.dev/v2/batch/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
      ],
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### イベントの種類

イベント説明`batch_scrape.started`バッチスクレイプジョブが開始されました`batch_scrape.page`1件のURLのスクレイプに成功しました`batch_scrape.completed`すべてのURLの処理が完了しました`batch_scrape.failed`バッチスクレイプジョブでエラーが発生しました

### ペイロード

各Webhook配信には、次の構造のJSONボディが含まれます:

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "batch-job-id",
  "data": [...],
  "metadata": {},
  "error": null
}
```

### Webhook シグネチャの検証

Firecrawl から送信されるすべての webhook リクエストには、HMAC-SHA256 シグネチャを含む `X-Firecrawl-Signature` ヘッダーが含まれます。Webhook が正当なものであり、改ざんされていないことを確認するために、必ずこのシグネチャを検証してください。

1. アカウント設定の [Advanced タブ](https://www.firecrawl.dev/app/settings?tab=advanced) から webhook secret を取得する
2. `X-Firecrawl-Signature` ヘッダーからシグネチャを取り出す
3. secret を使って、生のリクエストボディに対して HMAC-SHA256 を計算する
4. タイミング攻撃耐性のある (タイミングセーフな) 関数を用いて、計算結果とシグネチャヘッダーを比較する

JavaScript と Python による実装の完全な例については、[Webhook セキュリティのドキュメント](https://docs.firecrawl.dev/ja/webhooks/security) を参照してください。 詳細なイベントペイロード、高度な設定、トラブルシューティングなどを含む webhook の包括的なドキュメントについては、[Webhooks ドキュメント](https://docs.firecrawl.dev/ja/webhooks/overview) を参照してください。

> Firecrawl API key が必要な AI agent の方は、自動オンボーディング手順について [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。