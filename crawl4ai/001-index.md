---
title: Home - Crawl4AI Documentation (v0.7.x)
url: https://docs.crawl4ai.com/
source: sitemap
fetched_at: 2026-01-22T22:21:46.364038901-03:00
rendered_js: false
word_count: 628
summary: This document introduces Crawl4AI, an open-source web crawler and scraper designed to extract and process web content into clean, LLM-friendly formats for RAG pipelines and AI agents.
tags:
    - crawl4ai
    - web-crawling
    - web-scraping
    - llm-friendly
    - open-source
    - data-extraction
    - python-library
category: guide
---

## 🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper

* * *

#### 🚀 Crawl4AI Cloud API — Closed Beta (Launching Soon)

Reliable, large-scale web extraction, now built to be ***drastically more cost-effective*** than any of the existing solutions.

👉 **Apply [here](https://forms.gle/E9MyPaNXACnAMaqG7) for early access**  
*We’ll be onboarding in phases and working closely with early users. Limited slots.*

* * *

Crawl4AI is the #1 trending GitHub repository, actively maintained by a vibrant community. It delivers blazing-fast, AI-ready web crawling tailored for large language models, AI agents, and data pipelines. Fully open source, flexible, and built for real-time performance, **Crawl4AI** empowers developers with unmatched speed, precision, and deployment ease.

> Enjoy using Crawl4AI? Consider [**becoming a sponsor**](https://github.com/sponsors/unclecode) to support ongoing development and community growth!

## 🆕 AI Assistant Skill Now Available!

### 🤖 Crawl4AI Skill for Claude & AI Assistants

Supercharge your AI coding assistant with complete Crawl4AI knowledge! Download our comprehensive skill package that includes:

- 📚 Complete SDK reference (23K+ words)
- 🚀 Ready-to-use extraction scripts
- ⚡ Schema generation for efficient scraping
- 🔧 Version 0.7.4 compatible

Works with Claude, Cursor, Windsurf, and other AI coding assistants. Import the .zip file into your AI assistant's skill/knowledge system.

## 🎯 New: Adaptive Web Crawling

Crawl4AI now features intelligent adaptive crawling that knows when to stop! Using advanced information foraging algorithms, it determines when sufficient information has been gathered to answer your query.

[Learn more about Adaptive Crawling →](https://docs.crawl4ai.com/core/adaptive-crawling/)

## Quick Start

Here's a quick example to show you how easy it is to use Crawl4AI with its asynchronous capabilities:

```
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    # Create an instance of AsyncWebCrawler
    async with AsyncWebCrawler() as crawler:
        # Run the crawler on a URL
        result = await crawler.arun(url="https://crawl4ai.com")

        # Print the extracted content
        print(result.markdown)

# Run the async main function
asyncio.run(main())
```

* * *

## Video Tutorial

* * *

## What Does Crawl4AI Do?

Crawl4AI is a feature-rich crawler and scraper that aims to:

1. **Generate Clean Markdown**: Perfect for RAG pipelines or direct ingestion into LLMs.  
2. **Structured Extraction**: Parse repeated patterns with CSS, XPath, or LLM-based extraction.  
3. **Advanced Browser Control**: Hooks, proxies, stealth modes, session re-use—fine-grained control.  
4. **High Performance**: Parallel crawling, chunk-based extraction, real-time use cases.  
5. **Open Source**: No forced API keys, no paywalls—everyone can access their data.

**Core Philosophies**: - **Democratize Data**: Free to use, transparent, and highly configurable.  
\- **LLM Friendly**: Minimally processed, well-structured text, images, and metadata, so AI models can easily consume it.

* * *

## Documentation Structure

To help you get started, we’ve organized our docs into clear sections:

- **Setup & Installation**  
  Basic instructions to install Crawl4AI via pip or Docker.
- **Quick Start**  
  A hands-on introduction showing how to do your first crawl, generate Markdown, and do a simple extraction.
- **Core**  
  Deeper guides on single-page crawling, advanced browser/crawler parameters, content filtering, and caching.
- **Advanced**  
  Explore link & media handling, lazy loading, hooking & authentication, proxies, session management, and more.
- **Extraction**  
  Detailed references for no-LLM (CSS, XPath) vs. LLM-based strategies, chunking, and clustering approaches.
- **API Reference**  
  Find the technical specifics of each class and method, including `AsyncWebCrawler`, `arun()`, and `CrawlResult`.

Throughout these sections, you’ll find code samples you can **copy-paste** into your environment. If something is missing or unclear, raise an issue or PR.

* * *

## How You Can Support

- **Star & Fork**: If you find Crawl4AI helpful, star the repo on GitHub or fork it to add your own features.
- **File Issues**: Encounter a bug or missing feature? Let us know by filing an issue, so we can improve.
- **Pull Requests**: Whether it’s a small fix, a big feature, or better docs—contributions are always welcome.
- **Join Discord**: Come chat about web scraping, crawling tips, or AI workflows with the community.
- **Spread the Word**: Mention Crawl4AI in your blog posts, talks, or on social media.

**Our mission**: to empower everyone—students, researchers, entrepreneurs, data scientists—to access, parse, and shape the world’s data with speed, cost-efficiency, and creative freedom.

* * *

## Quick Links

- [**GitHub Repo**](https://github.com/unclecode/crawl4ai)
- [**Installation Guide**](https://docs.crawl4ai.com/core/installation/)
- [**Quick Start**](https://docs.crawl4ai.com/core/quickstart/)
- [**API Reference**](https://docs.crawl4ai.com/api/async-webcrawler/)
- [**Changelog**](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)

Thank you for joining me on this journey. Let’s keep building an **open, democratic** approach to data extraction and AI together.

Happy Crawling!  
— *Unclecode, Founder & Maintainer of Crawl4AI*