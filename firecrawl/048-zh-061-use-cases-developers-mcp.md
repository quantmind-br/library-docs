---
title: 开发者与 MCP - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/use-cases/developers-mcp
source: sitemap
fetched_at: 2026-03-23T07:28:25.00086-03:00
rendered_js: false
word_count: 67
summary: This document explains how to integrate Firecrawl's web scraping capabilities into AI coding assistants like Claude Desktop and Cursor using the Model Context Protocol (MCP).
tags:
    - firecrawl
    - mcp
    - web-scraping
    - ai-assistants
    - data-extraction
    - workflow-automation
category: guide
---

开发者可使用 Firecrawl 的 MCP 服务器，将网页抓取功能接入 Claude Desktop、Cursor 等 AI 编码助手。

## 从模板开始

## 工作原理

通过模型上下文协议 (MCP) 将 Firecrawl 直接集成到你的 AI 编码工作流中。配置完成后，你的 AI 助手即可使用一组可代你调用的网页抓取工具：

ToolWhat it does**Scrape**从单个 URL 提取内容或结构化数据**Batch Scrape**并行从多个已知 URL 中提取内容**Map**发现某个网站上所有已编入索引的 URL**Crawl**遍历网站的某个部分，并从每个页面提取内容**Search**搜索网页，并可选地从结果中提取内容

你的助手会自动选择合适的工具——让它“读取 Next.js 文档”，它会执行抓取；让它“查找 example.com 上的所有博客文章”，它会先执行 map，再执行 batch scrape。

### 构建更智能的 AI 助手

为你的 AI 提供对文档、API 和网页资源的实时访问。通过为助手提供最新数据，减少过时内容和幻觉。

### 无需任何基础设施

无需管理服务器，也无需维护爬虫。只需一次配置，你的 AI 助手即可通过模型上下文协议 (MCP) 即时访问网站。

## 客户案例

## 常见问题

- [AI Platforms](https://docs.firecrawl.dev/zh/use-cases/ai-platforms) - 构建 AI 驱动的开发工具
- [Deep Research](https://docs.firecrawl.dev/zh/use-cases/deep-research) - 复杂技术研究
- [Content Generation](https://docs.firecrawl.dev/zh/use-cases/content-generation) - 生成文档