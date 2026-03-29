---
title: OCR Processor | Mistral Docs
url: https://docs.mistral.ai/capabilities/document_ai/basic_ocr
source: crawler
fetched_at: 2026-01-29T07:33:16.223416645-03:00
rendered_js: false
word_count: 486
summary: Documentation for Mistral AI's OCR processor, detailing how to extract text and information from documents and images using their API.
tags:
    - OCR
    - Mistral AI
    - text extraction
    - API
    - vision
category: guide
---

## Document AI - OCR Processor

Mistral Document AI API comes with a Document OCR (Optical Character Recognition) processor, powered by our latest OCR model `mistral-ocr-latest`, which enables you to extract text and structured content from PDF documents.

![Basic OCR Graph](https://docs.mistral.ai/img/basic_ocr_graph.png)![Basic OCR Graph](https://docs.mistral.ai/img/basic_ocr_graph_dark.png)

### Key Features

- **Extracts text** in content while maintaining document structure and hierarchy.
- Preserves formatting like headers, paragraphs, lists and tables.
  
  - **Table formatting** can be toggled between `null`, `markdown` and `html` via the `table_format` parameter.
    
    - `null`: Tables are returned inline as markdown within the extracted page.
    - `markdown`: Tables are returned as markdown tables separately.
    - `html`: Tables are returned as html tables separately.
- Option to **extract headers and footers** via the `extract_header` and the `extract_footer` parameter, when used, the headers and footers content will be provided in the `header` and `footer` fields. By default, headers and footers are considered as part of the main content output.
- Returns results in markdown format for easy parsing and rendering.
- Handles complex layouts including multi-column text and mixed content and returns hyperlinks when available.
- Processes documents at scale with high accuracy
- Supports multiple document formats including:
  
  - `image_url`: png, jpeg/jpg, avif and more...
  - `document_url`: pdf, pptx, docx and more...
  - For a non-exaustive more comprehensive list, visit our [FAQ](#faq).

Learn more about our API [here](https://docs.mistral.ai/api/endpoint/ocr).

Table formatting as well as header and footer extraction is only available for OCR 2512 or newer.

The OCR processor returns the extracted **text content**, **images bboxes** and metadata about the document structure, making it easy to work with the recognized content programmatically.

### OCR your Documents

We provide different methods to OCR your documents. You can either OCR a **PDF** or an **Image**.

Among the PDF methods, you can use a **public available URL**, a **base64 encoded PDF** or by **uploading a PDF in our Cloud**.

Be sure the URL is **public** and accessible by our API.

The output will be a JSON object containing the extracted text content, images bboxes, metadata and other information about the document structure.

When extracting images and tables they will be replaced with placeholders, such as:

- `![img-0.jpeg](img-0.jpeg)`
- `[tbl-3.html](tbl-3.html)`

You can map them to the actual images and tables by using the `images` and `tables` fields.

To perform OCR on an image, you can either pass a URL to the image or directly use a Base64 encoded image.

You can perform OCR with any public available image as long as a direct url is available.

The output will be a JSON object containing the extracted text content, images bboxes, metadata and other information about the document structure.

When extracting images and tables they will be replaced with placeholders, such as:

- `![img-0.jpeg](img-0.jpeg)`
- `[tbl-3.html](tbl-3.html)`

You can map them to the actual images and tables by using the `images` and `tables` fields.

When performing OCR at scale, we recommend using our [Batch Inference service](https://docs.mistral.ai/capabilities/batch), this allows you to process large amounts of documents in parallel while being more cost-effective than using the OCR API directly. We also support [Annotations](https://docs.mistral.ai/capabilities/document_ai/annotations) for structured outputs and other features.

For more information and guides on how to make use of OCR, we have the following cookbooks: