---
title: 智能体 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/api-reference/endpoint/agent
source: sitemap
fetched_at: 2026-03-23T07:09:54.862224-03:00
rendered_js: false
word_count: 51
summary: This document provides the API specifications for configuring Firecrawl agent tasks, including authentication methods, request body parameters, and model selection options.
tags:
    - api-documentation
    - firecrawl
    - agent-configuration
    - authentication
    - data-extraction
    - schema-definition
category: api
---

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化入门说明。

#### 授权

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### 请求体

用于描述应提取哪些数据的提示词

Maximum string length: `10000`

用于定义提取数据结构的可选 JSON Schema

此代理任务可使用的最大额度。若未设置，默认值为 2500。高于 2,500 的值一律按付费请求计费。

如果为 true，代理将仅访问 urls 数组中提供的 URL

model

enum&lt;string&gt;

默认值:spark-1-mini

适用于智能体任务的模型。spark-1-mini（默认）成本更低，价格便宜约 60%；spark-1-pro 在处理复杂任务时能提供更高的准确率。

可用选项:

`spark-1-mini`,

`spark-1-pro`

#### 响应