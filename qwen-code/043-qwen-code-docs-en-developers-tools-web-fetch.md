---
title: Web Fetch Tool (web_fetch)
url: https://qwenlm.github.io/qwen-code-docs/en/developers/tools/web-fetch
source: github_pages
fetched_at: 2026-04-09T09:04:53.879976864-03:00
rendered_js: true
word_count: 308
summary: This document explains the `web_fetch` tool for Qwen Code, detailing its functionality to fetch content from a given URL, convert HTML to markdown, and process it using an AI model based on a user-provided prompt.
tags:
    - tool-usage
    - web-fetching
    - api-guide
    - url-processing
    - ai-model
category: tutorial
---

Developer Guide

[Tools](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/introduction/ "Tools")

Web Fetch

This document describes the `web_fetch` tool for Qwen Code.

## Description[](#description)

Use `web_fetch` to fetch content from a specified URL and process it using an AI model. The tool takes a URL and a prompt as input, fetches the URL content, converts HTML to markdown, and processes the content with the prompt using a small, fast model.

### Arguments[](#arguments)

`web_fetch` takes two arguments:

- `url` (string, required): The URL to fetch content from. Must be a fully-formed valid URL starting with `http://` or `https://`.
- `prompt` (string, required): The prompt describing what information you want to extract from the page content.

## How to use `web_fetch` with Qwen Code[](#how-to-use-web_fetch-with-qwen-code)

To use `web_fetch` with Qwen Code, provide a URL and a prompt describing what you want to extract from that URL. The tool will ask for confirmation before fetching the URL. Once confirmed, the tool will fetch the content directly and process it using an AI model.

The tool automatically converts HTML to text, handles GitHub blob URLs (converting them to raw URLs), and upgrades HTTP URLs to HTTPS for security.

Usage:

```
web_fetch(url="https://example.com", prompt="Summarize the main points of this article")
```

## `web_fetch` examples[](#web_fetch-examples)

Summarize a single article:

```
web_fetch(url="https://example.com/news/latest", prompt="Can you summarize the main points of this article?")
```

Extract specific information:

```
web_fetch(url="https://arxiv.org/abs/2401.0001", prompt="What are the key findings and methodology described in this paper?")
```

Analyze GitHub documentation:

```
web_fetch(url="https://github.com/QwenLM/Qwen/blob/main/README.md", prompt="What are the installation steps and main features?")
```

## Important notes[](#important-notes)

- **Single URL processing:** `web_fetch` processes one URL at a time. To analyze multiple URLs, make separate calls to the tool.
- **URL format:** The tool automatically upgrades HTTP URLs to HTTPS and converts GitHub blob URLs to raw format for better content access.
- **Content processing:** The tool fetches content directly and processes it using an AI model, converting HTML to readable text format.
- **Output quality:** The quality of the output will depend on the clarity of the instructions in the prompt.
- **MCP tools:** If an MCP-provided web fetch tool is available (starting with “mcp\_\_”), prefer using that tool as it may have fewer restrictions.

Last updated on March 31, 2026

[Exit Plan Mode](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/exit-plan-mode/ "Exit Plan Mode")[Web Search](https://qwenlm.github.io/qwen-code-docs/en/developers/tools/web-search/ "Web Search")