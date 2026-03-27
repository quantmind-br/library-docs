---
title: バッチスクレイプのエラーを取得する - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/batch-scrape-get-errors
source: sitemap
fetched_at: 2026-03-23T07:13:41.350789-03:00
rendered_js: false
word_count: 27
summary: This document provides the API specification for retrieving error information and details regarding blocked URLs from batch scraping jobs.
tags:
    - api-reference
    - batch-scraping
    - error-handling
    - robots-txt
    - authentication
category: api
---

バッチスクレイピングジョブで発生したエラーを取得する

> Firecrawl APIキーが必要なAI agent の場合は、自動オンボーディング手順について[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス

エラーが発生したスクレイピングジョブとエラーの詳細

スクレイピングを試行したが、robots.txt によってブロックされた URL の一覧