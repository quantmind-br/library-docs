---
title: Kontext projektu
url: https://docs.bmad-method.org/cs/explanation/project-context/
source: sitemap
fetched_at: 2026-04-08T11:29:08.902509027-03:00
rendered_js: false
word_count: 603
summary: This document serves as a comprehensive guide explaining the purpose, structure, and usage of the `project-context.md` file for AI agents working on development projects. It details how this single source of truth captures project standards, technological stacks, and critical implementation rules to ensure coding consistency across all workflows.
tags:
    - ai-agent-guidance
    - project-standardization
    - llm-context
    - software-development-process
    - coding-conventions
category: guide
---

Soubor `project-context.md` je implementační průvodce vašeho projektu pro AI agenty. Podobně jako „ústava“ v jiných vývojových systémech zachycuje pravidla, vzory a preference, které zajišťují konzistentní generování kódu napříč všemi workflow.

AI agenti neustále dělají implementační rozhodnutí — jaké vzory následovat, jak strukturovat kód, jaké konvence používat. Bez jasného vedení mohou:

- Následovat generické osvědčené postupy, které neodpovídají vaší kódové bázi
- Dělat nekonzistentní rozhodnutí napříč různými stories
- Přehlédnout požadavky nebo omezení specifická pro projekt

Soubor `project-context.md` toto řeší dokumentací toho, co agenti potřebují vědět, ve stručném formátu optimalizovaném pro LLM.

Každý implementační workflow automaticky načítá `project-context.md`, pokud existuje. Architektonický workflow ho také načítá, aby respektoval vaše technické preference při navrhování architektury.

**Načítán těmito workflow:**

- `bmad-create-architecture` — respektuje technické preference během solutioningu
- `bmad-create-story` — informuje tvorbu stories vzory projektu
- `bmad-dev-story` — vede implementační rozhodnutí
- `bmad-code-review` — validuje proti standardům projektu
- `bmad-quick-dev` — aplikuje vzory při implementaci specifikací
- `bmad-sprint-planning`, `bmad-retrospective`, `bmad-correct-course` — poskytuje celkový kontext projektu

Soubor `project-context.md` je užitečný v jakékoli fázi projektu:

ScénářKdy vytvořitÚčel**Nový projekt, před architekturou**Ručně, před `bmad-create-architecture`Dokumentujte vaše technické preference, aby je architekt respektoval**Nový projekt, po architektuře**Přes `bmad-generate-project-context` nebo ručněZachyťte architektonická rozhodnutí pro implementační agenty**Existující projekt**Přes `bmad-generate-project-context`Objevte existující vzory, aby agenti dodržovali zavedené konvence**Quick Flow projekt**Před nebo během `bmad-quick-dev`Zajistěte, aby rychlá implementace respektovala vaše vzory

Soubor má dvě hlavní sekce:

### Technologický stack a verze

[Section titled “Technologický stack a verze”](#technologick%C3%BD-stack-a-verze)

Dokumentuje frameworky, jazyky a nástroje, které váš projekt používá se specifickými verzemi:

```markdown

## Technology Stack & Versions
- Node.js 20.x, TypeScript 5.3, React 18.2
- State: Zustand (not Redux)
- Testing: Vitest, Playwright, MSW
- Styling: Tailwind CSS with custom design tokens
```

### Kritická pravidla implementace

[Section titled “Kritická pravidla implementace”](#kritick%C3%A1-pravidla-implementace)

Dokumentuje vzory a konvence, které by agenti jinak mohli přehlédnout:

```markdown

## Critical Implementation Rules
**TypeScript Configuration:**
- Strict mode enabled — no `any` types without explicit approval
- Use `interface` for public APIs, `type` for unions/intersections
**Code Organization:**
- Components in `/src/components/` with co-located `.test.tsx`
- Utilities in `/src/lib/` for reusable pure functions
- API calls use the `apiClient` singleton — never fetch directly
**Testing Patterns:**
- Unit tests focus on business logic, not implementation details
- Integration tests use MSW to mock API responses
- E2E tests cover critical user journeys only
**Framework-Specific:**
- All async operations use the `handleError` wrapper for consistent error handling
- Feature flags accessed via `featureFlag()` from `@/lib/flags`
- New routes follow the file-based routing pattern in `/src/app/`
```

Zaměřte se na to, co je **neočividné** — věci, které agenti nemusí odvodit z čtení úryvků kódu. Nedokumentujte standardní postupy, které platí univerzálně.

## Vytvoření souboru

[Section titled “Vytvoření souboru”](#vytvo%C5%99en%C3%AD-souboru)

Máte tři možnosti:

Vytvořte soubor na `_bmad-output/project-context.md` a přidejte svá pravidla:

```bash

# V kořeni projektu
mkdir-p_bmad-output
touch_bmad-output/project-context.md
```

Upravte ho s vaším technologickým stackem a pravidly implementace. Architektonický a implementační workflow ho automaticky najdou a načtou.

### Generování po architektuře

[Section titled “Generování po architektuře”](#generov%C3%A1n%C3%AD-po-architektu%C5%99e)

Spusťte workflow `bmad-generate-project-context` po dokončení architektury:

```bash

bmad-generate-project-context
```

Toto skenuje váš dokument architektury a soubory projektu a generuje kontextový soubor zachycující učiněná rozhodnutí.

### Generování pro existující projekty

[Section titled “Generování pro existující projekty”](#generov%C3%A1n%C3%AD-pro-existuj%C3%ADc%C3%AD-projekty)

Pro existující projekty spusťte `bmad-generate-project-context` pro objevení existujících vzorů:

```bash

bmad-generate-project-context
```

Workflow analyzuje vaši kódovou bázi, identifikuje konvence a vygeneruje kontextový soubor, který můžete zkontrolovat a upřesnit.

## Proč na tom záleží

[Section titled “Proč na tom záleží”](#pro%C4%8D-na-tom-z%C3%A1le%C5%BE%C3%AD)

Bez `project-context.md` agenti dělají předpoklady, které nemusí odpovídat vašemu projektu:

Bez kontextuS kontextemPoužívá generické vzoryDodržuje vaše zavedené konvenceNekonzistentní styl napříč storiesKonzistentní implementaceMůže přehlédnout omezení specifická pro projektRespektuje všechny technické požadavkyKaždý agent rozhoduje nezávisleVšichni agenti se řídí stejnými pravidly

To je zvláště důležité pro:

- **Quick Flow** — přeskakuje PRD a architekturu, takže kontextový soubor vyplní mezeru
- **Týmové projekty** — zajistí, že všichni agenti dodržují stejné standardy
- **Existující projekty** — zabrání porušení zavedených vzorů

## Editace a aktualizace

[Section titled “Editace a aktualizace”](#editace-a-aktualizace)

Soubor `project-context.md` je živý dokument. Aktualizujte ho, když:

- Se změní architektonická rozhodnutí
- Jsou zavedeny nové konvence
- Vzory se vyvíjejí během implementace
- Identifikujete mezery z chování agentů

Můžete ho kdykoli ručně upravit, nebo přegenerovat `bmad-generate-project-context` po významných změnách.