---
title: Vercel AI SDK - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/llm-sdks-and-frameworks/vercel-ai-sdk
source: sitemap
fetched_at: 2026-03-23T07:31:06.933705-03:00
rendered_js: false
word_count: 189
summary: This document provides a technical guide for integrating Firecrawl tools with the Vercel AI SDK to perform web scraping, searching, browsing, and data extraction within AI-driven applications.
tags:
    - firecrawl
    - vercel-ai-sdk
    - web-scraping
    - ai-agents
    - data-extraction
    - automation
    - typescript
category: guide
---

Ferramentas Firecrawl para o Vercel AI SDK. Faça scraping, busque, navegue e extraia dados da web em suas aplicações de IA.

## Instalação

```
npm install firecrawl-aisdk ai
```

Configure as variáveis de ambiente:

```
FIRECRAWL_API_KEY=fc-your-key       # https://firecrawl.dev
AI_GATEWAY_API_KEY=your-key         # https://vercel.com/ai-gateway
```

## Início rápido

A forma mais fácil de começar. `FirecrawlTools()` fornece ferramentas de busca, scraping e navegador com um prompt de sistema gerado automaticamente que orienta o modelo na escolha das ferramentas.

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

Com opções personalizadas:

```
const tools = FirecrawlTools({
  apiKey: 'fc-custom-key',                // opcional, usa variável de ambiente por padrão
  search: { limit: 3, country: 'US' },    // opções padrão de busca
  scrape: { onlyMainContent: true },       // opções padrão de scrape
  browser: {},                             // habilitar ferramenta de navegador
});
```

Desative qualquer ferramenta passando `false`:

```
const tools = FirecrawlTools({
  browser: false,   // somente search + scrape
});
```

Cada ferramenta é **de uso duplo** – você pode usá-la diretamente como ferramenta (lê `FIRECRAWL_API_KEY` das variáveis de ambiente) ou chamá-la como uma factory para configuração personalizada:

```
import { scrape, search } from 'firecrawl-aisdk';

// Use diretamente - lê FIRECRAWL_API_KEY do env
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape, search },
  prompt: '...',
});

// Ou chame como factory para configuração personalizada
const customScrape = scrape({ apiKey: 'fc-custom-key' });
const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { scrape: customScrape },
  prompt: '...',
});
```

### Scrape

```
import { generateText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Faça scraping de https://firecrawl.dev e resuma o que ele faz',
  tools: { scrape },
});
```

### Pesquisa

```
import { generateText } from 'ai';
import { search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Pesquise sobre Firecrawl e resuma o que encontrar',
  tools: { search },
});
```

### Busca + Raspagem

```
import { generateText } from 'ai';
import { search, scrape } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Busque por Firecrawl, faça scrape do primeiro resultado e explique o que ele faz',
  tools: { search, scrape },
});
```

### Mapeamento

```
import { generateText } from 'ai';
import { map } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Map https://docs.firecrawl.dev and list the main sections',
  tools: { map },
});
```

### Streaming

```
import { streamText } from 'ai';
import { scrape } from 'firecrawl-aisdk';

const result = streamText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Faça scraping de https://firecrawl.dev e explique o que ele faz',
  tools: { scrape },
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

## Browser

A ferramenta de navegador cria automaticamente uma sessão em nuvem no primeiro uso e realiza a limpeza ao encerrar o processo:

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

Para obter uma URL de visualização em tempo real (para acompanhar o navegador ao vivo) ou controlar manualmente o ciclo de vida da sessão:

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

### Navegador + Busca

```
import { generateText, stepCountIs } from 'ai';
import { browser, search } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  tools: { browser: browser(), search },
  stopWhen: stepCountIs(25),
  prompt: 'Busque o principal artigo de IA desta semana, navegue nele e resuma as principais descobertas.',
});
```

Crawl, batch scrape, extract e agent retornam um ID de job. Use-os com `poll` para obter os resultados:

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

### Batch Scrape

```
import { generateText } from 'ai';
import { batchScrape, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Scrape https://firecrawl.dev and https://docs.firecrawl.dev, then compare',
  tools: { batchScrape, poll },
});
```

### Agent

Coleta autônoma de dados na web - pesquisa, navega e extrai dados por conta própria.

```
import { generateText, stepCountIs } from 'ai';
import { agent, poll } from 'firecrawl-aisdk';

const { text } = await generateText({
  model: 'anthropic/claude-sonnet-4.5',
  prompt: 'Find the founders of Firecrawl, their roles, and their backgrounds',
  tools: { agent, poll },
  stopWhen: stepCountIs(10),
});
```

## Todas as exportações

```
import {
  // Ferramentas de uso duplo (use diretamente ou chame como factory)
  scrape,             // Faz scrape de uma única URL
  search,             // Pesquisa na web
  map,                // Descobre URLs em um site
  crawl,              // Faz crawl de múltiplas páginas (async)
  batchScrape,        // Faz scrape de múltiplas URLs (async)
  agent,              // Agente web autônomo (async)
  extract,            // Extrai dados estruturados (async)

  // Gerenciamento de jobs
  poll,               // Consulta jobs assíncronos por resultados
  status,             // Verifica o status do job
  cancel,             // Cancela jobs em execução

  // Browser (somente factory)
  browser,            // browser({ firecrawlApiKey: '...' })

  // Pacote tudo-em-um
  FirecrawlTools,     // FirecrawlTools({ apiKey, search, scrape, browser })

  // Utilitários
  stepLogger,         // Estatísticas de tokens por chamada de ferramenta
  logStep,            // Log simples em uma linha
} from 'firecrawl-aisdk';
```