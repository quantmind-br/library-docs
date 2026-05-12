---
title: "\U0001F6E0️ Crawl4AI v0.7.1: Minor Cleanup Update"
url: https://docs.crawl4ai.com/blog/releases/0.7.1/
source: sitemap
fetched_at: 2026-04-26T07:46:26.431235977-03:00
rendered_js: false
word_count: 105
summary: This release notes document outlines the maintenance updates for version 0.7.1, detailing the removal of unused codebase components and improvements to project documentation.
tags:
    - release-notes
    - code-cleanup
    - documentation-update
    - crawl4ai
    - maintenance-release
category: other
---

*July 17, 2025 • 2 min read*

* * *

A small maintenance release that removes unused code and improves documentation.

## 🎯 What's Changed

- **Removed unused StealthConfig** from `crawl4ai/browser_manager.py`
- **Updated documentation** with better examples and parameter explanations
- **Fixed virtual scroll configuration** examples in docs

## 🧹 Code Cleanup

Removed unused `StealthConfig` import and configuration that wasn't being used anywhere in the codebase. The project uses its own custom stealth implementation through JavaScript injection instead.

```
# Removed unused code:
fromplaywright_stealthimport StealthConfig
stealth_config = StealthConfig(...)  # This was never used
```

## 📖 Documentation Updates

- Fixed adaptive crawling parameter examples
- Updated session management documentation
- Corrected virtual scroll configuration examples

## 🚀 Installation

```
pipinstallcrawl4ai==0.7.1
```

No breaking changes - upgrade directly from v0.7.0.

* * *

Questions? Issues? - GitHub: [github.com/unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) - Discord: [discord.gg/crawl4ai](https://discord.gg/jP8KfhDhyN)