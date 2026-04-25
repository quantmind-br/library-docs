---
title: Premiers pas
url: https://docs.bmad-method.org/fr/tutorials/getting-started/
source: sitemap
fetched_at: 2026-04-08T11:31:05.668808532-03:00
rendered_js: false
word_count: 1177
summary: This document provides a comprehensive tutorial on using the BMad system, an AI-powered workflow methodology designed to help developers build software faster by guiding them through planning, architecture design, and actual implementation phases.
tags:
    - ai-workflow
    - software-development
    - bmad-method
    - project-planning
    - coding-guide
    - developer-toolkit
category: tutorial
---

Construisez des logiciels plus rapidement en utilisant des workflows propulsés par l’IA avec des agents spécialisés qui vous guident à travers la planification, l’architecture et l’implémentation.

## Ce que vous allez apprendre

[Section intitulée « Ce que vous allez apprendre »](#ce-que-vous-allez-apprendre)

- Installer et initialiser la méthode BMad pour un nouveau projet
- Utiliser **BMad-Help** — votre guide intelligent qui sait quoi faire ensuite
- Choisir la bonne voie de planification selon la taille de votre projet
- Progresser à travers les phases, des exigences au code fonctionnel
- Utiliser efficacement les agents et les workflows

## Découvrez BMad-Help : votre guide intelligent

[Section intitulée « Découvrez BMad-Help : votre guide intelligent »](#d%C3%A9couvrez-bmad-help--votre-guide-intelligent)

**BMad-Help est le moyen le plus rapide de démarrer avec BMad.** Vous n’avez pas besoin de mémoriser les workflows ou les phases — posez simplement la question, et BMad-Help va :

- **Inspecter votre projet** pour voir ce qui a déjà été fait
- **Vous montrer vos options** en fonction des modules que vous avez installés
- **Recommander la prochaine étape** — y compris la première tâche obligatoire
- **Répondre aux questions** comme « J’ai une idée de SaaS, par où commencer ? »

Exécutez-le dans votre IDE avec IA en invoquant la skill :

Ou combinez-le avec une question pour obtenir des conseils adaptés au contexte :

```plaintext

bmad-help J'ai une idée de produit SaaS, je connais déjà toutes les fonctionnalités que je veux. Par où dois-je commencer ?
```

BMad-Help répondra avec :

- Ce qui est recommandé pour votre situation
- Quelle est la première tâche obligatoire
- À quoi ressemble le reste du processus

### Il alimente aussi les workflows

[Section intitulée « Il alimente aussi les workflows »](#il-alimente-aussi-les-workflows)

BMad-Help ne se contente pas de répondre aux questions — **il s’exécute automatiquement à la fin de chaque workflow** pour vous dire exactement quoi faire ensuite. Pas de devinettes, pas de recherche dans la documentation — juste des conseils clairs sur le prochain workflow requis.

BMad vous aide à construire des logiciels grâce à des workflows guidés avec des agents IA spécialisés. Le processus suit quatre phases :

PhaseNomCe qui se passe1AnalyseBrainstorming, recherche, product brief *(optionnel)*2PlanificationCréer les exigences (PRD[1](#user-content-fn-1) ou spécification technique)3SolutioningConcevoir l’architecture *(BMad Method/Enterprise uniquement)*4ImplémentationConstruire epic[2](#user-content-fn-2) par epic, story[3](#user-content-fn-3) par story

[**Ouvrir la carte des workflows**](https://docs.bmad-method.org/fr/reference/workflow-map/) pour explorer les phases, les workflows et la gestion du contexte.

Selon la complexité de votre projet, BMad propose trois voies de planification :

VoieIdéal pourDocuments créés**Quick Dev**Corrections de bugs, fonctionnalités simples, périmètre clair (1-15 stories)Spécification technique uniquement**méthode BMad**Produits, plateformes, fonctionnalités complexes (10-50+ stories)PRD + Architecture + UX[4](#user-content-fn-4)**Enterprise**Conformité, systèmes multi-tenant[5](#user-content-fn-5) (30+ stories)PRD + Architecture + Security + DevOps

Ouvrez un terminal dans le répertoire de votre projet et exécutez :

Si vous souhaitez la version préliminaire la plus récente au lieu du canal de release par défaut, utilisez `npx bmad-method@next install`.

Lorsque vous êtes invité à sélectionner des modules, choisissez **méthode BMad**.

L’installateur crée deux dossiers :

- `_bmad/` — agents, workflows, tâches et configuration
- `_bmad-output/` — vide pour l’instant, mais c’est là que vos artefacts seront enregistrés

## Étape 1 : Créer votre plan

[Section intitulée « Étape 1 : Créer votre plan »](#%C3%A9tape-1--cr%C3%A9er-votre-plan)

Travaillez à travers les phases 1-3. **Utilisez de nouveaux chats pour chaque workflow.**

### Phase 1 : Analyse (Optionnel)

[Section intitulée « Phase 1 : Analyse (Optionnel) »](#phase-1--analyse-optionnel)

Tous les workflows de cette phase sont optionnels :

- **brainstorming** (`bmad-brainstorming`) — Idéation guidée
- **research** (`bmad-market-research` / `bmad-domain-research` / `bmad-technical-research`) — Recherche marché, domaine et technique
- **create-product-brief** (`bmad-create-product-brief`) — Document de base recommandé

### Phase 2 : Planification (Requis)

[Section intitulée « Phase 2 : Planification (Requis) »](#phase-2--planification-requis)

**Pour les voies BMad Method et Enterprise :**

1. Exécutez `bmad-create-prd` dans un nouveau chat
2. Sortie : `PRD.md`

**Pour la voie Quick Dev :**

- Utilisez le workflow `bmad-quick-dev` (`bmad-quick-dev`) à la place du PRD, puis passez à l’implémentation

### Phase 3 : Solutioning (méthode BMad/Enterprise)

[Section intitulée « Phase 3 : Solutioning (méthode BMad/Enterprise) »](#phase-3--solutioning-m%C3%A9thode-bmadenterprise)

**Créer l’Architecture**

1. Exécutez `bmad-create-architecture` dans un nouveau chat
2. Sortie : Document d’architecture avec les décisions techniques

**Créer les Epics et Stories**

1. Exécutez `bmad-create-epics-and-stories` dans un nouveau chat
2. Le workflow utilise à la fois le PRD et l’Architecture pour créer des stories techniquement éclairées

**Vérification de préparation à l’implémentation** *(Hautement recommandé)*

1. Exécutez `bmad-check-implementation-readiness` dans un nouveau chat
2. Valide la cohérence entre tous les documents de planification

## Étape 2 : Construire votre projet

[Section intitulée « Étape 2 : Construire votre projet »](#%C3%A9tape-2--construire-votre-projet)

Une fois la planification terminée, passez à l’implémentation. **Chaque workflow doit s’exécuter dans un nouveau chat.**

### Initialiser la planification de sprint

[Section intitulée « Initialiser la planification de sprint »](#initialiser-la-planification-de-sprint)

Exécutez `bmad-sprint-planning` dans un nouveau chat. Cela crée `sprint-status.yaml` pour suivre tous les epics et stories.

### Le cycle de construction

[Section intitulée « Le cycle de construction »](#le-cycle-de-construction)

Pour chaque story, répétez ce cycle avec de nouveaux chats :

ÉtapeWorkflowCommandeObjectif1`bmad-create-story``bmad-create-story`Créer le fichier story depuis l’epic2`bmad-dev-story``bmad-dev-story`Implémenter la story3`bmad-code-review``bmad-code-review`Validation de qualité *(recommandé)*

Après avoir terminé toutes les stories d’un epic, exécutez `bmad-retrospective` dans un nouveau chat.

## Ce que vous avez accompli

[Section intitulée « Ce que vous avez accompli »](#ce-que-vous-avez-accompli)

Vous avez appris les fondamentaux de la construction avec BMad :

- Installé BMad et configuré pour votre IDE
- Initialisé un projet avec votre voie de planification choisie
- Créé des documents de planification (PRD, Architecture, Epics & Stories)
- Compris le cycle de construction pour l’implémentation

Votre projet contient maintenant :

```text

your-project/
├── _bmad/                                   # Configuration BMad
├── _bmad-output/
│   ├── planning-artifacts/
│   │   ├── PRD.md                           # Votre document d'exigences
│   │   ├── architecture.md                  # Décisions techniques
│   │   └── epics/                           # Fichiers epic et story
│   ├── implementation-artifacts/
│   │   └── sprint-status.yaml               # Suivi de sprint
│   └── project-context.md                   # Règles d'implémentation (optionnel)
└── ...
```

WorkflowCommandeObjectif**`bmad-help`** ⭐`bmad-help`**Votre guide intelligent — posez n’importe quelle question !**`bmad-create-prd``bmad-create-prd`Créer le document d’exigences produit`bmad-create-architecture``bmad-create-architecture`Créer le document d’architecture`bmad-generate-project-context``bmad-generate-project-context`Créer le fichier de contexte projet`bmad-create-epics-and-stories``bmad-create-epics-and-stories`Décomposer le PRD en epics`bmad-check-implementation-readiness``bmad-check-implementation-readiness`Valider la cohérence de planification`bmad-sprint-planning``bmad-sprint-planning`Initialiser le suivi de sprint`bmad-create-story``bmad-create-story`Créer un fichier story`bmad-dev-story``bmad-dev-story`Implémenter une story`bmad-code-review``bmad-code-review`Revoir le code implémenté

**Ai-je toujours besoin d’une architecture ?** Uniquement pour les voies méthode BMad et Enterprise. Quick Dev passe directement de la spécification technique (spec) à l’implémentation.

**Puis-je modifier mon plan plus tard ?** Oui. Utilisez `bmad-correct-course` pour gérer les changements de périmètre.

**Et si je veux d’abord faire du brainstorming ?** Invoquez l’agent Analyst (`bmad-agent-analyst`) et exécutez `bmad-brainstorming` (`bmad-brainstorming`) avant de commencer votre PRD.

**Dois-je suivre un ordre strict ?** Pas strictement. Une fois que vous maîtrisez le flux, vous pouvez exécuter les workflows directement en utilisant la référence rapide ci-dessus.

- **Pendant les workflows** — Les agents vous guident avec des questions et des explications
- **Communauté** — [Discord](https://discord.gg/gk8jAdXWmj) (#bmad-method-help, #report-bugs-and-issues)

Prêt à commencer ? Installez BMad, invoquez `bmad-help`, et laissez votre guide intelligent vous montrer le chemin.

1. PRD (Product Requirements Document) : document de référence qui décrit les objectifs du produit, les besoins utilisateurs, les fonctionnalités attendues, les contraintes et les critères de succès, afin d’aligner les équipes sur ce qui doit être construit et pourquoi. [↩](#user-content-fnref-1)
2. Epic : grand ensemble de fonctionnalités ou de travaux qui peut être décomposé en plusieurs user stories. [↩](#user-content-fnref-2)
3. Story (User Story) : description courte et simple d’une fonctionnalité du point de vue de l’utilisateur ou du client. Elle représente une unité de travail implémentable en un court délai. [↩](#user-content-fnref-3)
4. UX (User Experience) : expérience utilisateur, englobant l’ensemble des interactions et perceptions d’un utilisateur face à un produit. Le design UX vise à créer des interfaces intuitives, efficaces et agréables en tenant compte des besoins, comportements et contexte d’utilisation. [↩](#user-content-fnref-4)
5. Multi-tenant : architecture logicielle où une seule instance de l’application sert plusieurs clients (tenants) tout en maintenant leurs données isolées et sécurisées les unes des autres. [↩](#user-content-fnref-5)