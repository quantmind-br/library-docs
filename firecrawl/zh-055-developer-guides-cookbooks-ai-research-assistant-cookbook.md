---
title: 使用 Firecrawl 与 AI SDK 构建 AI 研究助手 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/cookbooks/ai-research-assistant-cookbook
source: sitemap
fetched_at: 2026-03-23T07:34:11.528744-03:00
rendered_js: false
word_count: 157
summary: This document provides a technical guide on building an AI-powered research assistant using the AI SDK, Firecrawl, and OpenAI to perform automated web searching and scraping.
tags:
    - ai-sdk
    - web-scraping
    - chat-assistant
    - tool-calling
    - next-js
    - firecrawl
category: guide
---

构建一款完整的 AI 驱动研究助手，能够抓取网站并在网上搜索来回答问题。助手会自动判断何时使用网页抓取或搜索工具来收集信息，并基于汇总的数据提供全面的答案。 ![AI 研究助手聊天界面，展示使用 Firecrawl 实时进行网页抓取以及由 OpenAI 驱动的对话式回复](https://mintcdn.com/firecrawl/GKat0bF5SiRAHSEa/images/guides/cookbooks/ai-sdk-cookbook/firecrawl-ai-sdk-chatbot.gif?s=cfcbad69aa3f087a474414c0763a260b)

## 你将构建的内容

一个 AI 聊天界面，用户可以就任意主题提问。AI 助手会自动判断何时使用网页爬取或搜索工具收集信息，并基于所获取的数据提供全面答案。

## 前置条件

- 已安装 Node.js 18 或更高版本
- 来自 [platform.openai.com](https://platform.openai.com) 的 OpenAI API 密钥
- 来自 [firecrawl.dev](https://firecrawl.dev) 的 Firecrawl API 密钥
- 具备 React 和 Next.js 的基础知识

## 工作机制

### 消息流

1. **用户发送消息**：用户输入问题并点击提交
2. **前端发送请求**：`useChat` 携带所选模型和网页搜索设置，将消息发送到 `/api/chat`
3. **后端处理消息**：API 路由接收消息并调用 `streamText`
4. **AI 选择工具**：模型分析问题并决定是否使用 `scrapeWebsite` 或 `searchWeb`（仅在启用网页搜索时）
5. **工具执行**：若调用了工具，Firecrawl 将执行网页抓取或搜索
6. **AI 生成响应**：模型分析工具结果并生成自然语言响应
7. **前端展示结果**：UI 实时显示工具调用与最终响应

AI SDK 的工具调用系统（[ai-sdk.dev/docs/foundations/tools](https://ai-sdk.dev/docs/foundations/tools)）工作方式如下：

1. 模型接收用户消息和可用的工具描述
2. 如果模型判断需要使用工具，则生成带参数的工具调用
3. SDK 使用这些参数执行工具函数
4. 将工具结果返回给模型
5. 模型基于结果生成最终响应

以上过程会在一次 `streamText` 调用中自动完成，并将结果实时流式传输到前端。

## 核心功能

### 模型选择

该应用支持多种 OpenAI 模型：

- **GPT-5 Mini（Thinking）**：OpenAI 的新近模型，具备更强的推理能力
- **GPT-4o Mini**：速度快、成本友好的模型

用户可以通过下拉菜单在不同模型之间切换。

### Web Search 开关

Search 按钮用于控制 AI 是否可以使用 Firecrawl 工具：

- **启用**：AI 可按需调用 `scrapeWebsite` 和 `searchWeb` 工具
- **禁用**：AI 仅基于其训练知识作答

这让用户可以掌控何时使用网页数据，而非依赖模型的内置知识。

## 自定义方案思路

使用其他工具扩展助手：

- 查询公司内部数据的数据库
- 集成 CRM 以获取客户信息
- 发送电子邮件
- 生成文档

每个工具遵循相同模式：使用 Zod 定义模式（schema），实现 execute 函数，并将其注册到 `tools` 对象中。

### 更换 AI 模型

将 OpenAI 切换为其他供应商：

```
import { anthropic } from "@ai-sdk/anthropic";

const result = streamText({
  model: anthropic("claude-4.5-sonnet"),
  // ... 其余配置
});
```

AI SDK 通过同一套 API 支持 20 多家提供商。了解更多：[ai-sdk.dev/docs/foundations/providers-and-models](https://ai-sdk.dev/docs/foundations/providers-and-models)。

### 自定义 UI

AI Elements 组件基于 shadcn/ui 构建，因此你可以：

- 在组件文件中修改组件样式
- 为现有组件添加新的变体
- 创建符合设计系统的自定义组件

## 最佳实践

1. **使用合适的工具**：优先用 `searchWeb` 搜索相关页面，单页用 `scrapeWebsite`，或交由 AI 决定
2. **监控 API 使用**：跟踪你的 Firecrawl 与 OpenAI API 使用量，以避免意外开销
3. **优雅处理错误**：工具内置错误处理，但建议补充面向用户的错误提示
4. **优化性能**：使用流式输出提供即时反馈，并考虑缓存高频访问的内容
5. **设置合理的限制**：通过 `stopWhen: stepCountIs(5)` 避免过多工具调用与成本失控

* * *