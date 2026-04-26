---
title: Files upload | Mistral Docs
url: https://docs.mistral.ai/le-chat/research-analysis/files-upload
source: sitemap
fetched_at: 2026-04-26T04:08:15.730321217-03:00
rendered_js: false
word_count: 549
summary: This document explains how to upload and utilize various file types within Le Chat for analysis, including document extraction, image interpretation, and structured data processing with the Code Interpreter.
tags:
    - file-uploads
    - data-analysis
    - document-processing
    - code-interpreter
    - chat-interface
    - ai-assistant
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Upload documents, images, and spreadsheets directly into a conversation. Le Chat reads the content and uses it as context for questions, extraction, and answers based on your data.

File uploads are available on **all plans** with no setup required. Usage limits apply based on your plan. [Pricing page](https://mistral.ai/pricing).

## Upload Files

**Two ways:**
- **Drag and drop**: drag one or more files into the chat window
- **`+` button**: click the `+` icon in the chat toolbar → `Upload Files` → select files

You can upload multiple files at once (or even a folder). Le Chat keeps them in context for the full conversation.

> [!tip]
> Use descriptive filenames — they make it easier to reference specific files when you have several in the same conversation.

## Documents

Upload a PDF, Word file, or presentation and ask Le Chat to focus on what matters to you. Answers come directly from the uploaded content.

Typical prompts:
- *"Summarize this annual report with a focus on financial risks."*
- *"Extract all dates, parties, and obligations from this contract."*
- *"List the key security findings in this audit report."*
- *"Compare slide 3 and slide 7 and list the differences."*

Follow up to go deeper — Le Chat remembers uploaded files throughout the conversation.

## Images

Le Chat can interpret photos, diagrams, screenshots, and scanned pages.

- **Text extraction**: *"Extract all the text from this scanned invoice."*
- **Diagram interpretation**: *"Describe the architecture shown in this diagram."*
- **Screenshot analysis**: *"What error is shown in this screenshot?"*

For heavier document processing (structured extraction from scanned PDFs, multi-page forms, bulk handwritten content), check Studio's [Document Processing](https://docs.mistral.ai/studio-api/document-processing) features.

## Spreadsheets and Structured Data

For CSV or Excel files, enable [Code Interpreter](https://docs.mistral.ai/le-chat/content-creation/code-interpreter) to get the most out of your uploads:

1. Click the `+` icon or type `/` → select `Tools` → enable `Code Interpreter`
2. Upload your spreadsheet using the `+` button
3. Ask your question

Typical prompts:
- *"Show me all sales from the North region."*
- *"What's the average deal size by quarter?"*
- *"Graph the monthly revenue trend as a line chart."*

Code Interpreter writes and runs the Python code for you, displaying results (tables, charts, statistics) inline.

## Best Practices

- **Be specific** — tell Le Chat what to focus on: *"Summarize this contract for a compliance officer"* gives better results than *"Summarize this file"*
- **Use action verbs** — summarize, extract, compare, explain, highlight, list, convert
- **Reference files explicitly** — when you have several uploads, mention the filename: *"In `AnnualReport_2024.pdf`, page 14, extract the revenue breakdown"*
- **Iterate** — follow up to refine, translate, or reformat the output

## Related Tools

- [**Code Interpreter**](https://docs.mistral.ai/le-chat/content-creation/code-interpreter): run Python on your data for charts and statistics
- [**Canvas**](https://docs.mistral.ai/le-chat/content-creation/canvas): turn analysis results into polished documents
- [**Open URL**](https://docs.mistral.ai/le-chat/research-analysis/open-url): analyze web pages by sharing URLs
- [**Libraries**](https://docs.mistral.ai/le-chat/knowledge-integrations/libraries): build permanent knowledge bases from documents

#file-uploads #data-analysis #document-processing