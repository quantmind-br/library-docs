---
title: Build a Chrome Extension | Guides | Warp
url: https://docs.warp.dev/guides/build-an-app-in-warp/building-a-chrome-extension-d3.js-+-javascript-+-html-+-css
source: sitemap
fetched_at: 2026-04-29T15:06:54.979285129-03:00
rendered_js: false
word_count: 370
summary: This document provides a step-by-step guide on developing, debugging, and deploying a D3.js-based Chrome extension by leveraging multiple AI agents for parallel code generation, testing, and UI refinement.
tags:
    - chrome-extension
    - d3-js
    - ai-agents
    - web-development
    - data-visualization
    - browser-automation
    - multi-agent-systems
category: tutorial
optimized: true
optimized_at: 2026-04-29T15:06:54.979285129-03:00
---
Build a **Sankey diagram Chrome extension** called "Sankey Stone" using D3.js, debugging with AI agents, and deploying to the Chrome Web Store.

## Setup & Create Project

### Initial Files

- `manifest.json`
- `popup.html`
- `popup.css`
- `popup.js`
- Icon images (`icon16.png`, `icon32.png`, `icon48.png`, etc.)

### Load in Chrome

`chrome://extensions` → Developer Mode → Load unpacked → Select project folder

> [!warning]
> "Failed to load extension" errors usually mean manifest path or icon filename mismatches.

## Test Initial D3.js Rendering

If extension shows "Loading diagram" but no chart:
1. Take a screenshot
2. Ask agent: `It says loading diagram — why isn't the chart appearing?`
3. Agent regenerates `popup.js` with working D3.js Sankey chart

## Version Control & GitHub

```bash
git init
git add .
git commit -m "Initial Sankey Stone extension"
```

Agent can create GitHub repo and push automatically.

## Add Local Test Page

Launch a local web server with a test page that outputs traffic flow data. The extension reads and visualizes.

Prompt to update: `Update the test data page so that it generates random labels and different contexts when I hit the regenerate button.`

## Coordinate Multiple Agents in Parallel

Run agents simultaneously for different tasks:
- `Update the test data page to randomize labels and values`
- `Change the refresh page button to regenerate the chart in a different style`
- `Generate a useful README file`

Enable **Auto-approve all agent actions** for background updates.

> [!tip]
> Parallel agents mirror a small team: one for data, one for UI, one for docs.

## Refine Styles & Interactions

```bash
Apply new color themes and improve the layout.
```

Changes applied:
- Multiple color themes and improved node layout
- Hover highlights connected nodes
- Drag nodes to rearrange
- "Switch Style" button to cycle themes

Add PNG export: `Add a button to download this image as a PNG.`

## Add API Key Setup Screen

```bash
Add a settings page to enter the Anthropic API key and test it.
```

- Test key functionality
- Store keys locally in browser

## Summary

1. Scaffold Chrome extension with D3.js
2. Debug manifest and icon issues
3. Generate and refine code with agents
4. Use parallel agents for UI, data, docs
5. Add interactivity, themes, export options
6. Create API key setup screen
7. Package and publish to Chrome Web Store

> [!tip]
> Start small, scaffold with AI prompts, iterate with parallel agents, deploy from Warp.
