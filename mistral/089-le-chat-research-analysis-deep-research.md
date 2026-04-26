---
title: Deep Research | Mistral Docs
url: https://docs.mistral.ai/le-chat/research-analysis/deep-research
source: sitemap
fetched_at: 2026-04-26T04:08:13.354185034-03:00
rendered_js: false
word_count: 492
summary: This document explains how to use the Deep Research feature in Le Chat to automate multi-step web research, including creating search plans, monitoring progress, and generating cited reports.
tags:
    - deep-research
    - web-search
    - automated-reporting
    - le-chat
    - information-synthesis
    - research-tools
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Deep Research automates **multi-step web research** in Le Chat. It breaks down your question, searches multiple sources, evaluates findings, and generates a structured report with citations — reducing hours of manual work to minutes.

Use it for competitive landscape analysis, regulatory reviews, industry trend reports, or any question that benefits from pulling together information across multiple sources.

## How It Works

1. Creates a **search plan** based on your question
2. **Browses the web**, gathering information from multiple sources
3. Synthesizes everything into a structured, cited **report**

Your question can be open-ended (*"What are the latest trends in enterprise AI adoption?"*) or specific (*"Generate a report on renewable energy regulations in the EU for 2024-2025."*).

If your query is too broad, Le Chat will ask you to **add more context** before starting.

## How to Use

1. Select the `Research` option (`Fast` is the default) below the message box.
2. Type your question and send it.

> [!warning]
> When you enable Research mode, Libraries, Connectors, and Agents are temporarily disabled. They become available again once you switch back to standard chat.

## Edit the Search Plan

Before searching, Le Chat proposes a step-by-step research plan. You have full control:

- Click `Edit` to add, remove, or reorder steps
- Reply in the chat to suggest changes in natural language
- Click `Start research` when the plan looks right

Editing the plan lets you steer the research toward the sources and angles that matter most.

## Monitor Progress

Research runs **as a background task**. A progress widget shows live updates, search summaries, and reasoning **as Le Chat works through each step**.

You don't need to wait — open other conversations and come back when the research is done. To stop early, click `Cancel` in the progress widget and confirm.

When enabled, Deep Research uses [Flash Answers](https://docs.mistral.ai/le-chat/conversation/flash-answers) for fast text generation (over 1,000 tokens/minute).

## Report Output

When research finishes, the report includes:
- **Summary**: concise overview of key findings
- **Full report**: detailed analysis with supporting arguments, data, and inline citations
- **Sources**: list of all sources used for verification

**Export and share:**
- Click `Save as PDF` to download a formatted version
- Share reports using the standard conversation sharing feature

## Tips

- **Be specific in your query** — *"Market trends for residential solar in Western Europe, 2023-2025"* produces a more focused report than *"Tell me about solar energy"*
- **Edit the search plan** — adding or removing steps helps get the depth and scope you need
- **Use detailed briefs for complex topics** — include region, time frame, industry, or angle you care about

## Related Features

- [**Web search**](https://docs.mistral.ai/le-chat/research-analysis/web-search): quick, single-step lookups for current information
- [**Flash Answers**](https://docs.mistral.ai/le-chat/conversation/flash-answers): fast, concise answers for simpler questions
- [**Canvas**](https://docs.mistral.ai/le-chat/content-creation/canvas): refine and iterate on research outputs in an editor

#deep-research #web-search #automated-reporting