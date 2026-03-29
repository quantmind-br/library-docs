---
title: Financial News Tracker
url: https://docs.perplexity.ai/docs/cookbook/examples/financial-news-tracker/README.md
source: llms
fetched_at: 2026-02-04T07:21:23.084181323-03:00
rendered_js: false
word_count: 489
summary: This document provides instructions for installing and using a command-line tool that utilizes the Perplexity Sonar API to aggregate and analyze real-time financial news and market sentiment.
tags:
    - financial-news
    - perplexity-api
    - market-analysis
    - sentiment-analysis
    - cli-tool
    - data-extraction
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Financial News Tracker

> A real-time financial news monitoring tool that fetches and analyzes market news using Perplexity's Sonar API

# Financial News Tracker

A command-line tool that fetches and analyzes real-time financial news using Perplexity's Sonar API. Get comprehensive market insights, news summaries, and investment analysis for any financial topic.

## Features

* Real-time financial news aggregation from multiple sources
* Market sentiment analysis (Bullish/Bearish/Neutral)
* Impact assessment for news items (High/Medium/Low)
* Sector and company-specific analysis
* Investment insights and recommendations
* Customizable time ranges (24h to 1 year)
* Structured JSON output support
* Beautiful emoji-enhanced CLI output

## Installation

### 1. Install required dependencies

```bash  theme={null}
# Install from requirements file (recommended)
pip install -r requirements.txt

# Or install manually
pip install requests pydantic
```

### 2. Make the script executable

```bash  theme={null}
chmod +x financial_news_tracker.py
```

## API Key Setup

The tool requires a Perplexity API key. You can provide it in one of these ways:

### 1. As an environment variable (recommended)

```bash  theme={null}
export PPLX_API_KEY=YOUR_API_KEY
```

### 2. As a command-line argument

```bash  theme={null}
./financial_news_tracker.py "tech stocks" --api-key YOUR_API_KEY
```

### 3. In a file

Create a file named `pplx_api_key` or `.pplx_api_key` in the same directory:

```bash  theme={null}
echo "YOUR_API_KEY" > .pplx_api_key
chmod 600 .pplx_api_key
```

## Quick Start

Get the latest tech stock news:

```bash  theme={null}
./financial_news_tracker.py "tech stocks"
```

This will fetch recent financial news about tech stocks, analyze market sentiment, and provide actionable insights.

## Usage Examples

### Basic usage - Get news for a specific topic

```bash  theme={null}
./financial_news_tracker.py "S&P 500"
```

### Get cryptocurrency news from the past week

```bash  theme={null}
./financial_news_tracker.py "cryptocurrency" --time-range 1w
```

### Track specific company news

```bash  theme={null}
./financial_news_tracker.py "AAPL Apple stock"
```

### Get news about market sectors

```bash  theme={null}
./financial_news_tracker.py "energy sector oil prices"
```

### Output as JSON for programmatic use

```bash  theme={null}
./financial_news_tracker.py "inflation rates" --json
```

### Use a different model

```bash  theme={null}
./financial_news_tracker.py "Federal Reserve interest rates" --model sonar
```

### Enable structured output (requires Tier 3+ API access)

```bash  theme={null}
./financial_news_tracker.py "tech earnings" --structured-output
```

## Time Range Options

* `24h` - Last 24 hours (default)
* `1w` - Last week
* `1m` - Last month
* `3m` - Last 3 months
* `1y` - Last year

## Output Format

The tool provides comprehensive financial analysis including:

### 1. Executive Summary

A brief overview of the key financial developments

### 2. Market Analysis

* **Market Sentiment**: Overall market mood (🐂 Bullish, 🐻 Bearish, ⚖️ Neutral)
* **Key Drivers**: Factors influencing the market
* **Risks**: Current market risks and concerns
* **Opportunities**: Potential investment opportunities

### 3. News Items

Each news item includes:

* **Headline**: The main news title
* **Impact**: Market impact level (🔴 High, 🟡 Medium, 🟢 Low)
* **Summary**: Brief description of the news
* **Affected Sectors**: Industries or companies impacted
* **Source**: News source attribution

### 4. Investment Insights

Actionable recommendations and analysis based on the news

## Example Output

```
📊 FINANCIAL NEWS REPORT: tech stocks
📅 Period: Last 24 hours

📝 EXECUTIVE SUMMARY:
Tech stocks showed mixed performance today as AI-related companies surged while 
semiconductor stocks faced pressure from supply chain concerns...

📈 MARKET ANALYSIS:
  Sentiment: 🐂 BULLISH

  Key Drivers:
    • Strong Q4 earnings from major tech companies
    • AI sector momentum continues
    • Federal Reserve signals potential rate cuts

  ⚠️ Risks:
    • Semiconductor supply chain disruptions
    • Regulatory scrutiny on big tech
    • Valuation concerns in AI sector

  💡 Opportunities:
    • Cloud computing growth
    • AI infrastructure plays
    • Cybersecurity demand surge

📰 KEY NEWS ITEMS:

1. Microsoft Hits All-Time High on AI Growth
   Impact: 🔴 HIGH
   Summary: Microsoft stock reached record levels following strong Azure AI revenue...
   Sectors: Cloud Computing, AI, Software
   Source: Bloomberg

💼 INSIGHTS & RECOMMENDATIONS:
  • Consider diversifying within tech sector
  • AI infrastructure companies show strong momentum
  • Monitor semiconductor sector for buying opportunities
```

## Advanced Features

### Custom Queries

You can combine multiple topics for comprehensive analysis:

```bash  theme={null}
# Get news about multiple related topics
./financial_news_tracker.py "NVIDIA AMD semiconductor AI chips"

# Track geopolitical impacts on markets
./financial_news_tracker.py "oil prices Middle East geopolitics"

# Monitor economic indicators
./financial_news_tracker.py "inflation CPI unemployment Federal Reserve"
```

### JSON Output

For integration with other tools or scripts:

```bash  theme={null}
./financial_news_tracker.py "bitcoin" --json | jq '.market_analysis.market_sentiment'
```

## Tips for Best Results

1. **Be Specific**: Include company tickers, sector names, or specific events
2. **Combine Topics**: Mix company names with relevant themes (e.g., "TSLA electric vehicles")
3. **Use Time Ranges**: Match the time range to your investment horizon
4. **Regular Monitoring**: Set up cron jobs for daily market updates

## Limitations

* Results depend on available public information
* Not financial advice - always do your own research
* Historical data may be limited for very recent events
* Structured output requires Tier 3+ Perplexity API access

## Error Handling

The tool includes comprehensive error handling for:

* Invalid API keys
* Network connectivity issues
* API rate limits
* Invalid queries
* Parsing errors

## Integration Examples

### Daily Market Report

Create a script for daily updates:

```bash  theme={null}
#!/bin/bash
# daily_market_report.sh

echo "=== Daily Market Report ===" > market_report.txt
echo "Date: $(date)" >> market_report.txt
echo "" >> market_report.txt

./financial_news_tracker.py "S&P 500 market overview" >> market_report.txt
./financial_news_tracker.py "top gaining stocks" >> market_report.txt
./financial_news_tracker.py "cryptocurrency bitcoin ethereum" >> market_report.txt
```

### Python Integration

```python  theme={null}
import subprocess
import json

def get_financial_news(query, time_range="24h"):
    result = subprocess.run(
        ["./financial_news_tracker.py", query, "--time-range", time_range, "--json"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        raise Exception(f"Error fetching news: {result.stderr}")

# Example usage
news = get_financial_news("tech stocks", "1w")
print(f"Market sentiment: {news['market_analysis']['market_sentiment']}")
```