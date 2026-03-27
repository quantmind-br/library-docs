---
title: 增强模式 | Firecrawl
url: https://docs.firecrawl.dev/zh/features/enhanced-mode
source: sitemap
fetched_at: 2026-03-23T07:20:34.309366-03:00
rendered_js: false
word_count: 46
summary: This document explains how to configure proxy settings in Firecrawl to manage web scraping requests, including descriptions of available proxy types and their associated costs.
tags:
    - firecrawl
    - web-scraping
    - proxy-configuration
    - api-usage
    - data-extraction
category: configuration
---

Firecrawl 提供不同类型的代理服务，帮助你抓取不同复杂程度的网站。设置 `proxy` 参数，以控制请求使用哪种代理策略。

## 代理类型

Firecrawl 支持三种代理类型：

类型描述速度成本`basic`适用于大多数网站的标准代理快1 额度`enhanced`适用于复杂网站的增强代理较慢每次请求 5 额度`auto`先尝试 `basic`，失败后再使用 `enhanced` 重试视情况而定如果 `basic` 成功，则为 1 额度；如果需要 `enhanced`，则为 5 额度

如果未指定代理，Firecrawl 默认使用 `auto`。

## 基本用法

设置 `proxy` 参数以选择代理策略。以下示例使用 `auto`，让 Firecrawl 决定何时升级到增强代理。

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')

# 选择代理类型：'basic' | 'enhanced' | 'auto'
doc = firecrawl.scrape('https://example.com', formats=['markdown'], proxy='auto')

print(doc.warning or 'ok')
```

增强代理请求**每次请求 5 额度**。使用 `auto` 时，只有在基础代理失败且增强代理重试成功的情况下，才会扣除这 5 额度。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化接入说明。