---
description: Auto-generated documentation index for Crawl4AI
generated: 2026-01-22T22:24:00Z
source: https://docs.crawl4ai.com/sitemap.xml
total_docs: 78
categories: 12
---

# Crawl4AI Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://docs.crawl4ai.com/sitemap.xml |
| **Generated** | 2026-01-22 |
| **Total Documents** | 78 |
| **Strategy** | sitemap |
| **Version** | v0.7.x |

---

## Document Index

### 1. Introduction & Overview (001-002)
*Project introduction, branding guidelines, and visual identity*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-index.md` | Home | Introduction to Crawl4AI, an open-source web crawler for LLM-friendly formats | crawl4ai, web-crawling, llm-friendly, open-source |
| 002 | `002-branding.md` | Brand Book | Visual identity and design system with terminal-inspired aesthetic | brand-guidelines, design-system, typography |

### 2. Installation & Quick Start (003-005)
*Getting started with installation and first crawl*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 003 | `003-basic-installation.md` | Installation | Comprehensive setup options including pip and system dependencies | installation, setup-guide, playwright |
| 004 | `004-core-installation.md` | Installation | Core setup with diagnostic tools and optional features | installation, environment-config, dependencies |
| 005 | `005-core-quickstart.md` | Quick Start | Introductory guide covering async crawling and data extraction | web-crawling, quickstart, markdown-generation |

### 3. Core Fundamentals - Crawling Basics (006-015)
*Essential crawling concepts, configuration, and techniques*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 006 | `006-core-simple-crawling.md` | Simple Crawling | Fundamentals of web crawling with setup and configuration | web-crawling, python, async, data-extraction |
| 007 | `007-core-browser-crawler-config.md` | Browser & Crawler Config | BrowserConfig and CrawlerRunConfig customization | browser-config, crawler-settings, stealth |
| 008 | `008-core-crawler-result.md` | Crawler Result | CrawlResult object structure and output fields | crawl-result, data-models, html-processing |
| 009 | `009-core-cache-modes.md` | Cache Modes | CacheMode enum system migration from boolean flags | caching, migration-guide, cache-mode |
| 010 | `010-core-content-selection.md` | Content Selection | CSS selectors for content filtering and element exclusion | content-filtering, css-selectors, web-scraping |
| 011 | `011-core-page-interaction.md` | Page Interaction | JavaScript execution, wait conditions, session management | javascript, dynamic-content, form-interaction |
| 012 | `012-core-local-files.md` | Local Files & Raw HTML | Prefix-based input system for URLs, files, and raw HTML | html-parsing, input-handling, local-files |
| 013 | `013-core-url-seeding.md` | URL Seeding | Deep crawling vs URL seeding for web discovery | url-seeding, deep-crawling, data-extraction |
| 014 | `014-core-deep-crawling.md` | Deep Crawling | Multi-page crawling with BFS/DFS strategies and filtering | deep-crawling, bfs, dfs, content-filtering |
| 015 | `015-core-adaptive-crawling.md` | Adaptive Crawling | Intelligent stopping based on statistical/semantic metrics | adaptive-crawling, information-retrieval, semantic |

### 4. Markdown & Content Processing (016-020)
*Converting web content to clean markdown and structured data*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 016 | `016-core-markdown-generation.md` | Markdown Generation | Default Markdown Generator configuration and filters | markdown-generation, content-filtering, html-to-md |
| 017 | `017-core-fit-markdown.md` | Fit Markdown | Pruning and BM25 filters for concise markdown output | fit-markdown, pruning-filter, bm25-filter |
| 018 | `018-core-link-media.md` | Link & Media | Link extraction, filtering, scoring, and media handling | link-extraction, media-handling, image-filtering |
| 019 | `019-core-table-extraction.md` | Table Extraction | Strategy-based table extraction with LLM support | table-extraction, strategy-pattern, llm |
| 020 | `020-core-examples.md` | Code Examples | Directory of example scripts for various use cases | examples, web-scraping, automation-scripts |

### 5. Scripting, CLI & Hosting (021-025)
*Command-line tools, scripting DSL, and self-hosting*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 021 | `021-core-c4a-script.md` | C4A Script | Domain-specific language for web automation | dsl, web-automation, ui-testing, blockly |
| 022 | `022-core-cli.md` | Command Line Interface | CLI usage with LLM extraction and content filtering | cli, command-line, data-extraction |
| 023 | `023-core-self-hosting.md` | Hosting Guide | Docker and Docker Compose self-hosting instructions | self-hosting, docker, deployment, mcp |
| 024 | `024-core-llmtxt.md` | LLM Text | (Placeholder) | llmtxt |
| 025 | `025-core-ask-ai.md` | Ask AI | (Placeholder) | ask-ai |

### 6. Extraction Strategies (026-029)
*Data extraction methods with and without LLMs*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 026 | `026-extraction-no-llm-strategies.md` | Free Strategies | CSS and XPath extraction without LLMs | css-selectors, xpath, json-extraction |
| 027 | `027-extraction-llm-strategies.md` | LLM Strategies | LLM-based extraction via LiteLLM for complex content | llm-extraction, litellm, pydantic-schema |
| 028 | `028-extraction-chunking.md` | Chunking | Text chunking strategies for NLP and RAG systems | chunking, nlp, rag, text-segmentation |
| 029 | `029-extraction-clustring-strategies.md` | Clustering Strategies | Cosine similarity and vector clustering extraction | cosine-strategy, semantic, vector-embeddings |

### 7. Advanced Features (030-044)
*Authentication, stealth mode, proxies, and specialized crawling*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 030 | `030-advanced-advanced-features.md` | Advanced Overview | Proxy usage, screenshots, PDFs, SSL, session persistence | proxy, pdf, screenshot, ssl |
| 031 | `031-advanced-hooks-auth.md` | Hooks & Auth | Lifecycle hooks for authentication and route filtering | hooks, authentication, middleware |
| 032 | `032-advanced-session-management.md` | Session Management | State persistence across sequential crawling requests | session-management, dynamic-content, browser-tabs |
| 033 | `033-advanced-identity-based-crawling.md` | Identity Based Crawling | Managed browsers and Magic Mode for persistent sessions | managed-browsers, magic-mode, bot-evasion |
| 034 | `034-advanced-undetected-browser.md` | Undetected Browser | Stealth and undetected modes for anti-bot bypass | stealth-mode, undetected-browser, fingerprinting |
| 035 | `035-advanced-proxy-security.md` | Proxy & Security | Proxy configuration, rotation, and SSL analysis | proxy-config, proxy-rotation, ssl-certificates |
| 036 | `036-advanced-ssl-certificate.md` | SSL Certificate | SSLCertificate class for fetching and exporting certs | ssl-certificate, pem, der, json-export |
| 037 | `037-advanced-lazy-loading.md` | Lazy Loading | Handling lazy-loaded images with scroll and wait params | lazy-loading, image-extraction, scrolling |
| 038 | `038-advanced-virtual-scroll.md` | Virtual Scroll | Capturing content from windowed rendering websites | virtual-scroll, infinite-scroll, dom-manipulation |
| 039 | `039-advanced-multi-url-crawling.md` | Multi-URL Crawling | Dispatchers for rate limiting and concurrency control | multi-url, concurrency, memory-adaptive |
| 040 | `040-advanced-file-downloading.md` | File Downloading | Enabling and managing file downloads via JS execution | file-downloads, browser-config, automation |
| 041 | `041-advanced-network-console-capture.md` | Network & Console Capture | Capturing network requests and console messages | network-requests, console-messages, debugging |
| 042 | `042-advanced-pdf-parsing.md` | PDF Parsing | PDF crawling strategies for text and image extraction | pdf-processing, content-extraction, async |
| 043 | `043-advanced-adaptive-strategies.md` | Adaptive Strategies | Scoring systems and link ranking algorithms | adaptive-crawling, scoring, link-ranking |
| 044 | `044-advanced-crawl-dispatcher.md` | Crawl Dispatcher | (Coming soon) High-performance task management | crawl-dispatcher, scalability, monitoring |

### 8. API Reference (045-054)
*Complete API documentation for classes and methods*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 045 | `045-api-async-webcrawler.md` | AsyncWebCrawler | Core crawler class lifecycle and configuration | asyncwebcrawler, python-api, browser-config |
| 046 | `046-api-adaptive-crawler.md` | AdaptiveCrawler | Query-driven intelligent crawling class | adaptive-crawler, async, knowledge-base |
| 047 | `047-api-arun.md` | arun() | CrawlerRunConfig model and single-crawl parameters | arun, crawler-run-config, anti-bot |
| 048 | `048-api-arun-many.md` | arun_many() | Concurrent batch crawling with dispatchers | batch-crawling, concurrency, async-generator |
| 049 | `049-api-digest.md` | digest() | Query-guided crawling and information extraction | digest, information-retrieval, link-analysis |
| 050 | `050-api-crawl-result.md` | CrawlResult | Data structure returned after crawl operations | crawlresult, data-extraction, python-models |
| 051 | `051-api-parameters.md` | Browser & Crawler Config | BrowserConfig and CrawlerRunConfig parameter reference | browser-config, crawler-settings, api-ref |
| 052 | `052-api-strategies.md` | Strategies | Extraction and chunking strategy implementations | extraction-strategy, chunking, llm, regex |
| 053 | `053-api-c4a-script-reference.md` | Script Reference | C4A-Script API for browser navigation and interactions | c4a-script, api-reference, web-automation |
| 054 | `054-complete-sdk-reference.md` | Complete SDK Reference | Comprehensive SDK installation and usage guide | sdk, installation, content-processing |

### 9. Apps & Demo Tools (055-057)
*Interactive tools and visual editors*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 055 | `055-apps.md` | Demo Apps | Apps Hub with visual tools for scraping and automation | interactive-tools, visual-programming |
| 056 | `056-apps-llmtxt-why.md` | LLM Context Strategy | Modular documentation for AI assistant performance | llm-context, documentation-strategy, modular |
| 057 | `057-apps-llmtxt-build.md` | Build LLM Context | Tool for combining docs into single Markdown context | context-builder, markdown-generation |

### 10. Migration Guides (058-059)
*Upgrading between versions*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 058 | `058-migration-webscraping-strategy-migration.md` | WebScrapingStrategy Migration | BeautifulSoup to LXML transition guide | migration, lxml, performance |
| 059 | `059-migration-table-extraction-v073.md` | Table Extraction v0.7.3 | Table extraction strategy pattern migration | table-extraction, strategy-pattern, v0.7.3 |

### 11. Blog Articles (060-064)
*Technical articles and deep dives*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 060 | `060-blog.md` | Blog Home | Blog overview with articles and release notes | blog, changelog, updates |
| 061 | `061-blog-articles-adaptive-crawling-revolution.md` | Adaptive Crawling Revolution | Information theory-based intelligent data acquisition | adaptive-crawling, information-theory |
| 062 | `062-blog-articles-llm-context-revolution.md` | LLM Context Protocol | Memory, Reasoning, Examples framework for AI assistants | llm-context-protocol, ai-documentation |
| 063 | `063-blog-articles-virtual-scroll-revolution.md` | Virtual Scroll Revolution | Scraping dynamic content with DOM element replacement | virtual-scroll, dom-manipulation |
| 064 | `064-blog-articles-dockerize-hooks.md` | Dockerize Hooks | Event-driven streams and interactive hooks | event-streams, interactive-hooks, sse |

### 12. Release Notes (065-078)
*Version history from newest to oldest*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 065 | `065-blog-releases-v0.7.8.md` | v0.7.8 | Stability improvements and bug fixes | docker, llm-extraction, bug-fixes |
| 066 | `066-blog-releases-v0.7.7.md` | v0.7.7 | Self-hosting platform with monitoring and REST APIs | self-hosting, monitoring, observability |
| 067 | `067-blog-releases-0.7.6.md` | v0.7.6 | Webhook infrastructure for Docker job queue API | webhooks, docker-api, real-time |
| 068 | `068-blog-releases-v0.7.5.md` | v0.7.5 | Docker Hooks System and LLM integration | docker-hooks, llm-integration |
| 069 | `069-blog-releases-0.7.3.md` | v0.7.3 | Multi-Config Intelligence with URL-specific configs | multi-url, docker-config, llm-extraction |
| 070 | `070-blog-releases-0.7.2.md` | v0.7.2 | CI/CD pipelines and dependency optimization | cicd, github-actions, dependencies |
| 071 | `071-blog-releases-0.7.1.md` | v0.7.1 | Minor cleanup and documentation improvements | maintenance, documentation |
| 072 | `072-blog-releases-0.7.0.md` | v0.7.0 | Adaptive Intelligence Update with virtual scroll | adaptive-crawling, virtual-scroll, link-analysis |
| 073 | `073-blog-releases-0.6.0.md` | v0.6.0 | Geo-aware crawling and browser pooling | geo-aware, browser-pooling, mcp-api |
| 074 | `074-blog-releases-0.5.0.md` | v0.5.0 | Deep crawling strategies and Docker deployment | deep-crawling, docker, memory-management |
| 075 | `075-blog-releases-v0.4.3b1.md` | v0.4.3b1 | Memory-adaptive dispatching and LLM extraction | memory-adaptive, llm-integration |
| 076 | `076-blog-releases-0.4.2.md` | v0.4.2 | Configuration management and session handling | browser-config, session, pdf-export |
| 077 | `077-blog-releases-0.4.1.md` | v0.4.1 | Lazy-loaded images and text-only crawling | lazy-loading, performance, scraping |
| 078 | `078-blog-releases-0.4.0.md` | v0.4.0 | PruningContentFilter and thread safety | content-filtering, thread-safety, bm25 |

---

## Quick Reference

### By Topic
| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-005 |
| **Core Crawling** | 006-015 |
| **Content Processing** | 016-020 |
| **Scripting & CLI** | 021-025 |
| **Extraction** | 026-029 |
| **Advanced** | 030-044 |
| **API Reference** | 045-054 |
| **Apps & Tools** | 055-057 |
| **Migration** | 058-059 |
| **Blog & Releases** | 060-078 |

### By Concept
| Concept | Files |
|---------|-------|
| **Installation** | 003, 004, 054 |
| **Browser Config** | 007, 030, 045, 051 |
| **Session Management** | 011, 032, 033 |
| **LLM Extraction** | 019, 027, 052 |
| **Stealth/Anti-bot** | 033, 034, 047 |
| **Docker/Self-hosting** | 023, 064, 066, 067, 068 |
| **Adaptive Crawling** | 015, 043, 046, 061 |
| **Virtual Scroll** | 038, 063 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-002** for project introduction and overview
- Complete files **003-005** for installation and quick start

### Level 2: Core Understanding
- Learn basic crawling from files **006-015**
- Understand configuration with files **007, 009, 010**

### Level 3: Content Processing
- Master markdown generation in files **016-020**
- Learn extraction strategies in files **026-029**

### Level 4: Practical Application
- Explore CLI and scripting in files **021-025**
- Study code examples in file **020**

### Level 5: Advanced Usage
- Master advanced features in files **030-044**
- Handle anti-bot and stealth in files **033-035**

### Level 6: API Mastery
- Consult API reference docs **045-054**
- Review complete SDK in file **054**

### Level 7: Production & Deployment
- Self-hosting guide in file **023**
- Migration guides in files **058-059**
- Release notes for updates **065-078**

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression.*
