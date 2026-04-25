---
title: Agenti
url: https://docs.bmad-method.org/cs/reference/agents/
source: sitemap
fetched_at: 2026-04-08T11:29:31.316009952-03:00
rendered_js: false
word_count: 287
summary: This document details the built-in BMM (Agile suite) agents available through the BMad Method, outlining each agent's skill ID, primary workflow, and trigger codes. It also distinguishes between workflow triggers that use structured input and conversational triggers that require descriptive arguments.
tags:
    - bmm-agents
    - agile-suite
    - skill-ids
    - workflow-triggers
    - developer-tools
    - project-management
category: reference
---

Tato stránka uvádí výchozí BMM (Agile suite) agenty, kteří se instalují s BMad Method, společně s jejich skill ID, spouštěči nabídky a primárními workflow. Každý agent se vyvolává jako skill.

- Každý agent je dostupný jako skill, generovaný instalátorem. Skill ID (např. `bmad-dev`) se používá k vyvolání agenta.
- Spouštěče jsou krátké kódy nabídky (např. `CP`) a fuzzy shody zobrazené v nabídce každého agenta.
- Generování QA testů zajišťuje workflow skill `bmad-qa-generate-e2e-tests`, dostupný přes Developer agenta. Plný Test Architect (TEA) žije ve vlastním modulu.

AgentSkill IDSpouštěčePrimární workflowAnalyst (Mary)`bmad-analyst``BP`, `RS`, `CB`, `WB`, `DP`Brainstorm projektu, výzkum, tvorba briefu, PRFAQ výzva, dokumentace projektuProduct Manager (John)`bmad-pm``CP`, `VP`, `EP`, `CE`, `IR`, `CC`Tvorba/validace/editace PRD, tvorba epiců a stories, připravenost implementace, korekce kurzuArchitect (Winston)`bmad-architect``CA`, `IR`Tvorba architektury, připravenost implementaceDeveloper (Amelia)`bmad-agent-dev``DS`, `QD`, `QA`, `CR`, `SP`, `CS`, `ER`Dev story, Quick Dev, generování QA testů, revize kódu, plánování sprintu, tvorba story, retrospektiva epicuUX Designer (Sally)`bmad-ux-designer``CU`Tvorba UX designuTechnical Writer (Paige)`bmad-tech-writer``DP`, `WD`, `US`, `MG`, `VD`, `EC`Dokumentace projektu, psaní dokumentu, aktualizace standardů, generování Mermaid, validace dok., vysvětlení konceptu

Spouštěče nabídky agentů používají dva různé typy vyvolání. Znalost typu spouštěče vám pomůže poskytnout správný vstup.

### Workflow spouštěče (bez argumentů)

[Section titled “Workflow spouštěče (bez argumentů)”](#workflow-spou%C5%A1t%C4%9B%C4%8De-bez-argument%C5%AF)

Většina spouštěčů načítá strukturovaný soubor workflow. Zadejte kód spouštěče a agent zahájí workflow a vyzve vás k zadání vstupu v každém kroku.

Příklady: `CP` (tvorba PRD), `DS` (Dev story), `CA` (tvorba architektury), `QD` (Quick Dev)

### Konverzační spouštěče (vyžadují argumenty)

[Section titled “Konverzační spouštěče (vyžadují argumenty)”](#konverza%C4%8Dn%C3%AD-spou%C5%A1t%C4%9B%C4%8De-vy%C5%BEaduj%C3%AD-argumenty)

Některé spouštěče zahajují volnou konverzaci místo strukturovaného workflow. Tyto očekávají, že popíšete, co potřebujete, společně s kódem spouštěče.

AgentSpouštěčCo poskytnoutTechnical Writer (Paige)`WD`Popis dokumentu k napsáníTechnical Writer (Paige)`US`Preference nebo konvence k přidání do standardůTechnical Writer (Paige)`MG`Popis diagramu a typ (sekvence, vývojový diagram atd.)Technical Writer (Paige)`VD`Dokument k validaci a oblasti zaměřeníTechnical Writer (Paige)`EC`Název konceptu k vysvětlení

**Příklad:**

```text

WD Write a deployment guide for our Docker setup
MG Create a sequence diagram showing the auth flow
EC Explain how the module system works
```