---
title: Linkup Search | liteLLM
url: https://docs.litellm.ai/docs/search/linkup
source: sitemap
fetched_at: 2026-01-21T19:54:31.018067532-03:00
rendered_js: false
word_count: 0
summary: This code snippet demonstrates how to perform a search using the Linkup provider within the LiteLLM library, specifically detailing various configuration parameters like search depth, date filtering, and domain restrictions.
tags:
    - litellm
    - linkup
    - search-api
    - python-sdk
    - api-integration
category: api
---

```
import os
from litellm import search

os.environ["LINKUP_API_KEY"]="..."

response = search(
    query="machine learning research",
    search_provider="linkup",
    max_results=10,
# Linkup-specific parameters
    depth="deep",# "standard" (faster) or "deep" (more comprehensive)
    outputType="searchResults",# "searchResults", "sourcedAnswer", or "structured"
    includeSources=True,# Include sources in response
    includeImages=True,# Include images in results
    fromDate="2024-01-01",# Start date filter (YYYY-MM-DD)
    toDate="2024-12-31",# End date filter (YYYY-MM-DD)
    includeDomains=["arxiv.org","nature.com"],# Domains to search (max 100)
    excludeDomains=["wikipedia.com"],# Domains to exclude
    includeInlineCitations=True,# Include inline citations in sourcedAnswer
)
```