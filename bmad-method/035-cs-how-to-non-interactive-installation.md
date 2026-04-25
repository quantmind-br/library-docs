---
title: Neinteraktivní instalace
url: https://docs.bmad-method.org/cs/how-to/non-interactive-installation/
source: sitemap
fetched_at: 2026-04-08T11:29:21.30282088-03:00
rendered_js: false
word_count: 397
summary: This document serves as a comprehensive guide detailing how to perform non-interactive installations and updates for BMad using command-line arguments. It outlines available parameters, configuration options, and provides examples for CI/CD pipelines and quick updates.
tags:
    - cli-arguments
    - installation-guide
    - bmad-setup
    - ci-cd
    - module-management
    - automation
category: guide
---

Použijte příznaky příkazové řádky k neinteraktivní instalaci BMad. To je užitečné pro:

- Automatizovaná nasazení a CI/CD pipelines
- Skriptované instalace
- Hromadné instalace napříč více projekty
- Rychlé instalace se známými konfiguracemi

## Dostupné příznaky

[Section titled “Dostupné příznaky”](#dostupn%C3%A9-p%C5%99%C3%ADznaky)

### Možnosti instalace

[Section titled “Možnosti instalace”](#mo%C5%BEnosti-instalace)

PříznakPopisPříklad`--directory <cesta>`Instalační adresář`--directory ~/projects/myapp``--modules <moduly>`Čárkou oddělená ID modulů`--modules bmm,bmb``--tools <nástroje>`Čárkou oddělená ID nástrojů/IDE (použijte `none` pro přeskočení)`--tools claude-code,cursor` nebo `--tools none``--action <typ>`Akce pro existující instalace: `install` (výchozí), `update` nebo `quick-update``--action quick-update`

### Základní konfigurace

[Section titled “Základní konfigurace”](#z%C3%A1kladn%C3%AD-konfigurace)

PříznakPopisVýchozí`--user-name <jméno>`Jméno, které agenti použijíSystémové uživatelské jméno`--communication-language <jazyk>`Jazyk komunikace agentůEnglish`--document-output-language <jazyk>`Jazyk výstupních dokumentůEnglish`--output-folder <cesta>`Cesta k výstupní složce\_bmad-output

PříznakPopis`-y, --yes`Přijmout všechna výchozí nastavení a přeskočit výzvy`-d, --debug`Povolit ladící výstup pro generování manifestu

Dostupná ID modulů pro příznak `--modules`:

- `bmm` — BMad Method Master
- `bmb` — BMad Builder

Zkontrolujte [registr BMad](https://github.com/bmad-code-org) pro dostupné externí moduly.

Dostupná ID nástrojů pro příznak `--tools`:

**Preferované:** `claude-code`, `cursor`

Spusťte `npx bmad-method install` interaktivně jednou pro zobrazení aktuálního seznamu podporovaných nástrojů, nebo zkontrolujte [konfiguraci kódů platforem](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/tools/cli/installers/lib/ide/platform-codes.yaml).

RežimPopisPříkladPlně neinteraktivníZadejte všechny příznaky pro přeskočení výzev`npx bmad-method install --directory . --modules bmm --tools claude-code --yes`Polo-interaktivníZadejte některé příznaky; BMad se zeptá na zbytek`npx bmad-method install --directory . --modules bmm`Pouze výchozíPřijměte vše výchozí s `-y``npx bmad-method install --yes`Bez nástrojůPřeskočte konfiguraci nástrojů/IDE`npx bmad-method install --modules bmm --tools none`

### Instalace v CI/CD pipeline

[Section titled “Instalace v CI/CD pipeline”](#instalace-v-cicd-pipeline)

```bash

#!/bin/bash
npxbmad-methodinstall\
--directory"${GITHUB_WORKSPACE}"\
--modulesbmm\
--toolsclaude-code\
--user-name"CI Bot"\
--communication-languageEnglish\
--document-output-languageEnglish\
--output-folder_bmad-output\
--yes
```

### Aktualizace existující instalace

[Section titled “Aktualizace existující instalace”](#aktualizace-existuj%C3%ADc%C3%AD-instalace)

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionupdate\
--modulesbmm,bmb,custom-module
```

### Rychlá aktualizace (zachování nastavení)

[Section titled “Rychlá aktualizace (zachování nastavení)”](#rychl%C3%A1-aktualizace-zachov%C3%A1n%C3%AD-nastaven%C3%AD)

```bash

npxbmad-methodinstall\
--directory~/projects/myapp\
--actionquick-update
```

- Plně nakonfigurovaný adresář `_bmad/` ve vašem projektu
- Agenty a workflow nakonfigurované pro vybrané moduly a nástroje
- Složku `_bmad-output/` pro generované artefakty

## Validace a zpracování chyb

[Section titled “Validace a zpracování chyb”](#validace-a-zpracov%C3%A1n%C3%AD-chyb)

BMad validuje všechny zadané příznaky:

- **Adresář** — Musí být platná cesta s oprávněním k zápisu
- **Moduly** — Upozorní na neplatná ID modulů (ale nespadne)
- **Nástroje** — Upozorní na neplatná ID nástrojů (ale nespadne)
- **Vlastní obsah** — Každá cesta musí obsahovat platný soubor `module.yaml`
- **Akce** — Musí být jedna z: `install`, `update`, `quick-update`

Neplatné hodnoty buď:

1. Zobrazí chybu a ukončí se (pro kritické možnosti jako adresář)
2. Zobrazí varování a přeskočí (pro volitelné položky jako vlastní obsah)
3. Přepnou na interaktivní výzvy (pro chybějící povinné hodnoty)

### Instalace selže s „Invalid directory“

[Section titled “Instalace selže s „Invalid directory“”](#instalace-sel%C5%BEe-s-invalid-directory)

- Cesta k adresáři musí existovat (nebo musí existovat jeho nadřazený adresář)
- Potřebujete oprávnění k zápisu
- Cesta musí být absolutní nebo správně relativní k aktuálnímu adresáři

<!--THE END-->

- Ověřte, že ID modulu je správné
- Externí moduly musí být dostupné v registru