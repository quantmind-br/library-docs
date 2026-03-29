---
title: Executive Intelligence | AI-Powered Strategic Decision Platform
url: https://docs.perplexity.ai/docs/cookbook/showcase/executive-intelligence.md
source: llms
fetched_at: 2026-02-04T07:21:51.077216774-03:00
rendered_js: false
word_count: 331
summary: This document provides an overview and setup guide for Executive Intelligence, a platform leveraging the Perplexity Sonar API to generate competitive intelligence, scenario planning, and benchmarking reports for executive decision-making.
tags:
    - perplexity-sonar
    - executive-intelligence
    - competitive-analysis
    - nextjs
    - typescript
    - decision-support
    - real-time-data
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Executive Intelligence | AI-Powered Strategic Decision Platform

> A comprehensive Perplexity Sonar-powered application that provides executives and board members with instant, accurate, and credible intelligence for strategic decision-making

**Executive Intelligence** is a comprehensive Perplexity Sonar-powered application that provides executives and board members with instant, accurate, and credible intelligence for strategic decision-making. It delivers board-ready insights derived from real-time data sources, powered by Perplexity's Sonar API.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/SB1pxIl9Mp0" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Features

* **Competitive Intelligence Briefs** with comprehensive, board-ready competitive analysis and verifiable citations
* **Scenario Planning ("What If?" Analysis)** for dynamic future scenario generation based on real-time data
* **Board Pack Memory** for saving and organizing intelligence briefs, scenario analyses, and benchmark reports
* **Instant Benchmarking & Peer Comparison** with source-cited visual comparisons across critical metrics
* **Real-time Data Integration** leveraging Perplexity Sonar API for up-to-date market intelligence
* **Professional Formatting** with structured reports, executive summaries, and board-ready presentations

## Prerequisites

* Node.js 18+ and npm/yarn
* Git
* Perplexity API key (Sonar Pro)

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/raishs/perplexityhackathon.git
cd perplexityhackathon

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
```

## Configuration

Create `.env.local` file:

```ini  theme={null}
PERPLEXITY_API_KEY=your_perplexity_api_key
```

## Usage

1. **Start Development Server**:
   ```bash  theme={null}
   npm run dev
   ```

2. **Access Application**: Open [http://localhost:3000](http://localhost:3000) in your browser

3. **Generate Intelligence**:
   * Enter a company name in the input field
   * Click "Competitive Analysis" for comprehensive briefs
   * Use "Scenario Planning" for "what-if" analysis
   * Access "Benchmarking" for peer comparisons
   * Save reports to "Board Pack" for later access

4. **Board Pack Management**: Use the "📁 Board Pack" button to view and manage saved intelligence reports

## Code Explanation

* **Frontend**: Next.js with TypeScript and React for modern, responsive UI
* **Backend**: Next.js API routes handling Perplexity Sonar API integration
* **AI Integration**: Perplexity Sonar Pro for real-time competitive intelligence and scenario analysis
* **State Management**: React Context for boardroom memory and persistent data storage
* **Markdown Processing**: Custom utilities for parsing AI responses and citation handling
* **Error Handling**: Comprehensive timeout and error management for API calls
* **Professional Output**: Structured formatting for board-ready presentations with source citations

## Links

* [GitHub Repository](https://github.com/raishs/perplexityhackathon)