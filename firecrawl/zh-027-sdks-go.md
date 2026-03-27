---
title: Go SDK | Firecrawl
url: https://docs.firecrawl.dev/zh/sdks/go
source: sitemap
fetched_at: 2026-03-23T07:20:11.526004-03:00
rendered_js: false
word_count: 79
summary: This document provides instructions on how to install and use the Firecrawl Go SDK to scrape, crawl, and map websites.
tags:
    - go-sdk
    - web-scraping
    - web-crawling
    - api-integration
    - data-extraction
category: tutorial
---

## 安装

要安装 Firecrawl 的 Go SDK，您可以使用 go get：

```
go get github.com/mendableai/firecrawl-go
```

## 使用

1. 从 [firecrawl.dev](https://firecrawl.dev) 获取 API 密钥。
2. 在 `FirecrawlApp` 结构体中将 `API key` 设置为参数。
3. 设置 `API URL`，并/或将其作为参数传递给 `FirecrawlApp` 结构体。默认值为 `https://api.firecrawl.dev`。
4. 设置 `version`，并/或将其作为参数传递给 `FirecrawlApp` 结构体。默认值为 `v1`。

下面是一个包含错误处理的 SDK 使用示例：

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
	// 使用你的 API 密钥初始化 FirecrawlApp
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"

	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("初始化 FirecrawlApp 失败：%v", err)
	}

  // 抓取网站
  scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
    Formats: []string{"markdown", "html"},
  })
  if err != nil {
    log.Fatalf("发送抓取请求失败：%v", err)
  }

  fmt.Println(scrapeStatus)

	// 爬取网站
  idempotencyKey := uuid.New().String() // 可选的幂等性键
  crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     ptr(2),
	}

	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("发送爬取请求失败：%v", err)
	}

	fmt.Println(crawlStatus) 
}
```

### 抓取单个 URL

要在包含错误处理的情况下抓取单个 URL，请使用 `ScrapeURL` 方法。该方法接收 URL 作为参数，并以字典形式返回抓取结果。

```
// 抓取网站
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
  "formats": []string{"markdown", "html"},
})
if err != nil {
  log.Fatalf("抓取 URL 失败：%v", err)
}

fmt.Println(scrapeResult)
```

### 爬取网站

要爬取网站，请使用 `CrawlUrl` 方法。该方法接受起始 URL 和可选参数。通过 `params` 参数，你可以为爬取任务设置其他选项，例如最大爬取页数、允许的域名以及输出 formats。

```
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
  "limit": 100,
  "scrapeOptions": map[string]any{
    "formats": []string{"markdown", "html"},
  },
})
if err != nil {
  log.Fatalf("发送爬取请求失败：%v", err)
}

fmt.Println(crawlStatus) 
```

### 检查爬取状态

要检查爬取作业的状态，请使用 `CheckCrawlStatus` 方法。该方法接受作业 ID 作为参数，并返回该爬取作业的当前状态。

```
// 获取抓取状态
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")

if err != nil {
  log.Fatalf("获取抓取状态失败：%v", err)
}

fmt.Println(crawlStatus)
```

### 映射网站

使用 `MapUrl` 从网站生成 URL 列表。你可以通过 `params` 参数自定义映射过程，包括排除子域名或使用站点地图等选项。

```
// 映射网站
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
  log.Fatalf("URL 映射失败：%v", err)
}

fmt.Println(mapResult)
```

## 错误处理

SDK 会处理 Firecrawl API 返回的错误并抛出相应异常。若请求过程中发生错误，将抛出包含详细错误信息的异常。

> 你是需要 Firecrawl API 密钥的 AI 代理吗？请参见 [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) 了解自动化入门说明。