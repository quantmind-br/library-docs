---
title: Webhooks | Firecrawl
url: https://docs.firecrawl.dev/ja/webhooks/overview
source: sitemap
fetched_at: 2026-03-23T07:38:04.465133-03:00
rendered_js: false
word_count: 39
summary: This document explains how to configure and use webhooks to receive real-time notifications for data processing tasks such as crawling and batch scraping.
tags:
    - webhook-configuration
    - real-time-notifications
    - api-integration
    - event-handling
    - asynchronous-processing
category: guide
---

Webhook を利用すると、ステータスをポーリングするのではなく、処理の進行状況に応じてリアルタイムに通知を受け取れます。

## サポートされている操作

OperationイベントCrawl`started`, `page`, `completed`Batch Scrape`started`, `page`, `completed`Extract`started`, `completed`, `failed`Agent`started`, `action`, `completed`, `failed`, `cancelled`

## 設定

リクエストに `webhook` オブジェクトを追加します:

```
{
  "webhook": {
    "url": "https://your-domain.com/webhook",
    "metadata": {
      "any_key": "any_value"
    },
    "events": ["started", "page", "completed", "failed"]
  }
}
```

フィールド型必須説明`url`stringYesWebhook エンドポイントの URL（HTTPS）`headers`objectNoWebhook リクエストに含めるカスタムヘッダー`metadata`objectNoペイロードに含めるカスタムデータ`events`arrayNo受信するイベントタイプ（既定: すべて）

## 使い方

### Webhookでのクロール

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### Webhook を用いたバッチスクレイプ

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

## タイムアウトとリトライ

エンドポイントは **10秒以内** に `2xx` ステータスで応答する必要があります。 配信に失敗した場合（タイムアウト、非2xx、またはネットワークエラー）、Firecrawl は自動的にリトライします:

リトライ回数失敗後の遅延時間1回目1分2回目5分3回目15分

3回のリトライがすべて失敗すると、Webhook は失敗としてマークされ、それ以上のリトライは行われません。