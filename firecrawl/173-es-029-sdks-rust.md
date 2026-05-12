---
title: Rust SDK | Firecrawl
url: https://docs.firecrawl.dev/es/sdks/rust
source: sitemap
fetched_at: 2026-03-23T07:25:05.491962-03:00
rendered_js: false
word_count: 288
summary: This document provides a comprehensive guide on integrating and using the Firecrawl Rust SDK to perform web scraping, site crawling, data extraction, and URL mapping.
tags:
    - rust
    - firecrawl
    - web-scraping
    - api-integration
    - data-extraction
    - crawling
category: guide
---

## Instalación

Para instalar el SDK de Rust de Firecrawl, agrega lo siguiente a tu `Cargo.toml`:

```
# Añade esto a tu Cargo.toml
[dependencies]
firecrawl = "^1.0"
tokio = { version = "^1", features = ["full"] }
```

## Uso

Primero, obtén una clave de API en [firecrawl.dev](https://firecrawl.dev). Luego, inicializa `FirecrawlApp`. A partir de ahí, puedes acceder a funciones como `FirecrawlApp::scrape_url`, que te permiten usar nuestra API. Aquí tienes un ejemplo de cómo usar el SDK en Rust:

```
use firecrawl::{crawl::{CrawlOptions, CrawlScrapeOptions, CrawlScrapeFormats}, FirecrawlApp, scrape::{ScrapeOptions, ScrapeFormats}};

#[tokio::main]
async fn main() {
    // Inicializa FirecrawlApp con la clave de API
    let app = FirecrawlApp::new("fc-YOUR_API_KEY").expect("Error al inicializar FirecrawlApp");

    // Realiza un scraping de una URL
    let options = ScrapeOptions {
        formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
        ..Default::default()
    };

    let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

    match scrape_result {
        Ok(data) => println!("Resultado del scraping:\n{}", data.markdown.unwrap()),
        Err(e) => eprintln!("Error en map: {}", e),
    }

    // Realiza un rastreo del sitio
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
        Ok(data) => println!("Resultado del rastreo (se usaron {} créditos):\n{:#?}", data.credits_used, data.data),
        Err(e) => eprintln!("Error en el rastreo: {}", e),
    }
}
```

Para extraer una única URL, utiliza el método `scrape_url`. Recibe la URL como parámetro y devuelve los datos extraídos como un `Document`.

```
let options = ScrapeOptions {
    formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
    ..Default::default()
};

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
    Ok(data) => println!("Resultado del scrape:\n{}", data.markdown.unwrap()),
    Err(e) => eprintln!("Error en el mapeo: {}", e),
}
```

Con Extract, puedes extraer fácilmente datos estructurados de cualquier URL. Debes definir tu esquema en formato JSON Schema, usando la macro `serde_json::json!`.

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
            "description": "Las 5 noticias principales de Hacker News"
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
    Ok(data) => println!("Resultado de la extracción con LLM:\n{:#?}", data.extract.unwrap()),
    Err(e) => eprintln!("La extracción con LLM falló: {}", e),
}
```

### Rastreo de un sitio web

Para rastrear un sitio web, utiliza el método `crawl_url`. Este método esperará a que el rastreo termine, lo que puede llevar bastante tiempo según la URL inicial y las opciones que elijas.

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
    Ok(data) => println!("Resultado del rastreo ({} créditos usados):\n{:#?}", data.credits_used, data.data),
    Err(e) => eprintln!("Error en el rastreo: {}", e),
}
```

### Rastreo solo mediante sitemap (API v2)

El SDK de Rust actualmente se dirige a v1. Para usar `sitemap: "only"`, llama directamente al endpoint de v2:

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

#### Rastreo asíncrono

Para rastrear sin esperar el resultado, usa el método `crawl_url_async`. Acepta los mismos parámetros, pero devuelve una estructura `CrawlAsyncResponse` que contiene el ID del rastreo. Puedes usar ese ID con el método `check_crawl_status` para consultar el estado en cualquier momento. Ten en cuenta que los rastreos completados se borran después de 24 horas.

```
let crawl_id = app.crawl_url_async("https://mendable.ai", None).await?.id;

// ... later ...

let status = app.check_crawl_status(crawl_id).await?;

if status.status == CrawlStatusTypes::Completed {
    println!("El rastreo ha finalizado: {:#?}", status.data);
} else {
    // ... espera un poco más ...
}
```

### Mapear una URL

Enumera todos los enlaces asociados a partir de una URL inicial.

```
let map_result = app.map_url("https://firecrawl.dev", None).await;

match map_result {
    Ok(data) => println!("URLs mapeadas: {:#?}", data),
    Err(e) => eprintln!("Error de mapeo: {}", e),
}
```

## Manejo de errores

El SDK gestiona los errores devueltos por la API de Firecrawl y por nuestras dependencias, y los unifica en el enum `FirecrawlError`, que implementa `Error`, `Debug` y `Display`. Todos nuestros métodos devuelven un `Result<T, FirecrawlError>`.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizadas.