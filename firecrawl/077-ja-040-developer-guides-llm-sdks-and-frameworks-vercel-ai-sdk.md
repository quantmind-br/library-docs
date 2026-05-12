---
title: Vercel AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk
source: sitemap
fetched_at: 2026-03-23T07:31:11.181376-03:00
rendered_js: false
word_count: 54
summary: This document provides an implementation guide for using the Firecrawl AI SDK tools within Vercel's AI framework to perform web scraping, searching, browsing, and autonomous data extraction.
tags:
    - vercel-ai-sdk
    - firecrawl
    - web-scraping
    - ai-agents
    - browser-automation
    - data-extraction
category: guide
---

Vercel AI SDK 向け Firecrawl ツール。AI アプリケーション向けの Web スクレイピング、検索、ブラウジング、データ抽出。

## インストール

```
npm install firecrawl-aisdk ai
```

環境変数を設定する：

```
FIRECRAWL_API_KEY=fc-your-key       # https://firecrawl.dev
AI_GATEWAY_API_KEY=your-key         # https://vercel.com/ai-gateway
```

## クイックスタート

これが最も手軽な始め方です。`FirecrawlTools()` を使うと、検索・スクレイピング・ブラウザ操作用のツールに加え、どのツールを使うべきかをモデルに指示する自動生成のシステムプロンプトをまとめて利用できます。

```
import { generateText, stepCountIs } from 'ai';
import { FirecrawlTools } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Search for Firecrawl, scrape the top result, and summarize what it does',
  tools: FirecrawlTools(),
  stopWhen: stepCountIs(5),
});
```

カスタムオプションを指定する場合:

```
const tools = FirecrawlTools({
  apiKey: 'fc-custom-key',                // 省略可能。デフォルトは環境変数
  search: { limit: 3, country: 'US' },    // デフォルトの検索オプション
  scrape: { onlyMainContent: true },       // デフォルトのスクレイプオプション
  browser: {},                             // ブラウザツールを有効化
});
```

任意のツールは `false` を渡すことで無効化できます:

```
const tools = FirecrawlTools({
  browser: false,   // 検索 + スクレイプのみ
});
```

各ツールは **2 通りの使い方** ができます。ツールとして直接利用することも（環境変数から `FIRECRAWL_API_KEY` を読み取ります）、カスタム設定用のファクトリ関数として呼び出すこともできます。

```
import { scrape, search } from 'firecrawl-aisdk';

// 直接使用 - 環境変数からFIRECRAWL_API_KEYを読み込む
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape, search },
  prompt: '...',
});

// またはカスタム設定のファクトリとして呼び出す
const customScrape = scrape({ apiKey: 'fc-custom-key' });
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape: customScrape },
  prompt: '...',
});
```

### スクレイピング

```
import { generateText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'https://firecrawl.dev をスクレイピングして、その機能を要約してください',
  tools: { scrape },
});
```

### 検索

```
import { generateText } from 'ai';
import { search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Search for Firecrawl and summarize what you find',
  tools: { search },
});
```

### 検索 + スクレイピング

```
import { generateText } from 'ai';
import { search, scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Search for Firecrawl, scrape the top result, and explain what it does',
  tools: { search, scrape },
});
```

### マップ

```
import { generateText } from 'ai';
import { map } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'https://docs.firecrawl.dev をマップして主要なセクションをリストアップしてください',
  tools: { map },
});
```

### ストリーミング

```
import { streamText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const result = streamText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'https://firecrawl.dev をスクレイピングして、それが何をするものか説明してください',
  tools: { scrape },
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

## ブラウザ

`browser` ツールは、初回の利用時に自動的にクラウドセッションを作成し、プロセス終了時に自動でクリーンアップを行います。

```
import { generateText, stepCountIs } from 'ai';
import { browser } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser() },
  stopWhen: stepCountIs(25),
  prompt: 'Go to https://news.ycombinator.com and get the top 3 stories.',
});
```

ブラウザをリアルタイムで観察できるライブビュー用URLを取得したり、セッションのライフサイクルを手動で制御したりするには、次のようにします：

```
const browserTool = browser();
console.log('Live view:', await browserTool.start());

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browserTool },
  stopWhen: stepCountIs(25),
  prompt: 'Go to https://news.ycombinator.com and get the top 3 stories.',
});

await browserTool.close();
```

### Browser + Search

```
import { generateText, stepCountIs } from 'ai';
import { browser, search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser(), search },
  stopWhen: stepCountIs(25),
  prompt: '今週のトップAI論文を検索し、閲覧して、主要な知見を要約する。',
});
```

Crawl、batch scrape、extract、agent はジョブ ID を返します。結果を取得するには `poll` と組み合わせて使用します：

### Crawl

```
import { generateText } from 'ai';
import { crawl, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Crawl https://docs.firecrawl.dev (limit 3 pages) and summarize',
  tools: { crawl, poll },
});
```

### バッチスクレイプ

```
import { generateText } from 'ai';
import { batchScrape, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Scrape https://firecrawl.dev and https://docs.firecrawl.dev, then compare',
  tools: { batchScrape, poll },
});
```

### エージェント

自律的な Web データ収集 — 自動で検索・ページ遷移・データ抽出を行います。

```
import { generateText, stepCountIs } from 'ai';
import { agent, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Find the founders of Firecrawl, their roles, and their backgrounds',
  tools: { agent, poll },
  stopWhen: stepCountIs(10),
});
```

## エクスポート一覧

```
import {
  // デュアルパーパスツール（直接使用またはファクトリーとして呼び出し可能）
  scrape,             // 単一URLをスクレイプ
  search,             // ウェブを検索
  map,                // サイト上のURLを探索
  crawl,              // 複数ページをクロール（非同期）
  batchScrape,        // 複数URLをスクレイプ（非同期）
  agent,              // 自律型ウェブエージェント（非同期）
  extract,            // 構造化データを抽出（非同期）

  // ジョブ管理
  poll,               // 非同期ジョブの結果をポーリング
  status,             // ジョブのステータスを確認
  cancel,             // 実行中のジョブをキャンセル

  // ブラウザ（ファクトリー専用）
  browser,            // browser({ firecrawlApiKey: '...' })

  // オールインワンバンドル
  FirecrawlTools,     // FirecrawlTools({ apiKey, search, scrape, browser })

  // ヘルパー
  stepLogger,         // ツール呼び出しごとのトークン統計
  logStep,            // シンプルな1行ロギング
} from 'firecrawl-aisdk';
```