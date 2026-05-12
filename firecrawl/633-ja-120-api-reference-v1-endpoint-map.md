---
title: マップ - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/map
source: sitemap
fetched_at: 2026-03-23T07:12:05.656497-03:00
rendered_js: false
word_count: 37
summary: This document provides the API specifications for the map endpoint, including authentication requirements, request parameters, and response behavior for generating website sitemaps.
tags:
    - api-reference
    - sitemap-generation
    - web-scraping
    - authentication
    - api-endpoint
category: api
---

> 注意: 機能とパフォーマンスが向上した本 API の新しい [v2 バージョン](https://docs.firecrawl.dev/ja/api-reference/endpoint/map) が利用可能です。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### ボディ

マッピングに使用する検索クエリです。Alpha フェーズ中は、検索機能の「スマート」な部分は検索結果 500 件までに制限されています。ただし、map によってそれ以上の結果が見つかった場合でも、その件数には制限はありません。

ウェブサイトのサイトマップに含まれるリンクだけを返す

返すリンク数の上限

必須範囲: `x <= 30000`

タイムアウト時間（ミリ秒単位）。デフォルトではタイムアウトは設定されていません。

リクエストのロケーション設定。指定した場合、利用可能であれば対応するプロキシを使用し、対応する言語とタイムゾーン設定をエミュレートします。指定しない場合は、デフォルトで「US」が使用されます。

#### レスポンス