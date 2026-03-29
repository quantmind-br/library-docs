---
title: Error Handling
url: https://docs.perplexity.ai/docs/sdk/error-handling.md
source: llms
fetched_at: 2026-02-04T07:24:57.566497974-03:00
rendered_js: false
word_count: 310
summary: This document explains how to identify and manage various API error types using the Perplexity SDKs for Python and JavaScript. It provides strategies for basic error catching, advanced retry logic with exponential backoff, and implementing fallback mechanisms for robust applications.
tags:
    - error-handling
    - perplexity-sdk
    - python
    - typescript
    - rate-limiting
    - api-integration
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Handling

> Learn how to handle API errors gracefully with the Perplexity SDKs for Python and TypeScript/JavaScript.

## Overview

The Perplexity SDKs provide robust error handling with specific exception types for different error scenarios. This guide covers how to catch and handle common API errors gracefully.

## Common Error Types

The SDKs provide specific exception types for different error scenarios:

* **APIConnectionError** - Network connection issues
* **RateLimitError** - API rate limit exceeded
* **APIStatusError** - HTTP status errors (4xx, 5xx)
* **AuthenticationError** - Invalid API key or authentication issues
* **ValidationError** - Invalid request parameters

## Basic Error Handling

Handle common API errors with try-catch blocks:

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  client = Perplexity()

  try:
      search = client.search.create(query="machine learning")
      print(search.results)
  except perplexity.APIConnectionError as e:
      print("Network connection failed")
      print(e.__cause__)
  except perplexity.RateLimitError as e:
      print("Rate limit exceeded, please retry later")
  except perplexity.APIStatusError as e:
      print(f"API error: {e.status_code}")
      print(e.response)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  try {
      const search = await client.search.create({ query: "machine learning" });
      console.log(search.results);
  } catch (error) {
      if (error.constructor.name === 'APIConnectionError') {
          console.log("Network connection failed");
          console.log(error.cause);
      } else if (error.constructor.name === 'RateLimitError') {
          console.log("Rate limit exceeded, please retry later");
      } else if (error.constructor.name === 'APIStatusError') {
          console.log(`API error: ${error.status}`);
          console.log(error.response);
      }
  }
  ```
</CodeGroup>

<Info>
  Common HTTP status codes: 400 (Bad Request), 401 (Authentication), 403 (Permission Denied), 404 (Not Found), 429 (Rate Limit), 500+ (Server Error).
</Info>

## Advanced Error Handling

### Exponential Backoff for Rate Limits

Implement intelligent retry logic for rate limit errors:

<CodeGroup>
  ```python Python theme={null}
  import time
  import random
  import perplexity
  from perplexity import Perplexity

  def search_with_retry(client, query, max_retries=3):
      for attempt in range(max_retries):
          try:
              return client.search.create(query=query)
          except perplexity.RateLimitError:
              if attempt == max_retries - 1:
                  raise  # Re-raise on final attempt
              
              # Exponential backoff with jitter
              delay = (2 ** attempt) + random.uniform(0, 1)
              print(f"Rate limited. Retrying in {delay:.2f} seconds...")
              time.sleep(delay)
          except perplexity.APIConnectionError:
              if attempt == max_retries - 1:
                  raise
              
              # Shorter delay for connection errors
              delay = 1 + random.uniform(0, 1)
              print(f"Connection error. Retrying in {delay:.2f} seconds...")
              time.sleep(delay)

  # Usage
  client = Perplexity()
  result = search_with_retry(client, "artificial intelligence")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function searchWithRetry(
      client: Perplexity, 
      query: string, 
      maxRetries: number = 3
  ) {
      for (let attempt = 0; attempt < maxRetries; attempt++) {
          try {
              return await client.search.create({ query });
          } catch (error) {
              if (attempt === maxRetries - 1) {
                  throw error; // Re-throw on final attempt
              }
              
              if (error.constructor.name === 'RateLimitError') {
                  // Exponential backoff with jitter
                  const delay = (2 ** attempt + Math.random()) * 1000;
                  console.log(`Rate limited. Retrying in ${delay}ms...`);
                  await new Promise(resolve => setTimeout(resolve, delay));
              } else if (error.constructor.name === 'APIConnectionError') {
                  // Shorter delay for connection errors
                  const delay = (1 + Math.random()) * 1000;
                  console.log(`Connection error. Retrying in ${delay}ms...`);
                  await new Promise(resolve => setTimeout(resolve, delay));
              } else {
                  throw error; // Don't retry other errors
              }
          }
      }
  }

  // Usage
  const client = new Perplexity();
  const result = await searchWithRetry(client, "artificial intelligence");
  ```
</CodeGroup>

### Error Context and Debugging

Extract detailed error information for debugging:

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  client = Perplexity()

  try:
      chat = client.chat.completions.create(
          model="sonar-pro",
          messages=[{"role": "user", "content": "What's the weather?"}]
      )
  except perplexity.APIStatusError as e:
      print(f"Status Code: {e.status_code}")
      print(f"Error Type: {e.type}")
      print(f"Error Message: {e.message}")
      
      # Access raw response for detailed debugging
      if hasattr(e, 'response'):
          print(f"Raw Response: {e.response.text}")
          print(f"Request ID: {e.response.headers.get('X-Request-ID')}")
          
  except perplexity.ValidationError as e:
      print(f"Validation Error: {e}")
      # Handle parameter validation errors
      
  except Exception as e:
      print(f"Unexpected error: {type(e).__name__}: {e}")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  try {
      const chat = await client.chat.completions.create({
          model: "sonar-pro",
          messages: [{ role: "user", content: "What's the weather?" }]
      });
  } catch (error: any) {
      if (error.constructor.name === 'APIStatusError') {
          console.log(`Status Code: ${error.status}`);
          console.log(`Error Type: ${error.type}`);
          console.log(`Error Message: ${error.message}`);
          
          // Access raw response for detailed debugging
          if (error.response) {
              console.log(`Raw Response: ${await error.response.text()}`);
              console.log(`Request ID: ${error.response.headers.get('X-Request-ID')}`);
          }
      } else if (error.constructor.name === 'ValidationError') {
          console.log(`Validation Error: ${error.message}`);
          // Handle parameter validation errors
      } else {
          console.log(`Unexpected error: ${error.constructor.name}: ${error.message}`);
      }
  }
  ```
</CodeGroup>

## Error Recovery Strategies

### Graceful Degradation

Implement fallback mechanisms when API calls fail:

<CodeGroup>
  ```python Python theme={null}
  import perplexity
  from perplexity import Perplexity

  def get_ai_response(query, fallback_response="I'm sorry, I'm temporarily unavailable."):
      client = Perplexity()
      
      try:
          # Primary: Try online model
          response = client.chat.completions.create(
              model="sonar-pro",
              messages=[{"role": "user", "content": query}]
          )
          return response.choices[0].message.content
          
      except perplexity.RateLimitError:
          try:
              # Fallback: Try offline model if rate limited
              response = client.chat.completions.create(
                  model="llama-3.1-8b-instruct",
                  messages=[{"role": "user", "content": query}]
              )
              return response.choices[0].message.content
          except Exception:
              return fallback_response
              
      except perplexity.APIConnectionError:
          # Network issues - return cached response or fallback
          return fallback_response
          
      except Exception as e:
          print(f"Unexpected error: {e}")
          return fallback_response

  # Usage
  response = get_ai_response("What is machine learning?")
  print(response)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function getAIResponse(
      query: string, 
      fallbackResponse: string = "I'm sorry, I'm temporarily unavailable."
  ): Promise<string> {
      const client = new Perplexity();
      
      try {
          // Primary: Try online model
          const response = await client.chat.completions.create({
              model: "sonar-pro",
              messages: [{ role: "user", content: query }]
          });
          return response.choices[0].message.content || "";
          
      } catch (error: any) {
          if (error.constructor.name === 'RateLimitError') {
              try {
                  // Fallback: Try offline model if rate limited
                  const response = await client.chat.completions.create({
                      model: "llama-3.1-8b-instruct",
                      messages: [{ role: "user", content: query }]
                  });
                  return response.choices[0].message.content || "";
              } catch {
                  return fallbackResponse;
              }
          } else if (error.constructor.name === 'APIConnectionError') {
              // Network issues - return cached response or fallback
              return fallbackResponse;
          } else {
              console.log(`Unexpected error: ${error.message}`);
              return fallbackResponse;
          }
      }
  }

  // Usage
  const response = await getAIResponse("What is machine learning?");
  console.log(response);
  ```
</CodeGroup>

## Best Practices

<Steps>
  <Step title="Always handle rate limits">
    Rate limiting is common with API usage. Always implement retry logic with exponential backoff.

    <Warning>
      Don't implement aggressive retry loops without delays - this can worsen rate limiting.
    </Warning>
  </Step>

  <Step title="Log errors for monitoring">
    Include proper logging to track error patterns and API health.

    <CodeGroup>
      ```python Python theme={null}
      import logging
      import perplexity

      logging.basicConfig(level=logging.INFO)
      logger = logging.getLogger(__name__)

      try:
          result = client.search.create(query="example")
      except perplexity.APIStatusError as e:
          logger.error(f"API Error {e.status_code}: {e.message}", 
                      extra={'request_id': e.response.headers.get('X-Request-ID')})
      ```

      ```typescript TypeScript/JavaScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      try {
          const result = await client.search.create({ query: "example" });
      } catch (error: any) {
          console.error(`API Error ${error.status}: ${error.message}`, {
              requestId: error.response?.headers.get('X-Request-ID')
          });
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Set appropriate timeouts">
    Configure timeouts to prevent hanging requests.

    <CodeGroup>
      ```python Python theme={null}
      import httpx
      from perplexity import Perplexity

      client = Perplexity(
          timeout=httpx.Timeout(connect=5.0, read=30.0, write=5.0, pool=10.0)
      )
      ```

      ```typescript TypeScript/JavaScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity({
          timeout: 30000 // 30 seconds
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Handle authentication errors">
    Check for invalid API keys and provide helpful error messages.

    <CodeGroup>
      ```python Python theme={null}
      try:
          result = client.search.create(query="test")
      except perplexity.AuthenticationError:
          print("Invalid API key. Please check your PERPLEXITY_API_KEY environment variable.")
      ```

      ```typescript TypeScript/JavaScript theme={null}
      try {
          const result = await client.search.create({ query: "test" });
      } catch (error: any) {
          if (error.constructor.name === 'AuthenticationError') {
              console.log("Invalid API key. Please check your PERPLEXITY_API_KEY environment variable.");
          }
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related Resources

<CardGroup cols={2}>
  <Card title="Configuration" icon="gear" href="/docs/sdk/configuration">
    Configure timeouts and retries
  </Card>

  <Card title="Best Practices" icon="star" href="/docs/sdk/best-practices">
    Environment variables and rate limiting
  </Card>
</CardGroup>