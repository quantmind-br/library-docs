---
title: Rust SDK | Firecrawl
url: https://docs.firecrawl.dev/fr/sdks/rust
source: sitemap
fetched_at: 2026-03-23T07:23:39.215492-03:00
rendered_js: false
word_count: 282
summary: This document provides a guide for integrating and using the Firecrawl SDK with Rust, covering installation, URL scraping, web crawling, and data extraction features.
tags:
    - rust-sdk
    - web-scraping
    - data-extraction
    - web-crawling
    - api-integration
    - firecrawl
category: guide
---

## Installation

Pour installer le SDK Rust Firecrawl, ajoutez ce qui suit à votre `Cargo.toml` :

```
# Ajoutez ceci à votre Cargo.toml
[dependencies]
firecrawl = "^1.0"
tokio = { version = "^1", features = ["full"] }
```

## Utilisation

Commencez par obtenir une clé API sur [firecrawl.dev](https://firecrawl.dev). Initialisez ensuite `FirecrawlApp`. Vous pourrez alors accéder à des fonctions comme `FirecrawlApp::scrape_url`, qui vous permettent d’utiliser notre API. Voici un exemple d’utilisation du SDK en Rust :

```
use firecrawl::{crawl::{CrawlOptions, CrawlScrapeOptions, CrawlScrapeFormats}, FirecrawlApp, scrape::{ScrapeOptions, ScrapeFormats}};

#[tokio::main]
async fn main() {
    // Initialiser FirecrawlApp avec la clé API
    let app = FirecrawlApp::new("fc-YOUR_API_KEY").expect("Échec de l’initialisation de FirecrawlApp");

    // Scraper une URL
    let options = ScrapeOptions {
        formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
        ..Default::default()
    };

    let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

    match scrape_result {
        Ok(data) => println!("Résultat du scraping :\n{}", data.markdown.unwrap()),
        Err(e) => eprintln!("Échec du mapping : {}", e),
    }

    // Crawler un site web
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
        Ok(data) => println!("Résultat du crawl ({} crédits utilisés) :\n{:#?}", data.credits_used, data.data),
        Err(e) => eprintln!("Échec du crawl : {}", e),
    }
}
```

### Scraper une URL

Pour scraper une seule URL, utilisez la méthode `scrape_url`. Elle prend l’URL en paramètre et renvoie les données scrappées sous forme de `Document`.

```
let options = ScrapeOptions {
    formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
    ..Default::default()
};

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
    Ok(data) => println!("Résultat du scraping :\n{}", data.markdown.unwrap()),
    Err(e) => eprintln!("Échec du scraping : {}", e),
}
```

Avec Extract, vous pouvez facilement extraire des données structurées à partir de n’importe quelle URL. Spécifiez votre schéma au format JSON Schema en utilisant la macro `serde_json::json!`.

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
            "description": "Top 5 actualités sur Hacker News"
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
    Ok(data) => println!("Résultat de l’extraction LLM :\n{:#?}", data.extract.unwrap()),
    Err(e) => eprintln!("Échec de l’extraction LLM : {}", e),
}
```

### Explorer un site web

Pour explorer un site web, utilisez la méthode `crawl_url`. L’appel attendra la fin de l’exploration, ce qui peut prendre du temps selon l’URL de départ et les options choisies.

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
    Ok(data) => println!("Résultat du crawl ({} crédits consommés) :\n{:#?}", data.credits_used, data.data),
    Err(e) => eprintln!("Échec du crawl : {}", e),
}
```

### Crawl du sitemap uniquement (API v2)

Le SDK Rust cible actuellement l’API v1. Pour utiliser `sitemap: "only"`, appelez directement l’endpoint v2 :

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

#### Exploration asynchrone

Pour lancer une exploration sans attendre le résultat, utilisez la méthode `crawl_url_async`. Elle accepte les mêmes paramètres, mais renvoie une structure `CrawlAsyncRespone` contenant l’ID de l’exploration. Vous pouvez utiliser cet ID avec la méthode `check_crawl_status` pour vérifier l’état à tout moment. Notez que les explorations terminées sont supprimées après 24 heures.

```
let crawl_id = app.crawl_url_async("https://mendable.ai", None).await?.id;

// ... later ...

let status = app.check_crawl_status(crawl_id).await?;

if status.status == CrawlStatusTypes::Completed {
    println!("L’exploration est terminée : {:#?}", status.data);
} else {
    // ... attendre encore un peu ...
}
```

### Cartographier une URL

Cartographier tous les liens associés à partir d’une URL de départ.

```
let map_result = app.map_url("https://firecrawl.dev", None).await;

match map_result {
    Ok(data) => println!("URLs cartographiées : {:#?}", data),
    Err(e) => eprintln!("Échec du mappage : {}", e),
}
```

## Gestion des erreurs

Le SDK gère les erreurs renvoyées par l’API Firecrawl et par nos dépendances, et les regroupe dans l’énumération `FirecrawlError`, qui implémente `Error`, `Debug` et `Display`. Toutes nos méthodes renvoient un `Result<T, FirecrawlError>`.

> Êtes-vous un agent IA qui a besoin d’une clé API pour Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour obtenir des instructions d’intégration automatisée.