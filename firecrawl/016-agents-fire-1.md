---
title: FIRE-1 AI Agent (Beta) | Firecrawl
url: https://docs.firecrawl.dev/agents/fire-1
source: sitemap
fetched_at: 2026-03-23T07:40:21.996078-03:00
rendered_js: false
word_count: 144
summary: This document introduces the FIRE-1 AI agent, which utilizes autonomous planning and browser automation to extract data from complex or dynamic websites.
tags:
    - fire-1
    - ai-agent
    - web-scraping
    - browser-automation
    - data-extraction
    - firecrawl
category: concept
---

FIRE-1 is an AI agent that enhances Firecrawl’s scraping capabilities. It can controls browser actions and navigates complex website structures to enable comprehensive data extraction beyond traditional scraping methods.

### What FIRE-1 Can Do:

- Plan and take actions to uncover data
- Interact with buttons, links, inputs, and dynamic elements.
- Get multiple pages of data that require pagination, multiple steps, etc.

## How to use FIRE-1

You can leverage the FIRE-1 agent with the `/v1/extract` endpoint for complex extraction tasks that require navigation across multiple pages or interaction with elements. **Example:**

## Billing

The cost of using FIRE-1 is non-deterministic. See our [credit calculator](https://www.firecrawl.dev/extract-calculator) to learn about the base cost of each Extract request. **Why is FIRE-1 more expensive?**  
FIRE-1 leverages advanced browser automation and AI planning to interact with complex web pages, which requires more compute resources than standard extraction.

## Rate limits

- `/extract`: 10 requests per minute