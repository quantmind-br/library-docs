---
title: Choosing the Data Extractor | Firecrawl
url: https://docs.firecrawl.dev/developer-guides/usage-guides/choosing-the-data-extractor
source: sitemap
fetched_at: 2026-03-23T07:30:16.022974-03:00
rendered_js: false
word_count: 869
summary: This document compares the three primary methods for structured data extraction in Firecrawl—agent, extract, and scrape—providing a decision guide based on use cases, cost, and URL requirements.
tags:
    - web-scraping
    - data-extraction
    - firecrawl
    - autonomous-agents
    - api-guide
    - structured-data
category: guide
---

Firecrawl offers three approaches for extracting structured data from web pages. Each serves different use cases with varying levels of automation and control.

## Quick Comparison

Feature`/agent``/extract``/scrape` (JSON mode)**Status**ActiveUse `/agent` insteadActive**URL Required**No (optional)Yes (wildcards supported)Yes (single URL)**Scope**Web-wide discoveryMultiple pages/domainsSingle page**URL Discovery**Autonomous web searchCrawls from given URLsNone**Processing**AsynchronousAsynchronousSynchronous**Schema Required**No (prompt or schema)No (prompt or schema)No (prompt or schema)**Pricing**Dynamic (5 free runs/day)Token-based (1 credit = 15 tokens)1 credit/page**Best For**Research, discovery, complex gatheringMulti-page extraction (when you know URLs)Known single-page extraction

## 1. `/agent` Endpoint

The `/agent` endpoint is Firecrawl’s most advanced offering—the successor to `/extract`. It uses AI agents to autonomously search, navigate, and gather data from across the web.

### Key Characteristics

- **URLs Optional**: Just describe what you need via `prompt`; URLs are completely optional
- **Autonomous Navigation**: The agent searches and navigates deep into sites to find your data
- **Deep Web Search**: Autonomously discovers information across multiple domains and pages
- **Parallel Processing**: Processes multiple sources simultaneously for faster results
- **Models Available**: `spark-1-mini` (default, 60% cheaper) and `spark-1-pro` (higher accuracy)

### Example

### Best Use Case: Autonomous Research & Discovery

**Scenario**: You need to find information about AI startups that raised Series A funding, including their founders and funding amounts. **Why `/agent`** : You don’t know which websites contain this information. The agent will autonomously search the web, navigate to relevant sources (Crunchbase, news sites, company pages), and compile the structured data for you. For more details, see the [Agent documentation](https://docs.firecrawl.dev/features/agent).

* * *

The `/extract` endpoint collects structured data from specified URLs or entire domains using LLM-powered extraction.

### Key Characteristics

- **URLs Typically Required**: Provide at least one URL (supports wildcards like `example.com/*`)
- **Domain Crawling**: Can crawl and parse all URLs discovered in a domain
- **Web Search Enhancement**: Optional `enableWebSearch` to follow links outside specified domains
- **Schema Optional**: Supports strict JSON schema OR natural language prompts
- **Async Processing**: Returns job ID for status checking

### The URL Limitation

The fundamental challenge with `/extract` is that you typically need to know URLs upfront:

1. **Discovery gap**: For tasks like “find YC W24 companies,” you don’t know which URLs contain the data. You’d need a separate search step before calling `/extract`.
2. **Awkward web search**: While `enableWebSearch` exists, it’s constrained to start from URLs you provide—an awkward workflow for discovery tasks.
3. **Why `/agent` was created**: `/extract` is good at extracting from known locations, but less effective at discovering where data lives.

### Example

**Scenario**: You have your competitor’s documentation URL and want to extract all their API endpoints from `docs.competitor.com/*`. **Why `/extract` worked here**: You knew the exact domain. But even then, `/agent` with URLs provided would typically give better results today. For more details, see the [Extract documentation](https://docs.firecrawl.dev/features/extract).

* * *

## 3. `/scrape` Endpoint with JSON Mode

The `/scrape` endpoint with JSON mode is the most controlled approach—it extracts structured data from a single known URL using an LLM to parse the page content into your specified schema.

### Key Characteristics

- **Single URL Only**: Designed for extracting data from one specific page at a time
- **Exact URL Required**: You must know the precise URL containing the data
- **Schema Optional**: Can use JSON schema OR just a prompt (LLM chooses structure)
- **Synchronous**: Returns data immediately (no job polling needed)
- **Additional Formats**: Can combine JSON extraction with markdown, HTML, screenshots in one request

### Example

**Scenario**: You’re building a price monitoring tool and need to extract the price, stock status, and product details from a specific product page you already have the URL for. **Why `/scrape` with JSON mode**: You know exactly which page contains the data, need precise single-page extraction, and want synchronous results without job management overhead. For more details, see the [JSON mode documentation](https://docs.firecrawl.dev/features/llm-extract).

* * *

## Decision Guide

**Do you know the exact URL(s) containing your data?**

- **NO** → Use `/agent` (autonomous web discovery)
- **YES**
  
  - **Single page?** → Use `/scrape` with JSON mode
  - **Multiple pages?** → Use `/agent` with URLs (or batch `/scrape`)

### Recommendations by Scenario

ScenarioRecommended Endpoint”Find all AI startups and their funding”`/agent`”Extract data from this specific product page”`/scrape` (JSON mode)“Get all blog posts from competitor.com”`/agent` with URL”Monitor prices across multiple known URLs”`/scrape` with batch processing”Research companies in a specific industry”`/agent`”Extract contact info from 50 known company pages”`/scrape` with batch processing

* * *

## Pricing

EndpointCostNotes`/scrape` (JSON mode)1 credit/pageFixed, predictable`/extract`Token-based (1 credit = 15 tokens)Variable based on content`/agent`Dynamic5 free runs/day; varies by complexity

### Example: “Find the founders of Firecrawl”

EndpointHow It WorksCredits Used`/scrape`You find the URL manually, then scrape 1 page~1 credit`/extract`You provide URL(s), it extracts structured dataVariable (token-based)`/agent`Just send the prompt—agent finds and extracts~100–500 credits

**Tradeoff**: `/scrape` is cheapest but requires you to know the URL. `/agent` costs more but handles discovery automatically. For detailed pricing, see [Firecrawl Pricing](https://firecrawl.dev/pricing).

* * *

If you’re currently using `/extract`, migration is straightforward: **Before (extract):**

```
result = app.extract(
    urls=["https://example.com/*"],
    prompt="Extract product information",
    schema=schema
)
```

**After (agent):**

```
result = app.agent(
    urls=["https://example.com"],  # Optional - can omit entirely
    prompt="Extract product information from example.com",
    schema=schema,
    model="spark-1-mini"  # or "spark-1-pro" for higher accuracy
)
```

The key advantage: with `/agent`, you can drop the URLs entirely and just describe what you need.

* * *

## Key Takeaways

1. **Know the exact URL?** Use `/scrape` with JSON mode—it’s the cheapest (1 credit/page), fastest (synchronous), and most predictable option.
2. **Need autonomous research?** Use `/agent`—it handles discovery automatically with 5 free runs/day, then dynamic pricing based on complexity.
3. **Migrate from `/extract`** to `/agent` for new projects—`/agent` is the successor with better capabilities.
4. **Cost vs. convenience tradeoff**: `/scrape` is most cost-effective when you know your URLs; `/agent` costs more but eliminates manual URL discovery.

* * *

## Further Reading

- [Agent documentation](https://docs.firecrawl.dev/features/agent)
- [Agent models](https://docs.firecrawl.dev/features/models)
- [JSON mode documentation](https://docs.firecrawl.dev/features/llm-extract)
- [Extract documentation](https://docs.firecrawl.dev/features/extract)
- [Batch scraping](https://docs.firecrawl.dev/features/batch-scrape)