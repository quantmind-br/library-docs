---
title: Gemini - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/llm-sdks-and-frameworks/gemini
source: sitemap
fetched_at: 2026-03-23T07:35:16.484522-03:00
rendered_js: false
word_count: 192
summary: This document provides a technical guide on integrating Firecrawl for web scraping with Google Gemini to enable summarization, multi-turn analysis, and structured data extraction.
tags:
    - firecrawl
    - gemini
    - web-scraping
    - ai-integration
    - structured-data
    - data-extraction
category: tutorial
---

Web データを活用する AI アプリケーション向けに、Firecrawl を Google の Gemini と統合します。

## セットアップ

```
npm install @mendable/firecrawl-js @google/genai
```

「.env」ファイルを作成:

```
FIRECRAWL_API_KEY=your_firecrawl_key
GEMINI_API_KEY=your_gemini_key
```

> **注意:** Node &lt; 20 を使用している場合は、`dotenv` をインストールし、コードに `import 'dotenv/config'` を追加してください。

## スクレイピング + 要約

この例では、ウェブサイトをスクレイピングし、そのコンテンツを Gemini で要約するというシンプルなワークフローを紹介します。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: `Summarize: ${scrapeResult.markdown}`,
});

console.log('Summary:', response.text);
```

## コンテンツ分析

この例では、Gemini のマルチターン会話機能を使ってウェブサイトのコンテンツを分析する方法を示します。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://news.ycombinator.com/', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const chat = ai.chats.create({
    model: 'gemini-2.5-flash'
});

// Hacker Newsのトップ3の記事を取得
const result1 = await chat.sendMessage({
    message: `Based on this website content from Hacker News, what are the top 3 stories right now?\n\n${scrapeResult.markdown}`
});
console.log('Top 3 Stories:', result1.text);

// Hacker Newsの4番目と5番目の記事を取得
const result2 = await chat.sendMessage({
    message: `Now, what are the 4th and 5th top stories on Hacker News from the same content?`
});
console.log('4th and 5th Stories:', result2.text);
```

この例では、スクレイピングしたウェブサイトのコンテンツから、Gemini の JSONモード を使って構造化データを抽出する方法を示します。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { GoogleGenAI, Type } from '@google/genai';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: `Extract company information: ${scrapeResult.markdown}`,
    config: {
        responseMimeType: 'application/json',
        responseSchema: {
            type: Type.OBJECT,
            properties: {
                name: { type: Type.STRING },
                industry: { type: Type.STRING },
                description: { type: Type.STRING },
                products: {
                    type: Type.ARRAY,
                    items: { type: Type.STRING }
                }
            },
            propertyOrdering: ['name', 'industry', 'description', 'products']
        }
    }
});

console.log('Extracted company info:', response?.text);
```

より多くの例については、[Gemini のドキュメント](https://ai.google.dev/docs)を参照してください。