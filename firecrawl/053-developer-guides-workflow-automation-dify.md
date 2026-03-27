---
title: Firecrawl + Dify - Firecrawl Docs
url: https://docs.firecrawl.dev/developer-guides/workflow-automation/dify
source: sitemap
fetched_at: 2026-03-23T07:39:23.148474-03:00
rendered_js: false
word_count: 156
summary: This document outlines how to integrate the Firecrawl plugin into Dify to enable web scraping, crawling, and mapping capabilities within AI-driven workflows and agents.
tags:
    - dify-integration
    - firecrawl-plugin
    - web-scraping
    - llm-workflows
    - ai-agents
    - data-extraction
category: guide
---

## Dify Integration Overview

Dify is an open-source LLM app development platform. The official Firecrawl plugin enables web crawling and scraping directly in your AI workflows.

## Getting Started

## Usage Patterns

- Chatflow Apps
- Workflow Apps
- Agent Apps

**Visual Pipeline Integration**

1. Add Firecrawl node to your pipeline
2. Select action (Map, Crawl, Scrape)
3. Define input variables
4. Execute pipeline sequentially

**Example Flow:**

```
User Input → Firecrawl (Scrape) → LLM Processing → Response
```

**Automated Data Processing**Build multi-step workflows with:

- Scheduled scraping
- Data transformation
- Database storage
- Notifications

**Example Flow:**

```
Schedule Trigger → Firecrawl (Crawl) → Data Processing → Storage
```

**AI-Powered Web Access**Give agents real-time web scraping capabilities:

1. Add Firecrawl tool to Agent
2. Agent autonomously decides when to scrape
3. LLM analyzes extracted content
4. Agent provides informed responses

**Use Case:** Customer support agents that reference live documentation

## Common Use Cases

## Firecrawl Actions

ToolDescriptionBest For**Scrape**Single-page data extractionQuick content capture**Crawl**Multi-page recursive crawlingFull site extraction**Map**URL discovery and site mappingSEO analysis, URL lists**Crawl Job**Async job managementLong-running operations

## Best Practices

## Dify vs Other Platforms

FeatureDifyMakeZapiern8n**Type**LLM app platformWorkflow automationWorkflow automationWorkflow automation**Best For**AI agents & chatbotsVisual workflowsQuick automationDeveloper control**Pricing**Open-source + CloudOperations-basedPer-taskFlat monthly**AI-Native**YesPartialPartialPartial**Self-Hosted**YesNoNoYes