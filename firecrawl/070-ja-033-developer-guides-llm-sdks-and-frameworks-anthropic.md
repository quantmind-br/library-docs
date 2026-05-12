---
title: Anthropic - Firecrawl Docs
url: https://docs.firecrawl.dev/ja/developer-guides/llm-sdks-and-frameworks/anthropic
source: sitemap
fetched_at: 2026-03-23T07:35:22.026327-03:00
rendered_js: false
word_count: 221
summary: This document provides a guide on integrating Firecrawl with Claude to build AI applications capable of scraping web data, summarizing content, using tools for dynamic navigation, and extracting structured information.
tags:
    - firecrawl
    - claude
    - web-scraping
    - ai-integration
    - structured-data-extraction
    - tool-use
    - llm-applications
category: tutorial
---

Firecrawl を Claude と統合して、ウェブデータを活用する AI アプリケーションを構築しましょう。

## セットアップ

```
npm install @mendable/firecrawl-js @anthropic-ai/sdk zod zod-to-json-schema
```

「.env」ファイルを作成:

```
FIRECRAWL_API_KEY=your_firecrawl_key
ANTHROPIC_API_KEY=your_anthropic_key
```

> **注意:** Node &lt; 20 を使用している場合は、`dotenv` をインストールし、コードに `import 'dotenv/config'` を追加してください。

## スクレイプ + 要約

この例では、ウェブサイトをスクレイプし、その内容を Claude で要約するシンプルなワークフローを示します。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import Anthropic from '@anthropic-ai/sdk';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const scrapeResult = await firecrawl.scrape('https://firecrawl.dev', {
    formats: ['markdown']
});

console.log('Scraped content length:', scrapeResult.markdown?.length);

const message = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    messages: [
        { role: 'user', content: `Summarize in 100 words: ${scrapeResult.markdown}` }
    ]
});

console.log('Response:', message);
```

この例では、Claude のツール使用機能を使い、ユーザーからのリクエストに応じてモデル自身がいつウェブサイトをスクレイピングするかを判断するようにする方法を示します。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import { Anthropic } from '@anthropic-ai/sdk';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const firecrawl = new FirecrawlApp({
    apiKey: process.env.FIRECRAWL_API_KEY
});

const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY
});

const ScrapeArgsSchema = z.object({
    url: z.string()
});

console.log("Sending user message to Claude and requesting tool use if necessary...");
const response = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    tools: [{
        name: 'scrape_website',
        description: 'Scrape and extract markdown content from a website URL',
        input_schema: zodToJsonSchema(ScrapeArgsSchema, 'ScrapeArgsSchema') as any
    }],
    messages: [{
        role: 'user',
        content: 'What is Firecrawl? Check firecrawl.dev'
    }]
});

const toolUse = response.content.find(block => block.type === 'tool_use');

if (toolUse && toolUse.type === 'tool_use') {
    const input = toolUse.input as { url: string };
    console.log(`Calling tool: ${toolUse.name} | URL: ${input.url}`);

    const result = await firecrawl.scrape(input.url, {
        formats: ['markdown']
    });

    console.log(`スクレイピングしたコンテンツのプレビュー: ${result.markdown?.substring(0, 300)}...`);
    // Continue with the conversation or process the scraped content as needed
}
```

この例では、スクレイピングしたウェブサイトのコンテンツから構造化データを抽出するために Claude を利用する方法を示します。

```
import FirecrawlApp from '@mendable/firecrawl-js';
import Anthropic from '@anthropic-ai/sdk';
import { z } from 'zod';

const firecrawl = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });
const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const CompanyInfoSchema = z.object({
    name: z.string(),
    industry: z.string().optional(),
    description: z.string().optional()
});

const scrapeResult = await firecrawl.scrape('https://stripe.com', {
    formats: ['markdown'],
    onlyMainContent: true
});

const prompt = `このウェブサイトのコンテンツから企業情報を抽出してください。

この正確なフォーマットで有効なJSONのみを出力してください(マークダウンや説明は不要):

{
  "name": "企業名",
  "industry": "業種",
  "description": "一文での説明"
}

ウェブサイトのコンテンツ:
${scrapeResult.markdown}`;

const message = await anthropic.messages.create({
    model: 'claude-haiku-4-5',
    max_tokens: 1024,
    messages: [
        { role: 'user', content: prompt },
        { role: 'assistant', content: '{' }
    ]
});

const textBlock = message.content.find(block => block.type === 'text');

if (textBlock && textBlock.type === 'text') {
    const jsonText = '{' + textBlock.text;
    const companyInfo = CompanyInfoSchema.parse(JSON.parse(jsonText));

    console.log(companyInfo);
}
```

より多くの例については、[Claude のドキュメント](https://docs.anthropic.com/claude/docs)を参照してください。