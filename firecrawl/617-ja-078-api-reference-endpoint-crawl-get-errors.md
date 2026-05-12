---
title: クロールのエラーを取得 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/crawl-get-errors
source: sitemap
fetched_at: 2026-03-23T07:13:31.393024-03:00
rendered_js: false
word_count: 28
summary: This document provides the API reference for retrieving error logs and URLs blocked by robots.txt from a specific scraping job.
tags:
    - api-reference
    - error-handling
    - web-scraping
    - firecrawl-api
    - robots-txt
    - data-retrieval
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/crawl/{id}/errors \
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
  --url https://api.firecrawl.dev/v2/crawl/{id}/errors \
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

> Firecrawl API キーが必要な AI エージェントですか？自動オンボーディングの手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス

エラーが発生したスクレイピングジョブとエラーの詳細

スクレイピングを試行したが、robots.txt によってブロックされた URL の一覧