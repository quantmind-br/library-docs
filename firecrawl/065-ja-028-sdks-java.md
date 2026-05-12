---
title: Java SDK | Firecrawl
url: https://docs.firecrawl.dev/ja/sdks/java
source: sitemap
fetched_at: 2026-03-23T07:22:35.489167-03:00
rendered_js: false
word_count: 114
summary: This document provides a guide for installing and using the Firecrawl Java SDK to perform web scraping, crawling, site mapping, and AI-driven data extraction.
tags:
    - java-sdk
    - web-scraping
    - web-crawling
    - firecrawl
    - data-extraction
    - api-integration
category: guide
---

## インストール

公式の Java SDK は、Firecrawl のモノレポジトリ内にある [apps/java-sdk](https://github.com/firecrawl/firecrawl/tree/main/apps/java-sdk) で管理されています。 Firecrawl Java SDK をインストールするには、Maven Central から依存関係を追加します。

- Gradle（Kotlin DSL）
- Gradle（Groovy）
- Maven

```
repositories {
    mavenCentral()
}

dependencies {
    implementation("com.firecrawl:firecrawl-java:1.0.0")
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'com.firecrawl:firecrawl-java:1.0.0'
}

<dependency>
    <groupId>com.firecrawl</groupId>
    <artifactId>firecrawl-java</artifactId>
    <version>1.0.0</version>
</dependency>
```

## 使い方

1. [firecrawl.dev](https://firecrawl.dev) でAPI keyを取得します
2. API keyを `FIRECRAWL_API_KEY` という名前の環境変数に設定するか、`FirecrawlClient.builder().apiKey(...)` で渡します

現在のSDK APIを使った簡単な例を以下に示します。

```
import com.firecrawl.client.FirecrawlClient;
import com.firecrawl.models.CrawlJob;
import com.firecrawl.models.CrawlOptions;
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;

public class Example {
    public static void main(String[] args) {
        FirecrawlClient client = FirecrawlClient.fromEnv();

        Document doc = client.scrape(
            "https://firecrawl.dev",
            ScrapeOptions.builder()
                .formats(List.of((Object) "markdown"))
                .build()
        );

        CrawlJob crawl = client.crawl(
            "https://firecrawl.dev",
            CrawlOptions.builder().limit(5).build()
        );

        System.out.println(doc.getMarkdown());
        System.out.println("クロール済みページ数: " + (crawl.getData() != null ? crawl.getData().size() : 0));
    }
}
```

### URL のスクレイピング

単一の URL をスクレイピングするには、`scrape` メソッドを使用します。

```
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;

Document doc = client.scrape(
    "https://firecrawl.dev",
    ScrapeOptions.builder()
        .formats(List.of((Object) "markdown", "html"))
        .onlyMainContent(true)
        .waitFor(5000)
        .build()
);

System.out.println(doc.getMarkdown());
System.out.println(doc.getMetadata().get("title"));
```

`scrape` エンドポイントで `JsonFormat` を使って構造化された JSON を抽出します:

```
import com.firecrawl.models.Document;
import com.firecrawl.models.JsonFormat;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;
import java.util.Map;

JsonFormat jsonFmt = JsonFormat.builder()
    .prompt("Extract the product name and price")
    .schema(Map.of(
        "type", "object",
        "properties", Map.of(
            "name", Map.of("type", "string"),
            "price", Map.of("type", "number")
        )
    ))
    .build();

Document doc = client.scrape(
    "https://example.com/product",
    ScrapeOptions.builder()
        .formats(List.of((Object) jsonFmt))
        .build()
);

System.out.println(doc.getJson());
```

### Web サイトのクロール

Web サイトをクロールし、完了するまで待機するには、`crawl` を使用します。

```
import com.firecrawl.models.CrawlJob;
import com.firecrawl.models.CrawlOptions;
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;

CrawlJob job = client.crawl(
    "https://firecrawl.dev",
    CrawlOptions.builder()
        .limit(50)
        .maxDiscoveryDepth(3)
        .scrapeOptions(
            ScrapeOptions.builder()
                .formats(List.of((Object) "markdown"))
                .build()
        )
        .build()
);

System.out.println("Status: " + job.getStatus());
System.out.println("Progress: " + job.getCompleted() + "/" + job.getTotal());

if (job.getData() != null) {
    for (Document page : job.getData()) {
        System.out.println(page.getMetadata().get("sourceURL"));
    }
}
```

### クロールを開始する

`startCrawl` を使用すると、待機せずにジョブを開始できます。

```
import com.firecrawl.models.CrawlOptions;
import com.firecrawl.models.CrawlResponse;

CrawlResponse start = client.startCrawl(
    "https://firecrawl.dev",
    CrawlOptions.builder().limit(100).build()
);

System.out.println("Job ID: " + start.getId());
```

### クロールステータスの確認

`getCrawlStatus` でクロールの進行状況を確認できます。

```
import com.firecrawl.models.CrawlJob;

CrawlJob status = client.getCrawlStatus(start.getId());
System.out.println("Status: " + status.getStatus());
System.out.println("Progress: " + status.getCompleted() + "/" + status.getTotal());
```

### クロールのキャンセル

実行中のクロールをキャンセルするには、`cancelCrawl` を使用します。

```
import java.util.Map;

Map<String, Object> result = client.cancelCrawl(start.getId());
System.out.println(result);
```

### Web サイトのマッピング

`map` を使用してサイト上のリンクを検出します。

```
import com.firecrawl.models.MapData;
import com.firecrawl.models.MapOptions;
import java.util.Map;

MapData data = client.map(
    "https://firecrawl.dev",
    MapOptions.builder()
        .limit(100)
        .search("blog")
        .build()
);

if (data.getLinks() != null) {
    for (Map<String, Object> link : data.getLinks()) {
        System.out.println(link.get("url") + " - " + link.get("title"));
    }
}
```

### Web検索

`search` を使用すると、任意の検索設定で検索できます。

```
import com.firecrawl.models.SearchData;
import com.firecrawl.models.SearchOptions;
import java.util.Map;

SearchData results = client.search(
    "firecrawl web scraping",
    SearchOptions.builder()
        .limit(10)
        .build()
);

if (results.getWeb() != null) {
    for (Map<String, Object> result : results.getWeb()) {
        System.out.println(result.get("title") + " - " + result.get("url"));
    }
}
```

### バッチスクレイピング

`batchScrape` を使用して、複数のURLを並列にスクレイピングします。

```
import com.firecrawl.models.BatchScrapeJob;
import com.firecrawl.models.BatchScrapeOptions;
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;

BatchScrapeJob job = client.batchScrape(
    List.of("https://firecrawl.dev", "https://firecrawl.dev/blog"),
    BatchScrapeOptions.builder()
        .options(
            ScrapeOptions.builder()
                .formats(List.of((Object) "markdown"))
                .build()
        )
        .build()
);

if (job.getData() != null) {
    for (Document doc : job.getData()) {
        System.out.println(doc.getMarkdown());
    }
}
```

### エージェント

`agent` でAIエージェントを実行します。

```
import com.firecrawl.models.AgentOptions;
import com.firecrawl.models.AgentStatusResponse;

AgentStatusResponse result = client.agent(
    AgentOptions.builder()
        .prompt("Find the pricing plans for Firecrawl and compare them")
        .build()
);

System.out.println(result.getData());
```

構造化出力用のJSONスキーマを使用する場合：

```
import com.firecrawl.models.AgentOptions;
import com.firecrawl.models.AgentStatusResponse;
import java.util.List;
import java.util.Map;

AgentStatusResponse result = client.agent(
    AgentOptions.builder()
        .prompt("Extract pricing plan details")
        .urls(List.of("https://firecrawl.dev"))
        .schema(Map.of(
            "type", "object",
            "properties", Map.of(
                "plans", Map.of(
                    "type", "array",
                    "items", Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "name", Map.of("type", "string"),
                            "price", Map.of("type", "string")
                        )
                    )
                )
            )
        ))
        .build()
);

System.out.println(result.getData());
```

### 使用状況とメトリクス

同時実行数と残りのクレジットを確認できます。

```
import com.firecrawl.models.ConcurrencyCheck;
import com.firecrawl.models.CreditUsage;

ConcurrencyCheck concurrency = client.getConcurrency();
System.out.println("Concurrency: " + concurrency.getConcurrency() + "/" + concurrency.getMaxConcurrency());

CreditUsage credits = client.getCreditUsage();
System.out.println("Remaining credits: " + credits.getRemainingCredits());
```

## 非同期サポート

非同期版は標準で用意されており、`CompletableFuture` を返します。

```
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;
import java.util.concurrent.CompletableFuture;

CompletableFuture<Document> future = client.scrapeAsync(
    "https://example.com",
    ScrapeOptions.builder()
        .formats(List.of((Object) "markdown"))
        .build()
);

future.thenAccept(doc -> System.out.println(doc.getMarkdown()));
```

## Browser

Java SDK には、Browser Sandbox 用のヘルパーが含まれています。

### セッションを作成する

```
import com.firecrawl.models.BrowserCreateResponse;

BrowserCreateResponse session = client.browser(120, 60, true);
System.out.println(session.getId());
System.out.println(session.getCdpUrl());
System.out.println(session.getLiveViewUrl());
```

### コードの実行

```
import com.firecrawl.models.BrowserExecuteResponse;

BrowserExecuteResponse run = client.browserExecute(
    session.getId(),
    "await page.goto(\"https://example.com\"); console.log(await page.title());",
    "node",
    60
);

System.out.println(run.getStdout());
System.out.println(run.getExitCode());
```

### セッションの一覧表示 & 終了

```
import com.firecrawl.models.BrowserDeleteResponse;
import com.firecrawl.models.BrowserListResponse;
import com.firecrawl.models.BrowserSession;

BrowserListResponse active = client.listBrowsers("active");
if (active.getSessions() != null) {
    for (BrowserSession s : active.getSessions()) {
        System.out.println(s.getId() + " - " + s.getStatus());
    }
}

BrowserDeleteResponse closed = client.deleteBrowser(session.getId());
System.out.println("Closed: " + closed.isSuccess());
```

## 設定

`FirecrawlClient.builder()` では、次のオプションを使用できます。

OptionTypeDefaultDescription`apiKey``String``FIRECRAWL_API_KEY` 環境変数または `firecrawl.apiKey` システムプロパティFirecrawl の API キー`apiUrl``String``https://api.firecrawl.dev` (または `FIRECRAWL_API_URL`)API のベース URL`timeoutMs``long``300000`HTTP リクエストのタイムアウト (ミリ秒)`maxRetries``int``3`一時的な障害に対する自動リトライ回数`backoffFactor``double``0.5`秒単位の指数バックオフ係数`asyncExecutor``Executor``ForkJoinPool.commonPool()`非同期メソッド用のカスタム Executor

```
import com.firecrawl.client.FirecrawlClient;

FirecrawlClient client = FirecrawlClient.builder()
    .apiKey("fc-your-api-key")
    .apiUrl("https://api.firecrawl.dev")
    .timeoutMs(300_000)
    .maxRetries(3)
    .backoffFactor(0.5)
    .build();
```

## エラーハンドリング

SDK は `com.firecrawl.errors` 配下でランタイム例外をスローします。

```
import com.firecrawl.errors.AuthenticationException;
import com.firecrawl.errors.FirecrawlException;
import com.firecrawl.errors.JobTimeoutException;
import com.firecrawl.errors.RateLimitException;
import com.firecrawl.models.Document;

try {
    Document doc = client.scrape("https://example.com");
} catch (AuthenticationException e) {
    System.err.println("Auth failed: " + e.getMessage());
} catch (RateLimitException e) {
    System.err.println("Rate limited: " + e.getMessage());
} catch (JobTimeoutException e) {
    System.err.println("Job " + e.getJobId() + " timed out after " + e.getTimeoutSeconds() + "s");
} catch (FirecrawlException e) {
    System.err.println("Error " + e.getStatusCode() + ": " + e.getMessage());
}
```

> Firecrawl API キーが必要な AI エージェントですか？ 自動オンボーディングの手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。