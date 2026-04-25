---
title: Existující projekty
url: https://docs.bmad-method.org/cs/how-to/established-projects/
source: sitemap
fetched_at: 2026-04-08T11:29:15.123209338-03:00
rendered_js: false
word_count: 455
summary: Tento návod poskytuje workflow pro efektivní zapojení se do stávajících projektů pomocí BMad metody. Pokrývá kroky od čištění starých artefaktů přes generování kontextu projektu až po udržování aktuální dokumentace a použití pomocného nástroje bmad-help.
tags:
    - bmad-method
    - existující-projekty
    - workflow
    - projektová-dokumentace
    - kontext-generování
    - kódová-báze
category: guide
---

Používejte BMad Method efektivně při práci na existujících projektech a starších kódových bázích.

Tento návod pokrývá základní workflow pro zapojení se do existujících projektů s BMad Method.

## Krok 1: Vyčistěte dokončené plánovací artefakty

[Section titled “Krok 1: Vyčistěte dokončené plánovací artefakty”](#krok-1-vy%C4%8Dist%C4%9Bte-dokon%C4%8Den%C3%A9-pl%C3%A1novac%C3%AD-artefakty)

Pokud jste dokončili všechny PRD epicy a stories procesem BMad, vyčistěte tyto soubory. Archivujte je, smažte nebo se spoléhejte na historii verzí. Nenechávejte tyto soubory v:

- `docs/`
- `_bmad-output/planning-artifacts/`
- `_bmad-output/implementation-artifacts/`

## Krok 2: Vytvořte kontext projektu

[Section titled “Krok 2: Vytvořte kontext projektu”](#krok-2-vytvo%C5%99te-kontext-projektu)

Spusťte workflow pro generování kontextu projektu:

```bash

bmad-generate-project-context
```

Toto skenuje vaši kódovou bázi a identifikuje:

- Technologický stack a verze
- Vzory organizace kódu
- Konvence pojmenování
- Přístupy k testování
- Vzory specifické pro framework

Vygenerovaný soubor můžete zkontrolovat a upravit, nebo ho vytvořit ručně na `_bmad-output/project-context.md`.

[Zjistit více o kontextu projektu](https://docs.bmad-method.org/cs/explanation/project-context/)

## Krok 3: Udržujte kvalitní projektovou dokumentaci

[Section titled “Krok 3: Udržujte kvalitní projektovou dokumentaci”](#krok-3-udr%C5%BEujte-kvalitn%C3%AD-projektovou-dokumentaci)

Vaše složka `docs/` by měla obsahovat stručnou, dobře organizovanou dokumentaci, která přesně reprezentuje váš projekt:

- Záměr a obchodní zdůvodnění
- Obchodní pravidla
- Architektura
- Jakékoli další relevantní informace o projektu

Pro složité projekty zvažte použití workflow `bmad-document-project`. Nabízí varianty, které proskenují celý váš projekt a zdokumentují jeho aktuální stav.

## Krok 3: Získejte pomoc

[Section titled “Krok 3: Získejte pomoc”](#krok-3-z%C3%ADskejte-pomoc)

### BMad-Help: Váš výchozí bod

[Section titled “BMad-Help: Váš výchozí bod”](#bmad-help-v%C3%A1%C5%A1-v%C3%BDchoz%C3%AD-bod)

**Spusťte `bmad-help` kdykoli si nejste jisti, co dělat dál.** Tento inteligentní průvodce:

- Prozkoumá váš projekt a zjistí, co už bylo uděláno
- Ukáže možnosti na základě nainstalovaných modulů
- Rozumí dotazům v přirozeném jazyce

```plaintext

bmad-help I have an existing Rails app, where should I start?
bmad-help What's the difference between quick-flow and full method?
bmad-help Show me what workflows are available
```

BMad-Help se také **automaticky spouští na konci každého workflow** a poskytuje jasné pokyny, co přesně dělat dál.

Máte dvě hlavní možnosti v závislosti na rozsahu změn:

RozsahDoporučený přístup**Malé aktualizace či doplnění**Spusťte `bmad-quick-dev` pro vyjasnění záměru, plánování, implementaci a revizi v jednom workflow. Plná čtyřfázová metoda BMad je pravděpodobně přehnaná.**Velké změny či doplnění**Začněte s metodou BMad a aplikujte tolik nebo tak málo důkladnosti, kolik potřebujete.

Při vytváření briefu nebo přímém přechodu na PRD zajistěte, aby agent:

- Našel a analyzoval vaši existující projektovou dokumentaci
- Přečetl si správný kontext o vašem aktuálním systému

Agenta můžete navést explicitně, ale cílem je zajistit, aby se nová funkce dobře integrovala s vaším existujícím systémem.

Práce na UX je volitelná. Rozhodnutí nezávisí na tom, zda váš projekt má UX, ale na:

- Zda budete pracovat na změnách UX
- Zda jsou potřeba významné nové UX návrhy nebo vzory

Pokud vaše změny představují jednoduché aktualizace existujících obrazovek, se kterými jste spokojeni, plný UX proces je zbytečný.

### Úvahy o architektuře

[Section titled “Úvahy o architektuře”](#%C3%BAvahy-o-architektu%C5%99e)

Při práci na architektuře zajistěte, aby architekt:

- Používal správné zdokumentované soubory
- Skenoval existující kódovou bázi

Věnujte zde zvláštní pozornost, abyste předešli znovuvynalézání kola nebo rozhodnutím, která neodpovídají vaší existující architektuře.

- [**Rychlé opravy**](https://docs.bmad-method.org/cs/how-to/quick-fixes/) — Opravy chyb a ad-hoc změny
- [**FAQ pro existující projekty**](https://docs.bmad-method.org/cs/explanation/established-projects-faq/) — Časté otázky o práci na existujících projektech