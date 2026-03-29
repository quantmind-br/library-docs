---
title: Mistral Docs
url: https://docs.mistral.ai/capabilities/document_ai
source: crawler
fetched_at: 2026-01-29T07:33:09.022483699-03:00
rendered_js: false
word_count: 126
summary: This document introduces Mistral Document AI, an enterprise-level service for document processing that combines OCR technology with structured data extraction and multilingual support. It outlines key capabilities like document annotations and QnA, providing the primary API and SDK entry points for integration.
tags:
    - document-ai
    - ocr
    - structured-data
    - mistral-api
    - document-processing
    - annotations
    - document-qna
category: concept
---

## Document AI

Mistral Document AI offers enterprise-level document processing, combining cutting-edge OCR technology with advanced structured data extraction. Experience faster processing speeds, unparalleled accuracy, and cost-effective solutions, all scalable to meet your needs.

![document_ai_graph](https://docs.mistral.ai/img/document_ai_overview.png)![document_ai_graph](https://docs.mistral.ai/img/document_ai_overview_dark.png)

Unlock the full potential of your documents with our multilingual support, annotations and adaptable workflows for all document types, enabling you to extract, comprehend, and analyze information with ease.

Using `client.ocr.process` in our SDK Clients as the entry point and/or the `https://api.mistral.ai/v1/ocr` endpoint, you can access the following services from our Document AI stack:

- [OCR Processor](https://docs.mistral.ai/capabilities/document_ai/basic_ocr): Discover our OCR model and its extensive capabilities.
- [Annotations](https://docs.mistral.ai/capabilities/document_ai/annotations): Annotate and extract data from your documents using our built-in Structured Outputs.
- [Document QnA](https://docs.mistral.ai/capabilities/document_ai/document_qna): Harness the power of our vast models in conjunction with our OCR technology.