---
title: Enhanced Mode | Firecrawl
url: https://docs.firecrawl.dev/features/enhanced-mode
source: sitemap
fetched_at: 2026-03-23T07:24:45.548469-03:00
rendered_js: false
word_count: 122
summary: This document explains the available proxy strategies for web scraping with Firecrawl, detailing the different types and how to configure them for optimal request performance.
tags:
    - web-scraping
    - proxy-configuration
    - api-settings
    - firecrawl-integration
    - scraping-optimization
category: configuration
---

Firecrawl provides different proxy types to help you scrape websites with varying levels of complexity. Set the `proxy` parameter to control which proxy strategy is used for a request.

## Proxy types

Firecrawl supports three proxy types:

TypeDescriptionSpeedCost`basic`Standard proxies suitable for most sitesFast1 credit`enhanced`Enhanced proxies for complex sitesSlower5 credits per request`auto`Tries `basic` first, then retries with `enhanced` on failureVaries1 credit if basic succeeds, 5 credits if enhanced is needed

If you do not specify a proxy, Firecrawl defaults to `auto`.

## Basic usage

Set the `proxy` parameter to choose a proxy strategy. The following example uses `auto`, which lets Firecrawl decide when to escalate to enhanced proxies.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.