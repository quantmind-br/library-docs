---
title: Node SDK | Firecrawl
url: https://docs.firecrawl.dev/zh/sdks/node
source: sitemap
fetched_at: 2026-03-23T07:20:15.189748-03:00
rendered_js: false
word_count: 178
summary: This document provides a comprehensive guide for using the Firecrawl Node.js SDK to perform web scraping, site crawling, batch processing, and remote browser automation.
tags:
    - firecrawl
    - node-js
    - web-scraping
    - web-automation
    - sdk-guide
    - api-integration
    - browser-session
category: guide
---

## 安装

要安装 Firecrawl 的 Node SDK，你可以使用 npm：

```
# 使用 npm 安装 @mendable/firecrawl-js

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
```

## 使用

1. 在 [firecrawl.dev](https://firecrawl.dev) 获取 API 密钥
2. 将该密钥设置为名为 `FIRECRAWL_API_KEY` 的环境变量，或作为参数传递给 `FirecrawlApp` 类。

以下是一个包含错误处理的 SDK 使用示例：

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

// 抓取网站内容
const scrapeResponse = await firecrawl.scrape('https://firecrawl.dev', {
  formats: ['markdown', 'html'],
});

console.log(scrapeResponse)

// 爬取整站
const crawlResponse = await firecrawl.crawl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
});

console.log(crawlResponse)
```

### 抓取单个 URL

要带错误处理地抓取单个 URL，请使用 `scrapeUrl` 方法。它接收 URL 作为参数，并以字典形式返回抓取结果。

```
// 抓取网站：
const scrapeResult = await firecrawl.scrape('firecrawl.dev', { formats: ['markdown', 'html'] });

console.log(scrapeResult)
```

### 爬取网站

要在具备错误处理的情况下爬取网站，请使用 `crawlUrl` 方法。它接收起始 URL 和可选参数。通过 `params` 参数，你可以为爬取任务指定其他选项，例如最大爬取页数、允许的域名以及输出格式。有关自动/手动分页与限制的说明，请参见 [Pagination](#pagination)。

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 5, pollInterval: 1, timeout: 120 });
console.log(job.status);
```

### 仅爬取 Sitemap

使用 `sitemap: "only"` 仅爬取 sitemap 中的 URL（起始 URL 始终会被包含，并且会跳过 HTML 链接发现过程）。

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', {
  sitemap: 'only',
  limit: 25,
});
console.log(job.status, job.data.length);
```

### 启动 Crawl

使用 `startCrawl` 可立即启动作业且无需等待。它会返回一个作业 `ID`，可用于查询状态。若需要在完成前阻塞等待的方式，请使用 `crawl`。分页行为和限制详见 [Pagination](#pagination)。

```
const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
console.log(id);
```

### 检查爬取状态

要在带错误处理的情况下检查爬取任务的状态，请使用 `checkCrawlStatus` 方法。它接收 `ID` 作为参数，并返回该爬取任务的当前状态。

```
const status = await firecrawl.getCrawlStatus("<crawl-id>");
console.log(status);
```

### 取消爬取

要取消爬取任务，请使用 `cancelCrawl` 方法。该方法接收 `startCrawl` 返回的任务 ID 作为参数，并返回取消结果。

```
const ok = await firecrawl.cancelCrawl("<crawl-id>");
console.log("已取消：", ok);
```

### 网站映射

要在包含错误处理的情况下进行网站映射，请使用 `mapUrl` 方法。该方法接收起始 URL 作为参数，并以字典形式返回映射结果。

```
const res = await firecrawl.map('https://firecrawl.dev', { limit: 10 });
console.log(res.links);
```

### 使用 WebSockets 爬取网站

要通过 WebSockets 爬取网站，请使用 `crawlUrlAndWatch` 方法。它接受起始 URL 和可选参数。`params` 参数可用于为爬取任务指定更多选项，例如最大爬取页数、允许的域名，以及输出 formats。

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

// 启动一次爬取并开始监控
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

// 开始监控（优先使用 WS，回退到 HTTP）
await watcher.start();
```

当有更多数据可用时，Firecrawl 的 /crawl 和 batch 端点会返回一个 `next` URL。Node SDK 默认会自动分页并汇总所有文档；在这种情况下，`next` 将为 `null`。你可以禁用自动分页或设置上限。

#### 抓取

使用 waiter 方法 `crawl` 以获得最简便的体验，或启动一个任务并手动逐页处理。

- 请参阅[网站爬取](#crawling-a-website)中的默认流程。

<!--THE END-->

- 先启动作业，然后将 `autoPaginate: false` 设置为禁用自动分页，逐页获取。

```
const crawlStart = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 5 });
const crawlJobId = crawlStart.id;

const crawlSingle = await firecrawl.getCrawlStatus(crawlJobId, { autoPaginate: false });
console.log('单页抓取：', crawlSingle.status, '文档数：', crawlSingle.data.length, '下一页：', crawlSingle.next);
```

- 保持自动分页开启，但可通过 `maxPages`、`maxResults` 或 `maxWaitTime` 提前停止。

```
const crawlLimited = await firecrawl.getCrawlStatus(crawlJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 50,
  maxWaitTime: 15,
});
console.log('受限爬取：', crawlLimited.status, '文档数：', crawlLimited.data.length, '下一页：', crawlLimited.next);
```

#### 批量抓取

使用等待器方法 `batchScrape`，或手动启动作业并逐页处理。

- 默认流程请参见[批量抓取](https://docs.firecrawl.dev/zh/features/batch-scrape)。

<!--THE END-->

- 启动作业，将 `autoPaginate: false` 以禁用自动分页，并按页逐一获取。

```
const batchStart = await firecrawl.startBatchScrape([
  'https://docs.firecrawl.dev',
  'https://firecrawl.dev',
], { options: { formats: ['markdown'] } });
const batchJobId = batchStart.id;

const batchSingle = await firecrawl.getBatchScrapeStatus(batchJobId, { autoPaginate: false });
console.log('批量单页：', batchSingle.status, '文档数：', batchSingle.data.length, '下一页：', batchSingle.next);
```

- 保持自动分页开启，但可通过 `maxPages`、`maxResults` 或 `maxWaitTime` 提前停止。

```
const batchLimited = await firecrawl.getBatchScrapeStatus(batchJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 100,
  maxWaitTime: 20,
});
console.log('批处理受限：', batchLimited.status, '文档数：', batchLimited.data.length, '下一个：', batchLimited.next);
```

## 浏览器

在云端启动浏览器会话并远程执行代码。

### 创建会话

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const session = await firecrawl.browser({ ttl: 600 });
console.log(session.id);          // 会话 ID
console.log(session.cdpUrl);      // wss://cdp-proxy.firecrawl.dev/cdp/...
console.log(session.liveViewUrl); // https://liveview.firecrawl.dev/...
```

### 执行代码

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
});
console.log(result.result); // "Hacker News"
```

改为执行 JavaScript（而非 Python）：

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
  language: "node",
});
```

通过 agent-browser 执行 Bash：

```
const result = await firecrawl.browserExecute(session.id, {
  code: "agent-browser open https://example.com && agent-browser snapshot",
  language: "bash",
});
```

### 配置文件

在会话之间持久化并复用浏览器状态（cookies、localStorage 等）：

```
const session = await firecrawl.browser({
  ttl: 600,
  profile: {
    name: "my-profile",
    saveChanges: true,
  },
});
```

### 通过 CDP 连接

要获得对 Playwright 的完全控制能力，请使用 CDP URL 直接连接：

```
import { chromium } from "playwright";

const browser = await chromium.connectOverCDP(session.cdpUrl);
const context = browser.contexts()[0];
const page = context.pages()[0] || await context.newPage();

await page.goto("https://example.com");
console.log(await page.title());

await browser.close();
```

### 列出 & 关闭会话

```
// 列出活动会话
const { sessions } = await firecrawl.listBrowsers({ status: "active" });
for (const s of sessions) {
  console.log(s.id, s.status, s.createdAt);
}

// 关闭会话
await firecrawl.deleteBrowser(session.id);
```

## 错误处理

SDK 会处理 Firecrawl API 返回的错误并抛出相应异常。若在请求过程中发生错误，将抛出包含详细错误信息的异常。上面的示例展示了如何使用 `try/catch` 代码块来处理这些错误。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化接入说明。