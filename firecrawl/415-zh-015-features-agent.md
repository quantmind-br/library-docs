---
title: Agent | Firecrawl
url: https://docs.firecrawl.dev/zh/features/agent
source: sitemap
fetched_at: 2026-03-23T07:20:42.026204-03:00
rendered_js: false
word_count: 280
summary: This document introduces the Firecrawl /agent API, a tool designed for autonomous web research, navigation, and structured data extraction without requiring predefined scripts.
tags:
    - firecrawl
    - ai-agent
    - web-scraping
    - data-extraction
    - api-reference
    - structured-data
    - automation
category: api
---

Firecrawl `/agent` 是一个魔法般的 API，它可以在最广泛的网站范围内进行搜索、导航并收集数据，在难以触及的角落中找到数据，并以其他任何 API 都无法做到的方式发掘信息。它可以在几分钟内完成原本需要人类耗费数小时的工作——从端到端的数据采集，全程无需脚本或人工操作。 无论你只需要一个数据点，还是需要大规模的完整数据集，Firecrawl `/agent` 都能为你获取这些数据。 **把 `/agent` 想象成：无论数据藏在哪里，它都能替你做深度调研！**

Agent 构建于 `/extract` 的全部优势之上，并在此基础上更进一步：

- **无需提供 URL**：只需通过 `prompt` 参数描述你的需求，URL 是可选的。
- **深度网页搜索**：自主搜索并深入浏览站点以找到所需数据
- **可靠且准确**：适用于多种类型的查询和使用场景
- **更快**：并行处理多个数据源以更快返回结果

唯一必需的参数是 `prompt`。只需描述你想要提取的数据。要获得结构化输出，请提供一个 JSON schema。SDK 支持使用 Pydantic (Python) 和 Zod (Node) 来定义类型安全的 schema：

### 响应

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder",
        "background": "Previously at Mendable"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

## 提供 URL (可选)

你可以选择提供 URL，让 agent 专注于特定页面：

## 任务状态与完成

Agent 任务以异步方式运行。提交任务后，你会收到一个 Job ID，用于检查任务状态：

- **默认方式**：`agent()` 会阻塞等待，并返回最终结果
- **先启动再轮询**：使用 `start_agent` (Python) 或 `startAgent` (Node) 立即获取 Job ID，然后通过 `get_agent_status` / `getAgentStatus` 进行轮询

### 可能的状态

状态描述`processing`代理仍在处理你的请求`completed`提取已成功完成`failed`提取过程中发生错误`cancelled`用户取消了该任务

#### 等待中示例

```
{
  "success": true,
  "status": "processing",
  "expiresAt": "2024-12-15T00:00:00.000Z"
}
```

#### 已完成示例

```
{
  "success": true,
  "status": "completed",
  "data": {
    "founders": [
      {
        "name": "Eric Ciarla",
        "role": "Co-founder"
      },
      {
        "name": "Nicolas Camara",
        "role": "Co-founder"
      },
      {
        "name": "Caleb Peffer",
        "role": "Co-founder"
      }
    ]
  },
  "expiresAt": "2024-12-15T00:00:00.000Z",
  "creditsUsed": 15
}
```

你可以直接在 Agent playground 中分享代理运行记录。共享链接是公开的，任何拥有链接的人都可以查看运行输出和活动；你也可以随时撤销访问权限以停用该链接。共享页面不会被搜索引擎收录。

## 模型选择

Firecrawl Agent 提供两种模型。**Spark 1 Mini 成本低 60%**，并且是默认选项——适用于大多数使用场景。当你在复杂任务上需要最高准确率时，再升级到 Spark 1 Pro。

ModelCostAccuracyBest For`spark-1-mini`**成本低 60%**标准大多数任务 (默认)`spark-1-pro`标准更高复杂调研、关键数据抽取

### Spark 1 Mini (默认)

`spark-1-mini` 是我们的高效模型，非常适合简单直接的数据提取任务。 **在以下情况下使用 Mini：**

- 提取简单数据点 (联系方式、价格信息等)
- 处理结构清晰的网站
- 需要优先考虑成本效率
- 运行大批量提取任务时

### Spark 1 Pro

`spark-1-pro` 是我们的旗舰模型，专为在复杂数据提取任务中实现最高准确率而设计。 **在以下场景使用 Pro：**

- 进行复杂的竞品分析
- 提取需要深入推理的数据
- 你的用例对准确性要求极高
- 处理模糊或难以获取的数据

### 指定模型

通过传入 `model` 参数来选择要使用的模型：

## 参数

参数类型必填描述`prompt`string**是**用自然语言描述你想要提取的数据 (最多 10,000 个字符)`model`string否要使用的模型：`spark-1-mini` (默认) 或 `spark-1-pro``urls`array否可选的 URL 列表，用于聚焦提取`schema`object否用于结构化输出的可选 JSON schema`maxCredits`number否此代理任务中可花费的最大额度数。如果未设置，默认值为 **2,500**。Dashboard 最高支持 **2,500**；如需更高上限，请通过 API 设置 `maxCredits` (高于 2,500 的值始终按付费请求处理) 。如果达到上限，任务会失败，并且**不会返回任何数据**，但已执行工作的已消耗额度仍会计费。

特性Agent (新)Extract是否需要提供 URL否是速度更快标准成本更低标准可靠性更高标准查询灵活性高中等

## 示例用例

- **调研**: “找出前 5 家 AI 初创公司及其融资金额”
- **竞品分析**: “比较 Slack 和 Microsoft Teams 的定价方案”
- **数据收集**: “从公司网站中提取联系方式”
- **内容摘要**: “总结关于网页抓取的最新博客文章”

## 在 Agent Playground 中上传 CSV

[Agent Playground](https://www.firecrawl.dev/app/agent) 支持通过上传 CSV 进行批量处理。你的 CSV 可以包含一列或多列输入数据。例如：一列公司名称，或者多列数据，如公司名称、产品和网站 URL。每一行都代表一个需要由 Agent 处理的条目。 上传你的 CSV，编写一个提示词，描述你希望 Agent 针对每一行获取哪些数据，定义输出字段，然后运行。Agent 会并行处理每一行并填充结果。

## API 参考

请参阅 [Agent API Reference](https://docs.firecrawl.dev/zh/api-reference/endpoint/agent) 以了解更多详情。 有反馈或需要帮助？请发送邮件至 [help@firecrawl.com](mailto:help@firecrawl.com)。

## 价格

Firecrawl Agent 使用 **动态计费** 模式，费用会随你的数据提取请求复杂度而变化。你根据 Agent 实际完成的工作量付费，无论是提取简单的数据点，还是从多个来源获取复杂的结构化信息，都能享受公平的定价。

### Agent 计费方式

在 Research Preview 阶段，Agent 的计费是**动态的、基于 credit 的**：

- **简单抽取任务** (例如从单个页面提取联系方式) 通常消耗更少的 credits，成本更低
- **复杂研究任务** (例如对多个域名进行竞品分析) 会消耗更多 credits，但更能体现整体投入的工作量
- **用量透明**会清楚展示每个请求具体消耗了多少 credits
- **Credit 换算**会自动将 Agent 的 credit 使用量换算为 credits，便于计费

### 并行 Agent 计费

如果你使用 Spark-1 Fast 并行运行多个 agent，费用会更加可预测：每个 cell 消耗 10 个积分。

### 入门

**所有用户**每天都会获得**5 次免费运行**，可以通过 playground 或 API 使用，用于在无需付费的情况下体验 Agent 的功能。 额外用量会根据 credit 消耗计费，并换算为 credits。

### 成本管理

代理可能会比较昂贵，但有一些方法可以降低成本：

- **从免费运行开始**：利用你每天 5 次免费请求来了解定价
- **设置 `maxCredits` 参数**：通过设置你愿意花费的最大额度数来限制支出。Dashboard 将此上限设为 2,500 额度；若要设置更高的上限，请直接通过 API 使用 `maxCredits` 参数 (注意：高于 2,500 的值始终按付费请求计费)
- **优化提示词**：更具体的提示词通常会消耗更少的额度
- **监控用量**：通过 Dashboard 追踪你的使用情况
- **设定预期**：跨多个站点/领域的复杂研究会比简单的单页提取消耗更多额度

现在访问 [firecrawl.dev/app/agent](https://www.firecrawl.dev/app/agent) 试用代理，看看在你的具体用例下额度的使用如何随规模变化。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化引导说明。