---
title: WebScrapingStrategy Migration Guide - Crawl4AI Documentation (v0.8.x)
url: https://docs.crawl4ai.com/migration/webscraping-strategy-migration/
source: sitemap
fetched_at: 2026-04-26T07:47:42.481583543-03:00
rendered_js: false
word_count: 202
summary: This document outlines the transition of Crawl4AI's scraping architecture to an LXML-based implementation, confirming that all existing code remains fully compatible without requiring updates.
tags:
    - crawl4ai
    - web-scraping
    - lxml
    - code-migration
    - backward-compatibility
    - library-update
    - performance-optimization
category: guide
---

## Overview

Crawl4AI has simplified its content scraping architecture. The BeautifulSoup-based `WebScrapingStrategy` has been deprecated in favor of the faster LXML-based implementation. However, **no action is required** - your existing code will continue to work.

## What Changed?

1. **`WebScrapingStrategy` is now an alias** for `LXMLWebScrapingStrategy`
2. **The BeautifulSoup implementation has been removed** (~1000 lines of redundant code)
3. **`LXMLWebScrapingStrategy` inherits directly** from `ContentScrapingStrategy`
4. **Performance remains optimal** with LXML as the sole implementation

## Backward Compatibility

**Your existing code continues to work without any changes:**

```
# This still works perfectly
fromcrawl4aiimport AsyncWebCrawler, CrawlerRunConfig, WebScrapingStrategy

config = CrawlerRunConfig(
    scraping_strategy=WebScrapingStrategy()  # Works as before
)
```

## Migration Options

You have three options:

### Option 1: Do Nothing (Recommended)

Your code will continue to work. `WebScrapingStrategy` is permanently aliased to `LXMLWebScrapingStrategy`.

### Option 2: Update Imports (Optional)

For clarity, you can update your imports:

```
# Old (still works)
fromcrawl4aiimport WebScrapingStrategy
strategy = WebScrapingStrategy()

# New (more explicit)
fromcrawl4aiimport LXMLWebScrapingStrategy
strategy = LXMLWebScrapingStrategy()
```

### Option 3: Use Default Configuration

Since `LXMLWebScrapingStrategy` is the default, you can omit the strategy parameter:

```
# Simplest approach - uses LXMLWebScrapingStrategy by default
config = CrawlerRunConfig()
```

## Type Hints

If you use type hints, both work:

```
fromcrawl4aiimport WebScrapingStrategy, LXMLWebScrapingStrategy

defprocess_with_strategy(strategy: WebScrapingStrategy) -> None:
    # Works with both WebScrapingStrategy and LXMLWebScrapingStrategy
    pass

# Both are valid
process_with_strategy(WebScrapingStrategy())
process_with_strategy(LXMLWebScrapingStrategy())
```

## Subclassing

If you've subclassed `WebScrapingStrategy`, it continues to work:

```
classMyCustomStrategy(WebScrapingStrategy):
    def__init__(self):
        super().__init__()
        # Your custom code
```

## Performance Benefits

By consolidating to LXML: - **10-20x faster** HTML parsing for large documents - **Lower memory usage** - **Consistent behavior** across all use cases - **Simplified maintenance** and bug fixes

## Summary

This change simplifies Crawl4AI's internals while maintaining 100% backward compatibility. Your existing code continues to work, and you get better performance automatically.