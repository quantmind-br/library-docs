---
title: Jak získat odpovědi o BMad
url: https://docs.bmad-method.org/cs/how-to/get-answers-about-bmad/
source: sitemap
fetched_at: 2026-04-08T11:29:17.931669197-03:00
rendered_js: false
word_count: 380
summary: This guide explains how to effectively use the BMad-Help feature, an intelligent assistant that answers most questions about BMad directly within the IDE. It also details when and how to consult deeper resources like the local repository or documentation files for more context.
tags:
    - bmad
    - help-guide
    - ai-assistant
    - workflow
    - ide-integration
    - documentation
category: tutorial
---

## Začněte zde: BMad-Help

[Section titled “Začněte zde: BMad-Help”](#za%C4%8Dn%C4%9Bte-zde-bmad-help)

**Nejrychlejší způsob, jak získat odpovědi o BMad, je skill `bmad-help`.** Tento inteligentní průvodce zodpoví více než 80 % všech otázek a je vám k dispozici přímo ve vašem IDE při práci.

BMad-Help je víc než vyhledávací nástroj — umí:

- **Prozkoumat váš projekt** a zjistit, co už bylo dokončeno
- **Rozumět přirozenému jazyku** — ptejte se běžnou řečí
- **Přizpůsobit se nainstalovaným modulům** — zobrazí relevantní možnosti
- **Automaticky se spouštět po workflow** — řekne vám přesně, co dělat dál
- **Doporučit první povinný úkol** — žádné hádání, kde začít

### Jak používat BMad-Help

[Section titled “Jak používat BMad-Help”](#jak-pou%C5%BE%C3%ADvat-bmad-help)

Zavolejte ho jménem ve vaší AI relaci:

Spojte ho s dotazem v přirozeném jazyce:

```plaintext

bmad-help I have a SaaS idea and know all the features. Where do I start?
bmad-help What are my options for UX design?
bmad-help I'm stuck on the PRD workflow
bmad-help Show me what's been done so far
```

BMad-Help odpoví:

- Co je doporučeno pro vaši situaci
- Jaký je první povinný úkol
- Jak vypadá zbytek procesu

## Kdy použít tohoto průvodce

[Section titled “Kdy použít tohoto průvodce”](#kdy-pou%C5%BE%C3%ADt-tohoto-pr%C5%AFvodce)

Použijte tuto sekci, když:

- Chcete pochopit architekturu nebo interní fungování BMad
- Potřebujete odpovědi mimo to, co BMad-Help nabízí
- Zkoumáte BMad před instalací
- Chcete prozkoumat zdrojový kód přímo

### 1. Vyberte si zdroj

[Section titled “1. Vyberte si zdroj”](#1-vyberte-si-zdroj)

ZdrojNejlepší proPříklady**Složka `_bmad`**Jak BMad funguje — agenti, workflow, prompty„Co dělá PM agent?“**Celý GitHub repo**Historie, instalátor, architektura„Co se změnilo ve v6?“**`llms-full.txt`**Rychlý přehled z dokumentace„Vysvětli čtyři fáze BMad“

Složka `_bmad` se vytvoří při instalaci BMad. Pokud ji ještě nemáte, naklonujte si repo.

### 2. Nasměrujte AI na zdroj

[Section titled “2. Nasměrujte AI na zdroj”](#2-nasm%C4%9Brujte-ai-na-zdroj)

**Pokud vaše AI umí číst soubory (Claude Code, Cursor atd.):**

- **BMad nainstalován:** Nasměrujte na složku `_bmad` a ptejte se přímo
- **Chcete hlubší kontext:** Naklonujte si [celé repo](https://github.com/bmad-code-org/BMAD-METHOD)

**Pokud používáte ChatGPT nebo Claude.ai:**

Načtěte `llms-full.txt` do vaší relace:

```text

https://bmad-code-org.github.io/BMAD-METHOD/llms-full.txt
```

### 3. Položte svou otázku

[Section titled “3. Položte svou otázku”](#3-polo%C5%BEte-svou-ot%C3%A1zku)

Přímé odpovědi o BMad — jak agenti fungují, co dělají workflow, proč jsou věci strukturované tak, jak jsou — bez čekání na odpověď od někoho jiného.

- **Ověřte překvapivé odpovědi** — LLM se občas mýlí. Zkontrolujte zdrojový soubor nebo se zeptejte na Discordu.
- **Buďte konkrétní** — „Co dělá krok 3 PRD workflow?“ je lepší než „Jak funguje PRD?“

## Stále jste uvízli?

[Section titled “Stále jste uvízli?”](#st%C3%A1le-jste-uv%C3%ADzli)

Zkusili jste přístup přes LLM a stále potřebujete pomoc? Nyní máte mnohem lepší otázku k položení.

KanálPoužijte pro`#bmad-method-help`Rychlé otázky (chat v reálném čase)`help-requests` fórumDetailní otázky (vyhledatelné, trvalé)`#suggestions-feedback`Nápady a požadavky na funkce`#report-bugs-and-issues`Hlášení chyb

**Discord:** [discord.gg/gk8jAdXWmj](https://discord.gg/gk8jAdXWmj)

**GitHub Issues:** [github.com/bmad-code-org/BMAD-METHOD/issues](https://github.com/bmad-code-org/BMAD-METHOD/issues) (pro jasné chyby)