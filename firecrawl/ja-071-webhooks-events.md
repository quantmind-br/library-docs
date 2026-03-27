---
title: Webhook イベントタイプ | Firecrawl
url: https://docs.firecrawl.dev/ja/webhooks/events
source: sitemap
fetched_at: 2026-03-23T07:28:06.485696-03:00
rendered_js: false
word_count: 51
summary: This document provides a comprehensive reference for webhook event types, payload structures, and configuration options used for monitoring crawling, extraction, and agent-based scraping tasks.
tags:
    - webhook
    - api-reference
    - event-types
    - scraping
    - data-extraction
    - webhooks-configuration
category: reference
---

## クイックリファレンス

EventTrigger`crawl.started`クロールジョブの処理が開始される`crawl.page`クロール中にページがスクレイピングされる`crawl.completed`クロールジョブが完了し、すべてのページが処理される`batch_scrape.started`バッチスクレイプジョブの処理が開始される`batch_scrape.page`バッチスクレイプ中にURLがスクレイピングされる`batch_scrape.completed`バッチ内のすべてのURLが処理される`extract.started`抽出ジョブの処理が開始される`extract.completed`抽出が正常に完了する`extract.failed`抽出が失敗する`agent.started`エージェントジョブの処理が開始される`agent.action`エージェントがツール（スクレイピング、検索など）を実行する`agent.completed`エージェントが正常に完了する`agent.failed`エージェントでエラーが発生する`agent.cancelled`エージェントジョブがユーザーによってキャンセルされる

## ペイロード構造

すべてのWebhookイベントは、この共通の構造を持ちます。

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [...],
  "metadata": {}
}
```

FieldTypeDescription`success`boolean操作が成功したかどうか`type`stringイベントタイプ（例: `crawl.page`）`id`stringジョブID`data`arrayイベント固有のデータ（下記の例を参照）`metadata`objectWebhook 設定で指定したカスタムメタデータ`error`stringエラーメッセージ（`success` が `false` の場合）

## クロールイベント

### `crawl.started`

クロールジョブの処理が開始されるタイミングで送信されます。

```
{
  "success": true,
  "type": "crawl.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `crawl.page`

クロール中にスクレイピングされた各ページごとに送信されます。`data` 配列にはページのコンテンツとメタデータが含まれます。

```
{
  "success": true,
  "type": "crawl.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Page content...",
      "metadata": {
        "title": "Page Title",
        "description": "ページの説明",
        "url": "https://example.com/page",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com/page",
        "proxyUsed": "basic",
        "cacheState": "hit",
        "cachedAt": "2025-09-03T21:11:25.636Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `crawl.completed`

クロール処理が完了し、すべてのページの処理が終了したときに送信されます。

```
{
  "success": true,
  "type": "crawl.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

## バッチスクレイプイベント

### `batch_scrape.started`

バッチスクレイプジョブの処理開始時に送信されます。

```
{
  "success": true,
  "type": "batch_scrape.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `batch_scrape.page`

バッチ内でスクレイプされる各URLごとに送信されます。`data` 配列にはページコンテンツとメタデータが含まれます。

```
{
  "success": true,
  "type": "batch_scrape.page",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "markdown": "# Page content...",
      "metadata": {
        "title": "Page Title",
        "description": "ページの説明",
        "url": "https://example.com",
        "statusCode": 200,
        "contentType": "text/html",
        "scrapeId": "550e8400-e29b-41d4-a716-446655440001",
        "sourceURL": "https://example.com",
        "proxyUsed": "basic",
        "cacheState": "miss",
        "cachedAt": "2025-09-03T23:30:53.434Z",
        "creditsUsed": 1
      }
    }
  ],
  "metadata": {}
}
```

### `batch_scrape.completed`

バッチ内のすべてのURLの処理が完了したときに送信されます。

```
{
  "success": true,
  "type": "batch_scrape.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

抽出処理が開始されると送信されます。

```
{
  "success": true,
  "type": "extract.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

抽出オペレーションが正常に完了したときに送信されます。`data` 配列には、抽出されたデータと使用状況情報が含まれます。

```
{
  "success": true,
  "type": "extract.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "success": true,
      "data": { "siteName": "Example Site", "category": "Technology" },
      "extractId": "550e8400-e29b-41d4-a716-446655440000",
      "llmUsage": 0.0020118,
      "totalUrlsScraped": 1,
      "sources": {
        "siteName": ["https://example.com"],
        "category": ["https://example.com"]
      }
    }
  ],
  "metadata": {}
}
```

抽出処理でエラーが発生したときに送信されます。`error` フィールドに失敗理由が格納されます。

```
{
  "success": false,
  "type": "extract.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "error": "データの抽出に失敗しました：タイムアウトを超過しました",
  "metadata": {}
}
```

## エージェントイベント

### `agent.started`

エージェントのジョブの処理が開始されると送信されます。

```
{
  "success": true,
  "type": "agent.started",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [],
  "metadata": {}
}
```

### `agent.action`

各ツール（scrape、search など）の実行ごとに送信されます。

```
{
  "success": true,
  "type": "agent.action",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 5,
      "action": "mcp__tools__scrape",
      "input": {
        "url": "https://example.com"
      }
    }
  ],
  "metadata": {}
}
```

### `agent.completed`

エージェントの処理が正常に完了したときに送信されます。`data` 配列には、抽出されたデータと消費されたクレジットの合計が含まれます。

```
{
  "success": true,
  "type": "agent.completed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 15,
      "data": {
        "company": "Example Corp",
        "industry": "Technology",
        "founded": 2020
      }
    }
  ],
  "metadata": {}
}
```

### `agent.failed`

エージェントでエラーが発生したときに送信されます。`error` フィールドには失敗理由が含まれます。

```
{
  "success": false,
  "type": "agent.failed",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 8
    }
  ],
  "error": "最大クレジット数を超過しました",
  "metadata": {}
}
```

### `agent.cancelled`

ユーザーがエージェントジョブをキャンセルしたときに送信されます。

```
{
  "success": false,
  "type": "agent.cancelled",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "data": [
    {
      "creditsUsed": 3
    }
  ],
  "metadata": {}
}
```

## イベントのフィルタリング

デフォルトではすべてのイベントを受信します。特定のイベントだけを受信したい場合は、Webhook の設定で `events` 配列を指定してください。

```
{
  "url": "https://your-app.com/webhook",
  "events": ["completed", "failed"]
}
```

ジョブの完了だけ分かればよく、ページ単位の更新は不要な場合に便利です。