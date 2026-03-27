---
title: 在 Cursor 中使用 MCP 实现网页搜索与抓取 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/mcp-setup-guides/cursor
source: sitemap
fetched_at: 2026-03-23T07:32:05.342391-03:00
rendered_js: false
word_count: 84
summary: This document provides instructions for integrating the Firecrawl MCP server into the Cursor IDE to enable web crawling and search capabilities.
tags:
    - firecrawl
    - mcp
    - cursor-ide
    - web-crawling
    - automation
    - api-integration
    - development-tools
category: configuration
---

使用 Firecrawl MCP 为 Cursor 接入网页抓取与搜索功能。

## 快速安装

### 1. 获取 API 密钥

在 [firecrawl.dev/app](https://firecrawl.dev/app) 注册并复制你的 API 密钥。

### 2. 添加到 Cursor

打开设置（`Cmd+,`），搜索 “MCP”，并添加：

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

将 `your_api_key_here` 替换为你的实际 Firecrawl API 密钥。

### 3. 重启 Cursor

完成！现在你可以在 Cursor 中搜索并爬取网页了。

## 快速演示

在 Cursor Chat（`Cmd+K`）中试试以下操作： **搜索：**

**爬取：**

```
抓取 firecrawl.dev 并告诉我它是做什么的
```

**查看文档：**

```
抓取 React hooks 文档并解释 useEffect
```

Cursor 将自动使用 Firecrawl 工具。

## Windows 故障排查

如果你在 Windows 上看到 `spawn npx ENOENT` 或 “No server info found” 错误，说明 Cursor 在你的 PATH 中找不到 `npx`。请尝试以下任一解决方案： **选项 A：使用 `npx.cmd` 的完整路径** 在命令提示符中运行 `where npx` 获取完整路径，然后更新你的配置：

```
{
  "mcpServers": {
    "firecrawl": {
      "command": "C:\\Program Files\\nodejs\\npx.cmd",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

将 `command` 路径替换为 `where npx` 命令的输出。 **选项 B：使用远程托管的 URL（无需 Node.js）**

```
{
  "mcpServers": {
    "firecrawl": {
      "url": "https://mcp.firecrawl.dev/YOUR-API-KEY/v2/mcp"
    }
  }
}
```

将 `YOUR-API-KEY` 替换为你的 Firecrawl API 密钥。