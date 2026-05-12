---
title: Build a Real-time Chat App | Guides | Warp
url: https://docs.warp.dev/guides/build-an-app-in-warp/building-a-real-time-chat-app-github-mcp-+-railway
source: sitemap
fetched_at: 2026-04-29T15:06:54.076115473-03:00
rendered_js: false
word_count: 264
summary: This document provides a walkthrough on using the Warp AI development environment to plan, build, debug, and deploy a fullstack web application. It covers autonomous code execution, integrating MCP servers for GitHub, and streamlining cloud deployment via platforms like Railway.
tags:
    - warp
    - agentic-development
    - mcp-server
    - fullstack-app
    - autonomous-coding
    - application-deployment
    - ai-development-tools
category: tutorial
optimized: true
optimized_at: 2026-04-29T15:06:54.076115473-03:00
---
Build and deploy a fullstack real-time chat app using Warp, Python (FastAPI), JavaScript frontend, Railway, and GitHub MCP.

## Setup & Modes

Three core modes:
- **Auto Mode** — detects command vs AI prompt
- **Terminal Mode** — shell commands only
- **Agent Mode** — AI conversational prompts

Switch via top-bar buttons. Enable voice input or attach screenshots for debugging.

## Generate App Idea

Use *planning models* for AI-generated roadmaps:

```
I would like to make something of simple to medium complexity that I could finish in about 30 minutes. I want this to be web based. I want to have some kind of interface and some kind of backend. Can you give me a fun idea that's not going to be too complicated to build out and to eventually deploy?
```

Example suggestion: real-time chat application.

## Create Development Plan

```
I like idea one. Can you come up with a detailed plan on how to build this?
```

Plan includes:
- Frontend (React + Socket.IO)
- Backend (FastAPI server)
- Database integration
- Deployment steps

Modify plan interactively, then execute: `Please execute this plan.`

## Allow Autonomous Execution

1. **Settings** → **AI** → **Agents**
2. Change **"Always Ask"** → **"Always Allow"**
3. Restricted commands remain blocked

Warp runs shell commands, creates directories, writes code automatically.

## Run the App

Click any file to edit directly in Warp. Ask to run locally:

```
Can you run this app for me so I can test it? Tell me how to view it.
```

Debug conversationally: `I'm getting an internal server error. Can you fix this?`

## Add New Features

Request enhancements: `Can you add emoji reactions to the messages?`

Warp updates frontend and backend WebSocket logic for real-time reactions.

## Connect GitHub MCP

1. **Settings** → **AI** → **MCP Servers** → Add
2. Add JSON config:

```json
{
  "github": {
    "command": "docker",
    "args": ["run", "-i", "--rm", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN", "ghcr.io/github/github-mcp-server"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "${<INSERT_YOURS_HERE>}"
    }
  }
}
```

3. Generate GitHub token with scopes: `repo`, `workflow`, `secrets`, `pull_request`, `environments`
4. Save and restart Warp

Create repo automatically: `Can you make a new remote repo for me and upload my code?`

## Deploy via Railway

```
I have a FastAPI application built with Python. I want to deploy this. It just has an integrated frontend with JavaScript, HTML, and CSS. What's the easiest way to do that? Can you assist me?
```

Steps:
1. Create Railway account
2. Connect GitHub repo
3. Deploy from GitHub
4. Get public domain

Test live at the public URL.
