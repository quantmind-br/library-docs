---
title: Document Sharding Guide
url: https://docs.bmad-method.org/how-to/shard-large-documents/
source: sitemap
fetched_at: 2026-04-08T11:31:21.241449156-03:00
rendered_js: false
word_count: 166
summary: This document explains the `bmad-shard-doc` tool, which is used to split excessively large markdown files into smaller, manageable, and organized sections based on their level 2 headings. It also details how the system prioritizes finding sharded versus whole versions of documents.
tags:
    - document-sharding
    - markdown-files
    - context-management
    - tool-usage
    - bmad-workflows
category: guide
---

Use the `bmad-shard-doc` tool if you need to split large markdown files into smaller, organized files for better context management.

Only use this if you notice your chosen tool / model combination is failing to load and read all the documents as input when needed.

## What is Document Sharding?

[Section titled “What is Document Sharding?”](#what-is-document-sharding)

Document sharding splits large markdown files into smaller, organized files based on level 2 headings (`## Heading`).

```text

Before Sharding:
_bmad-output/planning-artifacts/
└── PRD.md (large 50k token file)
After Sharding:
_bmad-output/planning-artifacts/
└── prd/
├── index.md                    # Table of contents with descriptions
├── overview.md                 # Section 1
├── user-requirements.md        # Section 2
├── technical-requirements.md   # Section 3
└── ...                         # Additional sections
```

### 1. Run the Shard-Doc Tool

[Section titled “1. Run the Shard-Doc Tool”](#1-run-the-shard-doc-tool)

### 2. Follow the Interactive Process

[Section titled “2. Follow the Interactive Process”](#2-follow-the-interactive-process)

```text

Agent: Which document would you like to shard?
User: docs/PRD.md
Agent: Default destination: docs/prd/
Accept default? [y/n]
User: y
Agent: Sharding PRD.md...
✓ Created 12 section files
✓ Generated index.md
✓ Complete!
```

## How Workflow Discovery Works

[Section titled “How Workflow Discovery Works”](#how-workflow-discovery-works)

BMad workflows use a **dual discovery system**:

1. **Try whole document first** - Look for `document-name.md`
2. **Check for sharded version** - Look for `document-name/index.md`
3. **Priority rule** - Whole document takes precedence if both exist - remove the whole document if you want the sharded to be used instead

All BMM workflows support both formats:

- Whole documents
- Sharded documents
- Automatic detection
- Transparent to user