---
title: Adversariální revize
url: https://docs.bmad-method.org/cs/explanation/adversarial-review/
source: sitemap
fetched_at: 2026-04-08T11:29:04.245393684-03:00
rendered_js: false
word_count: 337
summary: This document explains adversarial review, a testing technique that forces reviewers to actively search for flaws rather than simply confirming existing work. It details how this method improves analysis depth and addresses AI-generated false positives.
tags:
    - adversarial-review
    - code-review
    - quality-assurance
    - flaw-finding
    - software-testing
    - analysis
category: guide
---

Vynuťte hlubší analýzu tím, že budete vyžadovat nalezení problémů.

## Co je adversariální revize?

[Section titled “Co je adversariální revize?”](#co-je-adversari%C3%A1ln%C3%AD-revize)

Technika revize, kde recenzent *musí* najít problémy. Žádné „vypadá dobře“ není povoleno. Recenzent zaujme cynický postoj — předpokládá, že problémy existují, a hledá je.

Nejde o negativismus. Jde o vynucení skutečné analýzy místo povrchního pohledu, který automaticky schválí cokoli, co bylo předloženo.

**Základní pravidlo:** Musíte najít problémy. Nulové nálezy spouštějí zastavení — analyzujte znovu nebo vysvětlete proč.

Běžné revize trpí konfirmačním zkreslením. Proletíte práci, nic nevyskočí, schválíte to. Mandát „najít problémy“ tento vzor rozbíjí:

- **Vynucuje důkladnost** — Nemůžete schválit, dokud jste nehledali dostatečně pečlivě
- **Zachytí chybějící věci** — „Co zde není?“ se stává přirozenou otázkou
- **Zlepšuje kvalitu signálu** — Nálezy jsou konkrétní a akční, ne vágní obavy
- **Informační asymetrie** — Provádějte revize s čerstvým kontextem (bez přístupu k původnímu uvažování), abyste hodnotili artefakt, ne záměr

Adversariální revize se objevuje v celém BMad workflow — revize kódu, kontroly připravenosti implementace, validace specifikací a další. Někdy je to povinný krok, někdy volitelný (jako pokročilá elicitace nebo party mode). Vzor se přizpůsobí jakémukoli artefaktu, který potřebuje kontrolu.

## Vyžadováno lidské filtrování

[Section titled “Vyžadováno lidské filtrování”](#vy%C5%BEadov%C3%A1no-lidsk%C3%A9-filtrov%C3%A1n%C3%AD)

Protože AI je *instruována* najít problémy, najde problémy — i když neexistují. Očekávejte falešné pozitivy: malichernosti převlečené za problémy, nepochopení záměru nebo přímo vymyšlené obavy.

**Vy rozhodujete, co je skutečné.** Zkontrolujte každý nález, odmítněte šum, opravte to, na čem záleží.

Místo:

> „Implementace autentizace vypadá rozumně. Schváleno.“

Adversariální revize produkuje:

> 1. **VYSOKÁ** — `login.ts:47` — Žádné omezení rychlosti neúspěšných pokusů
> 2. **VYSOKÁ** — Session token uložen v localStorage (zranitelný vůči XSS)
> 3. **STŘEDNÍ** — Validace hesla probíhá pouze na straně klienta
> 4. **STŘEDNÍ** — Žádné auditní logování neúspěšných pokusů o přihlášení
> 5. **NÍZKÁ** — Magické číslo `3600` by mělo být `SESSION_TIMEOUT_SECONDS`

První revize mohla přehlédnout bezpečnostní zranitelnost. Druhá zachytila čtyři.

## Iterace a klesající výnosy

[Section titled “Iterace a klesající výnosy”](#iterace-a-klesaj%C3%ADc%C3%AD-v%C3%BDnosy)

Po řešení nálezů zvažte opětovné spuštění. Druhý průchod obvykle zachytí více. Třetí také není vždy zbytečný. Ale každý průchod zabere čas a nakonec dosáhnete klesajících výnosů — jen malichernosti a falešné nálezy.