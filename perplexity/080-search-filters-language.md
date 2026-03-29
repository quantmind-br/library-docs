---
title: Search Language Filter
url: https://docs.perplexity.ai/docs/search/filters/language-filter.md
source: llms
fetched_at: 2026-02-04T07:25:21.056394824-03:00
rendered_js: false
word_count: 987
summary: This document explains how to use the search_language_filter parameter in the Perplexity Search API to restrict search results to specific languages using ISO 639-1 codes. It provides implementation details, usage constraints, and code examples for filtering search results across single or multiple languages.
tags:
    - perplexity-api
    - search-api
    - language-filtering
    - iso-639-1
    - api-parameters
    - localization
    - multilingual-search
category: reference
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Language Filter

<Note>
  The `search_language_filter` parameter allows you to filter search results by language using ISO 639-1 language codes. Only results in the specified languages will be returned.
</Note>

<Info>
  Language codes must be valid 2-letter ISO 639-1 codes (e.g., "en", "ru", "fr"). You can filter by up to 10 languages per request.
</Info>

## Overview

The language filter for the Search API allows you to control which search results are returned by limiting them to specific languages. This is particularly useful when you need to:

* Search for content in specific languages
* Conduct multilingual research across multiple languages
* Focus on regional content in local languages
* Build language-specific applications or features

The `search_language_filter` parameter accepts an array of ISO 639-1 language codes and returns only results that match those languages.

To filter search results by language:

```bash  theme={null}
"search_language_filter": ["en", "fr", "de"]
```

This filter will be applied in addition to any other search parameters.

## Examples

**1. Single Language Filter**

This example limits search results to English language content only.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="artificial intelligence",
      max_results=10,
      search_language_filter=["en"]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "artificial intelligence",
    maxResults: 10,
    searchLanguageFilter: ["en"]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "artificial intelligence",
      "max_results": 10,
      "search_language_filter": ["en"]
    }' | jq
  ```
</CodeGroup>

**2. Multiple Language Filter**

Search across multiple languages to gather diverse perspectives or multilingual content:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for content in English, French, and German
  response = client.search.create(
      query="renewable energy innovations",
      max_results=15,
      search_language_filter=["en", "fr", "de"]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for content in English, French, and German
  const response = await client.search.create({
    query: "renewable energy innovations",
    maxResults: 15,
    searchLanguageFilter: ["en", "fr", "de"]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "renewable energy innovations",
      "max_results": 15,
      "search_language_filter": ["en", "fr", "de"]
    }' | jq
  ```
</CodeGroup>

**3. Regional Language Search**

Focus on content from specific regions by using their local languages:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for Asian market news in Chinese, Japanese, and Korean
  response = client.search.create(
      query="technology market trends",
      max_results=10,
      search_language_filter=["zh", "ja", "ko"]
  )

  # Search for European tech news in multiple European languages
  eu_response = client.search.create(
      query="tech startups",
      max_results=10,
      search_language_filter=["en", "de", "fr", "es", "it"]
  )
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for Asian market news in Chinese, Japanese, and Korean
  const response = await client.search.create({
    query: "technology market trends",
    maxResults: 10,
    searchLanguageFilter: ["zh", "ja", "ko"]
  });

  // Search for European tech news in multiple European languages
  const euResponse = await client.search.create({
    query: "tech startups",
    maxResults: 10,
    searchLanguageFilter: ["en", "de", "fr", "es", "it"]
  });
  ```

  ```bash cURL theme={null}
  # Search for Asian market news
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "technology market trends",
      "max_results": 10,
      "search_language_filter": ["zh", "ja", "ko"]
    }' | jq
  ```
</CodeGroup>

**4. Combining with Other Filters**

Language filters work seamlessly with other search parameters for precise control:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Combine language filter with date and domain filters
  response = client.search.create(
      query="climate change research",
      max_results=20,
      search_language_filter=["en", "de"],
      search_domain_filter=["nature.com", "science.org"],
      search_recency_filter="month"
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"URL: {result.url}")
      print(f"Date: {result.date}")
      print("---")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Combine language filter with date and domain filters
  const response = await client.search.create({
    query: "climate change research",
    maxResults: 20,
    searchLanguageFilter: ["en", "de"],
    searchDomainFilter: ["nature.com", "science.org"],
    searchRecencyFilter: "month"
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`URL: ${result.url}`);
    console.log(`Date: ${result.date}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "climate change research",
      "max_results": 20,
      "search_language_filter": ["en", "de"],
      "search_domain_filter": ["nature.com", "science.org"],
      "search_recency_filter": "month"
    }' | jq
  ```
</CodeGroup>

## Parameter Reference

### `search_language_filter`

* **Type**: Array of strings
* **Format**: ISO 639-1 language codes (2 lowercase letters)
* **Description**: Filters search results to only include content in the specified languages
* **Optional**: Yes
* **Maximum**: 10 language codes per request
* **Example**: `"search_language_filter": ["en", "fr", "de"]`

## Common Language Codes

Here's a comprehensive list of frequently used ISO 639-1 language codes:

| Language   | Code | Language   | Code |
| ---------- | ---- | ---------- | ---- |
| English    | `en` | Portuguese | `pt` |
| Spanish    | `es` | Dutch      | `nl` |
| French     | `fr` | Polish     | `pl` |
| German     | `de` | Swedish    | `sv` |
| Italian    | `it` | Norwegian  | `no` |
| Russian    | `ru` | Danish     | `da` |
| Chinese    | `zh` | Finnish    | `fi` |
| Japanese   | `ja` | Czech      | `cs` |
| Korean     | `ko` | Hungarian  | `hu` |
| Arabic     | `ar` | Greek      | `el` |
| Hindi      | `hi` | Turkish    | `tr` |
| Bengali    | `bn` | Hebrew     | `he` |
| Indonesian | `id` | Thai       | `th` |
| Vietnamese | `vi` | Ukrainian  | `uk` |

<Tip>
  For a complete list of ISO 639-1 language codes, see the [ISO 639-1 standard](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
</Tip>

## Best Practices

### Language Code Validation

* **Use Valid Codes**: Always use valid 2-letter ISO 639-1 codes. Invalid codes will result in an API error.
* **Lowercase Only**: Language codes must be lowercase (e.g., "en" not "EN").
* **Client-Side Validation**: Validate language codes on the client side using a regex pattern:

<CodeGroup>
  ```python Python theme={null}
  import re

  def validate_language_code(code):
      pattern = r'^[a-z]{2}$'
      return bool(re.match(pattern, code))

  def validate_language_filters(codes):
      if len(codes) > 10:
          raise ValueError("Maximum 10 language codes allowed")
      
      for code in codes:
          if not validate_language_code(code):
              raise ValueError(f"Invalid language code: {code}")
      
      return True

  # Usage
  try:
      codes = ["en", "fr", "de"]
      validate_language_filters(codes)
      
      response = client.search.create(
          query="technology news",
          search_language_filter=codes
      )
  except ValueError as e:
      print(f"Validation error: {e}")
  ```

  ```typescript TypeScript theme={null}
  function validateLanguageCode(code: string): boolean {
    const pattern = /^[a-z]{2}$/;
    return pattern.test(code);
  }

  function validateLanguageFilters(codes: string[]): void {
    if (codes.length > 10) {
      throw new Error("Maximum 10 language codes allowed");
    }
    
    for (const code of codes) {
      if (!validateLanguageCode(code)) {
        throw new Error(`Invalid language code: ${code}`);
      }
    }
  }

  // Usage
  try {
    const codes = ["en", "fr", "de"];
    validateLanguageFilters(codes);
    
    const response = await client.search.create({
      query: "technology news",
      searchLanguageFilter: codes
    });
  } catch (error) {
    console.error("Validation error:", error.message);
  }
  ```
</CodeGroup>

### Strategic Language Selection

* **Be Specific**: Choose languages that are most relevant to your research or application needs.
* **Consider Your Audience**: Select languages that match your target audience's preferences.
* **Regional Relevance**: Combine language filters with geographic filters (`country` parameter) for better regional targeting.
* **Content Availability**: Some topics may have limited content in certain languages. Start broad and narrow down as needed.

### Performance Considerations

* **Filter Size**: While you can specify up to 10 languages, using fewer languages may improve response times.
* **Result Quality**: More languages mean a broader search scope, which can dilute result relevance. Be strategic about which languages to include.
* **Combination Effects**: Language filters combined with other restrictive filters (domain, date) may significantly reduce the number of results.

## Advanced Usage Patterns

### Multilingual Research

Conduct comprehensive research by searching across multiple languages:

```python  theme={null}
from perplexity import Perplexity

client = Perplexity()

# Research a global topic in multiple languages
languages = [
    ["en"],           # English-speaking countries
    ["zh", "ja"],     # East Asia
    ["es", "pt"],     # Latin America and Iberia
    ["fr", "de", "it"] # Western Europe
]

results_by_region = {}

for lang_group in languages:
    response = client.search.create(
        query="sustainable development goals progress",
        max_results=10,
        search_language_filter=lang_group
    )
    results_by_region[", ".join(lang_group)] = response.results

# Analyze results by language/region
for region, results in results_by_region.items():
    print(f"Results in {region}: {len(results)} found")
```

### Content Localization Research

Find examples and references in target languages for localization projects:

```python  theme={null}
# Find product reviews in target markets
target_languages = ["ja", "ko", "zh"]  # Asian markets

response = client.search.create(
    query="smartphone reviews 2024",
    max_results=15,
    search_language_filter=target_languages,
    search_recency_filter="month"
)
```

### Academic Research Across Languages

Access scholarly content in different languages:

```python  theme={null}
# Search for research papers in multiple languages
response = client.search.create(
    query="quantum computing algorithms",
    max_results=20,
    search_language_filter=["en", "de", "fr", "ru"],
    search_domain_filter=["arxiv.org", "nature.com", "science.org"]
)
```

### News Monitoring by Language

Track news stories across different language regions:

```python  theme={null}
# Monitor breaking news in different languages
news_queries = {
    "English": ["en"],
    "Chinese": ["zh"],
    "Spanish": ["es"],
    "Arabic": ["ar"]
}

for region, langs in news_queries.items():
    response = client.search.create(
        query="breaking news technology",
        max_results=5,
        search_language_filter=langs,
        search_recency_filter="day"
    )
    print(f"{region} News: {len(response.results)} articles")
```

## Error Handling

When using language filters, implement proper error handling for validation issues:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity, BadRequestError

  client = Perplexity()

  def safe_language_search(query, languages):
      """
      Perform a language-filtered search with error handling.
      """
      try:
          # Validate language codes
          if not isinstance(languages, list):
              raise ValueError("Languages must be provided as a list")
          
          if len(languages) > 10:
              raise ValueError("Maximum 10 language codes allowed")
          
          # Validate each code format
          for lang in languages:
              if not isinstance(lang, str) or len(lang) != 2 or not lang.islower():
                  raise ValueError(f"Invalid language code format: {lang}")
          
          # Perform search
          response = client.search.create(
              query=query,
              search_language_filter=languages,
              max_results=10
          )
          
          return response
          
      except ValueError as e:
          print(f"Validation error: {e}")
          return None
      except BadRequestError as e:
          print(f"API error: {e.message}")
          return None
      except Exception as e:
          print(f"Unexpected error: {e}")
          return None

  # Usage
  results = safe_language_search(
      "artificial intelligence",
      ["en", "fr", "de"]
  )

  if results:
      print(f"Found {len(results.results)} results")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  async function safeLanguageSearch(
    query: string,
    languages: string[]
  ): Promise<any | null> {
    try {
      // Validate language codes
      if (!Array.isArray(languages)) {
        throw new Error("Languages must be provided as an array");
      }
      
      if (languages.length > 10) {
        throw new Error("Maximum 10 language codes allowed");
      }
      
      // Validate each code format
      for (const lang of languages) {
        if (typeof lang !== 'string' || 
            lang.length !== 2 || 
            lang !== lang.toLowerCase()) {
          throw new Error(`Invalid language code format: ${lang}`);
        }
      }
      
      // Perform search
      const response = await client.search.create({
        query,
        searchLanguageFilter: languages,
        maxResults: 10
      });
      
      return response;
      
    } catch (error) {
      if (error instanceof Perplexity.BadRequestError) {
        console.error("API error:", error.message);
      } else if (error instanceof Error) {
        console.error("Error:", error.message);
      }
      return null;
    }
  }

  // Usage
  const results = await safeLanguageSearch(
    "artificial intelligence",
    ["en", "fr", "de"]
  );

  if (results) {
    console.log(`Found ${results.results.length} results`);
  }
  ```
</CodeGroup>

<Tip>
  For best results, combine language filtering with other filters like `search_domain_filter` or `search_recency_filter` to narrow down your search to highly relevant, timely content in your target languages.
</Tip>