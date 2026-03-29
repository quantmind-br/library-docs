---
title: Daily News Briefing | AI-Powered News Summaries for Obsidian
url: https://docs.perplexity.ai/docs/cookbook/showcase/daily-news-briefing.md
source: llms
fetched_at: 2026-02-04T07:21:49.513038081-03:00
rendered_js: false
word_count: 414
summary: This document describes the Daily News Briefing Obsidian plugin, explaining how to install and configure it to deliver AI-powered news summaries using the Perplexity Sonar API.
tags:
    - obsidian-plugin
    - perplexity-api
    - news-summarization
    - knowledge-management
    - automation
    - sonar-api
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Daily News Briefing | AI-Powered News Summaries for Obsidian

> An Obsidian plugin that delivers AI-powered daily news summaries directly to your vault using Perplexity's Sonar API for intelligent content curation

**Daily News Briefing** is an Obsidian plugin that delivers AI-powered news summaries directly to your vault. Stay informed about your topics of interest with smart, automated news collection and summarization using Perplexity's Sonar API for intelligent content curation.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/nbbisoqsZDc" title="Daily News Briefing Demo" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Features

* **Personalized News Collection** based on your topics of interest and preferences
* **AI-Powered Summarization** of news articles using Perplexity Sonar API
* **Automated Daily Briefings** delivered directly to your Obsidian vault
* **Customizable Delivery Schedule** and format options
* **Seamless Obsidian Integration** with your existing knowledge management workflow
* **Trusted Source Filtering** to ensure quality and reliability
* **Markdown Formatting** for easy linking and organization within your vault

## Prerequisites

* Obsidian desktop app installed
* Perplexity API key (Sonar API access)
* Internet connection for fetching news articles
* TypeScript development environment (for customization)

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/ChenziqiAdam/Daily-News-Briefing.git
cd Daily-News-Briefing

# Install dependencies
npm install

# Build the plugin
npm run build
```

## Configuration

1. **Install Plugin**: Copy the built plugin to your Obsidian plugins folder
2. **Enable Plugin**: Activate in Obsidian settings
3. **API Setup**: Enter your Perplexity API key in plugin settings
4. **Configure Topics**: Set up your news topics and delivery preferences

## Usage

1. **Configure Interests**: Set up preferred topics, sources, and delivery schedule
2. **Automated Collection**: Plugin uses Perplexity Sonar API to gather latest news
3. **AI Summarization**: Articles are processed and summarized using Perplexity's capabilities
4. **Vault Delivery**: Summaries are formatted as Markdown notes in your Obsidian vault
5. **Knowledge Integration**: Link news briefings with other notes in your knowledge base

## Code Explanation

* **Frontend**: TypeScript-based Obsidian plugin with custom UI components
* **AI Integration**: Perplexity Sonar API for intelligent news gathering and summarization
* **Content Processing**: Automated article extraction and summarization workflows
* **Scheduling**: Configurable delivery schedules and topic monitoring
* **Markdown Generation**: Structured content formatting for Obsidian compatibility
* **Error Handling**: Robust error management for API limits and network issues

## Technical Implementation

The plugin leverages Perplexity Sonar API for:

```typescript  theme={null}
// News gathering with Perplexity Sonar API
const newsQuery = `latest news about ${topic} in the past 24 hours`;
const searchResponse = await perplexityClient.search({
  query: newsQuery,
  max_results: 5,
  include_domains: userPreferences.trustedSources || []
});

// AI-powered summarization
const summaryPrompt = `Summarize these news articles about ${topic}`;
const summaryResponse = await perplexityClient.generate({
  prompt: summaryPrompt,
  model: "sonar-medium-online",
  max_tokens: 500
});
```

## Links

* [GitHub Repository](https://github.com/ChenziqiAdam/Daily-News-Briefing)