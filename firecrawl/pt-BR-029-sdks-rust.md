---
title: Rust SDK | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/sdks/rust
source: sitemap
fetched_at: 2026-03-23T07:21:27.221485-03:00
rendered_js: false
word_count: 282
summary: This document provides a comprehensive guide on installing and using the Firecrawl Rust SDK to perform web scraping, site crawling, data extraction, and URL mapping.
tags:
    - rust
    - firecrawl
    - web-scraping
    - api-integration
    - data-extraction
    - crawling
category: guide
---

## Instalação

Para instalar o SDK do Firecrawl para Rust, adicione o seguinte ao seu `Cargo.toml`:

```
# Adicione isto ao seu Cargo.toml
[dependencies]
firecrawl = "^1.0"
tokio = { version = "^1", features = ["full"] }
```

## Uso

Primeiro, obtenha uma chave de API em [firecrawl.dev](https://firecrawl.dev). Depois, inicialize o `FirecrawlApp`. A partir daí, você pode acessar funções como `FirecrawlApp::scrape_url`, que permitem usar nossa API. Veja um exemplo de como usar o SDK em Rust:

```
use firecrawl::{crawl::{CrawlOptions, CrawlScrapeOptions, CrawlScrapeFormats}, FirecrawlApp, scrape::{ScrapeOptions, ScrapeFormats}};

#[tokio::main]
async fn main() {
    // Inicialize o FirecrawlApp com a chave da API
    let app = FirecrawlApp::new("fc-YOUR_API_KEY").expect("Falha ao inicializar o FirecrawlApp");

    // Fazer scraping de uma URL
    let options = ScrapeOptions {
        formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
        ..Default::default()
    };

    let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

    match scrape_result {
        Ok(data) => println!("Resultado do scraping:\n{}", data.markdown.unwrap()),
        Err(e) => eprintln!("Falha no map: {}", e),
    }

    // Fazer crawling de um site
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
        Ok(data) => println!("Resultado do crawling (usou {} créditos):\n{:#?}", data.credits_used, data.data),
        Err(e) => eprintln!("Falha no crawling: {}", e),
    }
}
```

Para extrair dados de uma única URL, use o método `scrape_url`. Ele recebe a URL como parâmetro e retorna os dados extraídos como um `Document`.

```
let options = ScrapeOptions {
    formats vec! [ ScrapeFormats::Markdown, ScrapeFormats::HTML ].into(),
    ..Default::default()
};

let scrape_result = app.scrape_url("https://firecrawl.dev", options).await;

match scrape_result {
    Ok(data) => println!("Resultado da extração:\n{}", data.markdown.unwrap()),
    Err(e) => eprintln!("Falha na extração: {}", e),
}
```

Com o Extract, você pode extrair facilmente dados estruturados de qualquer URL. Especifique o seu esquema no formato JSON Schema, usando a macro `serde_json::json!`.

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
            "description": "Top 5 histórias do Hacker News"
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
    Ok(data) => println!("Resultado da extração via LLM:\n{:#?}", data.extract.unwrap()),
    Err(e) => eprintln!("Falha na extração via LLM: {}", e),
}
```

### Rastreamento de um site

Para rastrear um site, use o método `crawl_url`. Ele aguardará a conclusão do rastreamento, o que pode levar bastante tempo dependendo da URL inicial e das opções escolhidas.

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
    Ok(data) => println!("Resultado da varredura ({} créditos usados):\n{:#?}", data.credits_used, data.data),
    Err(e) => eprintln!("Falha na varredura: {}", e),
}
```

### Rastreamento apenas por sitemap (API v2)

O SDK de Rust atualmente oferece suporte à v1. Para usar `sitemap: "only"`, chame diretamente o endpoint da v2:

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

#### Rastreamento assíncrono

Para rastrear sem aguardar o resultado, use o método `crawl_url_async`. Ele recebe os mesmos parâmetros, mas retorna uma struct `CrawlAsyncRespone`, contendo o ID do rastreamento. Você pode usar esse ID com o método `check_crawl_status` para verificar o status a qualquer momento. Observe que rastreamentos concluídos são excluídos após 24 horas.

```
let crawl_id = app.crawl_url_async("https://mendable.ai", None).await?.id;

// ... mais tarde ...

let status = app.check_crawl_status(crawl_id).await?;

if status.status == CrawlStatusTypes::Completed {
    println!("Rastreamento concluído: {:#?}", status.data);
} else {
    // ... aguarde mais um pouco ...
}
```

### Mapear uma URL

Mapeie todos os links associados a partir de uma URL de origem.

```
let map_result = app.map_url("https://firecrawl.dev", None).await;

match map_result {
    Ok(data) => println!("URLs mapeadas: {:#?}", data),
    Err(e) => eprintln!("Falha ao mapear: {}", e),
}
```

## Tratamento de erros

O SDK trata os erros retornados pela API do Firecrawl e por nossas dependências, combinando-os no enum `FirecrawlError`, que implementa `Error`, `Debug` e `Display`. Todos os nossos métodos retornam um `Result<T, FirecrawlError>`.

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Veja [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções de onboarding automatizado.