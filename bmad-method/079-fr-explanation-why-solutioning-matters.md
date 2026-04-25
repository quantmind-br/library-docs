---
title: Pourquoi le Solutioning est Important
url: https://docs.bmad-method.org/fr/explanation/why-solutioning-matters/
source: sitemap
fetched_at: 2026-04-08T11:30:31.545473396-03:00
rendered_js: false
word_count: 473
summary: This document explains the crucial 'Solutioning' phase, which bridges high-level planning ('what') with technical design ('how'). It emphasizes that documenting architectural decisions explicitly prevents integration conflicts and ensures system coherence among different development agents.
tags:
    - solutioning
    - technical-design
    - software-architecture
    - integration-planning
    - development-process
category: guide
---

La Phase 3 (Solutioning) traduit le **quoi** construire (issu de la Planification) en **comment** le construire (conception technique). Cette phase évite les conflits entre agents dans les projets multi-epics en documentant les décisions architecturales avant le début de l’implémentation.

## Le Problème Sans Solutioning

[Section intitulée « Le Problème Sans Solutioning »](#le-probl%C3%A8me-sans-solutioning)

```text

Agent 1 implémente l'Epic 1 avec une API REST
Agent 2 implémente l'Epic 2 avec GraphQL
Résultat : Conception d'API incohérente, cauchemar d'intégration
```

Lorsque plusieurs agents implémentent différentes parties d’un système sans orientation architecturale partagée, ils prennent des décisions techniques indépendantes qui peuvent entrer en conflit.

## La Solution Avec le Solutioning

[Section intitulée « La Solution Avec le Solutioning »](#la-solution-avec-le-solutioning)

```text

le workflow architecture décide : "Utiliser GraphQL pour toutes les API"
Tous les agents suivent les décisions d'architecture
Résultat : Implémentation cohérente, pas de conflits
```

En documentant les décisions techniques de manière explicite, tous les agents implémentent de façon cohérente et l’intégration devient simple.

## Solutioning vs Planification

[Section intitulée « Solutioning vs Planification »](#solutioning-vs-planification)

AspectPlanification (Phase 2)Solutioning (Phase 3)QuestionQuoi et Pourquoi ?Comment ? Puis Quelles unités de travail ?SortieFRs/NFRs (Exigences)[1](#user-content-fn-1)Architecture + Epics[2](#user-content-fn-2)/Stories[3](#user-content-fn-3)AgentPMArchitect → PMAudienceParties prenantesDéveloppeursDocumentPRD[4](#user-content-fn-4) (FRs/NFRs)Architecture + Fichiers EpicsNiveauLogique métierConception technique + Décomposition du travail

**Rendre les décisions techniques explicites et documentées** pour que tous les agents implémentent de manière cohérente.

Cela évite :

- Les conflits de style d’API (REST vs GraphQL)
- Les incohérences de conception de base de données
- Les désaccords sur la gestion du state
- Les inadéquations de conventions de nommage
- Les variations d’approche de sécurité

## Quand le Solutioning est Requis

[Section intitulée « Quand le Solutioning est Requis »](#quand-le-solutioning-est-requis)

ParcoursSolutioning Requis ?Quick DevNon - l’ignore complètementMéthode BMad SimpleOptionnelMéthode BMad ComplexeOuiEnterpriseOui

## Conséquences de sauter la phase de Solutioning

[Section intitulée « Conséquences de sauter la phase de Solutioning »](#cons%C3%A9quences-de-sauter-la-phase-de-solutioning)

Sauter le solutioning sur des projets complexes entraîne :

- **Des problèmes d’intégration** découverts en milieu de sprint[5](#user-content-fn-5)
- **Du travail répété** dû à des implémentations conflictuelles
- **Un temps de développement plus long** globalement
- **De la dette technique**[6](#user-content-fn-6) due à des patterns incohérents

<!--THE END-->

1. FR / NFR (Functional / Non-Functional Requirement) : exigences décrivant respectivement **ce que le système doit faire** (fonctionnalités, comportements attendus) et **comment il doit le faire** (contraintes de performance, sécurité, fiabilité, ergonomie, etc.). [↩](#user-content-fnref-1)
2. Epic : dans les méthodologies agiles, une unité de travail importante qui peut être décomposée en plusieurs stories plus petites. Un epic représente généralement une fonctionnalité majeure ou un objectif métier. [↩](#user-content-fnref-2)
3. Story (User Story) : description courte et simple d’une fonctionnalité du point de vue de l’utilisateur, utilisée dans les méthodologies agiles pour planifier et prioriser le travail. [↩](#user-content-fnref-3)
4. PRD (Product Requirements Document) : document de référence qui décrit les objectifs du produit, les besoins utilisateurs, les fonctionnalités attendues, les contraintes et les critères de succès, afin d’aligner les équipes sur ce qui doit être construit et pourquoi. [↩](#user-content-fnref-4)
5. Sprint : période de temps fixe (généralement 1 à 4 semaines) dans les méthodologies agiles durant laquelle l’équipe complète un ensemble prédéfini de tâches. [↩](#user-content-fnref-5)
6. Dette technique : coût futur supplémentaire de travail résultant de choix de facilité ou de raccourcis pris lors du développement initial, nécessitant souvent une refonte ultérieure. [↩](#user-content-fnref-6)