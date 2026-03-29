---
title: Returning Images
url: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/media/returning-images.md
source: llms
fetched_at: 2026-02-04T07:23:29.80592105-03:00
rendered_js: false
word_count: 468
summary: This document explains how to enable and filter image results in Perplexity's Chat Completions API using the Sonar models. It covers parameters for including or excluding specific domains and restricting image formats like GIF or PNG.
tags:
    - sonar-models
    - chat-completions-api
    - image-results
    - domain-filtering
    - format-filtering
    - api-integration
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Returning Images

> Control image results with domain and format filters using Sonar models

## Overview

Grounded LLMs can return images as part of their responses to enhance the information provided. You can control which images are returned using domain and format filters, giving you fine-grained control over the sources and file types of image results. The `image_domain_filter` and `image_format_filter` parameters allow you to control the sources and file types of image results returned by Grounded LLMs. You can include a maximum of 10 entries in each of the filter lists, and these filters apply only when `"return_images": true` is set in your request.

<Info>
  The `return_images` feature is currently only available in the Chat Completions API.
</Info>

## Filter Types

### Domain Filtering

The `image_domain_filter` parameter controls which image sources are included or excluded:

* **Exclude domains**: Prefix with `-` (e.g., `-gettyimages.com`)
* **Include domains**: Use domain name directly (e.g., `wikimedia.org`)

### Format Filtering

The `image_format_filter` parameter restricts results to specific file formats:

* Use lowercase file extensions: `gif`, `jpg`, `png`, `webp`
* Omit the dot prefix: use `gif`, not `.gif`

## Basic Usage

To enable image returns, your request must include `"return_images": true`.

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "return_images": true,
      "messages": [
        {"role": "user", "content": "Show me images of Mount Everest"}
      ]
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Request with image returns enabled
  completion = client.chat.completions.create(
      model="sonar",
      return_images=True,
      messages=[
          {"role": "user", "content": "Show me images of Mount Everest"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Request with image returns enabled
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      messages: [
          { role: 'user', content: 'Show me images of Mount Everest' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Initialize the client
  const client = new Perplexity();

  // Request with image returns enabled
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      messages: [
          { role: 'user', content: 'Show me images of Mount Everest' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

## Filtering Examples

### 1. Exclude Specific Image Domains

Filter out images from specific providers like Getty Images:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "return_images": true,
      "image_domain_filter": ["-gettyimages.com"],
      "messages": [
        {"role": "user", "content": "What is the weather like today in London?"}
      ]
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Exclude Getty Images from results
  completion = client.chat.completions.create(
      model="sonar",
      return_images=True,
      image_domain_filter=["-gettyimages.com"],
      messages=[
          {"role": "user", "content": "Show me images of Mount Everest"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Exclude Getty Images from results
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_domain_filter: ['-gettyimages.com'],
      messages: [
          { role: 'user', content: 'Show me images of Mount Everest' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Initialize the client
  const client = new Perplexity();

  // Exclude Getty Images from results
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_domain_filter: ['-gettyimages.com'],
      messages: [
          { role: 'user', content: 'Show me images of Mount Everest' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

### 2. Only Return GIFs

Restrict results to GIF images only:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "return_images": true,
      "image_format_filter": ["gif"],
      "messages": [
        {"role": "user", "content": "Show me a funny cat gif"}
      ]
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Only return GIF images
  completion = client.chat.completions.create(
      model="sonar",
      return_images=True,
      image_format_filter=["gif"],
      messages=[
          {"role": "user", "content": "Show me a funny cat gif"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Only return GIF images
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_format_filter: ['gif'],
      messages: [
          { role: 'user', content: 'Show me a funny cat gif' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Initialize the client
  const client = new Perplexity();

  // Only return GIF images
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_format_filter: ['gif'],
      messages: [
          { role: 'user', content: 'Show me a funny cat gif' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

### 3. Combine Domain and Format Filters

Use both filters together for precise control:

<CodeGroup>
  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/chat/completions \
    --header "Authorization: Bearer $SONAR_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar",
      "return_images": true,
      "image_domain_filter": ["-gettyimages.com"],
      "image_format_filter": ["gif"],
      "messages": [
        {"role": "user", "content": "Show me a gif of a dog"}
      ]
    }' | jq
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Combine domain and format filtering
  completion = client.chat.completions.create(
      model="sonar",
      return_images=True,
      image_domain_filter=["-gettyimages.com"],
      image_format_filter=["gif"],
      messages=[
          {"role": "user", "content": "Show me a gif of a dog"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Combine domain and format filtering
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_domain_filter: ['-gettyimages.com'],
      image_format_filter: ['gif'],
      messages: [
          { role: 'user', content: 'Show me a gif of a dog' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Initialize the client
  const client = new Perplexity();

  // Combine domain and format filtering
  const completion = await client.chat.completions.create({
      model: 'sonar',
      return_images: true,
      image_domain_filter: ['-gettyimages.com'],
      image_format_filter: ['gif'],
      messages: [
          { role: 'user', content: 'Show me a gif of a dog' }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

## Advanced Filtering

### Multiple Domain Exclusions

```python  theme={null}
# Exclude multiple image providers
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_domain_filter=["-gettyimages.com", "-shutterstock.com", "-stockphoto.com"],
    messages=[
        {"role": "user", "content": "Show me nature photography"}
    ]
)
```

### Multiple Format Types

```python  theme={null}
# Allow multiple image formats
completion = client.chat.completions.create(
    model="sonar",
    return_images=True,
    image_format_filter=["jpg", "png", "webp"],
    messages=[
        {"role": "user", "content": "Show me high-quality landscape images"}
    ]
)
```

### Include Specific Domains

```python  theme={null}
# Include only Wikipedia images
completion = client.chat.completions.create(
    model="sonar", 
    return_images=True,
    image_domain_filter=["wikimedia.org"],
    messages=[
        {"role": "user", "content": "Show me historical images"}
    ]
)
```

## Common Use Cases

### Educational Content

```python  theme={null}
# Get educational images from trusted sources
image_domain_filter = ["wikimedia.org", "nasa.gov", "archive.org"]
image_format_filter = ["jpg", "png"]
```

### Creative Projects

```python  theme={null}
# Get animated content for presentations
image_format_filter = ["gif", "webp"]
image_domain_filter = ["-gettyimages.com", "-shutterstock.com"]  # Avoid watermarked images
```

### High-Quality Photography

```python  theme={null}
# Focus on professional photography formats
image_format_filter = ["jpg", "png"]
image_domain_filter = ["-lowres.com", "-thumbnail.com"]  # Exclude low-quality sources
```

## Best Practices

<AccordionGroup>
  <Accordion title="Domain Filtering Strategy">
    * Use simple domain names like `example.com` or `-gettyimages.com`
    * Do not include `http://`, `https://`, or subdomains
    * Mix inclusion and exclusion in domain filters for precise control
    * Keep lists short (≤10 entries) for performance and relevance
  </Accordion>

  <Accordion title="Format Filtering Guidelines">
    * File extensions must be lowercase: `["jpg"]`, not `["JPG"]`
    * Omit dot prefix: use `gif`, not `.gif`
    * Consider your use case: GIFs for animation, PNG for transparency, JPG for photos
    * WebP offers good compression but may have limited compatibility
  </Accordion>

  <Accordion title="Performance Optimization">
    * Filters may slightly increase response time
    * Overly restrictive filters may reduce result quality or quantity
    * Test different filter combinations to find the right balance
    * Monitor response times with different filter configurations
  </Accordion>
</AccordionGroup>

## Filter Reference

### Supported Image Formats

| Format | Extension | Best For                              |
| ------ | --------- | ------------------------------------- |
| JPEG   | `jpg`     | Photographs, complex images           |
| PNG    | `png`     | Screenshots, images with transparency |
| WebP   | `webp`    | Modern format with good compression   |
| GIF    | `gif`     | Animated images, simple graphics      |

### Common Domain Exclusions

| Domain              | Type         | Reason                    |
| ------------------- | ------------ | ------------------------- |
| `-gettyimages.com`  | Stock Photos | Watermarked content       |
| `-shutterstock.com` | Stock Photos | Watermarked content       |
| `-istockphoto.com`  | Stock Photos | Watermarked content       |
| `-pinterest.com`    | Social Media | Mixed quality/attribution |

<Tip>
  Start with broad filters and gradually refine them based on the quality and relevance of returned images.
</Tip>

## Limitations

<Warning>
  * Maximum of 30 images can be returned per response
  * Maximum of 10 entries in each filter list
  * Filters only apply when `"return_images": true` is set
  * Some domains may not be filterable due to CDN usage
  * Very restrictive filters may result in no images being returned
</Warning>