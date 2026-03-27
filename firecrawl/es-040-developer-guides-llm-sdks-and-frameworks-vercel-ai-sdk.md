---
title: Vercel AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/es/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk
source: sitemap
fetched_at: 2026-03-23T07:31:23.791339-03:00
rendered_js: false
word_count: 188
summary: This document provides a guide for integrating Firecrawl tools with the Vercel AI SDK to perform autonomous web scraping, search, mapping, and browsing operations within AI applications.
tags:
    - firecrawl
    - vercel-ai-sdk
    - web-scraping
    - ai-agents
    - javascript
    - data-extraction
category: guide
---

Herramientas de Firecrawl para Vercel AI SDK. Web scraping, búsqueda, navegación y extracción de datos para aplicaciones de IA.

## Instalación

```
npm install firecrawl-aisdk ai
```

Configura las variables de entorno:

```
FIRECRAWL_API_KEY=fc-your-key       # https://firecrawl.dev
AI_GATEWAY_API_KEY=your-key         # https://vercel.com/ai-gateway
```

## Inicio rápido

La manera más sencilla de comenzar. `FirecrawlTools()` te proporciona herramientas de búsqueda, scraping y navegador con un prompt de sistema autogenerado que guía al modelo en la selección de herramientas.

```
import { generateText, stepCountIs } from 'ai';
import { FirecrawlTools } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Search for Firecrawl, scrape the top result, and summarize what it does',
  tools: FirecrawlTools(),
  stopWhen: stepCountIs(5),
});
```

Con opciones personalizadas:

```
const tools = FirecrawlTools({
  apiKey: 'fc-custom-key',                // opcional, usa la variable de entorno por defecto
  search: { limit: 3, country: 'US' },    // opciones de búsqueda predeterminadas
  scrape: { onlyMainContent: true },       // opciones de scraping predeterminadas
  browser: {},                             // habilitar herramienta de navegador
});
```

Deshabilita cualquier herramienta pasando `false`:

```
const tools = FirecrawlTools({
  browser: false,   // solo búsqueda + scraping
});
```

Cada herramienta es de **doble propósito**: puedes usarla directamente como herramienta (lee `FIRECRAWL_API_KEY` de las variables de entorno) o utilizarla como fábrica para una configuración personalizada:

```
import { scrape, search } from 'firecrawl-aisdk';

// Usar directamente - lee FIRECRAWL_API_KEY del entorno
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape, search },
  prompt: '...',
});

// O llamar como factory para configuración personalizada
const customScrape = scrape({ apiKey: 'fc-custom-key' });
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape: customScrape },
  prompt: '...',
});

import { generateText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Extrae datos de https://firecrawl.dev y resume lo que hace',
  tools: { scrape },
});
```

### Búsqueda

```
import { generateText } from 'ai';
import { search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Busca información sobre Firecrawl y resume lo que encuentres',
  tools: { search },
});
```

### Búsqueda + Scraping

```
import { generateText } from 'ai';
import { search, scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Busca Firecrawl, extrae el resultado principal y explica qué hace',
  tools: { search, scrape },
});
```

### Mapeo

```
import { generateText } from 'ai';
import { map } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Mapea https://docs.firecrawl.dev y lista las secciones principales',
  tools: { map },
});
```

### Streaming

```
import { streamText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const result = streamText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Extrae https://firecrawl.dev y explica qué hace',
  tools: { scrape },
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

## Navegador

La herramienta del navegador crea automáticamente una sesión en la nube en su primer uso y la elimina al finalizar el proceso:

```
import { generateText, stepCountIs } from 'ai';
import { browser } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser() },
  stopWhen: stepCountIs(25),
  prompt: 'Go to https://news.ycombinator.com and get the top 3 stories.',
});
```

Para obtener una URL de visualización en tiempo real (para observar el navegador en tiempo real) o controlar manualmente el ciclo de vida de la sesión:

```
const browserTool = browser();
console.log('Live view:', await browserTool.start());

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browserTool },
  stopWhen: stepCountIs(25),
  prompt: 'Go to https://news.ycombinator.com and get the top 3 stories.',
});

await browserTool.close();
```

### Navegador + Búsqueda

```
import { generateText, stepCountIs } from 'ai';
import { browser, search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser(), search },
  stopWhen: stepCountIs(25),
  prompt: 'Search for the top AI paper this week, browse it, and summarize the key findings.',
});
```

Crawl, batch scrape, extract y agent devuelven un ID de trabajo. Combínalos con `poll` para obtener los resultados:

### Crawl

```
import { generateText } from 'ai';
import { crawl, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Crawl https://docs.firecrawl.dev (limit 3 pages) and summarize',
  tools: { crawl, poll },
});
```

### Rastreo por lotes

```
import { generateText } from 'ai';
import { batchScrape, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Scrape https://firecrawl.dev and https://docs.firecrawl.dev, then compare',
  tools: { batchScrape, poll },
});
```

### Agente

Recopilación autónoma de datos web: busca, navega y extrae datos de forma autónoma.

```
import { generateText, stepCountIs } from 'ai';
import { agent, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Encuentra los fundadores de Firecrawl, sus roles y sus trayectorias',
  tools: { agent, poll },
  stopWhen: stepCountIs(10),
});
```

## Todas las exportaciones

```
import {
  // Herramientas de doble propósito (usar directamente o llamar como factory)
  scrape,             // Extrae una sola URL
  search,             // Busca en la web
  map,                // Descubre URLs en un sitio
  crawl,              // Rastrea múltiples páginas (async)
  batchScrape,        // Extrae múltiples URLs (async)
  agent,              // Agente web autónomo (async)
  extract,            // Extrae datos estructurados (async)

  // Gestión de trabajos
  poll,               // Consulta trabajos async para obtener resultados
  status,             // Verifica el estado del trabajo
  cancel,             // Cancela trabajos en ejecución

  // Navegador (solo factory)
  browser,            // browser({ firecrawlApiKey: '...' })

  // Paquete todo en uno
  FirecrawlTools,     // FirecrawlTools({ apiKey, search, scrape, browser })

  // Utilidades
  stepLogger,         // Estadísticas de tokens por llamada a herramienta
  logStep,            // Registro simple en una línea
} from 'firecrawl-aisdk';
```