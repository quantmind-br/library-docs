---
title: 検索 | Firecrawl
url: https://docs.firecrawl.dev/ja/features/search
source: sitemap
fetched_at: 2026-03-23T07:22:39.490916-03:00
rendered_js: false
word_count: 261
summary: This document explains how to use the Firecrawl Search API to perform web searches, filter results by categories or sources, and extract structured content from search results using built-in scraping options.
tags:
    - firecrawl
    - search-api
    - web-scraping
    - api-reference
    - data-extraction
category: api
---

Firecrawlの検索APIを使うと、ウェブ検索を実行し、必要に応じて同一オペレーション内で検索結果をスクレイピングできます。

- 出力フォーマット (markdown、html、links、screenshot) を選択
- 位置情報などのパラメータを指定してウェブを検索
- 検索結果からコンテンツを任意で取得 (各種フォーマット対応)
- 取得件数の制御やタイムアウトの設定が可能

詳細は、[Search Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/search)を参照してください。

### /search エンドポイント

ウェブ検索を実行し、必要に応じて結果からコンテンツを取得します。

### インストール

### 基本的な使い方

### レスポンス

SDKはデータオブジェクトを直接返します。cURLはペイロード全体を返します。

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://www.firecrawl.dev/",
        "title": "Firecrawl - AI向けWebデータAPI",
        "description": "AI向けのウェブクローリング、スクレイピング、検索API。大規模運用に対応。Firecrawlはインターネット全体をAIエージェントやビルダーに提供します。",
        "position": 1
      },
      {
        "url": "https://github.com/firecrawl/firecrawl",
        "title": "mendableai/firecrawl: Turn entire websites into LLM-ready ... - GitHub",
        "description": "Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data.",
        "position": 2
      },
      ...
    ],
    "images": [
      {
        "title": "Quickstart | Firecrawl",
        "imageUrl": "https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png",
        "imageWidth": 5814,
        "imageHeight": 1200,
        "url": "https://docs.firecrawl.dev/",
        "position": 1
      },
      ...
    ],
    "news": [
      {
        "title": "Y Combinator startup Firecrawl is ready to pay $1M to hire three AI agents as employees",
        "url": "https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/",
        "snippet": "It's now placed three new ads on YC's job board for “AI agents only” and has set aside a $1 million budget total to make it happen.",
        "date": "3 months ago",
        "position": 1
      },
      ...
    ]
  }
}
```

## 検索結果の種類

通常のウェブ結果に加え、Search は `sources` パラメータで以下の特化タイプを指定できます:

- `web`: 標準的なウェブ結果 (デフォルト)
- `news`: ニュース特化の結果
- `images`: 画像検索の結果

1 回の呼び出しで複数のソースを指定できます (例: `sources: ["web", "news"]`) 。この場合、`limit` パラメータは**ソースタイプごと**に適用されます。そのため、`limit: 5` かつ `sources: ["web", "news"]` の場合、最大 5 件の web 結果と最大 5 件の news 結果 (合計 10 件) が返されます。ソースごとに異なるパラメータ (たとえば、異なる `limit` 値や異なる `scrapeOptions`) が必要な場合は、別々の呼び出しを行ってください。

## 検索カテゴリ

`categories` パラメータを使って、特定のカテゴリで検索結果を絞り込みます:

- `github`: GitHub のリポジトリ、コード、Issue、ドキュメントを検索
- `research`: 学術・研究サイト (arXiv、Nature、IEEE、PubMed など) を検索
- `pdf`: PDF を検索

### GitHubカテゴリ検索

GitHub のリポジトリ内を対象に絞り込んで検索します：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "web scraping python",
    "categories": ["github"],
    "limit": 10
  }'
```

### 研究カテゴリー検索

学術・研究系のウェブサイトを検索します:

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "機械学習 トランスフォーマー",
    "categories": ["研究"],
    "limit": 10
  }'
```

### 複合カテゴリ検索

1回の検索で複数のカテゴリを組み合わせる：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "ニューラルネットワーク",
    "categories": ["github", "research"],
    "limit": 15
  }'
```

### カテゴリのレスポンス形式

各検索結果には、出所を示す `category` フィールドが含まれます。

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/neural-network",
        "title": "ニューラルネットワーク実装",
        "description": "PyTorch によるニューラルネットワークの実装",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "ニューラルネットワークアーキテクチャの進展",
        "description": "ニューラルネットワークの改良に関する研究論文"
        "category": "research"
      }
    ]
  }
}
```

例：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "openai",
    "sources": ["news"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "jupiter",
    "sources": ["images"],
    "limit": 8
  }'
```

### サイズフィルタ付きHD画像検索

高解像度の画像を見つけるには、画像検索の演算子を使います：

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sunset imagesize:1920x1080",
    "sources": ["images"],
    "limit": 5
  }'

curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "mountain wallpaper larger:2560x1440",
    "sources": ["images"],
    "limit": 8
  }'
```

**一般的なHDの解像度:**

- `imagesize:1920x1080` - フルHD (1080p)
- `imagesize:2560x1440` - QHD (1440p)
- `imagesize:3840x2160` - 4K UHD
- `larger:1920x1080` - HD以上
- `larger:2560x1440` - QHD以上

## コンテンツのスクレイピング付き検索

1回の操作で検索し、検索結果からコンテンツを取得します。

この /search エンドポイントは、`scrapeOptions` パラメータ経由で /scrape エンドポイントのすべてのオプションに対応しています。

### スクレイプ済みコンテンツを含むレスポンス

```
{
  "success": true,
  "data": [
    {
      "title": "Firecrawl - 究極のWebスクレイピングAPI",
      "description": "Firecrawl は、あらゆるウェブサイトを AI や分析向けのクリーンで構造化されたデータに変換する強力なWebスクレイピングAPIです。",
      "url": "https://firecrawl.dev/",
      "markdown": "# Firecrawl\n\n究極のWebスクレイピングAPI\n\n## あらゆるウェブサイトをクリーンで構造化されたデータに変換\n\nFirecrawl は、AIアプリケーション、市場調査、コンテンツ集約などに向けて、ウェブサイトからデータを手軽に抽出できます...",
      "links": [
        "https://firecrawl.dev/pricing",
        "https://firecrawl.dev/docs",
        "https://firecrawl.dev/guides"
      ],
      "metadata": {
        "title": "Firecrawl - 究極のWebスクレイピングAPI",
        "description": "Firecrawl は、あらゆるウェブサイトを AI や分析向けのクリーンで構造化されたデータに変換する強力なWebスクレイピングAPIです。"
        "sourceURL": "https://firecrawl.dev/",
        "statusCode": 200
      }
    }
  ]
}
```

## 高度な検索オプション

Firecrawlの検索APIは、検索をカスタマイズできる各種パラメータに対応しています。

### 場所のカスタマイズ

### 時間指定検索

`tbs` パラメータを使って、結果を時間範囲でフィルタリングします。`tbs` は `web` ソースの結果にのみ適用され、`news` や `images` の結果には適用されない点に注意してください。時間で絞り込んだニュース結果が必要な場合は、特定のニュースドメインを対象にするために、`site:` 演算子と組み合わせた `web` ソースの利用を検討してください。

一般的な `tbs` の値:

- `qdr:h` - 過去1時間
- `qdr:d` - 過去24時間
- `qdr:w` - 過去1週間
- `qdr:m` - 過去1か月
- `qdr:y` - 過去1年
- `sbd:1` - 日付順にソート (新しい順)

より細かく絞り込みたい場合は、カスタム日付範囲フォーマットで日付範囲を指定できます:

`sbd:1` を時間フィルタと組み合わせることで、指定した期間内の結果を日付順にソートして取得できます。たとえば、`sbd:1,qdr:w` は過去1週間の結果を新しい順で返し、`sbd:1,cdr:1,cd_min:12/1/2024,cd_max:12/31/2024` は2024年12月の結果を日付順に返します。

### カスタムタイムアウト

検索処理のタイムアウトを任意に設定します:

## ゼロデータ保持 (ZDR)

厳格なデータ取り扱い要件を持つチーム向けに、Firecrawl では `enterprise` パラメータを通じて `/search` エンドポイント用のゼロデータ保持 (ZDR) オプションを提供しています。ZDR 検索は Enterprise プランで利用可能です。利用を開始するには、[firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) をご覧ください。

### エンドツーエンド ZDR

エンドツーエンド ZDR では、Firecrawl と上流の検索プロバイダーの両方でゼロデータ保持が適用されます。クエリや結果データは、パイプラインのどの時点でも保存されません。

- **コスト:** 10 件の結果につき 10 クレジット
- **パラメータ:** `enterprise: ["zdr"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["zdr"]
  }'
```

### 匿名化された ZDR

匿名化された ZDR では、Firecrawl は当社側で完全なゼロデータ保持を適用します。検索プロバイダーがクエリをキャッシュする場合がありますが、それは完全に匿名化されており、識別可能な情報は一切付随しません。

- **コスト:** 10 件の結果につき 2 クレジット
- **パラメータ:** `enterprise: ["anon"]`

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 10,
    "enterprise": ["anon"]
  }'
```

### 検索 ZDR と Scrape ZDR の組み合わせ

コンテンツのスクレイピング (`scrapeOptions`) とあわせて検索を使用している場合、`enterprise` パラメータは検索部分を対象とし、`scrapeOptions` の `zeroDataRetention` はスクレイピング部分を対象とします。両方にわたって完全な ZDR を実現するには、両方を設定してください。

```
curl -X POST https://api.firecrawl.dev/v2/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "query": "sensitive topic",
    "limit": 5,
    "enterprise": ["zdr"],
    "scrapeOptions": {
      "formats": ["markdown"],
      "zeroDataRetention": true
    }
  }'
```

## コストへの影響

検索1回あたりのコストは、検索結果10件ごとに2クレジットです。スクレイピングオプションを有効にすると、各検索結果に対して標準のスクレイピングコストが適用されます：

- **Basic scrape**: ウェブページ1枚あたり1クレジット
- **PDF parsing**: PDFページ1枚あたり1クレジット
- **Enhanced proxy mode**: ウェブページ1枚あたり追加で4クレジット
- **JSON mode**: ウェブページ1枚あたり追加で4クレジット

コストを抑えるために:

- PDF解析が不要な場合は `parsers: []` を設定する
- 可能な場合は `"enhanced"` の代わりに `proxy: "basic"` を使用するか、`"auto"` に設定する
- `limit` パラメータで検索結果数を制限する

## 高度なスクレイピングオプション

スクレイピングオプションの詳細については、[Scrape 機能のドキュメント](https://docs.firecrawl.dev/features/scrape)を参照してください。FIRE-1 エージェント機能と変更追跡機能を除き、これらはすべてこの Search エンドポイントでサポートされています。

> Firecrawl API キーが必要な AI エージェントですか？ 自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。