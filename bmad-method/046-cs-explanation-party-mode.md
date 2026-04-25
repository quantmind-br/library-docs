---
title: Party Mode
url: https://docs.bmad-method.org/cs/explanation/party-mode/
source: sitemap
fetched_at: 2026-04-08T11:29:08.025587829-03:00
rendered_js: false
word_count: 305
summary: This document explains the concept of 'Party Mode' for AI agents, which allows a user to engage with a team of specialized AI personas in a single conversation space. It details how these agents interact by debating, agreeing, or disagreeing on complex topics like poor architecture review and creative brainstorming.
tags:
    - ai-agents
    - party-mode
    - team-collaboration
    - brainstorming
    - conversation-flow
category: concept
---

Všichni vaši AI agenti v jedné konverzaci.

## Co je Party Mode?

[Section titled “Co je Party Mode?”](#co-je-party-mode)

Spusťte `bmad-party-mode` a máte celý svůj AI tým v jedné místnosti — PM, Architect, Dev, UX Designer, kohokoli potřebujete. BMad Master orchestruje, vybírá relevantní agenty pro každou zprávu. Agenti odpovídají v charakteru, souhlasí, nesouhlasí a staví na nápadech ostatních.

Konverzace pokračuje tak dlouho, jak chcete. Ptejte se na doplňující otázky, oponujte odpovědím, přesměrujte diskuzi — je to skutečná výměna s vašimi agenty, dokud neskončíte.

**Ideální pro:**

- Velká rozhodnutí s kompromisy
- Brainstormingová sezení
- Post-mortemy, když se něco pokazí
- Retrospektivy a plánování sprintů

### Kritika špatné architektury

[Section titled “Kritika špatné architektury”](#kritika-%C5%A1patn%C3%A9-architektury)

**Vy:** „Dobře, týme, náš poslední sprint byl katastrofa. Autentizační služba spadla třikrát. Kdo to pokazil?“

**Architect:** „Design byl v pořádku — distribuovaná autentizace se správnými záložními řešeními. Pokud se implementace odchýlila od specifikace…“

**Dev:** „Následoval jsem architektonický dokument přesně. Specifikace nepočítala s race conditions při souběžné invalidaci relací.“

**PM:** „Oba jste přehlédli větší problém — nevalidovali jsme požadavky na správu relací v PRD. Tohle je na mně, že jsem to nezachytil.“

**TEA:** „A já to měl zachytit v integračních testech. Testovací scénáře nepokrývaly souběžnou invalidaci.“

### Kreativní brainstorming

[Section titled “Kreativní brainstorming”](#kreativn%C3%AD-brainstorming)

**Vy:** „Jak udělat onboarding magický místo nudného?“

**UX Designer:** „Začněte s progresivním odhalováním — odhalujte funkce, jak je uživatelé potřebují, ne všechny najednou v tutoriálu.“

**Storyteller:** „Co kdyby onboarding byl příběh? Každý krok odhaluje cestu postavy — uživatel JE hrdina.“

**Game Designer:** „Navazuji na to — co kdyby první ‚quest’ vlastně řešil skutečný problém uživatele? Učí se tím, že dělají něco hodnotného.“

### Technické rozhodnutí

[Section titled “Technické rozhodnutí”](#technick%C3%A9-rozhodnut%C3%AD)

**Vy:** „Monolit nebo mikroslužby pro MVP?“

**Architect:** „Začněte monolitem. Mikroslužby přidávají složitost, kterou při 1000 uživatelích nepotřebujete.“

**PM:** „Souhlasím. Čas na trh je důležitější než teoretická škálovatelnost.“

**Dev:** „Monolit s jasnými hranicemi modulů. Služby můžeme extrahovat později, pokud bude potřeba.“