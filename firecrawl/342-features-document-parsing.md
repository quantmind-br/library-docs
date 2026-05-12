---
title: Document Parsing | Firecrawl
url: https://docs.firecrawl.dev/features/document-parsing
source: sitemap
fetched_at: 2026-03-23T07:24:38.527921-03:00
rendered_js: false
word_count: 297
summary: This document outlines Firecrawl's capabilities for parsing various file formats, including spreadsheets, Word documents, and PDFs, into structured markdown.
tags:
    - document-parsing
    - data-extraction
    - file-conversion
    - pdf-processing
    - markdown-output
    - automation
category: guide
---

Firecrawl provides powerful document parsing capabilities, allowing you to extract structured content from various document formats. This feature is particularly useful for processing files like spreadsheets, Word documents, and more.

## Supported Document Formats

Firecrawl currently supports the following document formats:

- **Excel Spreadsheets** (`.xlsx`, `.xls`)
  
  - Each worksheet is converted to an HTML table
  - Worksheets are separated by H2 headings with the sheet name
  - Preserves cell formatting and data types
- **Word Documents** (`.docx`, `.doc`, `.odt`, `.rtf`)
  
  - Extracts text content while preserving document structure
  - Maintains headings, paragraphs, lists, and tables
  - Preserves basic formatting and styling
- **PDF Documents** (`.pdf`)
  
  - Extracts text content with layout information
  - Preserves document structure including sections and paragraphs
  - Handles both text-based and scanned PDFs (with OCR support)
  - Supports `mode` option to control parsing strategy: `fast` (text-only), `auto` (text with OCR fallback, default), or `ocr` (force OCR)
  - Priced at 1 credit per-page. See [Pricing](https://docs.firecrawl.dev/pricing) for details.

### PDF Parsing Modes

Use the `parsers` option to control how PDFs are processed:

ModeDescription`auto`Attempts fast text-based extraction first, falls back to OCR if needed. This is the default.`fast`Text-based parsing only (embedded text). Fastest option, but will not extract text from scanned or image-heavy pages.`ocr`Forces OCR parsing on every page. Use for scanned documents or when `auto` misclassifies a page.

```
// Object syntax with mode
parsers: [{ type: "pdf", mode: "ocr", maxPages: 20 }]

// Default (auto mode)
parsers: [{ type: "pdf" }]
```

## How to Use Document Parsing

Document parsing in Firecrawl works automatically when you provide a URL that points to a supported document type. The system will detect the file type based on the URL extension or content-type header and process it accordingly.

### Example: Scraping an Excel File

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const doc = await firecrawl.scrape('https://example.com/data.xlsx');

console.log(doc.markdown);
```

### Example: Scraping a Word Document

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: "fc-YOUR-API-KEY" });

const doc = await firecrawl.scrape('https://example.com/data.docx');

console.log(doc.markdown);
```

## Output Format

All supported document types are converted to clean, structured markdown. For example, an Excel file with multiple sheets might be converted to:

```
## Sheet1

| Name  | Value |
|-------|-------|
| Item 1 | 100   |
| Item 2 | 200   |

## Sheet2

| Date       | Description  |
|------------|--------------|
| 2023-01-01 | First quarter|
```

> Are you an AI agent that needs a Firecrawl API key? See [firecrawl.dev/agent-onboarding/SKILL.md](https://www.firecrawl.dev/agent-onboarding/SKILL.md) for automated onboarding instructions.