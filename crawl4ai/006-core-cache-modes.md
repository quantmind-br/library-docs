---
title: Cache Modes - Crawl4AI Documentation (v0.8.x)
url: https://docs.crawl4ai.com/core/cache-modes/
source: sitemap
fetched_at: 2026-04-26T07:46:56.667405417-03:00
rendered_js: false
word_count: 157
summary: This document outlines the transition from legacy boolean cache flags to the CacheMode enum system introduced in Crawl4AI version 0.5.0. It provides migration mappings and implementation examples for updating existing codebases to the new caching configuration.
tags:
    - crawl4ai
    - caching-system
    - migration-guide
    - software-update
    - enum-configuration
category: guide
---

## Crawl4AI Cache System and Migration Guide

## Overview

Starting from version 0.5.0, Crawl4AI introduces a new caching system that replaces the old boolean flags with a more intuitive `CacheMode` enum. This change simplifies cache control and makes the behavior more predictable.

## Old vs New Approach

### Old Way (Deprecated)

The old system used multiple boolean flags: - `bypass_cache`: Skip cache entirely - `disable_cache`: Disable all caching - `no_cache_read`: Don't read from cache - `no_cache_write`: Don't write to cache

### New Way (Recommended)

The new system uses a single `CacheMode` enum: - `CacheMode.ENABLED`: Normal caching (read/write) - `CacheMode.DISABLED`: No caching at all - `CacheMode.READ_ONLY`: Only read from cache - `CacheMode.WRITE_ONLY`: Only write to cache - `CacheMode.BYPASS`: Skip cache for this operation

## Migration Example

### Old Code (Deprecated)

```
fromcrawl4aiimport AsyncWebCrawler

async defold_code(crawler: AsyncWebCrawler):
    # Legacy `bypass_cache` / `disable_cache` / `no_cache_read` / `no_cache_write`
    # were removed in v0.5+. This example no longer applies:
    result = await crawler.arun(
        url="https://www.nbcnews.com/business",
        # cache_mode is the only cache option now.
    )
    print(len(result.markdown))
```

### New Code (Recommended)

```
importasyncio
fromcrawl4aiimport AsyncWebCrawler, CacheMode
fromcrawl4ai.async_configsimport CrawlerRunConfig

async defuse_proxy():
    # Use CacheMode in CrawlerRunConfig
    config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)  
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            config=config  # Pass the configuration object
        )
        print(len(result.markdown))

async defmain():
    await use_proxy()

if __name__ == "__main__":
    asyncio.run(main())
```

## Common Migration Patterns

Legacy Flag Replacement `bypass_cache` `cache_mode=CacheMode.BYPASS` `disable_cache` `cache_mode=CacheMode.DISABLED` `no_cache_read` `cache_mode=CacheMode.READ_ONLY` `no_cache_write` `cache_mode=CacheMode.WRITE_ONLY`