---
title: Proč je solutioning důležitý
url: https://docs.bmad-method.org/cs/explanation/why-solutioning-matters/
source: sitemap
fetched_at: 2026-04-08T11:29:11.331320044-03:00
rendered_js: false
word_count: 193
summary: This document explains the 'Solutioning' phase, which transitions from defining what to build (planning) to deciding how it should be built by documenting architectural decisions. This process prevents technical conflicts among development agents working on large projects.
tags:
    - solutioning-phase
    - architectural-design
    - technical-decisions
    - project-workflow
    - development-coordination
category: concept
---

Fáze 3 (Solutioning) překládá **co** budovat (z plánování) na **jak** to budovat (technický návrh). Tato fáze zabraňuje konfliktům agentů v projektech s více epicy tím, že dokumentuje architektonická rozhodnutí před zahájením implementace.

## Problém bez solutioningu

[Section titled “Problém bez solutioningu”](#probl%C3%A9m-bez-solutioningu)

```text

Agent 1 implementuje Epic 1 pomocí REST API
Agent 2 implementuje Epic 2 pomocí GraphQL
Výsledek: Nekonzistentní design API, integrační noční můra
```

Když více agentů implementuje různé části systému bez sdíleného architektonického vedení, dělají nezávislá technická rozhodnutí, která si mohou odporovat.

## Řešení se solutioningem

[Section titled “Řešení se solutioningem”](#%C5%99e%C5%A1en%C3%AD-se-solutioningem)

```text

Architektonický workflow rozhodne: "Použít GraphQL pro všechna API"
Všichni agenti dodržují architektonická rozhodnutí
Výsledek: Konzistentní implementace, žádné konflikty
```

Explicitní dokumentací technických rozhodnutí všichni agenti implementují konzistentně a integrace se stává přímočarou.

## Solutioning vs. plánování

[Section titled “Solutioning vs. plánování”](#solutioning-vs-pl%C3%A1nov%C3%A1n%C3%AD)

AspektPlánování (Fáze 2)Solutioning (Fáze 3)OtázkaCo a proč?Jak? Pak jaké jednotky práce?VýstupFR/NFR (požadavky)Architektura + epicy/storiesAgentPMArchitect → PMPublikumZainteresované stranyVývojářiDokumentPRD (FR/NFR)Architektura + soubory epicůÚroveňObchodní logikaTechnický design + rozklad práce

**Učiňte technická rozhodnutí explicitní a zdokumentovaná**, aby všichni agenti implementovali konzistentně.

Toto zabraňuje:

- Konfliktům stylu API (REST vs GraphQL)
- Nekonzistencím v návrhu databáze
- Neshodám v řízení stavu
- Nesouladu konvencí pojmenování
- Variacím v bezpečnostním přístupu

## Kdy je solutioning vyžadován

[Section titled “Kdy je solutioning vyžadován”](#kdy-je-solutioning-vy%C5%BEadov%C3%A1n)

CestaSolutioning vyžadován?Quick FlowNe — přeskočte úplněBMad Method SimpleVolitelnýBMad Method ComplexAnoEnterpriseAno

Přeskočení solutioningu u složitých projektů vede k:

- **Integračním problémům** objeveným uprostřed sprintu
- **Přepracování** kvůli konfliktním implementacím
- **Delšímu celkovému času vývoje**
- **Technickému dluhu** z nekonzistentních vzorů