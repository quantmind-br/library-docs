---
title: 智能体模型 | Firecrawl
url: https://docs.firecrawl.dev/zh/features/models
source: sitemap
fetched_at: 2026-03-23T07:20:30.55804-03:00
rendered_js: false
word_count: 81
summary: This document outlines the available Firecrawl Agent models, Spark 1 Mini and Spark 1 Pro, providing guidance on choosing the appropriate model based on task complexity, cost-efficiency, and accuracy requirements.
tags:
    - firecrawl
    - data-extraction
    - model-selection
    - api-configuration
    - agent-optimization
category: guide
---

Firecrawl Agent 提供两种针对不同场景优化的模型。请根据你的提取复杂度和成本要求选择合适的模型。

## 可用模型

ModelCostAccuracyBest For`spark-1-mini`**成本低 60%**标准适用于大多数任务 (默认)`spark-1-pro`标准更高复杂研究、关键数据抽取

## Spark 1 Mini (默认)

`spark-1-mini` 是我们的高效模型，适合处理简单直接的数据提取任务。 **在以下场景使用 Mini：**

- 提取简单数据点 (联系信息、价格等)
- 处理结构清晰的网站
- 需要优先考虑成本效率
- 需要运行高频、大批量提取任务

**示例用例：**

- 从电商网站提取产品价格
- 从公司页面收集联系信息
- 从文章中获取基础元数据
- 简单的数据点查询

## Spark 1 Pro

`spark-1-pro` 是我们的旗舰模型，专为在复杂提取任务中实现最高准确率而设计。 **在以下情况下使用 Pro：**

- 执行复杂的竞品分析
- 提取需要深度推理的数据
- 你的用例对准确性要求极高
- 处理模糊或难以获取的数据

**示例用例：**

- 多领域竞品分析
- 需要推理的复杂研究任务
- 从多个来源提取细微信息
- 关键业务情报收集

## 指定模型

通过传递 `model` 参数来选择要使用的模型：

## 模型对比

特性Spark 1 MiniSpark 1 Pro**成本**成本降低 60%标准**准确率**标准更高**速度**快速快速**最适合**大部分任务复杂任务**推理能力**标准高级**多领域能力**良好卓越

## 按模型计费

这两种模型都采用动态的积分制计费方式，费用会随任务复杂度变化：

- **Spark 1 Mini**：在完成等效任务时，积分消耗比 Pro 模型低约 60%
- **Spark 1 Pro**：标准积分消耗，提供最高精度

## 选择合适的模型

```
                    ┌─────────────────────────────────┐
                    │   任务类型?                      │
                    └─────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  简单/直接      │           │ 复杂/研究       │
          │  数据提取       │           │ 多域            │
          └─────────────────┘           └─────────────────┘
                    │                             │
                    ▼                             ▼
          ┌─────────────────┐           ┌─────────────────┐
          │  spark-1-mini   │           │  spark-1-pro    │
          │  (成本降低60%)  │           │  (更高精度)     │
          └─────────────────┘           └─────────────────┘
```

## API 参考

有关完整的参数说明，请参见 [Agent API Reference](https://docs.firecrawl.dev/zh/api-reference/endpoint/agent)。 对应该使用哪个模型有疑问？请发送邮件至 [help@firecrawl.com](mailto:help@firecrawl.com)。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化入门说明。