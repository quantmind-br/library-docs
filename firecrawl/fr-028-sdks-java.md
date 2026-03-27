---
title: SDK Java | Firecrawl
url: https://docs.firecrawl.dev/fr/sdks/java
source: sitemap
fetched_at: 2026-03-23T07:23:23.776264-03:00
rendered_js: false
word_count: 322
summary: This document provides a comprehensive guide for installing and using the Firecrawl Java SDK to perform web scraping, crawling, site mapping, and AI-driven data extraction.
tags:
    - java-sdk
    - web-scraping
    - web-crawling
    - data-extraction
    - firecrawl
    - api-integration
category: tutorial
---

## Installation

Le SDK Java officiel est maintenu dans le monorepo Firecrawl sous [apps/java-sdk](https://github.com/firecrawl/firecrawl/tree/main/apps/java-sdk). Pour installer le SDK Java de Firecrawl, ajoutez la dépendance depuis Maven Central :

- Gradle (Kotlin DSL)
- Gradle (Groovy)
- Maven

```
repositories {
    mavenCentral()
}

dependencies {
    implementation("com.firecrawl:firecrawl-java:1.0.0")
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'com.firecrawl:firecrawl-java:1.0.0'
}

<dependency>
    <groupId>com.firecrawl</groupId>
    <artifactId>firecrawl-java</artifactId>
    <version>1.0.0</version>
</dependency>
```

## Utilisation

1. Obtenez une clé API sur [firecrawl.dev](https://firecrawl.dev)
2. Définissez la clé API dans une variable d’environnement nommée `FIRECRAWL_API_KEY`, ou passez-la avec `FirecrawlClient.builder().apiKey(...)`

Voici un exemple rapide utilisant l’API actuelle du SDK :

```
import com.firecrawl.client.FirecrawlClient;
import com.firecrawl.models.CrawlJob;
import com.firecrawl.models.CrawlOptions;
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;

public class Example {
    public static void main(String[] args) {
        FirecrawlClient client = FirecrawlClient.fromEnv();

        Document doc = client.scrape(
            "https://firecrawl.dev",
            ScrapeOptions.builder()
                .formats(List.of((Object) "markdown"))
                .build()
        );

        CrawlJob crawl = client.crawl(
            "https://firecrawl.dev",
            CrawlOptions.builder().limit(5).build()
        );

        System.out.println(doc.getMarkdown());
        System.out.println("Pages explorées : " + (crawl.getData() != null ? crawl.getData().size() : 0));
    }
}
```

### Scraping d’une URL

Pour scraper une seule URL, utilisez la méthode `scrape`.

```
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;

Document doc = client.scrape(
    "https://firecrawl.dev",
    ScrapeOptions.builder()
        .formats(List.of((Object) "markdown", "html"))
        .onlyMainContent(true)
        .waitFor(5000)
        .build()
);

System.out.println(doc.getMarkdown());
System.out.println(doc.getMetadata().get("title"));
```

Extrayez du JSON structuré avec `JsonFormat` via le point de terminaison `scrape` :

```
import com.firecrawl.models.Document;
import com.firecrawl.models.JsonFormat;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;
import java.util.Map;

JsonFormat jsonFmt = JsonFormat.builder()
    .prompt("Extract the product name and price")
    .schema(Map.of(
        "type", "object",
        "properties", Map.of(
            "name", Map.of("type", "string"),
            "price", Map.of("type", "number")
        )
    ))
    .build();

Document doc = client.scrape(
    "https://example.com/product",
    ScrapeOptions.builder()
        .formats(List.of((Object) jsonFmt))
        .build()
);

System.out.println(doc.getJson());
```

### Effectuer un crawl d’un site web

Pour effectuer un crawl d’un site web et attendre la fin de l’opération, utilisez `crawl`.

```
import com.firecrawl.models.CrawlJob;
import com.firecrawl.models.CrawlOptions;
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;

CrawlJob job = client.crawl(
    "https://firecrawl.dev",
    CrawlOptions.builder()
        .limit(50)
        .maxDiscoveryDepth(3)
        .scrapeOptions(
            ScrapeOptions.builder()
                .formats(List.of((Object) "markdown"))
                .build()
        )
        .build()
);

System.out.println("Status: " + job.getStatus());
System.out.println("Progress: " + job.getCompleted() + "/" + job.getTotal());

if (job.getData() != null) {
    for (Document page : job.getData()) {
        System.out.println(page.getMetadata().get("sourceURL"));
    }
}
```

### Démarrer un crawl

Démarrez une tâche sans attendre avec `startCrawl`.

```
import com.firecrawl.models.CrawlOptions;
import com.firecrawl.models.CrawlResponse;

CrawlResponse start = client.startCrawl(
    "https://firecrawl.dev",
    CrawlOptions.builder().limit(100).build()
);

System.out.println("Job ID: " + start.getId());
```

### Vérification de l’état d’un crawl

Vérifiez la progression du crawl avec `getCrawlStatus`.

```
import com.firecrawl.models.CrawlJob;

CrawlJob status = client.getCrawlStatus(start.getId());
System.out.println("Status: " + status.getStatus());
System.out.println("Progress: " + status.getCompleted() + "/" + status.getTotal());
```

### Annuler un crawl

Pour annuler un crawl en cours, utilisez `cancelCrawl`.

```
import java.util.Map;

Map<String, Object> result = client.cancelCrawl(start.getId());
System.out.println(result);
```

### Mapping d’un site web

Découvrez les liens d’un site à l’aide de `map`.

```
import com.firecrawl.models.MapData;
import com.firecrawl.models.MapOptions;
import java.util.Map;

MapData data = client.map(
    "https://firecrawl.dev",
    MapOptions.builder()
        .limit(100)
        .search("blog")
        .build()
);

if (data.getLinks() != null) {
    for (Map<String, Object> link : data.getLinks()) {
        System.out.println(link.get("url") + " - " + link.get("title"));
    }
}
```

### Recherche sur le web

Effectuez une recherche avec des paramètres facultatifs à l’aide de `search`.

```
import com.firecrawl.models.SearchData;
import com.firecrawl.models.SearchOptions;
import java.util.Map;

SearchData results = client.search(
    "firecrawl web scraping",
    SearchOptions.builder()
        .limit(10)
        .build()
);

if (results.getWeb() != null) {
    for (Map<String, Object> result : results.getWeb()) {
        System.out.println(result.get("title") + " - " + result.get("url"));
    }
}
```

### Batch Scraping

Scrapez plusieurs URL en parallèle avec `batchScrape`.

```
import com.firecrawl.models.BatchScrapeJob;
import com.firecrawl.models.BatchScrapeOptions;
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;

BatchScrapeJob job = client.batchScrape(
    List.of("https://firecrawl.dev", "https://firecrawl.dev/blog"),
    BatchScrapeOptions.builder()
        .options(
            ScrapeOptions.builder()
                .formats(List.of((Object) "markdown"))
                .build()
        )
        .build()
);

if (job.getData() != null) {
    for (Document doc : job.getData()) {
        System.out.println(doc.getMarkdown());
    }
}
```

### Agent

Exécutez un agent IA avec `agent`.

```
import com.firecrawl.models.AgentOptions;
import com.firecrawl.models.AgentStatusResponse;

AgentStatusResponse result = client.agent(
    AgentOptions.builder()
        .prompt("Find the pricing plans for Firecrawl and compare them")
        .build()
);

System.out.println(result.getData());
```

Avec un schéma JSON pour obtenir une sortie structurée :

```
import com.firecrawl.models.AgentOptions;
import com.firecrawl.models.AgentStatusResponse;
import java.util.List;
import java.util.Map;

AgentStatusResponse result = client.agent(
    AgentOptions.builder()
        .prompt("Extract pricing plan details")
        .urls(List.of("https://firecrawl.dev"))
        .schema(Map.of(
            "type", "object",
            "properties", Map.of(
                "plans", Map.of(
                    "type", "array",
                    "items", Map.of(
                        "type", "object",
                        "properties", Map.of(
                            "name", Map.of("type", "string"),
                            "price", Map.of("type", "string")
                        )
                    )
                )
            )
        ))
        .build()
);

System.out.println(result.getData());
```

### Utilisation & métriques

Vérifiez la concurrence et les crédits restants :

```
import com.firecrawl.models.ConcurrencyCheck;
import com.firecrawl.models.CreditUsage;

ConcurrencyCheck concurrency = client.getConcurrency();
System.out.println("Concurrency: " + concurrency.getConcurrency() + "/" + concurrency.getMaxConcurrency());

CreditUsage credits = client.getCreditUsage();
System.out.println("Remaining credits: " + credits.getRemainingCredits());
```

## Prise en charge de l’asynchrone

Des variantes asynchrones sont intégrées nativement et renvoient un `CompletableFuture`.

```
import com.firecrawl.models.Document;
import com.firecrawl.models.ScrapeOptions;
import java.util.List;
import java.util.concurrent.CompletableFuture;

CompletableFuture<Document> future = client.scrapeAsync(
    "https://example.com",
    ScrapeOptions.builder()
        .formats(List.of((Object) "markdown"))
        .build()
);

future.thenAccept(doc -> System.out.println(doc.getMarkdown()));
```

## Browser

Le SDK Java inclut des utilitaires pour Browser Sandbox.

### Créer une session

```
import com.firecrawl.models.BrowserCreateResponse;

BrowserCreateResponse session = client.browser(120, 60, true);
System.out.println(session.getId());
System.out.println(session.getCdpUrl());
System.out.println(session.getLiveViewUrl());
```

### Exécuter du code

```
import com.firecrawl.models.BrowserExecuteResponse;

BrowserExecuteResponse run = client.browserExecute(
    session.getId(),
    "await page.goto(\"https://example.com\"); console.log(await page.title());",
    "node",
    60
);

System.out.println(run.getStdout());
System.out.println(run.getExitCode());
```

### Lister & fermer les sessions

```
import com.firecrawl.models.BrowserDeleteResponse;
import com.firecrawl.models.BrowserListResponse;
import com.firecrawl.models.BrowserSession;

BrowserListResponse active = client.listBrowsers("active");
if (active.getSessions() != null) {
    for (BrowserSession s : active.getSessions()) {
        System.out.println(s.getId() + " - " + s.getStatus());
    }
}

BrowserDeleteResponse closed = client.deleteBrowser(session.getId());
System.out.println("Closed: " + closed.isSuccess());
```

## Configuration

`FirecrawlClient.builder()` prend en charge les options suivantes :

OptionTypePar défautDescription`apiKey``String`variable d’environnement `FIRECRAWL_API_KEY` ou propriété système `firecrawl.apiKey`Votre clé API Firecrawl`apiUrl``String``https://api.firecrawl.dev` (ou `FIRECRAWL_API_URL`)URL de base de l’API`timeoutMs``long``300000`Délai d’expiration de la requête HTTP en ms`maxRetries``int``3`Nouvelles tentatives automatiques en cas d’échecs temporaires`backoffFactor``double``0.5`Facteur de backoff exponentiel en secondes`asyncExecutor``Executor``ForkJoinPool.commonPool()`Exécuteur personnalisé pour les méthodes asynchrones

```
import com.firecrawl.client.FirecrawlClient;

FirecrawlClient client = FirecrawlClient.builder()
    .apiKey("fc-your-api-key")
    .apiUrl("https://api.firecrawl.dev")
    .timeoutMs(300_000)
    .maxRetries(3)
    .backoffFactor(0.5)
    .build();
```

## Gestion des erreurs

Le SDK lève des exceptions d’exécution dans `com.firecrawl.errors`.

```
import com.firecrawl.errors.AuthenticationException;
import com.firecrawl.errors.FirecrawlException;
import com.firecrawl.errors.JobTimeoutException;
import com.firecrawl.errors.RateLimitException;
import com.firecrawl.models.Document;

try {
    Document doc = client.scrape("https://example.com");
} catch (AuthenticationException e) {
    System.err.println("Auth failed: " + e.getMessage());
} catch (RateLimitException e) {
    System.err.println("Rate limited: " + e.getMessage());
} catch (JobTimeoutException e) {
    System.err.println("Job " + e.getJobId() + " timed out after " + e.getTimeoutSeconds() + "s");
} catch (FirecrawlException e) {
    System.err.println("Error " + e.getStatusCode() + ": " + e.getMessage());
}
```

> Êtes-vous un agent IA ayant besoin d’une clé API Firecrawl ? Consultez [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) pour les instructions d’intégration automatisée.