---
title: FIRE-1 AI 代理（测试版） | Firecrawl
url: https://docs.firecrawl.dev/zh/agents/fire-1
source: sitemap
fetched_at: 2026-03-23T07:34:19.99572-03:00
rendered_js: false
word_count: 44
summary: This document demonstrates how to use the Firecrawl JavaScript SDK to extract structured data from a website by providing a custom schema and prompt.
tags:
    - web-scraping
    - data-extraction
    - firecrawl-sdk
    - javascript
    - structured-data
    - api-integration
category: api
---

```
import FirecrawlApp, { ExtractResponse } from '@mendable/firecrawl-js';

const app = new FirecrawlApp({apiKey: "fc-YOUR_API_KEY"});

// 使用 schema 和提示词从网站提取：
const extractResult = await app.extract(['https://example-forum.com/topic/123'], {
  prompt: "提取此论坛线程中的所有用户评论。",
  schema: {
    type: "object",
    properties: {
      comments: {
        type: "array",
        items: {
          type: "object",
          properties: {
            author: {type: "string"},
            comment_text: {type: "string"}
          },
          required: ["author", "comment_text"]
        }
      }
    },
    required: ["comments"]
  },
  agent: {
    model: 'FIRE-1'
  }
}) as ExtractResponse;

if (!extractResult.success) {
  throw new Error(`提取失败：${extractResult.error}`)
}

console.log(extractResult)
```