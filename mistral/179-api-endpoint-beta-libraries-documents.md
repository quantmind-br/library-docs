---
title: Beta Libraries Documents
url: https://docs.mistral.ai/api/endpoint/beta/libraries/documents
source: sitemap
fetched_at: 2026-04-26T04:01:33.697942591-03:00
rendered_js: false
word_count: 316
summary: API specification for managing library documents, including endpoints for uploading, retrieving metadata, updating, deleting, and processing document content.
tags:
    - api-reference
    - document-management
    - library-api
    - ocr-processing
    - file-upload
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Libraries Documents

Document management API for library resources.

---

## List Documents

`GET /v1/libraries/{library_id}/documents`

List documents uploaded to a library.

---

## Upload Document

`POST /v1/libraries/{library_id}/documents`

Upload a document. Queued for processing; status changes when processed. Processing must complete for discoverability in search.

---

## Get Document Metadata

`GET /v1/libraries/{library_id}/documents/{document_id}`

Retrieve metadata for a document.

---

## Update Document Metadata

`PUT /v1/libraries/{library_id}/documents/{document_id}`

Update document name.

---

## Delete Document

`DELETE /v1/libraries/{library_id}/documents/{document_id}`

Delete document from library and search index.

---

## Get Text Content

`GET /v1/libraries/{library_id}/documents/{document_id}/text_content`

Retrieve text content. For PDF, DOCX, PPTX, content is extracted via Mistral OCR.

---

## Get Processing Status

`GET /v1/libraries/{library_id}/documents/{document_id}/status`

Retrieve document processing status.

---

## Get Signed URL

`GET /v1/libraries/{library_id}/documents/{document_id}/signed-url`

Get signed URL (expires in 30 minutes, publicly accessible).

---

## Get Extracted Text Signed URL

`GET /v1/libraries/{library_id}/documents/{document_id}/extracted-text-signed-url`

Get signed URL for OCR-extracted text.

---

## Reprocess Document

`POST /v1/libraries/{library_id}/documents/{document_id}/reprocess`

Reprocess a document (billed again).

#document-management #library-api #ocr-processing
