---
title: LlamaIndex - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/llm-sdks-and-frameworks/llamaindex
source: sitemap
fetched_at: 2026-03-23T07:35:04.300444-03:00
rendered_js: false
word_count: 124
summary: This document demonstrates how to build an AI application using Firecrawl for web data extraction integrated with LlamaIndex for RAG-based vector search.
tags:
    - firecrawl
    - llamaindex
    - rag
    - vector-search
    - web-crawling
    - embeddings
    - ai-development
category: tutorial
---

Webコンテンツを基にしたベクトル検索と埋め込みを用いて、FirecrawlをLlamaIndexと統合し、AIアプリケーションを構築します。

## セットアップ

```
npm install llamaindex @llamaindex/openai @mendable/firecrawl-js
```

「.env」ファイルを作成:

```
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **注意:** Node &lt; 20 を使用する場合は、`dotenv` をインストールし、コードに `import 'dotenv/config'` を追加してください。

## ベクター検索を用いたRAG

この例では、LlamaIndex と Firecrawl を組み合わせてウェブサイトをクロールし、埋め込みを作成し、RAG を用いてコンテンツにクエリを実行する方法を示します。

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

より多くの例については、[LlamaIndex のドキュメント](https://ts.llamaindex.ai/)を参照してください。