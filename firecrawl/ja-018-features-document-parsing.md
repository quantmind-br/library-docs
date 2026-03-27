---
title: ドキュメントパース | Firecrawl
url: https://docs.firecrawl.dev/ja/features/document-parsing
source: sitemap
fetched_at: 2026-03-23T07:23:09.506112-03:00
rendered_js: false
word_count: 75
summary: This document explains how to use Firecrawl to extract and convert various file formats, including Excel, Word, and PDF documents, into structured markdown content.
tags:
    - firecrawl
    - document-parsing
    - pdf-extraction
    - data-scraping
    - markdown-conversion
    - ocr-processing
category: guide
---

Firecrawl は強力なドキュメント解析機能を備えており、さまざまなドキュメントフォーマットから構造化コンテンツを抽出できます。この機能は、スプレッドシートや Word 文書などのファイルを処理する際に特に有用です。

## サポートされているドキュメントフォーマット

Firecrawl は現在、以下のドキュメントフォーマットをサポートしています：

- **Excel スプレッドシート**（`.xlsx`, `.xls`）
  
  - 各ワークシートを HTML テーブルに変換します
  - ワークシートはシート名の H2 見出しで区切られます
  - セルの書式とデータ型を保持します
- **Word ドキュメント**（`.docx`, `.doc`, `.odt`, `.rtf`）
  
  - ドキュメント構造を保ちながらテキストコンテンツを抽出します
  - 見出し、段落、リスト、表を保持します
  - 基本的な書式とスタイルを保持します
- **PDF ドキュメント**（`.pdf`）
  
  - レイアウト情報とともにテキストコンテンツを抽出します
  - セクションや段落を含むドキュメント構造を保持します
  - テキストベースおよびスキャン PDF の両方に対応します（OCR 対応）
  - 解析方法を制御するための `mode` オプションをサポートします：`fast`（テキストのみ）、`auto`（必要に応じて OCR を行うテキスト、デフォルト）、`ocr`（OCR のみを使用）
  - 料金は1ページあたり1クレジットです。詳細は [Pricing](https://docs.firecrawl.dev/pricing) を参照してください。

### PDF 解析モード

PDF の処理方法を制御するには、`parsers` オプションを使用します:

ModeDescription`auto`まず高速なテキストベースの抽出を試行し、必要に応じて OCR にフォールバックします。これがデフォルトです。`fast`テキストベースの解析のみ（埋め込みテキスト）。最速のオプションですが、スキャンされたページや画像が多いページからはテキストを抽出しません。`ocr`すべてのページで OCR による解析を強制します。スキャンされたドキュメントや、`auto` がページを誤って判定してしまう場合に使用します。

```
// モード指定のオブジェクト構文
parsers: [{ type: "pdf", mode: "ocr", maxPages: 20 }]

// デフォルト（autoモード）
parsers: [{ type: "pdf" }]
```

## ドキュメント解析の使い方

Firecrawl のドキュメント解析は、サポート対象のドキュメントタイプを指す URL を指定すると自動的に実行されます。システムは、URL の拡張子または Content-Type ヘッダーに基づいてファイルタイプを検出し、適切に処理します。

### 例: Excel ファイルのスクレイピング

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const doc = await firecrawl.scrape('https://example.com/data.xlsx');

console.log(doc.markdown);
```

### 例：Word ドキュメントのスクレイピング

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const doc = await firecrawl.scrape('https://example.com/data.docx');

console.log(doc.markdown);
```

## 出力フォーマット

サポートされているすべてのドキュメントタイプは、クリーンで構造化されたmarkdownに変換されます。たとえば、複数のシートを含むExcelファイルは、次のように変換されることがあります。

```
## Sheet1

| Name  | Value |
|-------|-------|
| Item 1 | 100   |
| Item 2 | 200   |

## Sheet2

| Date       | Description  |
|------------|--------------|
| 2023-01-01 | First quarter|
```

> Firecrawl API key が必要な AI エージェントですか？自動オンボーディングの手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。