---
title: Průvodce dělením dokumentů
url: https://docs.bmad-method.org/cs/how-to/shard-large-documents/
source: sitemap
fetched_at: 2026-04-08T11:29:27.61772649-03:00
rendered_js: false
word_count: 148
summary: This document explains the use of the `bmad-shard-doc` tool, which divides large markdown files into smaller, manageable sections based on level 2 headings to improve context handling for processing workflows. It also describes how BMad workflows utilize a dual search system that prioritizes whole documents over sharded versions.
tags:
    - markdown-sharding
    - document-management
    - context-handling
    - bmad-workflow
    - content-splitting
    - tool-usage
category: guide
---

Použijte nástroj `bmad-shard-doc`, pokud potřebujete rozdělit velké markdown soubory na menší, organizované soubory pro lepší správu kontextu.

Použijte pouze pokud si všimnete, že váš zvolený nástroj / model nedokáže načíst a přečíst všechny dokumenty jako vstup, když je to potřeba.

## Co je dělení dokumentů?

[Section titled “Co je dělení dokumentů?”](#co-je-d%C4%9Blen%C3%AD-dokument%C5%AF)

Dělení dokumentů rozděluje velké markdown soubory na menší, organizované soubory na základě nadpisů úrovně 2 (`## Nadpis`).

```text

Před dělením:
_bmad-output/planning-artifacts/
└── PRD.md (velký soubor o 50k tokenech)
Po dělení:
_bmad-output/planning-artifacts/
└── prd/
├── index.md                    # Obsah s popisy
├── overview.md                 # Sekce 1
├── user-requirements.md        # Sekce 2
├── technical-requirements.md   # Sekce 3
└── ...                         # Další sekce
```

### 1. Spusťte nástroj Shard-Doc

[Section titled “1. Spusťte nástroj Shard-Doc”](#1-spus%C5%A5te-n%C3%A1stroj-shard-doc)

### 2. Následujte interaktivní proces

[Section titled “2. Následujte interaktivní proces”](#2-n%C3%A1sledujte-interaktivn%C3%AD-proces)

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

## Jak funguje vyhledávání workflow

[Section titled “Jak funguje vyhledávání workflow”](#jak-funguje-vyhled%C3%A1v%C3%A1n%C3%AD-workflow)

BMad workflow používají **duální systém vyhledávání**:

1. **Nejprve zkusí celý dokument** — Hledá `document-name.md`
2. **Zkontroluje rozdělenou verzi** — Hledá `document-name/index.md`
3. **Pravidlo priority** — Celý dokument má přednost, pokud existují oba — odstraňte celý dokument, pokud chcete použít rozdělenou verzi

Všechny BMM workflow podporují oba formáty:

- Celé dokumenty
- Rozdělené dokumenty
- Automatická detekce
- Transparentní pro uživatele