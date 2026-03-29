---
title: Briefo | Perplexity Powered News & Finance Social App
url: https://docs.perplexity.ai/docs/cookbook/showcase/briefo.md
source: llms
fetched_at: 2026-02-04T07:21:39.236492305-03:00
rendered_js: false
word_count: 255
summary: This document provides an overview, installation instructions, and architectural details for Briefo, a social news and finance application powered by the Perplexity Sonar API.
tags:
    - perplexity-sonar-api
    - react-native
    - expo
    - supabase
    - edge-functions
    - financial-analysis
    - typescript
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Briefo | Perplexity Powered News & Finance Social App

> AI curated newsfeed, social discussion, and deep research reports built on the Sonar API

# Briefo | Perplexity Powered News & Finance Social App

**Briefo** delivers a personalized, AI generated newsfeed and company deep dives. Readers can follow breaking stories, request on demand financial analyses, and discuss insights with friends, all in one mobile experience powered by Perplexity’s Sonar API.

## Features

* Personalized newsfeed across 17 categories with AI summaries and source links
* Private and public threads for article discussion and sharing
* Watch list with real time market snapshots and optional AI analyses
* Deep research reports generated on 12 selectable criteria such as management, competitors, and valuation
* General purpose chat assistant that remembers each user’s preferred topics

## Prerequisites

* Node 18 LTS or newer
* npm, Yarn, or pnpm
* Expo CLI (`npm i -g expo-cli`)
* Supabase CLI 1.0 or newer for local emulation and Edge Function deploys

## Installation

```bash  theme={null}
git clone https://github.com/adamblackman/briefo-public.git
cd briefo-public
npm install
```

### Environment variables

```ini  theme={null}
# .env              (project root)
MY_SUPABASE_URL=https://<project>.supabase.co
MY_SUPABASE_SERVICE_ROLE_KEY=...
PERPLEXITY_API_KEY=...
LINKPREVIEW_API_KEY=...
ALPACA_API_KEY=...
ALPACA_SECRET_KEY=...

# .env.local        (inside supabase/)
# duplicate or override any secrets needed by Edge Functions
```

## Usage

Run the Expo development server:

```bash  theme={null}
npx expo start
```

Deploy Edge Functions when you are ready:

```bash  theme={null}
supabase functions deploy perplexity-news perplexity-chat perplexity-research portfolio-tab-data
```

## Code Explanation

* Frontend: React Native with Expo Router (TypeScript) targeting iOS, Android, and Web
* Backend: Supabase (PostgreSQL, Row Level Security, Realtime) for data and authentication
* Edge Functions: TypeScript on Deno calling Perplexity, Alpaca, Alpha Vantage, and LinkPreview APIs
* Hooks: Reusable React Query style data hooks live in lib/ and hooks/
* Testing and Linting: ESLint, Prettier, and Expo Lint maintain code quality

## Links

[GitHub Repository](https://github.com/adamblackman/briefo-public)
[Live Demo](https://www.briefo.fun/)