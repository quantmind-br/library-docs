---
title: 抽出 | Firecrawl
url: https://docs.firecrawl.dev/ja/features/extract
source: sitemap
fetched_at: 2026-03-23T07:22:43.258794-03:00
rendered_js: false
word_count: 171
summary: This document explains how to use the /extract endpoint in Firecrawl to scrape and structure web data from multiple URLs using natural language prompts or schemas.
tags:
    - api-documentation
    - web-scraping
    - structured-data
    - data-extraction
    - firecrawl
    - web-crawling
    - automation
category: api
---

`/extract` エンドポイントは、複数の URL やドメイン全体から構造化データを収集する作業を簡略化します。ワイルドカード (例: `example.com/*`) を含めることもできる URL のリストと、取得したい情報を記述するプロンプトまたはスキーマを指定してください。Firecrawl がクロール、解析、集約の処理を担い、大規模・小規模いずれのデータセットにも対応します。

ワイルドカードを含め、1つまたは複数のURLから構造化データを抽出できます:

- **単一ページ**  
  例: `https://firecrawl.dev/some-page`
- **複数ページ / ドメイン全体**  
  例: `https://firecrawl.dev/*`

`/*` を使用すると、Firecrawl はそのドメイン内で検出できるすべてのURLを自動的にクロールしてパースし、その後、指定されたデータを抽出します。この機能は実験的なものです。問題がある場合は [help@firecrawl.com](mailto:help@firecrawl.com) までメールでご連絡ください。

### 使用例

**主要パラメータ:**

- **urls**: 1つ以上のURLを含む配列。広範なクロールのためにワイルドカード (`/*`) に対応。
- **prompt** (スキーマがない場合のみ任意) : 取得したいデータ、またはそのデータの構造化方法を記述する自然言語のプロンプト。
- **schema** (プロンプトがない場合のみ任意) : すでにJSONのレイアウトが分かっている場合に用いる、より厳密な構造定義。
- **enableWebSearch** (任意) : `true` の場合、指定ドメイン外のリンクもたどって抽出を実行。

詳細は [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/extract) を参照してください。

### レスポンス (SDK)

```
{
  "success": true,
  "data": {
    "company_mission": "Firecrawl は、ウェブからデータを抽出する最も簡単な方法です。開発者は、単一の API コールで URL を LLM 向けのMarkdownや構造化データに確実に変換するために Firecrawl を利用しています。",
    "supports_sso": false,
    "is_open_source": true,
    "is_in_yc": true
  }
}
```

## ジョブのステータスと完了

抽出ジョブを送信すると (API またはスターター メソッド経由) 、ジョブ ID が返されます。この ID で次のことができます:

- ジョブ ステータスの取得: /extract/ エンドポイントにリクエストを送り、ジョブが実行中か完了済みかを確認します。
- 結果を待つ: デフォルトの `extract` メソッド (Python/Node) を使う場合、SDK が完了まで待機して最終結果を返します。
- 開始してポーリング: スタート メソッド (`start_extract` (Python) または `startExtract` (Node) ) を使う場合、SDK はすぐにジョブ ID を返します。進行状況の確認には `get_extract_status` (Python) または `getExtractStatus` (Node) を使用します。

以下は、Python、Node.js、cURL を使用して抽出ジョブのステータスを確認するコード例です:

### 取りうる状態

- **completed**: 抽出が正常に完了しました。
- **processing**: Firecrawl がリクエストを処理中です。
- **failed**: エラーが発生し、データを完全に抽出できませんでした。
- **cancelled**: ユーザーによってジョブがキャンセルされました。

#### 処理待ちの例

```
{
  "success": true,
  "data": [],
  "status": "processing",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

#### 完成例

```
{
  "success": true,
  "data": {
      "company_mission": "Firecrawl は、ウェブからデータを抽出する最も簡単な方法です。開発者は、単一の API コールで URL を LLM 向けのMarkdownまたは構造化データに確実に変換するために Firecrawl を利用します。",
      "supports_sso": false,
      "is_open_source": true,
      "is_in_yc": true
    },
  "status": "completed",
  "expiresAt": "2025-01-08T20:58:12.000Z"
}
```

厳密な構造を定義したくない場合は、`prompt` を渡すだけで構いません。基盤のモデルが適切な構造を自動で選択するため、探索的または柔軟なリクエストに適しています。

```
{
  "success": true,
  "data": {
    "company_mission": "WebサイトをLLM対応のデータに変換。あらゆるサイトをクロールして得たクリーンなデータでAIアプリを強化。"
  }
}
```

## Web検索で結果を向上させる

リクエストで `enableWebSearch = true` を設定すると、指定したURLの範囲を超えてクロールが拡張されます。これにより、リンク先のページから補助的・関連情報を取得できます。 以下は、ドライブレコーダー (ダッシュカム) に関する情報を抽出し、関連ページのデータで結果を補強する例です:

### ウェブ検索を使った応答例

```
{
  "success": true,
  "data": {
    "dash_cams": [
      {
        "name": "Nextbase 622GW",
        "price": "$399.99",
        "features": [
          "4K動画録画",
          "手ブレ補正",
          "Alexa内蔵",
          "What3Words対応"
        ],
        /* 以下の情報は、enableWebSearch パラメータで見つかった
        https://www.techradar.com/best/best-dash-cam などの他サイトをもとに補足されています
        */
        "pros": [
          "優れた映像品質",
          "夜間撮影に強い",
          "GPS内蔵"
        ],
        "cons": ["価格が高い", "アプリが不安定な場合がある"]
      }
    ],
  }

```

この応答には、関連ページから収集した追加のコンテキストが含まれており、より網羅的で正確な情報を提供します。

`/extract` エンドポイントは、特定の URL を指定せずに、プロンプトを使って構造化データを抽出できるようになりました。リサーチや正確な URL が分からない場合に便利です。現在はアルファ版です。

## 既知の制限事項 (ベータ)

1. **大規模サイトのカバレッジ**  
   巨大なサイト (例：「Amazonの全商品」) を単一のリクエストで完全にカバーすることは、まだサポートしていません。
2. **複雑な論理クエリ**  
   「2025年の投稿をすべて見つけて」のようなリクエストは、期待するデータを確実にすべて返せない場合があります。より高度なクエリ機能を開発中です。
3. **稀に発生する不一致**  
   特に非常に大規模または動的なサイトでは、実行ごとに結果が異なることがあります。通常は主要な情報を捉えますが、多少のばらつきが生じる可能性があります。
4. **ベータ版の状態**  
   `/extract` はまだベータ版のため、機能やパフォーマンスは今後も進化します。改善のためのバグ報告やフィードバックをお待ちしています。

## FIRE-1 の使用

FIRE-1 は Firecrawl のスクレイピング機能を強化する AI エージェントです。ブラウザのアクションを制御し、複雑なウェブサイト構造を横断して、従来のスクレイピングを超える包括的なデータ抽出を実現します。 複数ページにまたがる遷移や要素とのインタラクションが必要な複雑な抽出タスクには、`/extract` エンドポイントで FIRE-1 エージェントを活用できます。 **例 (cURL) ：**

```
curl -X POST https://api.firecrawl.dev/v2/extract \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "urls": ["https://example-forum.com/topic/123"],
      "prompt": "このフォーラムスレッドからすべてのユーザーコメントを抽出してください。",
      "schema": {
        "type": "object",
        "properties": {
          "comments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "author": {"type": "string"},
                "comment_text": {"type": "string"}
              },
              "required": ["author", "comment_text"]
            }
          }
        },
        "required": ["comments"]
      },
      "agent": {
        "model": "FIRE-1"
      }
    }'
```

> FIRE-1 はすでに稼働しており、プレビュー版として利用可能です。

## 請求と利用状況の追跡

請求を簡素化し、Extract は他のエンドポイントと同様にクレジット制になりました。1 クレジットは 15 トークンに相当します。 [ダッシュボード](https://www.firecrawl.dev/app/extract)で Extract の利用状況を確認できます。 ご意見やサポートが必要な方は、[help@firecrawl.com](mailto:help@firecrawl.com) までメールでご連絡ください。

> Firecrawl API key が必要な AI エージェントの方は、自動オンボーディング手順について [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。