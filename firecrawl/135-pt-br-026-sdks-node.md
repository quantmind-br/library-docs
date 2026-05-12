---
title: Node SDK | Firecrawl
url: https://docs.firecrawl.dev/pt-BR/sdks/node
source: sitemap
fetched_at: 2026-03-23T07:21:16.898903-03:00
rendered_js: false
word_count: 643
summary: This document provides a comprehensive guide for using the Firecrawl Node.js SDK to perform web scraping, site crawling, data mapping, and remote browser session management.
tags:
    - firecrawl
    - node-js
    - web-scraping
    - web-crawling
    - sdk-integration
    - browser-automation
category: guide
---

## Instalação

Para instalar o SDK do Firecrawl para Node, você pode usar o npm:

```
# npm install @mendable/firecrawl-js

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-SUA-CHAVE-API" });
```

## Uso

1. Obtenha uma chave de API em [firecrawl.dev](https://firecrawl.dev)
2. Defina a chave de API como uma variável de ambiente chamada `FIRECRAWL_API_KEY` ou passe-a como parâmetro para a classe `FirecrawlApp`.

Veja um exemplo de como usar o SDK com tratamento de erros:

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

// Fazer scraping de um site
const scrapeResponse = await firecrawl.scrape('https://firecrawl.dev', {
  formats: ['markdown', 'html'],
});

console.log(scrapeResponse)

// Fazer crawling de um site
const crawlResponse = await firecrawl.crawl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
});

console.log(crawlResponse)
```

Para extrair dados de uma única URL com tratamento de erros, use o método `scrapeUrl`. Ele recebe a URL como parâmetro e retorna os dados coletados como um dicionário.

```
// Fazer scraping de um site:
const scrapeResult = await firecrawl.scrape('firecrawl.dev', { formats: ['markdown', 'html'] });

console.log(scrapeResult)
```

### Rastreamento de um site

Para rastrear um site com tratamento de erros, use o método `crawlUrl`. Ele recebe a URL inicial e parâmetros opcionais como argumentos. O parâmetro `params` permite especificar opções adicionais para a tarefa de rastreamento, como o número máximo de páginas a rastrear, domínios permitidos e o formato de saída. Veja [Pagination](#pagination) para paginação automática/manual e limites.

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 5, pollInterval: 1, timeout: 120 });
console.log(job.status);
```

### Rastreamento Somente do Sitemap

Use `sitemap: "only"` para rastrear apenas URLs do sitemap (a URL inicial sempre é incluída e a descoberta de links em HTML é ignorada).

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', {
  sitemap: 'only',
  limit: 25,
});
console.log(job.status, job.data.length);
```

### Iniciar um Crawl

Inicie um job sem esperar usando `startCrawl`. Ele retorna um `ID` de job que você pode usar para verificar o status. Use `crawl` quando quiser um “waiter” que bloqueia até a conclusão. Veja [Paginação](#pagination) para comportamento e limites de paginação.

```
const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
console.log(id);
```

### Verificando o status do rastreamento

Para verificar o status de um trabalho de rastreamento com tratamento de erros, use o método `checkCrawlStatus`. Ele recebe o `ID` como parâmetro e retorna o status atual do trabalho de rastreamento.

```
const status = await firecrawl.getCrawlStatus("<id-da-varredura>");
console.log(status);
```

### Cancelando um Crawl

Para cancelar um job de crawl, use o método `cancelCrawl`. Ele recebe o ID do job retornado por `startCrawl` como parâmetro e retorna o status do cancelamento.

```
const ok = await firecrawl.cancelCrawl("<crawl-id>");
console.log("Cancelado:", ok);
```

### Mapeando um site

Para mapear um site com tratamento de erros, use o método `mapUrl`. Ele recebe a URL inicial como parâmetro e retorna os dados mapeados como um dicionário.

```
const res = await firecrawl.map('https://firecrawl.dev', { limit: 10 });
console.log(res.links);
```

### Rastreando um site com WebSockets

Para rastrear um site com WebSockets, use o método `crawlUrlAndWatch`. Ele recebe a URL inicial e parâmetros opcionais como argumentos. O parâmetro `params` permite especificar opções adicionais para a tarefa de rastreamento, como o número máximo de páginas a rastrear, os domínios permitidos e o formato de saída.

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

// Inicie um crawl e depois acompanhe
const { id } = await firecrawl.startCrawl('https://mendable.ai', {
  excludePaths: ['blog/*'],
  limit: 5,
});

const watcher = firecrawl.watcher(id, { kind: 'crawl', pollInterval: 2, timeout: 120 });

watcher.on('document', (doc) => {
  console.log('DOC', doc);
});

watcher.on('error', (err) => {
  console.error('ERR', err?.error || err);
});

watcher.on('done', (state) => {
  console.log('DONE', state.status);
});

// Comece a acompanhar (WS com fallback em HTTP)
await watcher.start();
```

Os endpoints do Firecrawl para crawl e batch retornam uma URL `next` quando há mais dados disponíveis. O SDK de Node faz paginação automática por padrão e agrega todos os documentos; nesse caso, `next` será `null`. Você pode desativar a paginação automática ou definir limites.

#### Rastreamento

Use o método waiter `crawl` para a experiência mais simples, ou inicie um job e faça a paginação manualmente.

- Veja o fluxo padrão em [Rastrear um site](#crawling-a-website).

<!--THE END-->

- Inicie um job e, em seguida, recupere uma página por vez com `autoPaginate: false`.

```
const crawlStart = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 5 });
const crawlJobId = crawlStart.id;

const crawlSingle = await firecrawl.getCrawlStatus(crawlJobId, { autoPaginate: false });
console.log('rastreamento de página única:', crawlSingle.status, 'docs:', crawlSingle.data.length, 'próximo:', crawlSingle.next);
```

- Mantenha a paginação automática ativada, mas interrompa antecipadamente com `maxPages`, `maxResults` ou `maxWaitTime`.

```
const crawlLimited = await firecrawl.getCrawlStatus(crawlJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 50,
  maxWaitTime: 15,
});
console.log('crawl limitado:', crawlLimited.status, 'docs:', crawlLimited.data.length, 'próximo:', crawlLimited.next);
```

#### Coleta em lote

Use o método waiter `batchScrape` ou inicie uma tarefa e pagine manualmente.

- Veja o fluxo padrão em [Raspagem em lote](https://docs.firecrawl.dev/pt-BR/features/batch-scrape).

<!--THE END-->

- Inicie um job e, em seguida, recupere uma página por vez com `autoPaginate: false`.

```
const batchStart = await firecrawl.startBatchScrape([
  'https://docs.firecrawl.dev',
  'https://firecrawl.dev',
], { options: { formats: ['markdown'] } });
const batchJobId = batchStart.id;

const batchSingle = await firecrawl.getBatchScrapeStatus(batchJobId, { autoPaginate: false });
console.log('página única do lote:', batchSingle.status, 'docs:', batchSingle.data.length, 'próximo:', batchSingle.next);
```

- Mantenha a paginação automática ligada, mas interrompa antes com `maxPages`, `maxResults` ou `maxWaitTime`.

```
const batchLimited = await firecrawl.getBatchScrapeStatus(batchJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 100,
  maxWaitTime: 20,
});
console.log('lote limitado:', batchLimited.status, 'docs:', batchLimited.data.length, 'próximo:', batchLimited.next);
```

## Browser

Inicie sessões de navegador na nuvem e execute código remotamente.

### Criar sessão

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const session = await firecrawl.browser({ ttl: 600 });
console.log(session.id);          // ID da sessão
console.log(session.cdpUrl);      // wss://cdp-proxy.firecrawl.dev/cdp/...
console.log(session.liveViewUrl); // https://liveview.firecrawl.dev/...
```

### Executar código

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
});
console.log(result.result); // "Hacker News"
```

Execute JavaScript em vez de Python:

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
  language: "node",
});
```

Execute bash com o agent-browser:

```
const result = await firecrawl.browserExecute(session.id, {
  code: "agent-browser open https://example.com && agent-browser snapshot",
  language: "bash",
});
```

### Perfis

Salve e reutilize o estado do navegador (cookies, localStorage, etc.) entre sessões:

```
const session = await firecrawl.browser({
  ttl: 600,
  profile: {
    name: "my-profile",
    saveChanges: true,
  },
});
```

### Conectar via CDP

Para controle completo do Playwright, conecte-se diretamente usando a URL do CDP:

```
import { chromium } from "playwright";

const browser = await chromium.connectOverCDP(session.cdpUrl);
const context = browser.contexts()[0];
const page = context.pages()[0] || await context.newPage();

await page.goto("https://example.com");
console.log(await page.title());

await browser.close();
```

### Listar e Encerrar Sessões

```
// Listar sessões ativas
const { sessions } = await firecrawl.listBrowsers({ status: "active" });
for (const s of sessions) {
  console.log(s.id, s.status, s.createdAt);
}

// Fechar uma sessão
await firecrawl.deleteBrowser(session.id);
```

## Tratamento de erros

O SDK trata os erros retornados pela API do Firecrawl e lança as exceções apropriadas. Se ocorrer um erro durante uma solicitação, uma exceção será lançada com uma mensagem descritiva. Os exemplos acima mostram como lidar com esses erros usando blocos `try/catch`.

> Você é um agente de IA que precisa de uma chave de API do Firecrawl? Veja [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para instruções automatizadas de onboarding.