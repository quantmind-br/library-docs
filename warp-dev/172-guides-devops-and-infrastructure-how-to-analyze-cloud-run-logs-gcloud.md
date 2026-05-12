---
title: Analyze Cloud Run Logs (gcloud) | Guides | Warp
url: https://docs.warp.dev/guides/devops-and-infrastructure/how-to-analyze-cloud-run-logs-gcloud
source: sitemap
fetched_at: 2026-04-29T15:07:02.124203736-03:00
rendered_js: false
word_count: 139
summary: This document explains how to use Warp's AI agent features to query, parse, and analyze cloud server logs using natural language prompts.
tags:
    - warp-terminal
    - log-analysis
    - ai-agent
    - gcloud-logging
    - natural-language-processing
    - cloud-monitoring
category: tutorial
optimized: true
optimized_at: 2026-04-29T15:07:02.124203736-03:00
---
Use Warp to retrieve, organize, and analyze Cloud Run logs using natural language prompts.

## Setup

Open Warp and enable **voice input** (optional) for hands-free prompting.

> [!tip]
> Voice input is optional — only enable if you prefer hands-free prompting.

## Prompt Example

```
Use the warp-server-staging gcloud project and pull logs
for the last 10 minutes from the warp-server Cloud Run instance.
Organize them by info, warning, and error levels.
Create a histogram across message types,
and highlight the most concerning errors to investigate.
```

## How It Works

1. Warp detects the command as an **Agent Mode** request
2. Gathers project context (`warp-server-staging`)
3. Executes `gcloud` logging queries automatically
4. Writes retrieved data to a temporary file for processing

## Automated Analysis

Warp's agent generates a Python script to:

- Parse logs
- Count messages by severity
- Output summary metrics

**Example output:**
```
1,000 log entries total
980 info
11 warning
9 errors
```

## Reviewing Results

Warp outputs a readable histogram and highlights anomalies:

> "Gemini AI error messages detected — worth reviewing."

Expand each log group interactively or inspect the temporary Python code for debugging.

#log-analysis #gcloud #cloud-monitoring
