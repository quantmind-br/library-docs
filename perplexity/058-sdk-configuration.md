---
title: Configuration
url: https://docs.perplexity.ai/docs/sdk/configuration.md
source: llms
fetched_at: 2026-02-04T07:24:57.023017743-03:00
rendered_js: false
word_count: 317
summary: This document explains how to configure Perplexity SDKs for both Python and TypeScript, covering request retries, timeout management, proxy settings, and advanced HTTP client customization.
tags:
    - perplexity-sdk
    - retry-logic
    - timeout-management
    - proxy-configuration
    - http-client
    - python
    - typescript
    - ssl-tls
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration

> Learn how to configure the Perplexity SDKs for retries, timeouts, proxies, and advanced HTTP client customization.

## Overview

The Perplexity SDKs provide extensive configuration options to customize client behavior for different environments and use cases. This guide covers retry configuration, timeout settings, and custom HTTP client setup.

## Retries and Timeouts

### Basic Retry Configuration

Configure how the SDK handles failed requests:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  import httpx

  client = Perplexity(
      max_retries=3,  # Default is 2
      timeout=httpx.Timeout(30.0, read=10.0, write=5.0, connect=2.0)
  )

  # Per-request configuration
  search = client.with_options(max_retries=5).search.create(
      query="example"
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity({
      maxRetries: 3, // Default is 2
      timeout: 30000, // 30 seconds in milliseconds
  });

  // Per-request configuration
  const search = await client.withOptions({ maxRetries: 5 }).search.create({
      query: "example"
  });
  ```
</CodeGroup>

### Advanced Timeout Configuration

Set granular timeout controls for different phases of the request:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity

  # Detailed timeout configuration
  timeout_config = httpx.Timeout(
      connect=5.0,    # Time to establish connection
      read=30.0,      # Time to read response
      write=10.0,     # Time to send request
      pool=10.0       # Time to get connection from pool
  )

  client = Perplexity(timeout=timeout_config)

  # For long-running operations
  long_timeout = httpx.Timeout(
      connect=5.0,
      read=120.0,  # 2 minutes for complex queries
      write=10.0,
      pool=10.0
  )

  client_long = Perplexity(timeout=long_timeout)
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Basic timeout (applies to entire request)
  const client = new Perplexity({
      timeout: 30000  // 30 seconds
  });

  // For long-running operations
  const clientLong = new Perplexity({
      timeout: 120000  // 2 minutes for complex queries
  });

  // Per-request timeout override
  const result = await client.withOptions({ 
      timeout: 60000  // 1 minute for this specific request
  }).chat.completions.create({
      model: "llama-3.1-sonar-large-128k-online",
      messages: [{ role: "user", content: "Complex research query..." }]
  });
  ```
</CodeGroup>

## Custom HTTP Client

### Proxy Configuration

Configure the SDK to work with corporate proxies:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # HTTP Proxy
  client = Perplexity(
      http_client=DefaultHttpxClient(
          proxy="http://proxy.company.com:8080"
      )
  )

  # HTTPS Proxy with authentication
  client_auth = Perplexity(
      http_client=DefaultHttpxClient(
          proxy="http://username:password@proxy.company.com:8080"
      )
  )

  # SOCKS proxy
  client_socks = Perplexity(
      http_client=DefaultHttpxClient(
          proxy="socks5://proxy.company.com:1080"
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import { HttpsProxyAgent } from 'https-proxy-agent';
  import { SocksProxyAgent } from 'socks-proxy-agent';

  // HTTP/HTTPS Proxy
  const client = new Perplexity({
      httpAgent: new HttpsProxyAgent('http://proxy.company.com:8080')
  });

  // Proxy with authentication
  const clientAuth = new Perplexity({
      httpAgent: new HttpsProxyAgent('http://username:password@proxy.company.com:8080')
  });

  // SOCKS proxy
  const clientSocks = new Perplexity({
      httpAgent: new SocksProxyAgent('socks5://proxy.company.com:1080')
  });
  ```
</CodeGroup>

### Custom Headers and User Agent

Add custom headers to all requests:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # Custom headers
  headers = {
      "User-Agent": "MyApp/1.0",
      "X-Custom-Header": "custom-value"
  }

  client = Perplexity(
      http_client=DefaultHttpxClient(
          headers=headers
      )
  )

  # Advanced HTTP client configuration
  transport = httpx.HTTPTransport(
      local_address="0.0.0.0",  # Bind to specific interface
      verify=True,              # SSL verification
      cert=None,                # Client certificate
      http2=True               # Enable HTTP/2
  )

  client_advanced = Perplexity(
      http_client=DefaultHttpxClient(
          transport=transport,
          headers=headers
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Custom headers
  const client = new Perplexity({
      defaultHeaders: {
          "User-Agent": "MyApp/1.0",
          "X-Custom-Header": "custom-value"
      }
  });

  // Advanced fetch configuration
  const clientAdvanced = new Perplexity({
      fetch: (url, options) => {
          return fetch(url, {
              ...options,
              headers: {
                  ...options?.headers,
                  "User-Agent": "MyApp/1.0",
                  "X-Custom-Header": "custom-value"
              }
          });
      }
  });
  ```
</CodeGroup>

### SSL/TLS Configuration

Configure SSL verification and certificates:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  import ssl
  from perplexity import Perplexity, DefaultHttpxClient

  # Disable SSL verification (not recommended for production)
  client_no_ssl = Perplexity(
      http_client=DefaultHttpxClient(
          verify=False
      )
  )

  # Custom SSL context
  ssl_context = ssl.create_default_context()
  ssl_context.check_hostname = False
  ssl_context.verify_mode = ssl.CERT_NONE

  client_custom_ssl = Perplexity(
      http_client=DefaultHttpxClient(
          verify=ssl_context
      )
  )

  # Client certificate authentication
  client_cert = Perplexity(
      http_client=DefaultHttpxClient(
          cert=("client.crt", "client.key")
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  // Custom HTTPS agent with SSL options
  const httpsAgent = new https.Agent({
      rejectUnauthorized: false, // Disable SSL verification (not recommended)
      keepAlive: true,
      maxSockets: 50
  });

  const client = new Perplexity({
      httpAgent: httpsAgent
  });

  // For Node.js environments with custom CA certificates
  const httpsAgentCA = new https.Agent({
      ca: [/* your CA certificates */],
      cert: /* client certificate */,
      key: /* client private key */
  });

  const clientCert = new Perplexity({
      httpAgent: httpsAgentCA
  });
  ```
</CodeGroup>

## Connection Pooling

Optimize performance with connection pooling:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # Configure connection limits
  limits = httpx.Limits(
      max_keepalive_connections=20,  # Keep-alive connections
      max_connections=100,           # Total connections
      keepalive_expiry=30.0         # Keep-alive timeout
  )

  client = Perplexity(
      http_client=DefaultHttpxClient(
          limits=limits
      )
  )

  # For high-throughput applications
  high_throughput_limits = httpx.Limits(
      max_keepalive_connections=100,
      max_connections=500,
      keepalive_expiry=60.0
  )

  client_high_throughput = Perplexity(
      http_client=DefaultHttpxClient(
          limits=high_throughput_limits
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  // Configure agent pool settings
  const httpsAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 30000,  // 30 seconds
      maxSockets: 50,         // Max connections per host
      maxFreeSockets: 10,     // Max idle connections per host
      timeout: 60000          // Socket timeout
  });

  const client = new Perplexity({
      httpAgent: httpsAgent
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

## Environment-Specific Configuration

### Development Configuration

Settings optimized for development and debugging:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # Development configuration
  dev_client = Perplexity(
      max_retries=1,           # Fail fast in development
      timeout=httpx.Timeout(10.0),  # Short timeout
      http_client=DefaultHttpxClient(
          # Enable detailed logging
          event_hooks={
              'request': [lambda request: print(f"Request: {request.method} {request.url}")],
              'response': [lambda response: print(f"Response: {response.status_code}")]
          }
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Development configuration
  const devClient = new Perplexity({
      maxRetries: 1,     // Fail fast in development
      timeout: 10000,    // 10 second timeout
      
      // Custom fetch with logging
      fetch: (url, options) => {
          console.log(`Request: ${options?.method || 'GET'} ${url}`);
          return fetch(url, options).then(response => {
              console.log(`Response: ${response.status}`);
              return response;
          });
      }
  });
  ```
</CodeGroup>

### Production Configuration

Settings optimized for production environments:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  # Production configuration
  prod_limits = httpx.Limits(
      max_keepalive_connections=50,
      max_connections=200,
      keepalive_expiry=60.0
  )

  prod_timeout = httpx.Timeout(
      connect=5.0,
      read=60.0,
      write=10.0,
      pool=10.0
  )

  prod_client = Perplexity(
      max_retries=3,
      timeout=prod_timeout,
      http_client=DefaultHttpxClient(
          limits=prod_limits,
          verify=True,  # Always verify SSL in production
          http2=True    # Enable HTTP/2 for better performance
      )
  )
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  // Production configuration
  const prodAgent = new https.Agent({
      keepAlive: true,
      keepAliveMsecs: 60000,
      maxSockets: 100,
      maxFreeSockets: 20,
      timeout: 60000
  });

  const prodClient = new Perplexity({
      maxRetries: 3,
      timeout: 60000,
      httpAgent: prodAgent
  });
  ```
</CodeGroup>

## Configuration Patterns

### Environment-Based Configuration

Use environment variables to configure the client:

<CodeGroup>
  ```python Python theme={null}
  import os
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  def create_client():
      # Base configuration
      timeout = httpx.Timeout(
          connect=float(os.getenv('PERPLEXITY_CONNECT_TIMEOUT', '5.0')),
          read=float(os.getenv('PERPLEXITY_READ_TIMEOUT', '30.0')),
          write=float(os.getenv('PERPLEXITY_WRITE_TIMEOUT', '10.0'))
      )
      
      max_retries = int(os.getenv('PERPLEXITY_MAX_RETRIES', '3'))
      
      # Optional proxy configuration
      proxy = os.getenv('PERPLEXITY_PROXY')
      http_client_kwargs = {}
      if proxy:
          http_client_kwargs['proxy'] = proxy
      
      return Perplexity(
          max_retries=max_retries,
          timeout=timeout,
          http_client=DefaultHttpxClient(**http_client_kwargs)
      )

  client = create_client()
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import { HttpsProxyAgent } from 'https-proxy-agent';

  function createClient(): Perplexity {
      const maxRetries = parseInt(process.env.PERPLEXITY_MAX_RETRIES || '3');
      const timeout = parseInt(process.env.PERPLEXITY_TIMEOUT || '30000');
      
      const config: any = {
          maxRetries,
          timeout
      };
      
      // Optional proxy configuration
      if (process.env.PERPLEXITY_PROXY) {
          config.httpAgent = new HttpsProxyAgent(process.env.PERPLEXITY_PROXY);
      }
      
      return new Perplexity(config);
  }

  const client = createClient();
  ```
</CodeGroup>

### Configuration Factory

Create reusable configuration patterns:

<CodeGroup>
  ```python Python theme={null}
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  class PerplexityClientFactory:
      @staticmethod
      def development():
          return Perplexity(
              max_retries=1,
              timeout=httpx.Timeout(10.0)
          )
      
      @staticmethod
      def production():
          return Perplexity(
              max_retries=3,
              timeout=httpx.Timeout(connect=5.0, read=60.0, write=10.0),
              http_client=DefaultHttpxClient(
                  limits=httpx.Limits(
                      max_keepalive_connections=50,
                      max_connections=200
                  )
              )
          )
      
      @staticmethod
      def high_throughput():
          return Perplexity(
              max_retries=2,
              timeout=httpx.Timeout(connect=2.0, read=30.0, write=5.0),
              http_client=DefaultHttpxClient(
                  limits=httpx.Limits(
                      max_keepalive_connections=100,
                      max_connections=500
                  )
              )
          )

  # Usage
  client = PerplexityClientFactory.production()
  ```

  ```typescript TypeScript/JavaScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  class PerplexityClientFactory {
      static development(): Perplexity {
          return new Perplexity({
              maxRetries: 1,
              timeout: 10000
          });
      }
      
      static production(): Perplexity {
          const agent = new https.Agent({
              keepAlive: true,
              maxSockets: 100,
              timeout: 60000
          });
          
          return new Perplexity({
              maxRetries: 3,
              timeout: 60000,
              httpAgent: agent
          });
      }
      
      static highThroughput(): Perplexity {
          const agent = new https.Agent({
              keepAlive: true,
              maxSockets: 500,
              maxFreeSockets: 100,
              timeout: 30000
          });
          
          return new Perplexity({
              maxRetries: 2,
              timeout: 30000,
              httpAgent: agent
          });
      }
  }

  // Usage
  const client = PerplexityClientFactory.production();
  ```
</CodeGroup>

## Related Resources

<CardGroup cols={2}>
  <Card title="Error Handling" icon="triangle-exclamation" href="/docs/sdk/error-handling">
    Handle timeouts and connection errors
  </Card>

  <Card title="Performance" icon="bolt" href="/docs/sdk/performance">
    Optimize async operations and connection pooling
  </Card>
</CardGroup>