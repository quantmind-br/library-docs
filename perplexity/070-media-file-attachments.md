---
title: File Attachments with Sonar
url: https://docs.perplexity.ai/docs/grounded-llm/chat-completions/media/file-attachments.md
source: llms
fetched_at: 2026-02-04T07:23:26.700516888-03:00
rendered_js: false
word_count: 380
summary: This document explains how to upload and analyze various file formats using Sonar models via the Perplexity API, covering both URL-based and base64-encoded methods.
tags:
    - file-attachments
    - sonar-models
    - document-analysis
    - base64-encoding
    - api-integration
    - file-upload
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# File Attachments with Sonar

> Learn how to upload and analyze documents (PDF, DOC, DOCX, TXT, RTF) using Sonar models

## Overview

Sonar models support document analysis through file uploads. You can provide files either as URLs to publicly accessible documents or as base64 encoded bytes. Ask questions about document content, get summaries, extract information, and perform detailed analysis of uploaded files in multiple formats including PDF, DOC, DOCX, TXT, and RTF.

<Note>
  Document files can be provided as:

  * A public URL pointing to the file
  * Base64 encoded bytes (without any prefix)

  Supported formats: PDF, DOC, DOCX, TXT, RTF.
</Note>

<Warning>
  The maximum file size is 50MB. Files larger than this limit will not be processed.
</Warning>

## Supported Features

* **Document Summarization**: Get concise summaries of document content
* **Question Answering**: Ask specific questions about the document
* **Content Extraction**: Extract key information, data, and insights
* **Multi-language Support**: Analyze documents in various languages
* **Large Document Handling**: Process lengthy documents efficiently
* **Multiple Formats**: Support for PDF, DOC, DOCX, TXT, and RTF files

## Basic Usage

### Simple Document Analysis

#### Using a Public URL

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.perplexity.ai/chat/completions" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        {
          "content": [
            {
              "type": "text",
              "text": "Summarize this document"
            },
            {
              "type": "file_url",
              "file_url": {
                "url": "https://example.com/document.pdf"
              },
            }
          ],
          "role": "user"
        }
      ],
      "model": "sonar-pro"
    }'
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client (uses PERPLEXITY_API_KEY environment variable)
  client = Perplexity()

  # Analyze the document
  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Summarize this document"
                  },
                  {
                      "type": "file_url",
                      "file_url": {
                          "url": "https://example.com/document.pdf"
                      },
                  }
              ]
          }
      ]
  )

  # Print the response
  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client (uses PERPLEXITY_API_KEY environment variable)
  const client = new Perplexity();

  // Analyze the document
  const completion = await client.chat.completions.create({
      model: 'sonar-pro',
      messages: [
          {
              role: 'user',
              content: [
                  {
                      type: 'text',
                      text: 'Summarize this document'
                  },
                  {
                      type: 'file_url',
                      file_url: {
                          url: 'https://example.com/document.pdf'
                      },
                      file_name: 'document.pdf'
                  }
              ]
          }
      ]
  });

  // Print the response
  console.log(completion.choices[0].message.content);
  ```

  ```go Go theme={null}
  package main

  import (
      "bytes"
      "encoding/json"
      "fmt"
      "net/http"
  )

  func main() {
      url := "https://api.perplexity.ai/chat/completions"
      
      payload := map[string]interface{}{
          "messages": []map[string]interface{}{
              {
                  "content": []map[string]interface{}{
                      {
                          "type": "text",
                          "text": "Summarize this document",
                      },
                      {
                          "type": "file_url",
                          "file_url": map[string]string{
                              "url": "https://example.com/document.pdf",
                          },
                      },
                  },
                  "role": "user",
              },
          },
          "model": "sonar-pro",
      }
      
      jsonData, _ := json.Marshal(payload)
      req, _ := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
      req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
      req.Header.Set("Content-Type", "application/json")
      
      client := &http.Client{}
      resp, _ := client.Do(req)
  }
  ```
</CodeGroup>

#### Using Base64 Encoded Bytes

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.perplexity.ai/chat/completions" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        {
          "content": [
            {
              "type": "text",
              "text": "Summarize this document"
            },
            {
              "type": "file_url",
              "file_url": {
                "url": "JVBERi0xLjQKJeLjz9MKNCAwIG9iago..."
              },
              "file_name": "report.pdf"
            }
          ],
          "role": "user"
        }
      ],
      "model": "sonar-pro"
    }'
  ```

  ```python Python theme={null}
  from perplexity import Perplexity
  import base64

  # Initialize the client
  client = Perplexity()

  # Read and encode file
  with open("document.pdf", "rb") as file:
      file_data = file.read()
      encoded_file = base64.b64encode(file_data).decode('utf-8')

  # Analyze the document
  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Summarize this document"
                  },
                  {
                      "type": "file_url",
                      "file_url": {
                          "url": encoded_file  # Just the base64 string, no prefix
                      },
                  }
              ]
          }
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');
  const fs = require('fs');

  // Initialize the client
  const client = new Perplexity();

  // Read and encode file
  const fileData = fs.readFileSync('document.pdf');
  const encodedFile = fileData.toString('base64');

  // Analyze the document
  const completion = await client.chat.completions.create({
      model: 'sonar-pro',
      messages: [
          {
              role: 'user',
              content: [
                  {
                      type: 'text',
                      text: 'Summarize this document'
                  },
                  {
                      type: 'file_url',
                      file_url: {
                          url: encodedFile  // Just the base64 string, no prefix
                      },
                      file_name: 'document.pdf'
                  }
              ]
          }
      ]
  });

  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

### Advanced Analysis with Web Search

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.perplexity.ai/chat/completions" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "messages": [
        {
          "content": [
            {
              "type": "text",
              "text": "What are the key findings in this research paper? Provide additional context from recent studies."
            },
            {
              "type": "file_url",
              "file_url": {
                "url": "https://example.com/research-paper.pdf"
              },
              "file_name": "research-paper.pdf"
            }
          ],
          "role": "user"
        }
      ],
      "model": "sonar-pro"
    }'
  ```

  ```python Python theme={null}
  from perplexity import Perplexity

  # Initialize the client
  client = Perplexity()

  # Analyze the document with web search
  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "What are the key findings in this research paper? Provide additional context from recent studies."
                  },
                  {
                      "type": "file_url",
                      "file_url": {
                          "url": "https://example.com/research-paper.pdf"
                      },
                      "file_name": "research-paper.pdf"
                  }
              ]
          }
      ]
  )

  # Print the response
  print(completion.choices[0].message.content)
  ```

  ```javascript JavaScript theme={null}
  const Perplexity = require('@perplexity-ai/perplexity_ai');

  // Initialize the client
  const client = new Perplexity();

  // Analyze the document with web search
  const completion = await client.chat.completions.create({
      model: 'sonar-pro',
      messages: [
          {
              role: 'user',
              content: [
                  {
                      type: 'text',
                      text: 'What are the key findings in this research paper? Provide additional context from recent studies.'
                  },
                  {
                      type: 'file_url',
                      file_url: {
                          url: 'https://example.com/research-paper.pdf'
                      },
                      file_name: 'research-paper.pdf'
                  }
              ]
          }
      ]
  });

  // Print the response
  console.log(completion.choices[0].message.content);
  ```
</CodeGroup>

## File Requirements

<CardGroup cols={2}>
  <Card title="Format Support" icon="check">
    * PDF files (.pdf extension)
    * Word documents (.doc, .docx extensions)
    * Text files (.txt extension)
    * Rich Text Format (.rtf extension)
    * Text-based documents (not scanned images)
    * Base64 encoded file bytes
    * Password-protected files (if publicly accessible)
  </Card>

  <Card title="Size Limits" icon="scale-balanced">
    * Maximum file size: 50MB per file
    * Maximum files per request: 30 files
    * Recommended: Under 50MB for optimal performance
    * Maximum processing time: 60 seconds
    * Large files may take longer to analyze
  </Card>
</CardGroup>

## Common Use Cases

### Academic Research

```python  theme={null}
question = "What methodology was used in this study and what were the main conclusions?"
```

### Legal Documents

```python  theme={null}
question = "Extract the key terms and conditions from this contract"
```

### Financial Reports

```python  theme={null}
question = "What are the revenue trends and key financial metrics mentioned?"
```

### Technical Documentation

```python  theme={null}
question = "Explain the implementation details and provide a step-by-step guide"
```

## Best Practices

<AccordionGroup>
  <Accordion title="Optimize Your Questions">
    * Be specific about what information you need
    * Ask one focused question per request for best results
    * Use follow-up questions to dive deeper into specific sections
  </Accordion>

  <Accordion title="Prepare Your Documents">
    * Ensure documents are text-based, not scanned images
    * For URLs: Use publicly accessible URLs (Google Drive, Dropbox, etc.)
    * For URLs: Verify the URL returns the document directly, not a preview page
    * For base64: Encode the entire file content properly
    * For base64: Provide only the base64 string without any prefix (no `data:` URI scheme)
  </Accordion>

  <Accordion title="Handle Large Documents">
    * Break down complex questions into smaller parts
    * Consider processing large documents in sections
    * Use streaming for real-time responses on lengthy analyses
  </Accordion>
</AccordionGroup>

## Error Handling

### Common Issues

| Error                | Cause                                | Solution                                                  |
| -------------------- | ------------------------------------ | --------------------------------------------------------- |
| `Invalid URL`        | URL not accessible or invalid base64 | Verify URL returns file directly or check base64 encoding |
| `File too large`     | File exceeds 50MB limit              | Compress or split the document                            |
| `Processing timeout` | Document too complex                 | Simplify question or use smaller sections                 |
| `Invalid base64`     | Malformed base64 string              | Ensure proper base64 encoding without prefix              |

## Pricing

PDF analysis follows standard Sonar pricing based on:

* Input tokens (document content + question)
* Output tokens (AI response)
* Web search usage (if enabled)

<Tip>
  Large documents consume more input tokens. Consider the document size when estimating costs.
</Tip>