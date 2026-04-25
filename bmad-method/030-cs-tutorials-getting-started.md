---
title: Začínáme
url: https://docs.bmad-method.org/cs/tutorials/getting-started/
source: sitemap
fetched_at: 2026-04-08T11:29:45.242724351-03:00
rendered_js: false
word_count: 805
summary: This guide explains how to accelerate software development using AI-driven workflows managed by specialized agents. It details a multi-stage process, from initial planning and architecture design through to story implementation, utilizing tools like BMad-Help as an intelligent assistant.
tags:
    - ai-workflow
    - software-development
    - agent-system
    - project-planning
    - technical-guide
    - bmad-method
category: tutorial
---

Vytvářejte software rychleji pomocí pracovních postupů řízených AI se specializovanými agenty, kteří vás provedou plánováním, architekturou a implementací.

- Nainstalovat a inicializovat BMad Method pro nový projekt
- Používat **BMad-Help** — vašeho inteligentního průvodce, který ví, co dělat dál
- Vybrat správnou plánovací cestu pro velikost vašeho projektu
- Postupovat fázemi od požadavků k fungujícímu kódu
- Efektivně používat agenty a pracovní postupy

## Seznamte se s BMad-Help: Váš inteligentní průvodce

[Section titled “Seznamte se s BMad-Help: Váš inteligentní průvodce”](#seznamte-se-s-bmad-help-v%C3%A1%C5%A1-inteligentn%C3%AD-pr%C5%AFvodce)

**BMad-Help je nejrychlejší způsob, jak začít s BMad.** Nemusíte si pamatovat workflow nebo fáze — prostě se zeptejte a BMad-Help:

- **Prozkoumá váš projekt** a zjistí, co už bylo uděláno
- **Ukáže vaše možnosti** na základě nainstalovaných modulů
- **Doporučí, co dál** — včetně prvního povinného úkolu
- **Odpoví na otázky** jako „Mám nápad na SaaS, kde začít?“

### Jak používat BMad-Help

[Section titled “Jak používat BMad-Help”](#jak-pou%C5%BE%C3%ADvat-bmad-help)

Spusťte ho ve vašem AI IDE vyvoláním skillu:

Nebo ho spojte s otázkou pro kontextové poradenství:

```plaintext

bmad-help I have an idea for a SaaS product, I already know all the features I want. where do I get started?
```

BMad-Help odpoví s:

- Co je doporučeno pro vaši situaci
- Jaký je první povinný úkol
- Jak vypadá zbytek procesu

### Řídí i pracovní postupy

[Section titled “Řídí i pracovní postupy”](#%C5%99%C3%ADd%C3%AD-i-pracovn%C3%AD-postupy)

BMad-Help nejen odpovídá na otázky — **automaticky se spouští na konci každého workflow** a řekne vám přesně, co dělat dál. Žádné hádání, žádné prohledávání dokumentace — jen jasné pokyny k dalšímu povinnému workflow.

BMad vám pomáhá vytvářet software prostřednictvím řízených pracovních postupů se specializovanými AI agenty. Proces probíhá ve čtyřech fázích:

FázeNázevCo se děje1AnalýzaBrainstorming, průzkum, product brief nebo PRFAQ *(volitelné)*2PlánováníVytvoření požadavků (PRD nebo specifikace)3SolutioningNávrh architektury *(pouze BMad Method/Enterprise)*4ImplementaceBudování epic po epicu, story po story

[**Otevřete Mapu pracovních postupů**](https://docs.bmad-method.org/cs/reference/workflow-map/) pro prozkoumání fází, workflow a správy kontextu.

Na základě složitosti vašeho projektu nabízí BMad tři plánovací cesty:

CestaNejlepší proVytvořené dokumenty**Quick Flow**Opravy chyb, jednoduché funkce, jasný rozsah (1–15 stories)Pouze tech-spec**BMad Method**Produkty, platformy, složité funkce (10–50+ stories)PRD + architektura + UX**Enterprise**Compliance, multi-tenant systémy (30+ stories)PRD + architektura + bezpečnost + DevOps

Otevřete terminál v adresáři vašeho projektu a spusťte:

Pokud chcete nejnovější prereleaseový build místo výchozího release kanálu, použijte `npx bmad-method@next install`.

Při výzvě k výběru modulů zvolte **BMad Method**.

Instalátor vytvoří dvě složky:

- `_bmad/` — agenti, workflow, úkoly a konfigurace
- `_bmad-output/` — prozatím prázdná, ale zde se budou ukládat vaše artefakty

## Krok 1: Vytvořte svůj plán

[Section titled “Krok 1: Vytvořte svůj plán”](#krok-1-vytvo%C5%99te-sv%C5%AFj-pl%C3%A1n)

Projděte fázemi 1–3. **Pro každý workflow používejte nové chaty.**

### Fáze 1: Analýza (volitelná)

[Section titled “Fáze 1: Analýza (volitelná)”](#f%C3%A1ze-1-anal%C3%BDza-voliteln%C3%A1)

Všechny workflow v této fázi jsou volitelné:

- **brainstorming** (`bmad-brainstorming`) — Řízená ideace
- **průzkum** (`bmad-market-research` / `bmad-domain-research` / `bmad-technical-research`) — Tržní, doménový a technický průzkum
- **product-brief** (`bmad-product-brief`) — Doporučený základní dokument, když je váš koncept jasný
- **prfaq** (`bmad-prfaq`) — Working Backwards výzva pro zátěžový test a zformování vašeho produktového konceptu

### Fáze 2: Plánování (povinná)

[Section titled “Fáze 2: Plánování (povinná)”](#f%C3%A1ze-2-pl%C3%A1nov%C3%A1n%C3%AD-povinn%C3%A1)

**Pro BMad Method a Enterprise cesty:**

1. Vyvolejte **PM agenta** (`bmad-agent-pm`) v novém chatu
2. Spusťte workflow `bmad-create-prd` (`bmad-create-prd`)
3. Výstup: `PRD.md`

**Pro Quick Flow cestu:**

- Spusťte `bmad-quick-dev` — zvládne plánování i implementaci v jednom workflow, přeskočte k implementaci

### Fáze 3: Solutioning (BMad Method/Enterprise)

[Section titled “Fáze 3: Solutioning (BMad Method/Enterprise)”](#f%C3%A1ze-3-solutioning-bmad-methodenterprise)

**Vytvoření architektury**

1. Vyvolejte **Architect agenta** (`bmad-agent-architect`) v novém chatu
2. Spusťte `bmad-create-architecture` (`bmad-create-architecture`)
3. Výstup: Dokument architektury s technickými rozhodnutími

**Vytvoření epiců a stories**

1. Vyvolejte **PM agenta** (`bmad-agent-pm`) v novém chatu
2. Spusťte `bmad-create-epics-and-stories` (`bmad-create-epics-and-stories`)
3. Workflow využívá jak PRD, tak architekturu k vytvoření technicky informovaných stories

**Kontrola připravenosti k implementaci** *(vysoce doporučeno)*

1. Vyvolejte **Architect agenta** (`bmad-agent-architect`) v novém chatu
2. Spusťte `bmad-check-implementation-readiness` (`bmad-check-implementation-readiness`)
3. Validuje soudržnost všech plánovacích dokumentů

## Krok 2: Sestavte svůj projekt

[Section titled “Krok 2: Sestavte svůj projekt”](#krok-2-sestavte-sv%C5%AFj-projekt)

Jakmile je plánování dokončeno, přejděte k implementaci. **Každý workflow by měl běžet v novém chatu.**

### Inicializace plánování sprintu

[Section titled “Inicializace plánování sprintu”](#inicializace-pl%C3%A1nov%C3%A1n%C3%AD-sprintu)

Vyvolejte **Developer agenta** (`bmad-agent-dev`) a spusťte `bmad-sprint-planning` (`bmad-sprint-planning`). Tím se vytvoří `sprint-status.yaml` pro sledování všech epiců a stories.

Pro každou story opakujte tento cyklus s novými chaty:

KrokAgentWorkflowPříkazÚčel1DEV`bmad-create-story``bmad-create-story`Vytvoření story souboru z epicu2DEV`bmad-dev-story``bmad-dev-story`Implementace story3DEV`bmad-code-review``bmad-code-review`Validace kvality *(doporučeno)*

Po dokončení všech stories v epicu vyvolejte **Developer agenta** (`bmad-agent-dev`) a spusťte `bmad-retrospective` (`bmad-retrospective`).

Naučili jste se základy budování s BMad:

- Nainstalovali BMad a nakonfigurovali ho pro vaše IDE
- Inicializovali projekt s vybranou plánovací cestou
- Vytvořili plánovací dokumenty (PRD, architektura, epicy a stories)
- Pochopili cyklus vývoje pro implementaci

Váš projekt nyní obsahuje:

```text

váš-projekt/
├── _bmad/                                   # Konfigurace BMad
├── _bmad-output/
│   ├── planning-artifacts/
│   │   ├── PRD.md                           # Váš dokument požadavků
│   │   ├── architecture.md                  # Technická rozhodnutí
│   │   └── epics/                           # Soubory epiců a stories
│   ├── implementation-artifacts/
│   │   └── sprint-status.yaml               # Sledování sprintu
│   └── project-context.md                   # Pravidla implementace (volitelné)
└── ...
```

WorkflowPříkazAgentÚčel**`bmad-help`** ⭐`bmad-help`Jakýkoli**Váš inteligentní průvodce — ptejte se na cokoli!**`bmad-create-prd``bmad-create-prd`PMVytvoření dokumentu požadavků (PRD)`bmad-create-architecture``bmad-create-architecture`ArchitectVytvoření dokumentu architektury`bmad-generate-project-context``bmad-generate-project-context`AnalystVytvoření souboru kontextu projektu`bmad-create-epics-and-stories``bmad-create-epics-and-stories`PMRozklad PRD na epicy`bmad-check-implementation-readiness``bmad-check-implementation-readiness`ArchitectValidace soudržnosti plánování`bmad-sprint-planning``bmad-sprint-planning`DEVInicializace sledování sprintu`bmad-create-story``bmad-create-story`DEVVytvoření souboru story`bmad-dev-story``bmad-dev-story`DEVImplementace story`bmad-code-review``bmad-code-review`DEVRevize implementovaného kódu

**Potřebuji vždy architekturu?** Pouze pro BMad Method a Enterprise cesty. Quick Flow přeskakuje ze specifikace rovnou k implementaci.

**Mohu později změnit svůj plán?** Ano. Workflow `bmad-correct-course` (`bmad-correct-course`) řeší změny rozsahu během implementace.

**Co když chci nejdřív brainstormovat?** Vyvolejte Analyst agenta (`bmad-agent-analyst`) a spusťte `bmad-brainstorming` (`bmad-brainstorming`) před zahájením PRD.

**Musím dodržovat striktní pořadí?** Ne striktně. Jakmile se naučíte postup, můžete spouštět workflow přímo pomocí Rychlého přehledu výše.

- **Během workflow** — Agenti vás provázejí otázkami a vysvětleními
- **Komunita** — [Discord](https://discord.gg/gk8jAdXWmj) (#bmad-method-help, #report-bugs-and-issues)

Jste připraveni začít? Nainstalujte BMad, vyvolejte `bmad-help` a nechte svého inteligentního průvodce ukázat cestu.