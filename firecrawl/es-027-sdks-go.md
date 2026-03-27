---
title: Go SDK | Firecrawl
url: https://docs.firecrawl.dev/es/sdks/go
source: sitemap
fetched_at: 2026-03-23T07:25:04.801746-03:00
rendered_js: false
word_count: 281
summary: This document provides instructions on how to install and utilize the Firecrawl SDK for Go, covering setup, web scraping, crawling, and mapping functionality.
tags:
    - firecrawl
    - go-sdk
    - web-scraping
    - web-crawling
    - data-extraction
    - api-integration
category: tutorial
---

## Instalación

Para instalar el SDK de Firecrawl para Go, puedes usar go get:

```
go get github.com/mendableai/firecrawl-go
```

## Uso

1. Obtén una clave de API en [firecrawl.dev](https://firecrawl.dev)
2. Define la `API key` como parámetro en la estructura `FirecrawlApp`.
3. Define la `API URL` y/o pásala como parámetro a la estructura `FirecrawlApp`. De forma predeterminada es `https://api.firecrawl.dev`.
4. Define la `version` y/o pásala como parámetro a la estructura `FirecrawlApp`. De forma predeterminada es `v1`.

Aquí tienes un ejemplo de cómo usar el SDK con manejo de errores:

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
	// Inicializa FirecrawlApp con tu clave de API
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"

	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("Error al inicializar FirecrawlApp: %v", err)
	}

  // Realiza scraping de un sitio web
  scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
    Formats: []string{"markdown", "html"},
  })
  if err != nil {
    log.Fatalf("Error al enviar la solicitud de scraping: %v", err)
  }

  fmt.Println(scrapeStatus)

	// Realiza un rastreo (crawl) de un sitio web
  idempotencyKey := uuid.New().String() // clave de idempotencia opcional
  crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     ptr(2),
	}

	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("Error al enviar la solicitud de rastreo: %v", err)
	}

	fmt.Println(crawlStatus) 
}
```

Para extraer una única URL con manejo de errores, usa el método `ScrapeURL`. Recibe la URL como parámetro y devuelve los datos extraídos como un diccionario.

```
// Extraer datos de un sitio web
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
  "formats": []string{"markdown", "html"},
})
if err != nil {
  log.Fatalf("Error al extraer la URL: %v", err)
}

fmt.Println(scrapeResult)
```

### Rastreo de un sitio web

Para rastrear un sitio web, usa el método `CrawlUrl`. Recibe la URL inicial y parámetros opcionales como argumentos. El argumento `params` te permite especificar opciones adicionales para la tarea de rastreo, como el número máximo de páginas a rastrear, los dominios permitidos y el formato de salida.

```
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
  "limit": 100,
  "scrapeOptions": map[string]any{
    "formats": []string{"markdown", "html"},
  },
})
if err != nil {
  log.Fatalf("No se pudo enviar la solicitud de rastreo: %v", err)
}

fmt.Println(crawlStatus) 
```

### Comprobar el estado del rastreo

Para comprobar el estado de un trabajo de rastreo, usa el método `CheckCrawlStatus`. Recibe el ID del trabajo como parámetro y devuelve el estado actual del rastreo.

```
// Obtener el estado del rastreo
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")

if err != nil {
  log.Fatalf("Error al obtener el estado del rastreo: %v", err)
}

fmt.Println(crawlStatus)
```

### Mapear un sitio web

Usa `MapUrl` para generar una lista de URL de un sitio web. El argumento `params` te permite personalizar el proceso de mapeo, incluidas opciones para excluir subdominios o utilizar el sitemap.

```
// Mapear un sitio web
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
  log.Fatalf("No se pudo mapear la URL: %v", err)
}

fmt.Println(mapResult)
```

## Manejo de errores

El SDK gestiona los errores que devuelve la API de Firecrawl y lanza las excepciones correspondientes. Si se produce un error durante una solicitud, se lanzará una excepción con un mensaje descriptivo de error.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automática.