---
title: 深度研究 - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/use-cases/deep-research
source: sitemap
fetched_at: 2026-03-23T07:28:28.304211-03:00
rendered_js: false
word_count: 88
summary: This document outlines how to use Firecrawl's research mode to build automated systems that search, scrape, and synthesize data from multiple web sources using iterative LLM analysis.
tags:
    - web-scraping
    - automated-research
    - data-extraction
    - llm-integration
    - search-api
    - research-tools
category: guide
---

学术研究人员和分析师使用 Firecrawl 的深度研究模式，可自动汇聚来自数百个来源的数据。

## 从模板入手

**从多个研究模板中进行选择。** 克隆仓库、配置你的 API 密钥，即可开始研究。

## 工作原理

构建强大的研究工具，将分散的网页数据转化为全面洞察。其核心模式是 **search → scrape → analyze → repeat** 循环：使用 Firecrawl 的 search API 发现相关来源，scrape 每个来源以获取完整内容，然后将结果输入 LLM，以综合分析结果并识别后续查询。

搜索信息源

使用 `/search` 端点查找与你的研究主题相关的页面。

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

results = firecrawl.search(
    "recent advances in quantum computing",
    limit=5,
    scrape_options={"formats": ["markdown", "links"]}
)
```

抓取已发现的页面

从每个结果中提取完整内容，以获取带引用的详细信息。

```
for result in results:
    doc = firecrawl.scrape(result["url"], formats=["markdown"])
    # 将 doc 内容输入 LLM 进行分析
```

分析并迭代

使用 LLM 整合发现、识别缺口并生成后续查询。重复这一循环，直到你的研究问题得到完整解答。

### 将研究从数周加速到数小时

构建自动化研究系统，跨全网发现、阅读并综合信息。打造可输出含完整引用的全面报告的工具，免去在数百个来源中手动检索。

### 确保研究完整性

降低遗漏关键信息的风险。构建能够沿引文链追溯、发现相关来源，并揭示传统搜索方法常常忽略的洞见的系统。

## 研究工具功能

- **迭代式探索**：构建可自动发现相关主题与来源的工具
- **多源融合**：汇聚并整合来自数百个网站的信息
- **引用保真**：在研究成果中保留完整的来源标注
- **智能摘要**：提取用于分析的关键发现与洞见
- **趋势识别**：从多来源中识别跨站模式

## 常见问题

如何用 Firecrawl 构建研究工具？

使用 Firecrawl 的 /crawl 和 /search 端点构建迭代式研究系统。以搜索结果为起点，从相关页面提取内容，跟进引用链接，并汇总结论。结合 LLM 生成结构化的综合研究报告。

Firecrawl 能处理学术和科研网站吗？

可以。Firecrawl 能从开放获取的研究论文、学术网站和公开发布的科学文献中提取数据，并保留格式、引用与研究所需的技术内容。

如何确保研究数据的准确性？

Firecrawl 保留来源标注，并按网站原样提取内容。所有数据都包含来源 URL 和时间戳，确保研究用途的完整可追溯性。

可以将 Firecrawl 用于纵向研究吗？

可以。设置定时爬取以跟踪信息随时间的变化，非常适合监测趋势、政策变动或任何需要时间序列分析的研究。

Firecrawl 如何应对大规模研究项目？

我们的爬取基础设施可横向扩展，能同时处理成千上万的来源。无论是在分析整个行业还是跟踪全球趋势，Firecrawl 都能提供所需的数据管道。

## 相关用例

- [AI 平台](https://docs.firecrawl.dev/zh/use-cases/ai-platforms) - 构建 AI 研究助手
- [内容生成](https://docs.firecrawl.dev/zh/use-cases/content-generation) - 基于研究的内容生成
- [竞争情报](https://docs.firecrawl.dev/zh/use-cases/competitive-intelligence) - 市场情报