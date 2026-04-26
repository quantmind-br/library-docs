---
title: Document QnA | Mistral Docs
url: https://docs.mistral.ai/studio-api/document-processing/document_qna
source: sitemap
fetched_at: 2026-04-26T04:12:48.583601747-03:00
rendered_js: false
word_count: 232
summary: Document QnA capability combining OCR and large language models for natural language interaction with document content and information extraction.
tags:
    - document-qna
    - ocr
    - natural-language-processing
    - information-extraction
    - document-analysis
    - ai-workflows
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Document QnA

Combines OCR with LLM capabilities to enable natural language interaction with document content.

![Document QnA](https://docs.mistral.ai/img/document_qna.png)

## Workflow

1. **OCR Processing** — Extracts text, structure, and formatting from document
2. **Language Model** — Analyzes document content and answers questions in natural language

## Capabilities

- Question answering about specific document content
- Information extraction and summarization
- Document analysis and insights
- Multi-document queries and comparisons
- Context-aware responses considering full document

## Use Cases

- Analyzing research papers and technical documents
- Extracting information from business documents
- Processing legal documents and contracts
- Building document Q&A applications
- Automating document-based workflows

## Usage

```python
from mistralai.client import MistralClient

client = MistralClient(api_key="your-api-key")

# PDF via URL (must be public)
response = client.chat(
    model="mistral-large-latest",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What is the main topic of this document?"},
            {"type": "document", "document": "https://example.com/report.pdf"}
        ]
    }]
)
```

## Example

```python
# Ask specific questions
response = client.chat(
    model="mistral-large-latest",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What are the key findings?"},
            {"type": "document", "document": "https://example.com/research.pdf"}
        ]
    }]
)
```

> [!tip] Cookbook with detailed examples available [here](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/ocr/document_understanding.ipynb).

#document-qna #ocr #natural-language-processing #information-extraction #document-analysis #ai-workflows
