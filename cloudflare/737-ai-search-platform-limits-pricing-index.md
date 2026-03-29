---
title: Limits & pricing · Cloudflare AI Search docs
url: https://developers.cloudflare.com/ai-search/platform/limits-pricing/index.md
source: llms
fetched_at: 2026-01-24T15:06:48.592684364-03:00
rendered_js: false
word_count: 223
summary: This document outlines the pricing model and operational limits for Cloudflare AI Search during its open beta phase, including billing details for underlying infrastructure services.
tags:
    - cloudflare-ai-search
    - pricing
    - limits
    - beta
    - billing
category: reference
---

## Pricing

During the open beta, AI Search is **free to enable**. When you create an AI Search instance, it provisions and runs on top of Cloudflare services in your account. These resources are **billed as part of your Cloudflare usage**, and includes:

| Service & Pricing | Description |
| - | - |
| [**R2**](https://developers.cloudflare.com/r2/pricing/) | Stores your source data |
| [**Vectorize**](https://developers.cloudflare.com/vectorize/platform/pricing/) | Stores vector embeddings and powers semantic search |
| [**Workers AI**](https://developers.cloudflare.com/workers-ai/platform/pricing/) | Handles image-to-Markdown conversion, embedding, query rewriting, and response generation |
| [**AI Gateway**](https://developers.cloudflare.com/ai-gateway/reference/pricing/) | Monitors and controls model usage |
| [**Browser Rendering**](https://developers.cloudflare.com/browser-rendering/pricing/) | Loads dynamic JavaScript content during [website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/) crawling with the Render option |

For more information about how each resource is used within AI Search, reference [How AI Search works](https://developers.cloudflare.com/ai-search/concepts/how-ai-search-works/).

## Limits

The following limits currently apply to AI Search during the open beta:

Need a higher limit?

To request an adjustment to a limit, complete the [Limit Increase Request Form](https://forms.gle/wnizxrEUW33Y15CT8). If the limit can be increased, Cloudflare will contact you with next steps.

| Limit | Value |
| - | - |
| Max AI Search instances per account | 10 |
| Max files per AI Search | 100,000 |
| Max file size | 4 MB |

These limits are subject to change as AI Search evolves beyond open beta.