---
title: Node SDK | Firecrawl
url: https://docs.firecrawl.dev/ja/sdks/node
source: sitemap
fetched_at: 2026-03-23T07:22:31.613705-03:00
rendered_js: false
word_count: 149
summary: This document provides a comprehensive guide on using the Firecrawl Node.js SDK to scrape, crawl, and map websites, including instructions on handling job statuses, pagination, and real-time monitoring via WebSockets.
tags:
    - firecrawl
    - node-sdk
    - web-scraping
    - web-crawling
    - automation
    - api-integration
    - javascript
category: guide
---

## インストール

Firecrawl の Node SDK をインストールするには、npm を使用します。

```
# npm install @mendable/firecrawl-js

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
```

## 使い方

1. [firecrawl.dev](https://firecrawl.dev) から API キーを取得します。
2. 環境変数 `FIRECRAWL_API_KEY` に API キーを設定するか、`FirecrawlApp` クラスにパラメータとして渡します。

エラーハンドリング付きで SDK を使用する例は次のとおりです:

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

// ウェブサイトをスクレイピングする
const scrapeResponse = await firecrawl.scrape('https://firecrawl.dev', {
  formats: ['markdown', 'html'],
});

console.log(scrapeResponse)

// ウェブサイトをクロールする
const crawlResponse = await firecrawl.crawl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
});

console.log(crawlResponse)
```

### URLをスクレイピングする

エラー処理付きで単一のURLをスクレイプするには、`scrapeUrl` メソッドを使用します。URLを引数に取り、スクレイプしたデータをディクショナリ（辞書）として返します。

```
// ウェブサイトをスクレイピングする：
const scrapeResult = await firecrawl.scrape('firecrawl.dev', { formats: ['markdown', 'html'] });

console.log(scrapeResult)
```

### ウェブサイトのクロール

エラーハンドリング込みでウェブサイトをクロールするには、`crawlUrl` メソッドを使用します。開始URLと任意のパラメータを引数に取ります。`params` 引数では、クロールする最大ページ数、許可ドメイン、出力フォーマットなど、クロールジョブの追加オプションを指定できます。自動／手動のページネーションや上限設定については [Pagination](#pagination) を参照してください。

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 5, pollInterval: 1, timeout: 120 });
console.log(job.status);
```

### サイトマップのみクロール

`sitemap: "only"` を使用すると、サイトマップ内の URL のみをクロールします（開始URLは常に対象に含まれ、HTML リンクの探索は行われません）。

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', {
  sitemap: 'only',
  limit: 25,
});
console.log(job.status, job.data.length);
```

### クローリングを開始

`startCrawl` を使うと待機せずにジョブを開始できます。ステータス確認に使えるジョブの `ID` が返されます。完了まで処理をブロックするウェイターが必要な場合は `crawl` を使用してください。ページングの挙動と制限については [Pagination](#pagination) を参照してください。

```
const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
console.log(id);
```

### クロールのステータス確認

エラー処理付きでクロールジョブのステータスを確認するには、`checkCrawlStatus` メソッドを使用します。`ID` を引数に取り、クロールジョブの現在のステータスを返します。

```
const status = await firecrawl.getCrawlStatus("<crawl-id>");
console.log(status);
```

### クロールのキャンセル

クロールジョブをキャンセルするには、`cancelCrawl` メソッドを使用します。`startCrawl` のジョブIDを引数に渡すと、キャンセル結果のステータスが返されます。

```
const ok = await firecrawl.cancelCrawl("<crawl-id>");
console.log("キャンセル済み:", ok);
```

### ウェブサイトのマッピング

エラー処理込みでウェブサイトをマッピングするには、`mapUrl` メソッドを使用します。開始 URL を引数に取り、マッピング結果をディクショナリとして返します。

```
const res = await firecrawl.map('https://firecrawl.dev', { limit: 10 });
console.log(res.links);
```

### WebSocket を使ったサイトのクロール

WebSocket を使ってサイトをクロールするには、`crawlUrlAndWatch` メソッドを使用します。開始 URL と任意のパラメータを引数に取ります。`params` 引数では、クロールする最大ページ数、許可ドメイン、出力フォーマットなど、クロールジョブの追加オプションを指定できます。

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

// クロールを開始して監視する
const { id } = await firecrawl.startCrawl('https://mendable.ai', {
  excludePaths: ['blog/*'],
  limit: 5,
});

const watcher = firecrawl.watcher(id, { kind: 'crawl', pollInterval: 2, timeout: 120 });

watcher.on('document', (doc) => {
  console.log('DOC', doc);
});

watcher.on('error', (err) => {
  console.error('ERR', err?.error || err);
});

watcher.on('done', (state) => {
  console.log('DONE', state.status);
});

// 監視を開始（WS と HTTP のフォールバック）
await watcher.start();
```

Firecrawl の /crawl と batch の各エンドポイントは、追加のデータがある場合に `next` URL を返します。Node SDK はデフォルトで自動ページネーションを行い、すべてのドキュメントを集約します。その場合は `next` が `null` になります。自動ページネーションを無効にしたり、上限を設定したりできます。

#### クロール

最も手軽なのはウェイター方式の `crawl` を使うことです。あるいはジョブを開始して、ページングを手動で行ってください。

- 既定のフローは[ウェブサイトのクロール](#crawling-a-website)を参照してください。

<!--THE END-->

- ジョブを開始し、`autoPaginate: false` を指定して1ページずつ取得します。

```
const crawlStart = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 5 });
const crawlJobId = crawlStart.id;

const crawlSingle = await firecrawl.getCrawlStatus(crawlJobId, { autoPaginate: false });
console.log('単一ページのクロール:', crawlSingle.status, 'ドキュメント数:', crawlSingle.data.length, '次:', crawlSingle.next);
```

- 自動ページネーションはオンのまま、`maxPages`、`maxResults`、または `maxWaitTime` で早めに停止します。

```
const crawlLimited = await firecrawl.getCrawlStatus(crawlJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 50,
  maxWaitTime: 15,
});
console.log('クロール制限:', crawlLimited.status, 'ドキュメント数:', crawlLimited.data.length, '次:', crawlLimited.next);
```

#### バッチスクレイプ

waiter メソッド `batchScrape` を使うか、ジョブを開始して手動でページングします。

- 既定のフローは [Batch Scrape](https://docs.firecrawl.dev/ja/features/batch-scrape) を参照してください。

<!--THE END-->

- ジョブを開始し、`autoPaginate: false` を指定して1ページずつ取得します。

```
const batchStart = await firecrawl.startBatchScrape([
  'https://docs.firecrawl.dev',
  'https://firecrawl.dev',
], { options: { formats: ['markdown'] } });
const batchJobId = batchStart.id;

const batchSingle = await firecrawl.getBatchScrapeStatus(batchJobId, { autoPaginate: false });
console.log('バッチ単一ページ:', batchSingle.status, 'ドキュメント数:', batchSingle.data.length, '次:', batchSingle.next);
```

- 自動ページネーションは有効のまま、`maxPages`、`maxResults`、または `maxWaitTime` で早期停止します。

```
const batchLimited = await firecrawl.getBatchScrapeStatus(batchJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 100,
  maxWaitTime: 20,
});
console.log('バッチ制限:', batchLimited.status, 'ドキュメント:', batchLimited.data.length, '次:', batchLimited.next);
```

## ブラウザ

クラウドブラウザセッションを起動し、リモートでコードを実行します。

### セッションを作成する

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const session = await firecrawl.browser({ ttl: 600 });
console.log(session.id);          // セッションID
console.log(session.cdpUrl);      // wss://cdp-proxy.firecrawl.dev/cdp/...
console.log(session.liveViewUrl); // https://liveview.firecrawl.dev/...
```

### コードの実行

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
});
console.log(result.result); // "Hacker News"
```

Python の代わりに JavaScript を実行する:

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
  language: "node",
});
```

agent-browser 経由で Bash を実行する:

```
const result = await firecrawl.browserExecute(session.id, {
  code: "agent-browser open https://example.com && agent-browser snapshot",
  language: "bash",
});
```

### プロファイル

ブラウザの状態（Cookie、localStorage など）をセッション間で保存して再利用できます:

```
const session = await firecrawl.browser({
  ttl: 600,
  profile: {
    name: "my-profile",
    saveChanges: true,
  },
});
```

### CDP 経由で接続する

Playwright をフルに制御するには、CDP URL を使用して直接接続します。

```
import { chromium } from "playwright";

const browser = await chromium.connectOverCDP(session.cdpUrl);
const context = browser.contexts()[0];
const page = context.pages()[0] || await context.newPage();

await page.goto("https://example.com");
console.log(await page.title());

await browser.close();
```

### セッションの一覧表示とクローズ

```
// アクティブなセッションを一覧表示
const { sessions } = await firecrawl.listBrowsers({ status: "active" });
for (const s of sessions) {
  console.log(s.id, s.status, s.createdAt);
}

// Close a session
await firecrawl.deleteBrowser(session.id);
```

## エラーハンドリング

この SDK は Firecrawl API から返されるエラーを処理し、適切な例外を送出します。リクエスト中にエラーが発生した場合は、わかりやすいエラーメッセージ付きの例外が送出されます。上記の例では、`try/catch` ブロックを使ってこれらのエラーを処理する方法を示しています。

> Firecrawl API キーが必要な AI agent ですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。