---
title: Nano Pdf — Edit PDFs with natural-language instructions using the nano-pdf CLI | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-nano-pdf
source: crawler
fetched_at: 2026-04-24T17:05:34.592406584-03:00
rendered_js: false
word_count: 40
summary: This document explains how to use the nano-pdf command-line interface (CLI) to modify PDF documents by providing natural language instructions, allowing users to make precise changes like updating titles or correcting text on specific pages.
tags:
    - pdf-editing
    - natural-language
    - cli-tool
    - document-modification
    - nano-pdf
category: tutorial
---

Edit PDFs with natural-language instructions using the nano-pdf CLI. Modify text, fix typos, update titles, and make content changes to specific pages without manual editing.

Edit PDFs using natural-language instructions. Point it at a page and describe what to change.

```bash
# Change a title on page 1
nano-pdf edit deck.pdf 1"Change the title to 'Q3 Results' and fix the typo in the subtitle"

# Update a date on a specific page
nano-pdf edit report.pdf 3"Update the date from January to February 2026"

# Fix content
nano-pdf edit contract.pdf 2"Change the client name from 'Acme Corp' to 'Acme Industries'"
```