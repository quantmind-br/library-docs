---
title: スクレイピング | Firecrawl
url: https://docs.firecrawl.dev/ja/features/scrape
source: sitemap
fetched_at: 2026-03-23T07:22:45.601932-03:00
rendered_js: false
word_count: 303
summary: FirecrawlはウェブサイトをクリーンなMarkdownや構造化データに変換し、LLMアプリケーションへの統合を容易にするスクレイピングAPIプラットフォームです。
tags:
    - web-scraping
    - llm
    - markdown-conversion
    - structured-data
    - api-reference
    - data-extraction
category: api
---

Firecrawl はウェブページをMarkdownに変換し、LLMアプリケーションに最適です。

- 複雑な処理を代行：プロキシ、キャッシュ、レート制限、JSでブロックされたコンテンツ
- 動的コンテンツに対応：動的サイト、JSレンダリングサイト、PDF、画像
- クリーンなMarkdown、構造化データ、スクリーンショット、またはHTMLを出力

詳細は、[Scrape Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape)を参照してください。

### /scrape エンドポイント

URL をスクレイピングして、その内容を取得するために使用します。

### インストール

### 使い方

パラメータの詳細は、[APIリファレンス](https://docs.firecrawl.dev/api-reference/endpoint/scrape)を参照してください。

### レスポンス

SDK はデータオブジェクトを直接返します。cURL は以下のとおり、ペイロードをそのまま返します。

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I が開幕！[2日目のリリースを見る 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 2か月無料をゲット...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "ホーム - Firecrawl",
      "description": "Firecrawl は、あらゆるウェブサイトをクリーンな Markdown にクロールして変換します。",
      "language": "en",
      "keywords": "Firecrawl,Markdown,データ,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "あらゆるウェブサイトを LLM で使えるデータに変換。",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl"
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
```

## スクレイプのフォーマット

出力のフォーマットを選択できます。複数の出力フォーマットを指定することも可能です。サポートされているフォーマットは次のとおりです:

- Markdown (`markdown`)
- Summary (`summary`)
- HTML (`html`) - ページの HTML をクリーンアップしたバージョン
- Raw HTML (`rawHtml`) - ページから取得した変更前の HTML
- Screenshot (`screenshot`、`fullPage`、`quality`、`viewport` などのオプションあり) — スクリーンショットのURLは24時間後に期限切れになります
- Links (`links`)
- JSON (`json`) - 構造化された出力
- Images (`images`) - ページ内のすべての画像URLを抽出
- Branding (`branding`) - ブランドアイデンティティとデザインシステムを抽出

出力のキーは、選択したフォーマットに対応します。

### /scrape (json あり) エンドポイント

スクレイピングしたページから構造化データを抽出するために使用します。

出力:

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI対応のウェブスクレイピングとデータ抽出",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI対応のウェブスクレイピングとデータ抽出",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI対応のウェブスクレイピングとデータ抽出",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

エンドポイントに `prompt` を渡すだけで、スキーマなしで抽出できます。LLM がデータ構造を決定します。

出力:

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI搭載のウェブスクレイピングとデータ抽出",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI搭載のウェブスクレイピングとデータ抽出",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI搭載のウェブスクレイピングとデータ抽出",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### JSON フォーマットのオプション

`json` フォーマットを使用する場合は、`formats` 内に以下のパラメータを含むオブジェクトを渡します:

- `schema`: 構造化出力のための JSON Schema。
- `prompt`: スキーマがある場合や、軽い指示で十分な場合に抽出を補助する任意のプロンプト。

## ブランドアイデンティティの抽出

### /scrape (ブランディング付き) エンドポイント

ブランディングフォーマットは、色、フォント、タイポグラフィ、余白・間隔、UIコンポーネントなど、ウェブページからブランドアイデンティティに関する包括的な情報を抽出します。デザインシステムの分析やブランド監視、ウェブサイトのビジュアルアイデンティティを把握する必要があるツールの構築に有用です。

### レスポンス

ブランディングフォーマットは、以下の構造を持つ包括的な `BrandingProfile` オブジェクトを返します。

```
{
  "success": true,
  "data": {
    "branding": {
      "colorScheme": "dark",
      "logo": "https://firecrawl.dev/logo.svg",
      "colors": {
        "primary": "#FF6B35",
        "secondary": "#004E89",
        "accent": "#F77F00",
        "background": "#1A1A1A",
        "textPrimary": "#FFFFFF",
        "textSecondary": "#B0B0B0"
      },
      "fonts": [
        {
          "family": "Inter"
        },
        {
          "family": "Roboto Mono"
        }
      ],
      "typography": {
        "fontFamilies": {
          "primary": "Inter",
          "heading": "Inter",
          "code": "Roboto Mono"
        },
        "fontSizes": {
          "h1": "48px",
          "h2": "36px",
          "h3": "24px",
          "body": "16px"
        },
        "fontWeights": {
          "regular": 400,
          "medium": 500,
          "bold": 700
        }
      },
      "spacing": {
        "baseUnit": 8,
        "borderRadius": "8px"
      },
      "components": {
        "buttonPrimary": {
          "background": "#FF6B35",
          "textColor": "#FFFFFF",
          "borderRadius": "8px"
        },
        "buttonSecondary": {
          "background": "transparent",
          "textColor": "#FF6B35",
          "borderColor": "#FF6B35",
          "borderRadius": "8px"
        }
      },
      "images": {
        "logo": "https://firecrawl.dev/logo.svg",
        "favicon": "https://firecrawl.dev/favicon.ico",
        "ogImage": "https://firecrawl.dev/og-image.png"
      }
    }
  }
}
```

### ブランディングプロファイルの構造

`branding` オブジェクトには次のプロパティが含まれます:

- `colorScheme`: 検出された配色 (`"light"` または `"dark"`)
- `logo`: メインロゴの URL
- `colors`: ブランドカラーを含むオブジェクト:
  
  - `primary`, `secondary`, `accent`: 主要なブランドカラー
  - `background`, `textPrimary`, `textSecondary`: UI カラー
  - `link`, `success`, `warning`, `error`: セマンティックカラー
- `fonts`: ページで使用されているフォントファミリーの配列
- `typography`: タイポグラフィの詳細情報:
  
  - `fontFamilies`: 基本、見出し、コード用のフォントファミリー
  - `fontSizes`: 見出しと本文のサイズ定義
  - `fontWeights`: ウェイトの定義 (light、regular、medium、bold)
  - `lineHeights`: テキスト種別ごとの行の高さ
- `spacing`: 余白とレイアウト情報:
  
  - `baseUnit`: 基準となるスペーシング単位 (px)
  - `borderRadius`: 既定の角丸半径
  - `padding`, `margins`: スペーシング値
- `components`: UI コンポーネントのスタイル:
  
  - `buttonPrimary`, `buttonSecondary`: ボタンスタイル
  - `input`: 入力フィールドのスタイル
- `icons`: アイコンのスタイル情報
- `images`: ブランド画像 (ロゴ、favicon、og:image)
- `animations`: アニメーションおよびトランジション設定
- `layout`: レイアウト構成 (グリッド、ヘッダー／フッターの高さ)
- `personality`: ブランドの特性 (トーン、エネルギー、対象ユーザー)

### 他のフォーマットとの併用

ブランディング用フォーマットを他のフォーマットと組み合わせることで、ページの包括的なデータを取得できます:

## アクションを使ってページとやり取りする

Firecrawl を使うと、スクレイピングの前に Web ページ上でさまざまなアクションを実行できます。これは、動的コンテンツとのインタラクション、ページ遷移、ユーザー操作が必要なコンテンツへのアクセスに特に有効です。 以下は、アクションを使って google.com に移動し、Firecrawl を検索し、最初の結果をクリックしてスクリーンショットを取得する例です。 ページの読み込み時間を確保するため、他のアクションの前後には基本的に `wait` アクションを使用することが重要です。

### 例

### 出力

アクションのパラメーターの詳細は、[APIリファレンス](https://docs.firecrawl.dev/api-reference/endpoint/scrape)を参照してください。

## ロケーションと言語

ターゲットの地域と言語設定に基づいて関連性の高いコンテンツを得るため、国と言語の優先順を指定します。

### 仕組み

ロケーション設定を指定すると、Firecrawl は利用可能な場合は適切なプロキシを使用し、対応する言語とタイムゾーンをエミュレートします。指定がない場合、ロケーションのデフォルトは「US」です。

### 使い方

場所と言語の設定を使うには、リクエストボディに `location` オブジェクトを含め、次のプロパティを指定します:

- `country`: ISO 3166-1 alpha-2 の国コード (例: ‘US’, ‘AU’, ‘DE’, ‘JP’) 。既定値は ‘US’。
- `languages`: 優先度順に並べた、リクエストで使用する希望言語およびロケールの配列。既定値は指定した location の言語。

対応している地域の詳細は、[Proxies ドキュメント](https://docs.firecrawl.dev/ja/features/proxies)を参照してください。

## キャッシュと maxAge

リクエストを高速化するため、Firecrawl は最近のコピーがある場合、デフォルトでキャッシュから結果を返します。

- **デフォルトの鮮度ウィンドウ**: `maxAge = 172800000` ms (2日) 。キャッシュされたページがこの値より新しければ即時に返し、そうでなければスクレイプしてからキャッシュします。
- **パフォーマンス**: データが厳密な最新性を要さない場合、スクレイプを最大5倍高速化できます。
- **常に最新を取得**: `maxAge` を `0` に設定します。この設定ではキャッシュを完全にバイパスするため、すべてのリクエストがスクレイピングパイプライン全体を通過し、リクエストが完了するまでの時間が長くなり、失敗する可能性も高くなります。すべてのリクエストで厳密な最新性が必須でない場合は、0以外の `maxAge` を使用してください。
- **保存しない**: このリクエストの結果を Firecrawl にキャッシュ/保存させたくない場合は、`storeInCache` を `false` に設定します。
- **キャッシュのみの参照**: 新しいスクレイプを実行せず、キャッシュのみを参照するには `minAge` を設定します。値はミリ秒単位で、キャッシュデータが満たす必要のある最小経過時間を指定します。キャッシュデータが見つからない場合は、エラーコード `SCRAPE_NO_CACHED_DATA` を伴う `404` が返されます。経過時間に関係なく任意のキャッシュデータを受け入れるには、`minAge` を `1` に設定します。
- **変更トラッキング**: `changeTracking` を含むリクエストはキャッシュをバイパスするため、`maxAge` は無視されます。

例 (常に最新コンテンツを取得) :

例 (10分のキャッシュウィンドウを使用) :

## 複数のURLのバッチスクレイピング

複数のURLを同時にバッチスクレイピングできるようになりました。開始URLと任意のパラメータを引数として受け取ります。params引数では、出力フォーマットなど、バッチスクレイピングジョブの追加オプションを指定できます。

### 仕組み

これは `/crawl` エンドポイントの動作に非常によく似ています。バッチスクレイプのジョブを送信し、進行状況を確認するためのジョブIDを返します。 SDK は同期型と非同期型の2つのメソッドを提供します。同期型はバッチスクレイプジョブの結果を返し、非同期型はバッチスクレイプのステータス確認に使えるジョブIDを返します。

### 使い方

### Response

SDK の同期メソッドを使用している場合は、バッチスクレイプジョブの結果が返ります。同期メソッド以外では、バッチスクレイプのステータス確認に使用できるジョブ ID が返ります。

#### 同期処理

```
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Firecrawl Docs のホームページ![light logo](https://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg)!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Groq Llama 3 で「ウェブサイトと会話できる」機能を構築する | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Firecrawl、Groq Llama 3、LangChain を使って「自分のウェブサイトと会話できる」ボットを構築する方法を学びます。",
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

#### 非同期

その後、ジョブIDを使って `/batch/scrape/{id}` エンドポイントを呼び出し、バッチスクレイプのステータスを確認できます。 このエンドポイントは、ジョブの実行中、または完了直後に使用することを想定しています。**バッチスクレイプのジョブは24時間で有効期限が切れるため**です。

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## 強化モード

複雑なウェブサイト向けに、Firecrawl はプライバシーを保護しながら成功率を向上させる強化モードを提供しています。 [強化モード](https://docs.firecrawl.dev/ja/features/enhanced-mode)について詳しくはこちら。

## ゼロデータ保持 (ZDR)

Firecrawl は、厳格なデータ取り扱い要件を持つチーム向けに、ゼロデータ保持 (ZDR) をサポートしています。有効にすると、Firecrawl はページのコンテンツや抽出されたデータを、request の存続期間を超えて保持しません。 ZDR を有効にするには、request で `zeroDataRetention: true` を設定します。

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fc-YOUR_API_KEY" \
  -d '{
    "url": "https://example.com",
    "formats": ["markdown"],
    "zeroDataRetention": true
  }'
```

ZDR は Enterprise プランで利用でき、チームで有効化する必要があります。利用を開始するには、[firecrawl.dev/enterprise](https://www.firecrawl.dev/enterprise) をご覧ください。 ZDR では、基本のスクレイピングコストに加えて、**1ページあたり追加で1クレジット**が発生します。

> Firecrawl API キーが必要な AI エージェントですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。