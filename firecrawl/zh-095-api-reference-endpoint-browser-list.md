---
title: 列出浏览器会话 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/browser-list
source: sitemap
fetched_at: 2026-03-23T07:21:05.177216-03:00
rendered_js: false
word_count: 51
summary: This document provides the API specification for retrieving a list of browser sessions, including their status, connection URLs, and activity timestamps.
tags:
    - api-reference
    - browser-sessions
    - rest-api
    - firecrawl
    - web-automation
category: api
---

请求头值`Authorization``Bearer <API_KEY>`

## 查询参数

参数类型是否必填描述`status`string否根据会话状态进行筛选：`"active"` 或 `"destroyed"`

## 响应

字段类型描述`success`boolean请求是否成功`sessions`array会话对象列表

### 会话对象

字段类型描述`id`string唯一会话标识符`status`string当前会话状态（`"active"` 或 `"destroyed"`）`cdpUrl`string用于 CDP 连接的 WebSocket URL`liveViewUrl`string实时查看会话的 URL`interactiveLiveViewUrl`string实时与会话交互（点击、输入、滚动）的 URL`createdAt`string会话创建时的 ISO 8601 时间戳`lastActivity`string上次活动的 ISO 8601 时间戳

### 请求示例

```
curl -X GET "https://api.firecrawl.dev/v2/browser?status=active" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY"
```

### 示例响应

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
      "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true",
      "createdAt": "2025-06-01T12:00:00Z",
      "lastActivity": "2025-06-01T12:05:30Z"
    }
  ]
}
```

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化接入说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 查询参数

#### 响应