---
title: 検索 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/api-reference/endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:13:06.518487-03:00
rendered_js: false
word_count: 188
summary: このドキュメントは、Firecrawlの検索エンドポイントを使用してWeb検索およびスクレイピングを実行するためのパラメータや設定方法を説明するリファレンスです。
tags:
    - web-search
    - scraping
    - api-documentation
    - query-operators
    - data-extraction
    - firecrawl
category: api
---

この search エンドポイントは、Web 検索と Firecrawl のスクレイピング機能を組み合わせることで、あらゆるクエリに対してページ全体のコンテンツを返します。 各検索結果の Markdown 形式の完全なコンテンツを取得するには、`scrapeOptions` に `formats: [{"type": "markdown"}]` を指定してください。指定しない場合は、結果（url、title、description）がデフォルトで返されます。要約されたコンテンツが必要な場合は、`{"type": "summary"}` など他のフォーマットも使用できます。

## サポートされているクエリ演算子

検索をより的確に絞り込むための各種クエリ演算子をサポートしています。

演算子機能例`""`テキストを厳密一致で検索する`"Firecrawl"``-`特定のキーワードを除外、または他の演算子を否定する`-bad`, `-site:firecrawl.dev``site:`指定したサイトの結果のみを返す`site:firecrawl.dev``filetype:`特定のファイル拡張子を持つ結果のみを返す`filetype:pdf`, `-filetype:pdf``inurl:`URL に特定の語を含む結果のみを返す`inurl:firecrawl``allinurl:`URL に複数の語を含む結果のみを返す`allinurl:git firecrawl``intitle:`ページタイトルに特定の語を含む結果のみを返す`intitle:Firecrawl``allintitle:`ページタイトルに複数の語を含む結果のみを返す`allintitle:firecrawl playground``related:`特定のドメインに関連する結果のみを返す`related:firecrawl.dev``imagesize:`指定した寸法と完全一致の画像のみを返す`imagesize:1920x1080``larger:`指定した寸法より大きい画像のみを返す`larger:1920x1080`

## Location パラメータ

`location` パラメータで地域ターゲットの検索結果を取得します。形式: `"string"`。例: `"Germany"`、`"San Francisco,California,United States"`。 利用可能な国と言語の一覧は、[サポート対象ロケーションの全リスト](https://firecrawl.dev/search_locations.json)をご覧ください。

## Country パラメータ

`country` パラメータで、ISO の国コードを用いて検索結果の対象国を指定します。既定値: `"US"`。 例: `"US"`, `"DE"`, `"FR"`, `"JP"`, `"UK"`, `"CA"`。

```
{
  "query": "レストラン",
  "country": "DE"
}
```

## Categories パラメータ

`categories` パラメータで、特定のカテゴリに検索結果を絞り込みます：

- **`github`** : GitHub のリポジトリ、コード、Issue、ドキュメントを検索
- **`research`** : 学術系・研究系のウェブサイト（arXiv、Nature、IEEE、PubMed など）を検索
- **`pdf`** : PDF を検索

### 使い方の例

```
{
  "query": "機械学習",
  "categories": ["github", "research"],
  "limit": 10
}
```

### カテゴリレスポンス

各結果には、どのソースからのものかを示す `category` フィールドが含まれます。

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/ml-project",
        "title": "Machine Learning Project",
        "description": "Implementation of ML algorithms",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "ML Research Paper",
        "description": "Latest advances in machine learning",
        "category": "research"
      }
    ]
  }
}
```

## 時間ベースの検索

`tbs` パラメータを使用すると、カスタム日付範囲を含む期間で検索結果を時間別に絞り込むことができます。詳細な例とサポートされている形式については、[検索機能のドキュメント](https://docs.firecrawl.dev/features/search#time-based-search)を参照してください。

> Firecrawl API key が必要な AI agent ですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md)を参照してください。

#### 承認

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### ボディ

検索クエリ

Maximum string length: `500`

返す結果の最大数

必須範囲: `1 <= x <= 100`

sources

(Web · object | Images · object | News · object)\[]

検索対象とするソース。レスポンスに含まれる配列の種類を決定します。デフォルトは \['web'] です。

- Web
- Images
- News

categories

(GitHub · object | Research · object | PDF · object)\[]

結果をカテゴリでフィルタリングするための指定。デフォルト値は \[] で、この場合はカテゴリによるフィルタリングは行われません。

- GitHub
- Research
- PDF

時間ベースの検索パラメータで、あらかじめ定義された期間（`qdr:h`, `qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`）、カスタム日付範囲（`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`）、日付順でのソート（`sbd:1`）をサポートします。値は組み合わせて指定できます（例: `sbd:1,qdr:w`）。

検索結果のロケーションを指定するパラメータ（例: `San Francisco,California,United States`）。最適な結果を得るには、このパラメータと `country` パラメータの両方を設定してください。

検索結果のジオターゲティングに使用する ISO 国コード（例：`US`）。最適な結果を得るには、これと `location` パラメータの両方を設定してください。

他の Firecrawl エンドポイントでは無効となる URL を検索結果から除外します。これにより、検索から取得したデータを他の Firecrawl API エンドポイントに渡す際のエラーを減らせます。

Zero Data Retention（ZDR）向けのエンタープライズ search options。エンドツーエンドの ZDR には `["zdr"]`（10 credits / 10件の結果）、匿名化された ZDR には `["anon"]`（2 credits / 10件の結果）を使用します。利用するには、チームで有効になっている必要があります。

#### レスポンス

検索結果。利用可能な配列は、リクエストで指定したソースに応じて変わります。デフォルトでは `web` 配列が返されます。