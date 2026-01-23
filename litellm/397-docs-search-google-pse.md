---
title: Google Programmable Search Engine (PSE) | liteLLM
url: https://docs.litellm.ai/docs/search/google_pse
source: sitemap
fetched_at: 2026-01-21T19:54:30.269789388-03:00
rendered_js: false
word_count: 0
summary: This document demonstrates how to use the litellm library to perform web searches using the Google Programmable Search Engine with advanced filtering parameters.
tags:
    - litellm
    - google-pse
    - search-api
    - python-library
    - api-integration
category: tutorial
---

```
import os
from litellm import search

os.environ["GOOGLE_PSE_API_KEY"]="AIza..."
os.environ["GOOGLE_PSE_ENGINE_ID"]="your-search-engine-id"

response = search(
    query="latest AI research papers",
    search_provider="google_pse",
    max_results=10,
    search_domain_filter=["arxiv.org"],
# Google PSE-specific parameters (use actual Google PSE API parameter names)
    dateRestrict="m6",# 'm6' = last 6 months, 'd7' = last 7 days
    lr="lang_en",# Language restriction (e.g., 'lang_en', 'lang_es')
    safe="active",# Search safety level ('active' or 'off')
    exactTerms="machine learning",# Phrase that all documents must contain
    fileType="pdf"# File type to restrict results to
)
```