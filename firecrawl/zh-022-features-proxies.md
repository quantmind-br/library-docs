---
title: 代理 | Firecrawl
url: https://docs.firecrawl.dev/zh/features/proxies
source: sitemap
fetched_at: 2026-03-23T07:20:27.102466-03:00
rendered_js: false
word_count: 58
summary: This document explains how to configure proxy settings in Firecrawl, including choosing geographical locations and selecting between basic, enhanced, or auto proxy modes for web scraping.
tags:
    - firecrawl
    - web-scraping
    - proxy-configuration
    - geographical-proxy
    - api-settings
    - scraping-performance
category: configuration
---

Firecrawl 提供多种代理类型，帮助你抓取复杂程度各异的网站。可通过 `proxy` 参数指定代理类型。

> 默认情况下，Firecrawl 会将所有请求经由代理转发，以提升可靠性与可访问性，即使你未指定代理类型或位置也同样生效。

## 基于位置的代理选择

Firecrawl 会根据你指定或自动检测到的位置，自动选择最合适的代理，从而优化抓取性能和可靠性。但目前并非所有地区都受支持。当前可用的地区如下：

国家代码国家名称基础代理支持增强代理支持AE阿拉伯联合酋长国是否AU澳大利亚是否BR巴西是否CA加拿大是否CN中国是否CZ捷克是否DE德国是否EE爱沙尼亚是否EG埃及是否ES西班牙是否FR法国是否GB英国是否GR希腊是否HU匈牙利是否ID印度尼西亚是否IL以色列是否IN印度是否IT意大利是否JP日本是否MY马来西亚是否NO挪威是否PL波兰是否PT葡萄牙是否QA卡塔尔是否SG新加坡是否US美国是是VN越南是否

如果你需要上述列表以外地区的代理，请[联系我们](mailto:help@firecrawl.com)并告知你的需求。 如果你未指定代理或位置，Firecrawl 将自动使用美国代理。

## 如何指定代理位置

你可以在请求中通过设置 `location.country` 参数来指定代理位置。例如，要使用巴西代理，将 `location.country` 设置为 `BR`。 更多详情请参阅 [`location.country` 的 API 参考](https://docs.firecrawl.dev/api-reference/endpoint/scrape#body-location)。

## 代理类型

Firecrawl 支持三种类型的代理：

- **basic**：用于抓取大多数网站的代理。速度快，通常能正常工作。
- **enhanced**：用于抓取复杂网站并同时保持隐私的增强型代理。速度较慢，但在某些网站上更可靠。[进一步了解 Enhanced 模式 →](https://docs.firecrawl.dev/zh/features/enhanced-mode)
- **auto**：如果 basic 代理抓取失败，Firecrawl 会自动使用 enhanced 代理重试抓取。如果使用 enhanced 重试成功，该次抓取将收取 5 点额度；如果第一次使用 basic 抓取就成功，则只会收取正常费用。

* * *

> **注意：** 关于使用 enhanced 代理的详细信息，包括额度成本和重试策略，请参阅[Enhanced 模式文档](https://docs.firecrawl.dev/zh/features/enhanced-mode)。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化接入说明。