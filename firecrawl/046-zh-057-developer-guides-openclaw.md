---
title: 将 OpenClaw 与 Firecrawl 搭配使用
url: https://docs.firecrawl.dev/zh/developer-guides/openclaw
source: sitemap
fetched_at: 2026-03-23T07:31:03.164269-03:00
rendered_js: false
word_count: 111
summary: This document outlines how to integrate Firecrawl CLI with OpenClaw to equip AI agents with web crawling, searching, and remote browser automation capabilities.
tags:
    - firecrawl
    - openclaw
    - web-scraping
    - ai-agents
    - browser-automation
    - cli-tools
category: guide
---

将 Firecrawl 集成到 OpenClaw 中，为你的智能体提供抓取、搜索、爬取、提取以及与网页交互的能力——全部通过 [Firecrawl CLI](https://docs.firecrawl.dev/zh/sdks/cli) 完成。

- **无需本地浏览器** —— 每个会话都在远程、隔离的沙箱中运行。无需安装 Chromium、无需处理驱动冲突，也不会给你的机器带来内存压力。
- **真正的并行能力** —— 可同时运行多个浏览器会话，而不会争抢本地资源。Agent 可以成批并行浏览多个站点。
- **默认即安全** —— 导航、DOM 评估和内容抽取都在可丢弃的沙箱环境中完成，而不是在你的工作站上。
- **更优的 Token 使用效率** —— Agent 获取的是干净的结果产物 (快照、抽取字段) ，而不是把巨大的 DOM 和驱动日志放入上下文窗口。
- **完整的 Web 工具集** —— 通过一个你的 Agent 已经会用的单一 CLI 完成抓取、搜索和浏览器自动化。

## 设置

让你的 Agent 安装 Firecrawl CLI，完成身份验证，并通过以下命令初始化该技能：

```
npx -y firecrawl-cli init --browser --all
```

- `--all` 会将 Firecrawl 技能安装到所有已检测到的 AI 编码 Agent 上
- `--browser` 会自动打开浏览器以完成 Firecrawl 身份验证

或者分别安装所有组件：

```
npm install -g firecrawl-cli
firecrawl init skills
firecrawl login --browser
# 或者，跳过浏览器，直接提供您的 API 密钥：
export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"
```

验证一切是否已正确配置：

## 抓取

爬取单个页面并提取其中的内容：

```
firecrawl https://example.com --only-main-content
```

获取指定 formats：

```
firecrawl https://example.com --format markdown,links --pretty
```

## 搜索

在网上搜索，并可选择抓取搜索结果：

```
firecrawl search "latest AI funding rounds 2025" --limit 10

# 搜索并抓取结果
firecrawl search "OpenClaw documentation" --scrape --scrape-formats markdown
```

## 浏览器

启动远程浏览器会话，用于交互式自动化。每个会话都在隔离的沙箱环境中运行——无需在本地安装 Chromium。`agent-browser` 预装了 40 多个命令。

```
# 简写形式：若无活跃会话，则自动启动一个
firecrawl browser "open https://news.ycombinator.com"
firecrawl browser "snapshot"
firecrawl browser "scrape"
firecrawl browser close
```

使用快照中的引用 (ref) 与页面元素进行交互：

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
# snapshot 返回 @ref ID — 使用它们与页面元素交互
firecrawl browser "click @e5"
firecrawl browser "fill @e3 'search query'"
firecrawl browser "scrape"
firecrawl browser close
```

## 示例：告诉你的 Agent

以下是一些你可以给 OpenClaw agent 的提示词：

- *「使用 Firecrawl 抓取 [https://example.com，并总结主要内容。」](https://example.com%EF%BC%8C%E5%B9%B6%E6%80%BB%E7%BB%93%E4%B8%BB%E8%A6%81%E5%86%85%E5%AE%B9%E3%80%82%E3%80%8D)*
- *「搜索最新的 OpenAI 新闻，并给我前 5 条结果的摘要。」*
- *「使用 Firecrawl Browser 打开 Hacker News，获取排名前 5 的帖子，以及每个帖子的前 10 条评论。」*
- *「爬取 [https://docs.firecrawl.dev](https://docs.firecrawl.dev) 上的文档，并将其保存到文件中。」*

## 延伸阅读

- [Firecrawl CLI 参考文档](https://docs.firecrawl.dev/zh/sdks/cli)
- [Browser Sandbox 文档](https://docs.firecrawl.dev/zh/features/browser)
- [Agent 文档](https://docs.firecrawl.dev/zh/features/agent)