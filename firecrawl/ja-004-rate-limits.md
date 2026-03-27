---
title: レート制限 | Firecrawl
url: https://docs.firecrawl.dev/ja/rate-limits
source: sitemap
fetched_at: 2026-03-23T07:27:34.246768-03:00
rendered_js: false
word_count: 71
summary: This document outlines the billing model, concurrency limits for browser sessions, and API rate limits associated with different Firecrawl subscription plans.
tags:
    - billing-models
    - api-rate-limits
    - concurrency-limits
    - subscription-plans
    - firecrawl-service
    - service-quotas
category: reference
---

## 課金モデル

Firecrawl はサブスクリプション型の月額プランを採用しています。完全な従量課金モデルは提供していませんが、**自動チャージ機能** により柔軟にスケールできます。プランに加入すると、クレジット残高が設定したしきい値を下回ったときに自動的に追加クレジットを購入でき、より大きな自動チャージパックほどお得なレートが適用されます。より大きなプランを検討する前の検証用途には、まず Free または Hobby プランから始めることをおすすめします。 プランのダウングレードは次回更新時に反映され、残り期間に相当するクレジットは付与されません。

## 同時ブラウザ数の上限

同時ブラウザ数は、Firecrawl が同時に処理できるウェブページ数を指します。 ご利用プランによって同時実行できるジョブ数が決まり、上限を超えた場合は、 追加のジョブはリソースが空くまでキューで待機します。キューで待機している時間もリクエストの [`timeout`](https://docs.firecrawl.dev/ja/advanced-scraping-guide#timing-and-cache) パラメータに対してカウントされるため、待ち続けるのではなく早期に失敗させたい場合は、`timeout` を短めに設定できます。現在の空き状況は [Queue Status](https://docs.firecrawl.dev/ja/api-reference/endpoint/queue-status) エンドポイントで確認できます。

### 現在のプラン

プラン同時ブラウザ数最大キュー待機ジョブ数Free250,000Hobby550,000Standard50100,000Growth100200,000Scale / Enterprise150+300,000+

各チームで、同時実行キューに待機できるジョブ数には上限があります。この上限を超えると、既存のジョブが完了するまで、新しいジョブは `429` ステータスコードで拒否されます。カスタムの同時実行上限が設定された上位プランでは、最大キュー待機ジョブ数は同時実行上限の 2,000 倍で、上限は 2,000,000 です。 より高い同時実行上限が必要な場合は、[Enterprise プランについてお問い合わせください](https://firecrawl.dev/enterprise)。

プラン同時ブラウザ数最大キュー待機ジョブ数Free250,000Starter50100,000Explorer100200,000Pro200400,000

## API のレート制限

レート制限は 1 分あたりのリクエスト数で測定されており、主な目的は悪用を防ぐことです。適切に設定されていれば、実際のボトルネックとなるのは同時に動作するブラウザ数になります。

### 現在のプラン

プラン/scrape/map/crawl/search/agent/crawl/status/agent/statusFree101015101500500Hobby1001001550100150025000Standard50050050250500150025000Growth5000500025025001000150025000Scale75007500750750010002500025000

これらのレートリミットは、すべてのユーザーがAPIを公平に利用できるようにし、その可用性を確保するために設けられています。より高い上限が必要な場合は、カスタムプランについてご相談いただくために [help@firecrawl.com](mailto:help@firecrawl.com) までお問い合わせください。

Extract エンドポイントには、対応する `/agent` エンドポイントと同じレート制限が適用されます。

### バッチスクレイプエンドポイント

バッチスクレイプエンドポイントには、対応する `/crawl` と同じレート制限が適用されます。

### ブラウザセッション

`/browser` エンドポイントがプレビュー版である間、各チームで同時に利用できるアクティブなブラウザセッションは最大 20 件です。この上限を超えると、既存のセッションが破棄されるまで、新しいセッションリクエストは `429` ステータスコードを返します。

### FIRE-1 エージェント

FIRE-1 エージェントを利用するリクエストには、各エンドポイントごとに独立してカウントされる専用のレート制限が設定されています。

エンドポイントレート制限 (リクエスト/分) /scrape10/extract10

プラン/extract (リクエスト/分) /extract/status (リクエスト/分) Starter10025000Explorer50025000Pro100025000