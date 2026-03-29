---
title: Type Safety
url: https://docs.perplexity.ai/docs/sdk/type-safety.md
source: llms
fetched_at: 2026-02-04T07:25:10.019161681-03:00
rendered_js: false
word_count: 725
summary: This document explains how to implement type safety using TypeScript definitions and Python type hints within the Perplexity SDKs. It covers basic type usage, runtime validation, and advanced patterns like generic helpers and type guards.
tags:
    - type-safety
    - typescript
    - python
    - sdk
    - pydantic
    - type-hints
    - intellisense
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Type Safety

> Learn how to leverage full TypeScript definitions and Python type hints with the Perplexity SDKs for better development experience and code safety.

## Overview

Both Perplexity SDKs provide comprehensive type definitions to help you catch errors at development time and provide better IDE support. This guide covers type annotations, generic types, and advanced typing patterns.

## Basic Type Usage

### Type Imports and Annotations

Use type imports for better IDE support and type checking:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  from perplexity.types import (
      SearchCreateResponse,
      ChatCompletionCreateResponse,
      SearchResult,
      ChatCompletionMessage
  )

  client = Perplexity()

  # Type hints for better IDE support
  search_response: SearchCreateResponse = client.search.create(
      query="artificial intelligence"
  )

  # Access typed properties
  result: SearchResult = search_response.results[0]
  print(f"Title: {result.title}")
  print(f"URL: {result.url}")
  print(f"Snippet: {result.snippet}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // TypeScript provides full intellisense and type checking
  const searchResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({
      query: "artificial intelligence"
  });

  // Access typed properties with intellisense
  const result = searchResponse.results[0];
  console.log(`Title: ${result.title}`);
  console.log(`URL: ${result.url}`);
  console.log(`Snippet: ${result.snippet}`);
  ```
</CodeGroup>

### Runtime Type Validation

Python SDK uses Pydantic for runtime type validation:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse

  client = Perplexity()

  # Runtime validation ensures type safety
  try:
      search_response = client.search.create(
          query="machine learning",
          max_results=10
      )
      
      # Pydantic model methods for serialization
      json_data = search_response.to_json()
      dict_data = search_response.to_dict()
      
      # Type validation on field access
      first_result = search_response.results[0]
      print(f"Result type: {type(first_result)}")
      
  except ValueError as e:
      print(f"Type validation error: {e}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // TypeScript compile-time type checking
  const searchResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({
      query: "machine learning",
      max_results: 10  // TypeScript ensures correct property names
  });

  // Serialization (already plain objects)
  const jsonData = JSON.stringify(searchResponse);
  const objectData = searchResponse; // Already a plain object

  // Type safety at compile time
  const firstResult = searchResponse.results[0];
  console.log(`Result type available in IDE: ${typeof firstResult}`);
  ```
</CodeGroup>

## Advanced Type Patterns

### Generic Type Helpers

Create reusable typed functions:

<CodeGroup>
  ```python Python theme={null}
  from typing import TypeVar, Generic, List, Optional, Callable
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse, ChatCompletionCreateResponse

  T = TypeVar('T')
  R = TypeVar('R')

  class TypedPerplexityClient:
      def __init__(self, client: Perplexity):
          self.client = client
      
      def search_with_transform(
          self, 
          query: str, 
          transform: Callable[[SearchCreateResponse], T]
      ) -> T:
          """Perform search and transform the result with type safety"""
          response = self.client.search.create(query=query)
          return transform(response)
      
      def batch_search(
          self, 
          queries: List[str]
      ) -> List[SearchCreateResponse]:
          """Perform multiple searches with proper typing"""
          results = []
          for query in queries:
              response = self.client.search.create(query=query)
              results.append(response)
          return results

  # Usage with type safety
  client = TypedPerplexityClient(Perplexity())

  def extract_titles(response: SearchCreateResponse) -> List[str]:
      return [result.title for result in response.results]

  # Typed function call
  titles: List[str] = client.search_with_transform("AI research", extract_titles)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class TypedPerplexityClient {
      constructor(private client: Perplexity) {}
      
      async searchWithTransform<T>(
          query: string,
          transform: (response: Perplexity.Search.SearchCreateResponse) => T
      ): Promise<T> {
          const response = await this.client.search.create({ query });
          return transform(response);
      }
      
      async batchSearch(queries: string[]): Promise<Perplexity.Search.SearchCreateResponse[]> {
          const tasks = queries.map(query => 
              this.client.search.create({ query })
          );
          return Promise.all(tasks);
      }
  }

  // Usage with type safety
  const client = new TypedPerplexityClient(new Perplexity());

  function extractTitles(response: Perplexity.Search.SearchCreateResponse): string[] {
      return response.results.map(result => result.title);
  }

  // Typed function call with full intellisense
  const titles: string[] = await client.searchWithTransform("AI research", extractTitles);
  ```
</CodeGroup>

### Custom Type Guards

Create type guards for safer type checking:

<CodeGroup>
  ```python Python theme={null}
  from typing import Union, TypeGuard
  from perplexity.types import (
      SearchCreateResponse, 
      ChatCompletionCreateResponse,
      SearchResult
  )

  def is_search_response(
      response: Union[SearchCreateResponse, ChatCompletionCreateResponse]
  ) -> TypeGuard[SearchCreateResponse]:
      """Type guard to check if response is a search response"""
      return hasattr(response, 'results')

  def is_valid_search_result(result: SearchResult) -> TypeGuard[SearchResult]:
      """Type guard to validate search result structure"""
      return (
          hasattr(result, 'title') and 
          hasattr(result, 'url') and 
          hasattr(result, 'snippet') and
          result.title is not None and
          result.url is not None
      )

  # Usage
  def process_response(
      response: Union[SearchCreateResponse, ChatCompletionCreateResponse]
  ) -> None:
      if is_search_response(response):
          # TypeScript now knows this is SearchCreateResponse
          for result in response.results:
              if is_valid_search_result(result):
                  print(f"Valid result: {result.title}")
              else:
                  print("Invalid result format")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  function isSearchResponse(
      response: Perplexity.Search.SearchCreateResponse | Perplexity.StreamChunk
  ): response is Perplexity.Search.SearchCreateResponse {
      return 'results' in response;
  }

  function isValidSearchResult(result: { title: string; url: string; snippet: string }): boolean {
      return (
          typeof result.title === 'string' &&
          typeof result.url === 'string' &&
          typeof result.snippet === 'string' &&
          result.title.length > 0 &&
          result.url.length > 0
      );
  }

  // Usage
  function processResponse(
      response: Perplexity.Search.SearchCreateResponse | Perplexity.StreamChunk
  ): void {
      if (isSearchResponse(response)) {
          // TypeScript now knows this is SearchCreateResponse
          response.results.forEach(result => {
              if (isValidSearchResult(result)) {
                  console.log(`Valid result: ${result.title}`);
              } else {
                  console.log("Invalid result format");
              }
          });
      }
  }
  ```
</CodeGroup>

## Response Type Utilities

### Extracting Nested Types

Work with nested response structures safely:

<CodeGroup>
  ```python Python theme={null}
  from typing import List, Optional
  from perplexity import Perplexity
  from perplexity.types import (
      SearchCreateResponse,
      SearchResult,
      ChatCompletionCreateResponse,
      ChatCompletionChoice
  )

  class ResponseUtils:
      @staticmethod
      def extract_search_titles(response: SearchCreateResponse) -> List[str]:
          """Extract all search result titles with type safety"""
          return [result.title for result in response.results if result.title]
      
      @staticmethod
      def extract_search_urls(response: SearchCreateResponse) -> List[str]:
          """Extract all search result URLs with type safety"""
          return [result.url for result in response.results if result.url]
      
      @staticmethod
      def get_first_search_result(
          response: SearchCreateResponse
      ) -> Optional[SearchResult]:
          """Get first search result safely"""
          return response.results[0] if response.results else None
      
      @staticmethod
      def extract_chat_content(
          response: ChatCompletionCreateResponse
      ) -> Optional[str]:
          """Extract chat completion content safely"""
          if response.choices and response.choices[0].message:
              return response.choices[0].message.content
          return None

  # Usage
  client = Perplexity()
  search_response = client.search.create(query="Python programming")

  titles = ResponseUtils.extract_search_titles(search_response)
  urls = ResponseUtils.extract_search_urls(search_response)
  first_result = ResponseUtils.get_first_search_result(search_response)

  print(f"Found {len(titles)} results")
  if first_result:
      print(f"First result: {first_result.title}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class ResponseUtils {
      static extractSearchTitles(response: Perplexity.Search.SearchCreateResponse): string[] {
          return response.results
              .filter(result => result.title)
              .map(result => result.title);
      }
      
      static extractSearchUrls(response: Perplexity.Search.SearchCreateResponse): string[] {
          return response.results
              .filter(result => result.url)
              .map(result => result.url);
      }
      
      static getFirstSearchResult(
          response: Perplexity.Search.SearchCreateResponse
      ) {
          return response.results[0];
      }
      
      static extractChatContent(
          response: Perplexity.StreamChunk
      ): string | undefined {
          const content = response.choices[0]?.message?.content;
          // Handle content which can be string, array of chunks, or null
          if (typeof content === 'string') {
              return content;
          }
          if (Array.isArray(content)) {
              // Extract text from content chunks
              return content
                  .filter(chunk => chunk.type === 'text' && 'text' in chunk)
                  .map(chunk => (chunk as { text: string }).text)
                  .join('');
          }
          return undefined;
      }
  }

  // Usage
  const client = new Perplexity();
  const searchResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({ 
      query: "Python programming" 
  });

  const titles = ResponseUtils.extractSearchTitles(searchResponse);
  const urls = ResponseUtils.extractSearchUrls(searchResponse);
  const firstResult = ResponseUtils.getFirstSearchResult(searchResponse);

  console.log(`Found ${titles.length} results`);
  if (firstResult) {
      console.log(`First result: ${firstResult.title}`);
  }
  ```
</CodeGroup>

### Custom Response Mappers

Create typed mappers for domain-specific data structures:

<CodeGroup>
  ```python Python theme={null}
  from typing import List, Optional, Dict, Any
  from dataclasses import dataclass
  from perplexity.types import SearchCreateResponse, SearchResult

  @dataclass
  class SimplifiedSearchResult:
      title: str
      url: str
      snippet: str
      domain: str

  @dataclass
  class SearchSummary:
      query: str
      total_results: int
      results: List[SimplifiedSearchResult]
      domains: List[str]

  class SearchResponseMapper:
      @staticmethod
      def to_simplified(response: SearchCreateResponse) -> SearchSummary:
          """Convert API response to simplified domain model"""
          simplified_results = []
          domains = set()
          
          for result in response.results:
              if result.title and result.url and result.snippet:
                  # Extract domain from URL
                  try:
                      from urllib.parse import urlparse
                      domain = urlparse(result.url).netloc
                      domains.add(domain)
                      
                      simplified_results.append(SimplifiedSearchResult(
                          title=result.title,
                          url=result.url,
                          snippet=result.snippet,
                          domain=domain
                      ))
                  except Exception:
                      # Skip invalid URLs
                      continue
          
          return SearchSummary(
              query=response.query,
              total_results=len(simplified_results),
              results=simplified_results,
              domains=list(domains)
          )

  # Usage with type safety
  client = Perplexity()
  api_response = client.search.create(query="machine learning frameworks")
  summary: SearchSummary = SearchResponseMapper.to_simplified(api_response)

  print(f"Query: {summary.query}")
  print(f"Results: {summary.total_results}")
  print(f"Unique domains: {len(summary.domains)}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  interface SimplifiedSearchResult {
      title: string;
      url: string;
      snippet: string;
      domain: string;
  }

  interface SearchSummary {
      query: string;
      totalResults: number;
      results: SimplifiedSearchResult[];
      domains: string[];
  }

  class SearchResponseMapper {
      static toSimplified(response: Perplexity.Search.SearchCreateResponse): SearchSummary {
          const simplifiedResults: SimplifiedSearchResult[] = [];
          const domains = new Set<string>();
          
          for (const result of response.results) {
              if (result.title && result.url && result.snippet) {
                  try {
                      const domain = new URL(result.url).hostname;
                      domains.add(domain);
                      
                      simplifiedResults.push({
                          title: result.title,
                          url: result.url,
                          snippet: result.snippet,
                          domain
                      });
                  } catch {
                      // Skip invalid URLs
                      continue;
                  }
              }
          }
          
          return {
              query: response.id, // response.id contains the search identifier
              totalResults: simplifiedResults.length,
              results: simplifiedResults,
              domains: Array.from(domains)
          };
      }
  }

  // Usage with type safety
  const client = new Perplexity();
  const apiResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({ 
      query: "machine learning frameworks" 
  });
  const summary: SearchSummary = SearchResponseMapper.toSimplified(apiResponse);

  console.log(`ID: ${summary.query}`);
  console.log(`Results: ${summary.totalResults}`);
  console.log(`Unique domains: ${summary.domains.length}`);
  ```
</CodeGroup>

## IDE Integration

### Enhanced Development Experience

Maximize IDE support with proper type usage:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse
  from typing import TYPE_CHECKING

  if TYPE_CHECKING:
      # Import types only for type checking (no runtime cost)
      from perplexity.types import ChatCompletionCreateResponse

  class EnhancedClient:
      def __init__(self):
          self.client = Perplexity()
      
      def search(self, query: str, **kwargs) -> SearchCreateResponse:
          """
          Perform search with full type hints
          
          Args:
              query: Search query string
              **kwargs: Additional search parameters
              
          Returns:
              SearchCreateResponse: Typed search results
          """
          return self.client.search.create(query=query, **kwargs)
      
      def chat(self, message: str, model: str = "sonar-pro") -> "ChatCompletionCreateResponse":
          """
          Chat completion with type hints
          
          Args:
              message: User message
              model: Model to use for completion
              
          Returns:
              ChatCompletionCreateResponse: Typed chat response
          """
          return self.client.chat.completions.create(
              model=model,
              messages=[{"role": "user", "content": message}]
          )

  # Usage with full IDE support
  enhanced_client = EnhancedClient()

  # IDE provides full autocomplete and type checking
  search_result = enhanced_client.search("Python tutorials")
  print(search_result.results[0].title)  # Full intellisense available

  chat_result = enhanced_client.chat("Explain decorators")
  # Access content safely (can be string, list, or None)
  content = chat_result.choices[0].message.content
  if isinstance(content, str):
      print(content)  # Type-safe access
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class EnhancedClient {
      private client: Perplexity;
      
      constructor() {
          this.client = new Perplexity();
      }
      
      /**
       * Perform search with full type hints
       */
      async search(
          query: string, 
          options?: Partial<Perplexity.Search.SearchCreateParams>
      ): Promise<Perplexity.Search.SearchCreateResponse> {
          return this.client.search.create({ 
              query, 
              ...options 
          });
      }
      
      /**
       * Chat completion with type hints
       */
      async chat(
          message: string, 
          model: string = "sonar"
      ): Promise<Perplexity.StreamChunk> {
          return this.client.chat.completions.create({
              model,
              messages: [{ role: "user", content: message }]
          });
      }
  }

  // Usage with full IDE support
  const enhancedClient = new EnhancedClient();

  // IDE provides full autocomplete and type checking
  const searchResult = await enhancedClient.search("Python tutorials");
  console.log(searchResult.results[0].title); // Full intellisense available

  const chatResult = await enhancedClient.chat("Explain decorators");
  // Content can be string, array of chunks, or null - handle appropriately
  const content = chatResult.choices[0]?.message?.content;
  if (typeof content === 'string') {
      console.log(content); // Type-safe access
  }
  ```
</CodeGroup>

## Type Safety Best Practices

<Steps>
  <Step title="Always use type imports">
    Import and use specific types for better IDE support and error catching.

    <CodeGroup>
      ```python Python theme={null}
      # Good: Specific type imports
      from perplexity.types import SearchCreateResponse, SearchResult

      def process_search(response: SearchCreateResponse) -> List[str]:
          return [result.title for result in response.results]
      ```

      ```typescript TypeScript/JavaScript theme={null}
      // Good: Use namespace types for type safety
      import Perplexity from '@perplexity-ai/perplexity_ai';

      function processSearch(response: Perplexity.Search.SearchCreateResponse): string[] {
          return response.results.map(result => result.title);
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Use type guards for runtime safety">
    Implement proper type checking for dynamic data.

    <Warning>
      TypeScript types are compile-time only. Use type guards for runtime validation.
    </Warning>
  </Step>

  <Step title="Leverage generic types">
    Create reusable typed functions and classes for common patterns.

    <Tip>
      Generic types help maintain type safety while providing flexibility.
    </Tip>
  </Step>

  <Step title="Document with types">
    Use type annotations as documentation for better code maintainability.

    <CodeGroup>
      ```python Python theme={null}
      def analyze_search_results(
          response: SearchCreateResponse,
          min_score: float = 0.5
      ) -> Dict[str, Any]:
          """
          Analyze search results with scoring
          
          Args:
              response: Search API response
              min_score: Minimum quality score threshold
              
          Returns:
              Analysis results with scores and recommendations
          """
          # Implementation with type safety
      ```

      ```typescript TypeScript/JavaScript theme={null}
      /**
       * Analyze search results with scoring
       */
      function analyzeSearchResults(
          response: Perplexity.Search.SearchCreateResponse,
          minScore: number = 0.5
      ): { scores: number[]; recommendations: string[] } {
          // Implementation with type safety
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related Resources

<CardGroup cols={2}>
  <Card title="Error Handling" icon="triangle-exclamation" href="/docs/sdk/error-handling">
    Type-safe error handling patterns
  </Card>

  <Card title="Best Practices" icon="star" href="/docs/sdk/best-practices">
    Type safety in production code
  </Card>
</CardGroup>