---
title: Enhanced Mode | Firecrawl
url: https://docs.firecrawl.dev/ja/features/enhanced-mode
source: sitemap
fetched_at: 2026-03-23T07:22:55.191263-03:00
rendered_js: false
word_count: 40
summary: This document explains the proxy strategy options available in Firecrawl for web scraping, detailing how to select between basic, enhanced, and automatic modes.
tags:
    - web-scraping
    - proxy-configuration
    - firecrawl-api
    - data-extraction
    - network-settings
category: configuration
---

Firecrawl は、さまざまな複雑さのウェブサイトをスクレイピングできるように、異なるプロキシタイプを提供しています。リクエストにどのプロキシ戦略を使用するかを制御するには、`proxy` パラメータを設定します。

## プロキシタイプ

Firecrawl は 3 つのプロキシタイプをサポートしています。

TypeDescriptionSpeedCost`basic`ほとんどのサイトに適した標準プロキシFast1 credit`enhanced`複雑なサイト向けの強化プロキシSlower1 リクエストあたり 5 クレジット`auto`まず `basic` を試し、失敗した場合は `enhanced` で再試行Varies`basic` が成功した場合は 1 credit、`enhanced` が必要な場合は 5 credits

プロキシを指定しない場合、Firecrawl はデフォルトで `auto` を使用します。

## 基本的な使い方

`proxy` パラメータを設定して、プロキシ戦略を選択します。次の例では `auto` を使用しており、強化プロキシに切り替えるタイミングは Firecrawl が自動的に判断します。

> Firecrawl API キーが必要な AI エージェントですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。