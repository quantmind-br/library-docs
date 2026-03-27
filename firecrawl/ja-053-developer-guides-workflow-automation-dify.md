---
title: Firecrawl + Dify - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/workflow-automation/dify
source: sitemap
fetched_at: 2026-03-23T07:38:18.927447-03:00
rendered_js: false
word_count: 54
summary: This document explains how to integrate Firecrawl into Dify for web crawling and scraping tasks within AI workflows, agents, and automated data pipelines.
tags:
    - dify
    - firecrawl
    - web-scraping
    - llm-agents
    - workflow-automation
    - data-extraction
category: guide
---

Dify はオープンソースの LLM アプリ開発プラットフォームです。公式の Firecrawl プラグインにより、AI ワークフロー内でウェブのクロールとスクレイピングを直接実行できます。

## はじめに

## 利用パターン

- Chatflow Apps
- Workflow Apps
- Agent Apps

**ビジュアルパイプライン統合**

1. パイプラインに Firecrawl ノードを追加
2. アクションを選択（Map、Crawl、Scrape）
3. 入力変数を定義
4. パイプラインを順次実行

**フロー例:**

```
User Input → Firecrawl (Scrape) → LLM Processing → Response
```

**自動データ処理**次の機能で複数段階のワークフローを構築:

- 定期スクレイピング
- データ変換
- データベース保存
- 通知

**フロー例:**

```
Schedule Trigger → Firecrawl (Crawl) → Data Processing → Storage
```

**AIによるウェブアクセス**エージェントにリアルタイムのウェブスクレイピング機能を付与:

1. Agent に Firecrawl ツールを追加
2. エージェントがスクレイプ実行のタイミングを自律的に判断
3. LLM が抽出コンテンツを解析
4. エージェントが根拠に基づく応答を提供

**ユースケース:** ライブドキュメントを参照するカスタマーサポートエージェント

## 一般的なユースケース

## Firecrawl アクション

ツール説明最適な用途**Scrape**単一ページのデータ抽出コンテンツの素早い取得**Crawl**複数ページの再帰的クロールサイト全体の抽出**Map**URL の発見とサイトマップ化SEO 分析、URL リスト作成**Crawl Job**非同期ジョブ管理長時間実行タスク

## ベストプラクティス

## Dify と他プラットフォームの比較

機能DifyMakeZapiern8n**タイプ**LLMアプリプラットフォームワークフロー自動化ワークフロー自動化ワークフロー自動化**最適**AIエージェントとチャットボットビジュアルワークフロー手早い自動化開発者主導の制御**料金**オープンソース + クラウドオペレーション数ベースタスク単位月額固定**AIネイティブ**あり部分的部分的部分的**セルフホスト**可不可不可可