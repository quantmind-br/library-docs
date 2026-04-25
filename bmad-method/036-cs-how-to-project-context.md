---
title: Správa kontextu projektu
url: https://docs.bmad-method.org/cs/how-to/project-context/
source: sitemap
fetched_at: 2026-04-08T11:29:23.516800825-03:00
rendered_js: false
word_count: 360
summary: This document explains how to create and utilize a 'project-context.md' file to ensure AI agents adhere to the specific technical preferences, conventions, and architectural decisions of an existing project across all workflows.
tags:
    - ai-agents
    - project-context
    - coding-conventions
    - implementation-rules
    - software-architecture
    - metadata
category: guide
---

Použijte soubor `project-context.md` k zajištění toho, aby AI agenti dodržovali technické preference a pravidla implementace vašeho projektu ve všech workflow. Aby byl vždy dostupný, můžete také přidat řádek `Important project context and conventions are located in [cesta k project context]/project-context.md` do souboru kontextu nebo pravidel vašeho nástroje (jako je `AGENTS.md`).

- Máte silné technické preference před začátkem architektury
- Dokončili jste architekturu a chcete zachytit rozhodnutí pro implementaci
- Pracujete na existující kódové bázi se zavedenými vzory
- Všimnete si, že agenti dělají nekonzistentní rozhodnutí napříč stories

## Krok 1: Vyberte přístup

[Section titled “Krok 1: Vyberte přístup”](#krok-1-vyberte-p%C5%99%C3%ADstup)

**Ruční vytvoření** — Nejlepší, když přesně víte, jaká pravidla chcete dokumentovat

**Generování po architektuře** — Nejlepší pro zachycení rozhodnutí učiněných během solutioningu

**Generování pro existující projekty** — Nejlepší pro objevení vzorů v existujících kódových bázích

## Krok 2: Vytvořte soubor

[Section titled “Krok 2: Vytvořte soubor”](#krok-2-vytvo%C5%99te-soubor)

### Možnost A: Ruční vytvoření

[Section titled “Možnost A: Ruční vytvoření”](#mo%C5%BEnost-a-ru%C4%8Dn%C3%AD-vytvo%C5%99en%C3%AD)

Vytvořte soubor na `_bmad-output/project-context.md`:

```bash

mkdir-p_bmad-output
touch_bmad-output/project-context.md
```

Přidejte váš technologický stack a pravidla implementace:

```markdown

---
project_name: 'MyProject'
user_name: 'YourName'
date: '2026-02-15'
sections_completed: ['technology_stack', 'critical_rules']
---
# Project Context for AI Agents
## Technology Stack & Versions
- Node.js 20.x, TypeScript 5.3, React 18.2
- State: Zustand
- Testing: Vitest, Playwright
- Styling: Tailwind CSS
## Critical Implementation Rules
**TypeScript:**
- Strict mode enabled, no `any` types
- Use `interface` for public APIs, `type` for unions
**Code Organization:**
- Components in `/src/components/` with co-located tests
- API calls use `apiClient` singleton — never fetch directly
**Testing:**
- Unit tests focus on business logic
- Integration tests use MSW for API mocking
```

### Možnost B: Generování po architektuře

[Section titled “Možnost B: Generování po architektuře”](#mo%C5%BEnost-b-generov%C3%A1n%C3%AD-po-architektu%C5%99e)

Spusťte workflow v novém chatu:

```bash

bmad-generate-project-context
```

Workflow skenuje váš dokument architektury a soubory projektu a generuje kontextový soubor zachycující učiněná rozhodnutí.

### Možnost C: Generování pro existující projekty

[Section titled “Možnost C: Generování pro existující projekty”](#mo%C5%BEnost-c-generov%C3%A1n%C3%AD-pro-existuj%C3%ADc%C3%AD-projekty)

Pro existující projekty spusťte:

```bash

bmad-generate-project-context
```

Workflow analyzuje vaši kódovou bázi, identifikuje konvence a vygeneruje kontextový soubor, který můžete zkontrolovat a upřesnit.

## Krok 3: Ověřte obsah

[Section titled “Krok 3: Ověřte obsah”](#krok-3-ov%C4%9B%C5%99te-obsah)

Zkontrolujte vygenerovaný soubor a ujistěte se, že zachycuje:

- Správné verze technologií
- Vaše skutečné konvence (ne generické osvědčené postupy)
- Pravidla, která předcházejí běžným chybám
- Vzory specifické pro framework

Ručně upravte pro doplnění chybějícího nebo odstranění nepřesností.

Soubor `project-context.md`, který:

- Zajistí, že všichni agenti dodržují stejné konvence
- Zabrání nekonzistentním rozhodnutím napříč stories
- Zachytí architektonická rozhodnutí pro implementaci
- Slouží jako reference pro vzory a pravidla vašeho projektu

<!--THE END-->

- [**Vysvětlení kontextu projektu**](https://docs.bmad-method.org/cs/explanation/project-context/) — Zjistěte více o tom, jak to funguje
- [**Mapa pracovních postupů**](https://docs.bmad-method.org/cs/reference/workflow-map/) — Podívejte se, které workflow načítají kontext projektu