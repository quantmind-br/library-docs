---
title: Rust SDK | Firecrawl
url: https://docs.firecrawl.dev/zh/sdks/rust
source: sitemap
fetched_at: 2026-03-23T07:20:18.841009-03:00
rendered_js: false
word_count: 98
summary: This document provides a technical guide for integrating and using the Firecrawl Rust SDK to perform web scraping, site crawling, and structured data extraction.
tags:
    - rust
    - firecrawl
    - web-scraping
    - data-extraction
    - sdk-integration
    - api-client
category: guide
---

## 安装

要安装 Firecrawl 的 Rust SDK，请在你的 `Cargo.toml` 中添加以下内容：

```
# 将以下内容添加到你的 Cargo.toml
[dependencies]
firecrawl = "^1.0"
tokio = { version = "^1", features = ["full"] }
```

## 使用

首先，你需要在 [firecrawl.dev](https://firecrawl.dev) 获取一个 API 密钥。接着，初始化 `FirecrawlApp`。此后即可调用 `FirecrawlApp::scrape_url` 等函数来使用我们的 API。 下面是在 Rust 中使用该 SDK 的示例：

```
use firecrawl::{crawl::{CrawlOptions, CrawlScrapeOptions, CrawlScrapeFormats}, FirecrawlApp, scrape::{ScrapeOptions, ScrapeFormats}};

#[tokio::main]
async fn main() {
    // 使用 API 密钥初始化 FirecrawlApp
    let app = FirecrawlApp::new("fc-YOUR_API_KEY").expect("初始化 FirecrawlApp 失败");

    // 抓取 URL
    let options = ScrapeOptions {
        formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
        ..Default::default()
    };

    let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

    match scrape_result {
        Ok(data) => println!("抓取结果：\n{}", data.markdown.unwrap()),
        Err(e) => eprintln!("抓取失败：{}", e),
    }

    // 爬取网站
    let crawl_options = CrawlOptions {
        scrape_options: CrawlScrapeOptions {
            formats: vec![ CrawlScrapeFormats::Markdown, CrawlScrapeFormats::HTML ].into(),
            ..Default::default()
        }.into(),
        limit: 100.into(),
        ..Default::default()
    };

    let crawl_result = app
        .crawl_url("https://mendable.ai", crawl_options)
        .await;

    match crawl_result {
        Ok(data) => println!("爬取结果（消耗了 {} 点数）：\n{:#?}", data.credits_used, data.data),
        Err(e) => eprintln!("爬取失败：{}", e),
    }
}
```

### 抓取单个 URL

要抓取单个 URL，请使用 `scrape_url` 方法。该方法以 URL 为参数，返回抓取结果，类型为 `Document`。

```
let options = ScrapeOptions {
    formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
    ..Default::default()
};

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
    Ok(data) => println!("抓取结果：\n{}", data.markdown.unwrap()),
    Err(e) => eprintln!("抓取失败：{}", e),
}
```

借助 Extract，你可以轻松从任意 URL 提取结构化数据。你需要使用 `serde_json::json!` 宏，以 JSON Schema 格式指定你的 schema。

```
let json_schema = json!({
    "type": "object",
    "properties": {
        "top": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "points": {"type": "number"},
                    "by": {"type": "string"},
                    "commentsURL": {"type": "string"}
                },
                "required": ["title", "points", "by", "commentsURL"]
            },
            "minItems": 5,
            "maxItems": 5,
            "description": "Hacker News 热门的 5 篇文章"
        }
    },
    "required": ["top"]
});

let llm_extraction_options = ScrapeOptions {
    formats: vec![ ScrapeFormats::Json ].into(),
    jsonOptions: ExtractOptions {
        schema: json_schema.into(),
        ..Default::default()
    }.into(),
    ..Default::default()
};

let llm_extraction_result = app
    .scrape_url("https://news.ycombinator.com", llm_extraction_options)
    .await;

match llm_extraction_result {
    Ok(data) => println!("LLM 提取结果：\n{:#?}", data.extract.unwrap()),
    Err(e) => eprintln!("LLM 提取失败：{}", e),
}
```

### 爬取网站

要爬取网站，请使用 `crawl_url` 方法。该方法会等待爬取过程完成；具体耗时取决于起始 URL 和所选参数，可能会较长。

```
let crawl_options = CrawlOptions {
    scrape_options: CrawlScrapeOptions {
        formats: vec![ CrawlScrapeFormats::Markdown, CrawlScrapeFormats::HTML ].into(),
        ..Default::default()
    }.into(),
    limit: 100.into(),
    ..Default::default()
};

let crawl_result = app
    .crawl_url("https://mendable.ai", crawl_options)
    .await;

match crawl_result {
    Ok(data) => println!("抓取结果（消耗了 {} 积分）：\n{:#?}", data.credits_used, data.data),
    Err(e) => eprintln!("抓取失败：{}", e),
}
```

### 仅站点地图抓取（v2 API）

Rust SDK 当前仅支持 v1。要使用 `sitemap: "only"`，请直接调用 v2 端点：

```
use reqwest::Client;
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();
    let res = client
        .post("https://api.firecrawl.dev/v2/crawl")
        .bearer_auth("fc-YOUR-API-KEY")
        .json(&json!({
            "url": "https://docs.firecrawl.dev",
            "sitemap": "only",
            "limit": 25,
        }))
        .send()
        .await?;

    println!("{}", res.text().await?);
    Ok(())
}
```

#### 异步爬取

若要在不等待结果的情况下进行爬取，请使用 `crawl_url_async` 方法。它接受相同的参数，但会返回一个 `CrawlAsyncRespone` 结构体，其中包含本次爬取的 ID。你可以使用该 ID 调用 `check_crawl_status` 方法随时查询状态。请注意，已完成的爬取将在 24 小时后被删除。

```
let crawl_id = app.crawl_url_async("https://mendable.ai", None).await?.id;

// ... 稍后 ...

let status = app.check_crawl_status(crawl_id).await?;

if status.status == CrawlStatusTypes::Completed {
    println!("抓取完成：{:#?}", status.data);
} else {
    // ... 再等一会儿 ...
}
```

### 映射 URL

从起始 URL 获取其所有关联链接的映射。

```
let map_result = app.map_url("https://firecrawl.dev", None).await;

match map_result {
    Ok(data) => println!("已映射的 URL：{:#?}", data),
    Err(e) => eprintln!("映射失败：{}", e),
}
```

## 错误处理

SDK 会处理由 Firecrawl API 及其依赖返回的错误，并将它们统一为 `FirecrawlError` 枚举，并实现了 `Error`、`Debug` 和 `Display` 接口。我们的所有方法都返回 `Result<T, FirecrawlError>`。

> 如果你是需要 Firecrawl API 密钥的 AI 代理，请参阅 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 获取自动化接入说明。