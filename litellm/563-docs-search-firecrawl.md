---
title: Firecrawl Search | liteLLM
url: https://docs.litellm.ai/docs/search/firecrawl
source: sitemap
fetched_at: 2026-01-21T19:54:29.767596716-03:00
rendered_js: false
word_count: 0
summary: This code example demonstrates how to use the LiteLLM search function with Firecrawl as the provider, including configuration for advanced filtering, geo-targeting, and content scraping.
tags:
    - litellm
    - firecrawl
    - search-api
    - python-sdk
    - web-scraping
category: guide
---

```
import os
from litellm import search

os.environ["FIRECRAWL_API_KEY"]="fc-..."

response = search(
    query="machine learning research",
    search_provider="firecrawl",
    max_results=10,
    country="US",
# Firecrawl-specific parameters
    sources=["web","news"],# Search multiple sources
    categories=[{"type":"github"},{"type":"research"}],# Filter by categories
    tbs="qdr:m",# Time-based search (past month)
    location="San Francisco,California,United States",# Geo-targeting
    ignoreInvalidURLs=True,# Exclude invalid URLs
    scrapeOptions={# Scraping options for results
"formats":["markdown"],
"onlyMainContent":True,
"removeBase64Images":True
}
)
```