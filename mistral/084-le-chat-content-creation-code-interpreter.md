---
title: Code Interpreter | Mistral Docs
url: https://docs.mistral.ai/le-chat/content-creation/code-interpreter
source: sitemap
fetched_at: 2026-04-26T04:07:37.70841923-03:00
rendered_js: false
word_count: 506
summary: This document explains how to use the Code Interpreter tool in Le Chat to execute Python code for data analysis, file processing, and visualization in a secure sandbox environment.
tags:
    - code-interpreter
    - python-execution
    - data-analysis
    - file-processing
    - le-chat
    - sandbox-environment
    - visualization
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Code Interpreter lets you **run Python directly inside Le Chat**. Describe what you want in plain language and Le Chat generates and executes the code for you.

Code runs in a **secure, isolated environment** with no internet access. It cannot reach your system or external services. Common data-analysis packages are preinstalled (pandas, numpy, matplotlib). Uploaded files are available for the current conversation only.

## What You Can Do

- **Data analysis**: explore CSV, XLSX, or JSON files — summarize, filter, flag outliers, clean missing values
- **Charts and visuals**: generate line charts, bar charts, pie charts, or any Matplotlib visualization
- **Calculations**: work through formulas, financial models, unit conversions with verified accuracy
- **File transformations**: convert formats, merge datasets, export processed results

## Enable Code Interpreter

1. Click the `+` icon or type `/` in the chat window.
2. Select `Tools` then enable `Code Interpreter`.

The tool stays active for the duration of the conversation and subsequent chats.

> [!info]
> Usage is subject to rate limits based on your plan. [Pricing page](https://mistral.ai/pricing).

## How to Use

Describe what you want **in plain language**. Le Chat writes and executes the Python code for you. The code runs in the sandbox and returns tables, figures, or files inline.

Follow up to refine results, adjust filters, or ask for explanations of what the code does.

> [!warning]
> Code Interpreter cannot fetch files directly from URLs. Download data locally and upload the file, or enable [Web search](https://docs.mistral.ai/le-chat/research-analysis/web-search) and ask Le Chat to fetch the data first.

## Supported File Formats

| Category | Formats |
|----------|---------|
| **Documents** | PDF, Word (`.docx`, `.doc`), PowerPoint (`.pptx`, `.ppt`), ODT, EPUB, RTF |
| **Spreadsheets** | Excel (`.xlsx`, `.xls`), CSV, ODS, Numbers |
| **Images** | PNG, JPEG, WebP, GIF |
| **Text and markup** | TXT, Markdown, RST, LaTeX |
| **Data formats** | JSON, JSONL, XML, YAML |
| **Code** | Python, JavaScript/TypeScript, Java, Go, Rust, C/C++, Ruby, PHP, SQL, and more |
| **Email** | EML, MSG |

## Tips

- **Be specific** for charts or tables — specify column names, filters, desired output format
- **Ask for explanations** — try *"Explain the steps and show the code"*
- **Iterate** — follow up to fine-tune output (e.g., *"Now add a rolling average and label the axes"*)
- **Prototype with smaller files** — upload a sample to test approach, then scale up
- **Avoid sharing secrets** — never share API keys or credentials in the chat or in code

## Related Tools

- [**Canvas**](https://docs.mistral.ai/le-chat/content-creation/canvas): edit and refine code, data, and text in a side-by-side editor
- [**Files upload**](https://docs.mistral.ai/le-chat/research-analysis/files-upload): import documents, spreadsheets, images
- [**Chat**](https://docs.mistral.ai/le-chat/conversation/chat): the conversation interface where Code Interpreter runs

#code-interpreter #python-execution #data-analysis