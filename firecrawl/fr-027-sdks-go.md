---
title: Go SDK | Firecrawl
url: https://docs.firecrawl.dev/fr/sdks/go
source: sitemap
fetched_at: 2026-03-23T07:23:28.663315-03:00
rendered_js: false
word_count: 269
summary: This document provides instructions for installing and using the Firecrawl Go SDK to scrape, crawl, and map websites. It covers client initialization, method usage for data extraction, and handling API responses.
tags:
    - go-sdk
    - web-scraping
    - web-crawling
    - api-integration
    - firecrawl
category: tutorial
---

## Installation

Pour installer le SDK Go de Firecrawl, vous pouvez utiliser go get:

```
go get github.com/mendableai/firecrawl-go
```

## Utilisation

1. Récupérez une clé API sur [firecrawl.dev](https://firecrawl.dev)
2. Passez la `API key` en paramètre à la struct `FirecrawlApp`.
3. Définissez l’`API URL` et/ou passez-la en paramètre à la struct `FirecrawlApp`. Par défaut : `https://api.firecrawl.dev`.
4. Définissez la `version` et/ou passez-la en paramètre à la struct `FirecrawlApp`. Par défaut : `v1`.

Voici un exemple d’utilisation du SDK avec gestion des erreurs :

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
	// Initialisez FirecrawlApp avec votre clé API
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"

	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("Échec de l’initialisation de FirecrawlApp : %v", err)
	}

  // Extraire le contenu d’un site web
  scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
    Formats: []string{"markdown", "html"},
  })
  if err != nil {
    log.Fatalf("Échec de l’envoi de la requête d’extraction : %v", err)
  }

  fmt.Println(scrapeStatus)

	// Explorer un site web
  idempotencyKey := uuid.New().String() // clé d’idempotence (optionnel)
  crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:     ptr(2),
	}

	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("Échec de l’envoi de la requête de crawl : %v", err)
	}

	fmt.Println(crawlStatus) 
}
```

Pour extraire une seule URL avec gestion des erreurs, utilisez la méthode `ScrapeURL`. Elle prend l’URL en paramètre et renvoie les données extraites sous forme de dictionnaire.

```
// Extraire un site web
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
  "formats": []string{"markdown", "html"},
})
if err != nil {
  log.Fatalf("Échec du scraping de l’URL : %v", err)
}

fmt.Println(scrapeResult)
```

### Explorer un site web

Pour explorer un site web, utilisez la méthode `CrawlUrl`. Elle prend l’URL de départ et des paramètres optionnels en arguments. Le paramètre `params` vous permet de définir des options supplémentaires pour la tâche d’exploration, comme le nombre maximal de pages à explorer, les domaines autorisés et le format de sortie.

```
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
  "limit": 100,
  "scrapeOptions": map[string]any{
    "formats": []string{"markdown", "html"},
  },
})
if err != nil {
  log.Fatalf("Échec de l’envoi de la requête de crawl : %v", err)
}

fmt.Println(crawlStatus) 
```

### Vérifier l’état d’un crawl

Pour consulter l’état d’un job de crawl, utilisez la méthode `CheckCrawlStatus`. Elle prend l’ID du job en paramètre et renvoie l’état actuel du crawl.

```
// Récupérer l’état du crawl
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")

if err != nil {
  log.Fatalf("Impossible de récupérer l’état du crawl : %v", err)
}

fmt.Println(crawlStatus)
```

### Cartographier un site web

Utilisez `MapUrl` pour générer une liste d’URL à partir d’un site web. L’argument `params` vous permet de personnaliser le processus de cartographie, avec notamment des options pour exclure les sous-domaines ou exploiter le sitemap.

```
// Cartographier un site web
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
  log.Fatalf("Impossible de cartographier l’URL : %v", err)
}

fmt.Println(mapResult)
```

## Gestion des erreurs

Le SDK gère les erreurs renvoyées par l’API Firecrawl et déclenche des exceptions appropriées. En cas d’erreur lors d’une requête, une exception est levée avec un message d’erreur explicite.

> Êtes-vous un agent d’IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.