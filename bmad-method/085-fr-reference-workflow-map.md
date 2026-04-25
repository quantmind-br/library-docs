---
title: Carte des Workflows
url: https://docs.bmad-method.org/fr/reference/workflow-map/
source: sitemap
fetched_at: 2026-04-08T11:31:01.789569414-03:00
rendered_js: false
word_count: 669
summary: 'This document details the BMad method, a comprehensive framework designed to guide AI agents through software development by systematically building and maintaining a clear context across distinct phases: Analysis, Planning, and Implementation. It outlines specific workflows for various stages, from brainstorming initial ideas to developing final code.'
tags:
    - bmad-method
    - ai-agent-workflow
    - software-development
    - context-engineering
    - product-planning
    - tech-guide
category: guide
---

La méthode BMad (BMM) est un module de l’écosystème BMad, conçu pour suivre les meilleures pratiques de l’ingénierie du contexte et de la planification. Les agents IA fonctionnent de manière optimale avec un contexte clair et structuré. Le système BMM construit ce contexte progressivement à travers 4 phases distinctes — chaque phase, et plusieurs workflows optionnels au sein de chaque phase, produisent des documents qui alimentent la phase suivante, afin que les agents sachent toujours quoi construire et pourquoi.

La logique et les concepts proviennent des méthodologies agiles qui ont été utilisées avec succès dans l’industrie comme cadre mental de référence.

Si à tout moment vous ne savez pas quoi faire, le skill `bmad-help` vous aidera à rester sur la bonne voie ou à savoir quoi faire ensuite. Vous pouvez toujours vous référer à cette page également — mais `bmad-help` est entièrement interactif et beaucoup plus rapide si vous avez déjà installé la méthode BMad. De plus, si vous utilisez différents modules qui ont étendu la méthode BMad ou ajouté d’autres modules complémentaires non extensifs — `bmad-help` évolue pour connaître tout ce qui est disponible et vous donner les meilleurs conseils du moment.

Note finale importante : Chaque workflow ci-dessous peut être exécuté directement avec l’outil de votre choix via un skill ou en chargeant d’abord un agent et en utilisant l’entrée du menu des agents.

[Ouvrir le diagramme dans un nouvel onglet ↗](https://docs.bmad-method.org/workflow-map-diagram-fr.html)

## Phase 1 : Analyse (Optionnelle)

[Section intitulée « Phase 1 : Analyse (Optionnelle) »](#phase-1--analyse-optionnelle)

Explorez l’espace problème et validez les idées avant de vous engager dans la planification.

WorkflowObjectifProduit`bmad-brainstorming`Brainstormez des idées de projet avec l’accompagnement guidé d’un coach de brainstorming`brainstorming-report.md``bmad-domain-research`, `bmad-market-research`, `bmad-technical-research`Validez les hypothèses de marché, techniques ou de domaineRapport de recherches`bmad-create-product-brief`Capturez la vision stratégique`product-brief.md`

## Phase 2 : Planification

[Section intitulée « Phase 2 : Planification »](#phase-2--planification)

Définissez ce qu’il faut construire et pour qui.

WorkflowObjectifProduit`bmad-create-prd`Définissez les exigences (FRs/NFRs)[1](#user-content-fn-1)`PRD.md`[2](#user-content-fn-2)`bmad-create-ux-design`Concevez l’expérience utilisateur (lorsque l’UX compte)`ux-spec.md`

Décidez comment le construire et décomposez le travail en stories.

WorkflowObjectifProduit`bmad-create-architecture`Rendez les décisions techniques explicites`architecture.md` avec ADRs[3](#user-content-fn-3)`bmad-create-epics-and-stories`Décomposez les exigences en travail implémentableFichiers d’epic avec stories`bmad-check-implementation-readiness`Vérification avant implémentationDécision Passe/Réserves/Échec

## Phase 4 : Implémentation

[Section intitulée « Phase 4 : Implémentation »](#phase-4--impl%C3%A9mentation)

Construisez, une story à la fois. Bientôt disponible : automatisation complète de la phase 4 !

WorkflowObjectifProduit`bmad-sprint-planning`Initialisez le suivi (une fois par projet pour séquencer le cycle de développement)`sprint-status.yaml``bmad-create-story`Préparez la story suivante pour implémentation`story-[slug].md``bmad-dev-story`Implémentez la storyCode fonctionnel + tests`bmad-code-review`Validez la qualité de l’implémentationApprouvé ou changements demandés`bmad-correct-course`Gérez les changements significatifs en cours de sprintPlan mis à jour ou réorientation`bmad-sprint-status`Suivez la progression du sprint et le statut des storiesMise à jour du statut du sprint`bmad-retrospective`Revue après complétion d’un epicLeçons apprises

## Quick Dev (Parcours Parallèle)

[Section intitulée « Quick Dev (Parcours Parallèle) »](#quick-dev-parcours-parall%C3%A8le)

Sautez les phases 1-3 pour les travaux de faible envergure et bien compris.

WorkflowObjectifProduit`bmad-quick-dev`Flux rapide unifié — clarifie l’intention, planifie, implémente, révise et présente`spec-*.md` + code

Chaque document devient le contexte de la phase suivante. Le PRD[2](#user-content-fn-2) indique à l’architecte quelles contraintes sont importantes. L’architecture indique à l’agent de développement quels modèles suivre. Les fichiers de story fournissent un contexte focalisé et complet pour l’implémentation. Sans cette structure, les agents prennent des décisions incohérentes.

**Comment le créer :**

- **Manuellement** — Créez `_bmad-output/project-context.md` avec votre pile technologique et vos règles d’implémentation
- **Générez-le** — Exécutez `bmad-generate-project-context` pour l’auto-générer à partir de votre architecture ou de votre codebase

[**En savoir plus sur project-context.md**](https://docs.bmad-method.org/fr/explanation/project-context/)

1. FR / NFR (Functional / Non-Functional Requirement) : exigences décrivant respectivement **ce que le système doit faire** (fonctionnalités, comportements attendus) et **comment il doit le faire** (contraintes de performance, sécurité, fiabilité, ergonomie, etc.). [↩](#user-content-fnref-1)
2. PRD (Product Requirements Document) : document de référence qui décrit les objectifs du produit, les besoins utilisateurs, les fonctionnalités attendues, les contraintes et les critères de succès, afin d’aligner les équipes sur ce qui doit être construit et pourquoi. [↩](#user-content-fnref-2) [↩2](#user-content-fnref-2-2)
3. ADR (Architecture Decision Record) : document qui consigne une décision d’architecture, son contexte, les options envisagées, le choix retenu et ses conséquences, afin d’assurer la traçabilité et la compréhension des décisions techniques dans le temps. [↩](#user-content-fnref-3)