---
title: BazaarAISaathi | AI-Powered Indian Stock Market Assistant
url: https://docs.perplexity.ai/docs/cookbook/showcase/bazaar-ai-saathi.md
source: llms
fetched_at: 2026-02-04T07:21:38.964035439-03:00
rendered_js: false
word_count: 336
summary: This document provides an overview and installation guide for BazaarAISaathi, an AI-powered platform for Indian stock market analysis and portfolio optimization using the Perplexity Sonar API.
tags:
    - indian-stock-market
    - financial-analysis
    - perplexity-api
    - portfolio-optimization
    - streamlit
    - investment-strategies
    - python-application
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# BazaarAISaathi | AI-Powered Indian Stock Market Assistant

> An AI-powered platform for Indian stock market analysis, portfolio optimization, and investment strategies using Perplexity Sonar API

**BazaarAISaathi** is an AI-powered platform designed to empower investors with actionable insights into the Indian stock market. Leveraging advanced natural language processing, real-time data analytics, and expert-driven financial modeling, the app delivers personalized investment strategies, market sentiment analysis, and portfolio optimization recommendations.

## Features

* **Financial Independence Planner (FIRE)** with personalized plans based on age, salary, and goals
* **Investment Advice Tester** using EasyOCR for text extraction and AI validation
* **Fundamental & Technical Analysis** with comprehensive company reports and trading strategies
* **Portfolio Analysis** with multi-dimensional analysis and stock-wise recommendations
* **Market Research & Competitor Benchmarking** using AI-driven industry trend analysis
* **Real-Time Stock Data** with live price tracking and trend analysis
* **Hypothesis Testing** using historical and real-time market data
* **Investment Books Summary** with concise summaries of top 50 investment books

## Prerequisites

* Python 3.8+ and pip
* Streamlit for web application framework
* Perplexity API key (Sonar models)
* Optional: EasyOCR for image text extraction

## Installation

```bash  theme={null}
# Clone the repository
git clone https://github.com/mahanteshimath/BazaarAISaathi.git
cd BazaarAISaathi

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create `secrets.toml` file for Streamlit secrets:

```ini  theme={null}
PERPLEXITY_API_KEY = "your_perplexity_api_key"
# Add other API keys as needed
```

## Usage

1. **Start the Application**:
   ```bash  theme={null}
   streamlit run Home.py
   ```

2. **Access Features**:
   * Navigate through different pages for specific functionality
   * Use the main dashboard for overview and navigation
   * Access specialized tools like portfolio analysis, FIRE planning, and tip testing

3. **Run Specific Modules**:
   ```bash  theme={null}
   streamlit run pages/Financial_Independence.py
   streamlit run pages/Portfolio_Analysis.py
   streamlit run pages/Tip_Tester.py
   ```

## Code Explanation

* **Frontend**: Streamlit web application with interactive pages and real-time data visualization
* **Backend**: Python-based business logic with Pandas for data manipulation and analysis
* **AI Integration**: Perplexity Sonar API models (sonar-deep-research, sonar-reasoning-pro, sonar-pro) for financial analysis
* **Data Processing**: Real-time stock data fetching, CSV data management, and market insights generation
* **Text Extraction**: EasyOCR integration for processing investment tips from images
* **Portfolio Management**: Comprehensive portfolio analysis with optimization recommendations
* **Market Analysis**: Technical and fundamental analysis with sentiment scoring

## Demo Video

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/5t2ldWS3SJ8" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Links

* [GitHub Repository](https://github.com/mahanteshimath/BazaarAISaathi)
* [Live Application](https://bazaar-ai-saathi.streamlit.app/)
* [Architecture Diagram](https://github.com/mahanteshimath/BazaarAISaathi/raw/main/src/App_Architecture.jpg)