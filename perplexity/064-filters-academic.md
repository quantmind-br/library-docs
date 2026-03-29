---
title: Academic Filter Guide
url: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/academic-filter.md
source: llms
fetched_at: 2026-02-04T07:23:14.744189494-03:00
rendered_js: false
word_count: 452
summary: This guide explains how to use the academic search mode in the Perplexity Chat Completions API to prioritize scholarly sources and peer-reviewed research.
tags:
    - academic-filter
    - perplexity-api
    - search-mode
    - research-tools
    - scholarly-data
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Academic Filter Guide

<Note>
  The `search_mode: "academic"` parameter allows you to tailor your searches specifically to academic and scholarly sources, prioritizing peer-reviewed papers, journal articles, and research publications.
</Note>

<Info>
  The `search_mode: "academic"` feature is currently only available in the Chat Completions API. For the Agentic Research API, use domain filters to target academic sources (e.g., `arxiv.org`, `scholar.google.com`).
</Info>

## Overview

The academic filter—sometimes referred to as "academic mode" or "Focus: Academic"—is a feature in Perplexity that allows users to target their searches specifically to academic and scholarly sources. This is especially useful for students, researchers, and professionals who require peer-reviewed papers, journal articles, and research-focused answers rather than general web content.

When you activate the academic filter by setting `search_mode: "academic"`, Perplexity prioritizes results from scholarly databases, journals, and reputable academic publications, filtering out non-academic or general web sources. This ensures that the answers you receive are grounded in research and scholarly consensus.

## Key Features and Functionality

* **Source Filtering**: Prioritizes scholarly databases, academic journals, and research publications
* **Research Focus**: Returns results based on peer-reviewed research rather than general web content
* **Enhanced Precision**: Provides more technical and discipline-specific information for academic queries
* **Compatibility**: Works with other search parameters like `search_context_size` to further refine results

## Usage Examples

### Basic Academic Search

This example shows how to perform a basic search using the academic filter.

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[{"role": "user", "content": "What is the scientific name of the lions mane mushroom?"}],
      search_mode="academic",
      web_search_options={"search_context_size": "low"}
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar-pro",
    messages: [{"role": "user", "content": "What is the scientific name of the lions mane mushroom?"}],
    search_mode: "academic",
    web_search_options: {"search_context_size": "low"}
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "accept: application/json" \
    --header "authorization: Bearer $SONAR_API_KEY" \
    --header "content-type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [{"role": "user", "content": "What is the scientific name of the lions mane mushroom?"}],
      "search_mode": "academic",
      "web_search_options": {"search_context_size": "low"}
  }' | jq
  ```
</CodeGroup>

### Combining Academic Mode with Other Parameters

You can combine the academic filter with other parameters for more refined searches:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar",
      messages=[{"role": "user", "content": "What are the latest findings on neural networks for image recognition?"}],
      search_mode="academic",
      search_after_date_filter="1/1/2023",
      web_search_options={"search_context_size": "high"}
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
    model: "sonar",
    messages: [{"role": "user", "content": "What are the latest findings on neural networks for image recognition?"}],
    search_mode: "academic",
    search_after_date_filter: "1/1/2023",
    web_search_options: {"search_context_size": "high"}
  });

  console.log(completion.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "accept: application/json" \
    --header "authorization: Bearer $SONAR_API_KEY" \
    --header "content-type: application/json" \
    --data '{
      "model": "sonar",
      "messages": [{"role": "user", "content": "What are the latest findings on neural networks for image recognition?"}],
      "stream": false,
      "search_mode": "academic",
      "search_after_date_filter": "1/1/2023",
      "web_search_options": {"search_context_size": "high"}
  }' | jq
  ```
</CodeGroup>

## Recommended Use Cases

The academic filter is particularly valuable for:

1. **Research Literature Reviews**: When you need to gather scholarly information on a specific topic
2. **Technical and Scientific Queries**: For questions requiring scientifically accurate, peer-reviewed answers
3. **Academic Writing Assistance**: When working on papers, theses, or dissertations that require scholarly sources
4. **Educational Support**: For students and educators requiring academically rigorous information

## Best Practices

### Optimizing Academic Searches

* **Be Specific**: Formulate clear, focused questions to receive more precise academic responses
* **Use Technical Terminology**: Include field-specific terms to better target relevant academic literature
* **Combine with Date Filters**: For the most recent research, combine with `search_after_date_filter`
* **Adjust Context Size**: Use higher `search_context_size` values for more comprehensive academic responses

### Performance Considerations

* Academic searches may sometimes take slightly longer due to the specialized nature of scholarly databases
* Consider using models like `sonar-deep-research` for particularly complex academic inquiries
* For more comprehensive literature reviews, set `stream: false` to receive complete responses

### Limitations

* Availability of academic sources varies by field and topic
* Very recent research (published within the last few months) may not always be included
* Some paywalled or subscription-only academic content may not be fully accessible

⸻