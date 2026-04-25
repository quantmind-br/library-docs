---
title: Comment passer à la v6
url: https://docs.bmad-method.org/fr/how-to/upgrade-to-v6/
source: sitemap
fetched_at: 2026-04-08T11:30:49.17701752-03:00
rendered_js: false
word_count: 503
summary: Ce guide explique la procédure détaillée pour migrer depuis BMad version 4 vers la version 6 en utilisant l'installateur dédié, incluant les étapes de gestion des installations existantes, le nettoyage des compétences IDE, et la migration structurée des artefacts de planification et du développement en cours.
tags:
    - migration-bmad
    - v4-to-v6
    - gestion-projet
    - artefacts-planification
    - développement-assisté
category: guide
---

Utilisez l’installateur BMad pour passer de la v4 à la v6, qui inclut une détection automatique des installations existantes et une assistance à la migration.

## Quand utiliser ce guide

[Section intitulée « Quand utiliser ce guide »](#quand-utiliser-ce-guide)

- Vous avez BMad v4 installé (dossier `.bmad-method`)
- Vous souhaitez migrer vers la nouvelle architecture v6
- Vous avez des artefacts de planification existants à préserver

### 1. Lancer l’installateur

[Section intitulée « 1. Lancer l’installateur »](#1-lancer-linstallateur)

Suivez les [Instructions d’installation](https://docs.bmad-method.org/fr/how-to/install-bmad/).

### 2. Gérer l’installation existante

[Section intitulée « 2. Gérer l’installation existante »](#2-g%C3%A9rer-linstallation-existante)

Quand v4 est détecté, vous pouvez :

- Autoriser l’installateur à sauvegarder et supprimer `.bmad-method`
- Quitter et gérer le nettoyage manuellement

Si vous avez nommé votre dossier de méthode bmad autrement, vous devrez supprimer le dossier vous-même manuellement.

### 3. Nettoyer les skills IDE

[Section intitulée « 3. Nettoyer les skills IDE »](#3-nettoyer-les-skills-ide)

Supprimez manuellement les commandes/skills IDE v4 existants - par exemple si vous avez Claude Code, recherchez tous les dossiers imbriqués qui commencent par bmad et supprimez-les :

- `.claude/commands/`

Les nouveaux skills v6 sont installés dans :

- `.claude/skills/`

### 4. Migrer les artefacts de planification

[Section intitulée « 4. Migrer les artefacts de planification »](#4-migrer-les-artefacts-de-planification)

**Si vous avez des documents de planification (Brief/PRD/UX/Architecture) :**

Déplacez-les dans `_bmad-output/planning-artifacts/` avec des noms descriptifs :

- Incluez `PRD` dans le nom de fichier pour les documents PRD[1](#user-content-fn-1)
- Incluez `brief`, `architecture`, ou `ux-design` selon le cas
- Les documents divisés peuvent être dans des sous-dossiers nommés

**Si vous êtes en cours de planification :** Envisagez de redémarrer avec les workflows v6. Utilisez vos documents existants comme entrées - les nouveaux workflows de découverte progressive avec recherche web et mode plan IDE produisent de meilleurs résultats.

### 5. Migrer le développement en cours

[Section intitulée « 5. Migrer le développement en cours »](#5-migrer-le-d%C3%A9veloppement-en-cours)

Si vous avez des stories[2](#user-content-fn-3) créées ou implémentées :

1. Terminez l’installation v6
2. Placez `epics.md` ou `epics/epic*.md`[3](#user-content-fn-2) dans `_bmad-output/planning-artifacts/`
3. Lancez le workflow `bmad-sprint-planning`[4](#user-content-fn-4)
4. Indiquez quels epics/stories sont déjà terminés

**Structure unifiée v6 :**

```text

votre-projet/
├── _bmad/               # Dossier d'installation unique
│   ├── _config/         # Vos personnalisations
│   │   └── agents/      # Fichiers de personnalisation des agents
│   ├── core/            # Framework core universel
│   ├── bmm/             # Module BMad Method
│   ├── bmb/             # BMad Builder
│   └── cis/             # Creative Intelligence Suite
└── _bmad-output/        # Dossier de sortie (était le dossier doc en v4)
```

Module v4Statut v6`.bmad-2d-phaser-game-dev`Intégré dans le Module BMGD`.bmad-2d-unity-game-dev`Intégré dans le Module BMGD`.bmad-godot-game-dev`Intégré dans le Module BMGD`.bmad-infrastructure-devops`Déprécié - nouvel agent DevOps bientôt disponible`.bmad-creative-writing`Non adapté - nouveau module v6 bientôt disponible

Conceptv4v6**Core**`_bmad-core` était en fait la méthode BMad`_bmad/core/` est le framework universel**Method**`_bmad-method``_bmad/bmm/`**Config**Fichiers modifiés directement`config.yaml` par module**Documents**Division ou non division requiseEntièrement flexible, scan automatique

1. PRD (Product Requirements Document) : document de référence qui décrit les objectifs du produit, les besoins utilisateurs, les fonctionnalités attendues, les contraintes et les critères de succès, afin d’aligner les équipes sur ce qui doit être construit et pourquoi. [↩](#user-content-fnref-1)
2. Story (User Story) : une description courte et simple d’une fonctionnalité du point de vue de l’utilisateur. Les stories sont des unités de travail suffisamment petites pour être complétées en un sprint. [↩](#user-content-fnref-3)
3. Epic : dans les méthodologies agiles, une grande unité de travail qui peut être décomposée en plusieurs stories. Un epic représente généralement une fonctionnalité majeure ou un ensemble de capacités livrable sur plusieurs sprints. [↩](#user-content-fnref-2)
4. Sprint : dans Scrum, une période de temps fixe (généralement 1 à 4 semaines) pendant laquelle l’équipe travaille à livrer un incrément de produit potentiellement libérable. [↩](#user-content-fnref-4)