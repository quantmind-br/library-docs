---
title: Jak upgradovat na v6
url: https://docs.bmad-method.org/cs/how-to/upgrade-to-v6/
source: sitemap
fetched_at: 2026-04-08T11:29:29.386736124-03:00
rendered_js: false
word_count: 272
summary: This guide details the step-by-step process for upgrading from BMad v4 to the v6 architecture, covering everything from running the installer and cleaning up old skills to migrating planning artifacts and ongoing development.
tags:
    - upgrade-guide
    - bmad-v4-to-v6
    - migration-process
    - development-workflow
    - planning-artifacts
category: guide
---

Použijte instalátor BMad pro upgrade z v4 na v6, který zahrnuje automatickou detekci starších instalací a asistenci při migraci.

- Máte nainstalovaný BMad v4 (složka `.bmad-method`)
- Chcete migrovat na novou architekturu v6
- Máte existující plánovací artefakty k zachování

### 1. Spusťte instalátor

[Section titled “1. Spusťte instalátor”](#1-spus%C5%A5te-instal%C3%A1tor)

Postupujte podle [instrukcí instalátoru](https://docs.bmad-method.org/cs/how-to/install-bmad/).

### 2. Zpracování starší instalace

[Section titled “2. Zpracování starší instalace”](#2-zpracov%C3%A1n%C3%AD-star%C5%A1%C3%AD-instalace)

Když je detekována v4, můžete:

- Nechat instalátor zálohovat a odstranit `.bmad-method`
- Ukončit a zpracovat vyčištění ručně

Pokud jste pojmenovali složku bmad method jinak, musíte ji odstranit ručně.

### 3. Vyčištění IDE skills

[Section titled “3. Vyčištění IDE skills”](#3-vy%C4%8Di%C5%A1t%C4%9Bn%C3%AD-ide-skills)

Ručně odstraňte starší v4 IDE příkazy/skills — například pokud máte Claude Code, hledejte vnořené složky začínající na bmad a odstraňte je:

- `.claude/commands/`

Nové v6 skills se instalují do:

- `.claude/skills/`

### 4. Migrace plánovacích artefaktů

[Section titled “4. Migrace plánovacích artefaktů”](#4-migrace-pl%C3%A1novac%C3%ADch-artefakt%C5%AF)

**Pokud máte plánovací dokumenty (Brief/PRD/UX/Architektura):**

Přesuňte je do `_bmad-output/planning-artifacts/` s popisnými názvy:

- Zahrňte `PRD` v názvu souboru pro PRD dokumenty
- Zahrňte `brief`, `architecture` nebo `ux-design` odpovídajícím způsobem
- Rozdělené dokumenty mohou být v pojmenovaných podsložkách

**Pokud jste uprostřed plánování:** Zvažte restart s v6 workflow. Použijte existující dokumenty jako vstupy — nové workflow s progresivním objevováním, webovým vyhledáváním a plan mode IDE produkují lepší výsledky.

### 5. Migrace probíhajícího vývoje

[Section titled “5. Migrace probíhajícího vývoje”](#5-migrace-prob%C3%ADhaj%C3%ADc%C3%ADho-v%C3%BDvoje)

Pokud máte vytvořené nebo implementované stories:

1. Dokončete instalaci v6
2. Umístěte `epics.md` nebo `epics/epic*.md` do `_bmad-output/planning-artifacts/`
3. Spusťte workflow `bmad-sprint-planning` Scrum Mastera
4. Řekněte SM, které epicy/stories jsou již dokončené

**Sjednocená struktura v6:**

```text

váš-projekt/
├── _bmad/               # Jedna instalační složka
│   ├── _config/         # Vaše přizpůsobení
│   │   └── agents/      # Soubory přizpůsobení agentů
│   ├── core/            # Univerzální základní framework
│   ├── bmm/             # Modul BMad Method
│   ├── bmb/             # BMad Builder
│   └── cis/             # Creative Intelligence Suite
└── _bmad-output/        # Výstupní složka (v4 to byla složka dokumentů)
```

Modul v4Stav v6`.bmad-2d-phaser-game-dev`Integrován do modulu BMGD`.bmad-2d-unity-game-dev`Integrován do modulu BMGD`.bmad-godot-game-dev`Integrován do modulu BMGD`.bmad-infrastructure-devops`Zastaralý — nový DevOps agent brzy`.bmad-creative-writing`Neadaptován — nový v6 modul brzy

Konceptv4v6**Core**`_bmad-core` byl vlastně BMad Method`_bmad/core/` je univerzální framework**Method**`_bmad-method``_bmad/bmm/`**Konfigurace**Přímá editace souborů`config.yaml` pro každý modul**Dokumenty**Vyžadované nastavení shardůPlně flexibilní, auto-skenování