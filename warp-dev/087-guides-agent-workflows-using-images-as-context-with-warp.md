---
title: Use Images as Context for Agents | Guides | Warp
url: https://docs.warp.dev/guides/agent-workflows/using-images-as-context-with-warp
source: sitemap
fetched_at: 2026-04-29T15:06:28.285182787-03:00
rendered_js: false
word_count: 285
summary: This document explains how to use image-based context in Warp to enable AI agents to interpret visual UI mockups and translate them into functional code components.
tags:
    - ai-agents
    - image-context
    - frontend-development
    - ui-design
    - workflow-optimization
    - code-generation
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Humans process visuals faster than text — and the same applies to AI. Warp supports images as context, letting you attach screenshots directly to prompts.

> [!tip]
> "An image is worth a thousand words" — especially when debugging UI or building frontend components.

## What Image Context Does

- Attach one or more screenshots to an agent query
- Give visual references for bugs, designs, or features
- Let the agent visually interpret what you mean

Use cases:
- Rebuilding a design from Figma
- Identifying layout misalignments
- Debugging visual bugs

## Building an MCP Marketplace from Figma

### Step 1 — Capture the Mock

Take a screenshot of your design (e.g., the MCP Marketplace layout).

### Step 2 — Attach the Image

1. Click the 📎 image icon in the input bar
2. Select your screenshot
3. Confirm it's attached to the query

## Running the Task

Once attached, Warp's agent:

1. Detects the attached image
2. Searches your repo (e.g., `collection.rs`)
3. Generates diffs that recreate the UI from the mock
4. Creates corresponding components and layout logic

View and edit diffs in the Code Diff Viewer (similar to GitHub's diff interface).

> [!tip]
> Warp recommends smaller, focused diffs — agents perform better when working iteratively.

## Reviewing the Results

The agent built:

- A UI component for the MCP Marketplace
- Static data for three MCP servers (Linear, GitHub, Stripe)
- Proper rendering logic and styling

> "It matched the mock almost perfectly — something that would've taken me two days was done in 20 minutes."

## Optimizing for Performance

Warp automatically:

- Resizes images client-side
- Compresses them intelligently before sending
- Minimizes token usage without losing clarity
