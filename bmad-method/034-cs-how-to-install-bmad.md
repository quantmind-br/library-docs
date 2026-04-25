---
title: Jak nainstalovat BMad
url: https://docs.bmad-method.org/cs/how-to/install-bmad/
source: sitemap
fetched_at: 2026-04-08T11:29:19.401124394-03:00
rendered_js: false
word_count: 263
summary: This document provides a comprehensive guide on how to install and set up the BMad environment for a project, covering module selection, integrating various AI tools like Claude Code and Cursor, and verifying the successful installation using the bmad-help command.
tags:
    - bmad-installation
    - ai-tools
    - project-setup
    - command-line
    - developer-guide
category: tutorial
---

Použijte příkaz `npx bmad-method install` k nastavení BMad ve vašem projektu s výběrem modulů a AI nástrojů.

Pokud chcete použít neinteraktivní instalátor a zadat všechny možnosti na příkazové řádce, podívejte se na [tento návod](https://docs.bmad-method.org/cs/how-to/non-interactive-installation/).

- Začínáte nový projekt s BMad
- Přidáváte BMad do existující kódové báze
- Aktualizujete stávající instalaci BMad

### 1. Spusťte instalátor

[Section titled “1. Spusťte instalátor”](#1-spus%C5%A5te-instal%C3%A1tor)

### 2. Zvolte umístění instalace

[Section titled “2. Zvolte umístění instalace”](#2-zvolte-um%C3%ADst%C4%9Bn%C3%AD-instalace)

Instalátor se zeptá, kam nainstalovat soubory BMad:

- Aktuální adresář (doporučeno pro nové projekty, pokud jste adresář vytvořili sami a spouštíte z něj)
- Vlastní cesta

### 3. Vyberte své AI nástroje

[Section titled “3. Vyberte své AI nástroje”](#3-vyberte-sv%C3%A9-ai-n%C3%A1stroje)

Vyberte, které AI nástroje používáte:

- Claude Code
- Cursor
- Ostatní

Každý nástroj má svůj vlastní způsob integrace skills. Instalátor vytvoří drobné prompt soubory pro aktivaci workflow a agentů — jednoduše je umístí tam, kde je váš nástroj očekává.

Instalátor zobrazí dostupné moduly. Vyberte ty, které potřebujete — většina uživatelů chce pouze **BMad Method** (modul pro vývoj softwaru).

### 5. Následujte výzvy

[Section titled “5. Následujte výzvy”](#5-n%C3%A1sledujte-v%C3%BDzvy)

Instalátor vás provede zbytkem — vlastní obsah, nastavení atd.

```text

váš-projekt/
├── _bmad/
│   ├── bmm/            # Vaše vybrané moduly
│   │   └── config.yaml # Nastavení modulu (pokud byste ho někdy potřebovali změnit)
│   ├── core/           # Povinný základní modul
│   └── ...
├── _bmad-output/       # Generované artefakty
├── .claude/            # Claude Code skills (pokud používáte Claude Code)
│   └── skills/
│       ├── bmad-help/
│       ├── bmad-persona/
│       └── ...
└── .cursor/            # Cursor skills (pokud používáte Cursor)
└── skills/
└── ...
```

## Ověření instalace

[Section titled “Ověření instalace”](#ov%C4%9B%C5%99en%C3%AD-instalace)

Spusťte `bmad-help` pro ověření, že vše funguje, a zjistěte, co dělat dál.

**BMad-Help je váš inteligentní průvodce**, který:

- Potvrdí, že vaše instalace funguje
- Ukáže, co je dostupné na základě nainstalovaných modulů
- Doporučí váš první krok

Můžete mu také klást otázky:

```plaintext

bmad-help I just installed, what should I do first?
bmad-help What are my options for a SaaS project?
```

**Instalátor vyhodí chybu** — Zkopírujte výstup do svého AI asistenta a nechte ho to vyřešit.

**Instalátor fungoval, ale něco nefunguje později** — Vaše AI potřebuje kontext BMad, aby pomohla. Podívejte se na [Jak získat odpovědi o BMad](https://docs.bmad-method.org/cs/how-to/get-answers-about-bmad/) pro návod, jak nasměrovat AI na správné zdroje.