---
title: Financial Analysis with Yahoo Finance - DSPy
url: https://dspy.ai/tutorials/yahoo_finance_react/
source: sitemap
fetched_at: 2026-01-23T08:04:29.110199015-03:00
rendered_js: false
word_count: 168
summary: This tutorial demonstrates how to build a financial analysis agent using the DSPy ReAct framework integrated with LangChain's Yahoo Finance tools. It explains how to combine external tools and custom Python functions to perform real-time market news analysis and stock price comparisons.
tags:
    - dspy
    - react-agent
    - langchain-integration
    - financial-analysis
    - tools
    - python
    - yahoo-finance
category: tutorial
---

[](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/tutorials/yahoo_finance_react/index.md "Edit this page")

This tutorial shows how to build a financial analysis agent using DSPy ReAct with [LangChain's Yahoo Finance News tool](https://python.langchain.com/docs/integrations/tools/yahoo_finance_news/) for real-time market analysis.

## What You'll Build[¶](#what-youll-build "Permanent link")

A financial agent that fetches news, analyzes sentiment, and provides investment insights.

## Setup[¶](#setup "Permanent link")

```
pipinstalldspylangchainlangchain-communityyfinance
```

```
importdspy
fromlangchain_community.tools.yahoo_finance_newsimport YahooFinanceNewsTool
fromdspy.adapters.types.toolimport Tool
importjson
importyfinanceasyf

# Configure DSPy
lm = dspy.LM(model='openai/gpt-4o-mini')
dspy.configure(lm=lm, allow_tool_async_sync_conversion=True)

# Convert LangChain Yahoo Finance tool to DSPy
yahoo_finance_tool = YahooFinanceNewsTool()
finance_news_tool = Tool.from_langchain(yahoo_finance_tool)
```

```
defget_stock_price(ticker: str) -> str:
"""Get current stock price and basic info."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="1d")

        if hist.empty:
            return f"Could not retrieve data for {ticker}"

        current_price = hist['Close'].iloc[-1]
        prev_close = info.get('previousClose', current_price)
        change_pct = ((current_price - prev_close) / prev_close * 100) if prev_close else 0

        result = {
            "ticker": ticker,
            "price": round(current_price, 2),
            "change_percent": round(change_pct, 2),
            "company": info.get('longName', ticker)
        }

        return json.dumps(result)
    except Exception as e:
        return f"Error: {str(e)}"

defcompare_stocks(tickers: str) -> str:
"""Compare multiple stocks (comma-separated)."""
    try:
        ticker_list = [t.strip().upper() for t in tickers.split(',')]
        comparison = []

        for ticker in ticker_list:
            stock = yf.Ticker(ticker)
            info = stock.info
            hist = stock.history(period="1d")

            if not hist.empty:
                current_price = hist['Close'].iloc[-1]
                prev_close = info.get('previousClose', current_price)
                change_pct = ((current_price - prev_close) / prev_close * 100) if prev_close else 0

                comparison.append({
                    "ticker": ticker,
                    "price": round(current_price, 2),
                    "change_percent": round(change_pct, 2)
                })

        return json.dumps(comparison)
    except Exception as e:
        return f"Error: {str(e)}"
```

## Step 3: Build the Financial ReAct Agent[¶](#step-3-build-the-financial-react-agent "Permanent link")

```
classFinancialAnalysisAgent(dspy.Module):
"""ReAct agent for financial analysis using Yahoo Finance data."""

    def__init__(self):
        super().__init__()

        # Combine all tools
        self.tools = [
            finance_news_tool,  # LangChain Yahoo Finance News
            get_stock_price,
            compare_stocks
        ]

        # Initialize ReAct
        self.react = dspy.ReAct(
            signature="financial_query -> analysis_response",
            tools=self.tools,
            max_iters=6
        )

    defforward(self, financial_query: str):
        return self.react(financial_query=financial_query)
```

## Step 4: Run Financial Analysis[¶](#step-4-run-financial-analysis "Permanent link")

```
defrun_financial_demo():
"""Demo of the financial analysis agent."""

    # Initialize agent
    agent = FinancialAnalysisAgent()

    # Example queries
    queries = [
        "What's the latest news about Apple (AAPL) and how might it affect the stock price?",
        "Compare AAPL, GOOGL, and MSFT performance",
        "Find recent Tesla news and analyze sentiment"
    ]

    for query in queries:
        print(f"Query: {query}")
        response = agent(financial_query=query)
        print(f"Analysis: {response.analysis_response}")
        print("-" * 50)

# Run the demo
if __name__ == "__main__":
    run_financial_demo()
```

## Example Output[¶](#example-output "Permanent link")

When you run the agent with a query like "What's the latest news about Apple?", it will:

1. Use the Yahoo Finance News tool to fetch recent Apple news
2. Get current stock price data
3. Analyze the information and provide insights

**Sample Response:**

```
Analysis: Given the current price of Apple (AAPL) at $196.58 and the slight increase of 0.48%, it appears that the stock is performing steadily in the market. However, the inability to access the latest news means that any significant developments that could influence investor sentiment and stock price are unknown. Investors should keep an eye on upcoming announcements or market trends that could impact Apple's performance, especially in comparison to other tech stocks like Microsoft (MSFT), which is also showing a positive trend.
```

Many Langchain tools use async operations for better performance. For details on async tools, see the [Tools documentation](https://dspy.ai/learn/programming/tools/#async-tools).

## Key Benefits[¶](#key-benefits "Permanent link")

- **Tool Integration**: Seamlessly combine LangChain tools with DSPy ReAct
- **Real-time Data**: Access current market data and news
- **Extensible**: Easy to add more financial analysis tools
- **Intelligent Reasoning**: ReAct framework provides step-by-step analysis

This tutorial shows how DSPy's ReAct framework works with LangChain's financial tools to create intelligent market analysis agents.