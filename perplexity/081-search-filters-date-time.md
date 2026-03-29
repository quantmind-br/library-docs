---
title: Search Date and Time Filters
url: https://docs.perplexity.ai/docs/search/filters/date-time-filters.md
source: llms
fetched_at: 2026-02-04T07:25:16.983598017-03:00
rendered_js: false
word_count: 1014
summary: This document explains how to use date and time filters in the Search API to restrict results by publication date, last updated date, or relative recency intervals.
tags:
    - search-api
    - date-filters
    - search-recency
    - query-parameters
    - api-reference
    - data-filtering
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Date and Time Filters

<Note>
  The `search_after_date_filter` and `search_before_date_filter` parameters allow you to restrict search results to a specific publication date range. Only results with publication dates falling between these dates will be returned.

  The `last_updated_after_filter` and `last_updated_before_filter` parameters allow you to filter by when content was last modified or updated, rather than when it was originally published.

  The `search_recency_filter` parameter provides a convenient way to filter results by predefined time periods (e.g., "day", "week", "month", "year") relative to the current date.
</Note>

<Info>
  Specific date filters must be provided in the "%m/%d/%Y" format (e.g., "3/1/2025"). Recency filters use predefined values like "day", "week", "month", or "year". All filters are optional—you may supply either specific dates or recency filters as needed.
</Info>

## Overview

Date and time filters for the Search API allow you to control which search results are returned by limiting them to specific time periods. There are three types of date and time filters available:

### Publication Date Filters

The `search_after_date_filter` and `search_before_date_filter` parameters filter results based on when content was **originally created or published**. This is useful when you need to:

* Find content published within a specific timeframe
* Exclude outdated or overly recent publications
* Focus on content from a particular publication period

### Last Updated Date Filters

The `last_updated_after_filter` and `last_updated_before_filter` parameters filter results based on when content was **last modified or updated**. This is useful when you need to:

* Find recently updated or maintained content
* Exclude stale content that hasn't been updated recently
* Focus on content that has been refreshed within a specific period

### Search Recency Filter

The `search_recency_filter` parameter provides a simple way to filter results by predefined time periods relative to the current date. This is useful when you need to:

* Find content from the past day, week, month, or year
* Get recent results without specifying exact dates
* Quickly filter for timely information

**Available values:**

* `"day"` - Content from the past 24 hours
* `"week"` - Content from the past 7 days
* `"month"` - Content from the past 30 days
* `"year"` - Content from the past 365 days

**Important:** Publication filters use the original creation/publication date, last updated filters use the modification date, while recency filters use a relative time period from the current date.

To constrain search results by publication date:

```bash  theme={null}
"search_after_date_filter": "3/1/2025",
"search_before_date_filter": "3/5/2025"
```

To constrain search results by last updated date:

```bash  theme={null}
"last_updated_after_filter": "07/01/2025",
"last_updated_before_filter": "12/30/2025"
```

To constrain search results by recency:

```bash  theme={null}
"search_recency_filter": "week"
```

These filters will be applied in addition to any other search parameters.

## Examples

**1. Limiting Results by Publication Date Range**

This example limits search results to content published between March 1, 2025, and March 5, 2025.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search(
      query="latest AI developments",
      max_results=10,
      search_after_date_filter="3/1/2025",
      search_before_date_filter="3/5/2025"
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search({
    query: "latest AI developments",
    max_results: 10,
    search_after_date_filter: "3/1/2025",
    search_before_date_filter: "3/5/2025"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "latest AI developments",
      "max_results": 10,
      "search_after_date_filter": "3/1/2025",
      "search_before_date_filter": "3/5/2025"
    }' | jq
  ```
</CodeGroup>

**2. Filtering with a Single Publication Date Parameter**

If you only wish to restrict the results to those published on or after a specific date, include just the `search_after_date_filter`:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search(
      query="tech news published after March 1, 2025",
      max_results=10,
      search_after_date_filter="3/1/2025"
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search({
    query: "tech news published after March 1, 2025",
    max_results: 10,
    search_after_date_filter: "3/1/2025"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "tech news published after March 1, 2025",
      "max_results": 10,
      "search_after_date_filter": "3/1/2025"
    }' | jq
  ```
</CodeGroup>

**3. Filtering by Last Updated Date Range**

This example limits search results to content that was last updated between July 1, 2025, and December 30, 2025. This is useful for finding recently maintained or refreshed content.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search(
      query="recently updated tech articles",
      max_results=10,
      last_updated_after_filter="07/01/2025",
      last_updated_before_filter="12/30/2025"
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search({
    query: "recently updated tech articles",
    max_results: 10,
    last_updated_after_filter: "07/01/2025",
    last_updated_before_filter: "12/30/2025"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "recently updated tech articles",
      "max_results": 10,
      "last_updated_after_filter": "07/01/2025",
      "last_updated_before_filter": "12/30/2025"
    }' | jq
  ```
</CodeGroup>

**4. Using Search Recency Filter**

The `search_recency_filter` provides a convenient way to filter results by predefined time periods without specifying exact dates:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search(
      query="latest AI developments",
      max_results=10,
      search_recency_filter="week"
  )

  print(response)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search({
    query: "latest AI developments",
    max_results: 10,
    search_recency_filter: "week"
  });

  console.log(response);
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "latest AI developments",
      "max_results": 10,
      "search_recency_filter": "week"
    }' | jq
  ```
</CodeGroup>

This example will return only content from the past 7 days, automatically calculated from the current date.

**5. Different Recency Filter Options**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Get content from the past day
  day_response = client.search(
      query="breaking tech news",
      max_results=5,
      search_recency_filter="day"
  )

  # Get content from the past month
  month_response = client.search(
      query="AI research developments",
      max_results=10,
      search_recency_filter="month"
  )

  # Get content from the past year
  year_response = client.search(
      query="major tech trends",
      max_results=15,
      search_recency_filter="year"
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Get content from the past day
  const dayResponse = await client.search({
    query: "breaking tech news",
    max_results: 5,
    search_recency_filter: "day"
  });

  // Get content from the past month
  const monthResponse = await client.search({
    query: "AI research developments",
    max_results: 10,
    search_recency_filter: "month"
  });

  // Get content from the past year
  const yearResponse = await client.search({
    query: "major tech trends",
    max_results: 15,
    search_recency_filter: "year"
  });
  ```

  ```bash cURL theme={null}
  # Get content from the past day
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "breaking tech news",
      "max_results": 5,
      "search_recency_filter": "day"
    }' | jq

  # Get content from the past month
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "AI research developments",
      "max_results": 10,
      "search_recency_filter": "month"
    }' | jq
  ```
</CodeGroup>

## Parameter Reference

### `search_after_date_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "3/1/2025")
* **Description**: Filters search results to only include content published after this date
* **Optional**: Yes
* **Example**: `"search_after_date_filter": "1/1/2025"`

### `search_before_date_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "3/1/2025")
* **Description**: Filters search results to only include content published before this date
* **Optional**: Yes
* **Example**: `"search_before_date_filter": "12/31/2025"`

### `last_updated_after_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "07/01/2025")
* **Description**: Filters search results to only include content last updated after this date
* **Optional**: Yes
* **Example**: `"last_updated_after_filter": "07/01/2025"`

### `last_updated_before_filter`

* **Type**: String
* **Format**: "%m/%d/%Y" (e.g., "12/30/2025")
* **Description**: Filters search results to only include content last updated before this date
* **Optional**: Yes
* **Example**: `"last_updated_before_filter": "12/30/2025"`

### `search_recency_filter`

* **Type**: String
* **Allowed Values**: "day", "week", "month", "year"
* **Description**: Filters search results to content from the specified time period relative to the current date
* **Optional**: Yes
* **Example**: `"search_recency_filter": "week"`

## Best Practices

**Date Format**

* Strict Format: Dates must match the "%m/%d/%Y" format exactly. For example, "3/1/2025" or "03/01/2025" is acceptable.
* Consistency: Use one or both date filters consistently based on your search needs. Combining both provides a clear range.

**Filter Selection**

* Choose the Right Filter Type: Use publication date filters (`search_after_date_filter`/`search_before_date_filter`) when you care about when content was originally created. Use last updated filters (`last_updated_after_filter`/`last_updated_before_filter`) when you need recently maintained content. Use recency filters (`search_recency_filter`) for quick, relative time filtering.
* Recency vs. Exact Dates: Use `search_recency_filter` for convenience when you want recent content (e.g., "past week"). Use specific date filters when you need precise control over the time range.
* Combining Filters: You can use both publication and last updated filters together to find content that meets both criteria (e.g., published in 2024 but updated recently). Note that `search_recency_filter` cannot be combined with specific date filters (`search_after_date_filter`/`search_before_date_filter` or `last_updated_after_filter`/`last_updated_before_filter`).

**Client-Side Validation**

* Regex Check: Validate date strings on the client side using a regex such as:

<CodeGroup>
  ```bash  theme={null}
  date_regex='^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/[0-9]{4}$'
  ```

  ```python  theme={null}
  date_regex = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/\d{4}$'
  ```
</CodeGroup>

This ensures that dates conform to the required format before sending the request.

**Performance Considerations**

* Narrowing the Search: Applying date range filters typically reduces the number of results, which may improve response times and result relevance.
* Avoid Over-Restriction: Ensure that the date range is neither too narrow (limiting useful results) nor too broad (defeating the purpose of the filter).

## Advanced Usage Patterns

**Finding Breaking News**

Use the `search_recency_filter` with "day" to find the most recent breaking news:

```python  theme={null}
response = client.search(
    query="breaking news technology",
    max_results=5,
    search_recency_filter="day"
)
```

**Historical Research**

Use specific date ranges to research historical events or trends:

```python  theme={null}
response = client.search(
    query="AI developments",
    max_results=20,
    search_after_date_filter="1/1/2023",
    search_before_date_filter="12/31/2023"
)
```

**Finding Recently Maintained Content**

Use last updated filters to find content that has been refreshed or maintained recently:

```python  theme={null}
response = client.search(
    query="React best practices",
    max_results=10,
    last_updated_after_filter="07/01/2025"
)
```

**Trend Analysis**

Compare different time periods by making multiple searches:

```python  theme={null}
# Recent trends
recent = client.search(
    query="machine learning trends",
    search_recency_filter="month"
)

# Older trends for comparison
older = client.search(
    query="machine learning trends",
    search_after_date_filter="1/1/2023",
    search_before_date_filter="1/31/2023"
)
```

## Error Handling

When using date filters, ensure proper error handling for invalid date formats:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  import re

  def validate_date_format(date_string):
      pattern = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/\d{4}$'
      return bool(re.match(pattern, date_string))

  def search_with_date_filter(query, after_date=None, before_date=None):
      client = Perplexity()
      
      # Validate date formats
      if after_date and not validate_date_format(after_date):
          raise ValueError(f"Invalid date format: {after_date}")
      if before_date and not validate_date_format(before_date):
          raise ValueError(f"Invalid date format: {before_date}")
      
      try:
          response = client.search(
              query=query,
              search_after_date_filter=after_date,
              search_before_date_filter=before_date
          )
          return response
      except Exception as e:
          print(f"Search failed: {e}")
          return None
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  function validateDateFormat(dateString: string): boolean {
    const pattern = /^(0?[1-9]|1[0-2])\/(0?[1-9]|[12]\d|3[01])\/\d{4}$/;
    return pattern.test(dateString);
  }

  async function searchWithDateFilter(
    query: string, 
    afterDate?: string, 
    beforeDate?: string
  ) {
    const client = new Perplexity();
    
    // Validate date formats
    if (afterDate && !validateDateFormat(afterDate)) {
      throw new Error(`Invalid date format: ${afterDate}`);
    }
    if (beforeDate && !validateDateFormat(beforeDate)) {
      throw new Error(`Invalid date format: ${beforeDate}`);
    }
    
    try {
      const response = await client.search({
        query,
        search_after_date_filter: afterDate,
        search_before_date_filter: beforeDate
      });
      return response;
    } catch (error) {
      console.error('Search failed:', error);
      return null;
    }
  }
  ```
</CodeGroup>