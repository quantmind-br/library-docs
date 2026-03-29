---
title: Sonar Chromium Browser | Native Search Omnibox and Context Menu
url: https://docs.perplexity.ai/docs/cookbook/showcase/sonar-chromium-browser.md
source: llms
fetched_at: 2026-02-04T07:22:37.982602098-03:00
rendered_js: false
word_count: 306
summary: This document describes the Sonar Chromium Browser patch, which integrates Perplexity's Sonar API into Chromium for native AI-powered omnibox answers and context-menu summarization.
tags:
    - chromium
    - perplexity-api
    - browser-integration
    - ai-summarization
    - omnibox-search
    - sonar-model
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Sonar Chromium Browser | Native Search Omnibox and Context Menu

> Chromium browser patch with native Perplexity Sonar API integration providing omnibox answers and context-menu summarization

**Sonar Chromium Browser** is a Chromium browser patch that natively integrates Perplexity's Sonar API to provide AI-powered functionality directly in the browser. Users can type `sonar <query>` in the omnibox for instant AI answers or select text and right-click "Summarize with Sonar" for quick summaries, streamlining research and browsing workflows.

## Features

* **Omnibox AI Answers** with `sonar <query>` syntax for instant responses
* **Context-menu Summarization** for selected text with one-click access
* **Native Browser Integration** using Chromium's omnibox and context-menu APIs
* **Dual Model Support** using Sonar Pro for omnibox and Sonar for summaries
* **Debounced Input Handling** for efficient API usage
* **Custom Browser Build** demonstrating AI integration patterns

## Prerequisites

* Ubuntu 22.04 (WSL2 recommended)
* Chromium source code checkout
* Perplexity API key
* 16GB+ RAM for Chromium build
* Git and standard build tools

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/KoushikBaagh/perplexity-hackathon-chromium.git
cd perplexity-hackathon-chromium

# Apply patches to Chromium source
# Follow the README for detailed Chromium setup instructions
```

## Configuration

Update API keys in the modified files:

```cpp  theme={null}
// In sonar_autocomplete_provider.cc and render_view_context_menu.cc
const std::string API_KEY = "your_perplexity_api_key_here";
```

## Usage

1. **Build Chromium** with applied patches following the repository instructions
2. **Launch the custom browser** with AI integration
3. **Use Omnibox AI**: Type `sonar what is quantum tunneling?` in address bar
4. **Use Context Summarization**: Select text, right-click "Summarize with Sonar"

## Code Explanation

* **Omnibox Integration**: Custom autocomplete provider hooking into Chromium's omnibox API
* **Context Menu**: Modified render view context menu for text summarization
* **API Integration**: Direct Perplexity Sonar API calls with debounced input handling
* **Model Selection**: Sonar Pro for omnibox queries, Sonar for text summarization
* **Browser Architecture**: Demonstrates Chromium extension points for AI features
* **Build Process**: Custom Chromium build with AI patches applied

## Demo Video

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/nFhciodeQ-c" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Links

* [GitHub Repository](https://github.com/KoushikBaagh/perplexity-hackathon-chromium)
* [Chromium Gerrit Repository](https://chromium-review.googlesource.com/c/chromium/src/+/6778540)