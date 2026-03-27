---
title: 创建浏览器会话 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/browser-create
source: sitemap
fetched_at: 2026-03-23T07:21:00.560695-03:00
rendered_js: false
word_count: 70
summary: This document describes the API endpoint for creating and managing remote browser sessions, including configuration options for session TTL, inactivity timeouts, and persistent storage profiles.
tags:
    - browser-automation
    - api-endpoint
    - session-management
    - cdp-integration
    - web-scraping
category: api
---

Header值`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## 请求体

参数类型必填默认值描述`ttl`number否600会话总有效期（秒）（30-3600）`activityTtl`number否300会话在销毁前允许的不活动时长（秒）（10-3600）`profile`object否—启用跨会话的持久化存储。参见下文。`profile.name`string是\*—配置文件名称（1-128 字符）。具有相同名称的会话共享存储。`profile.saveChanges`boolean否`true`当为 `true` 时，在关闭时会将浏览器状态保存回该配置文件。设为 `false` 可在不写入的情况下加载已有数据。同一时间只允许一个保存方。

## 响应

字段类型描述`success`boolean会话是否创建成功`id`string唯一的会话标识符`cdpUrl`string用于 CDP 连接的 WebSocket 地址`liveViewUrl`string用于实时查看会话的 URL`interactiveLiveViewUrl`string用于与会话进行实时交互（点击、输入、滚动）的 URL`expiresAt`string会话基于 TTL 的过期时间

### 请求示例

```
curl -X POST "https://api.firecrawl.dev/v2/browser" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "ttl": 120
  }'
```

### 响应示例

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://cdp-proxy.firecrawl.dev/cdp/550e8400-e29b-41d4-a716-446655440000",
  "liveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/550e8400-e29b-41d4-a716-446655440000?interactive=true"
}
```

> 如果你是需要 Firecrawl API 密钥的 AI 代理，请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化接入说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 请求体

浏览器会话的最大存活时长（秒）

必填范围: `30 <= x <= 3600`

会话在空闲被销毁前的超时时长（秒）

必填范围: `10 <= x <= 3600`

在会话之间启用持久化存储。在一个会话中保存的数据，之后在使用相同名称的会话中可以重新加载。

#### 响应

用于访问 Chrome DevTools Protocol 的 WebSocket 地址

用于实时与浏览器会话交互的 URL（点击、输入、滚动）