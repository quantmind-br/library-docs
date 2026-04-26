---
title: Set up RAG with document search | Mistral Docs
url: https://docs.mistral.ai/getting-started/quickstarts/developer/rag-document-search
source: sitemap
fetched_at: 2026-04-26T04:07:13.617132726-03:00
rendered_js: false
word_count: 255
summary: This document explains how to utilize the Mistral Library feature to upload documents and perform grounded chat completions based on custom content.
tags:
    - mistral-api
    - rag
    - document-retrieval
    - file-indexing
    - chat-completion
    - library-management
category: tutorial
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Upload documents to a Library and query them in a chat completion.

- Create a Library and upload a file
- The model retrieves relevant passages from your documents
- Answers are grounded in your content instead of general knowledge

**Time to complete:** ~10 minutes

**Prerequisites:**
- A Mistral API key
- Python 3.9+ or Node.js 18+
- The Mistral SDK installed
- A document to upload (PDF, TXT, or DOCX)

## Create a Library

A Library is a container for documents that the model can search during conversations. We process and index the document for retrieval. Check the status before querying.

Small files (under 10 pages) typically process in under 30 seconds. Larger documents may take a few minutes.

## Query the Document

Ask a question and include the file reference so the model retrieves relevant passages before answering.

The response should reference information from your uploaded document instead of general knowledge. For example, if you uploaded a company handbook and asked about remote work policy, you should see specific details like:

> "According to the handbook, employees may work remotely up to 3 days per week with manager approval..."

## Verification

Look for:
- Specific details, names, or policies from your document
- Answers grounded in the uploaded content rather than generic advice
- Reduced hallucination compared to the same question without documents

> [!warning]
> If the response seems generic, confirm the file status is `processed` and that the `documents` parameter is included in your request.

#rag #document-retrieval #file-indexing
