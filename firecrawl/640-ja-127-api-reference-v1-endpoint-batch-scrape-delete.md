---
title: バッチスクレイプのキャンセル - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:12:55.422715-03:00
rendered_js: false
word_count: 30
summary: This document provides the API specification for cancelling a batch scrape job using a DELETE request with bearer token authentication.
tags:
    - api-endpoint
    - web-scraping
    - batch-processing
    - rest-api
    - authentication
category: api
---

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}

curl --request DELETE \
  --url https://api.firecrawl.dev/v1/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> 注意: 機能とパフォーマンスが向上した、この API の新しい [v2 版](https://docs.firecrawl.dev/ja/api-reference/endpoint/batch-scrape-delete) が利用可能です。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス

例:

`"Batch scrape job successfully cancelled."`