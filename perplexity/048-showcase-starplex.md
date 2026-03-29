---
title: StarPlex | AI-Powered Startup Intelligence Platform
url: https://docs.perplexity.ai/docs/cookbook/showcase/starplex.md
source: llms
fetched_at: 2026-02-04T07:22:42.061786263-03:00
rendered_js: false
word_count: 517
summary: This document provides an overview and technical setup guide for StarPlex, an AI-powered startup intelligence platform that utilizes Perplexity's Sonar API for market validation and resource discovery.
tags:
    - starplex
    - ai-startup-intelligence
    - perplexity-api
    - market-validation
    - business-intelligence
    - startup-tools
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# StarPlex | AI-Powered Startup Intelligence Platform

> An AI-powered startup intelligence platform that helps entrepreneurs validate their business ideas and find the right resources to succeed

**StarPlex** is an AI-powered startup intelligence platform that helps entrepreneurs validate their business ideas and connect with the resources they need to succeed. Powered primarily by **Perplexity Sonar Pro**, it features an interactive **3D globe interface** as its main UI. Simply enter your startup idea, and watch as the AI engine analyzes and visualizes insights directly on the globe—mapping out competitors, markets, demographics, VCs, and potential co-founders across the world in real-time.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/iusCyDNzY60" title="StarPlex Demo" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Features

* **Market Validation Analysis** with AI-proof scoring, market cap estimation, and growth trend analysis
* **Interactive 3D Globe Interface** for visualizing global startup intelligence data
* **Competitor Research** with threat scoring and competitive landscape mapping
* **VC & Investor Matching** based on investment thesis and portfolio alignment
* **Co-founder Discovery** with compatibility scoring and expertise matching
* **Demographic Research** with heatmap visualization of target audience locations
* **AI Pitch Deck Generation** creating investor-ready presentations
* **Context-Aware Chatbot** with RAG integration across all research data

## Prerequisites

* Node.js 18+ and npm
* Python 3.8+ and pip
* Perplexity API key (Sonar Pro)
* Mapbox token and SERP API key

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/JerryWu0430/StarPlex.git
cd StarPlex

# Backend setup
cd backend
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install
```

## Configuration

Create `.env` file in the backend directory:

```ini  theme={null}
PERPLEXITY_API_KEY=your_perplexity_api_key
MAPBOX_TOKEN=your_mapbox_token
SERPAPI_KEY=your_serpapi_key
```

## Usage

1. **Start Backend**:
   ```bash  theme={null}
   cd backend
   python main.py
   ```

2. **Start Frontend**:
   ```bash  theme={null}
   cd frontend
   npm run dev
   ```

3. **Access Application**: Open [http://localhost:3000](http://localhost:3000) and enter your startup idea

4. **Explore Intelligence**: Use the 3D globe to visualize competitors, VCs, demographics, and co-founders

5. **Generate Assets**: Create pitch decks and chat with the AI assistant about your analysis

## How StarPlex Uses Perplexity Sonar API

StarPlex leverages Perplexity's Sonar API through a **multi-module intelligence architecture**:

**Market Analysis Engine**
Uses Sonar Pro for comprehensive market validation, combining Google Trends data with AI analysis to generate market cap estimates, AI-disruption scores, and growth projections with structured JSON outputs.

**Competitor Intelligence**
Employs multiple concurrent Sonar queries to identify competing companies, funding status, and threat levels. Each competitor receives a 1-10 threat score with detailed competitive positioning analysis.

**VC & Co-founder Matching**
Leverages Sonar's real-time web knowledge to find relevant investors and potential co-founders, scoring matches based on investment thesis alignment, expertise fit, and geographic proximity.

**Context-Aware Business Assistant**
Implements RAG (Retrieval-Augmented Generation) by feeding all research data into Sonar conversations, creating a knowledgeable startup advisor that can answer questions about market positioning, competitive threats, and strategic decisions.

**Geographic Intelligence**
Combines Sonar's demographic insights with Mapbox geocoding to create interactive heatmaps showing where target audiences are concentrated globally.

## Code Explanation

* **Backend**: Python FastAPI with AsyncIO for concurrent Perplexity API calls across multiple analysis modules
* **Frontend**: Next.js with React 19, featuring Cobe for 3D globe visualization and Mapbox GL for interactive mapping
* **AI Integration**: Multi-model Perplexity strategy using Sonar Pro for complex analysis and Sonar for faster queries
* **Data Pipeline**: Intelligent caching, structured JSON responses, and real-time streaming for immediate user feedback
* **Visualization**: Dynamic data binding between Perplexity insights and interactive globe/map interfaces

## Links

* [GitHub Repository](https://github.com/JerryWu0430/StarPlex)
* [Live Demo](https://starplex.app)
* [Devpost Submission](https://devpost.com/software/starplex)