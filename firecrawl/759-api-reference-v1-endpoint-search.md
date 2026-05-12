---
title: Search - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/v1-endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:18:21.495872-03:00
rendered_js: false
word_count: 305
summary: This document describes the search API endpoint, which allows users to perform web searches and scrape resulting page content into structured formats.
tags:
    - web-search
    - scraping
    - api-documentation
    - data-extraction
    - query-operators
    - geo-targeting
category: api
---

Search and optionally scrape search results

> Note: A new [v2 version of this API](https://docs.firecrawl.dev/api-reference/endpoint/search) is now available with improved features and performance.

The search endpoint combines web search with Firecrawl’s scraping capabilities to return full page content for any query. Include `scrapeOptions` with `formats: ["markdown"]` to get complete markdown content for each search result otherwise you will default to getting the results (url, title, description).

## Supported query operators

We support a variety of query operators that allow you to filter your searches better.

OperatorFunctionalityExamples`""`Non-fuzzy matches a string of text`"Firecrawl"``-`Excludes certain keywords or negates other operators`-bad`, `-site:firecrawl.dev``site:`Only returns results from a specified website`site:firecrawl.dev``inurl:`Only returns results that include a word in the URL`inurl:firecrawl``allinurl:`Only returns results that include multiple words in the URL`allinurl:git firecrawl``intitle:`Only returns results that include a word in the title of the page`intitle:Firecrawl``allintitle:`Only returns results that include multiple words in the title of the page`allintitle:firecrawl playground``related:`Only returns results that are related to a specific domain`related:firecrawl.dev`

## Location Parameter

Use the `location` parameter to get geo-targeted search results. Format: `"string"`. Examples: `"Germany"`, `"San Francisco,California,United States"`. See the [complete list of supported locations](https://firecrawl.dev/search_locations.json) for all available countries and languages.

## Time-Based Search

Use the `tbs` parameter to filter results by time periods, including custom date ranges. See the [Search Feature documentation](https://docs.firecrawl.dev/features/search#time-based-search) for detailed examples and supported formats.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

Maximum number of results to return

Required range: `1 <= x <= 100`

Time-based search parameter. Supports predefined time ranges (`qdr:h`, `qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`) and custom date ranges (`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`)

Location parameter for search results

Excludes URLs from the search results that are invalid for other Firecrawl endpoints. This helps reduce errors if you are piping data from search into other Firecrawl API endpoints.

Options for scraping search results

#### Response

Warning message if any issues occurred