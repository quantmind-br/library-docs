---
title: Performance Optimization
url: https://docs.perplexity.ai/docs/sdk/performance.md
source: llms
fetched_at: 2026-02-04T07:25:03.371027689-03:00
rendered_js: false
word_count: 517
summary: This document explains how to optimize the Perplexity SDKs for high-throughput applications using asynchronous operations, concurrent requests, and batch processing. It also covers advanced features like response streaming and direct access to raw response metadata and headers.
tags:
    - performance-optimization
    - async-programming
    - concurrency
    - batch-processing
    - rate-limiting
    - streaming
    - sdk-optimization
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance Optimization

> Learn how to optimize the Perplexity SDKs for high-throughput applications with async support, connection pooling, and raw response access.

## Overview

The Perplexity SDKs provide several features to optimize performance for high-throughput applications. This guide covers async operations, connection pooling, raw response access, and other performance optimization techniques.

## Async Support

### Basic Async Usage

For applications that need to handle multiple requests concurrently:

<CodeGroup>
  ```bash Python Installation theme={null}
  pip install perplexityai[aiohttp]
  ```

  ```bash TypeScript/JavaScript Installation theme={null}
  npm install @perplexity-ai/perplexity_ai
  # Async support is built-in with TypeScript/JavaScript
  ```
</CodeGroup>

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def main():
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          # Single async request
          search = await client.search.create(query="machine learning")
          print(search.results)

  asyncio.run(main())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function main() {
      const client = new Perplexity();
      
      // Async is built-in for TypeScript/JavaScript
      const search = await client.search.create({ query: "machine learning" });
      console.log(search.results);
  }

  main();
  ```
</CodeGroup>

### Concurrent Requests

Process multiple requests simultaneously for better throughput:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def concurrent_searches():
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          # Concurrent requests
          queries = ["AI", "machine learning", "deep learning", "neural networks"]
          tasks = [
              client.search.create(query=query)
              for query in queries
          ]
          
          results = await asyncio.gather(*tasks)
          
          for i, result in enumerate(results):
              print(f"Query '{queries[i]}': {len(result.results)} results")

  asyncio.run(concurrent_searches())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function concurrentSearches() {
      const client = new Perplexity();
      
      // Concurrent requests
      const queries = ["AI", "machine learning", "deep learning", "neural networks"];
      const tasks = queries.map(query => 
          client.search.create({ query })
      );
      
      const results = await Promise.all(tasks);
      
      results.forEach((result, i) => {
          console.log(`Query '${queries[i]}': ${result.results.length} results`);
      });
  }

  concurrentSearches();
  ```
</CodeGroup>

### Batch Processing with Rate Limiting

Process large numbers of requests while respecting rate limits:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def batch_process_with_limit(queries, batch_size=5, delay=1.0):
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          results = []
          
          for i in range(0, len(queries), batch_size):
              batch = queries[i:i + batch_size]
              
              # Process batch concurrently
              tasks = [
                  client.search.create(query=query)
                  for query in batch
              ]
              
              batch_results = await asyncio.gather(*tasks, return_exceptions=True)
              results.extend(batch_results)
              
              # Delay between batches to respect rate limits
              if i + batch_size < len(queries):
                  await asyncio.sleep(delay)
          
          return results

  # Usage
  queries = [f"query {i}" for i in range(20)]
  results = asyncio.run(batch_process_with_limit(queries))
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function batchProcessWithLimit(
      queries: string[], 
      batchSize: number = 5, 
      delay: number = 1000
  ) {
      const client = new Perplexity();
      const results = [];
      
      for (let i = 0; i < queries.length; i += batchSize) {
          const batch = queries.slice(i, i + batchSize);
          
          // Process batch concurrently
          const tasks = batch.map(query => 
              client.search.create({ query }).catch(error => error)
          );
          
          const batchResults = await Promise.all(tasks);
          results.push(...batchResults);
          
          // Delay between batches to respect rate limits
          if (i + batchSize < queries.length) {
              await new Promise(resolve => setTimeout(resolve, delay));
          }
      }
      
      return results;
  }

  // Usage
  const queries = Array.from({ length: 20 }, (_, i) => `query ${i}`);
  const results = await batchProcessWithLimit(queries);
  ```
</CodeGroup>

## Raw Response Access

Access headers, status codes, and raw response data for advanced use cases:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Get raw response with headers
  response = client.search.with_raw_response.create(
      query="machine learning"
  )

  print(f"Status Code: {response.status_code}")
  print(f"Request ID: {response.headers.get('X-Request-ID')}")
  print(f"Rate Limit Remaining: {response.headers.get('X-RateLimit-Remaining')}")
  print(f"Rate Limit Reset: {response.headers.get('X-RateLimit-Reset')}")

  # Parse the actual search results
  search = response.parse()
  print(f"Found {len(search.results)} results")
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Get raw response with headers
  const response = await client.search.withRawResponse.create({
      query: "machine learning"
  });

  console.log(`Status Code: ${response.response.status}`);
  console.log(`Request ID: ${response.response.headers.get('X-Request-ID')}`);
  console.log(`Rate Limit Remaining: ${response.response.headers.get('X-RateLimit-Remaining')}`);
  console.log(`Rate Limit Reset: ${response.response.headers.get('X-RateLimit-Reset')}`);

  // Parse the actual search results
  const search = response.parse();
  console.log(`Found ${search.results.length} results`);
  ```
</CodeGroup>

### Response Streaming

For chat completions, use streaming to get partial results as they arrive:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Stream chat completion responses
  stream = client.chat.completions.create(
      model="llama-3.1-sonar-large-128k-online",
      messages=[{"role": "user", "content": "Explain quantum computing"}],
      stream=True
  )

  for chunk in stream:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="", flush=True)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Stream chat completion responses
  const stream = await client.chat.completions.create({
      model: "llama-3.1-sonar-large-128k-online",
      messages: [{ role: "user", content: "Explain quantum computing" }],
      stream: true
  });

  for await (const chunk of stream) {
      if (chunk.choices[0]?.delta?.content) {
          process.stdout.write(chunk.choices[0].delta.content);
      }
  }
  ```
</CodeGroup>

## Connection Pooling

### Optimized Connection Settings

Configure connection pooling for better performance:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient, AsyncPerplexity, DefaultAioHttpClient

  # Sync client with optimized connection pooling
  limits = httpx.Limits(
      max_keepalive_connections=50,  # Keep connections alive
      max_connections=100,           # Total connection pool size
      keepalive_expiry=30.0         # Keep-alive timeout
  )

  sync_client = Perplexity(
      http_client=DefaultHttpxClient(limits=limits)
  )

  # Async client with optimized connection pooling
  async_limits = httpx.Limits(
      max_keepalive_connections=100,
      max_connections=200,
      keepalive_expiry=60.0
  )

  async def create_async_client():
      return AsyncPerplexity(
          http_client=DefaultAioHttpClient(limits=async_limits)
      )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  // Optimized HTTPS agent for connection pooling
  const optimizedAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 30000,  // 30 seconds
      maxSockets: 50,         // Max connections per host
      maxFreeSockets: 10,     // Max idle connections per host
      timeout: 60000          // Socket timeout
  });

  const client = new Perplexity({
      httpAgent: optimizedAgent
  });

  // For high-throughput applications
  const highThroughputAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 60000,
      maxSockets: 200,
      maxFreeSockets: 50,
      timeout: 120000
  });

  const clientHighThroughput = new Perplexity({
      httpAgent: highThroughputAgent
  });
  ```
</CodeGroup>

## Performance Monitoring

### Request Timing and Metrics

Monitor performance metrics to identify bottlenecks:

<CodeGroup>
  ```python Python theme={null}
  import time
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  class PerformanceMonitor:
      def __init__(self):
          self.request_times = []
          self.error_count = 0
          
      async def timed_request(self, client, query):
          start_time = time.time()
          try:
              result = await client.search.create(query=query)
              duration = time.time() - start_time
              self.request_times.append(duration)
              return result
          except Exception as e:
              self.error_count += 1
              raise e
      
      def get_stats(self):
          if not self.request_times:
              return {"error": "No successful requests"}
          
          return {
              "total_requests": len(self.request_times),
              "error_count": self.error_count,
              "avg_response_time": sum(self.request_times) / len(self.request_times),
              "min_response_time": min(self.request_times),
              "max_response_time": max(self.request_times)
          }

  async def run_performance_test():
      monitor = PerformanceMonitor()
      
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          queries = [f"test query {i}" for i in range(10)]
          
          tasks = [
              monitor.timed_request(client, query)
              for query in queries
          ]
          
          await asyncio.gather(*tasks, return_exceptions=True)
          
      print(monitor.get_stats())

  asyncio.run(run_performance_test())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class PerformanceMonitor {
      private requestTimes: number[] = [];
      private errorCount: number = 0;
      
      async timedRequest(client: Perplexity, query: string) {
          const startTime = performance.now();
          try {
              const result = await client.search.create({ query });
              const duration = performance.now() - startTime;
              this.requestTimes.push(duration);
              return result;
          } catch (error) {
              this.errorCount++;
              throw error;
          }
      }
      
      getStats() {
          if (this.requestTimes.length === 0) {
              return { error: "No successful requests" };
          }
          
          return {
              totalRequests: this.requestTimes.length,
              errorCount: this.errorCount,
              avgResponseTime: this.requestTimes.reduce((a, b) => a + b, 0) / this.requestTimes.length,
              minResponseTime: Math.min(...this.requestTimes),
              maxResponseTime: Math.max(...this.requestTimes)
          };
      }
  }

  async function runPerformanceTest() {
      const monitor = new PerformanceMonitor();
      const client = new Perplexity();
      
      const queries = Array.from({ length: 10 }, (_, i) => `test query ${i}`);
      
      const tasks = queries.map(query => 
          monitor.timedRequest(client, query).catch(error => error)
      );
      
      await Promise.all(tasks);
      
      console.log(monitor.getStats());
  }

  runPerformanceTest();
  ```
</CodeGroup>

## Memory Optimization

### Efficient Data Processing

Process large datasets efficiently with streaming and pagination:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  async def process_large_dataset(queries, process_fn):
      """Process queries in batches to manage memory usage"""
      
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          
          async def process_single(query):
              try:
                  result = await client.search.create(query=query)
                  # Process immediately to avoid storing in memory
                  processed = process_fn(result)
                  # Clear the original result from memory
                  del result
                  return processed
              except Exception as e:
                  return f"Error processing {query}: {e}"
          
          # Process in small batches
          batch_size = 5
          for i in range(0, len(queries), batch_size):
              batch = queries[i:i + batch_size]
              
              # Process batch
              tasks = [process_single(query) for query in batch]
              batch_results = await asyncio.gather(*tasks)
              
              # Yield results instead of accumulating
              for result in batch_results:
                  yield result
              
              # Optional: Small delay to prevent overwhelming the API
              await asyncio.sleep(0.1)

  # Usage
  async def summarize_result(search_result):
      """Process function that extracts only what we need"""
      return {
          "query": search_result.query,
          "result_count": len(search_result.results),
          "top_title": search_result.results[0].title if search_result.results else None
      }

  async def main():
      queries = [f"query {i}" for i in range(100)]
      
      async for processed_result in process_large_dataset(queries, summarize_result):
          print(processed_result)

  asyncio.run(main())
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  async function* processLargeDataset<T>(
      queries: string[], 
      processFn: (result: any) => T
  ): AsyncGenerator<T | string> {
      const client = new Perplexity();
      
      async function processSingle(query: string): Promise<T | string> {
          try {
              const result = await client.search.create({ query });
              // Process immediately to avoid storing in memory
              const processed = processFn(result);
              return processed;
          } catch (error) {
              return `Error processing ${query}: ${error}`;
          }
      }
      
      // Process in small batches
      const batchSize = 5;
      for (let i = 0; i < queries.length; i += batchSize) {
          const batch = queries.slice(i, i + batchSize);
          
          // Process batch
          const tasks = batch.map(query => processSingle(query));
          const batchResults = await Promise.all(tasks);
          
          // Yield results instead of accumulating
          for (const result of batchResults) {
              yield result;
          }
          
          // Optional: Small delay to prevent overwhelming the API
          await new Promise(resolve => setTimeout(resolve, 100));
      }
  }

  // Usage
  function summarizeResult(searchResult: any) {
      return {
          query: searchResult.query,
          resultCount: searchResult.results.length,
          topTitle: searchResult.results[0]?.title || null
      };
  }

  async function main() {
      const queries = Array.from({ length: 100 }, (_, i) => `query ${i}`);
      
      for await (const processedResult of processLargeDataset(queries, summarizeResult)) {
          console.log(processedResult);
      }
  }

  main();
  ```
</CodeGroup>

## Best Practices

<Steps>
  <Step title="Use async for concurrent operations">
    Always use async clients when you need to process multiple requests simultaneously.

    <Tip>
      For CPU-bound processing after API calls, consider using worker threads or processes.
    </Tip>
  </Step>

  <Step title="Implement connection pooling">
    Configure appropriate connection limits based on your application's needs.

    <CodeGroup>
      ```python Python theme={null}
      # Good: Optimized for your use case
      limits = httpx.Limits(
          max_keepalive_connections=20,  # Based on expected concurrency
          max_connections=50,
          keepalive_expiry=30.0
      )
      ```

      ```typescript TypeScript/JavaScript theme={null}
      // Good: Optimized for your use case
      const agent = new https.Agent({
          keepAlive: true,
          maxSockets: 20,  // Based on expected concurrency
          keepAliveMsecs: 30000
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Monitor and tune performance">
    Use metrics to identify bottlenecks and optimize accordingly.

    <Warning>
      Don't optimize prematurely - measure first, then optimize based on actual performance data.
    </Warning>
  </Step>

  <Step title="Handle backpressure">
    Implement proper rate limiting and backpressure handling for high-throughput applications.

    <CodeGroup>
      ```python Python theme={null}
      # Use semaphores to limit concurrent requests
      semaphore = asyncio.Semaphore(10)  # Max 10 concurrent requests

      async def rate_limited_request(client, query):
          async with semaphore:
              return await client.search.create(query=query)
      ```

      ```typescript TypeScript/JavaScript theme={null}
      // Use a queue or throttling library
      import pLimit from 'p-limit';

      const limit = pLimit(10);  // Max 10 concurrent requests

      const rateLimitedRequest = (client: Perplexity, query: string) =>
          limit(() => client.search.create({ query }));
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related Resources

<CardGroup cols={2}>
  <Card title="Configuration" icon="gear" href="/docs/sdk/configuration">
    Optimize connection pooling and timeouts
  </Card>

  <Card title="Error Handling" icon="triangle-exclamation" href="/docs/sdk/error-handling">
    Handle errors in async operations
  </Card>
</CardGroup>