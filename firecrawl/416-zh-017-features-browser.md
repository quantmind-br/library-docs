---
title: 浏览器 | Firecrawl
url: https://docs.firecrawl.dev/zh/features/browser
source: sitemap
fetched_at: 2026-03-23T07:20:55.082552-03:00
rendered_js: false
word_count: 249
summary: Firecrawl Browser Sandbox 提供了一个托管的、隔离的浏览器环境，允许 AI 智能体通过 API、SDK 或 CLI 执行复杂的 Web 交互操作而无需本地配置。
tags:
    - browser-automation
    - headless-browser
    - ai-agents
    - playwright
    - web-scraping
    - sandbox-environment
    - api-integration
category: guide
---

Firecrawl Browser Sandbox 为你的智能体提供一个安全的浏览器环境，使智能体能够与 Web 交互。可以填写表单、点击按钮、进行身份验证等。 无需本地配置、无需安装 Chromium，也不存在驱动兼容性问题。环境中已预装 agent-browser 和 Playwright。 可通过 [API](https://docs.firecrawl.dev/zh/api-reference/endpoint/browser-create)、[CLI](https://docs.firecrawl.dev/zh/sdks/cli#browser) (Bash / agent-browser、Python、Node)、[Node SDK](https://docs.firecrawl.dev/zh/sdks/node#browser)、[Python SDK](https://docs.firecrawl.dev/zh/sdks/python#browser)、[Vercel AI SDK](https://docs.firecrawl.dev/zh/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk) 和 [MCP Server](https://docs.firecrawl.dev/zh/mcp-server) 使用。 要为 AI 代码智能体 (Claude Code、Codex、Open Code、Cursor 等) 添加浏览器支持，请安装 Firecrawl 技能：

```
npx -y firecrawl-cli@latest init --all --browser
```

每个会话都在隔离的一次性或持久化沙箱中运行，并且可在无需管理基础设施的情况下进行扩展。

## 快速开始

创建会话，执行代码，然后关闭它：

- **无需安装驱动** - 无需 Chromium 二进制文件，无需 `playwright install`，也没有驱动兼容性问题
- **Python、JavaScript 和 Bash** - 通过 API、CLI 或 SDK 发送代码并获取结果。三种语言都会在远程沙盒中运行
- **agent-browser** - 预装的 CLI，内置 60+ 条命令。AI 代理只需编写简单的 Bash 命令，无需编写 Playwright 代码
- **已加载 Playwright** - Playwright 已预装在沙盒中。代理如果愿意，也可以编写 Playwright 代码。
- **CDP 访问** - 当你需要完全控制时，可通过 WebSocket 连接你自己的 Playwright 实例
- **实时视图** - 通过可嵌入的流 URL 实时查看会话
- **交互式实时视图** - 通过可嵌入的交互式流，让用户直接与浏览器交互

## 启动一个会话

返回会话 ID、CDP URL 和实时视图 URL。

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}
```

## 执行代码

在会话中运行 Python、JavaScript 或 bash 代码。输出通过 `stdout` 返回；对于 Node.js，最后一个表达式的值也可在 `result` 中获得。

```
{
  "success": true,
  "stdout": "",
  "result": "Example Domain",
  "stderr": "",
  "exitCode": 0,
  "killed": false
}
```

### 处理文件下载

在会话中下载的文件可以捕获并以 base64 形式返回。可通过 execute 端点使用 Playwright 的下载 API：

## agent-browser (Bash 模式)

[agent-browser](https://github.com/vercel-labs/agent-browser) 是一个无头浏览器 CLI，已预装在每个沙箱中。智能体无需编写 Playwright 代码，只需发送简单的 bash 命令。CLI 会自动注入 `--cdp`，使 agent-browser 自动连接到你的当前会话。

### 简写

这是使用 browser 的最快方式。简写和 `execute` 都会自动将命令发送给 agent-browser。简写只是跳过了 `execute`，并在需要时自动启动会话：

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
firecrawl browser "click @e5"
```

### CLI

显式用法使用 `execute` 命令。命令会自动发送到 agent-browser —— 无需手动输入 `agent-browser` 或使用 `--bash`：

### API 与 SDK

使用 `language: "bash"`，通过 API 或 SDK 执行 agent-browser 命令：

## 会话管理

### 持久化会话

默认情况下，每个浏览器会话都会从全新环境开始。通过 `profile`，你可以在会话之间保存并复用浏览器状态。这对于保持登录状态和保留偏好设置非常有用。 若要保存或选择某个持久化配置文件，请在创建会话时使用 `profile` 参数。

参数默认值描述`name`—持久化配置文件的名称。使用相同名称的会话会共享存储。`saveChanges``true`当为 `true` 时，浏览器状态会在关闭时保存回该配置文件。将其设置为 `false` 可在不写入的情况下加载已有数据——在需要多个并发只读访问时很有用。

浏览器会话状态只有在会话关闭时才会保存。因此，我们建议在使用完成后关闭浏览器会话，以便后续复用。会话一旦关闭，其会话 ID 将不再有效——你无法再次使用它。请改为使用相同的配置文件名称创建一个新会话，并使用响应中返回的新会话 ID。要保存并关闭会话：

### 列出会话

```
{
  "success": true,
  "sessions": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "status": "active",
      "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
      "liveViewUrl": "https://liveview.firecrawl.dev/...",
      "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
      "createdAt": "2025-01-15T10:30:00Z",
      "lastActivity": "2025-01-15T10:35:00Z"
    }
  ]
}
```

### TTL 配置

会话有两个 TTL 参数：

参数默认值描述`ttl`600s (10 分钟)会话的最长存续时间 (30-3600s)`activityTtl`300s (5 分钟)会话空闲达到该时长后自动关闭 (10-3600s)

### 结束会话

## 实时视图

每个会话的响应中都会包含一个 `liveViewUrl`，你可以将其嵌入以实时查看浏览器行为。适用于调试、演示或构建由浏览器驱动的 UI。

```
{
  "success": true,
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "cdpUrl": "wss://browser.firecrawl.dev/cdp/550e8400...?token=abc123...",
  "liveViewUrl": "https://liveview.firecrawl.dev/...",
  "interactiveLiveViewUrl": "https://liveview.firecrawl.dev/...",
  "expiresAt": "2025-01-15T10:40:00Z"
}

<iframe src="LIVE_VIEW_URL" width="100%" height="600" />
```

### 交互式实时视图

响应中还包含一个 `interactiveLiveViewUrl`。与仅支持查看的标准实时视图不同，交互式实时视图允许用户通过嵌入的流直接点击、输入并与浏览器会话进行交互。这对于构建面向用户的浏览器界面、协同调试，或任何需要查看者直接控制浏览器的场景都非常有用。

```
<iframe src="INTERACTIVE_LIVE_VIEW_URL" width="100%" height="600" />
```

## 通过 CDP 连接

每个会话都会暴露一个 CDP WebSocket URL。execute API 和 `--bash` 参数覆盖了大多数用例，但如果你需要完全的本地控制，可以直接进行连接。

## 何时使用浏览器

使用场景合适工具从已知 URL 提取内容[Scrape](https://docs.firecrawl.dev/zh/features/scrape)在网上搜索并获取结果[Search](https://docs.firecrawl.dev/zh/features/search)执行分页导航、填写表单、点击操作流程**浏览器**包含交互的多步工作流**浏览器**在多个网站上并行浏览**浏览器** (每个会话彼此隔离)

## 使用场景

- **竞争情报** - 浏览竞争对手网站，操作搜索表单和筛选器，将价格和功能信息提取为结构化数据
- **知识库接入** - 浏览需要点击操作、分页或登录认证的帮助中心、文档和支持门户
- **市场调研** - 启动并行浏览器会话，从招聘网站、房产列表或法律数据库中构建数据集

## 价格

计费简单明了：每个浏览器使用分钟 2 个积分。免费用户可享有 5 小时的免费使用额度。

## 速率限制

在初始发布阶段，所有套餐均支持最多 20 个并发浏览器会话。

## API 参考文档

- [创建浏览器会话](https://docs.firecrawl.dev/zh/api-reference/endpoint/browser-create)
- [执行浏览器代码](https://docs.firecrawl.dev/zh/api-reference/endpoint/browser-execute)
- [列出浏览器会话](https://docs.firecrawl.dev/zh/api-reference/endpoint/browser-list)
- [删除浏览器会话](https://docs.firecrawl.dev/zh/api-reference/endpoint/browser-delete)

* * *

有反馈或需要帮助？请发送邮件至 [help@firecrawl.com](mailto:help@firecrawl.com) 或在 [Discord](https://discord.gg/firecrawl) 上联系我们。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化引导说明。