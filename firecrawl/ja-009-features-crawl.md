---
title: クロール | Firecrawl
url: https://docs.firecrawl.dev/ja/features/crawl
source: sitemap
fetched_at: 2026-03-23T07:22:51.802246-03:00
rendered_js: false
word_count: 214
summary: This document explains how to use Firecrawl's crawl functionality to recursively discover and scrape content from websites, including configuration options, polling, and real-time webhook integration.
tags:
    - web-scraping
    - api-integration
    - crawling
    - webhooks
    - data-extraction
    - firecrawl
category: api
---

Crawl は URL を Firecrawl に送信し、到達可能なすべてのサブページを再帰的に検出してスクレイピングします。サイトマップ、JavaScript レンダリング、レート制限を自動的に処理し、各ページについてクリーンな Markdown または構造化データを返します。

- サイトマップとリンクの再帰的なたどりによってページを検出
- パスのフィルタリング、深さ制限、サブドメインや外部リンクの制御をサポート
- ポーリング、WebSocket、または Webhook で結果を返す

## インストール

## 基本的な使い方

開始 URL を指定して `POST /v2/crawl` を呼び出し、クロールジョブを送信します。このエンドポイントは、結果をポーリングするために使用するジョブ ID を返します。

### スクレイプオプション

[Scrape エンドポイント](https://docs.firecrawl.dev/ja/api-reference/endpoint/scrape) のすべてのオプションは、`scrapeOptions` (JS) / `scrape_options` (Python) 経由で crawl でも利用できます。これらはクローラーがスクレイプするすべてのページに適用されます (フォーマット、プロキシ、キャッシュ、アクション、ロケーション、タグを含む) 。

## クロールステータスの確認

ジョブ ID を使用してクロールのステータスをポーリングし、結果を取得します。

### レスポンスの処理

レスポンスはクロールのステータスによって異なります。未完了のレスポンス、またはサイズが10MBを超える大きなレスポンスの場合は、`next` URLパラメータが付与されます。次の10MBのデータを取得するには、このURLにリクエストしてください。`next` パラメータがない場合は、クロールデータの終端を示します。

## SDK メソッド

SDK で crawl を使う方法は 2 通りあります。

### クロールして待つ

`crawl` メソッドはクロールの完了を待機し、完全なレスポンスを返します。ページネーションを自動処理します。ほとんどのユースケースで推奨されます。

レスポンスには、クロールのステータスと収集された全データが含まれます:

### 開始して後で確認

`startCrawl` / `start_crawl` メソッドは即時にクロール ID を返します。その後、ステータスを手動でポーリングして確認します。これは、長時間のクロールや独自のポーリングロジックに有用です。

最初のレスポンスではジョブ ID が返されます:

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/crawl/123-456-789"
}
```

## WebSocket によるリアルタイム結果

watcher メソッドでは、ページのクロール中にリアルタイムで更新を受け取れます。クロールを開始し、その後イベントを購読することで、データを即座に処理できます。

## Webhooks

クロールの進行に合わせてリアルタイム通知を受け取れるよう、webhook を設定できます。これにより、クロール全体の完了を待たずに、スクレイプされたページを随時処理できます。

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": {
        "url": "https://your-domain.com/webhook",
        "metadata": {
          "any_key": "any_value"
        },
        "events": ["started", "page", "completed"]
      }
    }'
```

### イベントタイプ

EventDescription`crawl.started`クロールが開始されたときに発火します`crawl.page`スクレイプに成功した各ページごとに発火します`crawl.completed`クロールが完了したときに発火します`crawl.failed`クロール中にエラーが発生した場合に発火します

### ペイロード

```
{
  "success": true,
  "type": "crawl.page",
  "id": "crawl-job-id",
  "data": [...], // 'page'イベントのページデータ
  "metadata": {}, // Your custom metadata
  "error": null
}
```

### Webhook シグネチャの検証

Firecrawl からのすべての webhook リクエストには、HMAC-SHA256 シグネチャを含む `X-Firecrawl-Signature` ヘッダーが含まれます。Webhook が正当で改ざんされていないことを確認するために、必ずこのシグネチャを検証してください。

1. アカウント設定の [Advanced タブ](https://www.firecrawl.dev/app/settings?tab=advanced) から webhook secret を取得する
2. `X-Firecrawl-Signature` ヘッダーからシグネチャを取得する
3. 取得した secret を使い、生のリクエストボディに対して HMAC-SHA256 を計算する
4. タイミング攻撃耐性のある関数を使って、計算結果とヘッダーのシグネチャを比較する

JavaScript と Python による完全な実装例については、[Webhook セキュリティのドキュメント](https://docs.firecrawl.dev/ja/webhooks/security) を参照してください。詳細なイベントペイロード、ペイロード構造、高度な設定、トラブルシューティングを含む包括的な webhook ドキュメントについては、[Webhooks ドキュメント](https://docs.firecrawl.dev/ja/webhooks/overview) を参照してください。

## 設定リファレンス

クロールジョブの送信時に指定できる全パラメータ:

ParameterTypeDefaultDescription`url``string`(required)クロール開始元の URL`limit``integer``10000`クロールするページの最大数`maxDiscoveryDepth``integer`(none)URL 内の `/` セグメント数ではなく、リンクの発見ホップ数に基づくルート URL からの最大深度。ページ上で新しい URL が見つかるたびに、その URL には発見元のページより 1 つ深い深度が割り当てられます。ルートサイトおよびサイトマップに含まれるページの発見深度は 0 です。最大深度のページもスクレイプされますが、そのページ上のリンクはたどりません。`includePaths``string[]`(none)含める URL パスの正規表現パターン。一致するパスのみをクロールします。`excludePaths``string[]`(none)クロール対象から除外する URL パスの正規表現パターン`regexOnFullURL``boolean``false``includePaths`/`excludePaths` を、パスのみではなく完全な URL (クエリパラメータを含む) に対して照合します`crawlEntireDomain``boolean``false`子パスだけでなく、同一ドメイン内の兄弟 URL や親 URL への内部リンクもたどります`allowSubdomains``boolean``false`メインドメインのサブドメインへのリンクもたどります`allowExternalLinks``boolean``false`外部サイトへのリンクもたどります`sitemap``string``"include"`サイトマップの扱い: `"include"` (デフォルト) 、`"skip"`、または `"only"``ignoreQueryParameters``boolean``false`クエリパラメータが異なっていても、同じパスの再スクレイピングを避けます`delay``number`(none)レート制限を順守するためのスクレイプ間の遅延 (秒)`maxConcurrency``integer`(none)同時スクレイプの最大数。デフォルトでは、チームの同時実行数上限が使用されます。`scrapeOptions``object`(none)すべてのスクレイプ対象ページに適用されるオプション (フォーマット、プロキシ、キャッシュ、アクションなど)`webhook``object`(none)リアルタイム通知用の Webhook 設定`prompt``string`(none)クロールオプションを生成するための自然言語プロンプト。明示的に設定したパラメータは、生成された対応項目より優先されます。

## 重要な詳細

- **サイトマップによる検出**: デフォルトでは、クローラーは URL を検出するためにウェブサイトのサイトマップを含めます (`sitemap: "include"`) 。`sitemap: "skip"` を設定すると、ルート URL から HTML リンクを通じて到達できるページのみが検出されます。HTML から直接リンクされていない PDF などのアセットや、サイトマップには記載されていても深い階層にあるページは見逃されます。最大限の網羅性を得るには、デフォルト設定のままにしてください。
- **クレジット使用量**: クロールした各ページにつき 1 クレジットかかります。JSONモードではページごとに 4 クレジット、enhanced proxy ではページごとに 4 クレジットが追加され、PDF の解析には PDF 1 ページごとに 1 クレジットかかります。
- **結果の有効期限**: ジョブの結果は、完了後 24 時間は API 経由で利用できます。その後は、[アクティビティログ](https://www.firecrawl.dev/app/logs)で結果を確認してください。
- **クロールエラー**: `data` 配列には、Firecrawl が正常にスクレイピングしたページが含まれます。ネットワークエラー、タイムアウト、または robots.txt によるブロックで失敗したページを取得するには、[Get Crawl Errors](https://docs.firecrawl.dev/ja/api-reference/endpoint/crawl-get-errors) エンドポイントを使用します。
- **非決定的な結果**: 同じ設定で実行しても、クロール結果は実行ごとに異なる場合があります。ページは並行してスクレイピングされるため、リンクが検出される順序はネットワークのタイミングや、どのページの読み込みが先に完了するかに左右されます。そのため、深さの境界付近ではサイト内の異なる分岐が異なる程度まで探索されることがあり、特に `maxDiscoveryDepth` の値が大きい場合に顕著です。より決定的な結果を得るには、`maxConcurrency` を `1` に設定するか、サイトに包括的なサイトマップがある場合は `sitemap: "only"` を使用してください。

> Firecrawl API キーが必要な AI エージェントですか？ 自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。