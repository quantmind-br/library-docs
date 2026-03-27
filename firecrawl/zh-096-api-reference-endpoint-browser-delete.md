---
title: 删除浏览器会话 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/browser-delete
source: sitemap
fetched_at: 2026-03-23T07:20:53.840459-03:00
rendered_js: false
word_count: 33
summary: This document provides the API specifications for destroying a specific browser session using the Firecrawl service.
tags:
    - api-reference
    - session-management
    - firecrawl-api
    - rest-api
    - authentication
category: api
---

Header值`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## 请求体

参数类型必填描述`id`string是要销毁的会话 ID

## 响应

字段类型描述`success`boolean会话是否已成功销毁

### 请求示例

```
curl -X DELETE "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }'
```

### 响应示例

> 你是需要 Firecrawl API 密钥的 AI 代理吗？有关自动化接入说明，请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 响应