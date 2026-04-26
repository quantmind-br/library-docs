---
title: Annotations | Mistral Docs
url: https://docs.mistral.ai/studio-api/document-processing/annotations
source: sitemap
fetched_at: 2026-04-26T04:12:45.498137108-03:00
rendered_js: false
word_count: 152
summary: Configure and utilize BBox Annotation for image-based data extraction using defined schemas and OCR processing.
tags:
    - bbox-annotation
    - image-processing
    - ocr-extraction
    - data-annotation
    - schema-definition
    - structured-output
category: tutorial
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# BBox Annotations

Extract structured data from document images using defined schemas.

## Define Response Format

### Pydantic/Zod Schema

```python
from pydantic import BaseModel

class DocumentAnnotation(BaseModel):
    invoice_number: str
    date: str
    total_amount: float
    vendor_name: str
```

### JSON Schema

```json
{
    "type": "object",
    "properties": {
        "invoice_number": {"type": "string"},
        "date": {"type": "string"},
        "total_amount": {"type": "number"},
        "vendor_name": {"type": "string"}
    },
    "required": ["invoice_number", "date", "total_amount"]
}
```

## Add Field Descriptions

```python
class DocumentAnnotation(BaseModel):
    invoice_number: str  # "Invoice number (e.g., INV-2024-001)"
    date: str  # "Invoice date in YYYY-MM-DD format"
    total_amount: float  # "Total amount in USD"
    vendor_name: str  # "Name of the vendor/supplier"
```

## Make Annotation Request

```python
response = client.ocr.bbox_annotation(
    model="mistral-ocr-latest",
    document=open("invoice.png", "rb"),
    bbox_annotation_format=DocumentAnnotation
)
```

## Response

The annotation response includes extracted values mapped to your schema:

```python
{
    "invoice_number": "INV-2024-123",
    "date": "2024-03-15",
    "total_amount": 1599.99,
    "vendor_name": "Acme Corp"
}
```

## Use with Extracted Document

```python
# First extract the document
doc_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=open("invoice.png", "rb")
)

# Then annotate
annotation = client.ocr.bbox_annotation(
    model="mistral-ocr-latest",
    document=open("invoice.png", "rb"),
    bbox_annotation_format=DocumentAnnotation
)
```

![BBox Annotation example](https://docs.mistral.ai/img/img-1.jpeg)

>bbox-annotation #image-processing #ocr-extraction #data-annotation #schema-definition #structured-output
