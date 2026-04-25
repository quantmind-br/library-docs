---
title: Comment installer BMad
url: https://docs.bmad-method.org/fr/how-to/install-bmad/
source: sitemap
fetched_at: 2026-04-08T11:30:39.555864252-03:00
rendered_js: false
word_count: 355
summary: This document serves as a comprehensive guide detailing the step-by-step process of installing and configuring BMad within a project, covering module selection, AI tool integration, and post-installation verification.
tags:
    - bmad
    - installation
    - configuration
    - ai-tools
    - project-setup
    - tutorial
category: guide
---

Utilisez la commande `npx bmad-method install` pour configurer BMad dans votre projet avec votre choix de modules et d’outils d’IA.

Si vous souhaitez utiliser un installateur non interactif et fournir toutes les options d’installation en ligne de commande, consultez [ce guide](https://docs.bmad-method.org/fr/how-to/non-interactive-installation/).

- Démarrer un nouveau projet avec BMad
- Ajouter BMad à une base de code existante
- Mettre à jour une installation BMad existante

### 1. Lancer l’installateur

[Section intitulée « 1. Lancer l’installateur »](#1-lancer-linstallateur)

### 2. Choisir l’emplacement d’installation

[Section intitulée « 2. Choisir l’emplacement d’installation »](#2-choisir-lemplacement-dinstallation)

L’installateur vous demandera où installer les fichiers BMad :

- Répertoire courant (recommandé pour les nouveaux projets si vous avez créé le répertoire vous-même et l’exécutez depuis ce répertoire)
- Chemin personnalisé

### 3. Sélectionner vos outils d’IA

[Section intitulée « 3. Sélectionner vos outils d’IA »](#3-s%C3%A9lectionner-vos-outils-dia)

Choisissez les outils d’IA que vous utilisez :

- Claude Code
- Cursor
- Autres

Chaque outil a sa propre façon d’intégrer les skills. L’installateur crée de petits fichiers de prompt pour activer les workflows et les agents — il les place simplement là où votre outil s’attend à les trouver.

### 4. Choisir les modules

[Section intitulée « 4. Choisir les modules »](#4-choisir-les-modules)

L’installateur affiche les modules disponibles. Sélectionnez ceux dont vous avez besoin — la plupart des utilisateurs veulent simplement **méthode BMad** (le module de développement logiciel).

### 5. Suivre les instructions

[Section intitulée « 5. Suivre les instructions »](#5-suivre-les-instructions)

L’installateur vous guide pour le reste — paramètres, intégrations d’outils, etc.

```text

votre-projet/
├── _bmad/
│   ├── bmm/            # Vos modules sélectionnés
│   │   └── config.yaml # Paramètres du module (si vous devez les modifier)
│   ├── core/           # Module core requis
│   └── ...
├── _bmad-output/       # Artefacts générés
├── .claude/            # Skills Claude Code (si vous utilisez Claude Code)
│   └── skills/
│       ├── bmad-help/
│       ├── bmad-persona/
│       └── ...
└── .cursor/            # Skills Cursor (si vous utilisez Cursor)
└── skills/
└── ...
```

## Vérifier l’installation

[Section intitulée « Vérifier l’installation »](#v%C3%A9rifier-linstallation)

Exécutez `bmad-help` pour vérifier que tout fonctionne et voir quoi faire ensuite.

**BMad-Help est votre guide intelligent** qui va :

- Confirmer que votre installation fonctionne
- Afficher ce qui est disponible en fonction de vos modules installés
- Recommander votre première étape

Vous pouvez aussi lui poser des questions :

```plaintext

bmad-help Je viens d'installer, que dois-je faire en premier ?
bmad-help Quelles sont mes options pour un projet SaaS ?
```

## Résolution de problèmes

[Section intitulée « Résolution de problèmes »](#r%C3%A9solution-de-probl%C3%A8mes)

**L’installateur affiche une erreur** — Copiez-collez la sortie dans votre assistant IA et laissez-le résoudre le problème.

**L’installateur a fonctionné mais quelque chose ne fonctionne pas plus tard** — Votre IA a besoin du contexte BMad pour vous aider. Consultez [Comment obtenir des réponses à propos de BMad](https://docs.bmad-method.org/fr/how-to/get-answers-about-bmad/) pour savoir comment diriger votre IA vers les bonnes sources.