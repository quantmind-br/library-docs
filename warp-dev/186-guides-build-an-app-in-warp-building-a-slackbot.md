---
title: Build a Slackbot | Guides | Warp
url: https://docs.warp.dev/guides/build-an-app-in-warp/building-a-slackbot
source: sitemap
fetched_at: 2026-04-29T15:07:00.965715581-03:00
rendered_js: false
word_count: 299
summary: This document provides instructions for deploying a self-hosted Slack bot that integrates Warp AI with GitHub repositories to facilitate repository-based queries and pull request assistance.
tags:
    - slack-bot
    - warp-ai
    - github-integration
    - docker-deployment
    - ai-coding-assistant
    - repository-management
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Spin up a self-hosted Slack bot that connects your team's GitHub repos to Warp AI. Mention it in Slack to answer repo questions or open pull requests — runs in Docker with minimal config.

## Quickstart Setup

### Clone the repository

```
git clone https://github.com/warpdotdev/warp-slackbot-public.git
cd warp-slackbot-public
```

Includes all config templates, Docker setup, and the Slack app manifest.

### Configure environment variables

```
cp .env.template .env
```

Fill in `.env`:

| Variable | Description |
|---|---|
| `SLACK_BOT_TOKEN` | Bot token from Slack app → **OAuth & Permissions** (`xoxb-`) |
| `SLACK_APP_TOKEN` | App-level token from **Basic Information → App-Level Tokens** (`xapp-`); requires `connections:write` scope for Socket Mode |
| `GITHUB_PAT` | GitHub PAT with `repo` access for cloning repositories |
| `WARP_API_KEY` | Warp API key for the agentic environment |

Docker reads these automatically on startup.

### Configure repositories

```
cp repos.yaml.template repos.yaml
```

Add repos in `repos.yaml`:

```yaml
repositories:
  - url: "myorg/backend"
    branch: "main"
  - url: "myorg/frontend"
    branch: "develop"
```

Behind the scenes: the bot clones each repo via GitHub PAT, stores them in a persistent Docker volume, and indexes them for context.

### Slack App Manifest

The `slack_app_manifest.json` configures the Slack app (paste it into **Create from Manifest**):

- Listens for `app_mention` events and thread replies
- Runs via Socket Mode (secure WebSocket)
- Sends/receives in invited channels

### Run the bot

```
docker-compose up --build
```

The bot authenticates to Slack and GitHub, then listens for messages. Logs activity in the terminal.

### Test in Slack

1. Invite the bot to a channel.
2. Mention it or reply in a thread:

```
@Warp analyze the recent changes in the main branch
@Warp help me review this PR
```

The bot pulls repo context and replies with AI-assisted insights.

## What happens on startup

1. Reads `.env` and `repos.yaml`
2. Authenticates to Slack (Socket Mode + Web API)
3. Authenticates to GitHub and clones listed repos
4. Starts listening for `app_mention` and threaded messages
5. Routes context/commands to Warp's AI agent backend

Stop with `Ctrl+C` or run persistently (e.g., `tmux`/`systemd`).

#slack-bot #warp-ai #github-integration #docker-deployment #ai-coding-assistant #repository-management
