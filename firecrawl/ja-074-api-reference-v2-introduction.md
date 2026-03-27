---
title: はじめに - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/v2-introduction
source: sitemap
fetched_at: 2026-03-23T07:31:57.408879-03:00
rendered_js: false
word_count: 44
summary: This document provides the foundational technical information for interacting with the Firecrawl API, including base URL, authentication procedures, HTTP response codes, and rate limiting policies.
tags:
    - api-reference
    - authentication
    - web-scraping
    - http-status-codes
    - rate-limiting
category: reference
---

Firecrawl API を使用すると、プログラムから Web データにアクセスできます。すべてのエンドポイントは、本ページで説明する共通のベース URL、認証方式、レスポンス形式を使用します。

## 機能

## エージェント機能

## ベースURL

すべてのリクエストは次のベースURLを使用します：

```
https://api.firecrawl.dev
```

## 認証

すべてのリクエストには API キーを指定した `Authorization` ヘッダーが必要です：

```
Authorization: Bearer fc-YOUR-API-KEY
```

すべての API 呼び出しにこのヘッダーを含めてください。API キーは [Firecrawl ダッシュボード](https://www.firecrawl.dev/app/api-keys) で確認できます。

## レスポンスコード

Firecrawl は、リクエストの結果を示すために標準的な HTTP ステータスコードを使用します。`2xx` 番台のコードは成功、`4xx` 番台のコードはクライアントエラー、`5xx` 番台のコードはサーバーエラーを示します。

Status説明`200`リクエストは成功しました。`400`無効なリクエストパラメータです。`401`API キーが未設定か無効です。`402`支払いが必要です。`404`要求されたリソースが見つかりませんでした。`429`レート制限を超過しました。`5xx`Firecrawl 側でサーバーエラーが発生しました。

`5xx` エラーが発生した場合、レスポンスボディには問題の診断に役立つ特定のエラーコードが含まれます。

## レート制限

Firecrawl API は、サービスの安定性を確保するため、すべてのエンドポイントに対してレート制限を適用しています。レート制限は、一定時間内のリクエスト数に基づいて決まります。 レート制限を超過した場合、API は `429` ステータスコードを返します。短時間待ってから、リクエストを再試行してください。