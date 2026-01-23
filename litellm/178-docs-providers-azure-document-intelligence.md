---
title: Azure Document Intelligence OCR | liteLLM
url: https://docs.litellm.ai/docs/providers/azure_document_intelligence
source: sitemap
fetched_at: 2026-01-21T19:48:12.460160385-03:00
rendered_js: false
word_count: 386
summary: This document provides a comprehensive guide on integrating Azure Document Intelligence with LiteLLM for OCR and document analysis, covering SDK usage, proxy configuration, and automated polling mechanisms.
tags:
    - azure-document-intelligence
    - litellm
    - ocr
    - text-extraction
    - document-analysis
    - python-sdk
    - api-gateway
category: guide
---

## Overview[​](#overview "Direct link to Overview")

PropertyDetailsDescriptionAzure Document Intelligence (formerly Form Recognizer) provides advanced document analysis capabilities including text extraction, layout analysis, and structure recognitionProvider Route on LiteLLM`azure_ai/doc-intelligence/`Supported Operations`/ocr`Link to Provider Doc[Azure Document Intelligence ↗](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)

Extract text and analyze document structure using Azure Document Intelligence's powerful prebuilt models.

## Quick Start[​](#quick-start "Direct link to Quick Start")

### **LiteLLM SDK**[​](#litellm-sdk "Direct link to litellm-sdk")

SDK Usage

```
import litellm
import os

# Set environment variables
os.environ["AZURE_DOCUMENT_INTELLIGENCE_API_KEY"]="your-api-key"
os.environ["AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"]="https://your-resource.cognitiveservices.azure.com"

# OCR with PDF URL
response = litellm.ocr(
    model="azure_ai/doc-intelligence/prebuilt-layout",
    document={
"type":"document_url",
"document_url":"https://example.com/document.pdf"
}
)

# Access extracted text
for page in response.pages:
print(f"Page {page.index}:")
print(page.markdown)
```

### **LiteLLM PROXY**[​](#litellm-proxy "Direct link to litellm-proxy")

proxy\_config.yaml

```
model_list:
-model_name: azure-doc-intel
litellm_params:
model: azure_ai/doc-intelligence/prebuilt-layout
api_key: os.environ/AZURE_DOCUMENT_INTELLIGENCE_API_KEY
api_base: os.environ/AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT
model_info:
mode: ocr
```

**Start Proxy**

```
litellm --config proxy_config.yaml
```

**Call OCR via Proxy**

cURL Request

```
curl -X POST http://localhost:4000/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "model": "azure-doc-intel",
    "document": {
      "type": "document_url",
      "document_url": "https://arxiv.org/pdf/2201.04234"
    }
  }'
```

## How It Works[​](#how-it-works "Direct link to How It Works")

Azure Document Intelligence uses an asynchronous API pattern. LiteLLM AI Gateway handles the request/response transformation and polling automatically.

### Complete Flow Diagram[​](#complete-flow-diagram "Direct link to Complete Flow Diagram")

### What LiteLLM Does For You[​](#what-litellm-does-for-you "Direct link to What LiteLLM Does For You")

When you call `litellm.ocr()` via SDK or `/ocr` via Proxy:

1. **Request Transformation**: Converts Mistral OCR format → Azure Document Intelligence format
2. **Submits Document**: Sends transformed request to Azure DI API
3. **Handles 202 Response**: Captures the `Operation-Location` URL from response headers
4. **Automatic Polling**:
   
   - Polls the operation URL at intervals specified by `retry-after` header (default: 2 seconds)
   - Continues until status is `succeeded` or `failed`
   - Respects Azure's rate limiting via `retry-after` headers
5. **Response Transformation**: Converts Azure DI format → Mistral OCR format
6. **Returns Result**: Sends unified Mistral format response to client

**Polling Configuration:**

- Default timeout: 120 seconds
- Configurable via `AZURE_OPERATION_POLLING_TIMEOUT` environment variable
- Uses sync (`time.sleep()`) or async (`await asyncio.sleep()`) based on call type

info

**Typical processing time**: 2-10 seconds depending on document size and complexity

## Supported Models[​](#supported-models "Direct link to Supported Models")

Azure Document Intelligence offers several prebuilt models optimized for different use cases:

### prebuilt-layout (Recommended)[​](#prebuilt-layout-recommended "Direct link to prebuilt-layout (Recommended)")

Best for general document OCR with structure preservation.

- SDK
- Proxy Config

Layout Model - SDK

```
import litellm
import os

os.environ["AZURE_DOCUMENT_INTELLIGENCE_API_KEY"]="your-api-key"
os.environ["AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"]="https://your-resource.cognitiveservices.azure.com"

response = litellm.ocr(
    model="azure_ai/doc-intelligence/prebuilt-layout",
    document={
"type":"document_url",
"document_url":"https://example.com/document.pdf"
}
)
```

**Features:**

- Text extraction with markdown formatting
- Table detection and extraction
- Document structure analysis
- Paragraph and section recognition

**Pricing:** $10 per 1,000 pages

### prebuilt-read[​](#prebuilt-read "Direct link to prebuilt-read")

Optimized for reading text from documents - fastest and most cost-effective.

- SDK
- Proxy Config

Read Model - SDK

```
import litellm
import os

os.environ["AZURE_DOCUMENT_INTELLIGENCE_API_KEY"]="your-api-key"
os.environ["AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"]="https://your-resource.cognitiveservices.azure.com"

response = litellm.ocr(
    model="azure_ai/doc-intelligence/prebuilt-read",
    document={
"type":"document_url",
"document_url":"https://example.com/document.pdf"
}
)
```

**Features:**

- Fast text extraction
- Optimized for reading-heavy documents
- Basic structure recognition

**Pricing:** $1.50 per 1,000 pages

### prebuilt-document[​](#prebuilt-document "Direct link to prebuilt-document")

General-purpose document analysis with key-value pairs.

- SDK
- Proxy Config

Document Model - SDK

```
import litellm
import os

os.environ["AZURE_DOCUMENT_INTELLIGENCE_API_KEY"]="your-api-key"
os.environ["AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"]="https://your-resource.cognitiveservices.azure.com"

response = litellm.ocr(
    model="azure_ai/doc-intelligence/prebuilt-document",
    document={
"type":"document_url",
"document_url":"https://example.com/document.pdf"
}
)
```

**Pricing:** $10 per 1,000 pages

## Document Types[​](#document-types "Direct link to Document Types")

Azure Document Intelligence supports various document formats.

### PDF Documents[​](#pdf-documents "Direct link to PDF Documents")

PDF OCR

```
response = litellm.ocr(
    model="azure_ai/doc-intelligence/prebuilt-layout",
    document={
"type":"document_url",
"document_url":"https://example.com/document.pdf"
}
)
```

### Image Documents[​](#image-documents "Direct link to Image Documents")

Image OCR

```
response = litellm.ocr(
    model="azure_ai/doc-intelligence/prebuilt-layout",
    document={
"type":"image_url",
"image_url":"https://example.com/image.png"
}
)
```

**Supported image formats:** JPEG, PNG, BMP, TIFF

### Base64 Encoded Documents[​](#base64-encoded-documents "Direct link to Base64 Encoded Documents")

Base64 PDF

```
import base64

# Read and encode PDF
withopen("document.pdf","rb")as f:
    pdf_base64 = base64.b64encode(f.read()).decode()

response = litellm.ocr(
    model="azure_ai/doc-intelligence/prebuilt-layout",
    document={
"type":"document_url",
"document_url":f"data:application/pdf;base64,{pdf_base64}"
}
)
```

## Response Format[​](#response-format "Direct link to Response Format")

Response Structure

```
# Response has the following structure
response.pages          # List of pages with extracted text
response.model          # Model used
response.object# "ocr"
response.usage_info     # Token usage information

# Access page content
for page in response.pages:
print(f"Page {page.index}:")
print(page.markdown)

# Page dimensions (in pixels)
if page.dimensions:
print(f"Width: {page.dimensions.width}px")
print(f"Height: {page.dimensions.height}px")
```

## Async Support[​](#async-support "Direct link to Async Support")

Async Usage

```
import litellm
import asyncio

asyncdefprocess_document():
    response =await litellm.aocr(
        model="azure_ai/doc-intelligence/prebuilt-layout",
        document={
"type":"document_url",
"document_url":"https://example.com/document.pdf"
}
)
return response

# Run async function
response = asyncio.run(process_document())
```

## Cost Tracking[​](#cost-tracking "Direct link to Cost Tracking")

LiteLLM automatically tracks costs for Azure Document Intelligence OCR:

ModelCost per 1,000 Pagesprebuilt-read$1.50prebuilt-layout$10.00prebuilt-document$10.00

View Cost

```
response = litellm.ocr(
    model="azure_ai/doc-intelligence/prebuilt-layout",
    document={"type":"document_url","document_url":"https://..."}
)

# Access cost information
print(f"Cost: ${response._hidden_params.get('response_cost',0)}")
```

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

- [Azure Document Intelligence Documentation](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
- [Pricing Details](https://azure.microsoft.com/en-us/pricing/details/ai-document-intelligence/)
- [Supported File Formats](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept-model-overview)
- [LiteLLM OCR Documentation](https://docs.litellm.ai/docs/ocr)