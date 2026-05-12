---
title: Firecrawl を使ったブランドスタイルガイドジェネレーターの構築 - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/cookbooks/brand-style-guide-generator-cookbook
source: sitemap
fetched_at: 2026-03-23T07:38:14.177064-03:00
rendered_js: false
word_count: 154
summary: This guide explains how to build a Node.js application that uses Firecrawl's branding format to extract visual identity tokens from a website and generate a comprehensive PDF style guide.
tags:
    - web-scraping
    - brand-identity
    - pdf-generation
    - design-systems
    - nodejs
    - typescript
    - firecrawl-api
category: guide
---

任意のウェブサイトから色、タイポグラフィ、余白（スペーシング）、ビジュアルアイデンティティを自動で抽出し、それらをプロフェッショナルな PDF ドキュメントとしてまとめるブランドスタイルガイドジェネレーターを構築します。 ![Firecrawl の branding format を使ってデザインシステムを抽出するブランドスタイルガイド PDF ジェネレーター](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/brand-style-guide-pdf-generator-firecrawl.gif?s=2c8e0a9d223ea655238b17442c7bf41b)

## このガイドで構築するもの

任意のウェブサイトの URL を入力として受け取り、Firecrawl の branding format を使ってブランドアイデンティティを完全に抽出し、次の内容を含む洗練された PDF スタイルガイドを生成する Node.js アプリケーションです:

- HEX 値付きのカラーパレット
- タイポグラフィシステム（フォント、サイズ、ウェイト）
- スペーシングとレイアウトの仕様
- ロゴおよびブランド画像
- テーマ情報（ライト / ダークモード）

![色・タイポグラフィ・余白を含む生成されたブランドスタイルガイド PDF の例](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/generated-brand-style-guide-pdf-example.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=de8be5319be990d6630591afa3fc2dc2)

## 前提条件

- Node.js 18 以降がインストールされていること
- [firecrawl.dev](https://firecrawl.dev) から取得した Firecrawl API キー
- TypeScript と Node.js の基礎知識

## 動作の仕組み

1. **URL 入力**: ジェネレーターが対象サイトの URL を受け取る
2. **Firecrawl スクレイピング**: `branding` フォーマットを指定して `/scrape` エンドポイントを呼び出す
3. **ブランド分析**: Firecrawl がページの CSS、フォント、ビジュアル要素を解析する
4. **データ返却**: すべてのデザイントークンを構造化された `BrandingProfile` オブジェクトとして返す

### PDF 生成プロセス

1. **ヘッダー作成**: ブランドのプライマリカラーを使ってカラーのヘッダーを生成します
2. **ロゴ取得**: 利用可能な場合はロゴまたはファビコンをダウンロードして埋め込みます
3. **カラーパレット**: 各色をメタデータ付きの色見本としてレンダリングします
4. **タイポグラフィセクション**: フォントファミリー、サイズ、ウェイトを記載します
5. **スペーシング情報**: ベースユニット、ボーダー半径、テーマモードを含みます

### ブランディングプロファイルの構造

[branding format](https://docs.firecrawl.dev/features/scrape#%2Fscrape-with-branding-endpoint) では、ブランドに関する詳細な情報が返されます。

```
{
  colorScheme: "dark" | "light",
  logo: "https://example.com/logo.svg",
  colors: {
    primary: "#FF6B35",
    secondary: "#004E89",
    accent: "#F77F00",
    background: "#1A1A1A",
    textPrimary: "#FFFFFF",
    textSecondary: "#B0B0B0"
  },
  typography: {
    fontFamilies: { primary: "Inter", heading: "Inter", code: "Roboto Mono" },
    fontSizes: { h1: "48px", h2: "36px", body: "16px" },
    fontWeights: { regular: 400, medium: 500, bold: 700 }
  },
  spacing: {
    baseUnit: 8,
    borderRadius: "8px"
  },
  images: {
    logo: "https://example.com/logo.svg",
    favicon: "https://example.com/favicon.ico"
  }
}
```

## 主な機能

ジェネレーターはすべてのブランドカラーを検出し、カテゴリ分けします:

- **Primary & Secondary**: メインのブランドカラー
- **Accent**: ハイライトやCTA用のアクセントカラー
- **Background & Text**: UIの土台となる背景・テキストカラー
- **Semantic Colors**: 成功・警告・エラーなどの状態を表すカラー

### タイポグラフィドキュメント

タイポグラフィシステム全体を網羅しています:

- **Font Families**: 基本、見出し、等幅フォント
- **Size Scale**: すべての見出しと本文テキストのサイズ
- **Font Weights**: 利用可能なウェイト（太さ）のバリエーション

### ビジュアル出力

PDF には以下が含まれます:

- ブランドカラーに合わせたヘッダー
- 利用可能な場合のロゴの埋め込み
- 明確な階層構造を持つプロフェッショナルなレイアウト
- 生成日時を含むメタデータフッター

![元の Web サイトと生成されたブランドスタイルガイド PDF を並べて比較した画像](https://mintcdn.com/firecrawl/cdt2w_aIKa5KajZT/images/guides/cookbooks/branding-format/website-to-brand-style-guide-comparison.png?fit=max&auto=format&n=cdt2w_aIKa5KajZT&q=85&s=90153b3c2c920eceb8cd454eb266f9d0)

## カスタマイズのアイデア

### コンポーネント用ドキュメントを追加する

ジェネレーターを拡張して、UI コンポーネントのスタイルも含めるようにします:

```
// Spacing & Theme セクションの後に追加
if (b.components) {
  doc.addPage();
  doc.fontSize(20).fillColor("#333").text("UI Components", 50, 50);

  // ボタンスタイルをドキュメント化
  if (b.components.buttonPrimary) {
    const btn = b.components.buttonPrimary;
    doc.fontSize(14).text("Primary Button", 50, 90);
    doc.rect(50, 110, 120, 40).fill(btn.background);
    doc.fontSize(12).fillColor(btn.textColor).text("Button", 50, 120, { width: 120, align: "center" });
  }
}
```

### 複数フォーマットでエクスポート

PDFに加えて、JSON形式でのエクスポートも追加します:

```
// doc.end() の前に追加
fs.writeFileSync("brand-data.json", JSON.stringify(b, null, 2));
```

### バッチ処理

複数のウェブサイト用のガイドを生成します:

```
const websites = [
  "https://stripe.com",
  "https://linear.app",
  "https://vercel.com"
];

for (const site of websites) {
  const { branding } = await fc.scrape(site, { formats: ["branding"] }) as any;
  // 各サイトのPDFを生成...
}
```

### カスタム PDF テーマ

抽出したテーマに基づいて、異なる PDF スタイルを作成します。

```
const isDarkMode = b.colorScheme === "dark";
const headerBg = isDarkMode ? b.colors?.background : b.colors?.primary;
const textColor = isDarkMode ? "#fff" : "#333";
```

## ベストプラクティス

1. **欠損データの扱い**: すべてのウェブサイトが完全なブランディング情報を公開しているとは限りません。欠損しているプロパティには必ずフォールバック値を用意してください。
2. **レート制限の順守**: 複数サイトをバッチ処理する場合は、リクエスト間に遅延を挟み、Firecrawl のレート制限を順守してください。
3. **結果のキャッシュ**: 同じサイトに対する API コールを繰り返さないよう、抽出したブランディングデータを保存してください。
4. **画像フォーマットの扱い**: 一部のロゴは PDFKit がサポートしていないフォーマット（SVG など）である場合があります。フォーマット変換や、適切なフォールバック処理の追加を検討してください。
5. **エラーハンドリング**: 生成処理は try-catch ブロックで囲み、わかりやすいエラーメッセージを提供してください。

* * *