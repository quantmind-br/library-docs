---
title: 执行浏览器代码 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/browser-execute
source: sitemap
fetched_at: 2026-03-23T07:21:07.112664-03:00
rendered_js: false
word_count: 65
summary: This document provides the API specification for executing arbitrary code within a browser sandbox environment, including request parameters, authentication requirements, and expected response fields.
tags:
    - api-reference
    - browser-sandbox
    - code-execution
    - firecrawl-api
    - rest-api
category: api
---

请求头字段值`Authorization``Bearer <API_KEY>``Content-Type``application/json`

## 请求体

参数类型必填默认值描述`code`string是-要执行的代码（1-100,000 个字符）`language`string否`"node"`代码语言：`"python"`、`"node"` 或 `"bash"`（用于 agent-browser CLI 命令）`timeout`number否-执行超时时间（单位：秒，范围 1-300）

## 响应

字段类型描述`success`boolean代码是否执行成功`stdout`string代码执行产生的标准输出`result`string代码执行产生的标准输出`stderr`string代码执行产生的标准错误输出`exitCode`number已执行进程的退出码`killed`boolean进程是否因超时被终止`error`string执行失败时的错误信息（仅在失败时存在）

### 请求示例

```
curl -X POST "https://api.firecrawl.dev/v2/browser/550e8400-e29b-41d4-a716-446655440000/execute" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "await page.goto(\"https://example.com\")\ntitle = await page.title()\nprint(title)",
    "language": "python"
  }'
```

### 示例响应（成功）

```
{
  "success": true,
  "result": "Example Domain"
}
```

### 示例响应 (错误情况)

```
{
  "success": true,
  "error": "TimeoutError: page.goto: Timeout 30000ms exceeded."
}
```

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化接入说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 路径参数

#### 请求体

在浏览器沙箱中运行的代码

Required string length: `1 - 100000`

要执行代码的语言。使用 JavaScript 时填 `node`，使用 agent-browser CLI 命令时填 `bash`。

执行超时时长（秒）

必填范围: `1 <= x <= 300`

#### 响应