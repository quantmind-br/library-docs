---
title: Polymarket — Query Polymarket prediction market data — search markets, get prices, orderbooks, and price history | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-polymarket
source: crawler
fetched_at: 2026-04-24T17:05:35.024812906-03:00
rendered_js: false
word_count: 425
summary: This document serves as a reference guide detailing how to query Polymarket prediction market data using public, read-only REST APIs. It outlines key concepts like markets and events, describes the three available APIs (Gamma, CLOB, Data), and details the typical workflow for retrieving and presenting odds information.
tags:
    - polymarket-data
    - rest-api
    - prediction-markets
    - odds-querying
    - market-reference
    - read-only
category: reference
---

Query Polymarket prediction market data — search markets, get prices, orderbooks, and price history. Read-only via public REST APIs, no API key needed.

SourceBundled (installed by default)Path`skills/research/polymarket`Version`1.0.0`AuthorHermes Agent + Teknium

## Reference: full SKILL.md[​](#reference-full-skillmd "Direct link to Reference: full SKILL.md")

info

The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.

## Polymarket — Prediction Market Data

Query prediction market data from Polymarket using their public REST APIs. All endpoints are read-only and require zero authentication.

See `references/api-endpoints.md` for the full endpoint reference with curl examples.

## When to Use[​](#when-to-use "Direct link to When to Use")

- User asks about prediction markets, betting odds, or event probabilities
- User wants to know "what are the odds of X happening?"
- User asks about Polymarket specifically
- User wants market prices, orderbook data, or price history
- User asks to monitor or track prediction market movements

## Key Concepts[​](#key-concepts "Direct link to Key Concepts")

- **Events** contain one or more **Markets** (1:many relationship)
- **Markets** are binary outcomes with Yes/No prices between 0.00 and 1.00
- Prices ARE probabilities: price 0.65 means the market thinks 65% likely
- `outcomePrices` field: JSON-encoded array like `["0.80", "0.20"]`
- `clobTokenIds` field: JSON-encoded array of two token IDs \[Yes, No] for price/book queries
- `conditionId` field: hex string used for price history queries
- Volume is in USDC (US dollars)

## Three Public APIs[​](#three-public-apis "Direct link to Three Public APIs")

1. **Gamma API** at `gamma-api.polymarket.com` — Discovery, search, browsing
2. **CLOB API** at `clob.polymarket.com` — Real-time prices, orderbooks, history
3. **Data API** at `data-api.polymarket.com` — Trades, open interest

## Typical Workflow[​](#typical-workflow "Direct link to Typical Workflow")

When a user asks about prediction market odds:

1. **Search** using the Gamma API public-search endpoint with their query
2. **Parse** the response — extract events and their nested markets
3. **Present** market question, current prices as percentages, and volume
4. **Deep dive** if asked — use clobTokenIds for orderbook, conditionId for history

## Presenting Results[​](#presenting-results "Direct link to Presenting Results")

Format prices as percentages for readability:

- outcomePrices `["0.652", "0.348"]` becomes "Yes: 65.2%, No: 34.8%"
- Always show the market question and probability
- Include volume when available

Example: `"Will X happen?" — 65.2% Yes ($1.2M volume)`

## Parsing Double-Encoded Fields[​](#parsing-double-encoded-fields "Direct link to Parsing Double-Encoded Fields")

The Gamma API returns `outcomePrices`, `outcomes`, and `clobTokenIds` as JSON strings inside JSON responses (double-encoded). When processing with Python, parse them with `json.loads(market['outcomePrices'])` to get the actual array.

## Rate Limits[​](#rate-limits "Direct link to Rate Limits")

Generous — unlikely to hit for normal usage:

- Gamma: 4,000 requests per 10 seconds (general)
- CLOB: 9,000 requests per 10 seconds (general)
- Data: 1,000 requests per 10 seconds (general)

## Limitations[​](#limitations "Direct link to Limitations")

- This skill is read-only — it does not support placing trades
- Trading requires wallet-based crypto authentication (EIP-712 signatures)
- Some new markets may have empty price history
- Geographic restrictions apply to trading but read-only data is globally accessible