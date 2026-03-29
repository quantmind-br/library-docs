---
title: Perplexity Discord Bot
url: https://docs.perplexity.ai/docs/cookbook/examples/discord-py-bot/README.md
source: llms
fetched_at: 2026-02-04T07:21:16.141323016-03:00
rendered_js: false
word_count: 352
summary: This document provides a step-by-step guide for creating and deploying a Discord bot using discord.py that integrates with the Perplexity Sonar API to provide AI-powered answers with citations.
tags:
    - discord-bot
    - perplexity-api
    - python
    - discord-py
    - ai-integration
    - chatbot-development
category: tutorial
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Perplexity Discord Bot

> A simple discord.py bot that integrates Perplexity's Sonar API to bring AI answers to your Discord server.

A simple `discord.py` bot that integrates [Perplexity's Sonar API](https://docs.perplexity.ai/) into your Discord server. Ask questions and get AI-powered answers with web access through slash commands or by mentioning the bot.

<img src="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-demo.png?fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=fec4e6c8feb8d56bc0165078d195b3cf" alt="Discord Bot Demo" data-og-width="1865" width="1865" data-og-height="1074" height="1074" data-path="docs/cookbook/static/img/discord-py-bot-demo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-demo.png?w=280&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=5086be8da91a67f103a053beb90cd6e7 280w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-demo.png?w=560&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=30f582c5987ee31ec3c0ea34219ef611 560w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-demo.png?w=840&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=e90584be4a55321bfed36cf9330fcbb6 840w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-demo.png?w=1100&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=cc132adf03b29a0afe5749a1f721277c 1100w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-demo.png?w=1650&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=44727667848f16c43a1c3389681b6d26 1650w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-demo.png?w=2500&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=997cd8d4204df98570b11d2dc4378441 2500w" />

## ✨ Features

* **🌐 Web-Connected AI**: Uses Perplexity's Sonar API for up-to-date information
* **⚡ Slash Command**: Simple `/ask` command for questions
* **💬 Mention Support**: Ask questions by mentioning the bot
* **🔗 Source Citations**: Automatically formats and links to sources
* **🔒 Secure Setup**: Environment-based configuration for API keys

## 🛠️ Prerequisites

<Steps>
  <Step title="Python Environment">
    **Python 3.8+** installed on your system

    ```bash  theme={null}
    python --version  # Should be 3.8 or higher
    ```
  </Step>

  <Step title="Perplexity API Access">
    **Active Perplexity API Key** from [Perplexity AI Settings](https://www.perplexity.ai/settings/api)

    <Note>You'll need a paid Perplexity account to access the API. See the [pricing page](https://www.perplexity.ai/pricing) for current rates.</Note>
  </Step>

  <Step title="Discord Bot Application">
    **Discord Bot Token** from the [Discord Developer Portal](https://discord.com/developers/applications)
  </Step>
</Steps>

## 🚀 Quick Start

### 1. Repository Setup

Clone the repository and navigate to the bot directory:

```bash  theme={null}
git clone https://github.com/perplexity-ai/api-cookbook.git
cd api-cookbook/docs/examples/discord-py-bot/
```

### 2. Install Dependencies

```bash  theme={null}
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Configure API Keys

<Steps>
  <Step title="Get Your Perplexity API Key">
    1. Visit [Perplexity AI Account Settings](https://www.perplexity.ai/settings/api)
    2. Generate a new API key
    3. Copy the key to the .env file

    <Warning>Keep your API key secure! Never commit it to version control or share it publicly.</Warning>
  </Step>

  <Step title="Create Discord Bot Application">
    1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
    2. Click **"New Application"** and give it a descriptive name
    3. Navigate to the **"Bot"** section
    4. Click **"Reset Token"** (or "Add Bot" if first time)
    5. Copy the bot token
  </Step>

  <Step title="Configure Environment Variables">
    Copy the example environment file and add your keys:

    ```bash  theme={null}
    cp env.example .env
    ```

    Edit `.env` with your credentials:

    ```bash title=".env" theme={null}
    DISCORD_TOKEN="your_discord_bot_token_here"
    PERPLEXITY_API_KEY="your_perplexity_api_key_here"
    ```
  </Step>
</Steps>

## 🎯 Usage Guide

### Bot Invitation & Setup

<Steps>
  <Step title="Generate Invite URL">
    In the Discord Developer Portal:

    1. Go to **OAuth2** → **URL Generator**
    2. Select scopes: `bot` and `applications.commands`
    3. Select bot permissions: `Send Messages`, `Use Slash Commands`
    4. Copy the generated URL
  </Step>

  <Step title="Invite to Server">
    1. Paste the URL in your browser
    2. Select the Discord server to add the bot to
    3. Confirm the permissions
  </Step>

  <Step title="Start the Bot">
    ```bash  theme={null}
    python bot.py
    ```

    You should see output confirming the bot is online and commands are synced.
  </Step>
</Steps>

### How to Use

**Slash Command:**

```
/ask [your question here]
```

<img src="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-slash-command.png?fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=e23fffab539e92df49bca22831efce1c" alt="Slash Command Demo" data-og-width="2140" width="2140" data-og-height="1062" height="1062" data-path="docs/cookbook/static/img/discord-py-bot-slash-command.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-slash-command.png?w=280&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=abbc8de57df96d1ca0aceef1cadb2eea 280w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-slash-command.png?w=560&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=e7f95f57124d77eef08147397eaf7539 560w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-slash-command.png?w=840&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=239ffb1068274187dcf529f67362bc55 840w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-slash-command.png?w=1100&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=bdd8f81b1e4234edc465fe872814cd00 1100w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-slash-command.png?w=1650&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=4cf6e562c50899db531233cff3e2df20 1650w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-slash-command.png?w=2500&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=ce5649a6edd3cb9576c803acce3b9e88 2500w" />

**Mention the Bot:**

```
@YourBot [your question here]
```

<img src="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-mention-command.png?fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=ddc57eeb7a44b4554b738f227b97f00f" alt="Mention Command Demo" data-og-width="2185" width="2185" data-og-height="843" height="843" data-path="docs/cookbook/static/img/discord-py-bot-mention-command.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-mention-command.png?w=280&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=c4ca45b66c3c6089b169d9c520b92eb1 280w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-mention-command.png?w=560&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=038614484cb583a98cffcbd40290568f 560w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-mention-command.png?w=840&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=6f037398417d487d6f044240620e1a37 840w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-mention-command.png?w=1100&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=4ef12f76ae570f0c32836a613c5eafa7 1100w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-mention-command.png?w=1650&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=2a67f1be936dcc4cb8b25dbecbaef701 1650w, https://mintcdn.com/perplexity/wXoWdjxPwagF2W_M/docs/cookbook/static/img/discord-py-bot-mention-command.png?w=2500&fit=max&auto=format&n=wXoWdjxPwagF2W_M&q=85&s=c0f710764e1b79e529ec42d0a8bcdf8a 2500w" />

## 📊 Response Format

The bot provides clean, readable responses with:

* **AI Answer**: Direct response from Perplexity's Sonar API
* **Source Citations**: Clickable links to sources (when available)
* **Automatic Truncation**: Responses are trimmed to fit Discord's limits

## 🔧 Technical Details

This bot uses:

* **Model**: Perplexity's `sonar-pro` model
* **Response Limit**: 2000 tokens from API, truncated to fit Discord
* **Temperature**: 0.2 for consistent, factual responses
* **No Permissions**: Anyone in the server can use the bot