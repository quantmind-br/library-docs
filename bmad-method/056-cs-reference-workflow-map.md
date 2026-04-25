---
title: Mapa pracovních postupů
url: https://docs.bmad-method.org/cs/reference/workflow-map/
source: sitemap
fetched_at: 2026-04-08T11:29:41.487424055-03:00
rendered_js: false
word_count: 440
summary: 'This document details the BMad Method (BMM), a structured process for AI agents to develop projects by progressively building context across four distinct phases: Analysis, Planning, Solutioning, and Implementation. It outlines specific workflows and their purposes at each stage, emphasizing that every output informs the next step to maintain consistency.'
tags:
    - bmad-method
    - ai-agent
    - context-engineering
    - software-development
    - workflow-planning
    - system-architecture
category: guide
---

BMad Method (BMM) je modul v ekosystému BMad, zaměřený na dodržování osvědčených postupů context engineeringu a plánování. AI agenti fungují nejlépe s jasným, strukturovaným kontextem. Systém BMM buduje tento kontext progresivně napříč 4 odlišnými fázemi — každá fáze a volitelně více workflow v každé fázi produkují dokumenty, které informují další, takže agenti vždy vědí, co budovat a proč.

Zdůvodnění a koncepty vycházejí z agilních metodik, které byly v průmyslu úspěšně používány jako mentální framework.

Pokud si kdykoli nejste jisti, co dělat, skill `bmad-help` vám pomůže zůstat na cestě nebo vědět, co dělat dál. Vždy se můžete odkázat sem — ale `bmad-help` je plně interaktivní a mnohem rychlejší, pokud již máte nainstalovaný BMad Method. Navíc, pokud používáte různé moduly, které rozšířily BMad Method nebo přidaly další komplementární moduly — `bmad-help` se vyvíjí a zná vše, co je dostupné, aby vám dal nejlepší radu v daném okamžiku.

Důležitá poznámka: Každý workflow níže lze spustit přímo vaším nástrojem přes skill nebo načtením agenta a použitím záznamu z nabídky agenta.

[Otevřít diagram v novém panelu ↗](https://docs.bmad-method.org/workflow-map-diagram.html)

## Fáze 1: Analýza (volitelná)

[Section titled “Fáze 1: Analýza (volitelná)”](#f%C3%A1ze-1-anal%C3%BDza-voliteln%C3%A1)

Prozkoumejte problémový prostor a validujte nápady před závazkem k plánování.

WorkflowÚčelProdukuje`bmad-brainstorming`Brainstorming nápadů na projekt s řízenou facilitací brainstormingového kouče`brainstorming-report.md``bmad-domain-research`, `bmad-market-research`, `bmad-technical-research`Validace tržních, technických nebo doménových předpokladůVýzkumné nálezy`bmad-product-brief`Zachycení strategické vize — nejlepší, když je váš koncept jasný`product-brief.md``bmad-prfaq`Working Backwards — zátěžový test a zformování vašeho produktového konceptu`prfaq-{project}.md`

## Fáze 2: Plánování

[Section titled “Fáze 2: Plánování”](#f%C3%A1ze-2-pl%C3%A1nov%C3%A1n%C3%AD)

Definujte, co budovat a pro koho.

WorkflowÚčelProdukuje`bmad-create-prd`Definice požadavků (FR/NFR)`PRD.md``bmad-create-ux-design`Návrh uživatelského zážitku (když záleží na UX)`ux-spec.md`

## Fáze 3: Solutioning

[Section titled “Fáze 3: Solutioning”](#f%C3%A1ze-3-solutioning)

Rozhodněte, jak to budovat, a rozložte práci na stories.

WorkflowÚčelProdukuje`bmad-create-architecture`Explicitní technická rozhodnutí`architecture.md` s ADR`bmad-create-epics-and-stories`Rozložení požadavků na implementovatelnou práciSoubory epiců se stories`bmad-check-implementation-readiness`Kontrola brány před implementacíRozhodnutí PASS/CONCERNS/FAIL

## Fáze 4: Implementace

[Section titled “Fáze 4: Implementace”](#f%C3%A1ze-4-implementace)

Budujte to, jednu story po druhé. Brzy plná automatizace fáze 4!

WorkflowÚčelProdukuje`bmad-sprint-planning`Inicializace sledování (jednou na projekt pro sekvencování dev cyklu)`sprint-status.yaml``bmad-create-story`Příprava další story pro implementaci`story-[slug].md``bmad-dev-story`Implementace storyFungující kód + testy`bmad-code-review`Validace kvality implementaceSchváleno nebo požadovány změny`bmad-correct-course`Řešení významných změn uprostřed sprintuAktualizovaný plán nebo přesměrování`bmad-sprint-status`Sledování průběhu sprintu a stavu storiesAktualizace stavu sprintu`bmad-retrospective`Revize po dokončení epicuPoučení

## Quick Flow (paralelní cesta)

[Section titled “Quick Flow (paralelní cesta)”](#quick-flow-paraleln%C3%AD-cesta)

Přeskočte fáze 1–3 pro malou, dobře pochopenou práci.

WorkflowÚčelProdukuje`bmad-quick-dev`Sjednocený quick flow — vyjasněte záměr, plánujte, implementujte, revidujte a prezentujte`spec-*.md` + kód

Každý dokument se stává kontextem pro další fázi. PRD říká architektovi, jaká omezení záleží. Architektura říká dev agentovi, jaké vzory následovat. Soubory stories poskytují zaměřený, kompletní kontext pro implementaci. Bez této struktury agenti dělají nekonzistentní rozhodnutí.

**Jak ho vytvořit:**

- **Ručně** — Vytvořte `_bmad-output/project-context.md` s vaším technologickým stackem a pravidly implementace
- **Vygenerujte ho** — Spusťte `bmad-generate-project-context` pro automatické generování z vaší architektury nebo kódové báze

[**Zjistit více o project-context.md**](https://docs.bmad-method.org/cs/explanation/project-context/)