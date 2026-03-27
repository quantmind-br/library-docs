---
title: Using OpenClaw with Firecrawl
url: https://docs.firecrawl.dev/developer-guides/openclaw
source: sitemap
fetched_at: 2026-03-23T07:33:44.096242-03:00
rendered_js: false
word_count: 321
summary: This document provides instructions for integrating the Firecrawl CLI with AI agents to enable web scraping, searching, and browser automation within isolated remote sandboxes.
tags:
    - web-scraping
    - ai-agents
    - browser-automation
    - cli-tools
    - remote-sandbox
    - data-extraction
category: guide
---

Integrate Firecrawl with OpenClaw to give your agents the ability to scrape, search, crawl, extract, and interact with the web — all through the [Firecrawl CLI](https://docs.firecrawl.dev/sdks/cli).

- **No local browser needed** — every session runs in a remote, isolated sandbox. No Chromium installs, no driver conflicts, no RAM pressure on your machine.
- **Real parallelism** — run many browser sessions at once without local resource fights. Agents can browse in batches across multiple sites simultaneously.
- **Secure by default** — navigation, DOM evaluation, and extraction all happen inside disposable sandboxes, not on your workstation.
- **Better token economics** — agents get back clean artifacts (snapshots, extracted fields) instead of hauling giant DOMs and driver logs into the context window.
- **Full web toolkit** — scrape, search, and browser automation all through a single CLI that your agent already knows how to use.

## Setup

Tell your agent to install the Firecrawl CLI, authenticate and initialize the skill with this command:

```
npx -y firecrawl-cli init --browser --all
```

- `--all` installs the Firecrawl skill to every detected AI coding agent
- `--browser` opens the browser for Firecrawl authentication automatically

or install everything seperately:

```
npm install -g firecrawl-cli
firecrawl init skills
firecrawl login --browser
# Or, skip the browser and provide your API key directly:
export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"
```

Verify everything is set up correctly:

## Scrape

Scrape a single page and extract its content:

```
firecrawl https://example.com --only-main-content
```

Get specific formats:

```
firecrawl https://example.com --format markdown,links --pretty
```

## Search

Search the web and optionally scrape the results:

```
firecrawl search "latest AI funding rounds 2025" --limit 10

# Search and scrape the results
firecrawl search "OpenClaw documentation" --scrape --scrape-formats markdown
```

## Browser

Launch a remote browser session for interactive automation. Each session runs in an isolated sandbox — no local Chromium install required. `agent-browser` is pre-installed with 40+ commands.

```
# Shorthand: auto-launches a session if none is active
firecrawl browser "open https://news.ycombinator.com"
firecrawl browser "snapshot"
firecrawl browser "scrape"
firecrawl browser close
```

Interact with page elements using refs from the snapshot:

```
firecrawl browser "open https://example.com"
firecrawl browser "snapshot"
# snapshot returns @ref IDs — use them to interact
firecrawl browser "click @e5"
firecrawl browser "fill @e3 'search query'"
firecrawl browser "scrape"
firecrawl browser close
```

## Example: tell your agent

Here are some prompts you can give your OpenClaw agent:

- *“Use Firecrawl to scrape [https://example.com](https://example.com) and summarize the main content.”*
- *“Search for the latest OpenAI news and give me a summary of the top 5 results.”*
- *“Use Firecrawl Browser to open Hacker News, get the top 5 stories, and the first 10 comments on each.”*
- *“Crawl the docs at [https://docs.firecrawl.dev](https://docs.firecrawl.dev) and save them to a file.”*

## Further reading

- [Firecrawl CLI reference](https://docs.firecrawl.dev/sdks/cli)
- [Browser Sandbox docs](https://docs.firecrawl.dev/features/browser)
- [Agent docs](https://docs.firecrawl.dev/features/agent)