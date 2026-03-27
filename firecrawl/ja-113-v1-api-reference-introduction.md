---
title: はじめに - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/v1/api-reference/introduction
source: sitemap
fetched_at: 2026-03-23T07:37:59.06499-03:00
rendered_js: false
word_count: 41
summary: This document provides the foundational technical information for interacting with the Firecrawl API, including base URL specifications, authentication requirements, standard HTTP response codes, and rate limiting policies.
tags:
    - api-authentication
    - rate-limiting
    - http-status-codes
    - developer-documentation
    - api-integration
category: api
---

## 機能

## エージェント機能

## ベースURL

すべてのリクエストは次のベースURLを使用します：

```
https://api.firecrawl.dev
```

## 認証

認証には Authorization ヘッダーの指定が必要です。ヘッダーには `Bearer fc-123456789` を含めてください。`fc-123456789` はあなたの API キーを指します。

```
Authorization: Bearer fc-123456789
```

​

## レスポンスコード

Firecrawl は、リクエストの結果を示すために一般的な HTTP ステータスコードを使用します。 通常、2xx の HTTP ステータスコードは成功、4xx はユーザー起因の失敗、5xx はインフラストラクチャ上の問題を示します。

StatusDescription200リクエストは成功しました。400パラメータが正しいか確認してください。401API キーが提供されていません。402支払いが必要です。404リクエストされたリソースが見つかりませんでした。429レート制限を超過しました。5xxFirecrawl のサーバーエラーを示します。

発生しうるすべての API エラーの詳細については、Error Codes セクションを参照してください。

## レート制限

Firecrawl API には、サービスの安定性と信頼性を確保するためのレート制限があります。レート制限はすべてのエンドポイントに適用され、一定の時間内に行われたリクエスト数に基づいています。 レート制限を超えると、ステータスコード 429 が返されます。