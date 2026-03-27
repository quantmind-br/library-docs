---
title: Search - Firecrawl Docs
url: https://docs.firecrawl.dev/api-reference/endpoint/search
source: sitemap
fetched_at: 2026-03-23T07:19:37.459807-03:00
rendered_js: false
word_count: 598
summary: This document provides a technical overview and parameter reference for the Firecrawl search endpoint, which enables web searching with integrated scraping capabilities.
tags:
    - api-reference
    - web-scraping
    - search-engine
    - data-extraction
    - geo-targeting
    - query-operators
    - enterprise-features
category: api
---

Search and optionally scrape search results

The search endpoint combines web search with Firecrawl’s scraping capabilities to return full page content for any query. Include `scrapeOptions` with `formats: [{"type": "markdown"}]` to get complete markdown content for each search result otherwise you will default to getting the results (url, title, description). You can also use other formats like `{"type": "summary"}` for condensed content.

## Supported query operators

We support a variety of query operators that allow you to filter your searches better.

OperatorFunctionalityExamples`""`Non-fuzzy matches a string of text`"Firecrawl"``-`Excludes certain keywords or negates other operators`-bad`, `-site:firecrawl.dev``site:`Only returns results from a specified website`site:firecrawl.dev``filetype:`Only returns results with a specific file extension`filetype:pdf`, `-filetype:pdf``inurl:`Only returns results that include a word in the URL`inurl:firecrawl``allinurl:`Only returns results that include multiple words in the URL`allinurl:git firecrawl``intitle:`Only returns results that include a word in the title of the page`intitle:Firecrawl``allintitle:`Only returns results that include multiple words in the title of the page`allintitle:firecrawl playground``related:`Only returns results that are related to a specific domain`related:firecrawl.dev``imagesize:`Only returns images with exact dimensions`imagesize:1920x1080``larger:`Only returns images larger than specified dimensions`larger:1920x1080`

## Location Parameter

Use the `location` parameter to get geo-targeted search results. Format: `"string"`. Examples: `"Germany"`, `"San Francisco,California,United States"`. See the [complete list of supported locations](https://firecrawl.dev/search_locations.json) for all available countries and languages.

## Country Parameter

Use the `country` parameter to specify the country for search results using ISO country codes. Default: `"US"`. Examples: `"US"`, `"DE"`, `"FR"`, `"JP"`, `"UK"`, `"CA"`.

```
{
  "query": "restaurants",
  "country": "DE"
}
```

## Categories Parameter

Filter search results by specific categories using the `categories` parameter:

- **`github`** : Search within GitHub repositories, code, issues, and documentation
- **`research`** : Search academic and research websites (arXiv, Nature, IEEE, PubMed, etc.)
- **`pdf`** : Search for PDFs

### Example Usage

```
{
  "query": "machine learning",
  "categories": ["github", "research"],
  "limit": 10
}
```

### Category Response

Each result includes a `category` field indicating its source:

```
{
  "success": true,
  "data": {
    "web": [
      {
        "url": "https://github.com/example/ml-project",
        "title": "Machine Learning Project",
        "description": "Implementation of ML algorithms",
        "category": "github"
      },
      {
        "url": "https://arxiv.org/abs/2024.12345",
        "title": "ML Research Paper",
        "description": "Latest advances in machine learning",
        "category": "research"
      }
    ]
  }
}
```

## Time-Based Search

Use the `tbs` parameter to filter results by time periods, including custom date ranges. See the [Search Feature documentation](https://docs.firecrawl.dev/features/search#time-based-search) for detailed examples and supported formats.

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.

#### Authorizations

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

The search query

Maximum string length: `500`

Maximum number of results to return

Required range: `1 <= x <= 100`

sources

(Web · object | Images · object | News · object)\[]

Sources to search. Will determine the arrays available in the response. Defaults to \['web'].

- Web
- Images
- News

categories

(GitHub · object | Research · object | PDF · object)\[]

Categories to filter results by. Defaults to \[], which means results will not be filtered by any categories.

- GitHub
- Research
- PDF

Time-based search parameter. Supports predefined time ranges (`qdr:h`, `qdr:d`, `qdr:w`, `qdr:m`, `qdr:y`), custom date ranges (`cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY`), and sort by date (`sbd:1`). Values can be combined, e.g. `sbd:1,qdr:w`.

Location parameter for search results (e.g. `San Francisco,California,United States`). For best results, set both this and the `country` parameter.

ISO country code for geo-targeting search results (e.g. `US`). For best results, set both this and the `location` parameter.

Excludes URLs from the search results that are invalid for other Firecrawl endpoints. This helps reduce errors if you are piping data from search into other Firecrawl API endpoints.

Enterprise search options for Zero Data Retention (ZDR). Use `["zdr"]` for end-to-end ZDR (10 credits / 10 results) or `["anon"]` for anonymized ZDR (2 credits / 10 results). Must be enabled for your team.

Available options:

`anon`,

`zdr`

Options for scraping search results

#### Response

The search results. The arrays available will depend on the sources you specified in the request. By default, the `web` array will be returned.

Warning message if any issues occurred

The number of credits used for the search