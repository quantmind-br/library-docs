---
title: マップ - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:13:26.695251-03:00
rendered_js: false
word_count: 47
summary: This document provides technical documentation for the Firecrawl API, detailing authentication, request body parameters for URL crawling, and configuration options for sitemap handling and location settings.
tags:
    - firecrawl-api
    - url-crawling
    - api-reference
    - sitemap-configuration
    - bearer-authentication
category: api
---

> Firecrawl APIキーを必要とするAIエージェントですか？自動オンボーディングの手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### ボディ

検索クエリを指定すると、結果が関連度の高い順に並べ替えられます。例: 「blog」を指定すると、URL 内に「blog」を含むものが関連度順に返されます。

sitemap

enum&lt;string&gt;

デフォルト:include

マッピング時のサイトマップモードです。`skip` に設定すると、URL の検出にサイトマップは使用されません。`only` に設定すると、サイトマップ内にある URL だけが返されます。デフォルトの `include` では、サイトマップとその他の手法を併用して URL を検出します。

利用可能なオプション:

`skip`,

`include`,

`only`

サイトマップキャッシュを無視して最新のURLを取得します。サイトマップデータは最大7日間キャッシュされるため、サイトマップを最近更新した場合はこのパラメータを指定してください。

返すリンクの最大数

必須範囲: `x <= 100000`

タイムアウト（ミリ秒単位）。既定ではタイムアウトはありません。

リクエストのロケーション設定です。指定すると、利用可能な場合は適切なプロキシを使用し、対応する言語およびタイムゾーン設定をエミュレートします。指定しない場合は、デフォルトで「US」が使用されます。

#### レスポンス