---
title: NLWeb · Cloudflare AI Search docs
url: https://developers.cloudflare.com/ai-search/how-to/nlweb/index.md
source: llms
fetched_at: 2026-01-24T14:00:38.072358767-03:00
rendered_js: false
word_count: 622
summary: This document explains how to enable conversational search on a website using Cloudflare AI Search and the NLWeb protocol to serve natural language queries to users and AI agents.
tags:
    - cloudflare-ai-search
    - nlweb
    - conversational-search
    - cloudflare-workers
    - model-context-protocol
    - website-indexing
category: tutorial
---

Enable conversational search on your website with NLWeb and Cloudflare AI Search. This template crawls your site, indexes the content, and deploys NLWeb-standard endpoints to serve both people and AI agents.

Note

This is a public preview ideal for experimentation. If you're interested in running this in production workflows, please contact us at <nlweb@cloudflare.com>.

## What is NLWeb

[NLWeb](https://github.com/nlweb-ai/NLWeb) is an open project developed by Microsoft that defines a standard protocol for natural language queries on websites. Its goal is to make every website as accessible and interactive as a conversational AI app, so both people and AI agents can reliably query site content. It does this by exposing two key endpoints:

* `/ask`: Conversational endpoint for user queries
* `/mcp`: Structured Model Context Protocol (MCP) endpoint for AI agents

## How to use it

You can deploy NLWeb on your website directly through the AI Search dashboard:

1. Log in to your [Cloudflare dashboard](https://dash.cloudflare.com/).
2. Go to **Compute & AI** > **AI Search**.
3. Select **Create AI Search**, then choose the **NLWeb Website** option.
4. Select your domain from your Cloudflare account.
5. Click **Start indexing**.

Once complete, AI Search will crawl and index your site, then deploy an NLWeb Worker for you.

## What this template includes

Choosing the NLWeb Website option extends a normal AI Search by tailoring it for content‑heavy websites and giving you everything that is required to adopt NLWeb as the standard for conversational search on your site. Specifically, the template provides:

* **Website as a data source:** Uses [Website](https://developers.cloudflare.com/ai-search/configuration/data-source/website/) as data source option to crawl and ingest pages with the Rendered Sites option.
* **Defaults for content-heavy websites:** Applies tuned embedding and retrieval configurations ideal for publishing and content‑rich websites.
* **NLWeb Worker deployment:** Automatically spins up a Cloudflare Worker from the [NLWeb Worker template](https://github.com/cloudflare/templates).

## What the Worker includes

Your deployed Worker provides two endpoints:

* `/ask` — NLWeb’s standard conversational endpoint

  * Powers the conversational UI at the root (`/`)
  * Powers the embeddable preview widget (`/snippet.html`)

* `/mcp` — NLWeb’s MCP server endpoint for trusted AI agents

These endpoints give both people and agents structured access to your content.

## Using It on Your Website

To integrate NLWeb search directly into your site you can:

1. Find your deployed Worker in the [Cloudflare dashboard](https://dash.cloudflare.com/):

* Go to **Compute & AI** > **AI Search**.
* Select **Connect**, then go to the **NLWeb** tab.
* Select **Go to Worker**.

1. Add a [custom domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) to your Worker (for example, ask.example.com)
2. Use the `/ask` endpoint on your custom domain to power the search (for example, ask.example.com/ask)

You can also use the embeddable snippet to add a search UI directly into your website. For example:

```html
<!-- Add css on head -->
    <link rel="stylesheet" href="https://ask.example.com/nlweb-dropdown-chat.css">
    <link rel="stylesheet" href="https://ask.example.com/common-chat-styles.css">


    <!-- Add container on body -->
    <div id="docs-search-container"></div>


    <!-- Include JavaScript -->
    <script type="module">
      import { NLWebDropdownChat } from 'https://ask.example.com/nlweb-dropdown-chat.js';


      const chat = new NLWebDropdownChat({
        containerId: 'docs-search-container',
        site: 'https://ask.example.com',
        placeholder: 'Search for docs...',
        endpoint: 'https://ask.example.com'
      });
    </script>
```

This lets you serve conversational AI search directly from your own domain, with control over how people and agents access your content.

## Modifying or updating the Worker

You may want to customize your Worker, for example, to adjust the UI for the embeddable snippet. In those cases, we recommend calling the `/ask` endpoint for queries and building your own UI on top of it, however, you may also choose to modify the Worker's code for the embeddable UI.

If the NLWeb standard is updated, you can update your Worker to stay compatible and recieve the latest updates.

The simplest way to apply changes or updates is to redeploy the Worker template:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/nlweb-template)

To do so:

1. Select the **Deploy to Cloudflare** button from above to deploy the Worker template to your Cloudflare account.
2. Enter the name of your AI Search in the `RAG_ID` environment variable field.
3. Click **Deploy**.
4. Select the **GitHub/GitLab** icon on the Workers Dashboard.
5. Clone the repository that is created for your Worker.
6. Make your modifications, then commit and push changes to the repository to update your Worker.

Now you can use this Worker as the new NLWeb endpoint for your website.