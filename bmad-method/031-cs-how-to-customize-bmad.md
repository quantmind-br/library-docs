---
title: Jak přizpůsobit BMad
url: https://docs.bmad-method.org/cs/how-to/customize-bmad/
source: sitemap
fetched_at: 2026-04-08T11:29:13.234087658-03:00
rendered_js: false
word_count: 389
summary: This document guides users on how to customize the behavior, personality, context memory, menu options, critical actions, and reusable prompts for AI agents using `.customize.yaml` files. It details which sections override or append existing configurations and outlines the steps for applying these changes.
tags:
    - agent-customization
    - yaml-configuration
    - workflow-setup
    - llm-tuning
    - bmad-tooling
category: guide
---

Použijte soubory `.customize.yaml` k přizpůsobení chování agentů, person a nabídek při zachování vašich změn napříč aktualizacemi.

- Chcete změnit jméno, osobnost nebo komunikační styl agenta
- Potřebujete, aby si agenti pamatovali kontextově specifické informace projektu
- Chcete přidat vlastní položky nabídky, které spouštějí vaše vlastní workflow nebo prompty
- Chcete, aby agenti prováděli specifické akce při každém spuštění

### 1. Najděte soubory přizpůsobení

[Section titled “1. Najděte soubory přizpůsobení”](#1-najd%C4%9Bte-soubory-p%C5%99izp%C5%AFsoben%C3%AD)

Po instalaci najdete jeden soubor `.customize.yaml` na agenta v:

```text

_bmad/_config/agents/
├── core-bmad-master.customize.yaml
├── bmm-dev.customize.yaml
├── bmm-pm.customize.yaml
└── ... (jeden soubor na instalovaného agenta)
```

### 2. Upravte soubor přizpůsobení

[Section titled “2. Upravte soubor přizpůsobení”](#2-upravte-soubor-p%C5%99izp%C5%AFsoben%C3%AD)

Otevřete soubor `.customize.yaml` pro agenta, kterého chcete upravit. Každá sekce je volitelná — přizpůsobte pouze to, co potřebujete.

SekceChováníÚčel`agent.metadata`NahrazujePřepsat zobrazované jméno agenta`persona`NahrazujeNastavit roli, identitu, styl a principy`memories`PřidáváPřidat trvalý kontext, který si agent vždy pamatuje`menu`PřidáváPřidat vlastní položky nabídky pro workflow nebo prompty`critical_actions`PřidáváDefinovat instrukce při spuštění agenta`prompts`PřidáváVytvořit znovupoužitelné prompty pro akce nabídky

Sekce označené **Nahrazuje** zcela přepíší výchozí hodnoty agenta. Sekce označené **Přidává** doplní existující konfiguraci.

**Jméno agenta**

Změňte, jak se agent představí:

```yaml

agent:
metadata:
name: 'Spongebob'# Výchozí: "Amelia"
```

**Persona**

Nahraďte osobnost, roli a komunikační styl agenta:

```yaml

persona:
role: 'Senior Full-Stack Engineer'
identity: 'Lives in a pineapple (under the sea)'
communication_style: 'Spongebob annoying'
principles:
- 'Never Nester, Spongebob Devs hate nesting more than 2 levels deep'
- 'Favor composition over inheritance'
```

Sekce `persona` nahrazuje celou výchozí personu, takže nastavte všechna čtyři pole.

**Memories**

Přidejte trvalý kontext, který si agent bude vždy pamatovat:

```yaml

memories:
- 'Works at Krusty Krab'
- 'Favorite Celebrity: David Hasselhoff'
- 'Learned in Epic 1 that it is not cool to just pretend that tests have passed'
```

**Položky nabídky**

Přidejte vlastní záznamy do nabídky agenta. Každá položka potřebuje `trigger`, cíl (`workflow` cestu nebo `action` referenci) a `description`:

```yaml

menu:
- trigger: my-workflow
workflow: 'my-custom/workflows/my-workflow.yaml'
description: My custom workflow
- trigger: deploy
action: '#deploy-prompt'
description: Deploy to production
```

**Kritické akce**

Definujte instrukce, které se spustí při startu agenta:

```yaml

critical_actions:
- 'Check the CI Pipelines with the XYZ Skill and alert user on wake if anything is urgently needing attention'
```

**Vlastní prompty**

Vytvořte znovupoužitelné prompty, na které mohou položky nabídky odkazovat s `action="#id"`:

```yaml

prompts:
- id: deploy-prompt
content: |
Deploy the current branch to production:
1. Run all tests
2. Build the project
3. Execute deployment script
```

### 3. Aplikujte změny

[Section titled “3. Aplikujte změny”](#3-aplikujte-zm%C4%9Bny)

Po editaci přeinstalujte pro aplikaci změn:

Instalátor detekuje existující instalaci a nabídne tyto možnosti:

MožnostCo udělá**Quick Update**Aktualizuje všechny moduly na nejnovější verzi a aplikuje přizpůsobení**Modify BMad Installation**Plný instalační postup pro přidání nebo odebrání modulů

Pro změny pouze přizpůsobení je **Quick Update** nejrychlejší možnost.

**Změny se nezobrazují?**

- Spusťte `npx bmad-method install` a vyberte **Quick Update** pro aplikaci změn
- Zkontrolujte, že vaše YAML syntaxe je platná (na odsazení záleží)
- Ověřte, že jste upravili správný soubor `.customize.yaml` pro daného agenta

**Agent se nenačítá?**

- Zkontrolujte YAML syntaxi pomocí online YAML validátoru
- Ujistěte se, že jste nenechali pole prázdná po odkomentování
- Zkuste se vrátit k původní šabloně a znovu sestavit

**Potřebujete resetovat agenta?**

- Vymažte nebo smažte soubor `.customize.yaml` agenta
- Spusťte `npx bmad-method install` a vyberte **Quick Update** pro obnovení výchozích hodnot

## Přizpůsobení workflow

[Section titled “Přizpůsobení workflow”](#p%C5%99izp%C5%AFsoben%C3%AD-workflow)

Přizpůsobení existujících BMad Method workflow a skills přijde brzy.

## Přizpůsobení modulů

[Section titled “Přizpůsobení modulů”](#p%C5%99izp%C5%AFsoben%C3%AD-modul%C5%AF)

Návod na tvorbu rozšiřujících modulů a přizpůsobení existujících modulů přijde brzy.