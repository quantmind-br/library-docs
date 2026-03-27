---
title: 取消爬取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/crawl-delete
source: sitemap
fetched_at: 2026-03-23T07:09:44.066953-03:00
rendered_js: false
word_count: 59
summary: This document provides the API specification for cancelling an active web crawling task using its unique task ID.
tags:
    - api-reference
    - web-crawling
    - task-cancellation
    - firecrawl-api
    - rest-api
category: api
---

取消抓取任务

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
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

取消抓取任务

```
curl --request DELETE \
  --url https://api.firecrawl.dev/v2/crawl/{id} \
  --header 'Authorization: Bearer <token>'

{
  "status": "cancelled"
}
```

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化入门说明。

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

爬取任务的 ID

#### 响应

已成功取消

[​](#response-status)

status

enum&lt;string&gt;

可用选项:

`cancelled`

示例:

`"cancelled"`

[建议编辑](https://github.com/firecrawl/firecrawl-docs/edit/main/zh/api-reference/endpoint/crawl-delete.mdx)[提出问题](https://github.com/firecrawl/firecrawl-docs/issues/new?title=Issue%20on%20docs&body=Path%3A%20%2Fzh%2Fapi-reference%2Fendpoint%2Fcrawl-delete)

[Crawl 参数预览  
\
上一页](https://docs.firecrawl.dev/zh/api-reference/endpoint/crawl-params-preview)

[获取抓取错误  
\
下一页](https://docs.firecrawl.dev/zh/api-reference/endpoint/crawl-get-errors)