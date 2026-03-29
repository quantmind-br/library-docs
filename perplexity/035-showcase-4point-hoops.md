---
title: 4Point Hoops | AI Basketball Analytics Platform
url: https://docs.perplexity.ai/docs/cookbook/showcase/4point-Hoops.md
source: llms
fetched_at: 2026-02-04T07:21:30.171971235-03:00
rendered_js: false
word_count: 348
summary: An overview and technical guide for 4Point Hoops, an NBA analytics platform that integrates real-time data from Basketball-Reference with AI-powered insights from Perplexity Sonar. The document details the platform's core features, system architecture, and provides setup instructions for local deployment.
tags:
    - nba-analytics
    - perplexity-api
    - sports-data
    - react
    - python-flask
    - ai-analysis
    - data-visualization
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 4Point Hoops | AI Basketball Analytics Platform

> Advanced NBA analytics platform that combines live Basketball-Reference data with Perplexity Sonar to deliver deep-dive player stats, cross-season comparisons and expert-grade AI explanations

![4Point Hoops Dashboard](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/003/442/047/datas/original.png)

**4Point Hoops** is an advanced NBA analytics platform that turns raw basketball statistics into actionable, narrative-driven insights. By scraping Basketball-Reference in real time and routing context-rich prompts to Perplexity's Sonar Pro model, it helps fans, analysts, and fantasy players understand the "why" and "what's next" – not just the numbers.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/lThCWq0ij7k" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Features

* **Player Analytics** with season & playoff splits, shot-type breakdowns, and performance radar for any NBA player
* **Cross-Era Comparisons** enabling side-by-side stat comparisons (e.g., Michael Jordan '97 vs. Stephen Curry '22)
* **Team Dashboards** with standings, playoff-probability Sankey flows, and auto-refreshing KPI tiles
* **AI Explain & Similar Players** providing one-click Sonar explanations of stat lines and AI-picked comparable athletes
* **Basketball AI Chat** allowing users to ask an expert LLM about NBA history, rosters, or projections
* **Credit-Based SaaS System** with Firebase Auth, Google login, credit wallets, and admin tooling

## Prerequisites

* Node.js 16+ and npm
* Python 3.8+ and pip
* Firebase project setup
* Perplexity API key (Sonar Pro)
* Basketball-Reference access

## Installation

```bash  theme={null}
# Clone the frontend repository
git clone https://github.com/rapha18th/hoop-ai-frontend-44.git
cd hoop-ai-frontend-44
npm install

# Clone the backend repository
git clone https://github.com/rapha18th/4Point-Hoops-Server.git
cd 4Point-Hoops-Server
pip install -r requirements.txt
```

## Configuration

Create `.env` file in the backend directory:

```ini  theme={null}
PERPLEXITY_API_KEY=your_sonar_pro_api_key
FIREBASE_PROJECT_ID=your_firebase_project_id
FIREBASE_PRIVATE_KEY=your_firebase_private_key
FIREBASE_CLIENT_EMAIL=your_firebase_client_email
```

## Usage

1. **Start Backend**:
   ```bash  theme={null}
   cd 4Point-Hoops-Server
   python app.py
   ```

2. **Start Frontend**:
   ```bash  theme={null}
   cd hoop-ai-frontend-44
   npm run dev
   ```

3. **Access Application**: Open the frontend URL and explore NBA analytics with AI-powered insights

4. **Use AI Features**: Click "AI Explain" on any player or stat to get intelligent analysis powered by Perplexity Sonar

## Code Explanation

* **Frontend**: React with shadcn/ui components and Recharts for data visualization
* **Backend**: Python Flask API serving Basketball-Reference data and managing Perplexity API calls
* **Data Pipeline**: BRScraper for real-time data collection with Firebase caching
* **AI Integration**: Perplexity Sonar Pro for intelligent basketball analysis and explanations
* **Authentication**: Firebase Auth with Google login and credit-based access control
* **Deployment**: Frontend on Netlify, backend on Hugging Face Spaces with Docker

## Links

* [Frontend Repository](https://github.com/rapha18th/hoop-ai-frontend-44)
* [Backend Repository](https://github.com/rapha18th/4Point-Hoops-Server)
* [Live Demo](https://4pointhoops.netlify.app/)
* [Devpost Submission](https://devpost.com/software/4point-hoops)