---
title: Tavily Web Search Extension | goose
url: https://block.github.io/goose/docs/mcp/tavily-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:56.932913916-03:00
rendered_js: true
word_count: 164
summary: This tutorial explains how to integrate the Tavily Web Search MCP server as an extension for goose Desktop and CLI to enable AI-powered web searching. It covers the required environment variables, installation steps, and provides examples of using search capabilities within goose.
tags:
    - goose-ai
    - tavily-search
    - mcp-server
    - web-search
    - extension-configuration
    - api-integration
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

This tutorial covers how to add the [Tavily Web Search MCP Server](https://github.com/tavily-ai/tavily-mcp) as a goose extension to enable AI-powered web search functionality.

TLDR

- goose Desktop
- goose CLI

**Environment Variable**

```
TAVILY_API_KEY: <YOUR_API_KEY>
```

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [uv](https://docs.astral.sh/uv/#installation) installed on your system to run this command, as it uses `uvx`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=-y&arg=tavily-mcp&id=tavily&name=Tavily%20Web%20Search&description=Search%20the%20web%20with%20Tavily%20MCP&env=TAVILY_API_KEY%3DTavily%20API%20Key)
2. Click `Yes` to confirm the installation
3. Get your [Tavily API Key](https://tavily.com/) and paste it in
4. Click `Add Extension`
5. Click the button in the top-left to open the sidebar
6. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

The Tavily MCP server enables AI-powered web search functionality in your goose interactions. When you obtain your API key, you'll have access to Tavily's advanced search capabilities including:

1. Real-time web search
2. Structured data extraction
3. Content analysis
4. Topic-specific search

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

```
Search for recent news about artificial intelligence breakthroughs in medicine and summarize the key findings.
```

### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll use the Tavily news search tool to find recent news about AI breakthroughs in medicine.

─── tavily_news_search | tavily ──────────────────────────
max_results: 5
query: ...


Let me summarize the key findings from the recent news about AI in medicine:

1. Personalized AI-Driven Healthcare:
- Development of AI systems that act as "personal doctors" that work alongside human clinicians rather than replacing them
- Focus on augmenting clinical capabilities while maintaining human oversight

2. Breakthrough in Medical Imaging:
- A significant advancement in CT scan analysis has been reported in Nature
- Development of a "Unified total-body CT image" (Uni-CT) algorithm that:
  - Automatically generates single series of total-body CT images
  - Concatenates multiple images of segmented organs using organ-specific window settings
  - Reduces diagnosis time by 35% without compromising accuracy
  - Improves efficiency in trauma cases

3. Future Trends:
- Movement toward democratized AI in healthcare, potentially reducing the gap between large and small healthcare providers
- Development of hyper-personalized medical experiences powered by AI
- Integration of AI systems that can perform human-like reasoning in medical contexts

The most concrete breakthrough appears to be in medical imaging, with the Uni-CT algorithm showing promising results in improving both the speed and accuracy of trauma diagnosis. This represents a practical application of AI that could have immediate benefits in emergency medicine.

Would you like me to search for more specific information about any of these developments or explore other areas of AI in medicine?
```

tip

You can adjust the [search parameters](https://github.com/tavily-ai/tavily-mcp#tavily-search-examples) for different types of queries and depths of information. The extension supports both quick searches and comprehensive research.