---
title: Streaming Responses
url: https://docs.perplexity.ai/docs/grounded-llm/output-control/streaming-responses.md
source: llms
fetched_at: 2026-02-04T07:24:06.962483864-03:00
rendered_js: false
word_count: 278
summary: This document explains how to implement and process real-time streaming responses using Perplexity's SDKs and APIs, including handling metadata and search results.
tags:
    - streaming
    - perplexity-api
    - real-time-responses
    - python-sdk
    - typescript-sdk
    - metadata-handling
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Streaming Responses

> Learn how to stream real-time responses using Perplexity's SDKs and APIs

## Overview

Streaming allows you to receive partial responses from the Perplexity API as they are generated, rather than waiting for the complete response. This is particularly useful for:

* **Real-time user experiences** - Display responses as they're generated
* **Long responses** - Start showing content immediately for lengthy analyses
* **Interactive applications** - Provide immediate feedback to users

<Info>
  Streaming is supported across all Perplexity models and both Chat Completions and Agentic Research APIs.
</Info>

## Quick Start

The easiest way to get started is with the Perplexity SDKs, which handle all the streaming parsing automatically.

To enable streaming, set `stream=True` (Python) or `stream: true` (TypeScript) when creating completions:

<Tabs>
  <Tab title="Agentic Research API">
    <CodeGroup>
      ```python Python SDK theme={null}
      from perplexity import Perplexity

      # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      client = Perplexity()

      # Create streaming response
      stream = client.responses.create(
          preset="fast-search",
          input="What is the latest in AI research?",
          stream=True
      )

      # Process streaming response
      for event in stream:
          if event.type == "response.output_text.delta":
              print(event.delta, end="")
      ```

      ```typescript TypeScript SDK theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      // Create streaming response
      const stream = await client.responses.create({
        preset: "fast-search",
        input: "What is the latest in AI research?",
        stream: true
      });

      // Process streaming response
      for await (const event of stream) {
        if (event.type === "response.output_text.delta") {
          process.stdout.write(event.delta);
        }
      }
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/v1/responses" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "preset": "fast-search",
          "input": "What is the latest in AI research?",
          "stream": true
        }'
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Chat Completions API">
    <CodeGroup>
      ```python Python SDK theme={null}
      from perplexity import Perplexity

      # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
      client = Perplexity()

      # Create streaming completion
      stream = client.chat.completions.create(
          model="sonar",
          messages=[{"role": "user", "content": "What is the latest in AI research?"}],
          stream=True
      )

      # Process streaming response
      for chunk in stream:
          if chunk.choices[0].delta.content:
              print(chunk.choices[0].delta.content, end="")
      ```

      ```typescript TypeScript SDK theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      const client = new Perplexity();

      // Create streaming completion
      const stream = await client.chat.completions.create({
        model: "sonar",
        messages: [{ role: "user", content: "What is the latest in AI research?" }],
        stream: true
      });

      // Process streaming response
      for await (const chunk of stream) {
        if (chunk.choices[0]?.delta?.content) {
          process.stdout.write(chunk.choices[0].delta.content);
        }
      }
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.perplexity.ai/chat/completions" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "sonar",
          "messages": [{"role": "user", "content": "What is the latest in AI research?"}],
          "stream": true
        }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Search Results and Metadata During Streaming

<Info>
  Search results and metadata are delivered in the **final chunk(s)** of a streaming response, not progressively during the stream.
</Info>

### How Metadata Works with Streaming

When streaming, you receive:

1. **Content chunks** which arrive progressively in real-time
2. **Search results** (delivered in the final chunk(s))
3. **Usage stats** and other metadata

### Collecting Metadata During Streaming

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
    from perplexity import Perplexity

    def stream_with_metadata():
        client = Perplexity()
        
        stream = client.chat.completions.create(
            model="sonar",
            messages=[{"role": "user", "content": "Explain quantum computing"}],
            stream=True
        )
        
        content = ""
        search_results = []
        usage_info = None
        
        for chunk in stream:
            # Process content
            if chunk.choices[0].delta.content:
                content_piece = chunk.choices[0].delta.content
                content += content_piece
                print(content_piece, end='', flush=True)
            
            # Collect metadata from final chunks
            if hasattr(chunk, 'search_results') and chunk.search_results:
                search_results = chunk.search_results
                
            if hasattr(chunk, 'usage') and chunk.usage:
                usage_info = chunk.usage
                
            # Check if streaming is complete
            if chunk.choices[0].finish_reason:
                print(f"\n\nSearch Results: {search_results}")
                print(f"Usage: {usage_info}")
        
        return content, search_results, usage_info

    stream_with_metadata()
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    async function streamWithMetadata(query: string) {
      const client = new Perplexity();
      
      const stream = await client.chat.completions.create({
        model: "sonar",
        messages: [{ role: "user", content: query }],
        stream: true
      });

      let content = "";
      let searchResults: any[] = [];
      let usage: any = undefined;

      for await (const chunk of stream) {
        // Process content
        if (chunk.choices[0]?.delta?.content) {
          const contentPiece = chunk.choices[0].delta.content;
          content += contentPiece;
          process.stdout.write(contentPiece);
        }

        // Collect metadata from final chunks
        if (chunk.search_results) {
          searchResults = chunk.search_results;
        }

        if (chunk.usage) {
          usage = chunk.usage;
        }

        // Check if streaming is complete
        if (chunk.choices[0]?.finish_reason) {
          console.log(`\n\nSearch Results:`, searchResults);
          console.log(`Usage:`, usage);
        }
      }

      return { content, searchResults, usage };
    }

    // Usage
    const result = await streamWithMetadata("Explain quantum computing");
    ```
  </Tab>

  <Tab title="Raw HTTP">
    ```python  theme={null}
    import requests
    import json

    def stream_with_requests_metadata():
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar",
            "messages": [{"role": "user", "content": "Explain quantum computing"}],
            "stream": True
        }
        
        response = requests.post(url, headers=headers, json=payload, stream=True)
        
        content = ""
        metadata = {}
        
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    data_str = line[6:]
                    if data_str == '[DONE]':
                        break
                    try:
                        chunk = json.loads(data_str)
                        
                        # Process content
                        if 'choices' in chunk and chunk['choices'][0]['delta'].get('content'):
                            content_piece = chunk['choices'][0]['delta']['content']
                            content += content_piece
                            print(content_piece, end='', flush=True)
                        
                        # Collect metadata
                        for key in ['search_results', 'usage']:
                            if key in chunk:
                                metadata[key] = chunk[key]
                                
                        # Check if streaming is complete
                        if chunk['choices'][0].get('finish_reason'):
                            print(f"\n\nMetadata: {metadata}")
                            
                    except json.JSONDecodeError:
                        continue
        
        return content, metadata

    stream_with_requests_metadata()
    ```
  </Tab>
</Tabs>

## Error Handling

Proper error handling is important to ensure your application can recover from errors and provide a good user experience.

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
    import perplexity
    from perplexity import Perplexity

    client = Perplexity()

    try:
        stream = client.chat.completions.create(
            model="sonar-pro",
            messages=[
                {"role": "user", "content": "Explain machine learning concepts"}
            ],
            stream=True
        )
        
        content = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content_chunk = chunk.choices[0].delta.content
                content += content_chunk
                print(content_chunk, end="")
                
    except perplexity.APIConnectionError as e:
        print(f"Network connection failed: {e}")
    except perplexity.RateLimitError as e:
        print(f"Rate limit exceeded, please retry later: {e}")
    except perplexity.APIStatusError as e:
        print(f"API error {e.status_code}: {e.response}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    import Perplexity from '@perplexity-ai/perplexity_ai';

    const client = new Perplexity();

    try {
      const stream = await client.chat.completions.create({
        model: "sonar-pro",
        messages: [
          { role: "user", content: "Explain machine learning concepts" }
        ],
        stream: true
      });
      
      for await (const chunk of stream) {
        if (chunk.choices[0]?.delta?.content) {
          process.stdout.write(chunk.choices[0].delta.content);
        }
      }
    } catch (error) {
      if (error instanceof Perplexity.APIConnectionError) {
        console.error("Network connection failed:", error.cause);
      } else if (error instanceof Perplexity.RateLimitError) {
        console.error("Rate limit exceeded, please retry later");
      } else if (error instanceof Perplexity.APIError) {
        console.error(`API error ${error.status}: ${error.message}`);
      } else {
        console.error("Unexpected error:", error);
      }
    }
    ```
  </Tab>

  <Tab title="Raw HTTP">
    ```python  theme={null}
    import requests
    import time
    import json

    def stream_with_retry(max_retries=3):
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        data = {
            "model": "sonar-pro",
            "messages": [
                {"role": "system", "content": "Be precise and concise."},
                {"role": "user", "content": "Explain machine learning concepts"}
            ],
            "stream": True,
            "max_tokens": 1000
        }

        for attempt in range(max_retries):
            try:
                with requests.post(url, headers=headers, json=data, stream=True, timeout=300) as resp:
                    resp.raise_for_status()
                    for line in resp.iter_lines(decode_unicode=True):
                        if line and line.startswith("data: "):
                            chunk_data = line[len("data: "):]
                            if chunk_data == "[DONE]":
                                break
                            try:
                                chunk = json.loads(chunk_data)
                                content = chunk["choices"][0].get("delta", {}).get("content")
                                if content:
                                    print(content, end="", flush=True)
                            except json.JSONDecodeError:
                                continue
                break
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    raise

    stream_with_retry()
    ```
  </Tab>
</Tabs>

## Proper SSE Parsing

For production use, you should properly parse Server-Sent Events (SSE) format:

<Tabs>
  <Tab title="Python with SSE Library">
    ```python  theme={null}
    # pip install sseclient-py
    import sseclient
    import requests
    import json

    def stream_with_proper_sse():
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar",
            "messages": [{"role": "user", "content": "Explain quantum computing"}],
            "stream": True
        }
        
        response = requests.post(url, headers=headers, json=payload, stream=True)
        client = sseclient.SSEClient(response)
        
        for event in client.events():
            if event.data == '[DONE]':
                break
            try:
                chunk_data = json.loads(event.data)
                content = chunk_data['choices'][0]['delta'].get('content', '')
                if content:
                    print(content, end='')
            except json.JSONDecodeError:
                continue

    stream_with_proper_sse()
    ```
  </Tab>

  <Tab title="JavaScript with EventSource">
    ```javascript  theme={null}
    // For browser environments
    function streamInBrowser() {
      const eventSource = new EventSource('/api/stream'); // Your server endpoint
      
      eventSource.onmessage = function(event) {
        if (event.data === '[DONE]') {
          eventSource.close();
          return;
        }
        
        try {
          const chunk = JSON.parse(event.data);
          const content = chunk.choices[0]?.delta?.content;
          if (content) {
            document.getElementById('output').innerHTML += content;
          }
        } catch (e) {
          console.error('Error parsing chunk:', e);
        }
      };
      
      eventSource.onerror = function(event) {
        console.error('EventSource failed:', event);
        eventSource.close();
      };
    }
    ```
  </Tab>

  <Tab title="Manual SSE Parsing">
    ```python  theme={null}
    import requests
    import json

    def stream_with_manual_parsing():
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar",
            "messages": [{"role": "user", "content": "Explain quantum computing"}],
            "stream": True
        }
        
        response = requests.post(url, headers=headers, json=payload, stream=True)
        
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    data_str = line[6:]  # Remove 'data: ' prefix
                    if data_str == '[DONE]':
                        break
                    try:
                        chunk_data = json.loads(data_str)
                        content = chunk_data['choices'][0]['delta'].get('content', '')
                        if content:
                            print(content, end='')
                    except json.JSONDecodeError:
                        continue

    stream_with_manual_parsing()
    ```
  </Tab>
</Tabs>

## Advanced Streaming Patterns

### Buffered Streaming

For applications that need to process chunks in batches:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
    from perplexity import Perplexity
    import time

    def buffered_streaming(buffer_size=50, flush_interval=1.0):
        client = Perplexity()
        
        stream = client.chat.completions.create(
            model="sonar",
            messages=[{"role": "user", "content": "Write a detailed explanation of machine learning"}],
            stream=True
        )
        
        buffer = ""
        last_flush = time.time()
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                buffer += chunk.choices[0].delta.content
                
                # Flush buffer if it's full or enough time has passed
                if len(buffer) >= buffer_size or (time.time() - last_flush) >= flush_interval:
                    print(buffer, end='', flush=True)
                    buffer = ""
                    last_flush = time.time()
        
        # Flush remaining buffer
        if buffer:
            print(buffer, end='', flush=True)

    buffered_streaming()
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    async function bufferedStreaming(bufferSize: number = 50, flushInterval: number = 1000) {
      const client = new Perplexity();
      
      const stream = await client.chat.completions.create({
        model: "sonar",
        messages: [{ role: "user", content: "Write a detailed explanation of machine learning" }],
        stream: true
      });
      
      let buffer = "";
      let lastFlush = Date.now();
      
      for await (const chunk of stream) {
        if (chunk.choices[0]?.delta?.content) {
          buffer += chunk.choices[0].delta.content;
          
          // Flush buffer if it's full or enough time has passed
          if (buffer.length >= bufferSize || (Date.now() - lastFlush) >= flushInterval) {
            process.stdout.write(buffer);
            buffer = "";
            lastFlush = Date.now();
          }
        }
      }
      
      // Flush remaining buffer
      if (buffer) {
        process.stdout.write(buffer);
      }
    }

    bufferedStreaming();
    ```
  </Tab>
</Tabs>

### Stream Processing with Callbacks

For applications that need to process chunks with custom logic:

<Tabs>
  <Tab title="Python SDK">
    ```python  theme={null}
    from perplexity import Perplexity
    from typing import Callable, Optional

    def stream_with_callbacks(
        query: str,
        on_content: Optional[Callable[[str], None]] = None,
        on_search_results: Optional[Callable[[list], None]] = None,
        on_complete: Optional[Callable[[str, dict], None]] = None
    ):
        client = Perplexity()
        
        stream = client.chat.completions.create(
            model="sonar",
            messages=[{"role": "user", "content": query}],
            stream=True
        )
        
        full_content = ""
        metadata = {}
        
        for chunk in stream:
            # Handle content chunks
            if chunk.choices[0].delta.content:
                content_piece = chunk.choices[0].delta.content
                full_content += content_piece
                if on_content:
                    on_content(content_piece)
            
            # Handle search results
            if hasattr(chunk, 'search_results') and chunk.search_results:
                metadata['search_results'] = chunk.search_results
                if on_search_results:
                    on_search_results(chunk.search_results)
            
            # Handle other metadata
            if hasattr(chunk, 'usage') and chunk.usage:
                metadata['usage'] = chunk.usage
            
            # Handle completion
            if chunk.choices[0].finish_reason:
                if on_complete:
                    on_complete(full_content, metadata)
        
        return full_content, metadata

    # Usage example
    def print_content(content: str):
        print(content, end='', flush=True)

    def handle_search_results(results: list):
        print(f"\n[Found {len(results)} sources]", end='')

    def handle_completion(content: str, metadata: dict):
        print(f"\n\nCompleted. Total length: {len(content)} characters")
        if 'usage' in metadata:
            print(f"Token usage: {metadata['usage']}")

    stream_with_callbacks(
        "Explain the latest developments in renewable energy",
        on_content=print_content,
        on_search_results=handle_search_results,
        on_complete=handle_completion
    )
    ```
  </Tab>

  <Tab title="TypeScript SDK">
    ```typescript  theme={null}
    interface StreamCallbacks {
      onContent?: (content: string) => void;
      onSearchResults?: (results: any[]) => void;
      onComplete?: (content: string, metadata: any) => void;
    }

    async function streamWithCallbacks(query: string, callbacks: StreamCallbacks = {}) {
      const client = new Perplexity();
      
      const stream = await client.chat.completions.create({
        model: "sonar",
        messages: [{ role: "user", content: query }],
        stream: true
      });
      
      let fullContent = "";
      const metadata: any = {};
      
      for await (const chunk of stream) {
        // Handle content chunks
        if (chunk.choices[0]?.delta?.content) {
          const contentPiece = chunk.choices[0].delta.content;
          fullContent += contentPiece;
          callbacks.onContent?.(contentPiece);
        }
        
        // Handle search results
        if (chunk.search_results) {
          metadata.search_results = chunk.search_results;
          callbacks.onSearchResults?.(chunk.search_results);
        }
        
        // Handle other metadata
        if (chunk.usage) {
          metadata.usage = chunk.usage;
        }
        
        // Handle completion
        if (chunk.choices[0]?.finish_reason) {
          callbacks.onComplete?.(fullContent, metadata);
        }
      }
      
      return { content: fullContent, metadata };
    }

    // Usage example
    const result = await streamWithCallbacks(
      "Explain the latest developments in renewable energy",
      {
        onContent: (content) => process.stdout.write(content),
        onSearchResults: (results) => process.stdout.write(`\n[Found ${results.length} sources]`),
        onComplete: (content, metadata) => {
          console.log(`\n\nCompleted. Total length: ${content.length} characters`);
          if (metadata.usage) {
            console.log(`Token usage:`, metadata.usage);
          }
        }
      }
    );
    ```
  </Tab>
</Tabs>

## Best Practices

<Steps>
  <Step title="Handle network interruptions">
    Implement reconnection logic for robust streaming applications.

    <Tabs>
      <Tab title="Python SDK">
        ```python  theme={null}
        import time
        import random
        from perplexity import Perplexity
        import perplexity

        def robust_streaming(query: str, max_retries: int = 3):
            client = Perplexity()
            
            for attempt in range(max_retries):
                try:
                    stream = client.chat.completions.create(
                        model="sonar",
                        messages=[{"role": "user", "content": query}],
                        stream=True
                    )
                    
                    for chunk in stream:
                        if chunk.choices[0].delta.content:
                            print(chunk.choices[0].delta.content, end='', flush=True)
                    
                    return  # Success, exit retry loop
                    
                except (perplexity.APIConnectionError, perplexity.APITimeoutError) as e:
                    if attempt < max_retries - 1:
                        delay = (2 ** attempt) + random.uniform(0, 1)
                        print(f"\nConnection error, retrying in {delay:.1f}s...")
                        time.sleep(delay)
                    else:
                        print(f"\nFailed after {max_retries} attempts: {e}")
                        raise

        robust_streaming("Explain quantum computing")
        ```
      </Tab>

      <Tab title="TypeScript SDK">
        ```typescript  theme={null}
        async function robustStreaming(query: string, maxRetries: number = 3) {
          const client = new Perplexity();
          
          for (let attempt = 0; attempt < maxRetries; attempt++) {
            try {
              const stream = await client.chat.completions.create({
                model: "sonar",
                messages: [{ role: "user", content: query }],
                stream: true
              });
              
              for await (const chunk of stream) {
                if (chunk.choices[0]?.delta?.content) {
                  process.stdout.write(chunk.choices[0].delta.content);
                }
              }
              
              return; // Success, exit retry loop
              
            } catch (error) {
              if (error instanceof Perplexity.APIConnectionError && attempt < maxRetries - 1) {
                const delay = Math.pow(2, attempt) * 1000 + Math.random() * 1000;
                console.log(`\nConnection error, retrying in ${delay / 1000:.1f}s...`);
                await new Promise(resolve => setTimeout(resolve, delay));
              } else {
                console.error(`\nFailed after ${maxRetries} attempts:`, error);
                throw error;
              }
            }
          }
        }

        robustStreaming("Explain quantum computing");
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Implement proper buffering">
    Use appropriate buffering strategies for your application's needs.

    ```python  theme={null}
    # For real-time chat applications
    buffer_size = 1  # Character-by-character for immediate display

    # For document processing
    buffer_size = 100  # Larger chunks for efficiency

    # For API responses
    buffer_size = 500  # Balance between responsiveness and efficiency
    ```
  </Step>

  <Step title="Handle metadata appropriately">
    Remember that search results and metadata arrive at the end of the stream.

    ```python  theme={null}
    # Don't expect search results until the stream is complete
    if chunk.choices[0].finish_reason == "stop":
        # Now search results and usage info are available
        process_search_results(chunk.search_results)
        log_usage_stats(chunk.usage)
    ```
  </Step>

  <Step title="Optimize for your use case">
    Choose streaming parameters based on your application requirements.

    <Tabs>
      <Tab title="Real-time Chat">
        ```python  theme={null}
        # Optimize for immediate response
        stream = client.chat.completions.create(
            model="sonar",
            messages=messages,
            stream=True,
            max_tokens=1000  # Reasonable limit
        )
        ```
      </Tab>

      <Tab title="Document Generation">
        ```python  theme={null}
        # Optimize for quality and completeness
        stream = client.chat.completions.create(
            model="sonar-pro",
            messages=messages,
            stream=True,
            max_tokens=4000  # Longer responses
        )
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

<Warning>
  **Important**: If you need search results immediately for your user interface, consider using non-streaming requests for use cases where search result display is critical to the real-time user experience.
</Warning>

## Resources

* [The Perplexity SDK Guide](/docs/sdk/overview) - The Perplexity SDK guide
* [Chat Completions Guide](/docs/grounded-llm/chat-completions/quickstart) - Complete chat completions guide
* [API Reference - Chat Completions](/api-reference/chat-completions-post) - Complete API documentation