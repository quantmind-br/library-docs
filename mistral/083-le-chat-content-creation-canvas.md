---
title: Canvas | Mistral Docs
url: https://docs.mistral.ai/le-chat/content-creation/canvas
source: sitemap
fetched_at: 2026-04-26T04:07:35.124933093-03:00
rendered_js: false
word_count: 486
summary: This document describes the Canvas feature in Le Chat, a collaborative AI-powered editor used for creating, editing, and managing text, code, data, and presentation documents.
tags:
    - le-chat
    - canvas-editor
    - ai-collaboration
    - content-creation
    - data-analysis
    - document-editing
    - version-control
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Canvas is the **built-in editor** in Le Chat for creating and refining text, data, code, and presentations **collaboratively with AI**.

You can go from a raw CSV to a polished slide deck without leaving the conversation.

## Activate Canvas

1. Click the `+` icon or type `/` in the chat window.
2. Select `Tools` then enable `Canvas`.

Canvas **opens automatically** when Le Chat determines it would be useful. You can also **trigger it manually** by typing `/canvas` or asking *"open in Canvas"*.

Typical prompts that open Canvas:
- *"Create a presentation outline for our Q3 results."*
- *"Analyze the attached CSV and show it as a table."*
- *"Write a Python script to parse JSON logs."*

## Features

| Feature | Description |
|---------|-------------|
| **Direct editing** | Click anywhere to edit text, code, or data by hand |
| **Multiple Canvases** | Open several Canvases as tabs; switch between them without losing context |
| **Version control** | Use navigation arrows to move between versions; toggle change-tracking to see what changed; restore any previous version |

## Typical Workflow

### 1. Upload and Explore Data

Import a CSV or spreadsheet using the `+` button → `Upload Files`, then ask questions.

Canvas displays your data as an editable table. Click into cells to fix headers, rename columns, or remove empty rows.

If Canvas opens in the wrong format, ask *"Show this as a table"* and it will switch.

### 2. Generate a Written Summary

Ask Canvas to produce a text summary based on your data. Edit directly or use inline prompts to refine specific sections.

### 3. Create a Slide Deck

Turn your analysis into presentation-ready slides:

```markdown
# Slide 1
## Q3 Results Overview

- Revenue: $X
- Key wins: ...
```

Canvas generates slides using [Marp](https://marp.app/) syntax. Click the **eye icon** to preview the rendered deck.

When the slides look good, use the export button to save as a PowerPoint file.

## Use Cases

- **Quarterly reports**: upload financial data, generate tables and summaries, export as slides
- **Project briefs**: draft structured documents with inline AI editing
- **Data analysis**: explore CSVs and spreadsheets with direct editing and quick visualizations
- **Presentations**: build and preview Marp slide decks without leaving Le Chat
- **Code prototyping**: write and iterate on Python scripts or React components
- **Email and content drafts**: compose, refine, and translate written content with inline prompts

## Related Tools

- [**Code Interpreter**](https://docs.mistral.ai/le-chat/content-creation/code-interpreter): run Python for data analysis and charting
- [**Files upload**](https://docs.mistral.ai/le-chat/research-analysis/files-upload): import documents, spreadsheets, images
- [**Deep Research**](https://docs.mistral.ai/le-chat/research-analysis/deep-research): automate multi-step web research

#canvas-editor #ai-collaboration #content-creation