---
title: Go SDK | Firecrawl
url: https://docs.firecrawl.dev/ja/sdks/go
source: sitemap
fetched_at: 2026-03-23T07:22:34.456441-03:00
rendered_js: false
word_count: 63
summary: This document provides a guide for installing and using the Firecrawl Go SDK, covering core functionalities such as scraping URLs, crawling websites, and checking job statuses.
tags:
    - firecrawl
    - go-sdk
    - web-scraping
    - crawling
    - api-client
    - data-extraction
category: tutorial
---

## インストール

Firecrawl の Go SDK をインストールするには、go get を使用します。

```
go get github.com/mendableai/firecrawl-go
```

## 使い方

1. [firecrawl.dev](https://firecrawl.dev) から API キーを取得します。
2. `API key` を `FirecrawlApp` 構造体のパラメータとして設定します。
3. `API URL` を設定するか、`FirecrawlApp` 構造体にパラメータとして渡します。デフォルトは `https://api.firecrawl.dev` です。
4. `version` を設定するか、`FirecrawlApp` 構造体にパラメータとして渡します。デフォルトは `v1` です。

エラーハンドリング付きで SDK を使用する例は次のとおりです:

```
import (
	"fmt"
	"log"
	"github.com/google/uuid"
	"github.com/mendableai/firecrawl-go"
)

func ptr[T any](v T) *T {
	return &v
}

func main() {
	// APIキーで FirecrawlApp を初期化する
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"

	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("FirecrawlApp の初期化に失敗しました: %v", err)
	}

  // ウェブサイトをスクレイピングする
  scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
    Formats: []string{"markdown", "html"},
  })
  if err != nil {
    log.Fatalf("スクレイピングリクエストの送信に失敗しました: %v", err)
  }

  fmt.Println(scrapeStatus)

	// ウェブサイトをクロールする
  idempotencyKey := uuid.New().String() // 任意のべき等性キー
  crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     ptr(2),
	}

	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("クロールリクエストの送信に失敗しました: %v", err)
	}

	fmt.Println(crawlStatus) 
}
```

### URLのスクレイピング

エラー処理付きで単一のURLをスクレイピングするには、`ScrapeURL` メソッドを使用します。URLを引数に取り、取得したデータをディクショナリとして返します。

```
// ウェブサイトをスクレイピングする
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
  "formats": []string{"markdown", "html"},
})
if err != nil {
  log.Fatalf("URL のスクレイピングに失敗しました: %v", err)
}

fmt.Println(scrapeResult)
```

### ウェブサイトをクロールする

ウェブサイトをクロールするには、`CrawlUrl` メソッドを使用します。開始URLと任意のパラメータを引数に取ります。`params` 引数では、クロールする最大ページ数、許可ドメイン、出力フォーマットなど、クロールジョブの追加オプションを指定できます。

```
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
  "limit": 100,
  "scrapeOptions": map[string]any{
    "formats": []string{"markdown", "html"},
  },
})
if err != nil {
  log.Fatalf("クロールリクエストの送信に失敗しました: %v", err)
}

fmt.Println(crawlStatus) 
```

### クロールステータスの確認

クロールジョブのステータスを確認するには、`CheckCrawlStatus` メソッドを使用します。ジョブ ID を引数に取り、クロールジョブの現在のステータスを返します。

```
// クロールステータスを取得
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")

if err != nil {
  log.Fatalf("クロールステータスの取得に失敗しました: %v", err)
}

fmt.Println(crawlStatus)
```

### ウェブサイトをマップする

`MapUrl` を使って、ウェブサイト内の URL 一覧を生成します。`params` 引数で、サブドメインの除外やサイトマップの活用など、マッピング処理をカスタマイズできます。

```
// ウェブサイトをマッピングする
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
  log.Fatalf("URL のマッピングに失敗しました: %v", err)
}

fmt.Println(mapResult)
```

## エラー処理

SDK は Firecrawl API から返されるエラーを処理し、適切な例外をスローします。リクエスト中にエラーが発生した場合は、わかりやすいエラーメッセージ付きで例外がスローされます。

> Firecrawl API キーが必要な AI Agent ですか？自動オンボーディング手順については、[firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) を参照してください。