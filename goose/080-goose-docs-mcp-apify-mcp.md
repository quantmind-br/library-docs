---
title: Apify Extension | goose
url: https://block.github.io/goose/docs/mcp/apify-mcp
source: github_pages
fetched_at: 2026-01-22T22:14:40.405116746-03:00
rendered_js: true
word_count: 110
summary: This document explains how to integrate the Apify MCP server with the goose extension to perform web scraping and data extraction using Apify Actors.
tags:
    - apify
    - mcp-server
    - goose-extension
    - web-scraping
    - data-extraction
    - ai-tools
category: tutorial
---

This tutorial covers how to add the [Apify MCP server](https://mcp.apify.com) as a goose extension, enabling goose to call thousands of tools from [Apify Store](https://apify.com/store) to extract data from social media, e-commerce sites, search engines, online maps, or any other website.

The Apify MCP server lets you connect goose to [Apify Store](https://apify.com/store), a marketplace of thousands of ready-made tools (called *Actors*) for all kinds of web scraping, crawling, and data extraction use cases. Learn more about Apify Actors in the [official documentation](https://docs.apify.com/platform/actors)

In this example, goose will use the [Google Places Scraper](https://apify.com/compass/crawler-google-places) Actor to identify the most credible, top-rated Italian restaurant in Prague based on public ratings, reviews, and fine-dining recognition.

```

( O)> Find the top-rated Italian restaurant in Prague with verifiable credibility — use Apify MCP to find Google Maps review scraper Actor, focus on places with at least 200+ reviews, an average rating of 4.7 or higher on Google, TripAdvisor, or OpenTable, and any Michelin or fine-dining recognition. Include the restaurant’s name, rating, total review count, address, cuisine style, and a short summary of what makes it stand out (e.g., service, ambiance, or signature dishes). Return to me only 1 restaurant with the highest rating to review count ratio

```

```

Based on the gathered information, the top-rated Italian restaurant in Prague with verifiable credibility is:

### **Al Tagliere**

* **Rating:** 4.7/5
* **Total Reviews:** 457
* **Address:** [Al Tagliere on TripAdvisor](https://www.tripadvisor.com/Restaurant_Review-g274707-d6835155-Reviews-Al_Tagliere-Prague_Bohemia.html)
* **Cuisine Style:** Italian
* **Summary:** Al Tagliere is celebrated for its authentic Italian dishes that showcase regional flavors. The restaurant is known for its delightful ambiance, attentive service, and signature dishes such as homemade pasta and traditional desserts. Patrons frequently highlight the freshness of ingredients and the welcoming atmosphere, making it a preferred choice for both locals and tourists.

This restaurant has a strong reputation and meets your criteria for quality and credibility.

```