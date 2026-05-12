---
title: Firecrawl + Dify - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/workflow-automation/dify
source: sitemap
fetched_at: 2026-03-23T07:37:09.253311-03:00
rendered_js: false
word_count: 60
summary: This document details how to integrate the Firecrawl plugin into Dify to enable web scraping and crawling capabilities within AI workflows, agents, and automated data pipelines.
tags:
    - dify
    - firecrawl
    - web-scraping
    - llm-workflows
    - ai-agents
    - data-extraction
category: guide
---

Dify 是一个开源的 LLM 应用开发平台。官方 Firecrawl 插件可让你在 AI 工作流中直接进行网页爬取与抓取。

## 快速上手

## 使用模式

- Chatflow Apps
- Workflow Apps
- Agent Apps

**可视化流水线集成**

1. 将 Firecrawl 节点添加到你的流水线
2. 选择操作（Map、Crawl、Scrape）
3. 定义输入变量
4. 按顺序执行流水线

**示例流程：**

```
用户输入 → Firecrawl（Scrape）→ LLM 处理 → 返回结果
```

**自动化数据处理**构建多步工作流，包括：

- 定时抓取
- 数据转换
- 数据库存储
- 通知

**示例流程：**

```
定时触发 → Firecrawl（Crawl）→ 数据处理 → 存储
```

**AI 驱动的网页访问**为智能体提供实时网页抓取能力：

1. 将 Firecrawl 工具添加到智能体
2. 智能体自主决定何时抓取
3. LLM 分析提取内容
4. 智能体给出有依据的响应

**使用场景：** 客服智能体引用实时文档

## 常见用例

## Firecrawl actions

工具描述最适合**Scrape**单页数据抽取快速捕获内容**Crawl**多页递归爬取全站抽取**Map**发现 URL 并生成站点地图SEO 分析、URL 清单**Crawl Job**异步任务管理长时运行的操作

## 最佳实践

## Dify 与其他平台对比

功能DifyMakeZapiern8n**类型**LLM 应用平台工作流自动化工作流自动化工作流自动化**最适合**AI Agent 与聊天机器人可视化工作流快速自动化开发者掌控**定价**开源 + 云端按操作计费按任务计费固定月费**AI 原生**是部分部分部分**自托管**是否否是