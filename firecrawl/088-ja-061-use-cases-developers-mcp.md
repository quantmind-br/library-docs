---
title: 開発者とMCP - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/use-cases/developers-mcp
source: sitemap
fetched_at: 2026-03-23T07:28:38.053278-03:00
rendered_js: false
word_count: 60
summary: This document explains how to integrate Firecrawl's Model Context Protocol (MCP) server with AI coding assistants to enable automated web scraping and data extraction capabilities.
tags:
    - firecrawl
    - mcp
    - web-scraping
    - ai-assistant
    - automation
    - data-extraction
category: guide
---

開発者は Firecrawl の Model Context Protocol (MCP) サーバーを使って、Claude Desktop、Cursor などの AI コーディングアシスタントにウェブスクレイピング機能を組み込みます。

## テンプレートから始める

## 仕組み

Model Context Protocol を通じて、Firecrawl を AI コーディングのワークフローに直接統合できます。設定が完了すると、AI アシスタントはユーザーに代わって呼び出せる一連のウェブスクレイピングツールを利用できるようになります。

Toolできること**Scrape**単一の URL からコンテンツまたは構造化データを抽出**Batch Scrape**複数の既知の URL からコンテンツを並列に抽出**Map**ウェブサイト上でインデックスされた URL をすべて検出**Crawl**サイト内の特定セクションをたどり、各ページからコンテンツを抽出**Search**ウェブを検索し、必要に応じて検索結果からコンテンツを抽出

アシスタントは適切なツールを自動的に選択します。たとえば、「Next.js のドキュメントを読んで」と依頼すればスクレイプを実行し、「example.com のブログ記事をすべて見つけて」と依頼すれば、まず Map を実行し、その後 Batch Scrape を行います。

### より賢いAIアシスタントを構築

AIにドキュメント、API、ウェブリソースへのリアルタイムアクセスを付与しましょう。最新のデータを取り込むことで、情報の陳腐化やハルシネーションを抑制できます。

### インフラは一切不要

サーバー管理もクローラーの保守も不要です。ひとたび設定すれば、Model Context Protocol を通じてAIアシスタントが即座にウェブサイトへアクセスできます。

## 顧客事例

## よくある質問

- [AI Platforms](https://docs.firecrawl.dev/ja/use-cases/ai-platforms) - AI 搭載の開発者向けツールの構築
- [Deep Research](https://docs.firecrawl.dev/ja/use-cases/deep-research) - 高度な技術リサーチ
- [Content Generation](https://docs.firecrawl.dev/ja/use-cases/content-generation) - ドキュメントの生成