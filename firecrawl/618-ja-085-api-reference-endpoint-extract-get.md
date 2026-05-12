---
title: 抽出ステータスの取得 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/extract-get
source: sitemap
fetched_at: 2026-03-23T07:13:30.33218-03:00
rendered_js: false
word_count: 29
summary: This document describes the API endpoint for retrieving the status and results of a data extraction job using a unique identifier.
tags:
    - api-reference
    - data-extraction
    - authentication
    - job-status
    - bearer-token
category: api
---

```
curl --request GET \
  --url https://api.firecrawl.dev/v2/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z",
  "tokensUsed": 123
}

curl --request GET \
  --url https://api.firecrawl.dev/v2/extract/{id} \
  --header 'Authorization: Bearer <token>'

{
  "success": true,
  "data": {},
  "status": "completed",
  "expiresAt": "2023-11-07T05:31:56Z",
  "tokensUsed": 123
}
```

> Firecrawl API キーが必要な AI エージェントですか？自動オンボーディングの手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス

抽出ジョブの現在の状態

利用可能なオプション:

`completed`,

`processing`,

`failed`,

`cancelled`

抽出ジョブで使用されたトークン数。ジョブが完了している場合にのみ取得できます。