---
title: 在 ChatGPT 中使用 MCP 进行网页搜索与抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/mcp-setup-guides/chatgpt
source: sitemap
fetched_at: 2026-03-23T07:37:03.155305-03:00
rendered_js: false
word_count: 120
summary: This document provides step-by-step instructions for integrating the Firecrawl MCP server into ChatGPT to enable web scraping, crawling, and content search capabilities.
tags:
    - firecrawl
    - mcp-server
    - chatgpt-integration
    - web-scraping
    - ai-tools
    - developer-mode
category: guide
---

使用 Firecrawl MCP 为 ChatGPT 添加网页抓取和搜索功能。

## 快速开始

### 1. 获取你的 API 密钥

在 [firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys) 注册并复制你的 API 密钥。

### 2. 启用开发者模式

点击左下角的用户名打开 ChatGPT 设置，或者直接访问 [chatgpt.com/#settings](https://chatgpt.com/#settings)。 在设置弹窗中，滚动到页面底部并选择 **Advanced Settings（高级设置）**。将 **Developer mode（开发者模式）** 切换为开启。

### 3. 创建 Connector

启用 Developer 模式后，在同一个设置弹窗中打开 **Apps & Connectors** 选项卡。 点击页面右上角的 **Create** 按钮。

填写 Connector 详情：

- **Name：** `Firecrawl MCP`
- **Description：** `Web scraping, crawling, search, and content extraction`（可选）
- **MCP Server URL：** `https://mcp.firecrawl.dev/YOUR_API_KEY_HERE/v2/mcp`
- **Authentication：** `None`

将 URL 中的 `YOUR_API_KEY_HERE` 替换为你的实际 [Firecrawl API key](https://www.firecrawl.dev/app/api-keys)。

勾选 **“I understand and want to continue”** 复选框，然后点击 **Create**。

### 4. 验证设置

返回 ChatGPT 主界面。你应该会看到显示 **开发者模式（Developer mode）**，这表示 MCP 连接器已启用。 如果你没有看到开发者模式，请刷新页面。如果仍未出现，请再次打开设置，并在 Advanced Settings 中确认开发者模式的开关已打开。

要在对话中使用 Firecrawl，点击聊天输入框中的 **+** 按钮，然后选择 **More**，再选择 **Firecrawl MCP**。

## 快速演示

在选中 Firecrawl MCP 后，尝试使用以下提示词： **搜索：**

```
Search for the latest React Server Components updates
```

**抓取：**

```
Scrape firecrawl.dev and tell me what it does
```

**获取文档：**

```
抓取 Vercel 的 Edge Functions 文档并进行总结
```

当 ChatGPT 使用 Firecrawl MCP 工具时，你会看到一个确认提示，要求你进行授权。

你可以勾选 **“Remember for this conversation”**，以避免在同一聊天会话中重复确认。这个安全措施由 OpenAI 实施，以确保 MCP 工具不会执行非预期的 actions。 确认后，ChatGPT 会执行请求并返回结果。