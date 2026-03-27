---
title: エージェント - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/agent
source: sitemap
fetched_at: 2026-03-23T07:13:52.606577-03:00
rendered_js: false
word_count: 52
summary: This document provides the technical specification for configuring and authenticating requests to the Firecrawl AI agent API, including parameters for data extraction, model selection, and usage limits.
tags:
    - firecrawl
    - ai-agent
    - api-specification
    - data-extraction
    - authentication
    - schema-configuration
category: api
---

> Firecrawl API キーが必要な AI エージェントの方は、自動オンボーディング手順について [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### ボディ

抽出するデータ内容を指定するプロンプト

Maximum string length: `10000`

エージェントのアクセス先を制限するための任意のURLリスト

抽出データを構造化するためのオプションの JSON スキーマ

このエージェントタスクで使用するクレジットの最大値です。未設定の場合、デフォルトは2500です。2,500を超える値は、常に有料リクエストとして課金されます。

true の場合、エージェントは urls 配列で指定された URL にのみアクセスします

model

enum&lt;string&gt;

デフォルト:spark-1-mini

エージェントタスクで使用するモデルを指定します。デフォルトの spark-1-mini はコストを約 60% 削減でき、spark-1-pro はより複雑なタスク向けに高い精度を提供します。

利用可能なオプション:

`spark-1-mini`,

`spark-1-pro`

#### レスポンス