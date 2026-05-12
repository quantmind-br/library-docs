---
title: 過去のトークン使用量 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v1-endpoint/token-usage-historical
source: sitemap
fetched_at: 2026-03-23T07:12:06.34344-03:00
rendered_js: false
word_count: 19
summary: This document describes the API endpoint for retrieving monthly token usage history for authenticated teams, including an optional breakdown by API key.
tags:
    - api-documentation
    - token-usage
    - billing-metrics
    - authentication
    - usage-analytics
category: api
---

認証済みのチームのトークン使用履歴を取得（Extractのみ）

月ごとのトークン使用量を返します。必要に応じて、APIキーごとの内訳も取得できます。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### クエリパラメータ

#### レスポンス