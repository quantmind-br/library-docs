---
title: 'Enterprise Document AI with Mistral: Healthcare Document Processing - Mistral AI Cookbook'
url: https://docs.mistral.ai/cookbooks/mistral-ocr-hcls-ocr_hcls
source: crawler
fetched_at: 2026-01-29T07:33:43.368412737-03:00
rendered_js: false
word_count: 699
---

Healthcare generates 30% of the world's data, yet much of it remains locked in PDFs, scanned faxes, and unstructured documents. As regulations like the CMS prior authorization mandate push toward digital-first operations and hospital staffing shortages intensify, automated document processing has become critical infrastructure, not just for patient intake, but for back office operations like invoice management, medical billing and coding, and clinical documentation at scale.

**Key challenges driving Document AI adoption:**

- 30% of global data originates in healthcare, mostly unstructured
- Legacy systems rely on paper, fax, and non-digital formats
- Regulatory pressure (CMS mandates, interoperability requirements)
- Severe staffing shortages across clinical and administrative roles

**Mistral OCR 3** handles intricate healthcare documents—handwritten notes, nested lab tables, checkboxes, and multi-page forms—with accuracy comparable to commercial solutions at a fraction of the cost. This cookbook demonstrates how to get started.

> You can also interactively explore Document AI in [AI Studio](https://console.mistral.ai/build/document-ai/ocr-playground)

## 1. Setup

First, let's install `mistralai` and download the document.

### Sample Document

This cookbook uses `patient-packet-completed.pdf` - a synthetic multi-page patient packet containing demographics, vitals, and clinical notes.

### Create Client

We will need to set up our client. You can create an API key on [AI Studio](https://console.mistral.ai/api-keys/).

* * *

## 2. Use Case: Patient Medical Record Packet OCR Processing

This section showcases **Mistral OCR 3** capabilities using a 3-page patient packet. We will use each page to highlight various features:

&gt; **Note**: Sample data is synthetic/anonymized.

### 2.1 Setup: Load and Process Document

First, let's encode the PDF and run OCR on the full packet. We'll then explore each page's output.

Process the full document and get the OCR output:

Let's stylize the output for easier understanding

### 2.2 Form Elements: Checkboxes & Structured Fields (Page 1)

Page 1 contains a **Patient Admission Form** with checkboxes, handwriting, and fill-in lines. Mistral OCR 3 uses **unified Unicode checkbox representation** (☐ unchecked, ☑ checked) for consistent parsing.

### 2.3 HTML Table Output: Vital Signs Flowsheet (Page 2)

Page 2 contains a **Vital Signs Flowsheet** with complex table structures. Mistral OCR 3 gives the option to output tables as **HTML** with proper `rowspan` and `colspan` attributes, preserving the original structure for accurate data extraction.

### 2.4 Image Annotations: X-ray (Page 3)

Page 3 contains an **X-ray image**. Mistral OCR 3 can detect, extract, and annotate images within documents. The image is embedded in the markdown output with base64 encoding.

## 3. Document Intelligence Using Annotations

Moving from notebooks to production requires patterns for scale, reliability, and interoperability. This section demonstrates a **progressive pipeline** where we perform the following using DocAI Annotations:

1. **Classification** → Identify document types before extraction
2. **Batch Processing** → Handle multiple documents concurrently
3. **FHIR Generation** → Transform extracted data into healthcare-standard formats

> **Note**: Refer to [this cookbook](https://docs.mistral.ai/cookbooks/mistral-ocr-data_extraction) for an intro to Annotations.

## Production Patterns Setup - imports and utilities

### 3.1 Document Classification and Intelligent Routing

Healthcare organizations receive mixed document types daily—faxes, scanned forms, digital PDFs. Before extraction, classify incoming documents to determine:

- **Document type** (demographics, vitals, lab results, progress notes)
- **Routing destination** (billing, clinical, pharmacy)
- **Processing urgency** (stat vs routine)

This information will then inform which extraction schema to apply in the next section.

Based on the classfication defined in the previous step, we'll extract different data elements from each classified document.

### 3.3 Combine Classification and Extraction with Batch Processing

Production systems process hundreds of documents daily. This pattern extends classification & extraction to handle **multi-page packets** where each page may be a different document type (demographics, vitals, lab results, etc.).

### 3.4 FHIR Resource Generation

Extracted data is only valuable if it integrates with clinical systems. **FHIR (Fast Healthcare Interoperability Resources)** is the industry standard for healthcare data exchange, supported by Epic, Cerner, and all major EHRs.

This pattern transforms our batch-extracted data into FHIR R4 resources:

- **Patient** → Demographics from intake forms
- **Observation** → Vital signs measurements

The resulting FHIR Bundle can be POSTed to any FHIR-compliant system.

## 4. Summary & Next Steps

This cookbook demonstrated a **complete production pipeline** for healthcare OCR:

**Production enhancements to consider:**

- **Confidence thresholds** → Flag low-confidence extractions for human review
- **Async processing** → Use `asyncio` for higher throughput
- **Audit logging** → Track PHI access for HIPAA compliance
- **FHIR validation** → Validate bundles against US Core profiles before submission
- **Webhook notifications** → Alert downstream systems when processing completes