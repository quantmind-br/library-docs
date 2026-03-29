---
title: Document QnA | Mistral Docs
url: https://docs.mistral.ai/capabilities/document_ai/document_qna
source: crawler
fetched_at: 2026-01-29T07:34:13.92190496-03:00
rendered_js: false
word_count: 232
summary: A guide on implementing and using document-based question and answering capabilities within the Mistral AI ecosystem.
tags:
    - Mistral AI
    - Document QnA
    - Natural Language Processing
    - AI Documentation
category: guide
---

The Document QnA capability combines OCR with large language model capabilities to enable natural language interaction with document content. This allows you to extract information and insights from documents by asking questions in natural language.

Before continuing, we recommend reading the [Chat Completions](https://docs.mistral.ai/capabilities/completion) documentation to learn more about the chat completions API and how to use it before proceeding.

### Workflow and Capabilities

The workflow consists of two main steps:

![Document QnA Graph](https://docs.mistral.ai/img/document_qna.png)

1. Document Processing: OCR extracts text, structure, and formatting, creating a machine-readable version of the document.
2. Language Model Understanding: The extracted document content is analyzed by a large language model. You can ask questions or request information in natural language. The model understands context and relationships within the document and can provide relevant answers based on the document content.

<!--THE END-->

- Question answering about specific document content
- Information extraction and summarization
- Document analysis and insights
- Multi-document queries and comparisons
- Context-aware responses that consider the full document

<!--THE END-->

- Analyzing research papers and technical documents
- Extracting information from business documents
- Processing legal documents and contracts
- Building document Q&A applications
- Automating document-based workflows

### Leverage Document QnA

The examples below show how to interact with a PDF document using natural language.

Be sure the URL is **public** and accessible by our API.

For more information on how to make use of Document QnA, we have the following [Document QnA Cookbook](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/ocr/document_understanding.ipynb) with a simple example.