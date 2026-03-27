---
title: クロールエラーの取得 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:12:24.56308-03:00
rendered_js: false
word_count: 29
summary: This document describes the API endpoint for retrieving error logs and robots.txt blocking information associated with a specific crawl task.
tags:
    - api-endpoint
    - web-scraping
    - error-logs
    - robots-txt
    - crawl-status
    - authentication
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id}/errors \
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

curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id}/errors \
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

> 注記: 機能とパフォーマンスが向上した、この API の新しい [v2 バージョン](https://docs.firecrawl.dev/ja/api-reference/endpoint/crawl-get-errors) が利用可能です。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス

スクレイピングを試みたが robots.txt によりブロックされた URL の一覧