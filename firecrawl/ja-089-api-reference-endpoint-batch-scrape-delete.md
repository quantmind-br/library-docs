---
title: バッチスクレイプのキャンセル - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/batch-scrape-delete
source: sitemap
fetched_at: 2026-03-23T07:13:37.366057-03:00
rendered_js: false
word_count: 32
summary: This document provides the API endpoint and authentication details for cancelling a batch scraping job in Firecrawl.
tags:
    - api-reference
    - batch-scraping
    - job-cancellation
    - bearer-authentication
    - firecrawl-api
category: api
---

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}

curl --request DELETE \
  --url https://api.firecrawl.dev/v2/batch/scrape/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "message": "Batch scrape job successfully cancelled."
}
```

> Firecrawl API key が必要な AI agent の場合は、自動オンボーディング手順について [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス

例:

`"Batch scrape job successfully cancelled."`