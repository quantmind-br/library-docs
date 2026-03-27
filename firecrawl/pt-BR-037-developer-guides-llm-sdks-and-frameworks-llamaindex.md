---
title: LlamaIndex - Firecrawl Docs
url: https://docs.firecrawl.dev/pt-BR/developer-guides/llm-sdks-and-frameworks/llamaindex
source: sitemap
fetched_at: 2026-03-23T07:34:41.032353-03:00
rendered_js: false
word_count: 175
summary: This document provides a guide on integrating Firecrawl with LlamaIndex to crawl web content and perform retrieval-augmented generation using vector search.
tags:
    - web-scraping
    - llamaindex
    - rag
    - vector-embeddings
    - ai-development
    - data-ingestion
category: guide
---

Integre o Firecrawl ao LlamaIndex para criar aplicações de IA com busca vetorial e embeddings baseados em conteúdo da web.

## Configuração

```
npm install llamaindex @llamaindex/openai @mendable/firecrawl-js
```

Crie o arquivo `.env`:

```
FIRECRAWL_API_KEY=sua_chave_firecrawl
OPENAI_API_KEY=sua_chave_openai
```

> **Observação:** Se estiver usando Node &lt; 20, instale `dotenv` e adicione `import 'dotenv/config'` ao seu código.

Este exemplo demonstra como usar LlamaIndex com Firecrawl para rastrear um site, criar embeddings e consultar o conteúdo por meio de RAG.

```
import Firecrawl from '@mendable/firecrawl-js';
import { Document, VectorStoreIndex, Settings } from 'llamaindex';
import { OpenAI, OpenAIEmbedding } from '@llamaindex/openai';

Settings.llm = new OpenAI({ model: "gpt-4o" });
Settings.embedModel = new OpenAIEmbedding({ model: "text-embedding-3-small" });

const firecrawl = new Firecrawl({ apiKey: process.env.FIRECRAWL_API_KEY });
const crawlResult = await firecrawl.crawl('https://firecrawl.dev', {
  limit: 10,
  scrapeOptions: { formats: ['markdown'] }
});
console.log(`Crawled ${crawlResult.data.length } pages`);

const documents = crawlResult.data.map((page: any, i: number) =>
  new Document({
    text: page.markdown,
    id_: `page-${i}`,
    metadata: { url: page.metadata?.sourceURL }
  })
);

const index = await VectorStoreIndex.fromDocuments(documents);
console.log('Vector index created with embeddings');

const queryEngine = index.asQueryEngine();
const response = await queryEngine.query({ query: 'What is Firecrawl and how does it work?' });

console.log('\nAnswer:', response.toString());
```

Para mais exemplos, consulte a [documentação do LlamaIndex](https://ts.llamaindex.ai/).