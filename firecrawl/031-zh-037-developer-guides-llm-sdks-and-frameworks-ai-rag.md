---
title: LlamaIndex - Firecrawl Docs
url: https://docs.firecrawl.dev/zh/developer-guides/llm-sdks-and-frameworks/llamaindex
source: sitemap
fetched_at: 2026-03-23T07:34:05.943474-03:00
rendered_js: false
word_count: 133
summary: This document provides a guide on integrating Firecrawl with LlamaIndex to perform web crawling and implement Retrieval-Augmented Generation (RAG) using vector search.
tags:
    - web-scraping
    - vector-search
    - rag
    - llamaindex
    - firecrawl
    - data-ingestion
category: tutorial
---

将 Firecrawl 与 LlamaIndex 集成，基于网页内容的向量搜索与嵌入来构建 AI 应用。

## 配置

```
npm install llamaindex @llamaindex/openai @mendable/firecrawl-js
```

创建“.env”文件：

```
FIRECRAWL_API_KEY=your_firecrawl_key
OPENAI_API_KEY=your_openai_key
```

> **注意：** 如果使用 Node 版本低于 20，请安装 `dotenv`，并在代码中添加 `import 'dotenv/config'`。

## 使用向量搜索实现 RAG

此示例演示如何将 LlamaIndex 与 Firecrawl 结合使用来爬取网站、创建嵌入向量，并通过 RAG 查询内容。

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

更多示例请参见 [LlamaIndex 文档](https://ts.llamaindex.ai/)。