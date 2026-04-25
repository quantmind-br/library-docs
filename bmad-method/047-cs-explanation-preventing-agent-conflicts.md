---
title: Předcházení konfliktům agentů
url: https://docs.bmad-method.org/cs/explanation/preventing-agent-conflicts/
source: sitemap
fetched_at: 2026-04-08T11:29:08.790626585-03:00
rendered_js: false
word_count: 325
summary: This document explains how establishing clear architectural standards and processes, such as using Architecture Decision Records (ADRs), prevents inconsistencies among multiple AI agents by defining shared conventions for APIs, database design, state management, and more.
tags:
    - software-architecture
    - ai-agents
    - consistency
    - adr
    - technical-standards
    - design-patterns
category: guide
---

Když více AI agentů implementuje různé části systému, mohou dělat protichůdná technická rozhodnutí. Dokumentace architektury tomu zabraňuje stanovením sdílených standardů.

## Běžné typy konfliktů

[Section titled “Běžné typy konfliktů”](#b%C4%9B%C5%BEn%C3%A9-typy-konflikt%C5%AF)

### Konflikty stylu API

[Section titled “Konflikty stylu API”](#konflikty-stylu-api)

Bez architektury:

- Agent A používá REST s `/users/{id}`
- Agent B používá GraphQL mutations
- Výsledek: Nekonzistentní vzory API, zmatení konzumenti

S architekturou:

- ADR specifikuje: „Použít GraphQL pro veškerou komunikaci klient-server“
- Všichni agenti dodržují stejný vzor

### Konflikty návrhu databáze

[Section titled “Konflikty návrhu databáze”](#konflikty-n%C3%A1vrhu-datab%C3%A1ze)

Bez architektury:

- Agent A používá snake\_case pro názvy sloupců
- Agent B používá camelCase pro názvy sloupců
- Výsledek: Nekonzistentní schéma, matoucí dotazy

S architekturou:

- Dokument standardů specifikuje konvence pojmenování
- Všichni agenti dodržují stejné vzory

### Konflikty řízení stavu

[Section titled “Konflikty řízení stavu”](#konflikty-%C5%99%C3%ADzen%C3%AD-stavu)

Bez architektury:

- Agent A používá Redux pro globální stav
- Agent B používá React Context
- Výsledek: Více přístupů k řízení stavu, složitost

S architekturou:

- ADR specifikuje přístup k řízení stavu
- Všichni agenti implementují konzistentně

## Jak architektura zabraňuje konfliktům

[Section titled “Jak architektura zabraňuje konfliktům”](#jak-architektura-zabra%C5%88uje-konflikt%C5%AFm)

### 1. Explicitní rozhodnutí skrze ADR

[Section titled “1. Explicitní rozhodnutí skrze ADR”](#1-explicitn%C3%AD-rozhodnut%C3%AD-skrze-adr)

Každé významné technologické rozhodnutí je zdokumentováno s:

- Kontext (proč toto rozhodnutí záleží)
- Zvažované možnosti (jaké alternativy existují)
- Rozhodnutí (co jsme zvolili)
- Zdůvodnění (proč jsme to zvolili)
- Důsledky (přijaté kompromisy)

### 2. Specifické pokyny pro FR/NFR

[Section titled “2. Specifické pokyny pro FR/NFR”](#2-specifick%C3%A9-pokyny-pro-frnfr)

Architektura mapuje každý funkční požadavek na technický přístup:

- FR-001: Správa uživatelů → GraphQL mutations
- FR-002: Mobilní aplikace → Optimalizované dotazy

### 3. Standardy a konvence

[Section titled “3. Standardy a konvence”](#3-standardy-a-konvence)

Explicitní dokumentace:

- Struktura adresářů
- Konvence pojmenování
- Organizace kódu
- Vzory testování

## Architektura jako sdílený kontext

[Section titled “Architektura jako sdílený kontext”](#architektura-jako-sd%C3%ADlen%C3%BD-kontext)

Představte si architekturu jako sdílený kontext, který všichni agenti čtou před implementací:

```text

PRD: "Co budovat"
↓
Architektura: "Jak to budovat"
↓
Agent A čte architekturu → implementuje Epic 1
Agent B čte architekturu → implementuje Epic 2
Agent C čte architekturu → implementuje Epic 3
↓
Výsledek: Konzistentní implementace
```

## Klíčová témata ADR

[Section titled “Klíčová témata ADR”](#kl%C3%AD%C4%8Dov%C3%A1-t%C3%A9mata-adr)

Běžná rozhodnutí, která zabraňují konfliktům:

TémaPříklad rozhodnutíStyl APIGraphQL vs REST vs gRPCDatabázePostgreSQL vs MongoDBAutentizaceJWT vs SessionsŘízení stavuRedux vs Context vs ZustandStylováníCSS Modules vs Tailwind vs Styled ComponentsTestováníJest + Playwright vs Vitest + Cypress

## Anti-vzory, kterým se vyhnout

[Section titled “Anti-vzory, kterým se vyhnout”](#anti-vzory-kter%C3%BDm-se-vyhnout)