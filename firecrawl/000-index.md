---
description: Auto-generated documentation index for Firecrawl
generated: 2026-03-23T10:53:58Z
source: https://docs.firecrawl.dev/sitemap.xml
total_docs: 135
categories: 15
---

# Firecrawl Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.
> Translations available in: Spanish (es), French (fr), Japanese (ja), Portuguese-BR (pt-BR), Chinese (zh)

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://docs.firecrawl.dev/sitemap.xml |
| **Generated** | 2026-03-23T10:53:58Z |
| **Total Documents** | 135 (English) + 675 translations = 810 total |
| **Categories** | Introduction & Overview, Configuration & Setup, Core Features, SDKs & CLI, LLM Framework Integration, MCP Setup Guides, Scraping Common Sites, Workflow Automation, Cookbooks & Usage Guides, Use Cases, Webhooks, API Reference V2 - Core Endpoints, API Reference V2 - Webhook Events, API Reference V1 (Legacy), Contributing & Self-Hosting |
| **Languages** | English (primary), Spanish, French, Japanese, Portuguese-BR, Chinese |

---

## Document Index

### 1. Introduction & Overview (001-003)
*Getting started with Firecrawl - overview, dashboard, and billing*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-introduction.md` | Quickstart \| Firecrawl | This document provides an introduction to Firecrawl, a web scraping and crawling service designed... | web-scraping, ai-agents, data-extraction, markdown-conversion |
| 002 | `002-dashboard.md` | Dashboard \| Firecrawl | This document provides an overview of the Firecrawl dashboard features, including tools for testi... | firecrawl-dashboard, account-management, team-roles, api-monitoring |
| 003 | `003-billing.md` | Billing \| Firecrawl | This document explains the credit-based billing system, subscription plans, usage tracking, and a... | credit-billing, api-usage, subscription-plans, web-scraping |

### 2. Configuration & Setup (004-007)
*Rate limits, MCP server setup, migration guide, and advanced scraping configuration*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 004 | `004-rate-limits.md` | Rate Limits \| Firecrawl | This document outlines the subscription-based billing model, concurrent browser limits, and API r... | billing-model, subscription-plans, concurrency-limits, rate-limiting |
| 005 | `005-mcp-server.md` | Firecrawl MCP Server | This document provides comprehensive instructions for installing and configuring the Firecrawl Mo... | mcp, firecrawl, web-scraping, ai-integration |
| 006 | `006-migrate-to-v2.md` | Migrating from v1 to v2 \| Firecrawl | This document provides a technical migration guide for upgrading from v1 to v2 of the Firecrawl A... | api-migration, sdk-update, web-scraping, firecrawl |
| 007 | `007-advanced-scraping-guide.md` | Advanced Scraping Guide \| Firecrawl | This document provides a comprehensive reference for configuring Firecrawl's scrape endpoints, in... | firecrawl, web-scraping, api-reference, pdf-parsing |

### 3. Core Features (008-023)
*All Firecrawl features - scraping, crawling, mapping, searching, extracting, and more*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 008 | `008-features-scrape.md` | Scrape \| Firecrawl | Firecrawl is a service that transforms websites into clean, LLM-ready data formats including mark... | web-scraping, data-extraction, markdown-conversion, llm-preparation |
| 009 | `009-features-crawl.md` | Crawl \| Firecrawl | This document explains how to use the Firecrawl API to recursively discover and scrape content ac... | web-scraping, api-reference, crawling, data-extraction |
| 010 | `010-features-map.md` | Map \| Firecrawl | This document explains the usage and configuration of the /map endpoint, which allows users to re... | web-crawling, url-discovery, api-endpoint, site-mapping |
| 011 | `011-features-search.md` | Search \| Firecrawl | This document describes the Firecrawl search API, detailing how to perform web, image, and news s... | api, web-scraping, search-engine, data-extraction |
| 012 | `012-features-extract.md` | Extract \| Firecrawl | This document describes how to use the Firecrawl /extract endpoint to perform structured data ext... | web-scraping, structured-data, api-documentation, data-extraction |
| 013 | `013-features-llm-extract.md` | JSON mode \| Firecrawl | This document explains how to use Firecrawl's scraping endpoint to extract structured data from w... | web-scraping, data-extraction, json-schema, ai-automation |
| 014 | `014-features-batch-scrape.md` | Batch Scrape \| Firecrawl | This document explains how to perform concurrent scraping of multiple URLs using Firecrawl's batc... | batch-scraping, web-scraping, api-integration, concurrency-control |
| 015 | `015-features-agent.md` | Agent \| Firecrawl | This document explains the functionality and usage of the Firecrawl /agent API, a tool designed t... | web-scraping, data-extraction, ai-agent, api-documentation |
| 016 | `016-agents-fire-1.md` | FIRE-1 AI Agent (Beta) \| Firecrawl | This document introduces the FIRE-1 AI agent, which utilizes autonomous planning and browser auto... | fire-1, ai-agent, web-scraping, browser-automation |
| 017 | `017-features-browser.md` | Browser \| Firecrawl | Firecrawl Browser Sandbox provides a secure, managed environment for AI agents to perform complex... | browser-automation, ai-agents, headless-browser, playwright |
| 018 | `018-features-document-parsing.md` | Document Parsing \| Firecrawl | This document outlines Firecrawl's capabilities for parsing various file formats, including sprea... | document-parsing, data-extraction, file-conversion, pdf-processing |
| 019 | `019-features-fast-scraping.md` | Faster Scraping \| Firecrawl | This document explains how to optimize scraping performance using Firecrawl's caching mechanism a... | web-scraping, cache-management, performance-optimization, data-freshness |
| 020 | `020-features-enhanced-mode.md` | Enhanced Mode \| Firecrawl | This document explains the available proxy strategies for web scraping with Firecrawl, detailing ... | web-scraping, proxy-configuration, api-settings, firecrawl-integration |
| 021 | `021-features-change-tracking.md` | Change Tracking \| Firecrawl | This document explains how to use Firecrawl's change tracking feature to detect modifications, ad... | change-tracking, web-scraping, diff-analysis, data-monitoring |
| 022 | `022-features-proxies.md` | Proxies \| Firecrawl | This document explains how to configure proxy settings in Firecrawl, including choosing specific ... | firecrawl, web-scraping, proxy-configuration, scraping-reliability |
| 023 | `023-features-models.md` | Agent Models \| Firecrawl | This document provides a comparative guide to Firecrawl's Spark 1 Mini and Spark 1 Pro models, he... | firecrawl, data-extraction, model-selection, api-configuration |

### 4. SDKs & CLI (024-030)
*Official SDK documentation for Python, Node.js, Go, Java, Rust, and CLI*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 024 | `024-sdks-overview.md` | SDKs \| Firecrawl | This document serves as an introduction to the Firecrawl platform, highlighting its capabilities ... | web-scraping, data-extraction, web-crawling, developer-tools |
| 025 | `025-sdks-python.md` | Python SDK \| Firecrawl | This document provides a comprehensive guide on using the Firecrawl Python SDK to scrape, crawl, ... | python-sdk, web-scraping, web-crawling, data-extraction |
| 026 | `026-sdks-node.md` | Node SDK \| Firecrawl | This document provides a comprehensive guide to using the Firecrawl Node.js SDK for scraping webs... | firecrawl, web-scraping, web-crawling, node-js |
| 027 | `027-sdks-go.md` | Go SDK \| Firecrawl | This document provides instructions for installing and using the Firecrawl Go SDK to scrape, craw... | go-sdk, web-scraping, web-crawling, firecrawl |
| 028 | `028-sdks-java.md` | Java SDK \| Firecrawl | This document provides a guide for installing and utilizing the Firecrawl Java SDK, covering func... | java-sdk, web-scraping, api-integration, crawling |
| 029 | `029-sdks-rust.md` | Rust SDK \| Firecrawl | This document provides a guide for integrating and using the Firecrawl Rust SDK to perform web sc... | rust-sdk, web-scraping, web-crawling, data-extraction |
| 030 | `030-sdks-cli.md` | CLI \| Firecrawl | This document provides a comprehensive guide to installing, configuring, and utilizing the Firecr... | firecrawl, cli, web-scraping, automation |

### 5. LLM Framework Integration (031-040)
*Integration guides for LLM SDKs and AI frameworks*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 031 | `031-developer-guides-examples.md` | Full-Stack Templates | This document serves as an introductory portal for the Firecrawl platform, encouraging users to s... | web-scraping, data-extraction, firecrawl-platform, developer-tools |
| 032 | `032-developer-guides-llm-sdks-and-frameworks-openai.md` | OpenAI | This document provides a technical guide on integrating Firecrawl with OpenAI to perform web scra... | web-scraping, openai-integration, data-extraction, ai-agents |
| 033 | `033-developer-guides-llm-sdks-and-frameworks-anthropic.md` | Anthropic | This document provides instructions on integrating the Firecrawl web scraping API with Anthropic'... | web-scraping, ai-integration, structured-data-extraction, llm-tool-use |
| 034 | `034-developer-guides-llm-sdks-and-frameworks-gemini.md` | Gemini | This document provides a technical guide on integrating Firecrawl for web scraping with Google's ... | web-scraping, ai-integration, gemini-api, firecrawl |
| 035 | `035-developer-guides-llm-sdks-and-frameworks-langchain.md` | LangChain | This document provides a technical guide on integrating Firecrawl with LangChain to enable web da... | firecrawl, langchain, web-scraping, ai-development |
| 036 | `036-developer-guides-llm-sdks-and-frameworks-langgraph.md` | LangGraph | This document provides instructions on integrating Firecrawl with LangGraph to automate web scrap... | firecrawl, langgraph, web-scraping, ai-agents |
| 037 | `037-developer-guides-llm-sdks-and-frameworks-llamaindex.md` | LlamaIndex | This document provides a guide on integrating Firecrawl with LlamaIndex to fetch web content and ... | firecrawl, llamaindex, rag, vector-search |
| 038 | `038-developer-guides-llm-sdks-and-frameworks-mastra.md` | Mastra | This document provides a guide on integrating the Firecrawl web scraping tool with the Mastra Typ... | firecrawl, mastra, ai-agents, typescript |
| 039 | `039-developer-guides-llm-sdks-and-frameworks-google-adk.md` | Agent Development Kit (ADK) | This document explains how to integrate Firecrawl with Google's Agent Development Kit using the M... | firecrawl, google-adk, web-scraping, mcp |
| 040 | `040-developer-guides-llm-sdks-and-frameworks-vercel-ai-sdk.md` | Vercel AI SDK | This document provides integration instructions and usage examples for using Firecrawl tools with... | firecrawl, vercel-ai-sdk, web-scraping, ai-agents |

### 6. MCP Setup Guides (041-045)
*Setting up Firecrawl MCP server with various AI coding tools*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 041 | `041-developer-guides-mcp-setup-guides-claude-code.md` | MCP Web Search & Scrape in Claude Code | This document provides instructions for integrating the Firecrawl MCP server with Claude Code to ... | web-scraping, claude-code, mcp-server, firecrawl |
| 042 | `042-developer-guides-mcp-setup-guides-cursor.md` | MCP Web Search & Scrape in Cursor | This document provides instructions on how to integrate the Firecrawl MCP server into the Cursor ... | web-scraping, mcp-server, cursor-editor, api-integration |
| 043 | `043-developer-guides-mcp-setup-guides-windsurf.md` | MCP Web Search & Scrape in Windsurf | This document provides instructions on integrating the Firecrawl Model Context Protocol (MCP) ser... | windsurf, firecrawl, mcp-server, web-scraping |
| 044 | `044-developer-guides-mcp-setup-guides-chatgpt.md` | MCP Web Search & Scrape in ChatGPT | This document provides step-by-step instructions for integrating the Firecrawl MCP server with Ch... | firecrawl, mcp-server, web-scraping, chatgpt-integration |
| 045 | `045-developer-guides-mcp-setup-guides-factory-ai.md` | MCP Web Search & Scrape in Factory AI | This document provides instructions on integrating the Firecrawl Model Context Protocol (MCP) ser... | factory-ai, firecrawl, web-scraping, mcp-server |

### 7. Scraping Common Sites (046-049)
*Step-by-step guides for scraping popular websites*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 046 | `046-developer-guides-common-sites-amazon.md` | Scraping Amazon | This document provides a technical guide on using the Firecrawl SDK to extract, search, and crawl... | web-scraping, firecrawl, amazon-api, data-extraction |
| 047 | `047-developer-guides-common-sites-etsy.md` | Scraping Etsy | This document provides a guide on using the Firecrawl SDK to scrape, crawl, and map Etsy marketpl... | web-scraping, etsy-api, data-extraction, firecrawl |
| 048 | `048-developer-guides-common-sites-github.md` | Scraping GitHub | This document provides a comprehensive guide on utilizing Firecrawl to scrape, map, crawl, and ex... | web-scraping, github-integration, data-extraction, structured-data |
| 049 | `049-developer-guides-common-sites-wikipedia.md` | Scraping Wikipedia | This document provides a guide on using the Firecrawl SDK to extract, crawl, and search Wikipedia... | web-scraping, wikipedia-api, data-extraction, firecrawl |

### 8. Workflow Automation (050-053)
*Integration with workflow automation platforms*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 050 | `050-developer-guides-workflow-automation-zapier.md` | Firecrawl + Zapier | This document provides an overview of Firecrawl's automation capabilities, its primary data extra... | web-scraping, automation-tools, data-extraction, workflow-integration |
| 051 | `051-developer-guides-workflow-automation-make.md` | Firecrawl + Make | This document provides an overview of the Firecrawl integration for the Make automation platform,... | make-integration, firecrawl, automation-workflow, web-scraping |
| 052 | `052-developer-guides-workflow-automation-n8n.md` | Firecrawl + n8n | This guide provides step-by-step instructions for integrating Firecrawl with n8n to build automat... | web-scraping, workflow-automation, n8n, firecrawl |
| 053 | `053-developer-guides-workflow-automation-dify.md` | Firecrawl + Dify | This document outlines how to integrate the Firecrawl plugin into Dify to enable web scraping, cr... | dify-integration, firecrawl-plugin, web-scraping, llm-workflows |

### 9. Cookbooks & Usage Guides (054-057)
*Advanced usage guides, cookbooks, and specialized tools*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 054 | `054-developer-guides-usage-guides-choosing-the-data-extractor.md` | Choosing the Data Extractor \| Firecrawl | This document compares the three primary methods for structured data extraction in Firecrawl—agen... | web-scraping, data-extraction, firecrawl, autonomous-agents |
| 055 | `055-developer-guides-cookbooks-ai-research-assistant-cookbook.md` | Building an AI Research Assistant with Firecrawl and AI SDK | This document provides a technical walkthrough for building an AI-powered research assistant that... | ai-sdk, web-scraping, tool-calling, nextjs |
| 056 | `056-developer-guides-cookbooks-brand-style-guide-generator-cookbook.md` | Building a Brand Style Guide Generator with Firecrawl | This document provides a technical guide for building a Node.js application that uses Firecrawl's... | web-scraping, design-systems, pdf-generation, brand-identity |
| 057 | `057-developer-guides-openclaw.md` | Using OpenClaw with Firecrawl | This document provides instructions for integrating the Firecrawl CLI with AI agents to enable we... | web-scraping, ai-agents, browser-automation, cli-tools |

### 10. Use Cases (058-069)
*Real-world use cases and industry applications*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 058 | `058-use-cases-overview.md` | Use Cases | This document provides an overview of how various teams utilize the Firecrawl platform to enhance... | firecrawl, ai-applications, data-workflows, use-cases |
| 059 | `059-use-cases-ai-platforms.md` | AI Platforms | Firecrawl is a data transformation tool that converts website content into structured, AI-ready d... | web-scraping, ai-data-processing, rag-systems, knowledge-bases |
| 060 | `060-use-cases-deep-research.md` | Deep Research | This document outlines how to use Firecrawl to build automated research systems that search, scra... | web-scraping, data-aggregation, automated-research, llm-synthesis |
| 061 | `061-use-cases-developers-mcp.md` | Developers & MCP | This document explains how to integrate Firecrawl's Model Context Protocol (MCP) server with AI c... | web-scraping, model-context-protocol, ai-assistant, data-extraction |
| 062 | `062-use-cases-content-generation.md` | Content Generation | This document outlines how Firecrawl enables content teams to extract web data and visual assets ... | web-scraping, ai-content-generation, data-extraction, marketing-automation |
| 063 | `063-use-cases-lead-enrichment.md` | Lead Enrichment | This document outlines how sales and business development teams can utilize Firecrawl to automate... | lead-generation, sales-automation, crm-enrichment, web-scraping |
| 064 | `064-use-cases-competitive-intelligence.md` | Competitive Intelligence | This document outlines how to use Firecrawl for competitive intelligence monitoring, detailing th... | competitive-intelligence, web-scraping, market-monitoring, business-strategy |
| 065 | `065-use-cases-product-ecommerce.md` | Product & E-commerce | This document outlines how Firecrawl can be used by e-commerce teams to extract and structure pro... | e-commerce, data-extraction, web-scraping, competitor-monitoring |
| 066 | `066-use-cases-seo-platforms.md` | SEO Platforms | This document outlines how Firecrawl can be used by SEO platforms to audit website content and op... | seo-optimization, ai-readability, content-analysis, website-auditing |
| 067 | `067-use-cases-investment-finance.md` | Investment & Finance | This document outlines how to use Firecrawl to monitor market data, company metrics, and financia... | web-scraping, financial-data, market-intelligence, investment-research |
| 068 | `068-use-cases-data-migration.md` | Data Migration | This document outlines how to utilize Firecrawl for extracting website content, structure, and me... | data-migration, content-extraction, web-scraping, platform-migration |
| 069 | `069-use-cases-observability.md` | Observability & Monitoring | This document outlines how to utilize Firecrawl for website monitoring, covering synthetic testin... | website-monitoring, devops, sre, synthetic-monitoring |

### 11. Webhooks (070-073)
*Webhook configuration, events, security, and testing*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 070 | `070-webhooks-overview.md` | Webhooks \| Firecrawl | This document describes how to configure and utilize webhooks to receive real-time notifications ... | webhooks, api-integration, real-time-notifications, data-scraping |
| 071 | `071-webhooks-events.md` | Webhook Event Types \| Firecrawl | This document provides a comprehensive reference for webhook event types and their JSON payload s... | webhooks, api-reference, event-notifications, data-scraping |
| 072 | `072-webhooks-security.md` | Webhook Security \| Firecrawl | This document explains how to verify the authenticity of webhook requests from Firecrawl using HM... | webhook-security, hmac-sha256, signature-verification, data-integrity |
| 073 | `073-webhooks-testing.md` | Webhook Testing \| Firecrawl | This document provides instructions for exposing a local development server for webhook testing a... | webhooks, local-development, cloudflare-tunnels, signature-verification |

### 12. API Reference V2 - Core Endpoints (074-101)
*V2 API endpoint reference - scrape, crawl, map, search, extract, batch, agent, browser*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 074 | `074-api-reference-v2-introduction.md` | Introduction | This document provides the foundational technical information for integrating with the Firecrawl ... | web-scraping, api-documentation, authentication, rate-limiting |
| 075 | `075-api-reference-endpoint-scrape.md` | Scrape | This document defines the schema for a web scraping response, detailing the structure of extracte... | web-scraping, api-schema, data-extraction, json-structure |
| 076 | `076-api-reference-endpoint-crawl-post.md` | Crawl | This document defines the request structure for the Firecrawl v2 crawl API endpoint, including co... | web-scraping, crawl-api, data-extraction, firecrawl |
| 077 | `077-api-reference-endpoint-crawl-get.md` | Get Crawl Status | This document defines the schema for a JSON response containing web page content, including proce... | json-schema, web-scraping, data-extraction, api-response |
| 078 | `078-api-reference-endpoint-crawl-get-errors.md` | Get Crawl Errors | This document describes the API endpoint for retrieving error logs and details regarding failed U... | api-reference, crawl-job, error-handling, web-scraping |
| 079 | `079-api-reference-endpoint-crawl-delete.md` | Cancel Crawl | This document provides the API endpoint and authentication details for cancelling a specific craw... | api-endpoint, firecrawl, data-scraping, http-delete |
| 080 | `080-api-reference-endpoint-crawl-active.md` | Get Active Crawls | This document defines the schema for a web crawling configuration, detailing the parameters used ... | web-scraping, api-schema, data-extraction, crawler-configuration |
| 081 | `081-api-reference-endpoint-crawl-params-preview.md` | Crawl Params Preview | This document defines the JSON structure and available configuration parameters for specifying cr... | crawler-configuration, web-scraping, api-schema, data-extraction-settings |
| 082 | `082-api-reference-endpoint-map.md` | Map | This document describes the parameters and authentication requirements for mapping multiple URLs ... | url-mapping, web-crawling, api-documentation, sitemap-configuration |
| 083 | `083-api-reference-endpoint-search.md` | Search | This document provides a technical overview and parameter reference for the Firecrawl search endp... | api-reference, web-scraping, search-engine, data-extraction |
| 084 | `084-api-reference-endpoint-extract.md` | Extract | This document provides the API request structure and parameter schema for the Firecrawl v2 extrac... | api-request, data-extraction, web-scraping, http-post |
| 085 | `085-api-reference-endpoint-extract-get.md` | Get Extract Status | This document provides the API specification for retrieving the current status and token usage of... | api-reference, extract-job, status-check, token-usage |
| 086 | `086-api-reference-endpoint-batch-scrape.md` | Batch Scrape | This document provides the API specification for performing batch web scraping tasks, including c... | web-scraping, api-documentation, data-extraction, batch-processing |
| 087 | `087-api-reference-endpoint-batch-scrape-get.md` | Get Batch Scrape Status | This document defines the JSON structure for a web scraping or content extraction API response, d... | api-schema, data-extraction, json-response, web-scraping |
| 088 | `088-api-reference-endpoint-batch-scrape-get-errors.md` | Get Batch Scrape Errors | This document provides the API specification for retrieving error information and blocked URL det... | batch-scrape, error-handling, api-documentation, scrape-job |
| 089 | `089-api-reference-endpoint-batch-scrape-delete.md` | Cancel Batch Scrape | This document provides instructions on how to cancel a previously initiated batch scraping job us... | api-reference, batch-scraping, job-cancellation, rest-api |
| 090 | `090-api-reference-endpoint-agent.md` | Agent | This document provides the API specifications for initiating an agentic data extraction task, det... | api-reference, data-extraction, agentic-workflow, firecrawl-api |
| 091 | `091-api-reference-endpoint-agent-get.md` | Get Agent Status | This document describes the API endpoint for retrieving the current status, model configuration, ... | api-reference, agent-job, status-check, job-monitoring |
| 092 | `092-api-reference-endpoint-agent-delete.md` | Cancel Agent | Provides the API endpoint and authorization requirements for canceling an active agent job within... | api-request, job-management, firecrawl-api, delete-request |
| 093 | `093-api-reference-endpoint-browser-create.md` | Create Browser Session | This document provides the API specifications for initiating a managed browser session, including... | api-reference, browser-automation, session-management, http-requests |
| 094 | `094-api-reference-endpoint-browser-execute.md` | Execute Browser Code | This document defines the API endpoint for executing arbitrary code within a sandboxed browser en... | api-reference, code-execution, browser-automation, firecrawl-api |
| 095 | `095-api-reference-endpoint-browser-list.md` | List Browser Sessions | This document provides the API specification for retrieving browser session details, including co... | api-reference, browser-sessions, rest-api, authentication |
| 096 | `096-api-reference-endpoint-browser-delete.md` | Delete Browser Session | This document provides the API specification for terminating an active browser session using a un... | api-reference, session-management, firecrawl, delete-request |
| 097 | `097-api-reference-endpoint-queue-status.md` | Queue Status | This document provides an overview of the scrape queue metrics available for team accounts, inclu... | scrape-queue, metrics-api, job-monitoring, concurrency-limits |
| 098 | `098-api-reference-endpoint-credit-usage.md` | Credit Usage | This document provides the API endpoint details and authentication requirements for retrieving th... | api-reference, credit-usage, billing-information, team-management |
| 099 | `099-api-reference-endpoint-credit-usage-historical.md` | Historical Credit Usage | This endpoint retrieves historical credit usage data for an authenticated team, providing a break... | api-reference, credit-usage, billing-analytics, authentication |
| 100 | `100-api-reference-endpoint-token-usage.md` | Token Usage | This document describes the API endpoint for retrieving the remaining credit and token usage for ... | api-endpoint, token-usage, billing-management, firecrawl-api |
| 101 | `101-api-reference-endpoint-token-usage-historical.md` | Historical Token Usage | This endpoint retrieves historical token consumption data for an authenticated team, organized by... | api-endpoint, token-usage, billing-metrics, historical-data |

### 13. API Reference V2 - Webhook Events (102-112)
*V2 API webhook event payload specifications*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 102 | `102-api-reference-endpoint-webhook-crawl-started.md` | Crawl Started | This document defines the schema and security requirements for webhook event notifications, speci... | webhook-delivery, hmac-signature, event-schema, api-integration |
| 103 | `103-api-reference-endpoint-webhook-crawl-page.md` | Crawl Page | This document represents a JSON-formatted response structure from a web crawling service, providi... | web-scraping, json-schema, data-extraction, crawl-service |
| 104 | `104-api-reference-endpoint-webhook-crawl-completed.md` | Crawl Completed | This document outlines the structure and expected response for webhook event deliveries, includin... | webhook-delivery, security-headers, event-payload, api-integration |
| 105 | `105-api-reference-endpoint-webhook-batch-scrape-started.md` | Batch Scrape Started | This document specifies the structure, security requirements, and expected response format for ha... | webhook, hmac-sha256, data-delivery, api-integration |
| 106 | `106-api-reference-endpoint-webhook-batch-scrape-page.md` | Batch Scrape Page | This document outlines the JSON schema and data structure for a batch web scraping response, deta... | web-scraping, data-extraction, json-schema, api-response |
| 107 | `107-api-reference-endpoint-webhook-batch-scrape-completed.md` | Batch Scrape Completed | This document outlines the structure and signature requirements for receiving and verifying webho... | webhooks, api-security, hmac-sha256, data-delivery |
| 108 | `108-api-reference-endpoint-webhook-agent-started.md` | Agent Started | This document specifies the structure and security verification requirements for receiving and ac... | webhook-security, hmac-signature, event-delivery, data-payload |
| 109 | `109-api-reference-endpoint-webhook-agent-action.md` | Agent Action | This document specifies the structure and security requirements for handling incoming webhook eve... | webhook-delivery, hmac-security, api-integration, request-payload |
| 110 | `110-api-reference-endpoint-webhook-agent-completed.md` | Agent Completed | This document specifies the structure and security requirements for webhook events, including hea... | webhook-security, hmac-sha256, data-delivery, api-integration |
| 111 | `111-api-reference-endpoint-webhook-agent-failed.md` | Agent Failed | This document outlines the expected headers, body parameters, and response requirements for webho... | webhooks, api-integration, security-headers, event-notifications |
| 112 | `112-api-reference-endpoint-webhook-agent-cancelled.md` | Agent Cancelled | This document defines the structure and authentication requirements for webhook notifications tri... | webhooks, api-documentation, event-notification, agent-cancellation |

### 14. API Reference V1 (Legacy) (113-132)
*V1 API endpoint reference (legacy version)*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 113 | `113-v1-api-reference-introduction.md` | Introduction | This document provides the foundational technical information for interacting with the Firecrawl ... | api-authentication, rate-limiting, http-status-codes, developer-documentation |
| 114 | `114-api-reference-v1-endpoint-scrape.md` | Scrape | This document provides the API specifications and request parameters for scraping web pages, incl... | web-scraping, api-documentation, data-extraction, proxy-configuration |
| 115 | `115-api-reference-v1-endpoint-crawl-post.md` | Crawl | This document provides the API request structure and parameter schema for initiating a web crawl ... | api-request, web-scraping, crawl-configuration, data-extraction |
| 116 | `116-api-reference-v1-endpoint-crawl-get.md` | Get Crawl Status | This document defines the schema for a JSON response containing processed web content, including ... | json-schema, data-structure, web-scraping, api-response |
| 117 | `117-api-reference-v1-endpoint-crawl-get-errors.md` | Get Crawl Errors | This document describes the API endpoint used to retrieve a list of failed URLs and specific erro... | api-endpoint, crawl-job, error-reporting, web-scraping |
| 118 | `118-api-reference-v1-endpoint-crawl-delete.md` | Cancel Crawl | This document provides the API endpoint and authentication requirements for cancelling an active ... | api-reference, crawl-service, bearer-authentication, delete-endpoint |
| 119 | `119-api-reference-v1-endpoint-crawl-active.md` | Get Active Crawls | This document defines the schema structure for a web crawling and scraping request, detailing con... | web-scraping, api-schema, data-extraction, json-config |
| 120 | `120-api-reference-v1-endpoint-map.md` | Map | This document provides the API specifications for mapping multiple URLs using specific search par... | api-reference, url-mapping, web-crawling, http-request |
| 121 | `121-api-reference-v1-endpoint-search.md` | Search | This document describes the search API endpoint, which allows users to perform web searches and s... | web-search, scraping, api-documentation, data-extraction |
| 122 | `122-api-reference-v1-endpoint-extract.md` | Extract | This document provides the API request structure and parameters for the Firecrawl extraction endp... | web-scraping, data-extraction, api-request, firecrawl-api |
| 123 | `123-api-reference-v1-endpoint-extract-get.md` | Get Extract Status | This document describes the API endpoint used to retrieve the current processing status and detai... | api-endpoint, job-status, data-extraction, firecrawl-api |
| 124 | `124-api-reference-v1-endpoint-batch-scrape.md` | Batch Scrape | This document provides the API request structure for initiating a batch web scraping operation us... | batch-scraping, api-request, data-extraction, web-crawling |
| 125 | `125-api-reference-v1-endpoint-batch-scrape-get.md` | Get Batch Scrape Status | This document defines the schema structure for a web scraping or content extraction API response,... | api-schema, data-extraction, json-response, web-scraping |
| 126 | `126-api-reference-v1-endpoint-batch-scrape-get-errors.md` | Get Batch Scrape Errors | This document describes the API endpoint used to retrieve error details and blocked URLs associat... | api-reference, batch-scraping, error-reporting, job-status |
| 127 | `127-api-reference-v1-endpoint-batch-scrape-delete.md` | Cancel Batch Scrape | This document provides the API endpoint and authentication requirements for cancelling a pending ... | api-reference, batch-scraping, job-cancellation, rest-api |
| 128 | `128-api-reference-v1-endpoint-queue-status.md` | Queue Status | This document provides the API specification for retrieving status metrics related to a team's we... | api-reference, scrape-queue, metrics, job-tracking |
| 129 | `129-api-reference-v1-endpoint-credit-usage.md` | Credit Usage | This document describes the API endpoint for retrieving the current credit usage, plan limits, an... | api-endpoint, credit-usage, billing-information, bearer-authentication |
| 130 | `130-api-reference-v1-endpoint-credit-usage-historical.md` | Historical Credit Usage | This endpoint retrieves the historical credit consumption data for an authenticated team, providi... | credit-usage, api-endpoint, billing-data, historical-metrics |
| 131 | `131-api-reference-v1-endpoint-token-usage.md` | Token Usage | This document provides the API specification for retrieving the current token usage and billing c... | api-endpoint, token-usage, authentication, billing-data |
| 132 | `132-api-reference-v1-endpoint-token-usage-historical.md` | Historical Token Usage | This endpoint retrieves historical token consumption data for an authenticated team, providing us... | api-endpoint, token-usage, historical-data, team-analytics |

### 15. Contributing & Self-Hosting (133-135)
*Contribution guidelines, open source vs cloud, and self-hosting setup*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 133 | `133-contributing-guide.md` | Running Locally \| Firecrawl | This document provides instructions for setting up and running the Firecrawl API server locally, ... | firecrawl, local-development, api-setup, docker |
| 134 | `134-contributing-open-source-or-cloud.md` | Open Source vs Cloud \| Firecrawl | This document outlines the differences between the open-source Firecrawl engine and the managed F... | firecrawl, web-scraping, open-source, cloud-services |
| 135 | `135-contributing-self-host.md` | Self-hosting \| Firecrawl | This document provides a guide for self-hosting Firecrawl, including installation steps, environm... | self-hosting, docker, environment-variables, setup-guide |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-003 |
| **Configuration** | 004-007 |
| **Core Features** | 008-023 |
| **SDKs** | 024-030 |
| **LLM Integrations** | 031-040 |
| **MCP Setup** | 041-045 |
| **Site-Specific Guides** | 046-049 |
| **Automation** | 050-053 |
| **Cookbooks** | 054-057 |
| **Use Cases** | 058-069 |
| **Webhooks** | 070-073 |
| **API V2 Endpoints** | 074-101 |
| **API V2 Webhook Events** | 102-112 |
| **API V1 (Legacy)** | 113-132 |
| **Contributing** | 133-135 |

### By Concept

| Concept | Files |
|---------|-------|
| **Web Scraping** | 008, 014, 019, 074-101 |
| **Web Crawling** | 009, 074-101 |
| **Data Extraction** | 012, 013, 074-101 |
| **AI Agents** | 015, 016, 031-040 |
| **Browser Automation** | 017, 074-101 |
| **Search** | 011, 074-101 |
| **Site Mapping** | 010, 074-101 |
| **Batch Processing** | 014, 074-101 |
| **Webhooks & Events** | 070-073, 102-112 |
| **Authentication** | 074, 070 |
| **Rate Limiting** | 004 |
| **Billing & Credits** | 003, 074-101 |
| **Proxy Configuration** | 022 |
| **Document Parsing** | 018 |
| **Change Tracking** | 021 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-003** for introduction, dashboard overview, and billing
- Review files **004-007** for rate limits, MCP setup, migration, and advanced config

### Level 2: Core Understanding
- Learn core features from files **008-023** (scrape, crawl, map, search, extract, agent, browser, etc.)
- Set up your preferred SDK from files **024-030** (Python, Node.js, Go, Java, Rust, CLI)

### Level 3: Practical Application
- Integrate with LLM frameworks using files **031-040** (OpenAI, Anthropic, LangChain, etc.)
- Set up MCP for AI coding tools with files **041-045** (Claude Code, Cursor, Windsurf)
- Follow site-specific guides in files **046-049** (Amazon, Etsy, GitHub, Wikipedia)

### Level 4: Advanced Usage
- Configure workflow automation with files **050-053** (Zapier, Make, n8n, Dify)
- Explore cookbooks and usage guides in files **054-057**
- Review real-world use cases in files **058-069**

### Level 5: Integration & Events
- Set up webhooks with files **070-073**
- Consult API V2 reference in files **074-112**
- Reference legacy V1 API in files **113-132** (if needed)

### Level 6: Contributing
- Learn how to contribute with files **133-135**

---

## Translation Files

Each English document has translations available with language prefix:
- Spanish: `es-{filename}` (135 files)
- French: `fr-{filename}` (135 files)
- Japanese: `ja-{filename}` (135 files)
- Portuguese-BR: `pt-BR-{filename}` (135 files)
- Chinese: `zh-{filename}` (135 files)

Example: `001-introduction.md` has translations at `es-001-introduction.md`, `fr-001-introduction.md`, etc.

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the Firecrawl documentation structure.*
