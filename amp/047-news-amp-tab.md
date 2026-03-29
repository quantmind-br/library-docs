---
title: Amp Tab
url: https://ampcode.com/news/amp-tab
source: crawler
fetched_at: 2026-02-06T02:08:48.320518502-03:00
rendered_js: false
word_count: 110
summary: This document introduces Amp Tab, an AI-powered code completion engine that suggests multi-line edits based on semantic context and recent changes. It explains how to enable the feature within VS Code settings during its research preview phase.
tags:
    - code-completion
    - ai-tools
    - developer-productivity
    - vs-code
    - amp-tab
    - semantic-context
category: guide
---

Today, we're launching Amp Tab, our new in-editor completion engine, designed to anticipate your next actions and reduce the time spent manually writing code.

It uses a custom model that was trained to understand what you are trying to do next, based on your recent changes, your language server's diagnostics, and what we call semantic context.

Amp Tab can suggest regular single or multi-line edits to change entire code blocks, next to your cursor or farther away, somewhere else in your current document.

We're releasing Amp Tab now as a research preview, free to use for all Amp users. Enable it by adding the following to your VS Code settings:

```
{
	"amp.tab.enabled": true
}
```