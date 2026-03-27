---
title: Go SDK | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/sdks/go
source: sitemap
fetched_at: 2026-03-23T07:21:28.72592-03:00
rendered_js: false
word_count: 273
summary: This document provides instructions for installing and using the Firecrawl SDK for Go, covering how to perform web scraping, site crawling, URL mapping, and status checking.
tags:
    - go-sdk
    - web-scraping
    - web-crawling
    - firecrawl
    - api-integration
    - data-extraction
category: guide
---

## Instalação

Para instalar o SDK do Firecrawl para Go, use o go get:

```
go get github.com/mendableai/firecrawl-go
```

## Uso

1. Obtenha uma chave de API em [firecrawl.dev](https://firecrawl.dev)
2. Defina a `API key` como parâmetro na struct `FirecrawlApp`.
3. Defina a `API URL` e/ou passe-a como parâmetro na struct `FirecrawlApp`. O padrão é `https://api.firecrawl.dev`.
4. Defina a `version` e/ou passe-a como parâmetro na struct `FirecrawlApp`. O padrão é `v1`.

Veja um exemplo de como usar o SDK com tratamento de erros:

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
	// Inicialize o FirecrawlApp com sua chave de API
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"

	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("Falha ao inicializar o FirecrawlApp: %v", err)
	}

  // Faça o scraping de um site
  scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
    Formats: []string{"markdown", "html"},
  })
  if err != nil {
    log.Fatalf("Falha ao enviar a solicitação de scraping: %v", err)
  }

  fmt.Println(scrapeStatus)

	// Faça o crawling de um site
  idempotencyKey := uuid.New().String() // chave de idempotência opcional
  crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     ptr(2),
	}

	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("Falha ao enviar a solicitação de crawling: %v", err)
	}

	fmt.Println(crawlStatus) 
}
```

### Scraping de uma URL

Para extrair uma única URL com tratamento de erros, use o método `ScrapeURL`. Ele recebe a URL como parâmetro e retorna os dados extraídos como um dicionário.

```
// Raspar um site
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
  "formats": []string{"markdown", "html"},
})
if err != nil {
  log.Fatalf("Falha ao raspar a URL: %v", err)
}

fmt.Println(scrapeResult)
```

### Rastreamento de um site

Para rastrear um site, use o método `CrawlUrl`. Ele recebe a URL inicial e parâmetros opcionais. O parâmetro `params` permite especificar opções adicionais para a tarefa de rastreamento, como o número máximo de páginas a rastrear, domínios permitidos e o formato de saída.

```
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
  "limit": 100,
  "scrapeOptions": map[string]any{
    "formats": []string{"markdown", "html"},
  },
})
if err != nil {
  log.Fatalf("Falha ao enviar a solicitação de crawl: %v", err)
}

fmt.Println(crawlStatus) 
```

### Verificando o status do crawl

Para verificar o status de um job de crawl, use o método `CheckCrawlStatus`. Ele recebe o ID do job como parâmetro e retorna o status atual do job de crawl.

```
// Obter status do crawl
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")

if err != nil {
  log.Fatalf("Falha ao obter o status do crawl: %v", err)
}

fmt.Println(crawlStatus)
```

### Mapear um site

Use `MapUrl` para gerar uma lista de URLs de um site. O argumento `params` permite personalizar o processo de mapeamento, incluindo opções para excluir subdomínios ou usar o sitemap.

```
// Mapear um site
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
  log.Fatalf("Falha ao mapear a URL: %v", err)
}

fmt.Println(mapResult)
```

## Tratamento de erros

O SDK trata os erros retornados pela API do Firecrawl e lança as exceções apropriadas. Se ocorrer um erro durante uma requisição, uma exceção será lançada com uma mensagem de erro descritiva.

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de onboarding automatizado.