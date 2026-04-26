---
title: Analyze data | Mistral Docs
url: https://docs.mistral.ai/le-chat/quickstarts/analyze-data
source: sitemap
fetched_at: 2026-04-26T04:08:06.937848624-03:00
rendered_js: false
word_count: 350
summary: This document provides a guide on how to use the Code Interpreter feature in Le Chat to perform automated data analysis, visualization, and statistical processing of spreadsheet files.
tags:
    - data-analysis
    - code-interpreter
    - le-chat
    - file-upload
    - data-visualization
    - natural-language-processing
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Upload a spreadsheet to [Le Chat](https://chat.mistral.ai) and ask questions in plain language. Code Interpreter runs Python in a secure sandbox to produce charts, tables, and statistical summaries.

- Upload CSV, XLSX, or JSON files via the attachment icon
- Ask natural language questions; the model writes and executes pandas/matplotlib code
- Download charts or copy tables directly from the chat

**Time to complete:** ~10 minutes

**Prerequisites:**
- Le Chat account (Pro or Team recommended; Free has daily limits)
- A data file (CSV, XLSX, or JSON)

> [!tip]
> Use files with clear column headers so the model reads them correctly.

## Steps

1. Open [New chat](https://chat.mistral.ai).
2. Click the **attachment icon** (paperclip) in the message bar.
3. Select your data file: e.g., `sales-q4-2025.csv`.
4. Le Chat displays a preview. Confirm it looks correct.

Type a question in natural language. Code Interpreter runs Python (pandas, matplotlib) in a secure sandbox and returns the result.

### Example prompts:

- *"Summarize this dataset — rows, columns, key statistics."*
- *"Show monthly revenue trends as a line chart."*
- *"Top 5 products by total sales as a bar chart."*
- *"Correlation between marketing spend and revenue."*

The model writes and runs Python code automatically. You see tables, charts, and text directly in the chat.

## Follow-up Questions

Build on previous results by asking follow-up questions. The model remembers the data context.

- **Refine a chart**: *"Make the chart wider and add data labels."*
- **Filter data**: *"Show only rows where region is Europe."*
- **Compare periods**: *"Compare Q3 vs Q4 revenue by product category."*

## Save Results

- **Download charts**: right-click any generated chart and select **Save image**
- **Copy tables**: highlight and copy any generated table
- **Use Canvas**: ask *"Put this summary in Canvas"* to create an editable document

## Verification

Your data analysis is working correctly if:
- The model correctly identified your column names and data types
- Generated charts display accurate data from your file
- Follow-up questions reference the same dataset without re-uploading
- Statistical calculations (mean, median, correlation) match expected values

If the model misinterprets a column, try: *"The 'Date' column is in DD/MM/YYYY format"* to clarify.

#data-analysis #code-interpreter #le-chat