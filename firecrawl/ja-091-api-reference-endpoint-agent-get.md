---
title: エージェントのステータスを取得 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/agent-get
source: sitemap
fetched_at: 2026-03-23T07:13:54.387155-03:00
rendered_js: false
word_count: 39
summary: This document outlines the authentication requirements, response statuses, and data extraction parameters for the Firecrawl API.
tags:
    - api-reference
    - authentication
    - data-extraction
    - firecrawl
    - api-documentation
category: api
---

> Firecrawl APIキーが必要なAIエージェントの方は、自動オンボーディング手順について [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### パスパラメータ

#### レスポンス

利用可能なオプション:

`processing`,

`completed`,

`failed`

抽出されたデータ（ステータスが completed の場合にのみ存在）

model

enum&lt;string&gt;

デフォルト:spark-1-pro

エージェント実行時に使用されたモデルプリセット

利用可能なオプション:

`spark-1-pro`,

`spark-1-mini`

エラーメッセージ（status が failed の場合にのみ含まれます）