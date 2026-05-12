---
title: 速率限制 | Firecrawl
url: https://docs.firecrawl.dev/zh/rate-limits
source: sitemap
fetched_at: 2026-03-23T07:27:35.806829-03:00
rendered_js: false
word_count: 95
summary: This document outlines the billing structure, concurrent browser limits, and API rate limiting policies for Firecrawl services across different subscription tiers.
tags:
    - billing-models
    - api-rate-limits
    - concurrent-processing
    - subscription-plans
    - service-quotas
category: reference
---

## 计费模式

Firecrawl 使用按月订阅的套餐模式。我们不提供纯按量付费模式，但我们的 **自动充值功能** 提供了灵活的扩容能力——一旦你订阅某个套餐，当余额低于阈值时，系统会自动购买额外额度，且更大额度的自动充值包享受更优惠的单价。若你想在选择更大套餐前先进行测试，可以从 Free 或 Hobby 方案开始。 套餐降级将在下一个续费周期生效，且不会退还未使用时长的费用。

## 并发浏览器限制

并发浏览器指的是 Firecrawl 可为你同时处理的网页数量。 你的套餐决定可并行运行的作业数——如果超出该上限， 多余的作业将进入队列等待，直到资源可用。请注意，在队列中等待的时间也会计入该请求的 [`timeout`](https://docs.firecrawl.dev/zh/advanced-scraping-guide#timing-and-cache) 参数，因此你可以设置较低的 `timeout` 以快速失败，而不是长时间等待。你也可以通过 [Queue Status](https://docs.firecrawl.dev/zh/api-reference/endpoint/queue-status) 端点检查当前可用资源情况。

### 当前方案

方案并发浏览器最大排队任务数Free (免费) 250,000Hobby (入门) 550,000Standard (标准) 50100,000Growth (增长) 100200,000Scale / Enterprise150+300,000+

每个团队在并发队列中可等待的任务数都有上限。如果超过此限制，在现有任务完成之前，新任务都会以 `429` 状态码被拒绝。对于带有自定义并发限制的更高阶方案，最大排队任务数为并发限制的 2,000 倍，最高不超过 2,000,000。 如果您需要更高的并发限制，请[联系我们咨询企业方案](https://firecrawl.dev/enterprise)。

方案并发浏览器最大排队任务数Free (免费) 250,000Starter50100,000Explorer100200,000Pro200400,000

## API 速率限制

速率限制以每分钟请求数来衡量，主要用于防止滥用。正确配置后，你真正的瓶颈将是并发浏览器实例的数量。

### 当前方案

方案/scrape/map/crawl/search/agent/crawl/status/agent/statusFree (免费) 101015101500500Hobby (入门) 1001001550100150025000Standard (标准) 50050050250500150025000Growth (增长) 5000500025025001000150025000Scale (扩展) 75007500750750010002500025000

这些速率限制旨在确保所有用户都能公平使用，并保障 API 的可用性。如果您需要更高的配额，请通过 [help@firecrawl.com](mailto:help@firecrawl.com) 与我们联系，商讨自定义方案。

`extract` 端点与对应的 `/agent` 端点共用同一套速率限制。

### 批量抓取端点

批量抓取端点与对应的 `/crawl` 端点共享相同的速率限制。

### 浏览器会话

当 /browser 端点处于预览阶段时，每个团队最多可同时拥有 20 个活跃的浏览器会话。如果超出此限制，新的会话请求将返回 `429` 状态码，直到现有会话被销毁。

### FIRE-1 Agent

涉及 FIRE-1 Agent 的请求具有单独的速率限制，并按每个端点分别计数：

Endpoint速率限制 (请求数/分钟) /scrape10/extract10

方案/extract (请求/分钟) /extract/status (请求/分钟) Starter10025000Explorer50025000Pro100025000