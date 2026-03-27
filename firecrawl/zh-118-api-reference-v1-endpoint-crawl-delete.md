---
title: 取消抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:08:18.447214-03:00
rendered_js: false
word_count: 55
summary: This document provides the API specification for cancelling a pending or active crawl job using a specific task identifier.
tags:
    - api-reference
    - firecrawl
    - crawl-job
    - delete-request
    - web-scraping
category: api
---

取消抓取作业

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

取消抓取作业

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> 注意：全新的 [v2 版本此 API](https://docs.firecrawl.dev/zh/api-reference/endpoint/crawl-delete) 现已推出，具备更完善的功能和更优的性能。

#### 授权

[​](#authorization-authorization)

Authorization

string

header

必填

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

[​](#parameter-id)

id

string&lt;uuid&gt;

必填

抓取任务 ID

#### 响应

已成功取消

[​](#response-status)

status

enum&lt;string&gt;

可用选项:

`cancelled`

示例:

`"cancelled"`

[建议编辑](https://github.com/firecrawl/firecrawl-docs/edit/main/zh/api-reference/v1-endpoint/crawl-delete.mdx)[提出问题](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path%3A%20%2Fzh%2Fapi-reference%2Fv1-endpoint%2Fcrawl-delete)

[获取爬取状态  
\
上一页](https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/crawl-get)

[获取爬取错误  
\
下一页](https://docs.firecrawl.dev/zh/api-reference/v1-endpoint/crawl-get-errors)