---
title: Rust SDK | Firecrawl
url: https://docs.firecrawl.dev/ja/sdks/rust
source: sitemap
fetched_at: 2026-03-23T07:22:27.718139-03:00
rendered_js: false
word_count: 86
summary: This document provides a comprehensive guide on installing and utilizing the Firecrawl Rust SDK to perform web scraping, site crawling, and structured data extraction from URLs.
tags:
    - rust
    - firecrawl
    - web-scraping
    - sdk-documentation
    - data-extraction
    - api-integration
category: tutorial
---

## インストール

Firecrawl の Rust SDK をインストールするには、`Cargo.toml` に次を追加してください:

```
# これを Cargo.toml に追加します
[dependencies]
firecrawl = "^1.0"
tokio = { version = "^1", features = ["full"] }
```

## 使用方法

まずは [firecrawl.dev](https://firecrawl.dev) で API キーを取得します。次に `FirecrawlApp` を初期化します。以降は `FirecrawlApp::scrape_url` などの関数にアクセスでき、API を利用できます。 以下は Rust での SDK 利用例です:

```
use firecrawl::{crawl::{CrawlOptions, CrawlScrapeOptions, CrawlScrapeFormats}, FirecrawlApp, scrape::{ScrapeOptions, ScrapeFormats}};

#[tokio::main]
async fn main() {
    // APIキーで FirecrawlApp を初期化
    let app = FirecrawlApp::new("fc-YOUR_API_KEY").expect("FirecrawlApp の初期化に失敗しました");

    // URL をスクレイプ
    let options = ScrapeOptions {
        formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
        ..Default::default()
    };

    let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

    match scrape_result {
        Ok(data) => println!("スクレイプ結果:\n{}", data.markdown.unwrap()),
        Err(e) => eprintln!("マップの実行に失敗しました: {}", e),
    }

    // ウェブサイトをクロール
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
        Ok(data) => println!("クロール結果（使用クレジット: {}）:\n{:#?}", data.credits_used, data.data),
        Err(e) => eprintln!("クロールに失敗しました: {}", e),
    }
}
```

### URLのスクレイピング

単一のURLをスクレイプするには、`scrape_url` メソッドを使用します。URLを引数に取り、スクレイプ結果を `Document` として返します。

```
let options = ScrapeOptions {
    formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
    ..Default::default()
};

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
    Ok(data) => println!("スクレイプ結果:\n{}", data.markdown.unwrap()),
    Err(e) => eprintln!("マップに失敗しました: {}", e),
}
```

Extract を使うと、任意の URL から構造化データを簡単に抽出できます。`serde_json::json!` マクロを用いて、JSON Schema 形式でスキーマを指定する必要があります。

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
            "description": "Hacker News のトップ5件のストーリー"
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
    Ok(data) => println!("LLM抽出結果:\n{:#?}", data.extract.unwrap()),
    Err(e) => eprintln!("LLM抽出に失敗しました: {}", e),
}
```

### ウェブサイトのクロール

ウェブサイトをクロールするには、`crawl_url` メソッドを使用します。クロールが完了するまで待機します。所要時間は開始URLや指定したオプションによっては長くなる場合があります。

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
    Ok(data) => println!("クロール結果（使用クレジット: {}）:\n{:#?}", data.credits_used, data.data),
    Err(e) => eprintln!("クロールに失敗しました：{}", e),
}
```

### サイトマップ専用クロール (v2 API)

Rust SDK は現在 v1 をサポートしています。`sitemap: "only"` を使用するには、v2 エンドポイントを直接呼び出してください:

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

#### 非同期でのクロール

結果を待たずにクロールするには、`crawl_url_async` メソッドを使用します。パラメータは同一ですが、クロールの ID を含む `CrawlAsyncRespone` 構造体を返します。その ID を `check_crawl_status` メソッドで使用して、いつでもステータスを確認できます。完了したクロールは 24 時間後に削除される点にご注意ください。

```
let crawl_id = app.crawl_url_async("https://mendable.ai", None).await?.id;

// ... later ...

let status = app.check_crawl_status(crawl_id).await?;

if status.status == CrawlStatusTypes::Completed {
    println!("クロールが完了しました: {:#?}", status.data);
} else {
    // ... もう少し待つ ...
}
```

### URL をマップする

開始 URL から関連するリンクをすべてマップします。

```
let map_result = app.map_url("https://firecrawl.dev", None).await;

match map_result {
    Ok(data) => println!("抽出したURL: {:#?}", data),
    Err(e) => eprintln!("マップ処理に失敗しました: {}", e),
}
```

## エラー処理

この SDK は、Firecrawl API および依存関係から返されるエラーを処理し、それらを `Error`、`Debug`、`Display` を実装する `FirecrawlError` 列挙型にまとめます。すべてのメソッドは `Result<T, FirecrawlError>` を返します。

> Firecrawl API キーを必要とする AI エージェントですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。