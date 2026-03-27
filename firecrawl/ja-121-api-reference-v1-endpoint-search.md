---
title: Search - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:12:15.944744-03:00
rendered_js: false
word_count: 76
summary: This document describes the search endpoint, which enables web searches combined with automated scraping capabilities and supports various query operators, location-based filtering, and time-based constraints.
tags:
    - search-api
    - web-scraping
    - query-operators
    - data-extraction
    - api-reference
category: api
---

検索を行い、必要に応じて検索結果をスクレイピングする

> 注意: 機能とパフォーマンスが向上した [new v2 version of this API](https://docs.firecrawl.dev/ja/api-reference/endpoint/search) が利用可能です。

search エンドポイントは、ウェブ検索と Firecrawl のスクレイピング機能を組み合わせ、任意のクエリに対してページ全体のコンテンツを返します。 各検索結果の完全な Markdown コンテンツを取得するには、`scrapeOptions` に `formats: ["markdown"]` を指定してください。指定しない場合は、既定で結果 (url、title、description) のみが返されます。

## サポートされているクエリ演算子

検索をより適切に絞り込める、さまざまなクエリ演算子をサポートしています。

OperatorFunctionalityExamples`""`文字列を厳密一致させる`"Firecrawl"``-`特定のキーワードを除外する、または他の演算子を否定する`-bad`, `-site:firecrawl.dev``site:`指定したウェブサイトからの結果のみを返す`site:firecrawl.dev``inurl:`URL に特定の語を含む結果のみを返す`inurl:firecrawl``allinurl:`URL に複数の語を含む結果のみを返す`allinurl:git firecrawl``intitle:`ページのタイトルに特定の語を含む結果のみを返す`intitle:Firecrawl``allintitle:`ページのタイトルに複数の語を含む結果のみを返す`allintitle:firecrawl playground``related:`特定のドメインに関連する結果のみを返す`related:firecrawl.dev`

## Location パラメータ

`location` パラメータを使うと、地域に最適化された検索結果を取得できます。形式: `"string"`。例: `"Germany"`、`"San Francisco,California,United States"`。 利用可能なすべての国と言語は、[サポート対象ロケーションの一覧](https://firecrawl.dev/search_locations.json)をご覧ください。

## 時間ベース検索

`tbs` パラメータを使うと、カスタムの日付範囲を含む期間で結果を絞り込めます。具体例や対応フォーマットは、[検索機能のドキュメント](https://docs.firecrawl.dev/features/search#time-based-search)を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### ボディ

返す結果の最大件数

必須範囲: `1 <= x <= 100`

時間指定の検索パラメータ。事前定義された時間範囲（`qdr:h`、`qdr:d`、`qdr:w`、`qdr:m`、`qdr:y`）と、カスタム日付範囲（`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`）をサポートします

他の Firecrawl エンドポイントでは無効となる URL を検索結果から除外します。検索結果のデータを他の Firecrawl API エンドポイントにパイプで渡す場合のエラー削減に役立ちます。

#### レスポンス