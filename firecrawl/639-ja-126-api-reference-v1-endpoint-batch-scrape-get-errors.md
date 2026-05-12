---
title: バッチスクレイプエラーを取得 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:12:50.425628-03:00
rendered_js: false
word_count: 37
summary: This document describes the API endpoint for retrieving error logs and blocked URL lists associated with a specific batch scraping job.
tags:
    - api-reference
    - batch-scraping
    - error-logs
    - robots-txt
    - web-scraping
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id}/errors \
  --header 'Authorization: Bearer <token>'

{
  "errors": [
    {
      "id": "<string>",
      "timestamp": "<string>",
      "url": "<string>",
      "error": "<string>"
    }
  ],
  "robotsBlocked": [
    "<string>"
  ]
}
```

GET

/

batch

/

scrape

/

{id}

/

errors

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id}/errors \
  --header 'Authorization: Bearer <token>'

{
  "errors": [
    {
      "id": "<string>",
      "timestamp": "<string>",
      "url": "<string>",
      "error": "<string>"
    }
  ],
  "robotsBlocked": [
    "<string>"
  ]
}
```

> 注記: エラー報告およびデバッグ機能が強化された新しい [v2 版 API](https://docs.firecrawl.dev/ja/api-reference/endpoint/batch-scrape-get-errors) が利用可能です。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス

スクレイピングを試みたが robots.txt によりブロックされた URL の一覧