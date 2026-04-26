---
title: OCR Processor | Mistral Docs
url: https://docs.mistral.ai/studio-api/document-processing/basic_ocr
source: sitemap
fetched_at: 2026-04-26T04:12:47.359669861-03:00
rendered_js: false
word_count: 530
summary: This document provides an overview of the Mistral Document AI OCR processor, detailing its capabilities for extracting text, tables, and structured data from various document formats.
tags:
    - ocr
    - document-ai
    - text-extraction
    - pdf-processing
    - machine-learning
    - api-documentation
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral Document AI OCR processor, powered by `mistral-ocr-latest`, extracts text and structured content from PDF documents.

![Basic OCR Graph](https://docs.mistral.ai/img/basic_ocr_graph.png)![Basic OCR Graph](https://docs.mistral.ai/img/basic_ocr_graph_dark.png)

## Key Features

- **Text extraction** with document structure and hierarchy preservation
- **Table formatting** via `table_format` parameter:
  - `null`: inline markdown
  - `markdown`: separate markdown tables
  - `html`: separate html tables
- **Header/footer extraction** via `extract_header` and `extract_footer` parameters
- **Markdown output** for easy parsing
- **Complex layout handling**: multi-column, mixed content, hyperlinks
- **Confidence scores** via `confidence_scores_granularity` parameter
- **Multiple formats**: `image_url` (png, jpeg, avif), `document_url` (pdf, pptx, docx)

> [!info]
> Table formatting and header/footer extraction require OCR 2512 or newer.

## OCR Methods

### PDF

| Method | Description |
|--------|-------------|
| Public URL | URL must be publicly accessible |
| Base64 encoded | Send encoded PDF directly |
| Cloud upload | Upload PDF to Mistral cloud |

### Image

URL or Base64 encoded image.

### Output

JSON containing extracted text, images bboxes, metadata. Images/tables replaced with placeholders:
- `![img-0.jpeg](img-0.jpeg)`
- `[tbl-3.html](tbl-3.html)`

Map to actual assets via `images` and `tables` fields.

## Confidence Scores

Use `confidence_scores_granularity` parameter for recognition quality assessment.

## At Scale

For large document processing, use [Batch Inference service](https://docs.mistral.ai/studio-api/batch-processing) for parallel, cost-effective processing.

Also supports [Annotations](https://docs.mistral.ai/studio-api/document-processing/annotations) for structured outputs.

See [API docs](https://docs.mistral.ai/api/endpoint/ocr) and related cookbooks. #ocr #document-ai #pdf-processing