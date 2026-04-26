---
title: Send your first API request | Mistral Docs
url: https://docs.mistral.ai/getting-started/quickstarts/developer/first-api-request
source: sitemap
fetched_at: 2026-04-26T04:07:10.894306333-03:00
rendered_js: false
word_count: 169
summary: This document provides a foundational guide for setting up the Mistral AI SDK, generating an API key, and executing a basic chat completion request.
tags:
    - api-setup
    - mistral-sdk
    - getting-started
    - api-key
    - python
    - typescript
category: tutorial
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Create an API key, install the SDK, and send a chat completion request.

- Install the Python or TypeScript SDK
- Send a request to a Mistral model
- Print the model's response

Everything here is the foundation for the agent and RAG quickstarts that follow.

**Time to complete:** ~5 minutes

**Prerequisites:**
- Python 3.9+ or Node.js 18+ installed
- A Mistral AI account. [Create account](https://console.mistral.ai)
- A Mistral API key (Experiment plan is free — no credit card required)

## Step 1: Get Your API Key

1. Open [Studio › API keys](https://console.mistral.ai/api-keys).
2. Click **Create new key**.
3. Give the key a name (e.g., `quickstart`) and click **Create**.
4. Copy the key to your clipboard — it appears only once; if you lose it, generate a new one.
5. Set the key as an environment variable in your terminal:

```bash
export Mistral_API_KEY="your-api-key-here"
```

## Step 2: Install the SDK

## Step 3: Send a Request

Create a file and add the chat completion code. The terminal prints a short description of Mistral AI.

#api-setup #mistral-sdk #getting-started
