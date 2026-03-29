---
title: SEC Filings Filter Guide
url: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/sec-guide.md
source: llms
fetched_at: 2026-02-04T07:23:24.558876486-03:00
rendered_js: false
word_count: 409
summary: 'This guide explains how to use the search_mode: ''sec'' parameter to filter API search results specifically for official U.S. Securities and Exchange Commission filings and regulatory documents.'
tags:
    - sec-filings
    - search-mode
    - financial-data
    - chat-completions-api
    - perplexity-api
    - regulatory-compliance
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# SEC Filings Filter Guide

<Note>
  The `search_mode: "sec"` parameter allows you to tailor your searches specifically to U.S. Securities and Exchange Commission (SEC) filings, prioritizing official financial documents, disclosures, and regulatory filings from public companies.
</Note>

<Info>
  The `search_mode: "sec"` feature is currently only available in the Chat Completions API. For the Agentic Research API, use domain filters to target SEC sources (e.g., `sec.gov`).
</Info>

## Overview

The SEC filter allows users to target their searches specifically to official SEC filings. This is especially useful for investors, analysts, journalists, and professionals who require authoritative financial documents, such as 10-Ks, 10-Qs, 8-Ks, and other regulatory filings, rather than general web content or news articles.

When you activate the SEC filter by setting `search_mode: "sec"`, Perplexity limits results to the SEC's EDGAR database and other reputable sources of regulatory filings, filtering out non-official or general web sources. This ensures that the answers you receive are grounded in official disclosures and regulatory compliance.

## Key Features and Functionality

* **Source Filtering**: Prioritizes SEC filings such as 10-K, 10-Q, 8-K, S-1, and more
* **Regulatory Focus**: Returns results based on official financial and regulatory documents
* **Enhanced Precision**: Provides more accurate and up-to-date information for financial and compliance queries

## Usage Examples

### Basic SEC Filings Search

This example shows how to perform a basic search using the SEC filter.

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "accept: application/json" \
    --header "authorization: Bearer $SONAR_API_KEY" \
    --header "content-type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "Prepare me for markets opening."}],
      "search_mode": "sec"
    }' | jq
  ```

  ```python Python theme={null}
  import requests

  url = "https://api.perplexity.ai/chat/completions"
  headers = {
      "accept": "application/json",
      "authorization": "Bearer YOUR_API_KEY",
      "content-type": "application/json"
  }
  payload = {
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "Prepare me for markets opening."}],
      "search_mode": "sec"
  }'

  response = requests.post(url, headers=headers, json=payload)
  print(response.json())
  ```

  ```javascript Node.js theme={null}
  const axios = require('axios');

  const url = "https://api.perplexity.ai/chat/completions";
  const headers = {
    "accept": "application/json",
    "authorization": "Bearer YOUR_API_KEY",
    "content-type": "application/json"
  };
  const payload = {
    "model": "sonar-pro",
    "messages": [{"role": "user", "content": "Prepare me for markets opening."}],
    "stream": false,
    "search_mode": "sec"
  };

  axios.post(url, payload, { headers })
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
  ```
</CodeGroup>

### Combining SEC Mode with Other Parameters

You can combine the SEC filter with other parameters for more refined searches:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "accept: application/json" \
    --header "authorization: Bearer $SONAR_API_KEY" \
    --header "content-type: application/json" \
    --data '{
      "model": "sonar",
      "messages": [{"role": "user", "content": "Summarize the latest 10-K filings for Apple Inc."}],
      "stream": false,
      "search_mode": "sec",
      "search_after_date_filter": "1/1/2023"
  }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar",
      messages=[{"role": "user", "content": "Summarize the latest 10-K filings for Apple Inc."}],
      search_mode="sec",
      search_after_date_filter="1/1/2023"
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar",
    messages: [{"role": "user", "content": "Summarize the latest 10-K filings for Apple Inc."}],
    search_mode: "sec",
    search_after_date_filter: "1/1/2023"
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

## Recommended Use Cases

The SEC filter is particularly valuable for:

1. **Financial Analysis**: When you need to review official financial statements and disclosures
2. **Regulatory Compliance**: For questions requiring up-to-date regulatory filings and compliance information
3. **Market Research**: When tracking company events, earnings, and risk factors
4. **Due Diligence**: For investors and analysts evaluating public companies

## Best Practices

### Optimizing SEC Filings Searches

* **Be Specific**: Reference the type of filing (e.g., 10-K, 8-K) and company name for more precise results
* **Use Financial Terminology**: Include terms like "earnings," "risk factors," or "management discussion" to target relevant sections
* **Combine with Date Filters**: For the most recent filings, combine with `search_after_date_filter`
* **Adjust Context Size**: Use higher `search_context_size` values for more comprehensive responses

### Limitations

* Availability is limited to filings made public through the SEC's EDGAR system
* Some filings may be delayed or amended after initial publication
* Only covers U.S. public companies and registered entities

⸻