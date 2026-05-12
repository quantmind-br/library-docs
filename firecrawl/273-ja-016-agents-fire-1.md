---
title: FIRE-1 AI エージェント（ベータ） | Firecrawl
url: https://docs.firecrawl.dev/ja/agents/fire-1
source: sitemap
fetched_at: 2026-03-23T07:35:32.758871-03:00
rendered_js: false
word_count: 32
summary: FIRE-1 is an AI-powered agent designed for Firecrawl that enhances data extraction capabilities by performing complex browser automation and navigating dynamic web content.
tags:
    - fire-1
    - firecrawl
    - ai-agent
    - web-scraping
    - browser-automation
    - data-extraction
category: concept
---

FIRE-1 は、Firecrawl のスクレイピング機能を強化する AI エージェントです。ブラウザのアクションを制御し、複雑なウェブサイト構造を自在に探索して、従来のスクレイピングを超える包括的なデータ抽出を実現します。

### FIRE-1 でできること:

- データを取得するために計画を立て、アクションを実行する
- ボタン、リンク、入力欄などの動的要素を操作する
- ページネーションや複数ステップが必要な、複数ページにわたるデータを取得する

## FIRE-1 の使い方

複数ページの移動や要素とのインタラクションを伴う複雑な抽出タスクには、`/v1/extract` エンドポイントで FIRE-1 エージェントを活用できます。 **例:**

## 請求

FIRE-1 のコストは一意に決まりません。各 Extract リクエストの基本コストは、[クレジット計算ツール](https://www.firecrawl.dev/extract-calculator)をご覧ください。 **なぜ FIRE-1 のほうが高いのですか？**  
FIRE-1 は高度なブラウザ自動化と AI によるプランニングを用いて複雑なウェブページと対話するため、標準的な抽出に比べてより多くの計算リソースを要します。

## レート制限

- `/extract`: 1分あたり10件のリクエスト