---
title: Financial Analyst with MistralAI Agents API and MCP - Mistral AI Cookbook
url: https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-financial_analyst-readme
source: crawler
fetched_at: 2026-01-29T07:33:46.467643057-03:00
rendered_js: false
word_count: 141
summary: This document describes a financial analysis application that integrates MistralAI agents with Model Context Protocol (MCP) servers to retrieve stock data and generate comprehensive reports.
tags:
    - mistral-ai
    - mcp-server
    - financial-analysis
    - agents-api
    - chainlit
    - stock-market-data
category: guide
---

A financial analysis application that uses MistralAI agents API with MCP servers for stock analysis and report generation.

[![Financial Analyst Demo](https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/gif/financial_analyst.gif)](https://docs.mistral.ai/cookbooks/mistral-agents-agents_api-financial_analyst-readme)

## Use Case

- Get real-time stock prices, historical data and analyst recommendations
- Generate comprehensive financial reports
- Save reports to files

## Architecture

### Main Application

- **app.py**: Chainlit interface with MistralAI agent integration

### MCP Servers

- **stdio\_yfinance\_server.py**: Yahoo Finance data retrieval (prices, financials)
- **stdio\_report\_gen\_server.py**: LLM-powered report generation using MistralAI
- **stdio\_save\_report\_server.py**: Report persistence to files

## Installation

## Environment Setup

Set your MistralAI API key:

Set your Mistral API key in the servers: `mcp_servers/stdio_report_gen_server.py`

## Usage

Run the application:

Open your browser and ask questions like:

- "What's the current stock price of AAPL?"
- "Get me a report on the historical stock prices of microsoft and save it to msft\_historical.md"
- "Show me Microsoft's analyst recommendations"

The app will automatically use the appropriate MCP servers to fetch data and generate reports.