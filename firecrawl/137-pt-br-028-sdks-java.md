---
title: SDK Java | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/sdks/java
source: sitemap
fetched_at: 2026-03-23T07:21:24.785067-03:00
rendered_js: false
word_count: 312
summary: This document provides a guide for integrating and using the Firecrawl Java SDK, covering installation via Maven or Gradle and detailing methods for web scraping, site crawling, data extraction, and AI agent interaction.
tags:
    - java
    - sdk
    - web-scraping
    - firecrawl
    - maven
    - gradle
    - data-extraction
category: guide
---

## Instalação

O SDK oficial para Java é mantido no monorepo do Firecrawl em [apps/java-sdk](https://github.com/firecrawl/firecrawl/tree/main/apps/java-sdk). Para instalar o SDK Java do Firecrawl, adicione a dependência do Maven Central:

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

1. Obtenha uma chave de API em [firecrawl.dev](https://firecrawl.dev)
2. Defina a chave de API como uma variável de ambiente chamada `FIRECRAWL_API_KEY` ou passe-a com `FirecrawlClient.builder().apiKey(...)`

Aqui está um exemplo rápido usando a superfície atual da API do SDK:

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

### Fazendo scraping de uma URL

Para fazer scraping de uma única URL, use o método `scrape`.

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

Extraia JSON estruturado com `JsonFormat` por meio do endpoint `scrape`:

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

### Rastreamento de um site

Para rastrear um site e aguardar sua conclusão, use `crawl`.

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

### Iniciar um Rastreamento

Inicie uma tarefa sem esperar usando `startCrawl`.

```
import com.firecrawl.models.CrawlOptions;
import com.firecrawl.models.CrawlResponse;

CrawlResponse start = client.startCrawl(
    "https://firecrawl.dev",
    CrawlOptions.builder().limit(100).build()
);

System.out.println("Job ID: " + start.getId());
```

### Verificando o status do rastreamento

Verifique o progresso do rastreamento com `getCrawlStatus`.

```
import com.firecrawl.models.CrawlJob;

CrawlJob status = client.getCrawlStatus(start.getId());
System.out.println("Status: " + status.getStatus());
System.out.println("Progress: " + status.getCompleted() + "/" + status.getTotal());
```

### Cancelando um Rastreamento

Cancele um rastreamento em execução com `cancelCrawl`.

```
import java.util.Map;

Map<String, Object> result = client.cancelCrawl(start.getId());
System.out.println(result);
```

### Mapear um site

Descubra links em um site com `map`.

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

### Buscando na Web

Faça uma busca com configurações de busca optional usando `search`.

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

### Scraping em batch

Faça o scraping de várias URLs em paralelo com `batchScrape`.

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

Execute um agente com IA usando `agent`.

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

Com um esquema JSON para saída estruturada:

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

### Uso & métricas

Verifique a concorrência e os créditos restantes:

```
import com.firecrawl.models.ConcurrencyCheck;
import com.firecrawl.models.CreditUsage;

ConcurrencyCheck concurrency = client.getConcurrency();
System.out.println("Concurrency: " + concurrency.getConcurrency() + "/" + concurrency.getMaxConcurrency());

CreditUsage credits = client.getCreditUsage();
System.out.println("Remaining credits: " + credits.getRemainingCredits());
```

## Suporte assíncrono

As variantes assíncronas já vêm integradas e retornam `CompletableFuture`.

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

O SDK Java inclui utilitários do Browser Sandbox.

### Criar uma sessão

```
import com.firecrawl.models.BrowserCreateResponse;

BrowserCreateResponse session = client.browser(120, 60, true);
System.out.println(session.getId());
System.out.println(session.getCdpUrl());
System.out.println(session.getLiveViewUrl());
```

### Executar código

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

### Listar & encerrar sessões

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

## Configuração

`FirecrawlClient.builder()` oferece suporte às seguintes opções:

OpçãoTipoPadrãoDescrição`apiKey``String`variável de ambiente `FIRECRAWL_API_KEY` ou propriedade do sistema `firecrawl.apiKey`Sua API key do Firecrawl`apiUrl``String``https://api.firecrawl.dev` (ou `FIRECRAWL_API_URL`)URL base da API`timeoutMs``long``300000`Tempo limite da requisição HTTP em ms`maxRetries``int``3`Tentativas automáticas para falhas transitórias`backoffFactor``double``0.5`Fator de backoff exponencial em segundos`asyncExecutor``Executor``ForkJoinPool.commonPool()`Executor personalizado para métodos assíncronos

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

## Tratamento de erros

O SDK lança exceções em tempo de execução em `com.firecrawl.errors`.

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

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Consulte [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obter instruções automatizadas de onboarding.