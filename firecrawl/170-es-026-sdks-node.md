---
title: Node SDK | Firecrawl
url: https://docs.firecrawl.dev/es/sdks/node
source: sitemap
fetched_at: 2026-03-23T07:25:01.137104-03:00
rendered_js: false
word_count: 660
summary: This document provides a comprehensive guide for using the Firecrawl Node.js SDK to scrape, crawl, and map websites, as well as manage cloud-based browser sessions.
tags:
    - firecrawl
    - node-sdk
    - web-scraping
    - web-crawling
    - browser-automation
    - api-integration
category: guide
---

## Instalación

Para instalar el SDK de Firecrawl para Node, puedes usar npm:

```
# npm install @mendable/firecrawl-js

import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });
```

## Uso

1. Obtén una clave de API en [firecrawl.dev](https://firecrawl.dev)
2. Define la clave de API como una variable de entorno llamada `FIRECRAWL_API_KEY` o pásala como parámetro a la clase `FirecrawlApp`.

Aquí tienes un ejemplo de cómo usar el SDK con manejo de errores:

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

// Extraer datos de un sitio web
const scrapeResponse = await firecrawl.scrape('https://firecrawl.dev', {
  formats: ['markdown', 'html'],
});

console.log(scrapeResponse)

// Rastrear un sitio web
const crawlResponse = await firecrawl.crawl('https://firecrawl.dev', {
  limit: 100,
  scrapeOptions: {
    formats: ['markdown', 'html'],
  }
});

console.log(crawlResponse)
```

Para extraer una única URL con manejo de errores, usa el método `scrapeUrl`. Recibe la URL como parámetro y devuelve los datos extraídos como un diccionario.

```
// Extraer un sitio web:
const scrapeResult = await firecrawl.scrape('firecrawl.dev', { formats: ['markdown', 'html'] });

console.log(scrapeResult)
```

### Rastreo de un sitio web

Para rastrear un sitio web con manejo de errores, usa el método `crawlUrl`. Recibe la URL inicial y parámetros opcionales como argumentos. El argumento `params` te permite especificar opciones adicionales para la tarea de rastreo, como el número máximo de páginas a rastrear, los dominios permitidos y el formato de salida. Consulta [Paginación](#pagination) para la paginación automática o manual y la configuración de límites.

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', { limit: 5, pollInterval: 1, timeout: 120 });
console.log(job.status);
```

### Rastreo solo del sitemap

Usa `sitemap: "only"` para rastrear únicamente las URL del sitemap (la URL inicial siempre se incluye y se omite la detección de enlaces HTML).

```
const job = await firecrawl.crawl('https://docs.firecrawl.dev', {
  sitemap: 'only',
  limit: 25,
});
console.log(job.status, job.data.length);
```

### Iniciar un rastreo

Inicia un trabajo sin esperar usando `startCrawl`. Devuelve un `ID` de trabajo que puedes usar para comprobar el estado. Usa `crawl` cuando necesites un proceso bloqueante que espere hasta la finalización. Consulta [Paginación](#pagination) para el comportamiento y los límites de paginación.

```
const { id } = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 10 });
console.log(id);
```

### Verificar el estado del rastreo

Para verificar el estado de un trabajo de rastreo con manejo de errores, usa el método `checkCrawlStatus`. Recibe el `ID` como parámetro y devuelve el estado actual del trabajo de rastreo.

```
const estado = await firecrawl.getCrawlStatus("<id-de-rastreo>");
console.log(estado);
```

### Cancelar un rastreo

Para cancelar un trabajo de rastreo, usa el método `cancelCrawl`. Recibe como parámetro el ID del trabajo iniciado con `startCrawl` y devuelve el estado de la cancelación.

```
const ok = await firecrawl.cancelCrawl("<crawl-id>");
console.log("Cancelado:", ok);
```

### Mapear un sitio web

Para mapear un sitio web con manejo de errores, utiliza el método `mapUrl`. Recibe la URL inicial como parámetro y devuelve los datos del mapeo como un diccionario.

```
const res = await firecrawl.map('https://firecrawl.dev', { limit: 10 });
console.log(res.links);
```

### Rastreo de un sitio web con WebSockets

Para rastrear un sitio web con WebSockets, usa el método `crawlUrlAndWatch`. Recibe la URL inicial y parámetros opcionales como argumentos. El argumento `params` te permite especificar opciones adicionales para la tarea de rastreo, como el número máximo de páginas a rastrear, los dominios permitidos y el formato de salida.

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

// Inicia un rastreo y luego míralo
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

// Comienza a mirar (WS con alternativa HTTP)
await watcher.start();
```

Los puntos de conexión de Firecrawl para crawl y batch devuelven una URL `next` cuando hay más datos disponibles. El SDK de Node realiza la paginación automáticamente por defecto y agrega todos los documentos; en ese caso, `next` será `null`. Puedes desactivar la paginación automática o establecer límites.

#### Rastreo

Usa el método auxiliar `crawl` para la forma más sencilla, o inicia un job y pagina manualmente.

- Consulta el flujo por defecto en [Rastrear un sitio web](#crawling-a-website).

<!--THE END-->

- Inicia un trabajo y luego recupera una página a la vez con `autoPaginate: false`.

```
const crawlStart = await firecrawl.startCrawl('https://docs.firecrawl.dev', { limit: 5 });
const crawlJobId = crawlStart.id;

const crawlSingle = await firecrawl.getCrawlStatus(crawlJobId, { autoPaginate: false });
console.log('rastreo de una sola página:', crawlSingle.status, 'docs:', crawlSingle.data.length, 'siguiente:', crawlSingle.next);
```

- Mantén la paginación automática activada, pero deténla antes con `maxPages`, `maxResults` o `maxWaitTime`.

```
const crawlLimited = await firecrawl.getCrawlStatus(crawlJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 50,
  maxWaitTime: 15,
});
console.log('rastreo limitado:', crawlLimited.status, 'docs:', crawlLimited.data.length, 'siguiente:', crawlLimited.next);
```

#### Scrape por lotes

Usa el método waiter `batchScrape`, o inicia un job y pagina manualmente.

- Consulta el flujo predeterminado en [Raspado por lotes](https://docs.firecrawl.dev/es/features/batch-scrape).

<!--THE END-->

- Inicia un job y luego recupera una página a la vez con `autoPaginate: false`.

```
const batchStart = await firecrawl.startBatchScrape([
  'https://docs.firecrawl.dev',
  'https://firecrawl.dev',
], { options: { formats: ['markdown'] } });
const batchJobId = batchStart.id;

const batchSingle = await firecrawl.getBatchScrapeStatus(batchJobId, { autoPaginate: false });
console.log('lote, una sola página:', batchSingle.status, 'docs:', batchSingle.data.length, 'siguiente:', batchSingle.next);
```

- Mantén la paginación automática activada, pero deténla antes con `maxPages`, `maxResults` o `maxWaitTime`.

```
const batchLimited = await firecrawl.getBatchScrapeStatus(batchJobId, {
  autoPaginate: true,
  maxPages: 2,
  maxResults: 100,
  maxWaitTime: 20,
});
console.log('lote limitado:', batchLimited.status, 'docs:', batchLimited.data.length, 'siguiente:', batchLimited.next);
```

## Browser

Inicia sesiones de navegador en la nube y ejecuta código de forma remota.

### Crear una sesión

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const session = await firecrawl.browser({ ttl: 600 });
console.log(session.id);          // ID de sesión
console.log(session.cdpUrl);      // wss://cdp-proxy.firecrawl.dev/cdp/...
console.log(session.liveViewUrl); // https://liveview.firecrawl.dev/...
```

### Ejecutar código

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://news.ycombinator.com")\ntitle = await page.title()\nprint(title)',
});
console.log(result.result); // "Hacker News"
```

Ejecutar JavaScript en lugar de Python:

```
const result = await firecrawl.browserExecute(session.id, {
  code: 'await page.goto("https://example.com"); const t = await page.title(); console.log(t);',
  language: "node",
});
```

Ejecutar Bash con agent-browser:

```
const result = await firecrawl.browserExecute(session.id, {
  code: "agent-browser open https://example.com && agent-browser snapshot",
  language: "bash",
});
```

### Perfiles

Guarda y reutiliza el estado del navegador (cookies, localStorage, etc.) entre sesiones:

```
const session = await firecrawl.browser({
  ttl: 600,
  profile: {
    name: "my-profile",
    saveChanges: true,
  },
});
```

### Conectar mediante CDP

Para obtener control completo de Playwright, conecta directamente usando la URL de CDP:

```
import { chromium } from "playwright";

const browser = await chromium.connectOverCDP(session.cdpUrl);
const context = browser.contexts()[0];
const page = context.pages()[0] || await context.newPage();

await page.goto("https://example.com");
console.log(await page.title());

await browser.close();
```

### Listar y cerrar sesiones

```
// Listar sesiones activas
const { sessions } = await firecrawl.listBrowsers({ status: "active" });
for (const s of sessions) {
  console.log(s.id, s.status, s.createdAt);
}

// Cerrar una sesión
await firecrawl.deleteBrowser(session.id);
```

## Manejo de errores

El SDK gestiona los errores devueltos por la API de Firecrawl y arroja las excepciones correspondientes. Si se produce un error durante una solicitud, se generará una excepción con un mensaje descriptivo. Los ejemplos anteriores muestran cómo manejar estos errores con bloques `try/catch`.

> ¿Eres un agente de IA que necesita una clave de API de Firecrawl? Consulta [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) para obtener instrucciones de incorporación automatizada.