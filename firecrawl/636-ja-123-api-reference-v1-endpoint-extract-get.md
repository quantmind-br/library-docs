---
title: 抽出ステータスの取得 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:12:02.673275-03:00
rendered_js: false
word_count: 29
summary: This document describes the endpoint used to retrieve the status and results of a data extraction job within the Firecrawl API.
tags:
    - api-reference
    - data-extraction
    - status-check
    - authentication
    - firecrawl-api
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}

curl --request GET \
  --url https://api.firecrawl.dev/v1/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z"
}
```

> 注意: 機能とパフォーマンスが向上した [v2 版 API](https://docs.firecrawl.dev/ja/api-reference/endpoint/extract-get) が利用可能です。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス

抽出ジョブの現在のステータス

利用可能なオプション:

`completed`,

`processing`,

`failed`,

`cancelled`