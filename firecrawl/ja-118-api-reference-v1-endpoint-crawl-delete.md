---
title: クロールのキャンセル - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:12:17.097064-03:00
rendered_js: false
word_count: 50
summary: This document provides the API endpoint details and instructions for canceling an active crawl job using its unique identifier.
tags:
    - api-reference
    - crawl-job
    - cancel-request
    - firecrawl
    - data-scraping
    - rest-api
category: api
---

クロールジョブをキャンセルする

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

DELETE

/

crawl

/

{id}

クロールジョブをキャンセルする

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> 注意：機能とパフォーマンスが向上した本APIの新しい[v2版](https://docs.firecrawl.dev/ja/api-reference/endpoint/crawl-delete)が利用可能です。

#### 承認

[​](#authorization-authorization)

Authorization

string

header

必須

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

[​](#parameter-id)

id

string&lt;uuid&gt;

必須

クロールジョブのID

#### レスポンス

キャンセルが完了しました

[​](#response-status)

status

enum&lt;string&gt;

利用可能なオプション:

`cancelled`

例:

`"cancelled"`

[編集を提案](https://github.com/firecrawl/firecrawl-docs/edit/main/ja/api-reference/v1-endpoint/crawl-delete.mdx)[問題を報告](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path%3A%20%2Fja%2Fapi-reference%2Fv1-endpoint%2Fcrawl-delete)

[クロールステータスを取得  
\
前へ](https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/crawl-get)

[クロールエラーの取得  
\
次へ](https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/crawl-get-errors)