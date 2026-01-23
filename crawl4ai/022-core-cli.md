---
title: Command Line Interface - Crawl4AI Documentation (v0.7.x)
url: https://docs.crawl4ai.com/core/cli/
source: sitemap
fetched_at: 2026-01-22T22:22:56.667671676-03:00
rendered_js: false
word_count: 349
summary: This document provides a comprehensive guide to using the Crawl4AI CLI, detailing its installation, configuration options, and advanced features like LLM-powered extraction and content filtering.
tags:
    - crawl4ai-cli
    - web-crawling
    - data-extraction
    - llm-integration
    - command-line-tool
    - browser-automation
category: guide
---

## Crawl4AI CLI Guide

## Table of Contents

- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Configuration](#configuration)
- [Browser Configuration](#browser-configuration)
- [Crawler Configuration](#crawler-configuration)
- [Extraction Configuration](#extraction-configuration)
- [Content Filtering](#content-filtering)
- [Advanced Features](#advanced-features)
- [LLM Q&A](#llm-qa)
- [Structured Data Extraction](#structured-data-extraction)
- [Content Filtering](#content-filtering-1)
- [Output Formats](#output-formats)
- [Examples](#examples)
- [Configuration Reference](#configuration-reference)
- [Best Practices & Tips](#best-practices--tips)

## Installation

The Crawl4AI CLI will be installed automatically when you install the library.

## Basic Usage

The Crawl4AI CLI (`crwl`) provides a simple interface to the Crawl4AI library:

```
# Basic crawling
crwlhttps://example.com

# Get markdown output
crwlhttps://example.com-omarkdown

# Verbose JSON output with cache bypass
crwlhttps://example.com-ojson-v--bypass-cache

# See usage examples
crwl--example
```

## Quick Example of Advanced Usage

If you clone the repository and run the following command, you will receive the content of the page in JSON format according to a JSON-CSS schema:

```
crwl"https://www.infoq.com/ai-ml-data-eng/"-edocs/examples/cli/extract_css.yml-sdocs/examples/cli/css_schema.json-ojson;
```

## Configuration

### Browser Configuration

Browser settings can be configured via YAML file or command line parameters:

```
# browser.yml
headless:true
viewport_width:1280
user_agent_mode:"random"
verbose:true
ignore_https_errors:true
```

```
# Using config file
crwlhttps://example.com-Bbrowser.yml

# Using direct parameters
crwlhttps://example.com-b"headless=true,viewport_width=1280,user_agent_mode=random"
```

### Crawler Configuration

Control crawling behavior:

```
# crawler.yml
cache_mode:"bypass"
wait_until:"networkidle"
page_timeout:30000
delay_before_return_html:0.5
word_count_threshold:100
scan_full_page:true
scroll_delay:0.3
process_iframes:false
remove_overlay_elements:true
magic:true
verbose:true
```

```
# Using config file
crwlhttps://example.com-Ccrawler.yml

# Using direct parameters
crwlhttps://example.com-c"css_selector=#main,delay_before_return_html=2,scan_full_page=true"
```

Two types of extraction are supported:

1. CSS/XPath-based extraction:
   
   ```
   # extract_css.yml
   type:"json-css"
   params:
   verbose:true
   ```

```
// css_schema.json
{
"name":"ArticleExtractor",
"baseSelector":".article",
"fields":[
{
"name":"title",
"selector":"h1.title",
"type":"text"
},
{
"name":"link",
"selector":"a.read-more",
"type":"attribute",
"attribute":"href"
}
]
}
```

1. LLM-based extraction:
   
   ```
   # extract_llm.yml
   type:"llm"
   provider:"openai/gpt-4"
   instruction:"Extractallarticleswiththeirtitlesandlinks"
   api_token:"your-token"
   params:
   temperature:0.3
   max_tokens:1000
   ```

```
// llm_schema.json
{
"title":"Article",
"type":"object",
"properties":{
"title":{
"type":"string",
"description":"The title of the article"
},
"link":{
"type":"string",
"description":"URL to the full article"
}
}
}
```

## Advanced Features

### LLM Q&A

Ask questions about crawled content:

```
# Simple question
crwlhttps://example.com-q"What is the main topic discussed?"

# View content then ask questions
crwlhttps://example.com-omarkdown# See content first
crwlhttps://example.com-q"Summarize the key points"
crwlhttps://example.com-q"What are the conclusions?"

# Combined with advanced crawling
crwlhttps://example.com\
-Bbrowser.yml\
-c"css_selector=article,scan_full_page=true"\
-q"What are the pros and cons mentioned?"
```

First-time setup: - Prompts for LLM provider and API token - Saves configuration in `~/.crawl4ai/global.yml` - Supports various providers (openai/gpt-4, anthropic/claude-3-sonnet, etc.) - For case of `ollama` you do not need to provide API token. - See [LiteLLM Providers](https://docs.litellm.ai/docs/providers) for full list

Extract structured data using CSS selectors:

```
crwlhttps://example.com\
-eextract_css.yml\
-scss_schema.json\
-ojson
```

Or using LLM-based extraction:

```
crwlhttps://example.com\
-eextract_llm.yml\
-sllm_schema.json\
-ojson
```

### Content Filtering

Filter content for relevance:

```
# filter_bm25.yml
type:"bm25"
query:"targetcontent"
threshold:1.0

# filter_pruning.yml
type:"pruning"
query:"focustopic"
threshold:0.48
```

```
crwlhttps://example.com-ffilter_bm25.yml-omarkdown-fit
```

## Output Formats

- `all` - Full crawl result including metadata
- `json` - Extracted structured data (when using extraction)
- `markdown` / `md` - Raw markdown output
- `markdown-fit` / `md-fit` - Filtered markdown for better readability

## Complete Examples

1. Basic Extraction:
   
   ```
   crwlhttps://example.com\
   -Bbrowser.yml\
   -Ccrawler.yml\
   -ojson
   ```
2. Structured Data Extraction:
   
   ```
   crwlhttps://example.com\
   -eextract_css.yml\
   -scss_schema.json\
   -ojson\
   -v
   ```
3. LLM Extraction with Filtering:
   
   ```
   crwlhttps://example.com\
   -Bbrowser.yml\
   -eextract_llm.yml\
   -sllm_schema.json\
   -ffilter_bm25.yml\
   -ojson
   ```
4. Interactive Q&A:
   
   ```
   # First crawl and view
   crwlhttps://example.com-omarkdown
   
   # Then ask questions
   crwlhttps://example.com-q"What are the main points?"
   crwlhttps://example.com-q"Summarize the conclusions"
   ```

## Best Practices & Tips

01. **Configuration Management**:
02. Keep common configurations in YAML files
03. Use CLI parameters for quick overrides
04. Store sensitive data (API tokens) in `~/.crawl4ai/global.yml`
05. **Performance Optimization**:
06. Use `--bypass-cache` for fresh content
07. Enable `scan_full_page` for infinite scroll pages
08. Adjust `delay_before_return_html` for dynamic content
09. **Content Extraction**:
10. Use CSS extraction for structured content
11. Use LLM extraction for unstructured content
12. Combine with filters for focused results
13. **Q&A Workflow**:
14. View content first with `-o markdown`
15. Ask specific questions
16. Use broader context with appropriate selectors

## Recap

The Crawl4AI CLI provides: - Flexible configuration via files and parameters - Multiple extraction strategies (CSS, XPath, LLM) - Content filtering and optimization - Interactive Q&A capabilities - Various output formats