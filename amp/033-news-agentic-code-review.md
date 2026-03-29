---
title: Agentic Review
url: https://ampcode.com/news/agentic-code-review
source: crawler
fetched_at: 2026-02-06T02:08:17.643687697-03:00
rendered_js: false
word_count: 421
summary: This document introduces Amp's new specialized code review agent for VS Code, detailing its workflow for analyzing diffs and generating actionable feedback within an integrated development environment.
tags:
    - code-review
    - ai-agent
    - vs-code
    - software-development
    - amp-editor
    - developer-productivity
category: guide
---

Amp has a new agent and it specializes in code review.

In the VS Code extension, you can use this agent by going to the review panel. Start by dragging the selection of changes you want to review. Sometimes, you want to review a single commit; other times you want to review all outstanding changes on your branch:

![](https://static.ampcode.com/news/agentic-review/range-finder.png)

Amp will pre-scan the diff and recommend an order in which to review the files. It will also provide a summary of the changes in each file and the changeset overall:

![](https://static.ampcode.com/news/agentic-review/changes.png?v=2)

This addresses a key difficulty in reviewing large changesets, as it's often difficult to know where to start.

Clicking on a file will open the full file diff, which is editable and has code navigation if your diff includes the current working changes:

![](https://static.ampcode.com/news/agentic-review/file-diff.png?v=2)

## Review Agent

The review agent lives in a separate panel below. It analyzes the changes and posts a list of actionable improvements, which can then be fed back into the main Amp agent to close the feedback loop:

![](https://static.ampcode.com/news/agentic-review/agentic-review.png?v=2)

There's a big improvement in review quality over the [first version](https://ampcode.com/news/review) of the review panel, which used a single-shot LLM request. The new review agent uses Gemini 3 Pro and a review-oriented toolset to perform a much deeper analysis that surfaces more bugs and actionable feedback while filtering out noise.

To get to the review panel, click the button in the navbar. We've also added a `⌘` `;` keybinding to make it easy to toggle in and out of review mode.

## An Opinionated Read-Write Loop

If you're wondering how best to incorporate this into your day-to-day workflow, here's our opinionated loop for agentic coding in the editor:

1

Write code with the agent

2

Open the review panel `⌘ ;`

3

Drag your target diff range

4

Request agentic review and  
read summaries + diffs while waiting

5

Feed comments back into the agent

## Open Questions

We think the review agent and UI help substantially with the bottleneck of reviewing code written by agent. But we're still pondering some more open questions:

- **How do reviews map to threads?** It's not 1-1, since you can review the output of multiple threads at once.
- **How do we incorporate review feedback into long-term memory?** When you accept or reject review comments, should Amp learn from that? Should it incorporate feedback into AGENTS.md?
- **What does the TUI version of this review interface look like?** Should there exist an editable review interface in the TUI? Or should we integrate with existing terminal-based editors and diff viewers?