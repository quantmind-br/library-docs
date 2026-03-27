---
title: SDK de Java | Firecrawl
url: https://docs.firecrawl.dev/es/sdks/java
source: sitemap
fetched_at: 2026-03-23T07:25:09.272604-03:00
rendered_js: false
word_count: 316
summary: This document provides a guide for installing and using the Firecrawl Java SDK to perform web scraping, crawling, site mapping, and AI-powered data extraction.
tags:
    - java
    - sdk
    - web-scraping
    - firecrawl
    - data-extraction
    - api-integration
category: guide
---

## Instalación

El SDK oficial de Java se mantiene en el monorepo de Firecrawl en [apps/java-sdk](https://github.com/firecrawl/firecrawl/tree/main/apps/java-sdk). Para instalar el SDK de Java de Firecrawl, agrega la dependencia desde Maven Central:

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

## Uso

1. Obtén una clave de API en [firecrawl.dev](https://firecrawl.dev)
2. Configura la clave de API como una variable de entorno llamada `FIRECRAWL_API_KEY`, o pásala con `FirecrawlClient.builder().apiKey(...)`

Aquí tienes un ejemplo rápido con la API actual del SDK:

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
        System.out.println("Páginas rastreadas: " + (crawl.getData() != null ? crawl.getData().size() : 0));
    }
}
```

### Scraping de una URL

Para hacer scraping de una sola URL, usa el método `scrape`.

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

Extrae JSON estructurado con `JsonFormat` mediante el endpoint `scrape`:

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

### Rastrear un sitio web

Para rastrear un sitio web y esperar a que finalice, usa `crawl`.

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

### Iniciar un rastreo

Inicia un trabajo de forma asíncrona con `startCrawl`.

```
import com.firecrawl.models.CrawlOptions;
import com.firecrawl.models.CrawlResponse;

CrawlResponse start = client.startCrawl(
    "https://firecrawl.dev",
    CrawlOptions.builder().limit(100).build()
);

System.out.println("Job ID: " + start.getId());
```

### Comprobar el estado del rastreo

Consulta el progreso del rastreo con `getCrawlStatus`.

```
import com.firecrawl.models.CrawlJob;

CrawlJob status = client.getCrawlStatus(start.getId());
System.out.println("Status: " + status.getStatus());
System.out.println("Progress: " + status.getCompleted() + "/" + status.getTotal());
```

### Cancelar un rastreo

Cancela un rastreo en ejecución con `cancelCrawl`.

```
import java.util.Map;

Map<String, Object> result = client.cancelCrawl(start.getId());
System.out.println(result);
```

### Mapeo de un sitio web

Descubre enlaces en un sitio web con `map`.

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

### Buscar en la Web

Busca con configuraciones de búsqueda optional usando `search`.

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

### Scraping por lotes

Haz scraping de varias URL en paralelo con `batchScrape`.

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

### Agente

Ejecuta un agente basado en IA con `agent`.

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

Con un esquema JSON para una salida estructurada:

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

### Uso y métricas

Consulta la concurrencia y los créditos restantes:

```
import com.firecrawl.models.ConcurrencyCheck;
import com.firecrawl.models.CreditUsage;

ConcurrencyCheck concurrency = client.getConcurrency();
System.out.println("Concurrency: " + concurrency.getConcurrency() + "/" + concurrency.getMaxConcurrency());

CreditUsage credits = client.getCreditUsage();
System.out.println("Remaining credits: " + credits.getRemainingCredits());
```

## Soporte asíncrono

Se incluyen variantes asíncronas que devuelven `CompletableFuture`.

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

## Navegador

El SDK de Java incluye utilidades de Browser Sandbox.

### Crear una sesión

```
import com.firecrawl.models.BrowserCreateResponse;

BrowserCreateResponse session = client.browser(120, 60, true);
System.out.println(session.getId());
System.out.println(session.getCdpUrl());
System.out.println(session.getLiveViewUrl());
```

### Ejecutar código

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

### Listar & cerrar sesiones

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

## Configuración

`FirecrawlClient.builder()` admite las siguientes opciones:

OpciónTipoPredeterminadoDescripción`apiKey``String`variable de entorno `FIRECRAWL_API_KEY` o propiedad del sistema `firecrawl.apiKey`Tu API key de Firecrawl`apiUrl``String``https://api.firecrawl.dev` (o `FIRECRAWL_API_URL`)URL base de la API`timeoutMs``long``300000`Tiempo de espera de la request HTTP en ms`maxRetries``int``3`Reintentos automáticos para fallos transitorios`backoffFactor``double``0.5`Factor de retroceso exponencial en segundos`asyncExecutor``Executor``ForkJoinPool.commonPool()`Ejecutor personalizado para métodos asíncronos

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

## Manejo de errores

El SDK lanza excepciones en tiempo de ejecución en `com.firecrawl.errors`.

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

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para ver las instrucciones de incorporación automática.